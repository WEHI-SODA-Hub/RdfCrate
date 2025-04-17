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

class BioChemEntity(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemEntity', 'https://bioschemas.org/draft_terms/BioChemEntity', [])

class DNA(schemaorg.BioChemEntity):
    term = RdfTerm('DNA', 'https://bioschemas.org/draft_terms/DNA', [])

class Enzyme(schemaorg.BioChemEntity):
    term = RdfTerm('Enzyme', 'https://bioschemas.org/draft_terms/Enzyme', [])

class BioChemStructure(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemStructure', 'https://bioschemas.org/draft_terms/BioChemStructure', [])

class Study(schemaorg.CreativeWork):
    term = RdfTerm('Study', 'https://bioschemas.org/draft_terms/Study', [])

class SequenceMatchingModel(schemaorg.CreativeWork):
    term = RdfTerm('SequenceMatchingModel', 'https://bioschemas.org/draft_terms/SequenceMatchingModel', [])

class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm('TaxonName', 'https://bioschemas.org/draft_terms/TaxonName', [])

class RNA(bioschemas.BioChemEntity):
    term = RdfTerm('RNA', 'https://bioschemas.org/draft_terms/RNA', [])

class SequenceAnnotation(bioschemas.BioChemEntity):
    term = RdfTerm('SequenceAnnotation', 'https://bioschemas.org/draft_terms/SequenceAnnotation', [])

class SequenceRange(bioschemas.BioChemEntity):
    term = RdfTerm('SequenceRange', 'https://bioschemas.org/draft_terms/SequenceRange', [])

class Taxon(schemaorg.Thing):
    term = RdfTerm('Taxon', 'https://bioschemas.org/draft_terms/Taxon', [])

class Sample(schemaorg.Thing):
    term = RdfTerm('Sample', 'https://bioschemas.org/draft_terms/Sample', [])

class Phenotype(schemaorg.Thing):
    term = RdfTerm('Phenotype', 'https://bioschemas.org/draft_terms/Phenotype', [])

class Gene(BioChemEntity):
    term = RdfTerm('Gene', 'https://bioschemas.org/draft_terms/Gene', [])

class Protein(BioChemEntity):
    term = RdfTerm('Protein', 'https://bioschemas.org/draft_terms/Protein', [])

class reagent(RdfProperty[schemaorg.ChemicalSubstance | schemaorg.PropertyValue | schemaorg.BioChemEntity | schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm | schemaorg.MolecularEntity]):
    term = RdfTerm('reagent', 'https://bioschemas.org/draft_terms/reagent', [])

class labEquipment(RdfProperty[schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm]):
    term = RdfTerm('labEquipment', 'https://bioschemas.org/draft_terms/labEquipment', [])

class scientificName(RdfProperty[schemaorg.URL | bioschemas_drafts.TaxonName | schemaorg.Text]):
    term = RdfTerm('scientificName', 'https://bioschemas.org/draft_terms/scientificName', [])

class taxonomicRange(RdfProperty[schemaorg.DefinedTerm | schemaorg.Taxon | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('taxonomicRange', 'https://bioschemas.org/draft_terms/taxonomicRange', [])

class hasAssociatedBioChemEntity(RdfProperty[schemaorg.Protein | bioschemas_drafts.RNA]):
    term = RdfTerm('hasAssociatedBioChemEntity', 'https://bioschemas.org/draft_terms/hasAssociatedBioChemEntity', [])

class studyProcess(RdfProperty[schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('studyProcess', 'https://bioschemas.org/draft_terms/studyProcess', [])

class protocolAdvantage(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('protocolAdvantage', 'https://bioschemas.org/draft_terms/protocolAdvantage', [])

class optimalTemperature(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm('optimalTemperature', 'https://bioschemas.org/draft_terms/optimalTemperature', [])

class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasStatus', 'https://bioschemas.org/draft_terms/hasStatus', [])

class protocolOutcome(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('protocolOutcome', 'https://bioschemas.org/draft_terms/protocolOutcome', [])

class intendedUse(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm]):
    term = RdfTerm('intendedUse', 'https://bioschemas.org/draft_terms/intendedUse', [])

class anatomicalLocation(RdfProperty[schemaorg.URL | schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('anatomicalLocation', 'https://bioschemas.org/draft_terms/anatomicalLocation', [])

class bioSample(RdfProperty[schemaorg.Text | schemaorg.BioChemEntity | bioschemas.BioSample | schemaorg.URL | schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.Taxon]):
    term = RdfTerm('bioSample', 'https://bioschemas.org/draft_terms/bioSample', [])

class studyLocation(RdfProperty[schemaorg.Place | schemaorg.AdministrativeArea]):
    term = RdfTerm('studyLocation', 'https://bioschemas.org/draft_terms/studyLocation', [])

class isCodingRNA(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isCodingRNA', 'https://bioschemas.org/draft_terms/isCodingRNA', [])

class hasKineticRate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasKineticRate', 'https://bioschemas.org/draft_terms/hasKineticRate', [])

class hasSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasSequence', 'https://bioschemas.org/draft_terms/hasSequence', [])

class studySubject(RdfProperty[schemaorg.MedicalEntity | schemaorg.BioChemEntity]):
    term = RdfTerm('studySubject', 'https://bioschemas.org/draft_terms/studySubject', [])

class protocolApplication(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('protocolApplication', 'https://bioschemas.org/draft_terms/protocolApplication', [])

class startDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('startDate', 'https://bioschemas.org/draft_terms/startDate', [])

class hasSequenceAnnotation(RdfProperty[bioschemas_drafts.SequenceAnnotation | schemaorg.URL]):
    term = RdfTerm('hasSequenceAnnotation', 'https://bioschemas.org/draft_terms/hasSequenceAnnotation', [])

class isLocatedInSubcellularLocation(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.DefinedTerm]):
    term = RdfTerm('isLocatedInSubcellularLocation', 'https://bioschemas.org/draft_terms/isLocatedInSubcellularLocation', [])

class expressedIn(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem | schemaorg.BioChemEntity | schemaorg.DefinedTerm]):
    term = RdfTerm('expressedIn', 'https://bioschemas.org/draft_terms/expressedIn', [])

class protocolLimitation(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('protocolLimitation', 'https://bioschemas.org/draft_terms/protocolLimitation', [])

class hasCofactor(RdfProperty[schemaorg.ChemicalSubstance]):
    term = RdfTerm('hasCofactor', 'https://bioschemas.org/draft_terms/hasCofactor', [])

class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm('additionalProperty', 'https://bioschemas.org/draft_terms/additionalProperty', [])

class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm('alternativeOf', 'https://bioschemas.org/draft_terms/alternativeOf', [])

class isInvolvedInBiologicalProcess(RdfProperty[schemaorg.URL | schemaorg.DefinedTerm | schemaorg.PropertyValue]):
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

class associatedDisease(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.MedicalCondition]):
    term = RdfTerm('associatedDisease', 'https://bioschemas.org/draft_terms/associatedDisease', [])

class biologicalType(RdfProperty[schemaorg.Text | schemaorg.BioChemEntity | schemaorg.URL | schemaorg.DefinedTerm]):
    term = RdfTerm('biologicalType', 'https://bioschemas.org/draft_terms/biologicalType', [])

class encodesBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('encodesBioChemEntity', 'https://bioschemas.org/draft_terms/encodesBioChemEntity', [])

class ethicalLegalSocial(RdfProperty[schemaorg.Text]):
    term = RdfTerm('ethicalLegalSocial', 'https://bioschemas.org/draft_terms/ethicalLegalSocial', [])

class modelSignature(RdfProperty[schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm('modelSignature', 'https://bioschemas.org/draft_terms/modelSignature', [])

class taxonRank(RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('taxonRank', 'https://bioschemas.org/draft_terms/taxonRank', [])

class hasMolecularFunction(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.DefinedTerm]):
    term = RdfTerm('hasMolecularFunction', 'https://bioschemas.org/draft_terms/hasMolecularFunction', [])

class modelDataset(RdfProperty[schemaorg.Dataset]):
    term = RdfTerm('modelDataset', 'https://bioschemas.org/draft_terms/modelDataset', [])

class studyDomain(RdfProperty[schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('studyDomain', 'https://bioschemas.org/draft_terms/studyDomain', [])

class optimalPH(RdfProperty[schemaorg.Number]):
    term = RdfTerm('optimalPH', 'https://bioschemas.org/draft_terms/optimalPH', [])

class computationalTool(RdfProperty[schemaorg.DefinedTerm | schemaorg.SoftwareApplication | bioschemas.ComputationalWorkflow | schemaorg.PropertyValue | schemaorg.SoftwareSourceCode]):
    term = RdfTerm('computationalTool', 'https://bioschemas.org/draft_terms/computationalTool', [])

class valueReference(RdfProperty[schemaorg.QuantitativeValue | schemaorg.DefinedTerm | schemaorg.StructuredValue | schemaorg.QualitativeValue | schemaorg.PropertyValue | schemaorg.Enumeration | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('valueReference', 'https://bioschemas.org/draft_terms/valueReference', [])

class sample(RdfProperty[schemaorg.Thing | schemaorg.DefinedTerm | schemaorg.PropertyValue]):
    term = RdfTerm('sample', 'https://bioschemas.org/draft_terms/sample', [])

class endDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('endDate', 'https://bioschemas.org/draft_terms/endDate', [])

class alternateScientificName(RdfProperty[bioschemas_drafts.TaxonName | schemaorg.Text | schemaorg.URL]):
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

class boundMolecule(RdfProperty[schemaorg.DefinedTerm | schemaorg.MolecularEntity | schemaorg.ChemicalSubstance | schemaorg.BioChemEntity | schemaorg.URL]):
    term = RdfTerm('boundMolecule', 'https://bioschemas.org/draft_terms/boundMolecule', [])

class bioChemAssociation(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('bioChemAssociation', 'https://bioschemas.org/draft_terms/bioChemAssociation', [])

class endUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('endUncertainty', 'https://bioschemas.org/draft_terms/endUncertainty', [])

class parentTaxon(RdfProperty[schemaorg.Taxon | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('parentTaxon', 'https://bioschemas.org/draft_terms/parentTaxon', [])