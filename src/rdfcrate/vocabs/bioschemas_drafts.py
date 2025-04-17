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

class Enzyme(schemaorg.BioChemEntity):
    term = RdfTerm('Enzyme', 'https://bioschemas.org/draft_terms/Enzyme', [])

class BioChemStructure(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemStructure', 'https://bioschemas.org/draft_terms/BioChemStructure', [])

class BioChemEntity(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemEntity', 'https://bioschemas.org/draft_terms/BioChemEntity', [])

class DNA(schemaorg.BioChemEntity):
    term = RdfTerm('DNA', 'https://bioschemas.org/draft_terms/DNA', [])

class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm('TaxonName', 'https://bioschemas.org/draft_terms/TaxonName', [])

class Study(schemaorg.CreativeWork):
    term = RdfTerm('Study', 'https://bioschemas.org/draft_terms/Study', [])

class SequenceMatchingModel(schemaorg.CreativeWork):
    term = RdfTerm('SequenceMatchingModel', 'https://bioschemas.org/draft_terms/SequenceMatchingModel', [])

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

class reagent(RdfProperty[schemaorg.DefinedTerm | schemaorg.ChemicalSubstance | schemaorg.URL | schemaorg.PropertyValue | schemaorg.BioChemEntity | schemaorg.MolecularEntity | schemaorg.Text]):
    term = RdfTerm('reagent', 'https://bioschemas.org/draft_terms/reagent', [])

class labEquipment(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('labEquipment', 'https://bioschemas.org/draft_terms/labEquipment', [])

class scientificName(RdfProperty[schemaorg.URL | schemaorg.Text | bioschemas_drafts.TaxonName]):
    term = RdfTerm('scientificName', 'https://bioschemas.org/draft_terms/scientificName', [])

class taxonomicRange(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Taxon]):
    term = RdfTerm('taxonomicRange', 'https://bioschemas.org/draft_terms/taxonomicRange', [])

class hasAssociatedBioChemEntity(RdfProperty[schemaorg.Protein | bioschemas_drafts.RNA]):
    term = RdfTerm('hasAssociatedBioChemEntity', 'https://bioschemas.org/draft_terms/hasAssociatedBioChemEntity', [])

class studyProcess(RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('studyProcess', 'https://bioschemas.org/draft_terms/studyProcess', [])

class protocolAdvantage(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('protocolAdvantage', 'https://bioschemas.org/draft_terms/protocolAdvantage', [])

class optimalTemperature(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm('optimalTemperature', 'https://bioschemas.org/draft_terms/optimalTemperature', [])

class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasStatus', 'https://bioschemas.org/draft_terms/hasStatus', [])

class protocolOutcome(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('protocolOutcome', 'https://bioschemas.org/draft_terms/protocolOutcome', [])

class intendedUse(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('intendedUse', 'https://bioschemas.org/draft_terms/intendedUse', [])

class anatomicalLocation(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('anatomicalLocation', 'https://bioschemas.org/draft_terms/anatomicalLocation', [])

class bioSample(RdfProperty[bioschemas.BioSample | schemaorg.Taxon | schemaorg.Text | schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.BioChemEntity]):
    term = RdfTerm('bioSample', 'https://bioschemas.org/draft_terms/bioSample', [])

class studyLocation(RdfProperty[schemaorg.Place | schemaorg.AdministrativeArea]):
    term = RdfTerm('studyLocation', 'https://bioschemas.org/draft_terms/studyLocation', [])

class isCodingRNA(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isCodingRNA', 'https://bioschemas.org/draft_terms/isCodingRNA', [])

class hasKineticRate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasKineticRate', 'https://bioschemas.org/draft_terms/hasKineticRate', [])

class hasSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasSequence', 'https://bioschemas.org/draft_terms/hasSequence', [])

class studySubject(RdfProperty[schemaorg.BioChemEntity | schemaorg.MedicalEntity]):
    term = RdfTerm('studySubject', 'https://bioschemas.org/draft_terms/studySubject', [])

class protocolApplication(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('protocolApplication', 'https://bioschemas.org/draft_terms/protocolApplication', [])

class startDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('startDate', 'https://bioschemas.org/draft_terms/startDate', [])

class hasSequenceAnnotation(RdfProperty[schemaorg.URL | bioschemas_drafts.SequenceAnnotation]):
    term = RdfTerm('hasSequenceAnnotation', 'https://bioschemas.org/draft_terms/hasSequenceAnnotation', [])

class isLocatedInSubcellularLocation(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('isLocatedInSubcellularLocation', 'https://bioschemas.org/draft_terms/isLocatedInSubcellularLocation', [])

class expressedIn(RdfProperty[schemaorg.BioChemEntity | schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem | schemaorg.DefinedTerm]):
    term = RdfTerm('expressedIn', 'https://bioschemas.org/draft_terms/expressedIn', [])

class protocolLimitation(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('protocolLimitation', 'https://bioschemas.org/draft_terms/protocolLimitation', [])

class hasCofactor(RdfProperty[schemaorg.ChemicalSubstance]):
    term = RdfTerm('hasCofactor', 'https://bioschemas.org/draft_terms/hasCofactor', [])

class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm('additionalProperty', 'https://bioschemas.org/draft_terms/additionalProperty', [])

class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm('alternativeOf', 'https://bioschemas.org/draft_terms/alternativeOf', [])

class isInvolvedInBiologicalProcess(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('isInvolvedInBiologicalProcess', 'https://bioschemas.org/draft_terms/isInvolvedInBiologicalProcess', [])

class creationMethod(RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('creationMethod', 'https://bioschemas.org/draft_terms/creationMethod', [])

class match(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('match', 'https://bioschemas.org/draft_terms/match', [])

class startUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('startUncertainty', 'https://bioschemas.org/draft_terms/startUncertainty', [])

class childTaxon(RdfProperty[schemaorg.URL | schemaorg.Taxon | schemaorg.Text]):
    term = RdfTerm('childTaxon', 'https://bioschemas.org/draft_terms/childTaxon', [])

class sequenceValue(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('sequenceValue', 'https://bioschemas.org/draft_terms/sequenceValue', [])

class massResolution(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm('massResolution', 'https://bioschemas.org/draft_terms/massResolution', [])

class rangeStart(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('rangeStart', 'https://bioschemas.org/draft_terms/rangeStart', [])

class isMatchedBy(RdfProperty[bioschemas_drafts.SequenceMatchingModel]):
    term = RdfTerm('isMatchedBy', 'https://bioschemas.org/draft_terms/isMatchedBy', [])

class associatedDisease(RdfProperty[schemaorg.MedicalCondition | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('associatedDisease', 'https://bioschemas.org/draft_terms/associatedDisease', [])

class biologicalType(RdfProperty[schemaorg.BioChemEntity | schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('biologicalType', 'https://bioschemas.org/draft_terms/biologicalType', [])

class encodesBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('encodesBioChemEntity', 'https://bioschemas.org/draft_terms/encodesBioChemEntity', [])

class ethicalLegalSocial(RdfProperty[schemaorg.Text]):
    term = RdfTerm('ethicalLegalSocial', 'https://bioschemas.org/draft_terms/ethicalLegalSocial', [])

class modelSignature(RdfProperty[schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm('modelSignature', 'https://bioschemas.org/draft_terms/modelSignature', [])

class taxonRank(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm('taxonRank', 'https://bioschemas.org/draft_terms/taxonRank', [])

class hasMolecularFunction(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('hasMolecularFunction', 'https://bioschemas.org/draft_terms/hasMolecularFunction', [])

class modelDataset(RdfProperty[schemaorg.Dataset]):
    term = RdfTerm('modelDataset', 'https://bioschemas.org/draft_terms/modelDataset', [])

class studyDomain(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('studyDomain', 'https://bioschemas.org/draft_terms/studyDomain', [])

class optimalPH(RdfProperty[schemaorg.Number]):
    term = RdfTerm('optimalPH', 'https://bioschemas.org/draft_terms/optimalPH', [])

class computationalTool(RdfProperty[schemaorg.SoftwareApplication | bioschemas.ComputationalWorkflow | schemaorg.DefinedTerm | schemaorg.SoftwareSourceCode | schemaorg.PropertyValue]):
    term = RdfTerm('computationalTool', 'https://bioschemas.org/draft_terms/computationalTool', [])

class valueReference(RdfProperty[schemaorg.QuantitativeValue | schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Enumeration | schemaorg.StructuredValue | schemaorg.QualitativeValue | schemaorg.Text]):
    term = RdfTerm('valueReference', 'https://bioschemas.org/draft_terms/valueReference', [])

class sample(RdfProperty[schemaorg.Thing | schemaorg.PropertyValue | schemaorg.DefinedTerm]):
    term = RdfTerm('sample', 'https://bioschemas.org/draft_terms/sample', [])

class endDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('endDate', 'https://bioschemas.org/draft_terms/endDate', [])

class alternateScientificName(RdfProperty[schemaorg.URL | schemaorg.Text | bioschemas_drafts.TaxonName]):
    term = RdfTerm('alternateScientificName', 'https://bioschemas.org/draft_terms/alternateScientificName', [])

class rangeEnd(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('rangeEnd', 'https://bioschemas.org/draft_terms/rangeEnd', [])

class hasCoenzyme(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('hasCoenzyme', 'https://bioschemas.org/draft_terms/hasCoenzyme', [])

class sequenceOrientation(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('sequenceOrientation', 'https://bioschemas.org/draft_terms/sequenceOrientation', [])

class relatedStudy(RdfProperty[bioschemas_drafts.Study]):
    term = RdfTerm('relatedStudy', 'https://bioschemas.org/draft_terms/relatedStudy', [])

class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasBioPolymerSequence', 'https://bioschemas.org/draft_terms/hasBioPolymerSequence', [])

class sequenceLocation(RdfProperty[bioschemas_drafts.SequenceRange]):
    term = RdfTerm('sequenceLocation', 'https://bioschemas.org/draft_terms/sequenceLocation', [])

class boundMolecule(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.BioChemEntity | schemaorg.MolecularEntity | schemaorg.ChemicalSubstance]):
    term = RdfTerm('boundMolecule', 'https://bioschemas.org/draft_terms/boundMolecule', [])

class bioChemAssociation(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('bioChemAssociation', 'https://bioschemas.org/draft_terms/bioChemAssociation', [])

class endUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('endUncertainty', 'https://bioschemas.org/draft_terms/endUncertainty', [])

class parentTaxon(RdfProperty[schemaorg.Taxon | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('parentTaxon', 'https://bioschemas.org/draft_terms/parentTaxon', [])