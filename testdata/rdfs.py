from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from . import rdfs
from rdfcrate.rdftype import RdfType


class Resource(RdfClass):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Resource", "Resource")


class Containermembershipproperty(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2000/01/rdf-schema#ContainerMembershipProperty",
        "Containermembershipproperty",
    )


class Class(Resource):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Class", "Class")


class Literal(Resource):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Literal", "Literal")


class Container(Resource):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Container", "Container")


class Datatype(Class):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#Datatype", "Datatype")


class Subclassof(RdfProperty[rdfs.Class]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#subClassOf", "Subclassof")


class Subpropertyof(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2000/01/rdf-schema#subPropertyOf", "Subpropertyof"
    )


class Comment(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#comment", "Comment")


class Label(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#label", "Label")


class Domain(RdfProperty[rdfs.Class]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#domain", "Domain")


class Range(RdfProperty[rdfs.Class]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#range", "Range")


class Seealso(RdfProperty[rdfs.Resource]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#seeAlso", "Seealso")


class Isdefinedby(RdfProperty[rdfs.Resource]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#isDefinedBy", "Isdefinedby")


class Member(RdfProperty[rdfs.Resource]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#member", "Member")
