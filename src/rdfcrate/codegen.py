"""
Generates URIs for everything in the RO-Crate context
"""
import ast
from dataclasses import dataclass, field
import itertools
from pathlib import Path
from typing import Annotated, Any, Iterable, cast
import keyword
from typing_extensions import Doc
from rdflib import Graph, RDFS, RDF, SDO, IdentifiedNode, URIRef
from rdflib.plugins.shared.jsonld.context import Context
from itertools import chain
import argparse

from rdflib.term import Identifier
from rdfcrate.spec_version import all_specs, SpecVersion
from graphlib import TopologicalSorter

VOCABS = [
    "https://bioschemas.org/types/bioschemas_types.jsonld",
    "https://bioschemas.org/types/bioschemas_draft_types.jsonld",
    "https://schema.org/version/latest/schemaorg-current-http.jsonld",
    "https://www.w3.org/1999/02/22-rdf-syntax-ns",
    "https://pcdm.org/models.rdf",
    "https://www.w3.org/ns/prov.ttl",
    "http://purl.org/pav",
    "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl",
    "https://www.w3.org/TR/dx-prof/rdf/prof.ttl",
    "https://opengeospatial.github.io/ogc-geosparql/geosparql11/geo.ttl"
]

@dataclass
class CodegenState:
    context_map: dict[SpecVersion, dict[str, Any]] = field(default_factory=dict)
    #: A map of URIs to Python modules in which they are located. This is used for resolving imports "
    term_map: dict[str, str] = field(default_factory=dict)
    #: List of class definitions. Functions should append to this to define new classes.
    classes: list[ast.ClassDef] = field(default_factory=list)
    #: List of imports, which can be appended to.
    imports: list[ast.ImportFrom] = field(default_factory=list)

    graph: Graph = field(default_factory=Graph)

    def __post_init__(self):
        self.imports = [
            ast.ImportFrom(
                module="__future__",
                names=[ast.alias("annotations")],
                level=0
            ),
            ast.ImportFrom(
                module="typing",
                names=[
                    ast.alias("TypedDict"),
                    ast.alias("Annotated"),
                ],
                level=0
            ),
            ast.ImportFrom(
                module="rdflib.term",
                names=[ast.alias("Identifier")],
                level=0
            ),
            ast.ImportFrom(
                module="rdfcrate.rdfdatatype",
                names=[ast.alias("RdfDataType")],
                level=0
            ),
            ast.ImportFrom(
                module="rdfcrate.rdfclass",
                names=[ast.alias("RdfClass")],
                level=0
            ),
            ast.ImportFrom(
                module="rdfcrate.rdfprop",
                names=[ast.alias("RdfProperty")],
                level=0
            ),
            ast.ImportFrom(
                module="rdfcrate.rdfterm",
                names=[ast.alias("RdfTerm")],
                level=0
            )
        ]

        for spec in all_specs:
            self.context_map[spec] = spec.get_context()

    def reset_graph(self):
        self.graph = Graph()

    def property_range(self, prop: URIRef) -> ast.expr:
        """
        Returns the range of a property, as a type annotation
        """
        range_options = []
        for range_ in itertools.chain(
            self.graph.objects(subject=prop, predicate=RDFS.range),
            self.graph.objects(subject=prop, predicate=SDO.rangeIncludes),
        ):
            # Check if the range is a class
            if triple_in_graph(self.graph, range_, RDF.type, RDFS.Class):
                _, _, range_name = self.graph.compute_qname(range_)
                range_options.append(range_name)
        if len(range_options) == 0:
            # If no range is found, use the default
            return ast.Name("Identifier")
        elif len(range_options) == 1:
            # If one range is found, use it
            return ast.Name(range_options[0])
        elif len(range_options) > 1:
            # If multiple ranges are found, use a type union with `|`
            union_expr = ast.BinOp(
                left=ast.Name(range_options[0]),
                op=ast.BitOr(),
                right=ast.Name(range_options[1])
            )
            for range_name in range_options[2:]:
                union_expr = ast.BinOp(
                    left=union_expr,
                    op=ast.BitOr(),
                    right=ast.Name(range_name)
                )
            return union_expr

        raise ValueError(f"Could not determine range for property {prop}. No range found.")

    def term_with_specs(self, term: str, uri: str) -> ast.Call:
        """
        Creates the Python code for something like:
        ```python
        RdfTerm('CoverArt', 'http://schema.org/CoverArt', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
        ```
        """
        return ast.Call(
            func=ast.Name("RdfTerm"),
            args=[
                ast.Constant(term),
                ast.Constant(str(uri)),
                ast.List([
                    # Add RO-Crate specs that this term is defined in
                    ast.Constant(spec.version) for spec, ctx in self.context_map.items() if ctx.get(term) == uri
                ])
            ],
            keywords=[]
        )

    def properties_from_rdfs(self, module_base: str):
        """
        Creates a PropertyList subclass from RDFS definitions

        e.g.
        ```
        @dataclass
        class Bioschemas:
            input: Annotated[list[FormalParameter], RdfTerm("input", "https://bioschemas.org/properties/input")] = field(default_factory=list)
        ```
        """
        for prop in self.graph.subjects(predicate=RDF.type, object=RDF.Property, unique=True):
            if prop in self.term_map:
                # Skip properties that are already defined
                continue

            _, _, name = self.graph.compute_qname(prop)

            """
            e.g. 
            @dataclass(frozen=True)
            class image:
                term = RdfTerm("image", "https://schema.org/image")
                object: ImageObject
            """
            # Register this URI as being defined in this module
            self.term_map[prop] = f"{module_base}.{name}"
            self.classes.append(ast.ClassDef(
                name=sanitize_cls_name(name),
                type_params=[],
                bases=[ast.Name("RdfProperty")],
                keywords=[],
                body=[
                    ast.Assign(
                        targets=[ast.Name("term")],
                        value=self.term_with_specs(name, str(prop)),
                        type_comment=None
                    ),
                    ast.AnnAssign(
                        target=ast.Name("object"),
                        annotation=self.property_range(prop),
                        value=None,
                        simple=1
                    )
                ],
                decorator_list=[]
            ))

    def datatypes_from_rdfs(self, module_base: str) -> Iterable[ast.ClassDef]:
        """
        Creates a list of datatypes from RDFS definitions
        e.g.
        ```
        class Html(RdfDataType):
            field = RdfTerm("field", "https://schema.org/field")
        ```
        """
        for datatype in graph.subjects(predicate=RDF.type, object=RDFS.Datatype, unique=True):
            if datatype in term_map:
                # Skip datatypes that are already defined
                continue

            _, _, name = graph.compute_qname(datatype)
            # Register this URI as being defined in this module
            term_map[datatype] = f"{module_base}.{name}"
            yield ast.ClassDef(
                name=sanitize_cls_name(name),
                type_params=[],
                bases=[ast.Name("RdfDataType")],
                keywords=[],
                body=[
                    ast.Assign(
                        targets=[ast.Name("term")],
                        value=term_with_specs(name, str(datatype), contexts),
                        type_comment=None
                    )
                ],
                decorator_list=[]
            )

    def classes_from_rdfs(self, module_base: str) -> Iterable[ast.stmt]:
        """
        Creates a list of classes from RDFS definitions
        """
        # Map of class names to their definitions
        classes: dict[str, ast.ClassDef] = {}
        # Map of class names to the parent classes they depend on
        class_deps: dict[str, list[str]] = {}
        imports: list[ast.ImportFrom] = []
        for cls_uri in self.graph.subjects(predicate=RDF.type, object=RDFS.Class, unique=True):
            if cls_uri in self.term_map:
                # Skip classes that are already defined
                continue

            # Compute the short term name by removing the base URI
            _, _, term_name = self.graph.compute_qname(cls_uri)
            
            # Determine the base classes from rdfs:subClassOf
            bases: list[ast.Name] = []
            for superclass_uri in self.graph.objects(subject=cls_uri, predicate=RDFS.subClassOf):
                if (superclass_uri, RDF.type, RDFS.Class) in self.graph:
                    _, _, superclass_term = self.graph.compute_qname(superclass_uri)
                    superclass_name = sanitize_cls_name(superclass_term)
                    bases.append(ast.Name(superclass_name))
                    if superclass_uri in self.term_map:
                        # If we find a previously defined superclass, we need to import it
                        imports.append(ast.ImportFrom(
                            module=self.term_map[superclass_uri],
                            names=[ast.alias(superclass_name)],
                            level=0
                        ))
                        
            if len(bases) == 0:
                bases = [ast.Name("RdfClass")]

            cls_name = sanitize_cls_name(term_name)
            classes[cls_name] = ast.ClassDef(
                name=cls_name,
                type_params=[],
                bases=bases,
                keywords=[],
                body=[
                    ast.Assign(
                        targets=[ast.Name("term")],
                        value=self.term_with_specs(term_name, cls_uri),
                        type_comment=None
                    )
                ],
                decorator_list=[]
            )
            self.term_map[cls_uri] = f"{module_base}.{cls_name}"
            # Update dependencies
            class_deps[cls_name] = [base.id for base in bases if base.id != "RdfClass"]
        
        # Sort the classes topologically so that parent classes are defined before child classes
        sorter = TopologicalSorter(class_deps)
        sorted_classes = [ classes[cls_name] for cls_name in sorter.static_order() ]
        return imports + sorted_classes

    def type_module(self, module_base: str) -> ast.Module:
        """
        Creates a module that lists all the classes and properties in the graph
        """
        self.classes_from_rdfs(module_base)
        self.properties_from_rdfs(module_base)
        self.datatypes_from_rdfs(module_base)

        return ast.fix_missing_locations(
            ast.Module([
                *self.imports,
                *self.classes
            ], type_ignores=[])
        )


