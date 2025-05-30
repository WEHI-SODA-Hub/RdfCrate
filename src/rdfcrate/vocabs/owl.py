from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import rdf
from rdfcrate.rdftype import RdfType
from rdfcrate.vocabs import owl

class DataRange(rdfs.Datatype):
    term = RdfTerm('http://www.w3.org/2002/07/owl#DataRange', 'DataRange')

class Class(rdfs.Class):
    term = RdfTerm('http://www.w3.org/2002/07/owl#Class', 'Class')

class DeprecatedClass(rdfs.Class):
    term = RdfTerm('http://www.w3.org/2002/07/owl#DeprecatedClass', 'DeprecatedClass')

class AnnotationProperty(rdf.Property):
    term = RdfTerm('http://www.w3.org/2002/07/owl#AnnotationProperty', 'AnnotationProperty')

class DatatypeProperty(rdf.Property):
    term = RdfTerm('http://www.w3.org/2002/07/owl#DatatypeProperty', 'DatatypeProperty')

class DeprecatedProperty(rdf.Property):
    term = RdfTerm('http://www.w3.org/2002/07/owl#DeprecatedProperty', 'DeprecatedProperty')

class FunctionalProperty(rdf.Property):
    term = RdfTerm('http://www.w3.org/2002/07/owl#FunctionalProperty', 'FunctionalProperty')

class ObjectProperty(rdf.Property):
    term = RdfTerm('http://www.w3.org/2002/07/owl#ObjectProperty', 'ObjectProperty')

class OntologyProperty(rdf.Property):
    term = RdfTerm('http://www.w3.org/2002/07/owl#OntologyProperty', 'OntologyProperty')

