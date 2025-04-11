from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs

class AgentClass(rdfs.Class):
    term = RdfTerm('AgentClass', 'http://purl.org/dc/terms/AgentClass', [])

class Agent(RdfClass):
    term = RdfTerm('Agent', 'http://purl.org/dc/terms/Agent', [])

class BibliographicResource(RdfClass):
    term = RdfTerm('BibliographicResource', 'http://purl.org/dc/terms/BibliographicResource', [])

class Frequency(RdfClass):
    term = RdfTerm('Frequency', 'http://purl.org/dc/terms/Frequency', [])

class LocationPeriodOrJurisdiction(RdfClass):
    term = RdfTerm('LocationPeriodOrJurisdiction', 'http://purl.org/dc/terms/LocationPeriodOrJurisdiction', [])

class RightsStatement(RdfClass):
    term = RdfTerm('RightsStatement', 'http://purl.org/dc/terms/RightsStatement', [])

class LinguisticSystem(RdfClass):
    term = RdfTerm('LinguisticSystem', 'http://purl.org/dc/terms/LinguisticSystem', [])

class MediaTypeOrExtent(RdfClass):
    term = RdfTerm('MediaTypeOrExtent', 'http://purl.org/dc/terms/MediaTypeOrExtent', [])

class MethodOfAccrual(RdfClass):
    term = RdfTerm('MethodOfAccrual', 'http://purl.org/dc/terms/MethodOfAccrual', [])

class MethodOfInstruction(RdfClass):
    term = RdfTerm('MethodOfInstruction', 'http://purl.org/dc/terms/MethodOfInstruction', [])

class PhysicalResource(RdfClass):
    term = RdfTerm('PhysicalResource', 'http://purl.org/dc/terms/PhysicalResource', [])

class Policy(RdfClass):
    term = RdfTerm('Policy', 'http://purl.org/dc/terms/Policy', [])

class ProvenanceStatement(RdfClass):
    term = RdfTerm('ProvenanceStatement', 'http://purl.org/dc/terms/ProvenanceStatement', [])

class Standard(RdfClass):
    term = RdfTerm('Standard', 'http://purl.org/dc/terms/Standard', [])

class Jurisdiction(LocationPeriodOrJurisdiction):
    term = RdfTerm('Jurisdiction', 'http://purl.org/dc/terms/Jurisdiction', [])

class Location(LocationPeriodOrJurisdiction):
    term = RdfTerm('Location', 'http://purl.org/dc/terms/Location', [])

class PeriodOfTime(LocationPeriodOrJurisdiction):
    term = RdfTerm('PeriodOfTime', 'http://purl.org/dc/terms/PeriodOfTime', [])

class LicenseDocument(RightsStatement):
    term = RdfTerm('LicenseDocument', 'http://purl.org/dc/terms/LicenseDocument', [])

class MediaType(MediaTypeOrExtent):
    term = RdfTerm('MediaType', 'http://purl.org/dc/terms/MediaType', [])

class SizeOrDuration(MediaTypeOrExtent):
    term = RdfTerm('SizeOrDuration', 'http://purl.org/dc/terms/SizeOrDuration', [])

class FileFormat(MediaType):
    term = RdfTerm('FileFormat', 'http://purl.org/dc/terms/FileFormat', [])

class PhysicalMedium(MediaType):
    term = RdfTerm('PhysicalMedium', 'http://purl.org/dc/terms/PhysicalMedium', [])

@dataclass(frozen=True)
class abstract(RdfProperty):
    term = RdfTerm('abstract', 'http://purl.org/dc/terms/abstract', [])
    object: Identifier

@dataclass(frozen=True)
class accessRights(RdfProperty):
    term = RdfTerm('accessRights', 'http://purl.org/dc/terms/accessRights', [])
    object: Identifier

@dataclass(frozen=True)
class accrualMethod(RdfProperty):
    term = RdfTerm('accrualMethod', 'http://purl.org/dc/terms/accrualMethod', [])
    object: Identifier

@dataclass(frozen=True)
class accrualPeriodicity(RdfProperty):
    term = RdfTerm('accrualPeriodicity', 'http://purl.org/dc/terms/accrualPeriodicity', [])
    object: Identifier