def camel_to_snake(camel: str) -> str:
    segments = []
    start = 0
    i = 0
    for i, letter in enumerate(camel):
        if letter.isupper():
            segments.append(camel[start:i].lower())
            start = i
    
    segments.append(camel[start:].lower())
    return "_".join(segments)

def sanitize_cls_name(name: str) -> str:
    """
    Sanitizes a class name to be a valid Python identifier
    """
    name = name.replace("-", "_")
    if not name.isidentifier() or keyword.iskeyword(name):
        return f"_{name}"
    return name

def triple_in_graph(graph: Graph, subject: IdentifiedNode, predicate: URIRef, object: IdentifiedNode) -> bool:
    """
    Checks if a triple is in the graph, checking both http and https versions of the subject
    """
    if (URIRef(subject.replace("http:", "https:")), predicate, object) in graph:
        return True
    if (URIRef(subject.replace("https:", "http:")), predicate, object) in graph:
        return True
    return False



def properties_from_context(context: dict) -> Iterable[ast.AnnAssign]:
    """
    Yields properties from a JSON-LD context
    """
    for term, uri in context["@context"].items():
        # Workaround for invalid Python identifiers
        field_name = term
        if (not field_name.isidentifier()) or keyword.iskeyword(field_name):
            field_name = "_" + field_name.replace("-", "_")
        
        if term[0].isupper():
            # Skip classes
            continue

        """
        e.g. `input: Annotated[list[FormalParameter], RdfTerm("input", "https://bioschemas.org/properties/input")] = field(default_factory=list)`
        """
        yield ast.AnnAssign(
            target=ast.Name(field_name),
            annotation=ast.Subscript(
                value=ast.Name("Annotated"),
                slice=ast.Tuple(elts=[
                    ast.Subscript(
                        value=ast.Name("list"),
                        slice=ast.Name("RdfClass")
                    ),
                    ast.Call(
                        func=ast.Name("RdfTerm"),
                        args=[
                            ast.Constant(term),
                            ast.Constant(uri)
                        ],
                        keywords=[]
                    )
                ])
            ),
            value=ast.Call(
                func=ast.Name("field"),
                args=[],
                keywords=[ast.keyword(arg="default_factory", value=ast.Name("list"))]
            ),
            simple=1
        )

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate Python code for RDF properties")
    parser.add_argument("input", type=str, help="Input RDF files", nargs="*", default=VOCABS)
    return parser

