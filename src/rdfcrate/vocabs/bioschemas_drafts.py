from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import schemaorg
from rdfcrate.vocabs import bioschemas
from rdfcrate.vocabs import bioschemas_drafts

class LabProtocol(schemaorg.HowTo):
    term = RdfTerm('LabProtocol', 'https://bioschemas.org/draft_terms/LabProtocol', [])

class DNA(schemaorg.BioChemEntity):
    term = RdfTerm('DNA', 'https://bioschemas.org/draft_terms/DNA', [])

class BioChemStructure(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemStructure', 'https://bioschemas.org/draft_terms/BioChemStructure', [])

class BioChemEntity(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemEntity', 'https://bioschemas.org/draft_terms/BioChemEntity', [])

class Enzyme(schemaorg.BioChemEntity):
    term = RdfTerm('Enzyme', 'https://bioschemas.org/draft_terms/Enzyme', [])

class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm('TaxonName', 'https://bioschemas.org/draft_terms/TaxonName', [])

class SequenceMatchingModel(schemaorg.CreativeWork):
    term = RdfTerm('SequenceMatchingModel', 'https://bioschemas.org/draft_terms/SequenceMatchingModel', [])

class Study(schemaorg.CreativeWork):
    term = RdfTerm('Study', 'https://bioschemas.org/draft_terms/Study', [])

class RNA(bioschemas.BioChemEntity):
    term = RdfTerm('RNA', 'https://bioschemas.org/draft_terms/RNA', [])

class SequenceAnnotation(bioschemas.BioChemEntity):
    term = RdfTerm('SequenceAnnotation', 'https://bioschemas.org/draft_terms/SequenceAnnotation', [])

class SequenceRange(bioschemas.BioChemEntity):
    term = RdfTerm('SequenceRange', 'https://bioschemas.org/draft_terms/SequenceRange', [])

class Sample(schemaorg.Thing):
    term = RdfTerm('Sample', 'https://bioschemas.org/draft_terms/Sample', [])

class Phenotype(schemaorg.Thing):
    term = RdfTerm('Phenotype', 'https://bioschemas.org/draft_terms/Phenotype', [])

class Taxon(schemaorg.Thing):
    term = RdfTerm('Taxon', 'https://bioschemas.org/draft_terms/Taxon', [])

class Gene(BioChemEntity):
    term = RdfTerm('Gene', 'https://bioschemas.org/draft_terms/Gene', [])

class Protein(BioChemEntity):
    term = RdfTerm('Protein', 'https://bioschemas.org/draft_terms/Protein', [])

@dataclass(frozen=True)
class reagent(RdfProperty):
    term = RdfTerm('reagent', 'https://bioschemas.org/draft_terms/reagent', [])
    object: schemaorg.BioChemEntity | schemaorg.ChemicalSubstance | schemaorg.DefinedTerm | schemaorg.MolecularEntity | schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class labEquipment(RdfProperty):
    term = RdfTerm('labEquipment', 'https://bioschemas.org/draft_terms/labEquipment', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class scientificName(RdfProperty):
    term = RdfTerm('scientificName', 'https://bioschemas.org/draft_terms/scientificName', [])
    object: bioschemas_drafts.TaxonName | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class taxonomicRange(RdfProperty):
    term = RdfTerm('taxonomicRange', 'https://bioschemas.org/draft_terms/taxonomicRange', [])
    object: schemaorg.DefinedTerm | schemaorg.Text | schemaorg.URL | schemaorg.Taxon

@dataclass(frozen=True)
class hasAssociatedBioChemEntity(RdfProperty):
    term = RdfTerm('hasAssociatedBioChemEntity', 'https://bioschemas.org/draft_terms/hasAssociatedBioChemEntity', [])
    object: schemaorg.Protein | bioschemas_drafts.RNA

@dataclass(frozen=True)
class studyProcess(RdfProperty):
    term = RdfTerm('studyProcess', 'https://bioschemas.org/draft_terms/studyProcess', [])
    object: schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class protocolAdvantage(RdfProperty):
    term = RdfTerm('protocolAdvantage', 'https://bioschemas.org/draft_terms/protocolAdvantage', [])
    object: schemaorg.Text | schemaorg.CreativeWork

@dataclass(frozen=True)
class optimalTemperature(RdfProperty):
    term = RdfTerm('optimalTemperature', 'https://bioschemas.org/draft_terms/optimalTemperature', [])
    object: schemaorg.Quantity

@dataclass(frozen=True)
class hasStatus(RdfProperty):
    term = RdfTerm('hasStatus', 'https://bioschemas.org/draft_terms/hasStatus', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class protocolOutcome(RdfProperty):
    term = RdfTerm('protocolOutcome', 'https://bioschemas.org/draft_terms/protocolOutcome', [])
    object: schemaorg.Text | schemaorg.CreativeWork

@dataclass(frozen=True)
class intendedUse(RdfProperty):
    term = RdfTerm('intendedUse', 'https://bioschemas.org/draft_terms/intendedUse', [])
    object: schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm

@dataclass(frozen=True)
class anatomicalLocation(RdfProperty):
    term = RdfTerm('anatomicalLocation', 'https://bioschemas.org/draft_terms/anatomicalLocation', [])
    object: schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm

@dataclass(frozen=True)
class bioSample(RdfProperty):
    term = RdfTerm('bioSample', 'https://bioschemas.org/draft_terms/bioSample', [])
    object: schemaorg.BioChemEntity | bioschemas.BioSample | schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.Taxon | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class studyLocation(RdfProperty):
    term = RdfTerm('studyLocation', 'https://bioschemas.org/draft_terms/studyLocation', [])
    object: schemaorg.Place | schemaorg.AdministrativeArea

@dataclass(frozen=True)
class isCodingRNA(RdfProperty):
    term = RdfTerm('isCodingRNA', 'https://bioschemas.org/draft_terms/isCodingRNA', [])
    object: schemaorg.Boolean

@dataclass(frozen=True)
class hasKineticRate(RdfProperty):
    term = RdfTerm('hasKineticRate', 'https://bioschemas.org/draft_terms/hasKineticRate', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class hasSequence(RdfProperty):
    term = RdfTerm('hasSequence', 'https://bioschemas.org/draft_terms/hasSequence', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class studySubject(RdfProperty):
    term = RdfTerm('studySubject', 'https://bioschemas.org/draft_terms/studySubject', [])
    object: schemaorg.MedicalEntity | schemaorg.BioChemEntity

@dataclass(frozen=True)
class protocolApplication(RdfProperty):
    term = RdfTerm('protocolApplication', 'https://bioschemas.org/draft_terms/protocolApplication', [])
    object: schemaorg.Text | schemaorg.CreativeWork

@dataclass(frozen=True)
class startDate(RdfProperty):
    term = RdfTerm('startDate', 'https://bioschemas.org/draft_terms/startDate', [])
    object: schemaorg.Date | schemaorg.DateTime

@dataclass(frozen=True)
class hasSequenceAnnotation(RdfProperty):
    term = RdfTerm('hasSequenceAnnotation', 'https://bioschemas.org/draft_terms/hasSequenceAnnotation', [])
    object: schemaorg.URL | bioschemas_drafts.SequenceAnnotation

@dataclass(frozen=True)
class isLocatedInSubcellularLocation(RdfProperty):
    term = RdfTerm('isLocatedInSubcellularLocation', 'https://bioschemas.org/draft_terms/isLocatedInSubcellularLocation', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL

@dataclass(frozen=True)
class expressedIn(RdfProperty):
    term = RdfTerm('expressedIn', 'https://bioschemas.org/draft_terms/expressedIn', [])
    object: schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem | schemaorg.BioChemEntity | schemaorg.DefinedTerm

@dataclass(frozen=True)
class protocolLimitation(RdfProperty):
    term = RdfTerm('protocolLimitation', 'https://bioschemas.org/draft_terms/protocolLimitation', [])
    object: schemaorg.Text | schemaorg.CreativeWork

@dataclass(frozen=True)
class hasCofactor(RdfProperty):
    term = RdfTerm('hasCofactor', 'https://bioschemas.org/draft_terms/hasCofactor', [])
    object: schemaorg.ChemicalSubstance

@dataclass(frozen=True)
class additionalProperty(RdfProperty):
    term = RdfTerm('additionalProperty', 'https://bioschemas.org/draft_terms/additionalProperty', [])
    object: schemaorg.PropertyValue

@dataclass(frozen=True)
class alternativeOf(RdfProperty):
    term = RdfTerm('alternativeOf', 'https://bioschemas.org/draft_terms/alternativeOf', [])
    object: schemaorg.Gene

@dataclass(frozen=True)
class isInvolvedInBiologicalProcess(RdfProperty):
    term = RdfTerm('isInvolvedInBiologicalProcess', 'https://bioschemas.org/draft_terms/isInvolvedInBiologicalProcess', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL

@dataclass(frozen=True)
class creationMethod(RdfProperty):
    term = RdfTerm('creationMethod', 'https://bioschemas.org/draft_terms/creationMethod', [])
    object: schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class match(RdfProperty):
    term = RdfTerm('match', 'https://bioschemas.org/draft_terms/match', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class startUncertainty(RdfProperty):
    term = RdfTerm('startUncertainty', 'https://bioschemas.org/draft_terms/startUncertainty', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class childTaxon(RdfProperty):
    term = RdfTerm('childTaxon', 'https://bioschemas.org/draft_terms/childTaxon', [])
    object: schemaorg.Taxon | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class sequenceValue(RdfProperty):
    term = RdfTerm('sequenceValue', 'https://bioschemas.org/draft_terms/sequenceValue', [])
    object: schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class massResolution(RdfProperty):
    term = RdfTerm('massResolution', 'https://bioschemas.org/draft_terms/massResolution', [])
    object: schemaorg.Quantity

@dataclass(frozen=True)
class rangeStart(RdfProperty):
    term = RdfTerm('rangeStart', 'https://bioschemas.org/draft_terms/rangeStart', [])
    object: schemaorg.Integer

@dataclass(frozen=True)
class isMatchedBy(RdfProperty):
    term = RdfTerm('isMatchedBy', 'https://bioschemas.org/draft_terms/isMatchedBy', [])
    object: bioschemas_drafts.SequenceMatchingModel

@dataclass(frozen=True)
class associatedDisease(RdfProperty):
    term = RdfTerm('associatedDisease', 'https://bioschemas.org/draft_terms/associatedDisease', [])
    object: schemaorg.MedicalCondition | schemaorg.PropertyValue | schemaorg.URL

@dataclass(frozen=True)
class biologicalType(RdfProperty):
    term = RdfTerm('biologicalType', 'https://bioschemas.org/draft_terms/biologicalType', [])
    object: schemaorg.BioChemEntity | schemaorg.DefinedTerm | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class encodesBioChemEntity(RdfProperty):
    term = RdfTerm('encodesBioChemEntity', 'https://bioschemas.org/draft_terms/encodesBioChemEntity', [])
    object: bioschemas.BioChemEntity

@dataclass(frozen=True)
class ethicalLegalSocial(RdfProperty):
    term = RdfTerm('ethicalLegalSocial', 'https://bioschemas.org/draft_terms/ethicalLegalSocial', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class modelSignature(RdfProperty):
    term = RdfTerm('modelSignature', 'https://bioschemas.org/draft_terms/modelSignature', [])
    object: schemaorg.Text | schemaorg.PropertyValue

@dataclass(frozen=True)
class taxonRank(RdfProperty):
    term = RdfTerm('taxonRank', 'https://bioschemas.org/draft_terms/taxonRank', [])
    object: schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class hasMolecularFunction(RdfProperty):
    term = RdfTerm('hasMolecularFunction', 'https://bioschemas.org/draft_terms/hasMolecularFunction', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL

@dataclass(frozen=True)
class modelDataset(RdfProperty):
    term = RdfTerm('modelDataset', 'https://bioschemas.org/draft_terms/modelDataset', [])
    object: schemaorg.Dataset

@dataclass(frozen=True)
class studyDomain(RdfProperty):
    term = RdfTerm('studyDomain', 'https://bioschemas.org/draft_terms/studyDomain', [])
    object: schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class optimalPH(RdfProperty):
    term = RdfTerm('optimalPH', 'https://bioschemas.org/draft_terms/optimalPH', [])
    object: schemaorg.Number

@dataclass(frozen=True)
class computationalTool(RdfProperty):
    term = RdfTerm('computationalTool', 'https://bioschemas.org/draft_terms/computationalTool', [])
    object: bioschemas.ComputationalWorkflow | schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.SoftwareApplication | schemaorg.SoftwareSourceCode

@dataclass(frozen=True)
class valueReference(RdfProperty):
    term = RdfTerm('valueReference', 'https://bioschemas.org/draft_terms/valueReference', [])
    object: schemaorg.DefinedTerm | schemaorg.Enumeration | schemaorg.PropertyValue | schemaorg.QualitativeValue | schemaorg.QuantitativeValue | schemaorg.StructuredValue | schemaorg.URL | schemaorg.Text

@dataclass(frozen=True)
class sample(RdfProperty):
    term = RdfTerm('sample', 'https://bioschemas.org/draft_terms/sample', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.Thing

@dataclass(frozen=True)
class endDate(RdfProperty):
    term = RdfTerm('endDate', 'https://bioschemas.org/draft_terms/endDate', [])
    object: schemaorg.Date | schemaorg.DateTime

@dataclass(frozen=True)
class alternateScientificName(RdfProperty):
    term = RdfTerm('alternateScientificName', 'https://bioschemas.org/draft_terms/alternateScientificName', [])
    object: bioschemas_drafts.TaxonName | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class rangeEnd(RdfProperty):
    term = RdfTerm('rangeEnd', 'https://bioschemas.org/draft_terms/rangeEnd', [])
    object: schemaorg.Integer

@dataclass(frozen=True)
class hasCoenzyme(RdfProperty):
    term = RdfTerm('hasCoenzyme', 'https://bioschemas.org/draft_terms/hasCoenzyme', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class sequenceOrientation(RdfProperty):
    term = RdfTerm('sequenceOrientation', 'https://bioschemas.org/draft_terms/sequenceOrientation', [])
    object: schemaorg.Integer

@dataclass(frozen=True)
class relatedStudy(RdfProperty):
    term = RdfTerm('relatedStudy', 'https://bioschemas.org/draft_terms/relatedStudy', [])
    object: bioschemas_drafts.Study

@dataclass(frozen=True)
class hasBioPolymerSequence(RdfProperty):
    term = RdfTerm('hasBioPolymerSequence', 'https://bioschemas.org/draft_terms/hasBioPolymerSequence', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class sequenceLocation(RdfProperty):
    term = RdfTerm('sequenceLocation', 'https://bioschemas.org/draft_terms/sequenceLocation', [])
    object: bioschemas_drafts.SequenceRange

@dataclass(frozen=True)
class boundMolecule(RdfProperty):
    term = RdfTerm('boundMolecule', 'https://bioschemas.org/draft_terms/boundMolecule', [])
    object: schemaorg.BioChemEntity | schemaorg.ChemicalSubstance | schemaorg.MolecularEntity | schemaorg.URL | schemaorg.DefinedTerm

@dataclass(frozen=True)
class bioChemAssociation(RdfProperty):
    term = RdfTerm('bioChemAssociation', 'https://bioschemas.org/draft_terms/bioChemAssociation', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class endUncertainty(RdfProperty):
    term = RdfTerm('endUncertainty', 'https://bioschemas.org/draft_terms/endUncertainty', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class parentTaxon(RdfProperty):
    term = RdfTerm('parentTaxon', 'https://bioschemas.org/draft_terms/parentTaxon', [])
    object: schemaorg.Taxon | schemaorg.Text | schemaorg.URL