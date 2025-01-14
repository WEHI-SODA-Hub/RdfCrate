"""
Generates URIs for everything in the RO-Crate context
"""
import ast
from typing import Iterable
import keyword
from rdflib import Graph, RDFS, RDF
from itertools import chain

def uris_from_rdfs(rdfs: str, format: str="json-ld") -> Iterable[ast.Assign]:
    """
    Yields AST nodes that define URIs for all classes and properties in the given RDFS document
    """
    graph = Graph().parse(data=rdfs, format=format)
    for cls in chain(
        graph.subjects(predicate=RDF.type, object=RDFS.Class, unique=True),
        graph.subjects(predicate=RDF.type, object=RDF.Property, unique=True)
    ):
        _, _, name = graph.compute_qname(cls)
        yield ast.Assign(
            targets=[ast.Name(name)],
            value=ast.Call(
                func=ast.Name("URIRef"),
                args=[ast.Constant(str(cls))],
                keywords=[]
            )
        )

def module_from_rdfs(uris: Iterable[ast.Assign]) -> ast.Module:
    """
    Compiles a Python module from a list of URI assignments
    """
    return ast.fix_missing_locations(ast.Module(
        body=[ast.ImportFrom(module="rdflib", names=[ast.alias(name="URIRef")], level=0)] + list(uris),
        type_ignores=[]
    ))

def module_from_context(context: dict) -> ast.Module:
    """
    Compiles a Python module containing URIs from a JSON-LD context
    """
    body: list[ast.stmt] = [
        ast.ImportFrom(module="rdflib", names=[ast.alias(name="URIRef")], level=0),
    ]
    for key, value in context["@context"].items():
        # Workaround for invalid Python identifiers
        if (not key.isidentifier()) or keyword.iskeyword(key):
            key = "_" + key.replace("-", "_")
        body.append(ast.Assign(
            targets=[ast.Name(key)],
            value=ast.Call(
                func=ast.Name("URIRef"),
                args=[ast.Constant(value)],
                keywords=[]
            )
        ))

    return ast.fix_missing_locations(ast.Module(body=body, type_ignores=[]))
