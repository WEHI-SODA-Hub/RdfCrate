from pathlib import Path
from typing import Any, Iterable
from rdflib import Graph, URIRef, Literal, RDF, IdentifiedNode
from rdfcrate import uris
from rdfcrate.spec_version import SpecVersion, ROCrate1_1
from dataclasses import InitVar, dataclass, field
import mimetypes
from os import stat
from datetime import datetime

#: Predicate-object tuple
Double = tuple[URIRef, Literal | IdentifiedNode]
Attributes = Iterable[Double]
Type = Iterable[URIRef]

def has_predicate(double: Iterable[Double], predicate: URIRef) -> bool:
    """
    Checks if an attribute list contains a specific predicate
    """
    return any(pred == predicate for pred, _ in double)

@dataclass
class RoCrate:
    """
    Abstract class containing common functionality for both attached and detached RO-Crates
    """
    graph: Graph = field(init=False, default_factory=Graph)
    """
    `rdflib.Graph` containing the RO-Crate metadata. This can be accessed directly, but it is recommended to use the other methods provided by this class where available.
    """
    version: SpecVersion = field(kw_only=True, default=ROCrate1_1)
    "Version of the RO-Crate specification to use"

    def add_entity(self, id: IdentifiedNode, type: Type, attrs: Attributes = []) -> IdentifiedNode:
        """
        Adds any type of entity to the crate

        Params:
            id: ID of the entity being added
            type: Type of the entity being added
            attrs: Attributes of the entity being added

        Returns:
            The ID of the new entity

        Example:
            ```python
            from rdflib import BNode,
            from rdfcrate import uris

            crate.add_entity(BNode(), [uris.Person], [(uris.name, Literal("Alice"))])
            ```
        """
        for t in type:
            self.graph.add((id, RDF.type, t))
        self.add_metadata(id, attrs)
        return id
    
    def register_file(self, path: str, attrs: Attributes = [], guess_mime: bool = True, **kwargs: Any) -> IdentifiedNode:
        """
        Adds file metadata to the crate

        Returns: The ID of the new file entity

        Params:
            path: Path or URL to the file being added
            attrs: Attributes used to describe the `File` entity
            guess_mime: If true, automatically guess and document the MIME type of the file based on its extension

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
                raise ValueError("Cannot guess MIME type when encodingFormat is provided")
            guess_type, _guess_encoding = mimetypes.guess_type(path)
            if guess_type is not None:
                self.add_metadata(file_id, [(uris.encodingFormat, Literal(guess_type))])
        return file_id

    def register_dir(self, path: str, attrs: Attributes = {}, **kwargs: Any) -> IdentifiedNode:
        """
        Adds metadata for a directory

        Returns:
            The ID of the new directory entity

        Params:
            path: Path to the directory, which must be within the crate root
            attrs: Attributes used to describe the `Dataset` entity

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
        return dir_id

    def add_metadata(self, entity: IdentifiedNode, attrs: Attributes) -> IdentifiedNode:
        """
        Add metadata for an existing entity.

        Returns:
            The ID of the updated entity

        Params:
            entity: ID of the entity being described
            attrs: Attributes of the entity being described
        """
        for pred, obj in attrs:
            self.graph.add((entity, pred, obj))
        return entity

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
    path: InitVar[str | Path]
    "The RO-Crate directory"
    root: Path = field(init=False)
    "The RO-Crate directory"

    #: If true, automatically initialize the crate with all files and directories in the root
    recursive_init: InitVar[bool] = field(default=False, kw_only=True)

    def __post_init__(self, path: Path | str, recursive_init: bool = False):
        self.root = Path(path)
        root_dataset = self.register_dir(self.root, recursive=recursive_init, attrs=[
            (uris.datePublished, Literal(datetime.now().isoformat()))
        ])
        self.add_entity(URIRef(self._resolve_path(self._ro_crate_metadata)), type=[uris.CreativeWork], attrs=[
            (uris.conformsTo, URIRef(self.version.conforms_to)),
            (uris.about, root_dataset),
            # Even though File aka MediaObject is already a subclass of CreativeWork, the spec demands this is explicitly present
            (RDF.type, uris.CreativeWork)
        ])

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

    def register_file(self, path: Path | str, attrs: Attributes = [], guess_mime: bool = True, add_size: bool = False, **kwargs: Any):
        """
        See [`RoCrate.register_file`][rdfcrate.wrapper.RoCrate.register_file].

        Params:
            add_size: If true, automatically add the size of the file to the metadata
        """
        path = Path(path)
        file_id = self._resolve_path(path)
        ret = super().register_file(file_id, attrs, guess_mime)
        if add_size:
            if has_predicate(attrs, uris.contentSize):
                raise ValueError("Cannot add size when contentSize is provided")
            self.add_metadata(URIRef(file_id), [(uris.contentSize, Literal(stat(path).st_size))])
        return ret

    def register_dir(self, path: Path | str, attrs: Attributes = [], recursive: bool = False, **kwargs: Any):
        """
        See [`RoCrate.register_dir`][rdfcrate.wrapper.RoCrate.register_dir].

        Params:
            recursive: If true, register all files and subdirectories in the directory. The automatically created children will only have default metadata.
                You can use `add_metadata` to document them more comprehensively.
        """
        id = super().register_dir(self._resolve_path(path), attrs)

        if recursive:
            for child in Path(path).iterdir():
                if child.is_dir():
                    child_id = self.register_dir(child, recursive=True)
                else:
                    child_id = self.register_file(child)
                self.add_metadata(id, [(uris.hasPart, child_id)])
        return id

@dataclass
class DetatchedCrate(RoCrate):
    """
    A crate describing local files.

    See <https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/structure#detached-ro-crate>
    """
    root: str

    def __post_init__(self):
        self.register_dir(self.root)
