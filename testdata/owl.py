from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfType
from . import owl


class Alldifferent(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#AllDifferent", "Alldifferent")


class Alldisjointclasses(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#AllDisjointClasses", "Alldisjointclasses"
    )


class Alldisjointproperties(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#AllDisjointProperties", "Alldisjointproperties"
    )


class Annotation(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#Annotation", "Annotation")


class Annotationproperty(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#AnnotationProperty", "Annotationproperty"
    )


class Objectproperty(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#ObjectProperty", "Objectproperty")


class Axiom(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#Axiom", "Axiom")


class Class(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#Class", "Class")


class Datarange(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#DataRange", "Datarange")


class Datatypeproperty(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#DatatypeProperty", "Datatypeproperty")


class Deprecatedclass(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#DeprecatedClass", "Deprecatedclass")


class Deprecatedproperty(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#DeprecatedProperty", "Deprecatedproperty"
    )


class Functionalproperty(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#FunctionalProperty", "Functionalproperty"
    )


class Thing(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#Thing", "Thing")


class Negativepropertyassertion(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#NegativePropertyAssertion",
        "Negativepropertyassertion",
    )


class Ontology(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#Ontology", "Ontology")


class Ontologyproperty(RdfClass):
    term = RdfTerm("http://www.w3.org/2002/07/owl#OntologyProperty", "Ontologyproperty")


class Asymmetricproperty(Objectproperty):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#AsymmetricProperty", "Asymmetricproperty"
    )


class Inversefunctionalproperty(Objectproperty):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#InverseFunctionalProperty",
        "Inversefunctionalproperty",
    )


class Irreflexiveproperty(Objectproperty):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#IrreflexiveProperty", "Irreflexiveproperty"
    )


class Reflexiveproperty(Objectproperty):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#ReflexiveProperty", "Reflexiveproperty"
    )


class Symmetricproperty(Objectproperty):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#SymmetricProperty", "Symmetricproperty"
    )


class Transitiveproperty(Objectproperty):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#TransitiveProperty", "Transitiveproperty"
    )


class Restriction(Class):
    term = RdfTerm("http://www.w3.org/2002/07/owl#Restriction", "Restriction")


class Namedindividual(Thing):
    term = RdfTerm("http://www.w3.org/2002/07/owl#NamedIndividual", "Namedindividual")


class Nothing(Thing):
    term = RdfTerm("http://www.w3.org/2002/07/owl#Nothing", "Nothing")


class allvaluesfrom(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#allValuesFrom", "allvaluesfrom")


class annotatedproperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#annotatedProperty", "annotatedproperty"
    )


class annotatedsource(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#annotatedSource", "annotatedsource")


class annotatedtarget(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#annotatedTarget", "annotatedtarget")


class assertionproperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#assertionProperty", "assertionproperty"
    )


class cardinality(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#cardinality", "cardinality")


class complementof(RdfProperty[owl.Class]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#complementOf", "complementof")


class datatypecomplementof(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#datatypeComplementOf", "datatypecomplementof"
    )


class differentfrom(RdfProperty[owl.Thing]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#differentFrom", "differentfrom")


class disjointunionof(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#disjointUnionOf", "disjointunionof")


class disjointwith(RdfProperty[owl.Class]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#disjointWith", "disjointwith")


class distinctmembers(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#distinctMembers", "distinctmembers")


class equivalentclass(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#equivalentClass", "equivalentclass")


class equivalentproperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#equivalentProperty", "equivalentproperty"
    )


class haskey(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#hasKey", "haskey")


class hasself(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#hasSelf", "hasself")


class hasvalue(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#hasValue", "hasvalue")


class intersectionof(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#intersectionOf", "intersectionof")


class inverseof(RdfProperty[owl.Objectproperty]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#inverseOf", "inverseof")


class maxcardinality(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#maxCardinality", "maxcardinality")


class maxqualifiedcardinality(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#maxQualifiedCardinality",
        "maxqualifiedcardinality",
    )


class members(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#members", "members")


class mincardinality(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#minCardinality", "mincardinality")


class minqualifiedcardinality(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#minQualifiedCardinality",
        "minqualifiedcardinality",
    )


class onclass(RdfProperty[owl.Class]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#onClass", "onclass")


class ondatarange(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#onDataRange", "ondatarange")


class ondatatype(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#onDatatype", "ondatatype")


class oneof(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#oneOf", "oneof")


class onproperties(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#onProperties", "onproperties")


class onproperty(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#onProperty", "onproperty")


class propertychainaxiom(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#propertyChainAxiom", "propertychainaxiom"
    )


class propertydisjointwith(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#propertyDisjointWith", "propertydisjointwith"
    )


class qualifiedcardinality(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#qualifiedCardinality", "qualifiedcardinality"
    )


class sameas(RdfProperty[owl.Thing]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#sameAs", "sameas")


class somevaluesfrom(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#someValuesFrom", "somevaluesfrom")


class sourceindividual(RdfProperty[owl.Thing]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#sourceIndividual", "sourceindividual")


class targetindividual(RdfProperty[owl.Thing]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#targetIndividual", "targetindividual")


class targetvalue(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#targetValue", "targetvalue")


class unionof(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#unionOf", "unionof")


class withrestrictions(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#withRestrictions", "withrestrictions")


class backwardcompatiblewith(RdfProperty[owl.Ontology]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#backwardCompatibleWith", "backwardcompatiblewith"
    )


class deprecated(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#deprecated", "deprecated")


class incompatiblewith(RdfProperty[owl.Ontology]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#incompatibleWith", "incompatiblewith")


class priorversion(RdfProperty[owl.Ontology]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#priorVersion", "priorversion")


class versioninfo(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#versionInfo", "versioninfo")


class bottomdataproperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#bottomDataProperty", "bottomdataproperty"
    )


class topdataproperty(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#topDataProperty", "topdataproperty")


class bottomobjectproperty(RdfProperty[owl.Thing]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#bottomObjectProperty", "bottomobjectproperty"
    )


class topobjectproperty(RdfProperty[owl.Thing]):
    term = RdfTerm(
        "http://www.w3.org/2002/07/owl#topObjectProperty", "topobjectproperty"
    )


class imports(RdfProperty[owl.Ontology]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#imports", "imports")


class versioniri(RdfProperty[owl.Ontology]):
    term = RdfTerm("http://www.w3.org/2002/07/owl#versionIRI", "versioniri")
