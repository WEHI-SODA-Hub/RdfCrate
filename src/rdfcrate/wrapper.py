from pathlib import Path
from typing import Any
from rdflib import Graph, URIRef, Literal, RDF, IdentifiedNode
from rdfcrate import uris
from rdfcrate.spec_version import SpecVersion, ROCrate1_1
from dataclasses import InitVar, dataclass, field
import mimetypes
from os import stat

Attributes = dict[URIRef, Literal | IdentifiedNode]

@dataclass
class RoCrate:
    """
    Abstract class containing common functionality for both attached and detached RO-Crates
    """
    #: rdflib Graph containing the RO-Crate metadata. This can be accessed directly, but it is recommended to use the other methods provided by this class where available.
    graph: Graph = field(init=False, default_factory=Graph)
    #: Version of the RO-Crate specification to use
    version: SpecVersion = field(kw_only=True, default=ROCrate1_1)

    def add_entity(self, id: IdentifiedNode, type: URIRef, attrs: Attributes = {}):
        """
        Adds any type of entity to the crate

        Params:
            id: ID of the entity being added
            type: Type of the entity being added
            attrs: Attributes of the entity being added

        Example:
            ```python
            from rdflib import BNode,
            from rdfcrate import uris

            crate.add_entity(BNode(), uris.Person, {uris.name: Literal("Alice")})
            ```
        """
        self.graph.add((id, RDF.type, type))
        self.add_metadata(id, attrs)
    
    def register_file(self, path: str, attrs: Attributes = {}, guess_mime: bool = True, **kwargs: Any):
        """
        Adds file metadata to the crate

        Params:
            path: Path or URL to the file being added
            attrs: Attributes used to describe the `File` entity
            guess_mime: If true, automatically guess and document the MIME type of the file based on its extension
        """
        file_id = URIRef(path)
        self.add_entity(file_id, uris.File, attrs)
        if guess_mime:
            if uris.encodingFormat in attrs:
                raise ValueError("Cannot guess MIME type when encodingFormat is provided")
            guess_type, _guess_encoding = mimetypes.guess_type(path)
            if guess_type is not None:
                self.add_metadata(file_id, {uris.encodingFormat: Literal(guess_type)})

    def register_dir(self, path: str, attrs: Attributes = {}, **kwargs: Any):
        """
        Adds metadata for a directory

        Params:
            path: Path to the directory, which must be within the crate root
            attrs: Attributes used to describe the `Dataset` entity
        """
        self.add_entity(URIRef(path), uris.Dataset, attrs)

    def add_metadata(self, entity: IdentifiedNode, attrs: Attributes):
        """
        Add metadata for an existing entity.

        Params:
            entity: ID of the entity being described
            attrs: Attributes of the entity being described
        """
        for key, value in attrs.items():
            self.graph.add((entity, key, value))

    def compile(self) -> str:
        """
        Compiles the RO-Crate to a JSON-LD string
        """
        return self.graph.serialize(format="json-ld", context=self.version.context)

@dataclass
class AttachedCrate(RoCrate):
    """
    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#attached-ro-crate>
    """
    #: The RO-Crate directory
    path: InitVar[str | Path]
    root: Path = field(init=False)

    #: If true, automatically initialize the crate with all files and directories in the root
    recursive_init: InitVar[bool] = False

    def __post_init__(self, path: Path | str, recursive_init: bool = False):
        self.root = Path(path)
        self.register_dir(self.root, recursive=recursive_init, attrs={})
        self.register_file(self._ro_crate_metadata, attrs={
            uris.conformsTo: URIRef(self.version.conforms_to),
            uris.about: URIRef(".")
        })

    @property
    def _ro_crate_metadata(self) -> Path:
        """
        Path to the RO-Crate metadata file
        """
        return self.root / "ro-crate-metadata.json"

    def write(self):
        """
        Writes the RO-Crate to `ro-crate-metadata.json`
        """
        self._ro_crate_metadata.write_text(self.compile())

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
                raise ValueError(f"Path ({path}) must be within the crate root ({self.root})")
        else:
            # Relative paths are assumed to be relative to the crate root
            path = self.root / path

        return path.relative_to(self.root).as_posix()

    def register_file(self, path: Path | str, attrs: Attributes = {}, guess_mime: bool = True, add_size: bool = False, **kwargs: Any):
        """
        See [`RoCrate.register_file`][rdfcrate.wrapper.RoCrate.register_file].

        Params:
            add_size: If true, automatically add the size of the file to the metadata
        """
        path = Path(path)
        file_id = self._resolve_path(path)
        super().register_file(file_id, attrs, guess_mime)
        if add_size:
            if uris.contentSize in attrs:
                raise ValueError("Cannot add size when contentSize is provided")
            self.add_metadata(URIRef(file_id), {uris.contentSize: Literal(stat(path).st_size)})

    def register_dir(self, path: Path | str, attrs: Attributes = {}, recursive: bool = False, **kwargs: Any):
        """
        See [`RoCrate.register_dir`][rdfcrate.wrapper.RoCrate.register_dir].

        Params:
            recursive: If true, register all files and subdirectories in the directory. The automatically created children will only have default metadata.
                You can use `add_metadata` to document them more comprehensively.
        """
        super().register_dir(self._resolve_path(path), attrs)

        if recursive:
            for child in Path(path).iterdir():
                self.add_metadata(URIRef(self._resolve_path(path)), {uris.hasPart: URIRef(self._resolve_path(child))})
                if child.is_dir():
                    self.register_dir(child, recursive=True)
                else:
                    self.register_file(child)

@dataclass
class DetatchedCrate(RoCrate):
    """
    A crate describing local files.

    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#detached-ro-crate>
    """
    root: str

    def __post_init__(self):
        self.register_dir(self.root)
