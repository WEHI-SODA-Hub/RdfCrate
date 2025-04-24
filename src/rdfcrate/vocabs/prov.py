from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs


class aq(RdfProperty[Identifier]):
    term = RdfTerm("aq", "http://www.w3.org/ns/prov#aq", [])


class category(RdfProperty[Identifier]):
    term = RdfTerm("category", "http://www.w3.org/ns/prov#category", [])


class component(RdfProperty[Identifier]):
    term = RdfTerm("component", "http://www.w3.org/ns/prov#component", [])


class constraints(RdfProperty[Identifier]):
    term = RdfTerm("constraints", "http://www.w3.org/ns/prov#constraints", [])


class definition(RdfProperty[Identifier]):
    term = RdfTerm("definition", "http://www.w3.org/ns/prov#definition", [])


class dm(RdfProperty[Identifier]):
    term = RdfTerm("dm", "http://www.w3.org/ns/prov#dm", [])


class editorialNote(RdfProperty[Identifier]):
    term = RdfTerm("editorialNote", "http://www.w3.org/ns/prov#editorialNote", [])


class editorsDefinition(RdfProperty[Identifier]):
    term = RdfTerm(
        "editorsDefinition", "http://www.w3.org/ns/prov#editorsDefinition", []
    )


class inverse(RdfProperty[Identifier]):
    term = RdfTerm("inverse", "http://www.w3.org/ns/prov#inverse", [])


class n(RdfProperty[Identifier]):
    term = RdfTerm("n", "http://www.w3.org/ns/prov#n", [])


class order(RdfProperty[Identifier]):
    term = RdfTerm("order", "http://www.w3.org/ns/prov#order", [])


class qualifiedForm(RdfProperty[Identifier]):
    term = RdfTerm("qualifiedForm", "http://www.w3.org/ns/prov#qualifiedForm", [])


class sharesDefinitionWith(RdfProperty[Identifier]):
    term = RdfTerm(
        "sharesDefinitionWith", "http://www.w3.org/ns/prov#sharesDefinitionWith", []
    )


class specializationOf(RdfProperty[Identifier]):
    term = RdfTerm("specializationOf", "http://www.w3.org/ns/prov#specializationOf", [])


class todo(RdfProperty[Identifier]):
    term = RdfTerm("todo", "http://www.w3.org/ns/prov#todo", [])


class unqualifiedForm(RdfProperty[Identifier]):
    term = RdfTerm("unqualifiedForm", "http://www.w3.org/ns/prov#unqualifiedForm", [])


class wasRevisionOf(RdfProperty[Identifier]):
    term = RdfTerm("wasRevisionOf", "http://www.w3.org/ns/prov#wasRevisionOf", [])


class atTime(RdfProperty[Identifier]):
    term = RdfTerm("atTime", "http://www.w3.org/ns/prov#atTime", [])


class endedAtTime(RdfProperty[Identifier]):
    term = RdfTerm("endedAtTime", "http://www.w3.org/ns/prov#endedAtTime", [])


class generatedAtTime(RdfProperty[Identifier]):
    term = RdfTerm("generatedAtTime", "http://www.w3.org/ns/prov#generatedAtTime", [])


class invalidatedAtTime(RdfProperty[Identifier]):
    term = RdfTerm(
        "invalidatedAtTime", "http://www.w3.org/ns/prov#invalidatedAtTime", []
    )


class startedAtTime(RdfProperty[Identifier]):
    term = RdfTerm("startedAtTime", "http://www.w3.org/ns/prov#startedAtTime", [])


class value(RdfProperty[Identifier]):
    term = RdfTerm("value", "http://www.w3.org/ns/prov#value", [])


class provenanceUriTemplate(RdfProperty[Identifier]):
    term = RdfTerm(
        "provenanceUriTemplate", "http://www.w3.org/ns/prov#provenanceUriTemplate", []
    )


class pairKey(RdfProperty[rdfs.Literal]):
    term = RdfTerm("pairKey", "http://www.w3.org/ns/prov#pairKey", [])


class removedKey(RdfProperty[rdfs.Literal]):
    term = RdfTerm("removedKey", "http://www.w3.org/ns/prov#removedKey", [])


class pairEntity(RdfProperty[Identifier]):
    term = RdfTerm("pairEntity", "http://www.w3.org/ns/prov#pairEntity", [])