# def load_spec_contexts() -> ContextMap:
#     """
#     Loads the RO-Crate contexts from the spec_version.py file
#     """
#     contexts = {}
#     for spec in all_specs:
#         contexts[spec] = spec.get_context()
#     return contexts

def schema_org_https(graph: Graph):
    """
    Rewrites the schema.org URIs in the graph to use http instead of https
    """
    for triple in graph:
        new_triple = tuple([uri.replace("http://schema.org/", "https://schema.org/") for uri in triple])
        if triple != new_triple:
            graph.remove(triple)
            graph.add(new_triple)

def generate_modules(vocabs: dict[str, list[str]], base_module: str, out_dir: Path):
    """
    Generates a module in the given directory for each vocabulary

    Params:
        vocabs: A dictionary of vocabulary names to URIs RDFS URIs. This should be ordered such that dependencies like schema.org come first.
        out_dir: The output directory
    """
    state = CodegenState()
    for vocab, uris in vocabs.items():
        state.reset_graph()
        for uri in uris:
            state.graph.parse(uri)
        module = state.type_module(base_module)
        out_path = out_dir / f"{vocab}.py"
        out_path.write_text(ast.unparse(module))

def core_vocab():
    generate_modules({
        "rdf": ["https://www.w3.org/1999/02/22-rdf-syntax-ns"],
        "schemaorg": ["https://schema.org/version/latest/schemaorg-current-http.jsonld"],
        "bioschemas": ["https://bioschemas.org/types/bioschemas_types.jsonld", "https://bioschemas.org/types/bioschemas_draft_types.jsonld"],
        "pcdm": ["https://pcdm.org/models.rdf"],
        "prov": ["https://www.w3.org/ns/prov.ttl"],
        "pav": ["http://purl.org/pav"],
        "dc": ["https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl"],
        "prof": ["https://www.w3.org/TR/dx-prof/rdf/prof.ttl"],
        "geo": ["https://opengeospatial.github.io/ogc-geosparql/geosparql11/geo.ttl"]
    }, "rdfcrate.vocabs", Path("src/rdfcrate/vocabs"))

if __name__ == "__main__":
    core_vocab()

# def main():
#     parser = get_parser()
#     args = parser.parse_args()
#     for input_file in args.input:
#         graph.parse(input_file)

#     ret = type_module(graph)

#     print(ast.unparse(ret))

# if __name__ == "__main__":
#     main()
