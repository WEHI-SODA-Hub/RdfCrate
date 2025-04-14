from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs


@dataclass(frozen=True)
class atTime(RdfProperty):
    term = RdfTerm("atTime", "http://www.w3.org/ns/prov#atTime", [])
    object: Identifier


@dataclass(frozen=True)
class endedAtTime(RdfProperty):
    term = RdfTerm("endedAtTime", "http://www.w3.org/ns/prov#endedAtTime", [])
    object: Identifier


@dataclass(frozen=True)
class generatedAtTime(RdfProperty):
    term = RdfTerm("generatedAtTime", "http://www.w3.org/ns/prov#generatedAtTime", [])
    object: Identifier


@dataclass(frozen=True)
class invalidatedAtTime(RdfProperty):
    term = RdfTerm(
        "invalidatedAtTime", "http://www.w3.org/ns/prov#invalidatedAtTime", []
    )
    object: Identifier


@dataclass(frozen=True)
class startedAtTime(RdfProperty):
    term = RdfTerm("startedAtTime", "http://www.w3.org/ns/prov#startedAtTime", [])
    object: Identifier


@dataclass(frozen=True)
class value(RdfProperty):
    term = RdfTerm("value", "http://www.w3.org/ns/prov#value", [])
    object: Identifier


@dataclass(frozen=True)
class provenanceUriTemplate(RdfProperty):
    term = RdfTerm(
        "provenanceUriTemplate", "http://www.w3.org/ns/prov#provenanceUriTemplate", []
    )
    object: Identifier


@dataclass(frozen=True)
class pairKey(RdfProperty):
    term = RdfTerm("pairKey", "http://www.w3.org/ns/prov#pairKey", [])
    object: rdfs.Literal


@dataclass(frozen=True)
class removedKey(RdfProperty):
    term = RdfTerm("removedKey", "http://www.w3.org/ns/prov#removedKey", [])
    object: rdfs.Literal


@dataclass(frozen=True)
class actedOnBehalfOf(RdfProperty):
    term = RdfTerm("actedOnBehalfOf", "http://www.w3.org/ns/prov#actedOnBehalfOf", [])
    object: Identifier


@dataclass(frozen=True)
class activity(RdfProperty):
    term = RdfTerm("activity", "http://www.w3.org/ns/prov#activity", [])
    object: Identifier


@dataclass(frozen=True)
class agent(RdfProperty):
    term = RdfTerm("agent", "http://www.w3.org/ns/prov#agent", [])
    object: Identifier


@dataclass(frozen=True)
class alternateOf(RdfProperty):
    term = RdfTerm("alternateOf", "http://www.w3.org/ns/prov#alternateOf", [])
    object: Identifier


@dataclass(frozen=True)
class atLocation(RdfProperty):
    term = RdfTerm("atLocation", "http://www.w3.org/ns/prov#atLocation", [])
    object: Identifier


@dataclass(frozen=True)
class entity(RdfProperty):
    term = RdfTerm("entity", "http://www.w3.org/ns/prov#entity", [])
    object: Identifier


@dataclass(frozen=True)
class generated(RdfProperty):
    term = RdfTerm("generated", "http://www.w3.org/ns/prov#generated", [])
    object: Identifier


@dataclass(frozen=True)
class hadActivity(RdfProperty):
    term = RdfTerm("hadActivity", "http://www.w3.org/ns/prov#hadActivity", [])
    object: Identifier


@dataclass(frozen=True)
class hadGeneration(RdfProperty):
    term = RdfTerm("hadGeneration", "http://www.w3.org/ns/prov#hadGeneration", [])
    object: Identifier


@dataclass(frozen=True)
class hadMember(RdfProperty):
    term = RdfTerm("hadMember", "http://www.w3.org/ns/prov#hadMember", [])
    object: Identifier


@dataclass(frozen=True)
class hadPlan(RdfProperty):
    term = RdfTerm("hadPlan", "http://www.w3.org/ns/prov#hadPlan", [])
    object: Identifier


@dataclass(frozen=True)
class hadPrimarySource(RdfProperty):
    term = RdfTerm("hadPrimarySource", "http://www.w3.org/ns/prov#hadPrimarySource", [])
    object: Identifier


@dataclass(frozen=True)
class hadRole(RdfProperty):
    term = RdfTerm("hadRole", "http://www.w3.org/ns/prov#hadRole", [])
    object: Identifier