class actedOnBehalfOf(RdfProperty[Identifier]):
    term = RdfTerm("actedOnBehalfOf", "http://www.w3.org/ns/prov#actedOnBehalfOf", [])


class activity(RdfProperty[Identifier]):
    term = RdfTerm("activity", "http://www.w3.org/ns/prov#activity", [])


class agent(RdfProperty[Identifier]):
    term = RdfTerm("agent", "http://www.w3.org/ns/prov#agent", [])


class alternateOf(RdfProperty[Identifier]):
    term = RdfTerm("alternateOf", "http://www.w3.org/ns/prov#alternateOf", [])


class atLocation(RdfProperty[Identifier]):
    term = RdfTerm("atLocation", "http://www.w3.org/ns/prov#atLocation", [])


class entity(RdfProperty[Identifier]):
    term = RdfTerm("entity", "http://www.w3.org/ns/prov#entity", [])


class generated(RdfProperty[Identifier]):
    term = RdfTerm("generated", "http://www.w3.org/ns/prov#generated", [])


class hadActivity(RdfProperty[Identifier]):
    term = RdfTerm("hadActivity", "http://www.w3.org/ns/prov#hadActivity", [])


class hadGeneration(RdfProperty[Identifier]):
    term = RdfTerm("hadGeneration", "http://www.w3.org/ns/prov#hadGeneration", [])


class hadMember(RdfProperty[Identifier]):
    term = RdfTerm("hadMember", "http://www.w3.org/ns/prov#hadMember", [])


class hadPlan(RdfProperty[Identifier]):
    term = RdfTerm("hadPlan", "http://www.w3.org/ns/prov#hadPlan", [])


class hadPrimarySource(RdfProperty[Identifier]):
    term = RdfTerm("hadPrimarySource", "http://www.w3.org/ns/prov#hadPrimarySource", [])


class hadRole(RdfProperty[Identifier]):
    term = RdfTerm("hadRole", "http://www.w3.org/ns/prov#hadRole", [])


class hadUsage(RdfProperty[Identifier]):
    term = RdfTerm("hadUsage", "http://www.w3.org/ns/prov#hadUsage", [])


class influenced(RdfProperty[Identifier]):
    term = RdfTerm("influenced", "http://www.w3.org/ns/prov#influenced", [])


class influencer(RdfProperty[Identifier]):
    term = RdfTerm("influencer", "http://www.w3.org/ns/prov#influencer", [])


class invalidated(RdfProperty[Identifier]):
    term = RdfTerm("invalidated", "http://www.w3.org/ns/prov#invalidated", [])


class qualifiedAssociation(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedAssociation", "http://www.w3.org/ns/prov#qualifiedAssociation", []
    )


class qualifiedAttribution(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedAttribution", "http://www.w3.org/ns/prov#qualifiedAttribution", []
    )


class qualifiedCommunication(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedCommunication", "http://www.w3.org/ns/prov#qualifiedCommunication", []
    )


class qualifiedDelegation(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedDelegation", "http://www.w3.org/ns/prov#qualifiedDelegation", []
    )


class qualifiedDerivation(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedDerivation", "http://www.w3.org/ns/prov#qualifiedDerivation", []
    )


class qualifiedEnd(RdfProperty[Identifier]):
    term = RdfTerm("qualifiedEnd", "http://www.w3.org/ns/prov#qualifiedEnd", [])


class qualifiedGeneration(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedGeneration", "http://www.w3.org/ns/prov#qualifiedGeneration", []
    )


class qualifiedInfluence(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedInfluence", "http://www.w3.org/ns/prov#qualifiedInfluence", []
    )


class qualifiedInvalidation(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedInvalidation", "http://www.w3.org/ns/prov#qualifiedInvalidation", []
    )


class qualifiedPrimarySource(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedPrimarySource", "http://www.w3.org/ns/prov#qualifiedPrimarySource", []
    )


class qualifiedQuotation(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedQuotation", "http://www.w3.org/ns/prov#qualifiedQuotation", []
    )


class qualifiedRevision(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedRevision", "http://www.w3.org/ns/prov#qualifiedRevision", []
    )


class qualifiedStart(RdfProperty[Identifier]):
    term = RdfTerm("qualifiedStart", "http://www.w3.org/ns/prov#qualifiedStart", [])


class qualifiedUsage(RdfProperty[Identifier]):
    term = RdfTerm("qualifiedUsage", "http://www.w3.org/ns/prov#qualifiedUsage", [])


