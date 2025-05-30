from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs
from rdfcrate.rdftype import RdfType


class Resource(RdfClass):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Resource", "Resource")


class ContainerMembershipProperty(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2000/01/rdf-schema#ContainerMembershipProperty",
        "ContainerMembershipProperty",
    )


class Class(Resource):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Class", "Class")


class Literal(Resource):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Literal", "Literal")


class Container(Resource):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Container", "Container")


class Datatype(Class):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Datatype", "Datatype")


class subClassOf(RdfProperty[rdfs.Class]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#subClassOf", "subClassOf")


class subPropertyOf(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2000/01/rdf-schema#subPropertyOf", "subPropertyOf"
    )


class comment(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#comment", "comment")


class label(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#label", "label")


class domain(RdfProperty[rdfs.Class]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#domain", "domain")


class range(RdfProperty[rdfs.Class]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#range", "range")


class seeAlso(RdfProperty[rdfs.Resource]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#seeAlso", "seeAlso")


class isDefinedBy(RdfProperty[rdfs.Resource]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#isDefinedBy", "isDefinedBy")


class member(RdfProperty[rdfs.Resource]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#member", "member")
