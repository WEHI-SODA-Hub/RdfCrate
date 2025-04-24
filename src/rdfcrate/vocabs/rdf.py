from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import rdf


class Bag(rdfs.Container):
    term = RdfTerm("Bag", "http://www.w3.org/1999/02/22-rdf-syntax-ns#Bag", [])


class Seq(rdfs.Container):
    term = RdfTerm("Seq", "http://www.w3.org/1999/02/22-rdf-syntax-ns#Seq", [])


class Alt(rdfs.Container):
    term = RdfTerm("Alt", "http://www.w3.org/1999/02/22-rdf-syntax-ns#Alt", [])


class Property(rdfs.Resource):
    term = RdfTerm(
        "Property", "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property", []
    )


class Statement(rdfs.Resource):
    term = RdfTerm(
        "Statement", "http://www.w3.org/1999/02/22-rdf-syntax-ns#Statement", []
    )


class List(rdfs.Resource):
    term = RdfTerm("List", "http://www.w3.org/1999/02/22-rdf-syntax-ns#List", [])


class CompoundLiteral(rdfs.Resource):
    term = RdfTerm(
        "CompoundLiteral",
        "http://www.w3.org/1999/02/22-rdf-syntax-ns#CompoundLiteral",
        [],
    )


class type(RdfProperty[rdfs.Class]):
    term = RdfTerm("type", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", [])


class subject(RdfProperty[rdfs.Resource]):
    term = RdfTerm("subject", "http://www.w3.org/1999/02/22-rdf-syntax-ns#subject", [])


class predicate(RdfProperty[rdfs.Resource]):
    term = RdfTerm(
        "predicate", "http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate", []
    )


class object(RdfProperty[rdfs.Resource]):
    term = RdfTerm("object", "http://www.w3.org/1999/02/22-rdf-syntax-ns#object", [])


class value(RdfProperty[rdfs.Resource]):
    term = RdfTerm("value", "http://www.w3.org/1999/02/22-rdf-syntax-ns#value", [])


class first(RdfProperty[rdfs.Resource]):
    term = RdfTerm("first", "http://www.w3.org/1999/02/22-rdf-syntax-ns#first", [])


class rest(RdfProperty[rdf.List]):
    term = RdfTerm("rest", "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest", [])


class language(RdfProperty[Identifier]):
    term = RdfTerm(
        "language", "http://www.w3.org/1999/02/22-rdf-syntax-ns#language", []
    )


class direction(RdfProperty[Identifier]):
    term = RdfTerm(
        "direction", "http://www.w3.org/1999/02/22-rdf-syntax-ns#direction", []
    )
