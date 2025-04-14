from dataclasses import dataclass
from typing import ClassVar, dataclass_transform
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


@dataclass(frozen=True)
class RdfProperty:
    """
    Represents the double of (predicate, object), with the subject being the class this is attached to.
    This is the normal way properties will be defined
    """

    term: ClassVar[RdfTerm]
    object: Identifier

    @classmethod
    def reverse(cls, subject: URIRef):
        return ReverseProperty(cls.term, subject)

    def add_to_graph(self, graph, subject: URIRef):
        graph.add((subject, self.term.uri, self.object))
