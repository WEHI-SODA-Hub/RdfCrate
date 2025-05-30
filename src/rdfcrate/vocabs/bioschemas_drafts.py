from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import schemaorg
from rdfcrate.vocabs import bioschemas
from rdfcrate.vocabs import bioschemas_drafts

class LabProtocol(schemaorg.HowTo):
    term = RdfTerm('https://bioschemas.org/draft_terms/LabProtocol', 'LabProtocol')

class DNA(schemaorg.BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/DNA', 'DNA')

class BioChemEntity(schemaorg.BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/BioChemEntity', 'BioChemEntity')

class BioChemStructure(schemaorg.BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/BioChemStructure', 'BioChemStructure')

class Enzyme(schemaorg.BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/Enzyme', 'Enzyme')

class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm('https://bioschemas.org/draft_terms/TaxonName', 'TaxonName')

class SequenceMatchingModel(schemaorg.CreativeWork):
    term = RdfTerm('https://bioschemas.org/draft_terms/SequenceMatchingModel', 'SequenceMatchingModel')

class Study(schemaorg.CreativeWork):
    term = RdfTerm('https://bioschemas.org/draft_terms/Study', 'Study')

class RNA(bioschemas.BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/RNA', 'RNA')

class SequenceAnnotation(bioschemas.BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/SequenceAnnotation', 'SequenceAnnotation')

class SequenceRange(bioschemas.BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/SequenceRange', 'SequenceRange')

class Sample(schemaorg.Thing):
    term = RdfTerm('https://bioschemas.org/draft_terms/Sample', 'Sample')

class Taxon(schemaorg.Thing):
    term = RdfTerm('https://bioschemas.org/draft_terms/Taxon', 'Taxon')

class Phenotype(schemaorg.Thing):
    term = RdfTerm('https://bioschemas.org/draft_terms/Phenotype', 'Phenotype')

class Gene(BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/Gene', 'Gene')

class Protein(BioChemEntity):
    term = RdfTerm('https://bioschemas.org/draft_terms/Protein', 'Protein')

class reagent(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.BioChemEntity | schemaorg.PropertyValue | schemaorg.MolecularEntity | schemaorg.ChemicalSubstance | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/reagent', 'reagent')

class labEquipment(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('https://bioschemas.org/draft_terms/labEquipment', 'labEquipment')

class scientificName(RdfProperty[schemaorg.URL | schemaorg.Text | bioschemas_drafts.TaxonName]):
    term = RdfTerm('https://bioschemas.org/draft_terms/scientificName', 'scientificName')

class taxonomicRange(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.Taxon | schemaorg.URL]):
    term = RdfTerm('https://bioschemas.org/draft_terms/taxonomicRange', 'taxonomicRange')

class hasAssociatedBioChemEntity(RdfProperty[bioschemas_drafts.RNA | schemaorg.Protein]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasAssociatedBioChemEntity', 'hasAssociatedBioChemEntity')

class studyProcess(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/studyProcess', 'studyProcess')

class protocolAdvantage(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/protocolAdvantage', 'protocolAdvantage')

class optimalTemperature(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/optimalTemperature', 'optimalTemperature')

class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasStatus', 'hasStatus')

class protocolOutcome(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/protocolOutcome', 'protocolOutcome')

class intendedUse(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('https://bioschemas.org/draft_terms/intendedUse', 'intendedUse')

class anatomicalLocation(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('https://bioschemas.org/draft_terms/anatomicalLocation', 'anatomicalLocation')

class bioSample(RdfProperty[schemaorg.Taxon | schemaorg.URL | schemaorg.BioChemEntity | schemaorg.PropertyValue | schemaorg.DefinedTerm | bioschemas.BioSample | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/bioSample', 'bioSample')

class studyLocation(RdfProperty[schemaorg.AdministrativeArea | schemaorg.Place]):
    term = RdfTerm('https://bioschemas.org/draft_terms/studyLocation', 'studyLocation')

class isCodingRNA(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('https://bioschemas.org/draft_terms/isCodingRNA', 'isCodingRNA')

class hasKineticRate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasKineticRate', 'hasKineticRate')

class hasSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasSequence', 'hasSequence')

class studySubject(RdfProperty[schemaorg.BioChemEntity | schemaorg.MedicalEntity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/studySubject', 'studySubject')

class protocolApplication(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('https://bioschemas.org/draft_terms/protocolApplication', 'protocolApplication')

class startDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('https://bioschemas.org/draft_terms/startDate', 'startDate')

class hasSequenceAnnotation(RdfProperty[schemaorg.URL | bioschemas_drafts.SequenceAnnotation]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasSequenceAnnotation', 'hasSequenceAnnotation')

class isLocatedInSubcellularLocation(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('https://bioschemas.org/draft_terms/isLocatedInSubcellularLocation', 'isLocatedInSubcellularLocation')

class expressedIn(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.DefinedTerm | schemaorg.AnatomicalSystem | schemaorg.BioChemEntity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/expressedIn', 'expressedIn')

class protocolLimitation(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('https://bioschemas.org/draft_terms/protocolLimitation', 'protocolLimitation')

class hasCofactor(RdfProperty[schemaorg.ChemicalSubstance]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasCofactor', 'hasCofactor')

class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm('https://bioschemas.org/draft_terms/additionalProperty', 'additionalProperty')

class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm('https://bioschemas.org/draft_terms/alternativeOf', 'alternativeOf')

class isInvolvedInBiologicalProcess(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('https://bioschemas.org/draft_terms/isInvolvedInBiologicalProcess', 'isInvolvedInBiologicalProcess')

class creationMethod(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/creationMethod', 'creationMethod')

class match(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/match', 'match')

class startUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/startUncertainty', 'startUncertainty')

class childTaxon(RdfProperty[schemaorg.Taxon | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/childTaxon', 'childTaxon')

class sequenceValue(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/sequenceValue', 'sequenceValue')

class massResolution(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/massResolution', 'massResolution')

class rangeStart(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('https://bioschemas.org/draft_terms/rangeStart', 'rangeStart')

class isMatchedBy(RdfProperty[bioschemas_drafts.SequenceMatchingModel]):
    term = RdfTerm('https://bioschemas.org/draft_terms/isMatchedBy', 'isMatchedBy')

class associatedDisease(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.MedicalCondition]):
    term = RdfTerm('https://bioschemas.org/draft_terms/associatedDisease', 'associatedDisease')

class biologicalType(RdfProperty[schemaorg.BioChemEntity | schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('https://bioschemas.org/draft_terms/biologicalType', 'biologicalType')

class encodesBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/encodesBioChemEntity', 'encodesBioChemEntity')

class ethicalLegalSocial(RdfProperty[schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/ethicalLegalSocial', 'ethicalLegalSocial')

class modelSignature(RdfProperty[schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm('https://bioschemas.org/draft_terms/modelSignature', 'modelSignature')

class taxonRank(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/taxonRank', 'taxonRank')

class hasMolecularFunction(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasMolecularFunction', 'hasMolecularFunction')

class modelDataset(RdfProperty[schemaorg.Dataset]):
    term = RdfTerm('https://bioschemas.org/draft_terms/modelDataset', 'modelDataset')

class studyDomain(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/studyDomain', 'studyDomain')

class optimalPH(RdfProperty[schemaorg.Number]):
    term = RdfTerm('https://bioschemas.org/draft_terms/optimalPH', 'optimalPH')

class computationalTool(RdfProperty[schemaorg.SoftwareSourceCode | schemaorg.PropertyValue | bioschemas.ComputationalWorkflow | schemaorg.SoftwareApplication | schemaorg.DefinedTerm]):
    term = RdfTerm('https://bioschemas.org/draft_terms/computationalTool', 'computationalTool')

class valueReference(RdfProperty[schemaorg.Text | schemaorg.QualitativeValue | schemaorg.DefinedTerm | schemaorg.StructuredValue | schemaorg.QuantitativeValue | schemaorg.Enumeration | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('https://bioschemas.org/draft_terms/valueReference', 'valueReference')

class sample(RdfProperty[schemaorg.PropertyValue | schemaorg.Thing | schemaorg.DefinedTerm]):
    term = RdfTerm('https://bioschemas.org/draft_terms/sample', 'sample')

class endDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('https://bioschemas.org/draft_terms/endDate', 'endDate')

class alternateScientificName(RdfProperty[schemaorg.URL | schemaorg.Text | bioschemas_drafts.TaxonName]):
    term = RdfTerm('https://bioschemas.org/draft_terms/alternateScientificName', 'alternateScientificName')

class rangeEnd(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('https://bioschemas.org/draft_terms/rangeEnd', 'rangeEnd')

class hasCoenzyme(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasCoenzyme', 'hasCoenzyme')

class sequenceOrientation(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('https://bioschemas.org/draft_terms/sequenceOrientation', 'sequenceOrientation')

class relatedStudy(RdfProperty[bioschemas_drafts.Study]):
    term = RdfTerm('https://bioschemas.org/draft_terms/relatedStudy', 'relatedStudy')

class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/hasBioPolymerSequence', 'hasBioPolymerSequence')

class sequenceLocation(RdfProperty[bioschemas_drafts.SequenceRange]):
    term = RdfTerm('https://bioschemas.org/draft_terms/sequenceLocation', 'sequenceLocation')

class boundMolecule(RdfProperty[schemaorg.MolecularEntity | schemaorg.ChemicalSubstance | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.BioChemEntity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/boundMolecule', 'boundMolecule')

class bioChemAssociation(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('https://bioschemas.org/draft_terms/bioChemAssociation', 'bioChemAssociation')

class endUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/endUncertainty', 'endUncertainty')

class parentTaxon(RdfProperty[schemaorg.Taxon | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('https://bioschemas.org/draft_terms/parentTaxon', 'parentTaxon')