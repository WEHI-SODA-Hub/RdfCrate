from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import schemaorg
from rdfcrate.vocabs import bioschemas

class Protein(schemaorg.BioChemEntity):
    term = RdfTerm('Protein', 'https://bioschemas.org/terms/Protein', [])

class MolecularEntity(schemaorg.BioChemEntity):
    term = RdfTerm('MolecularEntity', 'https://bioschemas.org/terms/MolecularEntity', [])

class BioSample(schemaorg.BioChemEntity):
    term = RdfTerm('BioSample', 'https://bioschemas.org/terms/BioSample', [])

class ChemicalSubstance(schemaorg.BioChemEntity):
    term = RdfTerm('ChemicalSubstance', 'https://bioschemas.org/terms/ChemicalSubstance', [])

class Gene(schemaorg.BioChemEntity):
    term = RdfTerm('Gene', 'https://bioschemas.org/terms/Gene', [])

class ComputationalWorkflow(schemaorg.SoftwareSourceCode):
    term = RdfTerm('ComputationalWorkflow', 'https://bioschemas.org/terms/ComputationalWorkflow', [])

class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm('TaxonName', 'https://bioschemas.org/terms/TaxonName', [])

class FormalParameter(schemaorg.Intangible):
    term = RdfTerm('FormalParameter', 'https://bioschemas.org/terms/FormalParameter', [])

class BioChemEntity(schemaorg.Thing):
    term = RdfTerm('BioChemEntity', 'https://bioschemas.org/terms/BioChemEntity', [])

class Taxon(schemaorg.Thing):
    term = RdfTerm('Taxon', 'https://bioschemas.org/terms/Taxon', [])

class molecularFormula(RdfProperty[schemaorg.Text]):
    term = RdfTerm('molecularFormula', 'https://bioschemas.org/terms/molecularFormula', [])

class expressedIn(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.BioChemEntity | schemaorg.DefinedTerm | schemaorg.AnatomicalSystem]):
    term = RdfTerm('expressedIn', 'https://bioschemas.org/terms/expressedIn', [])

class scientificName(RdfProperty[schemaorg.Text | bioschemas.TaxonName | schemaorg.URL]):
    term = RdfTerm('scientificName', 'https://bioschemas.org/terms/scientificName', [])

class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm('additionalProperty', 'https://bioschemas.org/terms/additionalProperty', [])

class funding(RdfProperty[schemaorg.Grant]):
    term = RdfTerm('funding', 'https://bioschemas.org/terms/funding', [])

class taxonomicRange(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | bioschemas.Taxon | schemaorg.DefinedTerm]):
    term = RdfTerm('taxonomicRange', 'https://bioschemas.org/terms/taxonomicRange', [])

class smiles(RdfProperty[schemaorg.Text]):
    term = RdfTerm('smiles', 'https://bioschemas.org/terms/smiles', [])

class iupacName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('iupacName', 'https://bioschemas.org/terms/iupacName', [])

class parentTaxon(RdfProperty[schemaorg.URL | schemaorg.Taxon | schemaorg.Text]):
    term = RdfTerm('parentTaxon', 'https://bioschemas.org/terms/parentTaxon', [])

class inChIKey(RdfProperty[schemaorg.Text]):
    term = RdfTerm('inChIKey', 'https://bioschemas.org/terms/inChIKey', [])

