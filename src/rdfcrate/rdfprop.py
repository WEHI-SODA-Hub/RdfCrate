from dataclasses import dataclass
from typing import ClassVar, Generic, TypeVar
from rdflib import URIRef
from rdflib.term import Identifier

from rdfcrate.rdfterm import RdfTerm


@dataclass
class ReverseProperty:
    """
    Represents the double of (subject, predicate), with the object being the class this is attached to.
    """

    term: RdfTerm
    subject: URIRef

    def add_to_graph(self, graph, object: URIRef):
        graph.add((self.subject, self.term.uri, object))


T = TypeVar("T", bound=Identifier)


@dataclass(frozen=True)
class RdfProperty(Generic[T]):
    """
    Represents the double of (predicate, object), with the subject being the class this is attached to.
    This is the normal way properties will be defined
    """

    term: ClassVar[RdfTerm]
    object: T

    @classmethod
    def reverse(cls, subject: URIRef):
        return ReverseProperty(cls.term, subject)

    def add_to_graph(self, graph, subject: URIRef):
        graph.add((subject, self.term.uri, self.object))
