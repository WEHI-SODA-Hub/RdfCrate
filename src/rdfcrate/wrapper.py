from __future__ import annotations

import mimetypes
import warnings
from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from os import stat
from pathlib import Path
from typing import TYPE_CHECKING, Annotated, Any
from urllib.parse import quote

from rdflib import DCTERMS, RDF, IdentifiedNode, Literal, Namespace, URIRef
from rdflib.plugins.shared.jsonld.context import Context
from typing_extensions import Doc, Unpack

from rdfcrate.context_builder import ContextBuilder
from rdfcrate.context_graph import ContextGraph, ContextGraphKwargs, PropertyArg
from rdfcrate.spec_version import ROCrate1_1, SpecVersion
from rdfcrate.types import Object, Predicate

if TYPE_CHECKING:
    from rocrate_validator.models import CheckIssue, Severity

#: Schema.org namespace as used by RO-Crate.
#: Note that this is different from `rdflib.SDO`, which uses `https://schema.org/`.
SCHEMA = Namespace("http://schema.org/")

Recursive = Annotated[
    bool,
    Doc(
        "If true, register all files and subdirectories in the directory.  The child entities will only have minimal metadata, but more can be added later with [`ContextGraph.add_entity`][rdfcrate.context_graph.ContextGraph.add_entity].  Also note that each registered data entity will be linked to the directory entity with `hasPart`."
    ),
]


def has_predicate(props: Iterable[PropertyArg], predicate: Predicate) -> bool:
    """
    Checks if a property list contains a specific predicate
    """
    return any(prop_predicate == predicate for prop_predicate, _ in props)


def as_literal(value: Object | str | date) -> Object:
    """
    Converts plain Python values to plain string literals, leaving RDF terms unchanged.
    Dates are converted to ISO 8601 strings, as required by RO-Crate.
    """
    if isinstance(value, date):
        return Literal(value.isoformat())
    if isinstance(value, str) and not isinstance(value, IdentifiedNode | Literal):
        return Literal(value)
    return value


class RoCrateKwargs(ContextGraphKwargs, total=False):
    version: SpecVersion