@dataclass(frozen=True)
class hadUsage(RdfProperty):
    term = RdfTerm("hadUsage", "http://www.w3.org/ns/prov#hadUsage", [])
    object: Identifier


@dataclass(frozen=True)
class influenced(RdfProperty):
    term = RdfTerm("influenced", "http://www.w3.org/ns/prov#influenced", [])
    object: Identifier


@dataclass(frozen=True)
class influencer(RdfProperty):
    term = RdfTerm("influencer", "http://www.w3.org/ns/prov#influencer", [])
    object: Identifier


@dataclass(frozen=True)
class invalidated(RdfProperty):
    term = RdfTerm("invalidated", "http://www.w3.org/ns/prov#invalidated", [])
    object: Identifier


@dataclass(frozen=True)
class qualifiedAssociation(RdfProperty):
    term = RdfTerm(
        "qualifiedAssociation", "http://www.w3.org/ns/prov#qualifiedAssociation", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedAttribution(RdfProperty):
    term = RdfTerm(
        "qualifiedAttribution", "http://www.w3.org/ns/prov#qualifiedAttribution", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedCommunication(RdfProperty):
    term = RdfTerm(
        "qualifiedCommunication", "http://www.w3.org/ns/prov#qualifiedCommunication", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedDelegation(RdfProperty):
    term = RdfTerm(
        "qualifiedDelegation", "http://www.w3.org/ns/prov#qualifiedDelegation", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedDerivation(RdfProperty):
    term = RdfTerm(
        "qualifiedDerivation", "http://www.w3.org/ns/prov#qualifiedDerivation", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedEnd(RdfProperty):
    term = RdfTerm("qualifiedEnd", "http://www.w3.org/ns/prov#qualifiedEnd", [])
    object: Identifier


@dataclass(frozen=True)
class qualifiedGeneration(RdfProperty):
    term = RdfTerm(
        "qualifiedGeneration", "http://www.w3.org/ns/prov#qualifiedGeneration", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedInfluence(RdfProperty):
    term = RdfTerm(
        "qualifiedInfluence", "http://www.w3.org/ns/prov#qualifiedInfluence", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedInvalidation(RdfProperty):
    term = RdfTerm(
        "qualifiedInvalidation", "http://www.w3.org/ns/prov#qualifiedInvalidation", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedPrimarySource(RdfProperty):
    term = RdfTerm(
        "qualifiedPrimarySource", "http://www.w3.org/ns/prov#qualifiedPrimarySource", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedQuotation(RdfProperty):
    term = RdfTerm(
        "qualifiedQuotation", "http://www.w3.org/ns/prov#qualifiedQuotation", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedRevision(RdfProperty):
    term = RdfTerm(
        "qualifiedRevision", "http://www.w3.org/ns/prov#qualifiedRevision", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedStart(RdfProperty):
    term = RdfTerm("qualifiedStart", "http://www.w3.org/ns/prov#qualifiedStart", [])
    object: Identifier


@dataclass(frozen=True)
class qualifiedUsage(RdfProperty):
    term = RdfTerm("qualifiedUsage", "http://www.w3.org/ns/prov#qualifiedUsage", [])
    object: Identifier


@dataclass(frozen=True)
class specializationOf(RdfProperty):
    term = RdfTerm("specializationOf", "http://www.w3.org/ns/prov#specializationOf", [])
    object: Identifier


@dataclass(frozen=True)
class used(RdfProperty):
    term = RdfTerm("used", "http://www.w3.org/ns/prov#used", [])
    object: Identifier


@dataclass(frozen=True)
class wasAssociatedWith(RdfProperty):
    term = RdfTerm(
        "wasAssociatedWith", "http://www.w3.org/ns/prov#wasAssociatedWith", []
    )
    object: Identifier


@dataclass(frozen=True)
class wasAttributedTo(RdfProperty):
    term = RdfTerm("wasAttributedTo", "http://www.w3.org/ns/prov#wasAttributedTo", [])
    object: Identifier


@dataclass(frozen=True)
class wasDerivedFrom(RdfProperty):
    term = RdfTerm(
        "wasDerivedFrom",
        "http://www.w3.org/ns/prov#wasDerivedFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class wasEndedBy(RdfProperty):
    term = RdfTerm("wasEndedBy", "http://www.w3.org/ns/prov#wasEndedBy", [])
    object: Identifier


@dataclass(frozen=True)
class wasGeneratedBy(RdfProperty):
    term = RdfTerm("wasGeneratedBy", "http://www.w3.org/ns/prov#wasGeneratedBy", [])
    object: Identifier


@dataclass(frozen=True)
class wasInfluencedBy(RdfProperty):
    term = RdfTerm("wasInfluencedBy", "http://www.w3.org/ns/prov#wasInfluencedBy", [])
    object: Identifier


@dataclass(frozen=True)
class wasInformedBy(RdfProperty):
    term = RdfTerm("wasInformedBy", "http://www.w3.org/ns/prov#wasInformedBy", [])
    object: Identifier


@dataclass(frozen=True)
class wasInvalidatedBy(RdfProperty):
    term = RdfTerm("wasInvalidatedBy", "http://www.w3.org/ns/prov#wasInvalidatedBy", [])
    object: Identifier


@dataclass(frozen=True)
class wasQuotedFrom(RdfProperty):
    term = RdfTerm("wasQuotedFrom", "http://www.w3.org/ns/prov#wasQuotedFrom", [])
    object: Identifier


@dataclass(frozen=True)
class wasRevisionOf(RdfProperty):
    term = RdfTerm("wasRevisionOf", "http://www.w3.org/ns/prov#wasRevisionOf", [])
    object: Identifier


@dataclass(frozen=True)
class wasStartedBy(RdfProperty):
    term = RdfTerm("wasStartedBy", "http://www.w3.org/ns/prov#wasStartedBy", [])
    object: Identifier


@dataclass(frozen=True)
class has_anchor(RdfProperty):
    term = RdfTerm("has_anchor", "http://www.w3.org/ns/prov#has_anchor", [])
    object: Identifier


@dataclass(frozen=True)
class has_provenance(RdfProperty):
    term = RdfTerm("has_provenance", "http://www.w3.org/ns/prov#has_provenance", [])
    object: Identifier


@dataclass(frozen=True)
class has_query_service(RdfProperty):
    term = RdfTerm(
        "has_query_service", "http://www.w3.org/ns/prov#has_query_service", []
    )
    object: Identifier


@dataclass(frozen=True)
class describesService(RdfProperty):
    term = RdfTerm("describesService", "http://www.w3.org/ns/prov#describesService", [])
    object: Identifier


@dataclass(frozen=True)
class pingback(RdfProperty):
    term = RdfTerm("pingback", "http://www.w3.org/ns/prov#pingback", [])
    object: Identifier


@dataclass(frozen=True)
class dictionary(RdfProperty):
    term = RdfTerm("dictionary", "http://www.w3.org/ns/prov#dictionary", [])
    object: Identifier


@dataclass(frozen=True)
class derivedByInsertionFrom(RdfProperty):
    term = RdfTerm(
        "derivedByInsertionFrom", "http://www.w3.org/ns/prov#derivedByInsertionFrom", []
    )
    object: Identifier


@dataclass(frozen=True)
class derivedByRemovalFrom(RdfProperty):
    term = RdfTerm(
        "derivedByRemovalFrom", "http://www.w3.org/ns/prov#derivedByRemovalFrom", []
    )
    object: Identifier


@dataclass(frozen=True)
class insertedKeyEntityPair(RdfProperty):
    term = RdfTerm(
        "insertedKeyEntityPair", "http://www.w3.org/ns/prov#insertedKeyEntityPair", []
    )
    object: Identifier


@dataclass(frozen=True)
class hadDictionaryMember(RdfProperty):
    term = RdfTerm(
        "hadDictionaryMember", "http://www.w3.org/ns/prov#hadDictionaryMember", []
    )
    object: Identifier


@dataclass(frozen=True)
class pairEntity(RdfProperty):
    term = RdfTerm("pairEntity", "http://www.w3.org/ns/prov#pairEntity", [])
    object: Identifier


@dataclass(frozen=True)
class qualifiedInsertion(RdfProperty):
    term = RdfTerm(
        "qualifiedInsertion", "http://www.w3.org/ns/prov#qualifiedInsertion", []
    )
    object: Identifier


@dataclass(frozen=True)
class qualifiedRemoval(RdfProperty):
    term = RdfTerm("qualifiedRemoval", "http://www.w3.org/ns/prov#qualifiedRemoval", [])
    object: Identifier


@dataclass(frozen=True)
class asInBundle(RdfProperty):
    term = RdfTerm("asInBundle", "http://www.w3.org/ns/prov#asInBundle", [])
    object: Identifier


@dataclass(frozen=True)
class mentionOf(RdfProperty):
    term = RdfTerm("mentionOf", "http://www.w3.org/ns/prov#mentionOf", [])
    object: Identifier
