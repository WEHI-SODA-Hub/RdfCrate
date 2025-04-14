from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import rdf
from rdfcrate.vocabs import owl


class DataRange(rdfs.Datatype):
    term = RdfTerm("DataRange", "http://www.w3.org/2002/07/owl#DataRange", [])


class Restriction(rdfs.Class):
    term = RdfTerm("Restriction", "http://www.w3.org/2002/07/owl#Restriction", [])


class DeprecatedClass(rdfs.Class):
    term = RdfTerm(
        "DeprecatedClass", "http://www.w3.org/2002/07/owl#DeprecatedClass", []
    )


class AnnotationProperty(rdf.Property):
    term = RdfTerm(
        "AnnotationProperty", "http://www.w3.org/2002/07/owl#AnnotationProperty", []
    )


class DatatypeProperty(rdf.Property):
    term = RdfTerm(
        "DatatypeProperty", "http://www.w3.org/2002/07/owl#DatatypeProperty", []
    )


class DeprecatedProperty(rdf.Property):
    term = RdfTerm(
        "DeprecatedProperty", "http://www.w3.org/2002/07/owl#DeprecatedProperty", []
    )


class FunctionalProperty(rdf.Property):
    term = RdfTerm(
        "FunctionalProperty", "http://www.w3.org/2002/07/owl#FunctionalProperty", []
    )


class ObjectProperty(rdf.Property):
    term = RdfTerm("ObjectProperty", "http://www.w3.org/2002/07/owl#ObjectProperty", [])


class OntologyProperty(rdf.Property):
    term = RdfTerm(
        "OntologyProperty", "http://www.w3.org/2002/07/owl#OntologyProperty", []
    )


class AllDifferent(rdfs.Resource):
    term = RdfTerm("AllDifferent", "http://www.w3.org/2002/07/owl#AllDifferent", [])


class AllDisjointClasses(rdfs.Resource):
    term = RdfTerm(
        "AllDisjointClasses", "http://www.w3.org/2002/07/owl#AllDisjointClasses", []
    )


class AllDisjointProperties(rdfs.Resource):
    term = RdfTerm(
        "AllDisjointProperties",
        "http://www.w3.org/2002/07/owl#AllDisjointProperties",
        [],
    )


class Annotation(rdfs.Resource):
    term = RdfTerm("Annotation", "http://www.w3.org/2002/07/owl#Annotation", [])


class Axiom(rdfs.Resource):
    term = RdfTerm("Axiom", "http://www.w3.org/2002/07/owl#Axiom", [])


class NegativePropertyAssertion(rdfs.Resource):
    term = RdfTerm(
        "NegativePropertyAssertion",
        "http://www.w3.org/2002/07/owl#NegativePropertyAssertion",
        [],
    )


class Ontology(rdfs.Resource):
    term = RdfTerm("Ontology", "http://www.w3.org/2002/07/owl#Ontology", [])


class NamedIndividual(RdfClass):
    term = RdfTerm(
        "NamedIndividual", "http://www.w3.org/2002/07/owl#NamedIndividual", []
    )


class AsymmetricProperty(ObjectProperty):
    term = RdfTerm(
        "AsymmetricProperty", "http://www.w3.org/2002/07/owl#AsymmetricProperty", []
    )


class InverseFunctionalProperty(ObjectProperty):
    term = RdfTerm(
        "InverseFunctionalProperty",
        "http://www.w3.org/2002/07/owl#InverseFunctionalProperty",
        [],
    )


class IrreflexiveProperty(ObjectProperty):
    term = RdfTerm(
        "IrreflexiveProperty", "http://www.w3.org/2002/07/owl#IrreflexiveProperty", []
    )


class ReflexiveProperty(ObjectProperty):
    term = RdfTerm(
        "ReflexiveProperty", "http://www.w3.org/2002/07/owl#ReflexiveProperty", []
    )


class SymmetricProperty(ObjectProperty):
    term = RdfTerm(
        "SymmetricProperty", "http://www.w3.org/2002/07/owl#SymmetricProperty", []
    )


class TransitiveProperty(ObjectProperty):
    term = RdfTerm(
        "TransitiveProperty", "http://www.w3.org/2002/07/owl#TransitiveProperty", []
    )


@dataclass(frozen=True)
class allValuesFrom(RdfProperty):
    term = RdfTerm("allValuesFrom", "http://www.w3.org/2002/07/owl#allValuesFrom", [])
    object: rdfs.Class


