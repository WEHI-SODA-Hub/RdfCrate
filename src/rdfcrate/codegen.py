"""
Generates URIs for everything in the RO-Crate context
"""
import ast
import itertools
from typing import Any, Iterable, cast
import keyword
from rdflib import Graph, RDFS, RDF, SDO, IdentifiedNode, URIRef
from rdflib.plugins.shared.jsonld.context import Context
from itertools import chain
import argparse

from rdflib.term import Identifier
from rdfcrate.spec_version import all_specs, SpecVersion
from graphlib import TopologicalSorter

type ContextMap = dict[SpecVersion, dict[str, Any]]

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


def property_range(graph: Graph, prop: URIRef) -> ast.expr:
    """
    Returns the range of a property, as a type annotation
    """
    range_options = []
    for range_ in itertools.chain(
        graph.objects(subject=prop, predicate=RDFS.range),
        graph.objects(subject=prop, predicate=SDO.rangeIncludes),
    ):
        # Check if the range is a class
        if triple_in_graph(graph, range_, RDF.type, RDFS.Class):
            _, _, range_name = graph.compute_qname(range_)
            range_options.append(range_name)
    if len(range_options) == 0:
        # If no range is found, use the default
        return ast.Name("RdfType")
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

def term_with_specs(term: str, uri: str, contexts: ContextMap) -> ast.Call:
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
            ast.Constant(uri),
            ast.List([
                # Add RO-Crate specs that this term is defined in
                ast.Constant(spec.version) for spec, ctx in contexts.items() if ctx.get(term) == uri
            ])
        ],
        keywords=[]
    )

def properties_from_rdfs(graph: Graph, context_map: ContextMap) -> Iterable[ast.ClassDef]:
    """
    Creates a PropertyList subclass from RDFS definitions

    e.g.
    ```
    @dataclass
    class Bioschemas:
        input: Annotated[list[FormalParameter], RdfTerm("input", "https://bioschemas.org/properties/input")] = field(default_factory=list)
    ```
    """
    for prop in graph.subjects(predicate=RDF.type, object=RDF.Property, unique=True):
        _, _, name = graph.compute_qname(prop)

        """
        e.g. 
        @dataclass(frozen=True)
        class image:
            term = RdfTerm("image", "https://schema.org/image")
            object: ImageObject
        """
        yield ast.ClassDef(
            name=sanitize_cls_name(name),
            type_params=[],
            bases=[ast.Name("RdfProperty")],
            keywords=[],
            body=[
                ast.Assign(
                    targets=[ast.Name("term")],
                    value=term_with_specs(name, str(prop), context_map),
                    type_comment=None
                ),
                ast.AnnAssign(
                    target=ast.Name("object"),
                    annotation=property_range(graph, prop),
                    value=None,
                    simple=1
                )
            ],
            decorator_list=[]
        )


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
                        slice=ast.Name("RdfType")  # Context mode does not handle ranges
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

def classes_from_rdfs(graph: Graph, context_map: ContextMap) -> Iterable[ast.ClassDef]:
    """
    Creates a list of classes from RDFS definitions
    e.g.
    ```
    class ComputationalWorkflow(RdfType):
        field = RdfTerm("field", "https://schema.org/field")
    ```
    """
    # Map of class names to their definitions
    classes: dict[str, ast.ClassDef] = {}
    # Map of class names to the parent classes they depend on
    class_deps: dict[str, list[str]] = {}
    for cls in graph.subjects(predicate=RDF.type, object=RDFS.Class, unique=True):
        _, _, name = graph.compute_qname(cls)
        
        # Determine the base classes from rdfs:subClassOf
        bases: list[ast.Name] = []
        for superclass in graph.objects(subject=cls, predicate=RDFS.subClassOf):
            if (superclass, RDF.type, RDFS.Class) in graph:
                _, _, superclass_name = graph.compute_qname(superclass)
                bases.append(ast.Name(sanitize_cls_name(superclass_name)))
        if len(bases) == 0:
            bases = [ast.Name("RdfType")]

        term = ast.Call(
            func=ast.Name("RdfTerm"),
            args=[
                ast.Constant(name),
                ast.Constant(str(cls)),
                ast.List([
                    # Add RO-Crate specs that this term is defined in
                    ast.Constant(spec.version) for spec, ctx in context_map.items() if ctx.get(name) == str(cls)
                ])
            ],
            keywords=[]
        )

        cls_name = sanitize_cls_name(name)
        classes[cls_name] = ast.ClassDef(
            name=cls_name,
            type_params=[],
            bases=bases,
            keywords=[],
            body=[
                ast.Assign(
                    targets=[ast.Name("term")],
                    value=term,
                    type_comment=None
                )
            ],
            decorator_list=[]
        )
        # Update dependencies
        class_deps[cls_name] = [base.id for base in bases if base.id != "RdfType"]
    
    # Sort the classes topologically so that parent classes are defined before child classes
    sorter = TopologicalSorter(class_deps)
    for cls_name in sorter.static_order():
        yield classes[cls_name]

def type_module(name: str, classes: Iterable[ast.ClassDef], properties: Iterable[ast.ClassDef]) -> ast.Module:
    """
    Creates an RdfType subclass from RDFS definitions
    e.g.
    ```
    from rdfcrate.rdftype import RdfType
    from rdfcrate.rdfterm import RdfTerm

    class ComputationalWorkflow(RdfType):
        field = RdfTerm("field", "https://schema.org/field")
    ```
    """
    return ast.fix_missing_locations(
        ast.Module([
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
                module="rdfcrate.rdftype",
                names=[ast.alias("RdfType")],
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
            ),
            *list(classes),
            *list(properties),
        ], type_ignores=[])
    )

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate Python code for RDF properties")
    parser.add_argument("input", type=str, help="Input RDF files", nargs="+")
    parser.add_argument("--name", type=str, help="Name of the class to generate")
    return parser

def load_spec_contexts() -> ContextMap:
    """
    Loads the RO-Crate contexts from the spec_version.py file
    """
    contexts = {}
    for spec in all_specs:
        contexts[spec] = spec.get_context()
    return contexts

def main():
    parser = get_parser()
    args = parser.parse_args()

    specs = load_spec_contexts()

    graph = Graph()
    for input_file in args.input:
        graph.parse(input_file)

    ret = type_module(args.name, classes_from_rdfs(graph, specs), properties_from_rdfs(graph, specs))

    print(ast.unparse(ret))

if __name__ == "__main__":
    main()
