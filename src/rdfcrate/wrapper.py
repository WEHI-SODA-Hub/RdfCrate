from pathlib import Path
from typing import Annotated, Any, Iterable
from typing_extensions import Doc
from rdflib import Graph, URIRef, Literal, RDF, IdentifiedNode
from rdfcrate import uris
from rdfcrate.rdfprop import RdfProperty, ReverseProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdfclass import RdfClass, EntityArgs, EntityUri
from rdfcrate.spec_version import SpecVersion, ROCrate1_1
from dataclasses import InitVar, dataclass, field
import mimetypes
from os import stat
from datetime import datetime
# from rdfcrate.context import Context
from abc import ABCMeta, abstractmethod
from rdflib.plugins.shared.jsonld.context import Context
from rdfcrate.vocabs import schemaorg

#: Predicate-object tuple
Double = tuple[URIRef, Literal | IdentifiedNode]
Attributes = Iterable[Double]
Type = Iterable[URIRef]
type EntityType = Annotated[type[RdfClass], Doc("The main type of the entity to create. An entity can have multiple types, which you can specify using `rdf.type()`. However for static type checking, you should choose a main type that agrees with the property (predicate) that it will be linked to.")]


def has_predicate(double: Iterable[Double], predicate: URIRef) -> bool:
    """
    Checks if an attribute list contains a specific predicate
    """
    return any(pred == predicate for pred, _ in double)


