from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, Generic, TypeVar, TYPE_CHECKING
from rdflib import Graph

from rdfcrate.rdfterm import RdfTerm
from rdfcrate.types import GraphId

if TYPE_CHECKING:
    from rdfcrate.rdftype import RdfType


@dataclass
class ReverseProperty:
    """
    Represents the double of (subject, predicate), with the object being the class this is attached to.
    """

    term: RdfTerm
    subject: RdfType

    def add_to_graph(self, graph: Graph, object: GraphId) -> None:
        graph.add((self.subject.id, self.term.uri, object))


T = TypeVar("T", bound="RdfType")


@dataclass(frozen=True)
class RdfProperty(Generic[T]):
    """
    Represents the double of (predicate, object), with the subject being the class this is attached to.
    This is the normal way properties will be defined
    """

    term: ClassVar[RdfTerm]
    object: T

    @classmethod
    def reverse(cls, subject: RdfType) -> ReverseProperty:
        return ReverseProperty(cls.term, subject)

    def add_to_graph(self, graph: Graph, subject: GraphId) -> None:
        graph.add((subject, self.term.uri, self.object.id))
