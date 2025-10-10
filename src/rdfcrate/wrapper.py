from __future__ import annotations
from pathlib import Path
from typing import Annotated, Any, Iterable, TypeVar, TYPE_CHECKING
from deprecated import deprecated
from typing_extensions import Doc, Unpack
from rdflib import URIRef
from rdfcrate.context_graph import ContextGraph, EntityArgs, ContextGraphKwargs
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdftype import RdfClass
from rdfcrate.spec_version import SpecVersion, ROCrate1_1
from dataclasses import dataclass
import mimetypes
from os import stat
from abc import ABCMeta, abstractmethod
from rdflib.plugins.shared.jsonld.context import Context
from rdfcrate.vocabs import dc, schemaorg, rocrate
from urllib.parse import quote
import warnings

if TYPE_CHECKING:
    from rocrate_validator.models import Severity, CheckIssue

EntityType = Annotated[
    type[RdfClass],
    Doc(
        "The main type of the entity to create. An entity can have multiple types, which you can specify using `rdf.type()`. However for static type checking, you should choose a main type that agrees with the property (predicate) that it will be linked to."
    ),
]
Recursive = Annotated[
    bool,
    Doc(
        "If true, register all files and subdirectories in the directory.  The child entities will only have minimal metadata, but more can be added later with [`RoCrate.add_metadata`][rdfcrate.wrapper.RoCrate.add_metadata].  Also note that each registered data entity will be linked to the directory entity with `hasPart`."
    ),
]
EntityClass = TypeVar("EntityClass", bound=RdfClass)


def has_prop(props: Iterable[EntityArgs], predicate: type[RdfProperty]) -> bool:
    """
    Checks if an attribute list contains a specific predicate
    """
    return any(isinstance(prop, predicate) for prop in props)


class RoCrateKwargs(ContextGraphKwargs, total=False):
    version: SpecVersion


