from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs


class Resource(RdfClass):
    term = RdfTerm("Resource", "http://www.w3.org/2000/01/rdf-schema#Resource", [])


class ContainerMembershipProperty(RdfClass):
    term = RdfTerm(
        "ContainerMembershipProperty",
        "http://www.w3.org/2000/01/rdf-schema#ContainerMembershipProperty",
        [],
    )


class Class(Resource):
    term = RdfTerm("Class", "http://www.w3.org/2000/01/rdf-schema#Class", [])


class Literal(Resource):
    term = RdfTerm("Literal", "http://www.w3.org/2000/01/rdf-schema#Literal", [])


class Container(Resource):
    term = RdfTerm("Container", "http://www.w3.org/2000/01/rdf-schema#Container", [])


class Datatype(Class):
    term = RdfTerm("Datatype", "http://www.w3.org/2000/01/rdf-schema#Datatype", [])


class Class(Class):
    term = RdfTerm("Class", "http://www.w3.org/2002/07/owl#Class", [])


@dataclass(frozen=True)
class subClassOf(RdfProperty):
    term = RdfTerm("subClassOf", "http://www.w3.org/2000/01/rdf-schema#subClassOf", [])
    object: rdfs.Class


@dataclass(frozen=True)
class subPropertyOf(RdfProperty):
    term = RdfTerm(
        "subPropertyOf", "http://www.w3.org/2000/01/rdf-schema#subPropertyOf", []
    )
    object: Identifier


@dataclass(frozen=True)
class comment(RdfProperty):
    term = RdfTerm("comment", "http://www.w3.org/2000/01/rdf-schema#comment", [])
    object: rdfs.Literal


@dataclass(frozen=True)
class label(RdfProperty):
    term = RdfTerm("label", "http://www.w3.org/2000/01/rdf-schema#label", [])
    object: rdfs.Literal


@dataclass(frozen=True)
class domain(RdfProperty):
    term = RdfTerm("domain", "http://www.w3.org/2000/01/rdf-schema#domain", [])
    object: rdfs.Class


@dataclass(frozen=True)
class range(RdfProperty):
    term = RdfTerm("range", "http://www.w3.org/2000/01/rdf-schema#range", [])
    object: rdfs.Class


@dataclass(frozen=True)
class seeAlso(RdfProperty):
    term = RdfTerm("seeAlso", "http://www.w3.org/2000/01/rdf-schema#seeAlso", [])
    object: rdfs.Resource


@dataclass(frozen=True)
class isDefinedBy(RdfProperty):
    term = RdfTerm(
        "isDefinedBy", "http://www.w3.org/2000/01/rdf-schema#isDefinedBy", []
    )
    object: rdfs.Resource


@dataclass(frozen=True)
class member(RdfProperty):
    term = RdfTerm("member", "http://www.w3.org/2000/01/rdf-schema#member", [])
    object: rdfs.Resource