class taxonRank(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('taxonRank', 'https://bioschemas.org/terms/taxonRank', [])

class alternateScientificName(RdfProperty[schemaorg.Text | bioschemas.TaxonName | schemaorg.URL]):
    term = RdfTerm('alternateScientificName', 'https://bioschemas.org/terms/alternateScientificName', [])

class locationCreated(RdfProperty[schemaorg.Place]):
    term = RdfTerm('locationCreated', 'https://bioschemas.org/terms/locationCreated', [])

class samplingAge(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('samplingAge', 'https://bioschemas.org/terms/samplingAge', [])

class defaultValue(RdfProperty[schemaorg.Text | schemaorg.Thing]):
    term = RdfTerm('defaultValue', 'https://bioschemas.org/terms/defaultValue', [])

class monoisotopicMolecularWeight(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm('monoisotopicMolecularWeight', 'https://bioschemas.org/terms/monoisotopicMolecularWeight', [])

class dateCreated(RdfProperty[schemaorg.Date]):
    term = RdfTerm('dateCreated', 'https://bioschemas.org/terms/dateCreated', [])

class documentation(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('documentation', 'https://bioschemas.org/terms/documentation', [])

class biologicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm('biologicalRole', 'https://bioschemas.org/terms/biologicalRole', [])

class custodian(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('custodian', 'https://bioschemas.org/terms/custodian', [])

class isInvolvedInBiologicalProcess(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm]):
    term = RdfTerm('isInvolvedInBiologicalProcess', 'https://bioschemas.org/terms/isInvolvedInBiologicalProcess', [])

class hasBioChemEntityPart(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('hasBioChemEntityPart', 'https://bioschemas.org/terms/hasBioChemEntityPart', [])

class potentialUse(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm('potentialUse', 'https://bioschemas.org/terms/potentialUse', [])

class output(RdfProperty[bioschemas.FormalParameter]):
    term = RdfTerm('output', 'https://bioschemas.org/terms/output', [])

class isEncodedByBioChemEntity(RdfProperty[bioschemas.Gene]):
    term = RdfTerm('isEncodedByBioChemEntity', 'https://bioschemas.org/terms/isEncodedByBioChemEntity', [])

class hasMolecularFunction(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.DefinedTerm]):
    term = RdfTerm('hasMolecularFunction', 'https://bioschemas.org/terms/hasMolecularFunction', [])

class softwareRequirements(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('softwareRequirements', 'https://bioschemas.org/terms/softwareRequirements', [])

class chemicalComposition(RdfProperty[schemaorg.Text]):
    term = RdfTerm('chemicalComposition', 'https://bioschemas.org/terms/chemicalComposition', [])

class collector(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('collector', 'https://bioschemas.org/terms/collector', [])

class isPartOfBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('isPartOfBioChemEntity', 'https://bioschemas.org/terms/isPartOfBioChemEntity', [])

class itemLocation(RdfProperty[schemaorg.Text | schemaorg.Place | schemaorg.PostalAddress]):
    term = RdfTerm('itemLocation', 'https://bioschemas.org/terms/itemLocation', [])

class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm('alternativeOf', 'https://bioschemas.org/terms/alternativeOf', [])

class gender(RdfProperty[schemaorg.GenderType | schemaorg.Text]):
    term = RdfTerm('gender', 'https://bioschemas.org/terms/gender', [])

class encodesBioChemEntity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('encodesBioChemEntity', 'https://bioschemas.org/terms/encodesBioChemEntity', [])

class encodingFormat(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('encodingFormat', 'https://bioschemas.org/terms/encodingFormat', [])

class input(RdfProperty[bioschemas.FormalParameter]):
    term = RdfTerm('input', 'https://bioschemas.org/terms/input', [])

class associatedDisease(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.MedicalCondition]):
    term = RdfTerm('associatedDisease', 'https://bioschemas.org/terms/associatedDisease', [])

class isControl(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isControl', 'https://bioschemas.org/terms/isControl', [])

class bioChemInteraction(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('bioChemInteraction', 'https://bioschemas.org/terms/bioChemInteraction', [])

class valueRequired(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('valueRequired', 'https://bioschemas.org/terms/valueRequired', [])

class molecularWeight(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm('molecularWeight', 'https://bioschemas.org/terms/molecularWeight', [])

class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasStatus', 'https://bioschemas.org/terms/hasStatus', [])

class chemicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm('chemicalRole', 'https://bioschemas.org/terms/chemicalRole', [])

class bioChemSimilarity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('bioChemSimilarity', 'https://bioschemas.org/terms/bioChemSimilarity', [])

class childTaxon(RdfProperty[schemaorg.Text | schemaorg.Taxon | schemaorg.URL]):
    term = RdfTerm('childTaxon', 'https://bioschemas.org/terms/childTaxon', [])

class isLocatedInSubcellularLocation(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm]):
    term = RdfTerm('isLocatedInSubcellularLocation', 'https://bioschemas.org/terms/isLocatedInSubcellularLocation', [])

class hasRepresentation(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm('hasRepresentation', 'https://bioschemas.org/terms/hasRepresentation', [])

class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasBioPolymerSequence', 'https://bioschemas.org/terms/hasBioPolymerSequence', [])

class inChI(RdfProperty[schemaorg.Text]):
    term = RdfTerm('inChI', 'https://bioschemas.org/terms/inChI', [])