from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Annotated, ClassVar, Mapping, NewType, Self, TypedDict, cast, get_args

from rdflib import Graph, Literal, URIRef
from rdflib.term import Identifier


class RdfTerm:
    #: The short name of the term
    label: str
    #: The URI of the term
    uri: URIRef

    def __init__(self, label: str, term: str) -> None:
        self.label = label
        self.uri = URIRef(term)

class PropertyList(TypedDict, total=False):
    input: list[input]
    output: list[output]
    # other properties go here

# AMRadioChannel = NewType(URIRefRdfType):
    # class_uri = URIRef("http://schema.org/AMRadioChannel")

type PropertyListBound = Mapping[str, list[RdfType]]
class RdfType[PropertyListType: PropertyListBound](URIRef):
    term: ClassVar[RdfTerm]
    def __new__(
        self,
        # class_uri: URIRef,
        graph: Graph,
        uri: URIRef,
        objects: PropertyListType | None = None,
        subjects: PropertyListType | None = None,
    ) -> Self:
        """
        Params:
            objects: The objects of the triples to be added to the graph. These are the typical properties of the class
            subjects: The subjects of the triples to be added to the graph. These are more like reverse properties, because this class is the object of the triple.
        """
        if objects is not None:
            for key, values in objects.items():
                for value in values:
                    term = value.__metadata__
                    if not isinstance(term, RdfTerm):
                        raise ValueError(f"All values in the property list must be annotated with an RdfTerm. Got {term}")
                    graph.add((uri, term.uri, value))

        if subjects is not None:
            for key, values in subjects.items():
                for value in values:
                    term = value.__metadata__
                    if not isinstance(term, RdfTerm):
                        raise ValueError(f"All values in the property list must be annotated with an RdfTerm. Got {term}")
                    graph.add((value, term.uri, uri))
        
        return super().__new__(cls, uri)
        
class RootDataEntity[T: PropertyListBound](RdfType[T]):
    class_uri = RdfTerm("Dataset", "https://schema.org/Dataset")

class FormalParameter[T: PropertyListBound](RdfType[T]):
    class_uri = RdfTerm("FormalParameter", URIRef("https://bioschemas.org/FormalParameter"))

type input = Annotated[FormalParameter, RdfTerm("input", "https://bioschemas.org/properties/input")]
type output = Annotated[FormalParameter, RdfTerm("output", "https://bioschemas.org/properties/input")]

graph = Graph()

x = RootDataEntity(
    graph,
    URIRef("#bar"),
    objects=PropertyList(
        output=[
            FormalParameter(graph, "#foo")
        ]
    )
)

"""
"""
