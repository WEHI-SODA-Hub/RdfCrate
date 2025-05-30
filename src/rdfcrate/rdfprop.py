from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, Generic, TypeVar, TYPE_CHECKING
from rdflib import Graph

from rdfcrate.rdfterm import RdfTerm
from rdfcrate.types import GraphId

if TYPE_CHECKING:
    from rdfcrate.rdftype import RdfClass

@dataclass
class ReverseProperty:
    """
    Represents the double of (subject, predicate), with the object being the class this is attached to.
    """

    term: RdfTerm
    subject: GraphId

    def add_to_graph(self, graph, object: GraphId) -> None:
        graph.add((self.subject, self.term.uri, object))


T = TypeVar("T", bound="RdfClass")


@dataclass(frozen=True)
class RdfProperty(Generic[T]):
    """
    Represents the double of (predicate, object), with the subject being the class this is attached to.
    This is the normal way properties will be defined
    """

    term: ClassVar[RdfTerm]
    object: T

    @classmethod
    def reverse(cls, subject: GraphId) -> ReverseProperty:
        return ReverseProperty(cls.term, subject)

    def add_to_graph(self, graph: Graph, subject: GraphId) -> None:
        graph.add((subject, self.term.uri, self.object.id))
