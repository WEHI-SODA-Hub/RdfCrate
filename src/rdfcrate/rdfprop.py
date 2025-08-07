from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, Generic, TypeVar, TYPE_CHECKING
from typing_extensions import Protocol
from rdflib import RDF

from rdfcrate.rdfterm import RdfTerm
from rdfcrate.types import GraphId

if TYPE_CHECKING:
    from rdfcrate.rdftype import RdfType
    from rdfcrate.context_graph import ContextGraph

T = TypeVar("T", bound="RdfType", covariant=True)

class PropertyProtocol(Protocol):
    def add_to_graph(self, graph: ContextGraph, entity: GraphId):
        """
        Adds the property to the graph and registers any terms if necessary.

        Params:
            graph: The graph to which the property will be added
            entity: The entity to which the property will be added
        """

@dataclass(frozen=True)
class RdfProperty(PropertyProtocol, Generic[T]):
    """
    Represents the double of (predicate, object), with the subject being the class this is attached to.
    This is the normal way properties will be defined
    """

    term: ClassVar[RdfTerm]
    object: T

    @staticmethod
    def adhoc(term: RdfTerm, object: T) -> RdfProperty:
        """
        Makes an ad-hoc property class from a term.
        """
        subclass = type(term.label, (RdfProperty,), {"term": term})
        return subclass(object=object)

    @classmethod
    def reverse(cls, subject: RdfType) -> ReverseProperty:
        return ReverseProperty(cls.term, subject)

    @classmethod
    def with_term_label(cls, label: str) -> type[RdfProperty[T]]:
        """
        Creates a new instance of this property with the given label.
        This is useful in cases where the term label is already defined by another vocabulary
        """
        from rdfcrate import RdfTerm

        # Create a new term with the given label
        term = RdfTerm(cls.term.uri, label)
        return type(cls.__name__, (cls,), {"term": term})

    def add_to_graph(self, graph: ContextGraph, entity: GraphId) -> None:
        graph.register_term(self.term)
        if self.term.uri == RDF.type:
            # rdf:type is a special case, it should not be registered as a term
            graph.register_term(self.object.term)
        graph.graph.add((entity, self.term.uri, self.object.id))

@dataclass
class ReverseProperty(PropertyProtocol):
    """
    Represents the double of (subject, predicate), with the object being the class this is attached to.
    """

    term: RdfTerm
    subject: RdfType

    def add_to_graph(self, graph: ContextGraph, entity: GraphId) -> None:
        graph.register_term(self.term)
        graph.graph.add((self.subject.id, self.term.uri, entity))
