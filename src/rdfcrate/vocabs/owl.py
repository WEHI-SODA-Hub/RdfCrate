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
    term = RdfTerm('DataRange', 'http://www.w3.org/2002/07/owl#DataRange', [])

class Class(rdfs.Class):
    term = RdfTerm('Class', 'http://www.w3.org/2002/07/owl#Class', [])

class DeprecatedClass(rdfs.Class):
    term = RdfTerm('DeprecatedClass', 'http://www.w3.org/2002/07/owl#DeprecatedClass', [])

class AnnotationProperty(rdf.Property):
    term = RdfTerm('AnnotationProperty', 'http://www.w3.org/2002/07/owl#AnnotationProperty', [])

class DatatypeProperty(rdf.Property):
    term = RdfTerm('DatatypeProperty', 'http://www.w3.org/2002/07/owl#DatatypeProperty', [])

class DeprecatedProperty(rdf.Property):
    term = RdfTerm('DeprecatedProperty', 'http://www.w3.org/2002/07/owl#DeprecatedProperty', [])

class FunctionalProperty(rdf.Property):
    term = RdfTerm('FunctionalProperty', 'http://www.w3.org/2002/07/owl#FunctionalProperty', [])

class ObjectProperty(rdf.Property):
    term = RdfTerm('ObjectProperty', 'http://www.w3.org/2002/07/owl#ObjectProperty', [])

class OntologyProperty(rdf.Property):
    term = RdfTerm('OntologyProperty', 'http://www.w3.org/2002/07/owl#OntologyProperty', [])

class AllDifferent(rdfs.Resource):
    term = RdfTerm('AllDifferent', 'http://www.w3.org/2002/07/owl#AllDifferent', [])

class AllDisjointClasses(rdfs.Resource):
    term = RdfTerm('AllDisjointClasses', 'http://www.w3.org/2002/07/owl#AllDisjointClasses', [])

class AllDisjointProperties(rdfs.Resource):
    term = RdfTerm('AllDisjointProperties', 'http://www.w3.org/2002/07/owl#AllDisjointProperties', [])

class Annotation(rdfs.Resource):
    term = RdfTerm('Annotation', 'http://www.w3.org/2002/07/owl#Annotation', [])

class Axiom(rdfs.Resource):
    term = RdfTerm('Axiom', 'http://www.w3.org/2002/07/owl#Axiom', [])

class NegativePropertyAssertion(rdfs.Resource):
    term = RdfTerm('NegativePropertyAssertion', 'http://www.w3.org/2002/07/owl#NegativePropertyAssertion', [])

class Ontology(rdfs.Resource):
    term = RdfTerm('Ontology', 'http://www.w3.org/2002/07/owl#Ontology', [])

class NamedIndividual(RdfClass):
    term = RdfTerm('NamedIndividual', 'http://www.w3.org/2002/07/owl#NamedIndividual', [])

class Restriction(Class):
    term = RdfTerm('Restriction', 'http://www.w3.org/2002/07/owl#Restriction', [])

class AsymmetricProperty(ObjectProperty):
    term = RdfTerm('AsymmetricProperty', 'http://www.w3.org/2002/07/owl#AsymmetricProperty', [])

class InverseFunctionalProperty(ObjectProperty):
    term = RdfTerm('InverseFunctionalProperty', 'http://www.w3.org/2002/07/owl#InverseFunctionalProperty', [])

class IrreflexiveProperty(ObjectProperty):
    term = RdfTerm('IrreflexiveProperty', 'http://www.w3.org/2002/07/owl#IrreflexiveProperty', [])

class ReflexiveProperty(ObjectProperty):
    term = RdfTerm('ReflexiveProperty', 'http://www.w3.org/2002/07/owl#ReflexiveProperty', [])

class SymmetricProperty(ObjectProperty):
    term = RdfTerm('SymmetricProperty', 'http://www.w3.org/2002/07/owl#SymmetricProperty', [])

class TransitiveProperty(ObjectProperty):
    term = RdfTerm('TransitiveProperty', 'http://www.w3.org/2002/07/owl#TransitiveProperty', [])

class allValuesFrom(RdfProperty[rdfs.Class]):
    term = RdfTerm('allValuesFrom', 'http://www.w3.org/2002/07/owl#allValuesFrom', [])