@dataclass(frozen=True)
class accrualPolicy(RdfProperty):
    term = RdfTerm('accrualPolicy', 'http://purl.org/dc/terms/accrualPolicy', [])
    object: Identifier

@dataclass(frozen=True)
class alternative(RdfProperty):
    term = RdfTerm('alternative', 'http://purl.org/dc/terms/alternative', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class audience(RdfProperty):
    term = RdfTerm('audience', 'http://purl.org/dc/terms/audience', [])
    object: Identifier

@dataclass(frozen=True)
class available(RdfProperty):
    term = RdfTerm('available', 'http://purl.org/dc/terms/available', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class bibliographicCitation(RdfProperty):
    term = RdfTerm('bibliographicCitation', 'http://purl.org/dc/terms/bibliographicCitation', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class conformsTo(RdfProperty):
    term = RdfTerm('conformsTo', 'http://purl.org/dc/terms/conformsTo', ['1.0', '1.1', '1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class contributor(RdfProperty):
    term = RdfTerm('contributor', 'http://purl.org/dc/terms/contributor', [])
    object: Identifier

@dataclass(frozen=True)
class coverage(RdfProperty):
    term = RdfTerm('coverage', 'http://purl.org/dc/terms/coverage', [])
    object: Identifier

@dataclass(frozen=True)
class created(RdfProperty):
    term = RdfTerm('created', 'http://purl.org/dc/terms/created', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class creator(RdfProperty):
    term = RdfTerm('creator', 'http://purl.org/dc/terms/creator', [])
    object: Identifier

@dataclass(frozen=True)
class date(RdfProperty):
    term = RdfTerm('date', 'http://purl.org/dc/terms/date', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class dateAccepted(RdfProperty):
    term = RdfTerm('dateAccepted', 'http://purl.org/dc/terms/dateAccepted', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class dateCopyrighted(RdfProperty):
    term = RdfTerm('dateCopyrighted', 'http://purl.org/dc/terms/dateCopyrighted', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class dateSubmitted(RdfProperty):
    term = RdfTerm('dateSubmitted', 'http://purl.org/dc/terms/dateSubmitted', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class description(RdfProperty):
    term = RdfTerm('description', 'http://purl.org/dc/terms/description', [])
    object: Identifier

@dataclass(frozen=True)
class educationLevel(RdfProperty):
    term = RdfTerm('educationLevel', 'http://purl.org/dc/terms/educationLevel', [])
    object: Identifier

@dataclass(frozen=True)
class extent(RdfProperty):
    term = RdfTerm('extent', 'http://purl.org/dc/terms/extent', [])
    object: Identifier

@dataclass(frozen=True)
class format(RdfProperty):
    term = RdfTerm('format', 'http://purl.org/dc/terms/format', [])
    object: Identifier

@dataclass(frozen=True)
class hasFormat(RdfProperty):
    term = RdfTerm('hasFormat', 'http://purl.org/dc/terms/hasFormat', [])
    object: Identifier

@dataclass(frozen=True)
class hasPart(RdfProperty):
    term = RdfTerm('hasPart', 'http://purl.org/dc/terms/hasPart', [])
    object: Identifier

@dataclass(frozen=True)
class hasVersion(RdfProperty):
    term = RdfTerm('hasVersion', 'http://purl.org/dc/terms/hasVersion', [])
    object: Identifier

@dataclass(frozen=True)
class identifier(RdfProperty):
    term = RdfTerm('identifier', 'http://purl.org/dc/terms/identifier', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class instructionalMethod(RdfProperty):
    term = RdfTerm('instructionalMethod', 'http://purl.org/dc/terms/instructionalMethod', [])
    object: Identifier

@dataclass(frozen=True)
class isFormatOf(RdfProperty):
    term = RdfTerm('isFormatOf', 'http://purl.org/dc/terms/isFormatOf', [])
    object: Identifier

@dataclass(frozen=True)
class isPartOf(RdfProperty):
    term = RdfTerm('isPartOf', 'http://purl.org/dc/terms/isPartOf', [])
    object: Identifier

@dataclass(frozen=True)
class isReferencedBy(RdfProperty):
    term = RdfTerm('isReferencedBy', 'http://purl.org/dc/terms/isReferencedBy', [])
    object: Identifier

@dataclass(frozen=True)
class isReplacedBy(RdfProperty):
    term = RdfTerm('isReplacedBy', 'http://purl.org/dc/terms/isReplacedBy', [])
    object: Identifier

@dataclass(frozen=True)
class isRequiredBy(RdfProperty):
    term = RdfTerm('isRequiredBy', 'http://purl.org/dc/terms/isRequiredBy', [])
    object: Identifier

@dataclass(frozen=True)
class isVersionOf(RdfProperty):
    term = RdfTerm('isVersionOf', 'http://purl.org/dc/terms/isVersionOf', [])
    object: Identifier

@dataclass(frozen=True)
class issued(RdfProperty):
    term = RdfTerm('issued', 'http://purl.org/dc/terms/issued', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class language(RdfProperty):
    term = RdfTerm('language', 'http://purl.org/dc/terms/language', [])
    object: Identifier

@dataclass(frozen=True)
class license(RdfProperty):
    term = RdfTerm('license', 'http://purl.org/dc/terms/license', [])
    object: Identifier

@dataclass(frozen=True)
class mediator(RdfProperty):
    term = RdfTerm('mediator', 'http://purl.org/dc/terms/mediator', [])
    object: Identifier

@dataclass(frozen=True)
class medium(RdfProperty):
    term = RdfTerm('medium', 'http://purl.org/dc/terms/medium', [])
    object: Identifier

@dataclass(frozen=True)
class modified(RdfProperty):
    term = RdfTerm('modified', 'http://purl.org/dc/terms/modified', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class provenance(RdfProperty):
    term = RdfTerm('provenance', 'http://purl.org/dc/terms/provenance', [])
    object: Identifier

@dataclass(frozen=True)
class publisher(RdfProperty):
    term = RdfTerm('publisher', 'http://purl.org/dc/terms/publisher', [])
    object: Identifier

@dataclass(frozen=True)
class references(RdfProperty):
    term = RdfTerm('references', 'http://purl.org/dc/terms/references', [])
    object: Identifier

@dataclass(frozen=True)
class relation(RdfProperty):
    term = RdfTerm('relation', 'http://purl.org/dc/terms/relation', [])
    object: Identifier

@dataclass(frozen=True)
class replaces(RdfProperty):
    term = RdfTerm('replaces', 'http://purl.org/dc/terms/replaces', [])
    object: Identifier

@dataclass(frozen=True)
class requires(RdfProperty):
    term = RdfTerm('requires', 'http://purl.org/dc/terms/requires', [])
    object: Identifier

@dataclass(frozen=True)
class rights(RdfProperty):
    term = RdfTerm('rights', 'http://purl.org/dc/terms/rights', [])
    object: Identifier

@dataclass(frozen=True)
class rightsHolder(RdfProperty):
    term = RdfTerm('rightsHolder', 'http://purl.org/dc/terms/rightsHolder', [])
    object: Identifier

@dataclass(frozen=True)
class source(RdfProperty):
    term = RdfTerm('source', 'http://purl.org/dc/terms/source', [])
    object: Identifier

@dataclass(frozen=True)
class spatial(RdfProperty):
    term = RdfTerm('spatial', 'http://purl.org/dc/terms/spatial', [])
    object: Identifier

@dataclass(frozen=True)
class subject(RdfProperty):
    term = RdfTerm('subject', 'http://purl.org/dc/terms/subject', [])
    object: Identifier

@dataclass(frozen=True)
class tableOfContents(RdfProperty):
    term = RdfTerm('tableOfContents', 'http://purl.org/dc/terms/tableOfContents', [])
    object: Identifier

@dataclass(frozen=True)
class temporal(RdfProperty):
    term = RdfTerm('temporal', 'http://purl.org/dc/terms/temporal', [])
    object: Identifier

@dataclass(frozen=True)
class title(RdfProperty):
    term = RdfTerm('title', 'http://purl.org/dc/terms/title', [])
    object: rdfs.Literal

@dataclass(frozen=True)
class type(RdfProperty):
    term = RdfTerm('type', 'http://purl.org/dc/terms/type', [])
    object: Identifier

@dataclass(frozen=True)
class valid(RdfProperty):
    term = RdfTerm('valid', 'http://purl.org/dc/terms/valid', [])
    object: rdfs.Literal