@dataclass
class RoCrate(metaclass=ABCMeta):
    """
    Abstract class containing common functionality for both attached and detached RO-Crates
    """
    graph: Graph = field(init=False, default_factory=Graph)
    "`rdflib.Graph` containing the RO-Crate metadata. This can be accessed directly, but it is recommended to use the other methods provided by this class where available."
    context: Context = field(init=False, default_factory=Context)
    "Collection of custom terms used in the RO-Crate. This is used to generate the JSON-LD context when serializing the crate."
    version: SpecVersion = field(kw_only=True, default=ROCrate1_1)
    "Version of the RO-Crate specification to use"

    @property
    @abstractmethod
    def root_data_entity(self) -> schemaorg.Dataset:
        """
        The root entity of the RO-Crate
        """
        pass

    def _register_terms(self, terms: Iterable[RdfTerm]) -> None:
        """
        Adds custom terms to the crate context
        """
        for term in terms:
            if self.version.version not in term.specs:
                # Skip terms that are already in the RO-Crate context
                self.context.add_term(
                    term.label,
                    term.uri
                )

    def add_entity(
        self,
        iri: EntityUri,
        type: EntityType,
        *args: RdfProperty | ReverseProperty
    ) -> IdentifiedNode:
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
        self._register_terms([arg.term for arg in args])
        return type(self.graph, iri, *args)

    def link_to_dataset(
        self, entity: schemaorg.Dataset | schemaorg.MediaObject, dataset: schemaorg.Dataset | None
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
        attrs: Attributes = [],
        *,
        guess_mime: bool = True,
        dataset: IdentifiedNode | None = None,
        **kwargs: Any,
    ) -> IdentifiedNode:
        """
        Adds file metadata to the crate

        Returns: The ID of the new file entity

        Params:
            path: Path or URL to the file being added
            attrs: Attributes used to describe the `File` entity
            guess_mime: If true, automatically guess and document the MIME type of the file based on its extension
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.

        Example:
            ```python
            from rdfcrate import uris, AttachedCrate

            AttachedCrate(".").register_file("./some/data.txt", [
                (uris.description, Literal("This is a file with some data")),
            ])
            ```
        """
        file_id = URIRef(path)
        self.add_entity(file_id, [uris.File], attrs)

        if guess_mime:
            if has_predicate(attrs, uris.encodingFormat):
                raise ValueError(
                    "Cannot guess MIME type when encodingFormat is provided"
                )
            guess_type, _guess_encoding = mimetypes.guess_type(path)
            if guess_type is not None:
                self.add_metadata(file_id, [(uris.encodingFormat, Literal(guess_type))])

        self.link_to_dataset(file_id, dataset)

        return file_id

    def register_dir(
        self,
        path: str,
        attrs: Attributes = {},
        *,
        dataset: IdentifiedNode | None = None,
        **kwargs: Any,
    ) -> IdentifiedNode:
        """
        Adds metadata for a directory

        Returns:
            The ID of the new directory entity

        Params:
            path: Path to the directory, which must be within the crate root
            attrs: Attributes used to describe the `Dataset` entity
            dataset: Dataset entity that the file should be linked to. If not provided, the file will be linked to the root dataset.
                Note that

        Example:
            ```python
            from rdfcrate import uris, AttachedCrate

            AttachedCrate(".").register_dir("./some/dir", [
                (uris.description, Literal("This is a directory I am describing")),
            ])
            ```
        """
        if not path.endswith("/"):
            # Directories must end with a slash in RO-Crate
            path += "/"
        dir_id = URIRef(path)
        self.add_entity(dir_id, [uris.Dataset], attrs)
        if self.root_data_entity != dir_id:
            # The root dataset is not linked to itself
            self.link_to_dataset(dir_id, dataset)
        return dir_id

    def add_metadata(self, uri: URIRef, *args: EntityArgs) -> IdentifiedNode:
        """
        Add metadata for an existing entity.

        Returns:
            The ID of the updated entity

        Params:
            entity: ID of the entity being described
        """
        for arg in args:
            arg.add_to_graph(self.graph, uri)
        return uri

    def compile(self, extra_context: Context | None = None) -> str:
        """
        Compiles the RO-Crate to a JSON-LD string

        Params:
            context: Additional context used to define compact JSON-LD terms. This is actually required if you use any custom terms that aren't in the crate. See: https://www.researchobject.org/ro-crate/specification/1.1/structure.html#ro-crate-metadata-file-ro-crate-metadatajson. You can use utility functions in [`rdfcrate.context`][rdfcrate.context] to generate this.
        """
        # Serializer kwargs are annoyingly not listed in the docs.
        # See them here: https://github.com/RDFLib/rdflib/blob/d220ee3bcba10a7af6630c4faaa37ca9cee33554/rdflib/plugins/serializers/jsonld.py#L76-L84
        if extra_context is not None:
            context = [
                self.version.context_url,
                extra_context,
            ]
        else:
            context = self.version.context_url

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

    #: If true, automatically initialize the crate with all files and directories in the root
    recursive_init: InitVar[bool] = field(default=False, kw_only=True)

    def __post_init__(
        self,
        name: str,
        description: str,
        license: str | URIRef,
        path: Path | str,
        recursive_init: bool = False,
    ):
        self.root = Path(path)
        root_dataset = self.register_dir(
            self.root,
            recursive=recursive_init,
            attrs=[
                (uris.datePublished, Literal(datetime.now().isoformat())),
                (uris.name, Literal(name)),
                (uris.description, Literal(description)),
                (
                    uris.license,
                    license if isinstance(license, URIRef) else Literal(license),
                ),
            ],
        )
        self.add_entity(
            URIRef(self._resolve_path(self._metadata_path)),
            type=[uris.CreativeWork],
            attrs=[
                (uris.conformsTo, URIRef(self.version.conforms_to_url)),
                (uris.about, root_dataset),
            ],
        )

    @property
    def metadata_entity(self) -> IdentifiedNode:
        """
        The metadata entity of the RO-Crate
        """
        return URIRef(self._resolve_path(self._metadata_path))

    @property
    def root_data_entity(self) -> IdentifiedNode:
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

    def _resolve_path(self, path: Path | str) -> str:
        """
        Converts a crate path to a platform independent path compatible with RO-Crate
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

        return path.relative_to(self.root).as_posix()

    def register_file(
        self,
        path: Path | str,
        attrs: Attributes = [],
        *,
        add_size: bool = False,
        **kwargs: Any,
    ):
        """
        See [`RoCrate.register_file`][rdfcrate.wrapper.RoCrate.register_file].

        Params:
            add_size: If true, automatically add the size of the file to the metadata
        """
        path = Path(path)
        file_id = self._resolve_path(path)
        ret = super().register_file(file_id, attrs, **kwargs)
        if add_size:
            if has_predicate(attrs, uris.contentSize):
                raise ValueError("Cannot add size when contentSize is provided")
            self.add_metadata(
                URIRef(file_id), [(uris.contentSize, Literal(stat(path).st_size))]
            )
        return ret

    def register_dir(
        self,
        path: Path | str,
        attrs: Attributes = [],
        *,
        recursive: bool = False,
        **kwargs: Any,
    ):
        """
        See [`RoCrate.register_dir`][rdfcrate.wrapper.RoCrate.register_dir].

        Params:
            recursive: If true, register all files and subdirectories in the directory.
                The child entities will only have minimal metadata, but more can be added later with [`RoCrate.add_metadata`][rdfcrate.wrapper.RoCrate.add_metadata].
                Also note that each registered data entity will be linked to the directory entity with `hasPart`.

        """
        id = super().register_dir(self._resolve_path(path), attrs, **kwargs)

        if recursive:
            for child in Path(path).iterdir():
                if child in {self._metadata_path, self.root}:
                    # Never register the metadata file or the root directory
                    continue
                if child.is_dir():
                    self.register_dir(child, recursive=True, dataset=id)
                else:
                    self.register_file(child, dataset=id)
        return id


@dataclass
class DetatchedCrate(RoCrate):
    """
    A crate describing remote files.

    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#detached-ro-crate>
    """

    root: str

    @property
    def root_data_entity(self) -> IdentifiedNode:
        return URIRef(self.root)

    def __post_init__(self, name: str, description: str, license: str | URIRef):
        self.register_dir(self.root)