class RoCrate(ContextGraph, metaclass=ABCMeta):
    """
    Abstract class containing common functionality for both attached and detached RO-Crates
    """

    version: SpecVersion
    "Version of the RO-Crate specification to use"

    def __init__(self, **kwargs: Unpack[RoCrateKwargs]):
        super().__init__(**kwargs)
        self.version = kwargs.get("version", ROCrate1_1)

        # We resolve the RO-Crate context now so we can use it to resolve terms and check if they are already defined
        self._roc_context = Context(self.version.context_url)

    def context_builder(self) -> ContextBuilder:
        # Terms in the RO-Crate context are already defined, so they mustn't be added or redefined
        return ContextBuilder(external=self._roc_context)

    @property
    def context_source(self) -> list[dict[str, Any] | str | None] | str:
        # Implements the requirements for context format according to the RO-Crate spec
        custom_terms = self.vocab_context()
        if len(custom_terms) == 0:
            return self.version.context_url
        else:
            return [self.version.context_url, custom_terms]

    @property
    @abstractmethod
    def root_data_entity(self) -> URIRef:
        """
        The root entity of the RO-Crate
        """

    def add_root_entity(
        self,
        name: Object | str,
        description: Object | str,
        date_published: Object | str | date,
        license: Object | str,
        *props: PropertyArg,
    ) -> URIRef:
        """
        Adds the root entity to the crate.

        Params:
            name: Name of the crate. Strings are converted to literals.
            description: Description of the crate. Strings are converted to literals.
            date_published: Publication date of the crate. Dates are converted to ISO 8601 strings.
            license: License of the crate. This should ideally be a `URIRef` of a license entity.
        """
        self.add_entity(
            self.root_data_entity,
            (RDF.type, SCHEMA.Dataset),
            *self._root_props(name, description, date_published, license),
            *props,
        )
        return self.root_data_entity

    def _root_props(
        self,
        name: Object | str,
        description: Object | str,
        date_published: Object | str | date,
        license: Object | str,
    ) -> list[PropertyArg]:
        return [
            (SCHEMA.name, as_literal(name)),
            (SCHEMA.description, as_literal(description)),
            (SCHEMA.datePublished, as_literal(date_published)),
            (SCHEMA.license, as_literal(license)),
        ]

    @property
    @abstractmethod
    def metadata_entity(self) -> URIRef:
        """
        The metadata entity of the RO-Crate
        """

    def add_metadata_entity(self, *props: PropertyArg) -> None:
        """
        Creates the `ro-crate-metadata.json` record.
        """
        self.add_entity(
            self.metadata_entity,
            (RDF.type, SCHEMA.CreativeWork),
            (SCHEMA.about, self.root_data_entity),
            (DCTERMS.conformsTo, self.version.conforms_to_url),
            *props,
        )

    def link_to_dataset(
        self,
        entity: IdentifiedNode,
        dataset: IdentifiedNode | None,
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
        self.add_entity(dataset, (SCHEMA.hasPart, entity))

    def register_file(
        self,
        path: str,
        *props: PropertyArg,
        guess_mime: bool = True,
        dataset: IdentifiedNode | None = None,
        **kwargs,
    ) -> URIRef:
        """
        Adds file metadata to the crate

        Returns: The ID of the new file entity

        Params:
            path: Path or URL to the file being added
            guess_mime: If true, automatically guess and document the MIME type of the file based on its extension
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.

        Example:
            ```python
            from rdflib import Literal
            from rdfcrate import AttachedCrate
            from rdfcrate.wrapper import SCHEMA

            AttachedCrate(".").register_file("./some/data.txt", (SCHEMA.description, Literal("This is a file with some data")))
            ```
        """
        file_id = URIRef(path)
        self.add_entity(file_id, (RDF.type, SCHEMA.MediaObject), *props)

        if guess_mime:
            if has_predicate(props, SCHEMA.encodingFormat):
                raise ValueError(
                    "Cannot guess MIME type when encodingFormat is provided"
                )
            guess_type, _guess_encoding = mimetypes.guess_type(path)
            if guess_type is not None:
                self.add_entity(file_id, (SCHEMA.encodingFormat, Literal(guess_type)))

        self.link_to_dataset(file_id, dataset)

        return file_id

    def register_dir(
        self,
        path: str,
        *props: PropertyArg,
        dataset: IdentifiedNode | None = None,
        **kwargs,
    ) -> URIRef:
        """
        Adds metadata for a directory

        Returns:
            The ID of the new directory entity

        Params:
            path: Path to the directory, which must be within the crate root
            props: Properties used to describe the `Dataset` entity
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.
            kwargs: Available for subclasses to extend the functionality.

        Example:
            ```python
            from rdflib import Literal
            from rdfcrate import AttachedCrate
            from rdfcrate.wrapper import SCHEMA

            AttachedCrate(".").register_dir("./some/dir", (SCHEMA.description, Literal("This is a directory I am describing")))
            ```
        """
        if not path.endswith("/"):
            # Directories must end with a slash in RO-Crate
            path += "/"
        dir_id = URIRef(path)
        self.add_entity(dir_id, (RDF.type, SCHEMA.Dataset), *props)
        if self.root_data_entity != dir_id:
            # The root dataset is not linked to itself
            self.link_to_dataset(dir_id, dataset)
        return dir_id

    def compile(self, **kwargs) -> str:
        """
        Compiles the RO-Crate to a JSON-LD string
        """
        if self.root_data_entity not in self.graph.subjects():
            raise ValueError(
                "Root data entity not found. Did you call `add_root_entity`?"
            )

        return super().compile(**kwargs)


class AttachedCrate(RoCrate):
    """
    An RO-Crate stored in a directory, with all contents local to that directory.

    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#attached-ro-crate>
    """

    root: Path
    "The RO-Crate directory"

    def __init__(self, path: str | Path, **kwargs: Unpack[RoCrateKwargs]):
        super().__init__(**kwargs)
        self.root = Path(path).resolve()

    @property
    def metadata_entity(self) -> URIRef:
        """
        The metadata entity of the RO-Crate
        """
        return self._resolve_path(self._metadata_path, existing=False)[1]

    @property
    def root_data_entity(self) -> URIRef:
        return URIRef("./")

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
        *props: PropertyArg,
        add_size: bool = False,
        **kwargs: Any,
    ) -> URIRef:
        """
        See [`RoCrate.register_file`][rdfcrate.wrapper.RoCrate.register_file].

        Params:
            add_size: If true, automatically add the size of the file to the metadata
        """
        path = Path(path)
        _, file_id = self._resolve_path(path)
        ret = super().register_file(file_id, *props, **kwargs)
        if add_size:
            if has_predicate(props, SCHEMA.contentSize):
                raise ValueError("Cannot add size when contentSize is provided")
            self.add_entity(ret, (SCHEMA.contentSize, Literal(str(stat(path).st_size))))
        return ret

    def add_root_entity(
        self,
        name: Object | str,
        description: Object | str,
        date_published: Object | str | date,
        license: Object | str,
        *props: PropertyArg,
        recursive: Recursive = False,
    ) -> URIRef:
        return self.register_dir(
            ".",
            *self._root_props(name, description, date_published, license),
            *props,
            recursive=recursive,
        )

    def register_dir(
        self,
        path: Path | str,
        *props: PropertyArg,
        recursive: Recursive = False,
        **kwargs: Any,
    ) -> URIRef:
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
            from rocrate_validator import models, services
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
    def root_data_entity(self) -> URIRef:
        return URIRef(self.root)
