from dataclasses import dataclass
from typing import ClassVar, dataclass_transform
from rdflib import URIRef
from rdflib.term import Identifier

from rdfcrate.rdfterm import RdfTerm

@dataclass
class ReverseProperty:
    term: RdfTerm
    subject: URIRef

    def add_to_graph(self, graph, object: URIRef):
        graph.add((self.subject, self.term.uri, object))

@dataclass(frozen=True)
# @dataclass_transform()
class RdfProperty:
    term: ClassVar[RdfTerm]
    object: Identifier

    # def __init__(self, object: Identifier):
    #     self.object = object

    @classmethod
    def reverse(cls, subject: URIRef):
        return ReverseProperty(cls.term, subject)

    def add_to_graph(self, graph, subject: URIRef):
        graph.add((subject, self.term.uri, self.object))
