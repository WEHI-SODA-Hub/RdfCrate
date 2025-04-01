from __future__ import annotations
from dataclasses import Field, dataclass, field, fields
from enum import Enum
from typing import Annotated, Any, ClassVar, Mapping, NewType, Protocol, Self, TypedDict, cast, get_args, get_type_hints
# from _typeshed import DataclassInstance

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

class PropertyList(Protocol):
    """
    A protocol that is satisfied only by dataclasses whose fields are all `list[RdfTerm]`.
    """
    __annotations__: dict[str, type[list[RdfType]]]
    # This is stolen from _typeshed
    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]

@dataclass
class Bioschemas:
    # This has to be a dataclass and not a TypedDict because we need to be able to get the type hints at runtime
    input: list[input] = field(default_factory=list)
    output: list[output] = field(default_factory=list)
    # other properties go here


# AMRadioChannel = NewType(URIRefRdfType):
    # class_uri = URIRef("http://schema.org/AMRadioChannel")

type PropertyListBound = Mapping[str, Any]
class RdfType(URIRef):
    term: ClassVar[RdfTerm]
    def __new__(
        cls,
        # class_uri: URIRef,
        graph: Graph,
        uri: URIRef,
        objects: PropertyList | None = None,
        subjects: PropertyList | None = None,
    ) -> Self:
        """
        Params:
            objects: The objects of the triples to be added to the graph. These are the typical properties of the class
            subjects: The subjects of the triples to be added to the graph. These are more like reverse properties, because this class is the object of the triple.
        """
        if objects is not None:
            hints = get_type_hints(objects, localns=globals(), include_extras=True)
            for field in fields(objects):
                values = getattr(objects, field.name)
                term = hints[field.name].__metadata__
                if not isinstance(term, RdfTerm):
                    raise ValueError(f"The objects parameter must be a TypedDict whose values are a list of `RdfType`, annotated with an `RdfTerm`.")
                if not isinstance(values, list):
                    raise ValueError(f"All values in the property list must be lists. Got {values}")
                for value in values:
                    graph.add((uri, term.uri, value))

        if subjects is not None:
            for key, values in subjects.items():
                for value in values:
                    term = value.__metadata__
                    if not isinstance(term, RdfTerm):
                        raise ValueError(f"All values in the property list must be annotated with an RdfTerm. Got {term}")
                    graph.add((value, term.uri, uri))
        
        return super().__new__(cls, uri)
        
class RootDataEntity(RdfType):
    class_uri = RdfTerm("Dataset", "https://schema.org/Dataset")

class FormalParameter(RdfType):
    class_uri = RdfTerm("FormalParameter", URIRef("https://bioschemas.org/FormalParameter"))

type input = Annotated[FormalParameter, RdfTerm("input", "https://bioschemas.org/properties/input")]
type output = Annotated[FormalParameter, RdfTerm("output", "https://bioschemas.org/properties/input")]

graph = Graph()

# y = FormalParameter(graph, URIRef("#foo"))
x = RootDataEntity(
    graph,
    URIRef("#bar"),
    objects=Bioschemas(
        output=[
            FormalParameter(graph, URIRef("#foo"))
        ]
    )
)

# class Foo(TypedDict):
#     bar: str
#     baz: str

# def bar(x: dict[str, str]): pass

# bar(Foo())