class annotatedProperty(RdfProperty[rdfs.Resource]):
    term = RdfTerm('annotatedProperty', 'http://www.w3.org/2002/07/owl#annotatedProperty', [])

class annotatedSource(RdfProperty[rdfs.Resource]):
    term = RdfTerm('annotatedSource', 'http://www.w3.org/2002/07/owl#annotatedSource', [])

class annotatedTarget(RdfProperty[rdfs.Resource]):
    term = RdfTerm('annotatedTarget', 'http://www.w3.org/2002/07/owl#annotatedTarget', [])

class assertionProperty(RdfProperty[rdf.Property]):
    term = RdfTerm('assertionProperty', 'http://www.w3.org/2002/07/owl#assertionProperty', [])

class cardinality(RdfProperty[Identifier]):
    term = RdfTerm('cardinality', 'http://www.w3.org/2002/07/owl#cardinality', [])

class complementOf(RdfProperty[owl.Class]):
    term = RdfTerm('complementOf', 'http://www.w3.org/2002/07/owl#complementOf', [])

class datatypeComplementOf(RdfProperty[rdfs.Datatype]):
    term = RdfTerm('datatypeComplementOf', 'http://www.w3.org/2002/07/owl#datatypeComplementOf', [])

class differentFrom(RdfProperty[Identifier]):
    term = RdfTerm('differentFrom', 'http://www.w3.org/2002/07/owl#differentFrom', [])

class disjointUnionOf(RdfProperty[rdf.List]):
    term = RdfTerm('disjointUnionOf', 'http://www.w3.org/2002/07/owl#disjointUnionOf', [])

class disjointWith(RdfProperty[owl.Class]):
    term = RdfTerm('disjointWith', 'http://www.w3.org/2002/07/owl#disjointWith', [])

class distinctMembers(RdfProperty[rdf.List]):
    term = RdfTerm('distinctMembers', 'http://www.w3.org/2002/07/owl#distinctMembers', [])

class equivalentClass(RdfProperty[rdfs.Class]):
    term = RdfTerm('equivalentClass', 'http://www.w3.org/2002/07/owl#equivalentClass', [])

class equivalentProperty(RdfProperty[rdf.Property]):
    term = RdfTerm('equivalentProperty', 'http://www.w3.org/2002/07/owl#equivalentProperty', [])

class hasKey(RdfProperty[rdf.List]):
    term = RdfTerm('hasKey', 'http://www.w3.org/2002/07/owl#hasKey', [])

class hasSelf(RdfProperty[rdfs.Resource]):
    term = RdfTerm('hasSelf', 'http://www.w3.org/2002/07/owl#hasSelf', [])

class hasValue(RdfProperty[rdfs.Resource]):
    term = RdfTerm('hasValue', 'http://www.w3.org/2002/07/owl#hasValue', [])

class intersectionOf(RdfProperty[rdf.List]):
    term = RdfTerm('intersectionOf', 'http://www.w3.org/2002/07/owl#intersectionOf', [])

class inverseOf(RdfProperty[owl.ObjectProperty]):
    term = RdfTerm('inverseOf', 'http://www.w3.org/2002/07/owl#inverseOf', [])

class maxCardinality(RdfProperty[Identifier]):
    term = RdfTerm('maxCardinality', 'http://www.w3.org/2002/07/owl#maxCardinality', [])

class maxQualifiedCardinality(RdfProperty[Identifier]):
    term = RdfTerm('maxQualifiedCardinality', 'http://www.w3.org/2002/07/owl#maxQualifiedCardinality', [])

class members(RdfProperty[rdf.List]):
    term = RdfTerm('members', 'http://www.w3.org/2002/07/owl#members', [])

class minCardinality(RdfProperty[Identifier]):
    term = RdfTerm('minCardinality', 'http://www.w3.org/2002/07/owl#minCardinality', [])

class minQualifiedCardinality(RdfProperty[Identifier]):
    term = RdfTerm('minQualifiedCardinality', 'http://www.w3.org/2002/07/owl#minQualifiedCardinality', [])

class onClass(RdfProperty[owl.Class]):
    term = RdfTerm('onClass', 'http://www.w3.org/2002/07/owl#onClass', [])

class onDataRange(RdfProperty[rdfs.Datatype]):
    term = RdfTerm('onDataRange', 'http://www.w3.org/2002/07/owl#onDataRange', [])

