from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs
from rdfcrate.rdftype import RdfType
from rdfcrate.vocabs import dc


class AgentClass(rdfs.Class):
    term = RdfTerm("http://purl.org/dc/terms/AgentClass", "AgentClass")


class Agent(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/Agent", "Agent")


class BibliographicResource(RdfClass):
    term = RdfTerm(
        "http://purl.org/dc/terms/BibliographicResource", "BibliographicResource"
    )


class Frequency(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/Frequency", "Frequency")


class LocationPeriodOrJurisdiction(RdfClass):
    term = RdfTerm(
        "http://purl.org/dc/terms/LocationPeriodOrJurisdiction",
        "LocationPeriodOrJurisdiction",
    )


class RightsStatement(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/RightsStatement", "RightsStatement")


class LinguisticSystem(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/LinguisticSystem", "LinguisticSystem")


class MediaTypeOrExtent(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/MediaTypeOrExtent", "MediaTypeOrExtent")


class MethodOfAccrual(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/MethodOfAccrual", "MethodOfAccrual")


class MethodOfInstruction(RdfClass):
    term = RdfTerm(
        "http://purl.org/dc/terms/MethodOfInstruction", "MethodOfInstruction"
    )


class PhysicalResource(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/PhysicalResource", "PhysicalResource")


class Policy(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/Policy", "Policy")


class ProvenanceStatement(RdfClass):
    term = RdfTerm(
        "http://purl.org/dc/terms/ProvenanceStatement", "ProvenanceStatement"
    )


class Standard(RdfClass):
    term = RdfTerm("http://purl.org/dc/terms/Standard", "Standard")


class Jurisdiction(LocationPeriodOrJurisdiction):
    term = RdfTerm("http://purl.org/dc/terms/Jurisdiction", "Jurisdiction")


class Location(LocationPeriodOrJurisdiction):
    term = RdfTerm("http://purl.org/dc/terms/Location", "Location")


class PeriodOfTime(LocationPeriodOrJurisdiction):
    term = RdfTerm("http://purl.org/dc/terms/PeriodOfTime", "PeriodOfTime")


class LicenseDocument(RightsStatement):
    term = RdfTerm("http://purl.org/dc/terms/LicenseDocument", "LicenseDocument")


class MediaType(MediaTypeOrExtent):
    term = RdfTerm("http://purl.org/dc/terms/MediaType", "MediaType")


class SizeOrDuration(MediaTypeOrExtent):
    term = RdfTerm("http://purl.org/dc/terms/SizeOrDuration", "SizeOrDuration")


class FileFormat(MediaType):
    term = RdfTerm("http://purl.org/dc/terms/FileFormat", "FileFormat")


class PhysicalMedium(MediaType):
    term = RdfTerm("http://purl.org/dc/terms/PhysicalMedium", "PhysicalMedium")


class abstract(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/abstract", "abstract")


class accessRights(RdfProperty[dc.RightsStatement]):
    term = RdfTerm("http://purl.org/dc/terms/accessRights", "accessRights")


class accrualMethod(RdfProperty[dc.MethodOfAccrual]):
    term = RdfTerm("http://purl.org/dc/terms/accrualMethod", "accrualMethod")


class accrualPeriodicity(RdfProperty[dc.Frequency]):
    term = RdfTerm("http://purl.org/dc/terms/accrualPeriodicity", "accrualPeriodicity")


class accrualPolicy(RdfProperty[dc.Policy]):
    term = RdfTerm("http://purl.org/dc/terms/accrualPolicy", "accrualPolicy")


class alternative(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/alternative", "alternative")


class audience(RdfProperty[dc.AgentClass]):
    term = RdfTerm("http://purl.org/dc/terms/audience", "audience")


class available(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/available", "available")


class bibliographicCitation(RdfProperty[rdfs.Literal]):
    term = RdfTerm(
        "http://purl.org/dc/terms/bibliographicCitation", "bibliographicCitation"
    )


class conformsTo(RdfProperty[dc.Standard]):
    term = RdfTerm("http://purl.org/dc/terms/conformsTo", "conformsTo")


class contributor(RdfProperty[dc.Agent]):
    term = RdfTerm("http://purl.org/dc/terms/contributor", "contributor")


class coverage(RdfProperty[dc.Jurisdiction | dc.Location]):
    term = RdfTerm("http://purl.org/dc/terms/coverage", "coverage")


class created(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/created", "created")


class creator(RdfProperty[dc.Agent]):
    term = RdfTerm("http://purl.org/dc/terms/creator", "creator")


class date(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/date", "date")


class dateAccepted(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/dateAccepted", "dateAccepted")


class dateCopyrighted(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/dateCopyrighted", "dateCopyrighted")


class dateSubmitted(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/dateSubmitted", "dateSubmitted")


class description(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/description", "description")


class educationLevel(RdfProperty[dc.AgentClass]):
    term = RdfTerm("http://purl.org/dc/terms/educationLevel", "educationLevel")


class extent(RdfProperty[dc.SizeOrDuration]):
    term = RdfTerm("http://purl.org/dc/terms/extent", "extent")


class format(RdfProperty[dc.MediaType]):
    term = RdfTerm("http://purl.org/dc/terms/format", "format")


class hasFormat(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/hasFormat", "hasFormat")


class hasPart(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/hasPart", "hasPart")


class hasVersion(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/hasVersion", "hasVersion")


class identifier(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/identifier", "identifier")


class instructionalMethod(RdfProperty[dc.MethodOfInstruction]):
    term = RdfTerm(
        "http://purl.org/dc/terms/instructionalMethod", "instructionalMethod"
    )


class isFormatOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/isFormatOf", "isFormatOf")


class isPartOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/isPartOf", "isPartOf")


class isReferencedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/isReferencedBy", "isReferencedBy")


class isReplacedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/isReplacedBy", "isReplacedBy")


class isRequiredBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/isRequiredBy", "isRequiredBy")


class isVersionOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/isVersionOf", "isVersionOf")


class issued(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/issued", "issued")


class language(RdfProperty[dc.LinguisticSystem]):
    term = RdfTerm("http://purl.org/dc/terms/language", "language")


class license(RdfProperty[dc.LicenseDocument]):
    term = RdfTerm("http://purl.org/dc/terms/license", "license")


class mediator(RdfProperty[dc.AgentClass]):
    term = RdfTerm("http://purl.org/dc/terms/mediator", "mediator")


class medium(RdfProperty[dc.PhysicalMedium]):
    term = RdfTerm("http://purl.org/dc/terms/medium", "medium")


class modified(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/modified", "modified")


class provenance(RdfProperty[dc.ProvenanceStatement]):
    term = RdfTerm("http://purl.org/dc/terms/provenance", "provenance")


class publisher(RdfProperty[dc.Agent]):
    term = RdfTerm("http://purl.org/dc/terms/publisher", "publisher")


class references(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/references", "references")


class relation(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/relation", "relation")


class replaces(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/replaces", "replaces")


class requires(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/requires", "requires")


class rights(RdfProperty[dc.RightsStatement]):
    term = RdfTerm("http://purl.org/dc/terms/rights", "rights")


class rightsHolder(RdfProperty[dc.Agent]):
    term = RdfTerm("http://purl.org/dc/terms/rightsHolder", "rightsHolder")


class source(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/source", "source")


class spatial(RdfProperty[dc.Location]):
    term = RdfTerm("http://purl.org/dc/terms/spatial", "spatial")


class subject(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/subject", "subject")


class tableOfContents(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/tableOfContents", "tableOfContents")


class temporal(RdfProperty[dc.PeriodOfTime]):
    term = RdfTerm("http://purl.org/dc/terms/temporal", "temporal")


class title(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/title", "title")


class type(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/type", "type")


class valid(RdfProperty[rdfs.Literal]):
    term = RdfTerm("http://purl.org/dc/terms/valid", "valid")
