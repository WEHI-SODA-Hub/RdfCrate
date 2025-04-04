"""
Generates URIs for everything in the RO-Crate context
"""
import ast
import itertools
from typing import Iterable, cast
import keyword
from rdflib import Graph, RDFS, RDF, SDO, URIRef
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


def property_range(graph: Graph, prop: URIRef) -> ast.expr:
    """
    Returns the range of a property, as a type annotation
    """
    # range_name = "RdfType"
    range_options = []
    for range_ in itertools.chain(
        graph.objects(subject=prop, predicate=RDFS.range),
        graph.objects(subject=prop, predicate=SDO.rangeIncludes),
    ):
        # Check if the range is a class
        if (range_, RDF.type, RDFS.Class) in graph:
            _, _, range_name = graph.compute_qname(range_)
            range_options.append(range_name)
    if len(range_options) == 0:
        # If no range is found, use the default
        return ast.Name("RdfType")
    elif len(range_options) == 1:
        # If one range is found, use it
        return ast.Name(range_options[0])
    elif len(range_options) > 1:
        # If multiple ranges are found, use a union of the ranges
        return ast.Subscript(
            value=ast.Name("Union"),
            slice=ast.Tuple(elts=[ast.Name(range_name) for range_name in range_options])
        )

    raise ValueError(f"Could not determine range for property {prop}. No range found.")

def properties_from_rdfs(graph: Graph) -> Iterable[ast.AnnAssign]:
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

        yield ast.AnnAssign(
            target=ast.Name(camel_to_snake(name)),
            annotation=ast.Subscript(
                value=ast.Name("Annotated"),
                slice=ast.Tuple(elts=[
                    ast.Subscript(
                        value=ast.Name("list"),
                        slice=property_range(graph, prop)
                    ),
                    ast.Call(
                        func=ast.Name("RdfTerm"),
                        args=[
                            ast.Constant(name),
                            ast.Constant(str(prop))
                        ],
                        keywords=[]
                    )
                ])
            ),
            value=None,
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

def classes_from_rdfs(graph: Graph) -> Iterable[ast.ClassDef]:
    """
    Creates a list of classes from RDFS definitions
    e.g.
    ```
    class ComputationalWorkflow(RdfType):
        field = RdfTerm("field", "https://schema.org/field")
    ```
    """
    for cls in graph.subjects(predicate=RDF.type, object=RDFS.Class, unique=True):
        _, _, name = graph.compute_qname(cls)
        
        # Determine the base classes from rdfs:subClassOf
        bases = [ast.Name("RdfType")]
        for superclass in graph.objects(subject=cls, predicate=RDFS.subClassOf):
            if (superclass, RDF.type, RDFS.Class) in graph:
                _, _, superclass_name = graph.compute_qname(superclass)
                bases.append(ast.Name(superclass_name))

        yield ast.ClassDef(
            name=name,
            type_params=[],
            bases=bases,
            keywords=[],
            body=[
                ast.Assign(
                    targets=[ast.Name("term")],
                    value=ast.Call(
                        func=ast.Name("RdfTerm"),
                        args=[
                            ast.Constant(name),
                            ast.Constant(str(cls))
                        ],
                        keywords=[],

                    ),
                    type_comment=None
                )
            ],
            decorator_list=[]
        )

def type_module(name: str, classes: Iterable[ast.ClassDef], properties: Iterable[ast.AnnAssign]) -> ast.Module:
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
                module="rdfcrate.rdfterm",
                names=[ast.alias("RdfTerm")],
                level=0
            ),
            *list(classes),
            ast.ClassDef(
                name=name.title(),
                type_params=[],
                bases=[ast.Name("TypedDict")],
                keywords=[ast.keyword(
                    "total", ast.Constant(False)
                )],
                body=list(properties),
                decorator_list=[]
            )
        ], type_ignores=[])
    )


def properties_module(name: str, properties: Iterable[ast.AnnAssign]) -> ast.Module:
    return ast.fix_missing_locations(
        ast.Module([
            ast.ImportFrom(
                module="typing",
                names=[ast.alias("TypedDict", None)],
                level=0
            ),
            ast.ImportFrom(
                module="rdfcrate.rdfterm",
                names=[ast.alias("RdfTerm", None)],
                level=0
            ),
            ast.ImportFrom(
                module="rdfcrate.rdftype",
                names=[ast.alias("RdfType", None)],
                level=0
            ),
            ast.ClassDef(
                name=name.title(),
                type_params=[],
                bases=[ast.Name("TypedDict")],#ast.Name("PropertyList")],
                keywords=[ast.keyword(
                    "total", ast.Constant(False)
                )],
                body=list(properties),
                decorator_list=[]
            )
        ], type_ignores=[])
    )

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate Python code for RDF properties")
    parser.add_argument("input", type=str, help="Input RDF files", nargs="+")
    parser.add_argument("--mode", choices=["context", "rdfs"], help="How to generate the properties. If context, then use the JSON-LD context. If RDFS, then use the RDFS class and property definitions.", default="rdfs")
    parser.add_argument("--name", type=str, help="Name of the class to generate")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.mode == "context":
        context = Context(args.input[0])
        context = cast(dict, context)
        raise NotImplementedError("Context mode is not implemented yet")
    else:
        graph = Graph()
        for input_file in args.input:
            graph.parse(input_file)

        ret = type_module(args.name, classes_from_rdfs(graph), properties_from_rdfs(graph))

    print(ast.unparse(ret))

    # if args.type == "class":
    # else:
    #     if args.mode == "context":
    #         context = Context(args.input[0])
    #         context = cast(dict, context)
    #         properties = properties_from_context(context)
    #     else:
    #         # Load the RDF graph
    #         graph = Graph()
    #         for input_file in args.input:
    #             graph.parse(input_file)

    #         properties = properties_from_rdfs(graph)

    #     print(ast.unparse(properties_module(args.name, properties)))
