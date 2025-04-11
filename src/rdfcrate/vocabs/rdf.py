from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import rdf

class Bag(rdfs.Container):
    term = RdfTerm('Bag', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Bag', [])

class Seq(rdfs.Container):
    term = RdfTerm('Seq', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Seq', [])

class Alt(rdfs.Container):
    term = RdfTerm('Alt', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Alt', [])

class Property(rdfs.Resource):
    term = RdfTerm('Property', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property', [])

class Statement(rdfs.Resource):
    term = RdfTerm('Statement', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement', [])

class List(rdfs.Resource):
    term = RdfTerm('List', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#List', [])

class CompoundLiteral(rdfs.Resource):
    term = RdfTerm('CompoundLiteral', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#CompoundLiteral', [])

@dataclass(frozen=True)
class type(RdfProperty):
    term = RdfTerm('type', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type', [])
    object: rdfs.Class

@dataclass(frozen=True)
class subject(RdfProperty):
    term = RdfTerm('subject', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#subject', [])
    object: rdfs.Resource

@dataclass(frozen=True)
class predicate(RdfProperty):
    term = RdfTerm('predicate', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate', [])
    object: rdfs.Resource

@dataclass(frozen=True)
class object(RdfProperty):
    term = RdfTerm('object', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#object', [])
    object: rdfs.Resource

@dataclass(frozen=True)
class value(RdfProperty):
    term = RdfTerm('value', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#value', [])
    object: rdfs.Resource

@dataclass(frozen=True)
class first(RdfProperty):
    term = RdfTerm('first', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#first', [])
    object: rdfs.Resource

@dataclass(frozen=True)
class rest(RdfProperty):
    term = RdfTerm('rest', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#rest', [])
    object: rdf.List

@dataclass(frozen=True)
class language(RdfProperty):
    term = RdfTerm('language', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#language', [])
    object: Identifier

@dataclass(frozen=True)
class direction(RdfProperty):
    term = RdfTerm('direction', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#direction', [])
    object: Identifier