class RoCrate(ContextGraph, metaclass=ABCMeta):
    """
    Abstract class containing common functionality for both attached and detached RO-Crates
    """

    version: SpecVersion
    "Version of the RO-Crate specification to use"
    _custom_terms: dict[str, Any]

    def __init__(self, **kwargs: Unpack[RoCrateKwargs]):
        super().__init__(**kwargs)
        self.version = kwargs.get("version", ROCrate1_1)

        # We resolve the RO-Crate context now so we can use it to resolve terms and check if they are already registered
        self._roc_context = Context(self.version.context_url)

    @property
    def context_source(self):
        # Implements the requirements for context format according to the RO-Crate spec
        if len(self._custom_terms) == 0:
            return self.version.context_url
        else:
            return [self.version.context_url, self._custom_terms]

    @property
    @abstractmethod
    def root_data_entity(self) -> schemaorg.Dataset:
        """
        The root entity of the RO-Crate
        """

    @deprecated("This is deprecated in favour of `.add(RootDataEntity(...))`")
    def add_root_entity(
        self,
        name: schemaorg.name,
        description: schemaorg.description,
        date_published: schemaorg.datePublished,
        license: schemaorg.license,
        *props: EntityArgs,
    ) -> schemaorg.Dataset:
        """
        Adds the root entity to the crate.
        """
        return self.add_entity(
            self.root_data_entity,
            name,
            description,
            date_published,
            license,
            *props,
        )

    @property
    @abstractmethod
    def metadata_entity(self) -> schemaorg.CreativeWork:
        """
        The metadata entity of the RO-Crate
        """

    @deprecated("This is deprecated in favour of `.add(MetadataEntity(...))`")
    def add_metadata_entity(self, *props: EntityArgs) -> None:
        """
        Creates the `ro-crate-metadata.json` record.
        """
        self.add_entity(
            self.metadata_entity,
            schemaorg.about(self.root_data_entity),
            dc.conformsTo(dc.Standard(self.version.conforms_to_url)),
            *props,
        )

    def link_to_dataset(
        self,
        entity: schemaorg.Dataset | rocrate.File,
        dataset: schemaorg.Dataset | None,
    ) -> None:
        """
        Links a data entity to a Dataset.

        See https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/data-entities.html#referencing-files-and-folders-from-the-root-data-entity

        Params:
            entity: ID of the entity being linked
            dataset: ID of the dataset being linked to. If not provided, the entity will be linked to the root dataset.
        """
        if dataset is None:
            dataset = self.root_data_entity
        self.add_metadata(dataset, schemaorg.hasPart(entity))

    @deprecated("This is deprecated in favour of `.add(FileEntity(...))`")
    def register_file(
        self,
        path: str,
        *args: EntityArgs,
        guess_mime: bool = True,
        dataset: schemaorg.Dataset | None = None,
        **kwargs,
    ) -> rocrate.File:
        """
        Adds file metadata to the crate

        Returns: The ID of the new file entity

        Params:
            path: Path or URL to the file being added
            guess_mime: If true, automatically guess and document the MIME type of the file based on its extension
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.

        Example:
            ```python
            from rdfcrate import AttachedCrate
            from rdfcrate.vocabs import schemaorg as sdo

            AttachedCrate(".").register_file("./some/data.txt", sdo.description(sdo.Text("This is a file with some data")))
            ```
        """
        file_id = rocrate.File(path)
        self.add_entity(file_id, *args)

        if guess_mime:
            if any(isinstance(arg, schemaorg.encodingFormat) for arg in args):
                raise ValueError(
                    "Cannot guess MIME type when encodingFormat is provided"
                )
            guess_type, _guess_encoding = mimetypes.guess_type(path)
            if guess_type is not None:
                self.add_metadata(
                    file_id, schemaorg.encodingFormat(schemaorg.Text(guess_type))
                )

        self.link_to_dataset(file_id, dataset)

        return file_id

    @deprecated("This is deprecated in favour of `.add(DirEntity(...))`")
    def register_dir(
        self,
        path: str,
        *props: EntityArgs,
        dataset: schemaorg.Dataset | None = None,
        **kwargs,
    ) -> schemaorg.Dataset:
        """
        Adds metadata for a directory

        Returns:
            The ID of the new directory entity

        Params:
            path: Path to the directory, which must be within the crate root
            attrs: Attributes used to describe the `Dataset` entity
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.
            kwargs: Available for subclasses to extend the functionality.

        Example:
            ```python
            from rdfcrate import AttachedCrate
            from rdfcrate.vocabs import schemaorg as sdo

            AttachedCrate(".").register_dir("./some/dir", sdo.description(sdo.Text("This is a directory I am describing")))
            ```
        """
        if not path.endswith("/"):
            # Directories must end with a slash in RO-Crate
            path += "/"
        dir_id = schemaorg.Dataset(path)
        self.add_entity(dir_id, *props)
        if self.root_data_entity != dir_id:
            # The root dataset is not linked to itself
            self.link_to_dataset(dir_id, dataset)
        return dir_id

    def compile(self, **kwargs) -> str:
        """
        Compiles the RO-Crate to a JSON-LD string
        """
        if self.root_data_entity.id not in self.graph.subjects():
            raise ValueError(
                "Root data entity not found. Did you call `add_root_entity`?"
            )

        return super().compile(**kwargs)


