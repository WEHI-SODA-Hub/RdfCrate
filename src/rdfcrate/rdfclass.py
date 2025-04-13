from __future__ import annotations
from abc import ABCMeta
from dataclasses import Field, dataclass, field, fields
from enum import Enum
from typing import Annotated, Any, ClassVar, Mapping, NewType, Protocol, Self, TypedDict, cast, get_args, get_type_hints
from typing_extensions import Doc
# from _typeshed import DataclassInstance

from rdflib import Graph, Literal, URIRef, RDF, IdentifiedNode
from rdflib.term import Identifier
from rdfcrate.rdfprop import RdfProperty, ReverseProperty

from rdfcrate.rdfterm import RdfTerm

# class ContextBound(Protocol):
#     # Ideally these would be constrained to `PropertyConstraint`, but Python doesn't seem to support that yet
#     def __getitem__(self, key: str, /) -> object: ...
#     def values(self) -> Iterable[object]: ...

# class PropertyList(Protocol):
#     """
#     A protocol that is satisfied only by dataclasses whose fields are all `list[RdfTerm]`.
#     """
#     __annotations__: dict[str, type[list[RdfType]]]
#     # This is stolen from _typeshed
#     __dataclass_fields__: ClassVar[dict[str, Field[list[RdfType]]]]

# @dataclass
# class RdfTypev2[T: ContextBound]:
#     term: RdfTerm
#     mandatory_properties: type[T]


#     def make(
#         self,
#         graph: Graph,
#         # The new entity always needs a URI
#         uri: URIRef,
#         # Allow implementers to add any other positional arguments, typically for mandatory properties
#         *args: IdentifiedNode,
#         # Objects and subjects are unconstrained, allowing for custom user properties
#         objects: PropertyList | None = None,
#         subjects: PropertyList | None = None,
#         # Allow implementers to add any other keyword arguments, typically for mandatory properties
#         **kwargs: T
#     ) -> URIRef:




# class RdfTypeProto(Protocol):
#     def __new__(
#         cls,
#         # We always need a graph, since we're adding triples to it
#         graph: Graph,
#         # The new entity always needs a URI
#         uri: URIRef,
#         # Allow implementers to add any other positional arguments, typically for mandatory properties
#         *args: IdentifiedNode,
#         # Objects and subjects are unconstrained, allowing for custom user properties
#         objects: PropertyList | None = None,
#         subjects: PropertyList | None = None,
#         # Allow implementers to add any other keyword arguments, typically for mandatory properties
#         **kwargs: IdentifiedNode
#     ) -> URIRef:
#         if not isinstance(cls.term, RdfTerm):
#             raise ValueError("The `term` class variable must be an instance of `RdfTerm`.")
#         graph.add((uri, RDF.type, cls.term.uri))
#         if objects is not None:
#             hints: dict[str, Any] = get_type_hints(objects, localns=globals(), include_extras=True)
#             for field in fields(objects):
#                 values = getattr(objects, field.name)
#                 # Pick the type hint for this field: list[input]
#                 # Pick the first type, using `get_args`, giving `input`
#                 # Evaluate the type alias using `__value))`, giving `Annotated[FormalParameter, RdfTerm()]``
#                 # Extract the annotation with `__metadata__`, giving `(RdfTerm(),)`
#                 # Get the first element of the tuple, giving `RdfTerm()`
#                 term = get_args(hints[field.name])[0].__value__.__metadata__[0]
#                 if not isinstance(term, RdfTerm):
#                     raise ValueError(f"The objects parameter must be a TypedDict whose values are a list of `RdfType`, annotated with an `RdfTerm`.")
#                 if not isinstance(values, list):
#                     raise ValueError(f"All values in the property list must be lists. Got {values}")
#                 for value in values:
#                     graph.add((uri, term.uri, value))

#         if subjects is not None:
#             for key, values in subjects.items():
#                 for value in values:
#                     term = value.__metadata__
#                     if not isinstance(term, RdfTerm):
#                         raise ValueError(f"All values in the property list must be annotated with an RdfTerm. Got {term}")
#                     graph.add((value, term.uri, uri))
        
#         return super().__new__(cls, uri)

class RdfClassMeta(ABCMeta):
    """
    Metaclass which picks the first base class of the class being created.
    This is needed to avoid the MRO issues with multiple inheritance, which we aren't actually using for method resolution.
    Its only purpose is static type checking
    """
    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any], /, **kwargs: Any):
        if len(bases) > 1:
            bases = (bases[0],)
        return super().__new__(mcls, name, bases, namespace, **kwargs)

type EntityUri = Annotated[str, Doc("The identifier of the new entity. This must be a valid IRI or a relative path within the crate root.")]
type EntityArgs = Annotated[RdfProperty | ReverseProperty, Doc("Additional properties to add to the entity. Instances of `RdfProperty` will create triples with this new entity as the subject. Instances of `ReverseProperty` will create triples with this new entity as the object.")]

class RdfClass(URIRef, metaclass=RdfClassMeta):
    """
    A class that represents an RDF type.
    """
    term: ClassVar[RdfTerm]

    @classmethod
    def add(
        cls,
        graph: Graph,
        uri: EntityUri,
        *args: EntityArgs
    ) -> Self:
        """
        Creates a new entity in the graph with the given URI and adds triples to it.

        Params:
            graph: The graph to which the triples will be added
        Returns:
            A URIRef subclass for this RDF type
        """
        # if not isinstance(uri, IdentifiedNode):
        #     # Assume that the identifier is a URI
        uri = cls(uri)
        if not isinstance(cls.term, RdfTerm):
            raise ValueError("The `term` class variable must be an instance of `RdfTerm`.")
        graph.add((uri, RDF.type, cls.term.uri))
        for arg in args:
            arg.add_to_graph(graph, uri)
        
        # See https://github.com/RDFLib/rdflib/issues/3107
        return super().__new__(cls, uri) # type: ignore

    def __new__(cls, uri: str) -> Self:
        """
        Casts the given URI to the class type.
        """
        return cast(Self, super().__new__(cls, uri))
        