from __future__ import annotations
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfType
from rdfcrate.vocabs import rdfs


class aq(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#aq", "aq")


class category(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#category", "category")


class component(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#component", "component")


class constraints(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#constraints", "constraints")


class definition(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#definition", "definition")


class dm(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#dm", "dm")


class editorialNote(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#editorialNote", "editorialNote")


class editorsDefinition(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#editorsDefinition", "editorsDefinition")


class inverse(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#inverse", "inverse")


class n(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#n", "n")


class order(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#order", "order")


class qualifiedForm(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedForm", "qualifiedForm")


class sharesDefinitionWith(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#sharesDefinitionWith", "sharesDefinitionWith"
    )


class specializationOf(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#specializationOf", "specializationOf")


class todo(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#todo", "todo")


class unqualifiedForm(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#unqualifiedForm", "unqualifiedForm")


class wasRevisionOf(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasRevisionOf", "wasRevisionOf")


class atTime(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#atTime", "atTime")


class endedAtTime(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#endedAtTime", "endedAtTime")


class generatedAtTime(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#generatedAtTime", "generatedAtTime")


class invalidatedAtTime(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#invalidatedAtTime", "invalidatedAtTime")


class startedAtTime(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#startedAtTime", "startedAtTime")


class value(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#value", "value")


class provenanceUriTemplate(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#provenanceUriTemplate", "provenanceUriTemplate"
    )


class pairKey(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://www.w3.org/ns/prov#pairKey", "pairKey")


class removedKey(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://www.w3.org/ns/prov#removedKey", "removedKey")


class pairEntity(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#pairEntity", "pairEntity")


class actedOnBehalfOf(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#actedOnBehalfOf", "actedOnBehalfOf")


class activity(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#activity", "activity")


class agent(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#agent", "agent")


class alternateOf(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#alternateOf", "alternateOf")


class atLocation(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#atLocation", "atLocation")


class entity(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#entity", "entity")


class generated(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#generated", "generated")


class hadActivity(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadActivity", "hadActivity")


class hadGeneration(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadGeneration", "hadGeneration")


class hadMember(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadMember", "hadMember")


class hadPlan(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadPlan", "hadPlan")


class hadPrimarySource(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadPrimarySource", "hadPrimarySource")


class hadRole(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadRole", "hadRole")


class hadUsage(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadUsage", "hadUsage")


class influenced(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#influenced", "influenced")


class influencer(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#influencer", "influencer")


class invalidated(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#invalidated", "invalidated")


class qualifiedAssociation(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedAssociation", "qualifiedAssociation"
    )


class qualifiedAttribution(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedAttribution", "qualifiedAttribution"
    )


class qualifiedCommunication(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedCommunication", "qualifiedCommunication"
    )


class qualifiedDelegation(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedDelegation", "qualifiedDelegation"
    )


class qualifiedDerivation(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedDerivation", "qualifiedDerivation"
    )


class qualifiedEnd(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedEnd", "qualifiedEnd")


class qualifiedGeneration(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedGeneration", "qualifiedGeneration"
    )


class qualifiedInfluence(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedInfluence", "qualifiedInfluence")


class qualifiedInvalidation(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedInvalidation", "qualifiedInvalidation"
    )


class qualifiedPrimarySource(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedPrimarySource", "qualifiedPrimarySource"
    )


class qualifiedQuotation(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedQuotation", "qualifiedQuotation")


class qualifiedRevision(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedRevision", "qualifiedRevision")


class qualifiedStart(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedStart", "qualifiedStart")


class qualifiedUsage(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedUsage", "qualifiedUsage")


class used(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#used", "used")


class wasAssociatedWith(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasAssociatedWith", "wasAssociatedWith")


class wasAttributedTo(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasAttributedTo", "wasAttributedTo")


class wasDerivedFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasDerivedFrom", "wasDerivedFrom")


class wasEndedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasEndedBy", "wasEndedBy")


class wasGeneratedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasGeneratedBy", "wasGeneratedBy")


class wasInfluencedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasInfluencedBy", "wasInfluencedBy")


class wasInformedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasInformedBy", "wasInformedBy")


class wasInvalidatedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasInvalidatedBy", "wasInvalidatedBy")


class wasQuotedFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasQuotedFrom", "wasQuotedFrom")


class wasStartedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasStartedBy", "wasStartedBy")


class has_anchor(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#has_anchor", "has_anchor")


class has_provenance(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#has_provenance", "has_provenance")


class has_query_service(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#has_query_service", "has_query_service")


class describesService(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#describesService", "describesService")


class pingback(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#pingback", "pingback")


class dictionary(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#dictionary", "dictionary")


class derivedByInsertionFrom(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#derivedByInsertionFrom", "derivedByInsertionFrom"
    )


class derivedByRemovalFrom(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#derivedByRemovalFrom", "derivedByRemovalFrom"
    )


class insertedKeyEntityPair(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#insertedKeyEntityPair", "insertedKeyEntityPair"
    )


class hadDictionaryMember(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#hadDictionaryMember", "hadDictionaryMember"
    )


class qualifiedInsertion(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedInsertion", "qualifiedInsertion")


class qualifiedRemoval(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedRemoval", "qualifiedRemoval")


class asInBundle(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#asInBundle", "asInBundle")


class mentionOf(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#mentionOf", "mentionOf")