class onDatatype(RdfProperty[rdfs.Datatype]):
    term = RdfTerm('onDatatype', 'http://www.w3.org/2002/07/owl#onDatatype', [])

class oneOf(RdfProperty[rdf.List]):
    term = RdfTerm('oneOf', 'http://www.w3.org/2002/07/owl#oneOf', [])

class onProperties(RdfProperty[rdf.List]):
    term = RdfTerm('onProperties', 'http://www.w3.org/2002/07/owl#onProperties', [])

class onProperty(RdfProperty[rdf.Property]):
    term = RdfTerm('onProperty', 'http://www.w3.org/2002/07/owl#onProperty', [])

class propertyChainAxiom(RdfProperty[rdf.List]):
    term = RdfTerm('propertyChainAxiom', 'http://www.w3.org/2002/07/owl#propertyChainAxiom', [])

class propertyDisjointWith(RdfProperty[rdf.Property]):
    term = RdfTerm('propertyDisjointWith', 'http://www.w3.org/2002/07/owl#propertyDisjointWith', [])

class qualifiedCardinality(RdfProperty[Identifier]):
    term = RdfTerm('qualifiedCardinality', 'http://www.w3.org/2002/07/owl#qualifiedCardinality', [])

class sameAs(RdfProperty[Identifier]):
    term = RdfTerm('sameAs', 'http://www.w3.org/2002/07/owl#sameAs', [])

class someValuesFrom(RdfProperty[rdfs.Class]):
    term = RdfTerm('someValuesFrom', 'http://www.w3.org/2002/07/owl#someValuesFrom', [])

class sourceIndividual(RdfProperty[Identifier]):
    term = RdfTerm('sourceIndividual', 'http://www.w3.org/2002/07/owl#sourceIndividual', [])

class targetIndividual(RdfProperty[Identifier]):
    term = RdfTerm('targetIndividual', 'http://www.w3.org/2002/07/owl#targetIndividual', [])

class targetValue(RdfProperty[rdfs.Literal]):
    term = RdfTerm('targetValue', 'http://www.w3.org/2002/07/owl#targetValue', [])

class unionOf(RdfProperty[rdf.List]):
    term = RdfTerm('unionOf', 'http://www.w3.org/2002/07/owl#unionOf', [])

class withRestrictions(RdfProperty[rdf.List]):
    term = RdfTerm('withRestrictions', 'http://www.w3.org/2002/07/owl#withRestrictions', [])

class backwardCompatibleWith(RdfProperty[owl.Ontology]):
    term = RdfTerm('backwardCompatibleWith', 'http://www.w3.org/2002/07/owl#backwardCompatibleWith', [])

class deprecated(RdfProperty[rdfs.Resource]):
    term = RdfTerm('deprecated', 'http://www.w3.org/2002/07/owl#deprecated', [])

class incompatibleWith(RdfProperty[owl.Ontology]):
    term = RdfTerm('incompatibleWith', 'http://www.w3.org/2002/07/owl#incompatibleWith', [])

class priorVersion(RdfProperty[owl.Ontology]):
    term = RdfTerm('priorVersion', 'http://www.w3.org/2002/07/owl#priorVersion', [])

class versionInfo(RdfProperty[rdfs.Resource]):
    term = RdfTerm('versionInfo', 'http://www.w3.org/2002/07/owl#versionInfo', [])

class bottomDataProperty(RdfProperty[rdfs.Literal]):
    term = RdfTerm('bottomDataProperty', 'http://www.w3.org/2002/07/owl#bottomDataProperty', [])

class topDataProperty(RdfProperty[rdfs.Literal]):
    term = RdfTerm('topDataProperty', 'http://www.w3.org/2002/07/owl#topDataProperty', [])

class bottomObjectProperty(RdfProperty[Identifier]):
    term = RdfTerm('bottomObjectProperty', 'http://www.w3.org/2002/07/owl#bottomObjectProperty', [])

class topObjectProperty(RdfProperty[Identifier]):
    term = RdfTerm('topObjectProperty', 'http://www.w3.org/2002/07/owl#topObjectProperty', [])

class imports(RdfProperty[owl.Ontology]):
    term = RdfTerm('imports', 'http://www.w3.org/2002/07/owl#imports', [])

class versionIRI(RdfProperty[owl.Ontology]):
    term = RdfTerm('versionIRI', 'http://www.w3.org/2002/07/owl#versionIRI', [])