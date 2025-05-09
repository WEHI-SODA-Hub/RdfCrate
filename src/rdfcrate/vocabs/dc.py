from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs


class AgentClass(rdfs.Class):
    term = RdfTerm("AgentClass", "http://purl.org/dc/terms/AgentClass", [])


class Agent(RdfClass):
    term = RdfTerm("Agent", "http://purl.org/dc/terms/Agent", [])


class BibliographicResource(RdfClass):
    term = RdfTerm(
        "BibliographicResource", "http://purl.org/dc/terms/BibliographicResource", []
    )


class Frequency(RdfClass):
    term = RdfTerm("Frequency", "http://purl.org/dc/terms/Frequency", [])


class LocationPeriodOrJurisdiction(RdfClass):
    term = RdfTerm(
        "LocationPeriodOrJurisdiction",
        "http://purl.org/dc/terms/LocationPeriodOrJurisdiction",
        [],
    )


class RightsStatement(RdfClass):
    term = RdfTerm("RightsStatement", "http://purl.org/dc/terms/RightsStatement", [])


class LinguisticSystem(RdfClass):
    term = RdfTerm("LinguisticSystem", "http://purl.org/dc/terms/LinguisticSystem", [])


class MediaTypeOrExtent(RdfClass):
    term = RdfTerm(
        "MediaTypeOrExtent", "http://purl.org/dc/terms/MediaTypeOrExtent", []
    )


class MethodOfAccrual(RdfClass):
    term = RdfTerm("MethodOfAccrual", "http://purl.org/dc/terms/MethodOfAccrual", [])


class MethodOfInstruction(RdfClass):
    term = RdfTerm(
        "MethodOfInstruction", "http://purl.org/dc/terms/MethodOfInstruction", []
    )


class PhysicalResource(RdfClass):
    term = RdfTerm("PhysicalResource", "http://purl.org/dc/terms/PhysicalResource", [])


class Policy(RdfClass):
    term = RdfTerm("Policy", "http://purl.org/dc/terms/Policy", [])


class ProvenanceStatement(RdfClass):
    term = RdfTerm(
        "ProvenanceStatement", "http://purl.org/dc/terms/ProvenanceStatement", []
    )


class Standard(RdfClass):
    term = RdfTerm("Standard", "http://purl.org/dc/terms/Standard", ["1.2-DRAFT"])


class Jurisdiction(LocationPeriodOrJurisdiction):
    term = RdfTerm("Jurisdiction", "http://purl.org/dc/terms/Jurisdiction", [])


class Location(LocationPeriodOrJurisdiction):
    term = RdfTerm("Location", "http://purl.org/dc/terms/Location", [])


class PeriodOfTime(LocationPeriodOrJurisdiction):
    term = RdfTerm("PeriodOfTime", "http://purl.org/dc/terms/PeriodOfTime", [])


class LicenseDocument(RightsStatement):
    term = RdfTerm("LicenseDocument", "http://purl.org/dc/terms/LicenseDocument", [])


class MediaType(MediaTypeOrExtent):
    term = RdfTerm("MediaType", "http://purl.org/dc/terms/MediaType", [])


class SizeOrDuration(MediaTypeOrExtent):
    term = RdfTerm("SizeOrDuration", "http://purl.org/dc/terms/SizeOrDuration", [])


class FileFormat(MediaType):
    term = RdfTerm("FileFormat", "http://purl.org/dc/terms/FileFormat", [])


class PhysicalMedium(MediaType):
    term = RdfTerm("PhysicalMedium", "http://purl.org/dc/terms/PhysicalMedium", [])


class abstract(RdfProperty[Identifier]):
    term = RdfTerm("abstract", "http://purl.org/dc/terms/abstract", [])


class accessRights(RdfProperty[Identifier]):
    term = RdfTerm("accessRights", "http://purl.org/dc/terms/accessRights", [])


class accrualMethod(RdfProperty[Identifier]):
    term = RdfTerm("accrualMethod", "http://purl.org/dc/terms/accrualMethod", [])


class accrualPeriodicity(RdfProperty[Identifier]):
    term = RdfTerm(
        "accrualPeriodicity", "http://purl.org/dc/terms/accrualPeriodicity", []
    )


class accrualPolicy(RdfProperty[Identifier]):
    term = RdfTerm("accrualPolicy", "http://purl.org/dc/terms/accrualPolicy", [])


class alternative(RdfProperty[rdfs.Literal]):
    term = RdfTerm("alternative", "http://purl.org/dc/terms/alternative", [])


class audience(RdfProperty[Identifier]):
    term = RdfTerm("audience", "http://purl.org/dc/terms/audience", [])


class available(RdfProperty[rdfs.Literal]):
    term = RdfTerm("available", "http://purl.org/dc/terms/available", [])


class bibliographicCitation(RdfProperty[rdfs.Literal]):
    term = RdfTerm(
        "bibliographicCitation", "http://purl.org/dc/terms/bibliographicCitation", []
    )


class conformsTo(RdfProperty[Identifier]):
    term = RdfTerm(
        "conformsTo", "http://purl.org/dc/terms/conformsTo", ["1.0", "1.1", "1.2-DRAFT"]
    )


class contributor(RdfProperty[Identifier]):
    term = RdfTerm("contributor", "http://purl.org/dc/terms/contributor", [])


class coverage(RdfProperty[Identifier]):
    term = RdfTerm("coverage", "http://purl.org/dc/terms/coverage", [])


class created(RdfProperty[rdfs.Literal]):
    term = RdfTerm("created", "http://purl.org/dc/terms/created", [])


class creator(RdfProperty[Identifier]):
    term = RdfTerm("creator", "http://purl.org/dc/terms/creator", [])


