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

class BioChemStructure(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemStructure', 'https://bioschemas.org/draft_terms/BioChemStructure', [])

class BioChemEntity(schemaorg.BioChemEntity):
    term = RdfTerm('BioChemEntity', 'https://bioschemas.org/draft_terms/BioChemEntity', [])

class Enzyme(schemaorg.BioChemEntity):
    term = RdfTerm('Enzyme', 'https://bioschemas.org/draft_terms/Enzyme', [])

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

class Phenotype(schemaorg.Thing):
    term = RdfTerm('Phenotype', 'https://bioschemas.org/draft_terms/Phenotype', [])

class Taxon(schemaorg.Thing):
    term = RdfTerm('Taxon', 'https://bioschemas.org/draft_terms/Taxon', [])

class Sample(schemaorg.Thing):
    term = RdfTerm('Sample', 'https://bioschemas.org/draft_terms/Sample', [])

class Gene(BioChemEntity):
    term = RdfTerm('Gene', 'https://bioschemas.org/draft_terms/Gene', [])

class Protein(BioChemEntity):
    term = RdfTerm('Protein', 'https://bioschemas.org/draft_terms/Protein', [])

class reagent(RdfProperty[schemaorg.Text | schemaorg.MolecularEntity | schemaorg.PropertyValue | schemaorg.URL | schemaorg.ChemicalSubstance | schemaorg.BioChemEntity | schemaorg.DefinedTerm]):
    term = RdfTerm('reagent', 'https://bioschemas.org/draft_terms/reagent', [])

class labEquipment(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('labEquipment', 'https://bioschemas.org/draft_terms/labEquipment', [])

class scientificName(RdfProperty[bioschemas_drafts.TaxonName | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('scientificName', 'https://bioschemas.org/draft_terms/scientificName', [])

class taxonomicRange(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text | schemaorg.URL | schemaorg.Taxon]):
    term = RdfTerm('taxonomicRange', 'https://bioschemas.org/draft_terms/taxonomicRange', [])

class hasAssociatedBioChemEntity(RdfProperty[bioschemas_drafts.RNA | schemaorg.Protein]):
    term = RdfTerm('hasAssociatedBioChemEntity', 'https://bioschemas.org/draft_terms/hasAssociatedBioChemEntity', [])

class studyProcess(RdfProperty[schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('studyProcess', 'https://bioschemas.org/draft_terms/studyProcess', [])

class protocolAdvantage(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('protocolAdvantage', 'https://bioschemas.org/draft_terms/protocolAdvantage', [])

class optimalTemperature(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm('optimalTemperature', 'https://bioschemas.org/draft_terms/optimalTemperature', [])

class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasStatus', 'https://bioschemas.org/draft_terms/hasStatus', [])

class protocolOutcome(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('protocolOutcome', 'https://bioschemas.org/draft_terms/protocolOutcome', [])

class intendedUse(RdfProperty[schemaorg.URL | schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('intendedUse', 'https://bioschemas.org/draft_terms/intendedUse', [])

class anatomicalLocation(RdfProperty[schemaorg.URL | schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('anatomicalLocation', 'https://bioschemas.org/draft_terms/anatomicalLocation', [])

class bioSample(RdfProperty[schemaorg.Taxon | schemaorg.PropertyValue | schemaorg.URL | schemaorg.BioChemEntity | schemaorg.DefinedTerm | bioschemas.BioSample | schemaorg.Text]):
    term = RdfTerm('bioSample', 'https://bioschemas.org/draft_terms/bioSample', [])

class studyLocation(RdfProperty[schemaorg.AdministrativeArea | schemaorg.Place]):
    term = RdfTerm('studyLocation', 'https://bioschemas.org/draft_terms/studyLocation', [])

class isCodingRNA(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isCodingRNA', 'https://bioschemas.org/draft_terms/isCodingRNA', [])

class hasKineticRate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasKineticRate', 'https://bioschemas.org/draft_terms/hasKineticRate', [])

class hasSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasSequence', 'https://bioschemas.org/draft_terms/hasSequence', [])

class studySubject(RdfProperty[schemaorg.BioChemEntity | schemaorg.MedicalEntity]):
    term = RdfTerm('studySubject', 'https://bioschemas.org/draft_terms/studySubject', [])

class protocolApplication(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('protocolApplication', 'https://bioschemas.org/draft_terms/protocolApplication', [])

class startDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('startDate', 'https://bioschemas.org/draft_terms/startDate', [])

class hasSequenceAnnotation(RdfProperty[schemaorg.URL | bioschemas_drafts.SequenceAnnotation]):
    term = RdfTerm('hasSequenceAnnotation', 'https://bioschemas.org/draft_terms/hasSequenceAnnotation', [])

class isLocatedInSubcellularLocation(RdfProperty[schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('isLocatedInSubcellularLocation', 'https://bioschemas.org/draft_terms/isLocatedInSubcellularLocation', [])

class expressedIn(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.BioChemEntity | schemaorg.DefinedTerm | schemaorg.AnatomicalSystem]):
    term = RdfTerm('expressedIn', 'https://bioschemas.org/draft_terms/expressedIn', [])

class protocolLimitation(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('protocolLimitation', 'https://bioschemas.org/draft_terms/protocolLimitation', [])

class hasCofactor(RdfProperty[schemaorg.ChemicalSubstance]):
    term = RdfTerm('hasCofactor', 'https://bioschemas.org/draft_terms/hasCofactor', [])

class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm('additionalProperty', 'https://bioschemas.org/draft_terms/additionalProperty', [])

class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm('alternativeOf', 'https://bioschemas.org/draft_terms/alternativeOf', [])

class isInvolvedInBiologicalProcess(RdfProperty[schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('isInvolvedInBiologicalProcess', 'https://bioschemas.org/draft_terms/isInvolvedInBiologicalProcess', [])

class creationMethod(RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('creationMethod', 'https://bioschemas.org/draft_terms/creationMethod', [])

class match(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('match', 'https://bioschemas.org/draft_terms/match', [])

class startUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('startUncertainty', 'https://bioschemas.org/draft_terms/startUncertainty', [])

class childTaxon(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.Taxon]):
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

class biologicalType(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.BioChemEntity | schemaorg.DefinedTerm]):
    term = RdfTerm('biologicalType', 'https://bioschemas.org/draft_terms/biologicalType', [])

class encodesBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('encodesBioChemEntity', 'https://bioschemas.org/draft_terms/encodesBioChemEntity', [])

class ethicalLegalSocial(RdfProperty[schemaorg.Text]):
    term = RdfTerm('ethicalLegalSocial', 'https://bioschemas.org/draft_terms/ethicalLegalSocial', [])

class modelSignature(RdfProperty[schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm('modelSignature', 'https://bioschemas.org/draft_terms/modelSignature', [])

class taxonRank(RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('taxonRank', 'https://bioschemas.org/draft_terms/taxonRank', [])

class hasMolecularFunction(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('hasMolecularFunction', 'https://bioschemas.org/draft_terms/hasMolecularFunction', [])

class modelDataset(RdfProperty[schemaorg.Dataset]):
    term = RdfTerm('modelDataset', 'https://bioschemas.org/draft_terms/modelDataset', [])

class studyDomain(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('studyDomain', 'https://bioschemas.org/draft_terms/studyDomain', [])

class optimalPH(RdfProperty[schemaorg.Number]):
    term = RdfTerm('optimalPH', 'https://bioschemas.org/draft_terms/optimalPH', [])

class computationalTool(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.SoftwareSourceCode | bioschemas.ComputationalWorkflow | schemaorg.SoftwareApplication]):
    term = RdfTerm('computationalTool', 'https://bioschemas.org/draft_terms/computationalTool', [])

class valueReference(RdfProperty[schemaorg.Text | schemaorg.Enumeration | schemaorg.QualitativeValue | schemaorg.PropertyValue | schemaorg.URL | schemaorg.DefinedTerm | schemaorg.QuantitativeValue | schemaorg.StructuredValue]):
    term = RdfTerm('valueReference', 'https://bioschemas.org/draft_terms/valueReference', [])

class sample(RdfProperty[schemaorg.DefinedTerm | schemaorg.Thing | schemaorg.PropertyValue]):
    term = RdfTerm('sample', 'https://bioschemas.org/draft_terms/sample', [])

class endDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('endDate', 'https://bioschemas.org/draft_terms/endDate', [])

class alternateScientificName(RdfProperty[schemaorg.URL | bioschemas_drafts.TaxonName | schemaorg.Text]):
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

class boundMolecule(RdfProperty[schemaorg.MolecularEntity | schemaorg.URL | schemaorg.ChemicalSubstance | schemaorg.BioChemEntity | schemaorg.DefinedTerm]):
    term = RdfTerm('boundMolecule', 'https://bioschemas.org/draft_terms/boundMolecule', [])

class bioChemAssociation(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('bioChemAssociation', 'https://bioschemas.org/draft_terms/bioChemAssociation', [])

class endUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('endUncertainty', 'https://bioschemas.org/draft_terms/endUncertainty', [])

class parentTaxon(RdfProperty[schemaorg.Text | schemaorg.Taxon | schemaorg.URL]):
    term = RdfTerm('parentTaxon', 'https://bioschemas.org/draft_terms/parentTaxon', [])