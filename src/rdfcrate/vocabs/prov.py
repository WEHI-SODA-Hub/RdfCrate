from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import owl
from rdfcrate.rdftype import RdfType
from rdfcrate.vocabs import prov
from rdfcrate.vocabs import rdfs


class Agent(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#Agent", "Agent")


class Activity(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#Activity", "Activity")


class Influence(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#Influence", "Influence")


class InstantaneousEvent(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#InstantaneousEvent", "InstantaneousEvent")


class Entity(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#Entity", "Entity")


class Dictionary(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#Dictionary", "Dictionary")


class Location(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#Location", "Location")


class Role(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#Role", "Role")


class KeyEntityPair(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/prov#KeyEntityPair", "KeyEntityPair")


class SoftwareAgent(Agent, owl.Thing):
    term = RdfTerm("http://www.w3.org/ns/prov#SoftwareAgent", "SoftwareAgent")


class Organization(Agent):
    term = RdfTerm("http://www.w3.org/ns/prov#Organization", "Organization")


class Person(Agent):
    term = RdfTerm("http://www.w3.org/ns/prov#Person", "Person")


class Accept(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#Accept", "Accept")


class Contribute(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#Contribute", "Contribute")


class Copyright(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#Copyright", "Copyright")


class Modify(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#Modify", "Modify")


class Publish(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#Publish", "Publish")


class Replace(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#Replace", "Replace")


class RightsAssignment(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#RightsAssignment", "RightsAssignment")


class Submit(Activity):
    term = RdfTerm("http://www.w3.org/ns/prov#Submit", "Submit")


class ActivityInfluence(Influence):
    term = RdfTerm("http://www.w3.org/ns/prov#ActivityInfluence", "ActivityInfluence")


class AgentInfluence(Influence):
    term = RdfTerm("http://www.w3.org/ns/prov#AgentInfluence", "AgentInfluence")


class EntityInfluence(Influence):
    term = RdfTerm("http://www.w3.org/ns/prov#EntityInfluence", "EntityInfluence")


class Bundle(Entity):
    term = RdfTerm("http://www.w3.org/ns/prov#Bundle", "Bundle")


class Collection(Entity):
    term = RdfTerm("http://www.w3.org/ns/prov#Collection", "Collection")


class Plan(Entity):
    term = RdfTerm("http://www.w3.org/ns/prov#Plan", "Plan")


class Contributor(Role):
    term = RdfTerm("http://www.w3.org/ns/prov#Contributor", "Contributor")


class Publisher(Role):
    term = RdfTerm("http://www.w3.org/ns/prov#Publisher", "Publisher")


class RightsHolder(Role):
    term = RdfTerm("http://www.w3.org/ns/prov#RightsHolder", "RightsHolder")


class ServiceDescription(SoftwareAgent):
    term = RdfTerm("http://www.w3.org/ns/prov#ServiceDescription", "ServiceDescription")


class DirectQueryService(SoftwareAgent):
    term = RdfTerm("http://www.w3.org/ns/prov#DirectQueryService", "DirectQueryService")


class Create(Contribute):
    term = RdfTerm("http://www.w3.org/ns/prov#Create", "Create")


class Communication(ActivityInfluence):
    term = RdfTerm("http://www.w3.org/ns/prov#Communication", "Communication")


class Generation(ActivityInfluence, InstantaneousEvent):
    term = RdfTerm("http://www.w3.org/ns/prov#Generation", "Generation")


class Invalidation(ActivityInfluence, InstantaneousEvent):
    term = RdfTerm("http://www.w3.org/ns/prov#Invalidation", "Invalidation")


class Association(AgentInfluence):
    term = RdfTerm("http://www.w3.org/ns/prov#Association", "Association")


class Attribution(AgentInfluence):
    term = RdfTerm("http://www.w3.org/ns/prov#Attribution", "Attribution")


class Delegation(AgentInfluence):
    term = RdfTerm("http://www.w3.org/ns/prov#Delegation", "Delegation")


class Derivation(EntityInfluence):
    term = RdfTerm("http://www.w3.org/ns/prov#Derivation", "Derivation")


class End(EntityInfluence, InstantaneousEvent):
    term = RdfTerm("http://www.w3.org/ns/prov#End", "End")


class Start(EntityInfluence, InstantaneousEvent):
    term = RdfTerm("http://www.w3.org/ns/prov#Start", "Start")


class Usage(EntityInfluence, InstantaneousEvent):
    term = RdfTerm("http://www.w3.org/ns/prov#Usage", "Usage")


class EmptyCollection(Collection):
    term = RdfTerm("http://www.w3.org/ns/prov#EmptyCollection", "EmptyCollection")


class Creator(Contributor):
    term = RdfTerm("http://www.w3.org/ns/prov#Creator", "Creator")


class PrimarySource(Derivation):
    term = RdfTerm("http://www.w3.org/ns/prov#PrimarySource", "PrimarySource")


class Quotation(Derivation):
    term = RdfTerm("http://www.w3.org/ns/prov#Quotation", "Quotation")


class Revision(Derivation):
    term = RdfTerm("http://www.w3.org/ns/prov#Revision", "Revision")


class Insertion(Derivation):
    term = RdfTerm("http://www.w3.org/ns/prov#Insertion", "Insertion")


class Removal(Derivation):
    term = RdfTerm("http://www.w3.org/ns/prov#Removal", "Removal")


class EmptyDictionary(EmptyCollection, Dictionary):
    term = RdfTerm("http://www.w3.org/ns/prov#EmptyDictionary", "EmptyDictionary")


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


class specializationOf(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#specializationOf", "specializationOf")


class todo(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#todo", "todo")


class unqualifiedForm(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#unqualifiedForm", "unqualifiedForm")


class wasRevisionOf(RdfProperty[prov.Entity]):
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


class pairEntity(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#pairEntity", "pairEntity")


class actedOnBehalfOf(RdfProperty[prov.Agent]):
    term = RdfTerm("http://www.w3.org/ns/prov#actedOnBehalfOf", "actedOnBehalfOf")


class activity(RdfProperty[prov.Activity]):
    term = RdfTerm("http://www.w3.org/ns/prov#activity", "activity")


class agent(RdfProperty[prov.Agent]):
    term = RdfTerm("http://www.w3.org/ns/prov#agent", "agent")


class alternateOf(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#alternateOf", "alternateOf")


class atLocation(RdfProperty[prov.Location]):
    term = RdfTerm("http://www.w3.org/ns/prov#atLocation", "atLocation")


class entity(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#entity", "entity")


class generated(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#generated", "generated")


class hadActivity(RdfProperty[prov.Activity]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadActivity", "hadActivity")


class hadGeneration(RdfProperty[prov.Generation]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadGeneration", "hadGeneration")


class hadMember(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadMember", "hadMember")


class hadPlan(RdfProperty[prov.Plan]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadPlan", "hadPlan")


class hadPrimarySource(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadPrimarySource", "hadPrimarySource")


class hadRole(RdfProperty[prov.Role]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadRole", "hadRole")


class hadUsage(RdfProperty[prov.Usage]):
    term = RdfTerm("http://www.w3.org/ns/prov#hadUsage", "hadUsage")


class influenced(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#influenced", "influenced")


class influencer(RdfProperty[owl.Thing]):
    term = RdfTerm("http://www.w3.org/ns/prov#influencer", "influencer")


class invalidated(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#invalidated", "invalidated")


class qualifiedAssociation(RdfProperty[prov.Association]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedAssociation", "qualifiedAssociation"
    )


class qualifiedAttribution(RdfProperty[prov.Attribution]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedAttribution", "qualifiedAttribution"
    )


class qualifiedCommunication(RdfProperty[prov.Communication]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedCommunication", "qualifiedCommunication"
    )


class qualifiedDelegation(RdfProperty[prov.Delegation]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedDelegation", "qualifiedDelegation"
    )


class qualifiedDerivation(RdfProperty[prov.Derivation]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedDerivation", "qualifiedDerivation"
    )


class qualifiedEnd(RdfProperty[prov.End]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedEnd", "qualifiedEnd")


class qualifiedGeneration(RdfProperty[prov.Generation]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedGeneration", "qualifiedGeneration"
    )


class qualifiedInfluence(RdfProperty[prov.Influence]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedInfluence", "qualifiedInfluence")


class qualifiedInvalidation(RdfProperty[prov.Invalidation]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedInvalidation", "qualifiedInvalidation"
    )


class qualifiedPrimarySource(RdfProperty[prov.PrimarySource]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#qualifiedPrimarySource", "qualifiedPrimarySource"
    )


class qualifiedQuotation(RdfProperty[prov.Quotation]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedQuotation", "qualifiedQuotation")


class qualifiedRevision(RdfProperty[prov.Revision]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedRevision", "qualifiedRevision")


class qualifiedStart(RdfProperty[prov.Start]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedStart", "qualifiedStart")


class qualifiedUsage(RdfProperty[prov.Usage]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedUsage", "qualifiedUsage")


class used(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#used", "used")


class wasAssociatedWith(RdfProperty[prov.Agent]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasAssociatedWith", "wasAssociatedWith")


class wasAttributedTo(RdfProperty[prov.Agent]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasAttributedTo", "wasAttributedTo")


class wasDerivedFrom(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasDerivedFrom", "wasDerivedFrom")


class wasEndedBy(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasEndedBy", "wasEndedBy")


class wasGeneratedBy(RdfProperty[prov.Activity]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasGeneratedBy", "wasGeneratedBy")


class wasInfluencedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasInfluencedBy", "wasInfluencedBy")


class wasInformedBy(RdfProperty[prov.Activity]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasInformedBy", "wasInformedBy")


class wasInvalidatedBy(RdfProperty[prov.Activity]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasInvalidatedBy", "wasInvalidatedBy")


class wasQuotedFrom(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#wasQuotedFrom", "wasQuotedFrom")


class wasStartedBy(RdfProperty[prov.Entity]):
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


class dictionary(RdfProperty[prov.Dictionary]):
    term = RdfTerm("http://www.w3.org/ns/prov#dictionary", "dictionary")


class derivedByInsertionFrom(RdfProperty[prov.Dictionary]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#derivedByInsertionFrom", "derivedByInsertionFrom"
    )


class derivedByRemovalFrom(RdfProperty[prov.Dictionary]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#derivedByRemovalFrom", "derivedByRemovalFrom"
    )


class insertedKeyEntityPair(RdfProperty[prov.KeyEntityPair]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#insertedKeyEntityPair", "insertedKeyEntityPair"
    )


class hadDictionaryMember(RdfProperty[prov.KeyEntityPair]):
    term = RdfTerm(
        "http://www.w3.org/ns/prov#hadDictionaryMember", "hadDictionaryMember"
    )


class qualifiedInsertion(RdfProperty[prov.Insertion]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedInsertion", "qualifiedInsertion")


class qualifiedRemoval(RdfProperty[prov.Removal]):
    term = RdfTerm("http://www.w3.org/ns/prov#qualifiedRemoval", "qualifiedRemoval")


class asInBundle(RdfProperty[prov.Bundle]):
    term = RdfTerm("http://www.w3.org/ns/prov#asInBundle", "asInBundle")


class mentionOf(RdfProperty[prov.Entity]):
    term = RdfTerm("http://www.w3.org/ns/prov#mentionOf", "mentionOf")
