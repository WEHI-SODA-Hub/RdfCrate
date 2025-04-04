"""
Generates URIs for everything in the RO-Crate context
"""
import ast
from typing import Iterable, cast
import keyword
from rdflib import Graph, RDFS, RDF
from rdflib.plugins.shared.jsonld.context import Context
from itertools import chain
import argparse

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


def properties_from_rdfs(graph: Graph) -> Iterable[ast.AnnAssign]:
    """
    Creates a PropertyList subclass from RDFS definitions

    e.g.
    ```
    @dataclass
    class Bioschemas:
        input: list[Annotated[FormalParameter, RdfTerm("input", "https://bioschemas.org/properties/input")]] = field(default_factory=list)
    ```
    """
    for prop in graph.subjects(predicate=RDF.type, object=RDF.Property, unique=True):
        _, _, name = graph.compute_qname(prop)
        yield ast.AnnAssign(
            target=ast.Name(camel_to_snake(name)),
            annotation=ast.Subscript(
                value=ast.Name("list"),
                slice=ast.Subscript(
                    value=ast.Name("Annotated"),
                    slice=ast.Tuple(elts=[
                        ast.Name("RdfType"),
                        ast.Call(
                            func=ast.Name("RdfTerm"),
                            args=[
                                ast.Constant(name),
                                ast.Constant(str(prop))
                            ],
                            keywords=[]
                        )
                    ])
                )
            ),
            value=ast.Call(
                func=ast.Name("field"),
                args=[],
                keywords=[ast.keyword(arg="default_factory", value=ast.Name("list"))]
            ),
            simple=1
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
        e.g. `input: list[Annotated[FormalParameter, RdfTerm("input", "https://bioschemas.org/properties/input")]] = field(default_factory=list)`
        """
        yield ast.AnnAssign(
            target=ast.Name(field_name),
            annotation=ast.Subscript(
                value=ast.Name("list"),
                slice=ast.Subscript(
                    value=ast.Name("Annotated"),
                    slice=ast.Tuple(elts=[
                        ast.Name("RdfType"),
                        ast.Call(
                            func=ast.Name("RdfTerm"),
                            args=[
                                ast.Constant(term),
                                ast.Constant(uri)
                            ],
                            keywords=[]
                        )
                    ])
                )
            ),
            value=ast.Call(
                func=ast.Name("field"),
                args=[],
                keywords=[ast.keyword(arg="default_factory", value=ast.Name("list"))]
            ),
            simple=1
        )

def class_with_properties(name: str, properties: Iterable[ast.AnnAssign]) -> ast.ClassDef:
    return ast.fix_missing_locations(ast.ClassDef(
        name=name,
        type_params=[],
        bases=[],#ast.Name("PropertyList")],
        keywords=[],
        body=list(properties),
        decorator_list=[]
    ))

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate Python code for RDF properties")
    parser.add_argument("input", type=str, help="Input RDF files", nargs="+")
    parser.add_argument("--mode", choices=["context", "rdfs"], help="How to generate the properties. If context, then use the JSON-LD context. If RDFS, then use the RDFS class and property definitions.", default="rdfs")
    parser.add_argument("--type", choices=["class", "property"], help="Which code to generate. If `class`, then RDF classes/types, if `property` then RDF properties", default="rdfs")
    parser.add_argument("--name", type=str, help="Name of the class to generate")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    # Generate the properties
    if args.mode == "context":
        context = Context(args.input[0])
        context = cast(dict, context)
        properties = properties_from_context(context)
    else:
        # Load the RDF graph
        graph = Graph()
        for input_file in args.input:
            graph.parse(input_file)

        properties = properties_from_rdfs(graph)

    # Print the generated code
    print(ast.unparse(class_with_properties(args.name, properties)))
    
