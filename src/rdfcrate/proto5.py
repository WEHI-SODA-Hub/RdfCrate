from __future__ import annotations
from dataclasses import Field, dataclass, field, fields
from enum import Enum
from typing import Annotated, Any, ClassVar, Mapping, NewType, Protocol, Self, TypedDict, cast, get_args, get_type_hints
# from _typeshed import DataclassInstance

from rdflib import Graph, Literal, URIRef, RDF
from rdflib.term import Identifier

from rdfcrate.property_list import PropertyList, RdfType
from rdfcrate.rdfterm import RdfTerm


@dataclass
class Bioschemas:
    # This has to be a dataclass and not a TypedDict because we need to be able to get the type hints at runtime from an instance of this class.
    # TypedDicts instances aren't connected to their class at runtime.
    input: list[input] = field(default_factory=list)
    output: list[output] = field(default_factory=list)
    # other properties go here


# AMRadioChannel = NewType(URIRefRdfType):
    # class_uri = URIRef("http://schema.org/AMRadioChannel")

# class RootDataEntity(RdfType):
#     class Fields(Protocol):
#         name: 

#     term = RdfTerm("Dataset", "https://schema.org/Dataset")

class FormalParameter(RdfType):
    term = RdfTerm("FormalParameter", URIRef("https://bioschemas.org/FormalParameter"))

class ComputationalWorkflowFields(PropertyList, Protocol):
    input: input
    output: output

class ComputationalWorkflow(RdfType[ComputationalWorkflowFields]):
    term = RdfTerm("ComputationalWorkflow", URIRef("https://bioschemas.org/ComputationalWorkflow"))

type input = Annotated[FormalParameter, RdfTerm("input", "https://bioschemas.org/properties/input")]
type output = Annotated[FormalParameter, RdfTerm("output", "https://bioschemas.org/properties/input")]

graph = Graph()

x = ComputationalWorkflow(
    graph,
    URIRef("#foo"),
    objects=Bioschemas(
        input=[
            FormalParameter(graph, URIRef("#bar"))
        ]
    )
)
# y = FormalParameter(graph, URIRef("#foo"))
# x = RootDataEntity(
#     graph,
#     URIRef("#bar"),
#     objects=Bioschemas(
#         output=[
#             FormalParameter(graph, URIRef("#foo"))
#         ]
#     )
# )
print(x)

# class Foo(TypedDict):
#     bar: str
#     baz: str

# def bar(x: dict[str, str]): pass

# bar(Foo())