@dataclass(frozen=True)
class annotatedProperty(RdfProperty):
    term = RdfTerm(
        "annotatedProperty", "http://www.w3.org/2002/07/owl#annotatedProperty", []
    )
    object: rdfs.Resource


@dataclass(frozen=True)
class annotatedSource(RdfProperty):
    term = RdfTerm(
        "annotatedSource", "http://www.w3.org/2002/07/owl#annotatedSource", []
    )
    object: rdfs.Resource


@dataclass(frozen=True)
class annotatedTarget(RdfProperty):
    term = RdfTerm(
        "annotatedTarget", "http://www.w3.org/2002/07/owl#annotatedTarget", []
    )
    object: rdfs.Resource


@dataclass(frozen=True)
class assertionProperty(RdfProperty):
    term = RdfTerm(
        "assertionProperty", "http://www.w3.org/2002/07/owl#assertionProperty", []
    )
    object: rdf.Property


@dataclass(frozen=True)
class cardinality(RdfProperty):
    term = RdfTerm("cardinality", "http://www.w3.org/2002/07/owl#cardinality", [])
    object: Identifier


@dataclass(frozen=True)
class complementOf(RdfProperty):
    term = RdfTerm("complementOf", "http://www.w3.org/2002/07/owl#complementOf", [])
    object: rdfs.Class


@dataclass(frozen=True)
class datatypeComplementOf(RdfProperty):
    term = RdfTerm(
        "datatypeComplementOf", "http://www.w3.org/2002/07/owl#datatypeComplementOf", []
    )
    object: rdfs.Datatype


@dataclass(frozen=True)
class differentFrom(RdfProperty):
    term = RdfTerm("differentFrom", "http://www.w3.org/2002/07/owl#differentFrom", [])
    object: Identifier


@dataclass(frozen=True)
class disjointUnionOf(RdfProperty):
    term = RdfTerm(
        "disjointUnionOf", "http://www.w3.org/2002/07/owl#disjointUnionOf", []
    )
    object: rdf.List


@dataclass(frozen=True)
class disjointWith(RdfProperty):
    term = RdfTerm("disjointWith", "http://www.w3.org/2002/07/owl#disjointWith", [])
    object: rdfs.Class


@dataclass(frozen=True)
class distinctMembers(RdfProperty):
    term = RdfTerm(
        "distinctMembers", "http://www.w3.org/2002/07/owl#distinctMembers", []
    )
    object: rdf.List


@dataclass(frozen=True)
class equivalentClass(RdfProperty):
    term = RdfTerm(
        "equivalentClass", "http://www.w3.org/2002/07/owl#equivalentClass", []
    )
    object: rdfs.Class


@dataclass(frozen=True)
class equivalentProperty(RdfProperty):
    term = RdfTerm(
        "equivalentProperty", "http://www.w3.org/2002/07/owl#equivalentProperty", []
    )
    object: rdf.Property


@dataclass(frozen=True)
class hasKey(RdfProperty):
    term = RdfTerm("hasKey", "http://www.w3.org/2002/07/owl#hasKey", [])
    object: rdf.List


@dataclass(frozen=True)
class hasSelf(RdfProperty):
    term = RdfTerm("hasSelf", "http://www.w3.org/2002/07/owl#hasSelf", [])
    object: rdfs.Resource


@dataclass(frozen=True)
class hasValue(RdfProperty):
    term = RdfTerm("hasValue", "http://www.w3.org/2002/07/owl#hasValue", [])
    object: rdfs.Resource


@dataclass(frozen=True)
class intersectionOf(RdfProperty):
    term = RdfTerm("intersectionOf", "http://www.w3.org/2002/07/owl#intersectionOf", [])
    object: rdf.List


@dataclass(frozen=True)
class inverseOf(RdfProperty):
    term = RdfTerm("inverseOf", "http://www.w3.org/2002/07/owl#inverseOf", [])
    object: owl.ObjectProperty


@dataclass(frozen=True)
class maxCardinality(RdfProperty):
    term = RdfTerm("maxCardinality", "http://www.w3.org/2002/07/owl#maxCardinality", [])
    object: Identifier


