from pathlib import Path
from rdflib import Graph, URIRef, Literal, RDF
import requests
from rdfcrate import uris
from rdfcrate.spec_version import SpecVersion, ROCrate1_1
from dataclasses import dataclass, field

@dataclass
class RoCrate:
    graph: Graph = field(init=False, default_factory=Graph)
    root: Path
    version: SpecVersion = ROCrate1_1

    def add_entity(self, id: URIRef, type: URIRef, attrs: dict[URIRef, URIRef | Literal]):
        """
        Adds any type of entity to the crate

        Params:
            id: ID of the entity being added
            type: Type of the entity being added
            attrs: Attributes of the entity being added
        """
        self.graph.add((id, RDF.type, type))
        for key, value in attrs.items():
            # _value: Literal | URIRef
            # if not isinstance(value, (Literal, URIRef)):
            #     _value = Literal(value)
            # else:
            #     _value = value
            self.graph.add((id, key, value))
    
    def register_file(self, path: Path, attrs: dict[URIRef, URIRef | Literal] = {}):
        """
        Adds metadata for a file already in the crate
        """
        if not path.is_relative_to(self.root):
            raise ValueError("File must be within the crate root")
        relative = URIRef(path.relative_to(self.root).as_posix())
        self.add_entity(relative, uris.File, attrs)

    def register_dir(self, path: Path, recursive: bool = False, attrs: dict[URIRef, URIRef | Literal] = {}):
        """
        Adds metadata for a directory already in the crate

        Params:
            path: Path to the directory, which must be within the crate root
            recursive: Whether to add metadata for all files and subdirectories in the directory. Note that if you do this, the children will only have default metadata.
                If you want to add complex metadata to the children, you should add them manually using `register_file` and `register_dir`.
            attrs: Attributes used to describe the `Dataset` entity
        """
        if not path.is_relative_to(self.root):
            raise ValueError("Directory must be within the crate root")
        relative = URIRef(path.relative_to(self.root).as_posix())
        self.add_entity(relative, uris.Dataset, attrs)

        if recursive:
            for child in path.iterdir():
                if child.is_dir():
                    self.register_dir(child, recursive=True, attrs={})
                else:
                    self.register_file(child, {})

    def compile(self) -> str:
        """
        Compiles the RO-Crate to a JSON-LD string
        """
        context_url = self.version.context
        context = requests.get(context_url).json()

        return self.graph.serialize(format="json-ld", context=context)

    @property
    def ro_crate_metadata(self) -> Path:
        """
        Path to the RO-Crate metadata file
        """
        return self.root / "ro-crate-metadata.json"

    def write(self):
        """
        Writes the RO-Crate to "ro-crate-metadata.json"
        """
        self.ro_crate_metadata.write_text(self.compile())