class AllDifferent(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/2002/07/owl#AllDifferent', 'AllDifferent')

class AllDisjointClasses(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/2002/07/owl#AllDisjointClasses', 'AllDisjointClasses')

class AllDisjointProperties(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/2002/07/owl#AllDisjointProperties', 'AllDisjointProperties')

class Annotation(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/2002/07/owl#Annotation', 'Annotation')

class Axiom(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/2002/07/owl#Axiom', 'Axiom')

class NegativePropertyAssertion(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/2002/07/owl#NegativePropertyAssertion', 'NegativePropertyAssertion')

class Ontology(rdfs.Resource):
    term = RdfTerm('http://www.w3.org/2002/07/owl#Ontology', 'Ontology')

class NamedIndividual(RdfClass):
    term = RdfTerm('http://www.w3.org/2002/07/owl#NamedIndividual', 'NamedIndividual')

class Restriction(Class):
    term = RdfTerm('http://www.w3.org/2002/07/owl#Restriction', 'Restriction')

class AsymmetricProperty(ObjectProperty):
    term = RdfTerm('http://www.w3.org/2002/07/owl#AsymmetricProperty', 'AsymmetricProperty')

class InverseFunctionalProperty(ObjectProperty):
    term = RdfTerm('http://www.w3.org/2002/07/owl#InverseFunctionalProperty', 'InverseFunctionalProperty')

class IrreflexiveProperty(ObjectProperty):
    term = RdfTerm('http://www.w3.org/2002/07/owl#IrreflexiveProperty', 'IrreflexiveProperty')

class ReflexiveProperty(ObjectProperty):
    term = RdfTerm('http://www.w3.org/2002/07/owl#ReflexiveProperty', 'ReflexiveProperty')

class SymmetricProperty(ObjectProperty):
    term = RdfTerm('http://www.w3.org/2002/07/owl#SymmetricProperty', 'SymmetricProperty')

class TransitiveProperty(ObjectProperty):
    term = RdfTerm('http://www.w3.org/2002/07/owl#TransitiveProperty', 'TransitiveProperty')

class allValuesFrom(RdfProperty[rdfs.Class]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#allValuesFrom', 'allValuesFrom')

class annotatedProperty(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#annotatedProperty', 'annotatedProperty')

class annotatedSource(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#annotatedSource', 'annotatedSource')

class annotatedTarget(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#annotatedTarget', 'annotatedTarget')

class assertionProperty(RdfProperty[rdf.Property]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#assertionProperty', 'assertionProperty')

class cardinality(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#cardinality', 'cardinality')

class complementOf(RdfProperty[owl.Class]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#complementOf', 'complementOf')

class datatypeComplementOf(RdfProperty[rdfs.Datatype]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#datatypeComplementOf', 'datatypeComplementOf')

class differentFrom(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#differentFrom', 'differentFrom')

class disjointUnionOf(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#disjointUnionOf', 'disjointUnionOf')

class disjointWith(RdfProperty[owl.Class]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#disjointWith', 'disjointWith')

class distinctMembers(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#distinctMembers', 'distinctMembers')

class equivalentClass(RdfProperty[rdfs.Class]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#equivalentClass', 'equivalentClass')

class equivalentProperty(RdfProperty[rdf.Property]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#equivalentProperty', 'equivalentProperty')

class hasKey(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#hasKey', 'hasKey')

class hasSelf(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#hasSelf', 'hasSelf')

class hasValue(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#hasValue', 'hasValue')

class intersectionOf(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#intersectionOf', 'intersectionOf')

class inverseOf(RdfProperty[owl.ObjectProperty]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#inverseOf', 'inverseOf')

class maxCardinality(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#maxCardinality', 'maxCardinality')

class maxQualifiedCardinality(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#maxQualifiedCardinality', 'maxQualifiedCardinality')

class members(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#members', 'members')

class minCardinality(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#minCardinality', 'minCardinality')

class minQualifiedCardinality(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#minQualifiedCardinality', 'minQualifiedCardinality')

class onClass(RdfProperty[owl.Class]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#onClass', 'onClass')

class onDataRange(RdfProperty[rdfs.Datatype]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#onDataRange', 'onDataRange')

class onDatatype(RdfProperty[rdfs.Datatype]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#onDatatype', 'onDatatype')

class oneOf(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#oneOf', 'oneOf')

class onProperties(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#onProperties', 'onProperties')

class onProperty(RdfProperty[rdf.Property]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#onProperty', 'onProperty')

class propertyChainAxiom(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#propertyChainAxiom', 'propertyChainAxiom')

class propertyDisjointWith(RdfProperty[rdf.Property]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#propertyDisjointWith', 'propertyDisjointWith')

class qualifiedCardinality(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#qualifiedCardinality', 'qualifiedCardinality')

class sameAs(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#sameAs', 'sameAs')

class someValuesFrom(RdfProperty[rdfs.Class]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#someValuesFrom', 'someValuesFrom')

class sourceIndividual(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#sourceIndividual', 'sourceIndividual')

class targetIndividual(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#targetIndividual', 'targetIndividual')

class targetValue(RdfProperty[rdfs.Literal]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#targetValue', 'targetValue')

class unionOf(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#unionOf', 'unionOf')

class withRestrictions(RdfProperty[rdf.List]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#withRestrictions', 'withRestrictions')

class backwardCompatibleWith(RdfProperty[owl.Ontology]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#backwardCompatibleWith', 'backwardCompatibleWith')

class deprecated(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#deprecated', 'deprecated')

class incompatibleWith(RdfProperty[owl.Ontology]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#incompatibleWith', 'incompatibleWith')

class priorVersion(RdfProperty[owl.Ontology]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#priorVersion', 'priorVersion')

class versionInfo(RdfProperty[rdfs.Resource]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#versionInfo', 'versionInfo')

class bottomDataProperty(RdfProperty[rdfs.Literal]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#bottomDataProperty', 'bottomDataProperty')

class topDataProperty(RdfProperty[rdfs.Literal]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#topDataProperty', 'topDataProperty')

class bottomObjectProperty(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#bottomObjectProperty', 'bottomObjectProperty')

class topObjectProperty(RdfProperty[RdfType]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#topObjectProperty', 'topObjectProperty')

class imports(RdfProperty[owl.Ontology]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#imports', 'imports')

class versionIRI(RdfProperty[owl.Ontology]):
    term = RdfTerm('http://www.w3.org/2002/07/owl#versionIRI', 'versionIRI')