@dataclass(frozen=True)
class maxQualifiedCardinality(RdfProperty):
    term = RdfTerm(
        "maxQualifiedCardinality",
        "http://www.w3.org/2002/07/owl#maxQualifiedCardinality",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class members(RdfProperty):
    term = RdfTerm("members", "http://www.w3.org/2002/07/owl#members", [])
    object: rdf.List


@dataclass(frozen=True)
class minCardinality(RdfProperty):
    term = RdfTerm("minCardinality", "http://www.w3.org/2002/07/owl#minCardinality", [])
    object: Identifier


@dataclass(frozen=True)
class minQualifiedCardinality(RdfProperty):
    term = RdfTerm(
        "minQualifiedCardinality",
        "http://www.w3.org/2002/07/owl#minQualifiedCardinality",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class onClass(RdfProperty):
    term = RdfTerm("onClass", "http://www.w3.org/2002/07/owl#onClass", [])
    object: rdfs.Class


@dataclass(frozen=True)
class onDataRange(RdfProperty):
    term = RdfTerm("onDataRange", "http://www.w3.org/2002/07/owl#onDataRange", [])
    object: rdfs.Datatype


@dataclass(frozen=True)
class onDatatype(RdfProperty):
    term = RdfTerm("onDatatype", "http://www.w3.org/2002/07/owl#onDatatype", [])
    object: rdfs.Datatype


@dataclass(frozen=True)
class oneOf(RdfProperty):
    term = RdfTerm("oneOf", "http://www.w3.org/2002/07/owl#oneOf", [])
    object: rdf.List


@dataclass(frozen=True)
class onProperties(RdfProperty):
    term = RdfTerm("onProperties", "http://www.w3.org/2002/07/owl#onProperties", [])
    object: rdf.List


@dataclass(frozen=True)
class onProperty(RdfProperty):
    term = RdfTerm("onProperty", "http://www.w3.org/2002/07/owl#onProperty", [])
    object: rdf.Property


@dataclass(frozen=True)
class propertyChainAxiom(RdfProperty):
    term = RdfTerm(
        "propertyChainAxiom", "http://www.w3.org/2002/07/owl#propertyChainAxiom", []
    )
    object: rdf.List


@dataclass(frozen=True)
class propertyDisjointWith(RdfProperty):
    term = RdfTerm(
        "propertyDisjointWith", "http://www.w3.org/2002/07/owl#propertyDisjointWith", []
    )
    object: rdf.Property


@dataclass(frozen=True)
class qualifiedCardinality(RdfProperty):
    term = RdfTerm(
        "qualifiedCardinality", "http://www.w3.org/2002/07/owl#qualifiedCardinality", []
    )
    object: Identifier


@dataclass(frozen=True)
class sameAs(RdfProperty):
    term = RdfTerm("sameAs", "http://www.w3.org/2002/07/owl#sameAs", [])
    object: Identifier


@dataclass(frozen=True)
class someValuesFrom(RdfProperty):
    term = RdfTerm("someValuesFrom", "http://www.w3.org/2002/07/owl#someValuesFrom", [])
    object: rdfs.Class


@dataclass(frozen=True)
class sourceIndividual(RdfProperty):
    term = RdfTerm(
        "sourceIndividual", "http://www.w3.org/2002/07/owl#sourceIndividual", []
    )
    object: Identifier


@dataclass(frozen=True)
class targetIndividual(RdfProperty):
    term = RdfTerm(
        "targetIndividual", "http://www.w3.org/2002/07/owl#targetIndividual", []
    )
    object: Identifier


@dataclass(frozen=True)
class targetValue(RdfProperty):
    term = RdfTerm("targetValue", "http://www.w3.org/2002/07/owl#targetValue", [])
    object: rdfs.Literal


@dataclass(frozen=True)
class unionOf(RdfProperty):
    term = RdfTerm("unionOf", "http://www.w3.org/2002/07/owl#unionOf", [])
    object: rdf.List


@dataclass(frozen=True)
class withRestrictions(RdfProperty):
    term = RdfTerm(
        "withRestrictions", "http://www.w3.org/2002/07/owl#withRestrictions", []
    )
    object: rdf.List


@dataclass(frozen=True)
class bottomDataProperty(RdfProperty):
    term = RdfTerm(
        "bottomDataProperty", "http://www.w3.org/2002/07/owl#bottomDataProperty", []
    )
    object: rdfs.Literal


@dataclass(frozen=True)
class topDataProperty(RdfProperty):
    term = RdfTerm(
        "topDataProperty", "http://www.w3.org/2002/07/owl#topDataProperty", []
    )
    object: rdfs.Literal


@dataclass(frozen=True)
class bottomObjectProperty(RdfProperty):
    term = RdfTerm(
        "bottomObjectProperty", "http://www.w3.org/2002/07/owl#bottomObjectProperty", []
    )
    object: Identifier


@dataclass(frozen=True)
class topObjectProperty(RdfProperty):
    term = RdfTerm(
        "topObjectProperty", "http://www.w3.org/2002/07/owl#topObjectProperty", []
    )
    object: Identifier
