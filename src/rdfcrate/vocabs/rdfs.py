from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs

class Resource(RdfClass):
    term = RdfTerm('Resource', 'http://www.w3.org/2000/01/rdf-schema#Resource', [])

class ContainerMembershipProperty(RdfClass):
    term = RdfTerm('ContainerMembershipProperty', 'http://www.w3.org/2000/01/rdf-schema#ContainerMembershipProperty', [])

class Class(Resource):
    term = RdfTerm('Class', 'http://www.w3.org/2000/01/rdf-schema#Class', [])

class Literal(Resource):
    term = RdfTerm('Literal', 'http://www.w3.org/2000/01/rdf-schema#Literal', [])

class Container(Resource):
    term = RdfTerm('Container', 'http://www.w3.org/2000/01/rdf-schema#Container', [])

class Datatype(Class):
    term = RdfTerm('Datatype', 'http://www.w3.org/2000/01/rdf-schema#Datatype', [])

class subClassOf(RdfProperty[rdfs.Class]):
    term = RdfTerm('subClassOf', 'http://www.w3.org/2000/01/rdf-schema#subClassOf', [])

class subPropertyOf(RdfProperty[Identifier]):
    term = RdfTerm('subPropertyOf', 'http://www.w3.org/2000/01/rdf-schema#subPropertyOf', [])

class comment(RdfProperty[rdfs.Literal]):
    term = RdfTerm('comment', 'http://www.w3.org/2000/01/rdf-schema#comment', [])

class label(RdfProperty[rdfs.Literal]):
    term = RdfTerm('label', 'http://www.w3.org/2000/01/rdf-schema#label', [])

class domain(RdfProperty[rdfs.Class]):
    term = RdfTerm('domain', 'http://www.w3.org/2000/01/rdf-schema#domain', [])

class range(RdfProperty[rdfs.Class]):
    term = RdfTerm('range', 'http://www.w3.org/2000/01/rdf-schema#range', [])

class seeAlso(RdfProperty[rdfs.Resource]):
    term = RdfTerm('seeAlso', 'http://www.w3.org/2000/01/rdf-schema#seeAlso', [])

class isDefinedBy(RdfProperty[rdfs.Resource]):
    term = RdfTerm('isDefinedBy', 'http://www.w3.org/2000/01/rdf-schema#isDefinedBy', [])

class member(RdfProperty[rdfs.Resource]):
    term = RdfTerm('member', 'http://www.w3.org/2000/01/rdf-schema#member', [])