class used(RdfProperty[Identifier]):
    term = RdfTerm("used", "http://www.w3.org/ns/prov#used", [])


class wasAssociatedWith(RdfProperty[Identifier]):
    term = RdfTerm(
        "wasAssociatedWith", "http://www.w3.org/ns/prov#wasAssociatedWith", []
    )


class wasAttributedTo(RdfProperty[Identifier]):
    term = RdfTerm("wasAttributedTo", "http://www.w3.org/ns/prov#wasAttributedTo", [])


class wasDerivedFrom(RdfProperty[Identifier]):
    term = RdfTerm(
        "wasDerivedFrom",
        "http://www.w3.org/ns/prov#wasDerivedFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class wasEndedBy(RdfProperty[Identifier]):
    term = RdfTerm("wasEndedBy", "http://www.w3.org/ns/prov#wasEndedBy", [])


class wasGeneratedBy(RdfProperty[Identifier]):
    term = RdfTerm("wasGeneratedBy", "http://www.w3.org/ns/prov#wasGeneratedBy", [])


class wasInfluencedBy(RdfProperty[Identifier]):
    term = RdfTerm("wasInfluencedBy", "http://www.w3.org/ns/prov#wasInfluencedBy", [])


class wasInformedBy(RdfProperty[Identifier]):
    term = RdfTerm("wasInformedBy", "http://www.w3.org/ns/prov#wasInformedBy", [])


class wasInvalidatedBy(RdfProperty[Identifier]):
    term = RdfTerm("wasInvalidatedBy", "http://www.w3.org/ns/prov#wasInvalidatedBy", [])


class wasQuotedFrom(RdfProperty[Identifier]):
    term = RdfTerm("wasQuotedFrom", "http://www.w3.org/ns/prov#wasQuotedFrom", [])


class wasStartedBy(RdfProperty[Identifier]):
    term = RdfTerm("wasStartedBy", "http://www.w3.org/ns/prov#wasStartedBy", [])


class has_anchor(RdfProperty[Identifier]):
    term = RdfTerm("has_anchor", "http://www.w3.org/ns/prov#has_anchor", [])


class has_provenance(RdfProperty[Identifier]):
    term = RdfTerm("has_provenance", "http://www.w3.org/ns/prov#has_provenance", [])


class has_query_service(RdfProperty[Identifier]):
    term = RdfTerm(
        "has_query_service", "http://www.w3.org/ns/prov#has_query_service", []
    )


class describesService(RdfProperty[Identifier]):
    term = RdfTerm("describesService", "http://www.w3.org/ns/prov#describesService", [])


class pingback(RdfProperty[Identifier]):
    term = RdfTerm("pingback", "http://www.w3.org/ns/prov#pingback", [])


class dictionary(RdfProperty[Identifier]):
    term = RdfTerm("dictionary", "http://www.w3.org/ns/prov#dictionary", [])


class derivedByInsertionFrom(RdfProperty[Identifier]):
    term = RdfTerm(
        "derivedByInsertionFrom", "http://www.w3.org/ns/prov#derivedByInsertionFrom", []
    )


class derivedByRemovalFrom(RdfProperty[Identifier]):
    term = RdfTerm(
        "derivedByRemovalFrom", "http://www.w3.org/ns/prov#derivedByRemovalFrom", []
    )


class insertedKeyEntityPair(RdfProperty[Identifier]):
    term = RdfTerm(
        "insertedKeyEntityPair", "http://www.w3.org/ns/prov#insertedKeyEntityPair", []
    )


class hadDictionaryMember(RdfProperty[Identifier]):
    term = RdfTerm(
        "hadDictionaryMember", "http://www.w3.org/ns/prov#hadDictionaryMember", []
    )


class qualifiedInsertion(RdfProperty[Identifier]):
    term = RdfTerm(
        "qualifiedInsertion", "http://www.w3.org/ns/prov#qualifiedInsertion", []
    )


class qualifiedRemoval(RdfProperty[Identifier]):
    term = RdfTerm("qualifiedRemoval", "http://www.w3.org/ns/prov#qualifiedRemoval", [])


class asInBundle(RdfProperty[Identifier]):
    term = RdfTerm("asInBundle", "http://www.w3.org/ns/prov#asInBundle", [])


class mentionOf(RdfProperty[Identifier]):
    term = RdfTerm("mentionOf", "http://www.w3.org/ns/prov#mentionOf", [])
