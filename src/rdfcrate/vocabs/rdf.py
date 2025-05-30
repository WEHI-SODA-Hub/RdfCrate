from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import rdf
from rdfcrate.rdftype import RdfType

class Bag(rdfs.Container):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#Bag', 'Bag')

class Seq(rdfs.Container):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#Seq', 'Seq')

class Alt(rdfs.Container):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#Alt', 'Alt')

class Property(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#Property', 'Property')

class Statement(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement', 'Statement')

class List(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#List', 'List')

class CompoundLiteral(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#CompoundLiteral', 'CompoundLiteral')

class type(RdfProperty[rdfs.Class]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#type', 'type')

class subject(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#subject', 'subject')

class predicate(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate', 'predicate')

class object(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#object', 'object')

class value(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#value', 'value')

class first(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#first', 'first')

class rest(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#rest', 'rest')

class language(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#language', 'language')

class direction(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/1999/02/22-rdf-syntax-ns#direction', 'direction')