class AttachedCrate(RoCrate):
    """
    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#attached-ro-crate>
    """

    root: Path
    "The RO-Crate directory"

    def __init__(self, path: str | Path, **kwargs: Unpack[RoCrateKwargs]):
        super().__init__(**kwargs)
        self.root = Path(path).resolve()

    @property
    def metadata_entity(self) -> schemaorg.CreativeWork:
        """
        The metadata entity of the RO-Crate
        """
        return schemaorg.CreativeWork(
            self._resolve_path(self._metadata_path, existing=False)[1]
        )

    @property
    def root_data_entity(self) -> schemaorg.Dataset:
        return schemaorg.Dataset("./")

    @property
    def _metadata_path(self) -> Path:
        """
        Path to the RO-Crate metadata file
        """
        return self.root / "ro-crate-metadata.json"

    def write(self):
        """
        Writes the RO-Crate to `ro-crate-metadata.json`
        """
        self._metadata_path.write_text(self.compile())

    def _resolve_path(
        self, path: Path | str, existing: bool = True
    ) -> tuple[Path, URIRef]:
        """
        Converts a crate path to a platform independent path compatible with RO-Crate

        Params:
            existing: If true, the path must exist, and an exception will be raised if it does not

        Returns:
            A tuple of:
                - The absolute path
                - The path as a URI, suitable for us as an IRI
        """
        if isinstance(path, str):
            # Paths can be provided as strings
            path = Path(path)

        if path.is_absolute():
            # Absolute paths are accepted, but must be within the crate root
            if not path.is_relative_to(self.root):
                raise ValueError(
                    f"Path ({path}) must be within the crate root ({self.root})"
                )
        else:
            # Relative paths are assumed to be relative to the crate root
            path = self.root / path

        if existing and not path.exists():
            raise ValueError(f"Path {path} does not exist")

        return path.resolve(), URIRef(quote(path.relative_to(self.root).as_posix()))

    def register_file(
        self,
        path: Path | str,
        *props: EntityArgs,
        add_size: bool = False,
        **kwargs: Any,
    ):
        """
        See [`RoCrate.register_file`][rdfcrate.wrapper.RoCrate.register_file].

        Params:
            add_size: If true, automatically add the size of the file to the metadata
        """
        path = Path(path)
        _, file_id = self._resolve_path(path)
        ret = super().register_file(file_id, *props, **kwargs)
        if add_size:
            if has_prop([*props], schemaorg.contentSize):
                raise ValueError("Cannot add size when contentSize is provided")
            self.add_metadata(
                ret,
                schemaorg.contentSize(schemaorg.Text(stat(path).st_size)),
            )
        return ret

    def add_root_entity(
        self,
        name: schemaorg.name,
        description: schemaorg.description,
        date_published: schemaorg.datePublished,
        license: schemaorg.license,
        *props: EntityArgs,
        recursive: Recursive = False,
    ) -> schemaorg.Dataset:
        return self.register_dir(
            ".", name, description, date_published, license, *props, recursive=recursive
        )

    def register_dir(
        self,
        path: Path | str,
        *props: EntityArgs,
        recursive: Recursive = False,
        **kwargs: Any,
    ) -> schemaorg.Dataset:
        """
        See [`RoCrate.register_dir`][rdfcrate.wrapper.RoCrate.register_dir].
        """
        full_path, id = self._resolve_path(path)
        id = super().register_dir(id, *props, **kwargs)

        if recursive:
            for child in full_path.iterdir():
                if child in {self._metadata_path, self.root}:
                    # Never register the metadata file or the root directory
                    continue
                if child.is_dir():
                    self.register_dir(child, recursive=True, dataset=id)
                else:
                    self.register_file(child, dataset=id)
        return id

    def get_issues(self) -> list[CheckIssue]:
        """
        Returns a list of issues found in the RO-Crate using the `rocrate-validator` package.
        """
        try:
            from rocrate_validator import services, models
            from rocrate_validator.utils import URI
        except ImportError:
            raise ImportError(
                "rocrate-validator is not installed. Please use the `validation` extra, e.g. `pip install rdfcrate[validation]`."
            )

        self.write()
        result = services.validate(
            services.ValidationSettings(
                rocrate_uri=URI(self.root),
                # TODO: Support other profiles
                profile_identifier="ro-crate-1.1",
                requirement_severity=models.Severity.RECOMMENDED,
            )
        )
        return result.get_issues()

    def validate(self, threshold: Severity | None = None) -> None:
        """
        Raises an exception if the RO-Crate is not valid.
        """
        if threshold is None:
            from rocrate_validator.models import Severity

            threshold = Severity.RECOMMENDED
        for issue in self.get_issues():
            msg = f'Detected issue of severity {issue.severity.name} with check "{issue.check.identifier}": {issue.message}'
            if issue.severity >= threshold:
                raise Exception(msg)
            else:
                warnings.warn(msg)


@dataclass
class DetatchedCrate(RoCrate):
    """
    A crate describing remote files.

    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#detached-ro-crate>
    """

    root: str

    @property
    def root_data_entity(self):
        return schemaorg.Dataset(self.root)
