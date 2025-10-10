from typing import Annotated, Iterable, Protocol, TypedDict

from rdflib import Graph, URIRef, Literal, IdentifiedNode, RDF

from rdfcrate.rdfterm import RdfTerm


type PropertyConstraint = list[IdentifiedNode]


class ContextBound(Protocol):
    # Ideally these would be constrained to `PropertyConstraint`, but Python doesn't seem to support that yet
    def __getitem__(self, key: str, /) -> object: ...
    def values(self) -> Iterable[object]: ...


# Parameterising the class with a TypedDict allows users to define their own custom properties without needing to subclass.
# Using a TypedDict rather than a `dict[RdfTerm, IdentifiedNode]` means we can make specific properties mandatory and enforce types.
class RoCrate[T: ContextBound]:
    graph: Graph
    context: type[T]

    def __init__(self, context: type[T]):
        # Saving the context as a class variable allows us to query the Annotated[] fields later
        self.context = context

    # Parameterised by the URIType, which is a subclass of URIRef.
    # These subclasses can be for a specific RDF type, which then allows us to constrain the property list to only allow certain type ranges.
    # Alternatively, we can constrain the RDF types using the method signature
    def add_entity[URIType: URIRef](
        self,
        uri: URIType,
        # We can enforce certain mandatory properties by adding them to the method signature
        # In theory, subclasses could override this to add new constraints
        type: Annotated[list[URIRef], RdfTerm("type", RDF.type)],
        name: Annotated[Literal, RdfTerm("name", "https://schema.org/name")],
        description: Annotated[Literal, RdfTerm("name", "https://schema.org/name")],
        # Optional properties are user defined. We can't merge this with the mandatory properties because of https://typing.python.org/en/latest/spec/callables.html#keyword-collisions.
        # Intersection types would also solve this problem, but they are not yet supported in Python.
        objects: T,
        subjects: T,
    ) -> URIType: ...


class Context(TypedDict):
    name: PropertyConstraint


x = RoCrate[Context](Context)
