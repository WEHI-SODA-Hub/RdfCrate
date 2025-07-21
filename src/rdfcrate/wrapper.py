from __future__ import annotations
from pathlib import Path
from typing import Annotated, Any, Iterable, TypeVar, TYPE_CHECKING
from rocrate_validator.models import CheckIssue
from typing_extensions import Doc
from rdflib import RDF, Graph, URIRef
from rdfcrate.vocabs import rdf
from rdfcrate.rdfprop import RdfProperty, ReverseProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfClass, EntityArgs
from rdfcrate.spec_version import SpecVersion, ROCrate1_1
from dataclasses import InitVar, dataclass, field
import mimetypes
from os import stat
from abc import ABCMeta, abstractmethod
from rdflib.plugins.shared.jsonld.context import Context
from rdfcrate.vocabs import dc, schemaorg, rocrate
from urllib.parse import quote
import warnings

if TYPE_CHECKING:
    from rocrate_validator.models import Severity

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


@dataclass
class RoCrate(metaclass=ABCMeta):
    """
    Abstract class containing common functionality for both attached and detached RO-Crates
    """

    graph: Graph = field(init=False, default_factory=Graph)
    "`rdflib.Graph` containing the RO-Crate metadata. This can be accessed directly, but it is recommended to use the other methods provided by this class where available."
    custom_terms: dict[str, str] = field(init=False, default_factory=dict)
    "Set of custom terms not in the standard RO-Crate context that need to be in the final JSON-LD context."
    context: Context = field(init=False)
    "Dynamically updated version of the JSON-LD context. By default, this contains the current RO-Crate spec's context, but additional terms are added as they are added to the graph."
    version: SpecVersion = field(kw_only=True, default=ROCrate1_1)
    "Version of the RO-Crate specification to use"

    def __post_init__(self):
        self.context = Context(self.version.context_url)

    @property
    @abstractmethod
    def root_data_entity(self) -> schemaorg.Dataset:
        """
        The root entity of the RO-Crate
        """

    def register_terms(self, terms: Iterable[RdfTerm]) -> None:
        """
        Adds custom terms to the crate context
        """
        for term in terms:
            existing = self.context.expand(term.label)
            if existing == str(term.uri):
                # Skip terms that are already in the RO-Crate context
                continue
            if existing is not None:
                raise ValueError(
                    f'Term "{term.label}" is already defined to mean {existing}. Cannot redefine to {term.uri}.'
                )

            if term.uri == RDF.type:
                # rdf:type should never be re-defined
                continue

            # The context keeps track of all terms, including the base RO-Crate terms.
            self.context.add_term(term.label, str(term.uri))
            # Custom terms only tracks the non-standard terms
            self.custom_terms[term.label] = str(term.uri)

    def add_entity(self, entity: EntityClass, *args: EntityArgs) -> EntityClass:
        """
        Adds any type of entity to the crate

        Returns:
            The ID of the new entity

        Example:
            ```python
            from rdflib import BNode,
            from rdfcrate.vocabs import schemaorg

            crate.add_entity(
                BNode(),
                schemaorg.Person,
                schemaorg.name("Alice")
            )
            ```
        """

        self.register_terms(
            # Register property terms
            [prop.term for prop in args]
            +
            # Register class terms
            [entity.term]
            # Register supplementary class terms
            + [
                prop.object.term
                for prop in args
                # rdf:type is a special case. All other objects do not need to be registered
                # since they are allowed to be full IRIs
                if isinstance(prop, RdfProperty) and isinstance(prop, rdf.type)
            ]
        )
        entity.add(self.graph, *args)
        return entity

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

    def add_metadata(self, entity: RdfClass, *args: EntityArgs) -> None:
        """
        Add metadata for an existing entity.

        Returns:
            The ID of the updated entity

        Params:
            uri: ID of the entity being described
        """
        self.register_terms(
            # Register property terms
            [prop.term for prop in args]
            + 
            # Register supplementary class terms
            [
                prop.object.term
                for prop in args
                if isinstance(prop, RdfProperty) and isinstance(prop, rdf.type)
            ]
        )
        for arg in args:
            arg.add_to_graph(self.graph, entity.id)

    def compile(self) -> str:
        """
        Compiles the RO-Crate to a JSON-LD string
        """
        if self.root_data_entity.id not in self.graph.subjects():
            raise ValueError(
                "Root data entity not found. Did you call `add_root_entity`?"
            )

        if len(self.custom_terms) == 0:
            context = self.version.context_url
        else:
            context = [self.version.context_url, self.custom_terms]

        # Serializer kwargs are annoyingly not listed in the docs.
        # See them here: https://github.com/RDFLib/rdflib/blob/d220ee3bcba10a7af6630c4faaa37ca9cee33554/rdflib/plugins/serializers/jsonld.py#L76-L84
        return self.graph.serialize(format="json-ld", context=context)


@dataclass
class AttachedCrate(RoCrate):
    """
    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#attached-ro-crate>
    """

    path: InitVar[str | Path]
    "The RO-Crate directory"
    root: Path = field(init=False)
    "The RO-Crate directory"

    def __post_init__(self, path: str | Path):
        self.root = Path(path).resolve()
        super().__post_init__()

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
        *props: RdfProperty | ReverseProperty,
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