class date(RdfProperty[rdfs.Literal]):
    term = RdfTerm("date", "http://purl.org/dc/terms/date", [])


class dateAccepted(RdfProperty[rdfs.Literal]):
    term = RdfTerm("dateAccepted", "http://purl.org/dc/terms/dateAccepted", [])


class dateCopyrighted(RdfProperty[rdfs.Literal]):
    term = RdfTerm("dateCopyrighted", "http://purl.org/dc/terms/dateCopyrighted", [])


class dateSubmitted(RdfProperty[rdfs.Literal]):
    term = RdfTerm("dateSubmitted", "http://purl.org/dc/terms/dateSubmitted", [])


class description(RdfProperty[Identifier]):
    term = RdfTerm("description", "http://purl.org/dc/terms/description", [])


class educationLevel(RdfProperty[Identifier]):
    term = RdfTerm("educationLevel", "http://purl.org/dc/terms/educationLevel", [])


class extent(RdfProperty[Identifier]):
    term = RdfTerm("extent", "http://purl.org/dc/terms/extent", [])


class format(RdfProperty[Identifier]):
    term = RdfTerm("format", "http://purl.org/dc/terms/format", [])


class hasFormat(RdfProperty[Identifier]):
    term = RdfTerm("hasFormat", "http://purl.org/dc/terms/hasFormat", [])


class hasPart(RdfProperty[Identifier]):
    term = RdfTerm("hasPart", "http://purl.org/dc/terms/hasPart", [])


class hasVersion(RdfProperty[Identifier]):
    term = RdfTerm("hasVersion", "http://purl.org/dc/terms/hasVersion", [])


class identifier(RdfProperty[rdfs.Literal]):
    term = RdfTerm("identifier", "http://purl.org/dc/terms/identifier", [])


class instructionalMethod(RdfProperty[Identifier]):
    term = RdfTerm(
        "instructionalMethod", "http://purl.org/dc/terms/instructionalMethod", []
    )


class isFormatOf(RdfProperty[Identifier]):
    term = RdfTerm("isFormatOf", "http://purl.org/dc/terms/isFormatOf", [])


class isPartOf(RdfProperty[Identifier]):
    term = RdfTerm("isPartOf", "http://purl.org/dc/terms/isPartOf", [])


class isReferencedBy(RdfProperty[Identifier]):
    term = RdfTerm("isReferencedBy", "http://purl.org/dc/terms/isReferencedBy", [])


class isReplacedBy(RdfProperty[Identifier]):
    term = RdfTerm("isReplacedBy", "http://purl.org/dc/terms/isReplacedBy", [])


class isRequiredBy(RdfProperty[Identifier]):
    term = RdfTerm("isRequiredBy", "http://purl.org/dc/terms/isRequiredBy", [])


class isVersionOf(RdfProperty[Identifier]):
    term = RdfTerm("isVersionOf", "http://purl.org/dc/terms/isVersionOf", [])


class issued(RdfProperty[rdfs.Literal]):
    term = RdfTerm("issued", "http://purl.org/dc/terms/issued", [])


class language(RdfProperty[Identifier]):
    term = RdfTerm("language", "http://purl.org/dc/terms/language", [])


class license(RdfProperty[Identifier]):
    term = RdfTerm("license", "http://purl.org/dc/terms/license", [])


class mediator(RdfProperty[Identifier]):
    term = RdfTerm("mediator", "http://purl.org/dc/terms/mediator", [])


class medium(RdfProperty[Identifier]):
    term = RdfTerm("medium", "http://purl.org/dc/terms/medium", [])


class modified(RdfProperty[rdfs.Literal]):
    term = RdfTerm("modified", "http://purl.org/dc/terms/modified", [])


class provenance(RdfProperty[Identifier]):
    term = RdfTerm("provenance", "http://purl.org/dc/terms/provenance", [])


class publisher(RdfProperty[Identifier]):
    term = RdfTerm("publisher", "http://purl.org/dc/terms/publisher", [])


class references(RdfProperty[Identifier]):
    term = RdfTerm("references", "http://purl.org/dc/terms/references", [])


class relation(RdfProperty[Identifier]):
    term = RdfTerm("relation", "http://purl.org/dc/terms/relation", [])


class replaces(RdfProperty[Identifier]):
    term = RdfTerm("replaces", "http://purl.org/dc/terms/replaces", [])


class requires(RdfProperty[Identifier]):
    term = RdfTerm("requires", "http://purl.org/dc/terms/requires", [])


class rights(RdfProperty[Identifier]):
    term = RdfTerm("rights", "http://purl.org/dc/terms/rights", [])


class rightsHolder(RdfProperty[Identifier]):
    term = RdfTerm("rightsHolder", "http://purl.org/dc/terms/rightsHolder", [])


class source(RdfProperty[Identifier]):
    term = RdfTerm("source", "http://purl.org/dc/terms/source", [])


class spatial(RdfProperty[Identifier]):
    term = RdfTerm("spatial", "http://purl.org/dc/terms/spatial", [])


class subject(RdfProperty[Identifier]):
    term = RdfTerm("subject", "http://purl.org/dc/terms/subject", [])


class tableOfContents(RdfProperty[Identifier]):
    term = RdfTerm("tableOfContents", "http://purl.org/dc/terms/tableOfContents", [])


class temporal(RdfProperty[Identifier]):
    term = RdfTerm("temporal", "http://purl.org/dc/terms/temporal", [])


class title(RdfProperty[rdfs.Literal]):
    term = RdfTerm("title", "http://purl.org/dc/terms/title", [])


class type(RdfProperty[Identifier]):
    term = RdfTerm("type", "http://purl.org/dc/terms/type", [])


class valid(RdfProperty[rdfs.Literal]):
    term = RdfTerm("valid", "http://purl.org/dc/terms/valid", [])
