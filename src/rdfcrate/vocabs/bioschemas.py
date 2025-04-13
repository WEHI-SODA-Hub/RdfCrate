from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import schemaorg
from rdfcrate.vocabs import bioschemas

class ComputationalWorkflow(schemaorg.SoftwareSourceCode):
    term = RdfTerm('ComputationalWorkflow', 'https://bioschemas.org/terms/ComputationalWorkflow', [])

class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm('TaxonName', 'https://bioschemas.org/terms/TaxonName', [])

class MolecularEntity(schemaorg.BioChemEntity):
    term = RdfTerm('MolecularEntity', 'https://bioschemas.org/terms/MolecularEntity', [])

class Protein(schemaorg.BioChemEntity):
    term = RdfTerm('Protein', 'https://bioschemas.org/terms/Protein', [])

class BioSample(schemaorg.BioChemEntity):
    term = RdfTerm('BioSample', 'https://bioschemas.org/terms/BioSample', [])

class Gene(schemaorg.BioChemEntity):
    term = RdfTerm('Gene', 'https://bioschemas.org/terms/Gene', [])

class ChemicalSubstance(schemaorg.BioChemEntity):
    term = RdfTerm('ChemicalSubstance', 'https://bioschemas.org/terms/ChemicalSubstance', [])

class FormalParameter(schemaorg.Intangible):
    term = RdfTerm('FormalParameter', 'https://bioschemas.org/terms/FormalParameter', [])

class Taxon(schemaorg.Thing):
    term = RdfTerm('Taxon', 'https://bioschemas.org/terms/Taxon', [])

class BioChemEntity(schemaorg.Thing):
    term = RdfTerm('BioChemEntity', 'https://bioschemas.org/terms/BioChemEntity', [])

@dataclass(frozen=True)
class molecularFormula(RdfProperty):
    term = RdfTerm('molecularFormula', 'https://bioschemas.org/terms/molecularFormula', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class expressedIn(RdfProperty):
    term = RdfTerm('expressedIn', 'https://bioschemas.org/terms/expressedIn', [])
    object: schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem | schemaorg.BioChemEntity | schemaorg.DefinedTerm

@dataclass(frozen=True)
class scientificName(RdfProperty):
    term = RdfTerm('scientificName', 'https://bioschemas.org/terms/scientificName', [])
    object: bioschemas.TaxonName | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class additionalProperty(RdfProperty):
    term = RdfTerm('additionalProperty', 'https://bioschemas.org/terms/additionalProperty', [])
    object: schemaorg.PropertyValue

@dataclass(frozen=True)
class funding(RdfProperty):
    term = RdfTerm('funding', 'https://bioschemas.org/terms/funding', [])
    object: schemaorg.Grant

@dataclass(frozen=True)
class taxonomicRange(RdfProperty):
    term = RdfTerm('taxonomicRange', 'https://bioschemas.org/terms/taxonomicRange', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL | bioschemas.Taxon

@dataclass(frozen=True)
class smiles(RdfProperty):
    term = RdfTerm('smiles', 'https://bioschemas.org/terms/smiles', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class iupacName(RdfProperty):
    term = RdfTerm('iupacName', 'https://bioschemas.org/terms/iupacName', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class parentTaxon(RdfProperty):
    term = RdfTerm('parentTaxon', 'https://bioschemas.org/terms/parentTaxon', [])
    object: schemaorg.Taxon | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class inChIKey(RdfProperty):
    term = RdfTerm('inChIKey', 'https://bioschemas.org/terms/inChIKey', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class taxonRank(RdfProperty):
    term = RdfTerm('taxonRank', 'https://bioschemas.org/terms/taxonRank', [])
    object: schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class alternateScientificName(RdfProperty):
    term = RdfTerm('alternateScientificName', 'https://bioschemas.org/terms/alternateScientificName', [])
    object: bioschemas.TaxonName | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class locationCreated(RdfProperty):
    term = RdfTerm('locationCreated', 'https://bioschemas.org/terms/locationCreated', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class samplingAge(RdfProperty):
    term = RdfTerm('samplingAge', 'https://bioschemas.org/terms/samplingAge', [])
    object: schemaorg.Integer

@dataclass(frozen=True)
class defaultValue(RdfProperty):
    term = RdfTerm('defaultValue', 'https://bioschemas.org/terms/defaultValue', [])
    object: schemaorg.Text | schemaorg.Thing

@dataclass(frozen=True)
class monoisotopicMolecularWeight(RdfProperty):
    term = RdfTerm('monoisotopicMolecularWeight', 'https://bioschemas.org/terms/monoisotopicMolecularWeight', [])
    object: schemaorg.QuantitativeValue | schemaorg.Text

@dataclass(frozen=True)
class dateCreated(RdfProperty):
    term = RdfTerm('dateCreated', 'https://bioschemas.org/terms/dateCreated', [])
    object: schemaorg.Date

@dataclass(frozen=True)
class documentation(RdfProperty):
    term = RdfTerm('documentation', 'https://bioschemas.org/terms/documentation', [])
    object: schemaorg.CreativeWork | schemaorg.URL

@dataclass(frozen=True)
class biologicalRole(RdfProperty):
    term = RdfTerm('biologicalRole', 'https://bioschemas.org/terms/biologicalRole', [])
    object: schemaorg.DefinedTerm

@dataclass(frozen=True)
class custodian(RdfProperty):
    term = RdfTerm('custodian', 'https://bioschemas.org/terms/custodian', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class isInvolvedInBiologicalProcess(RdfProperty):
    term = RdfTerm('isInvolvedInBiologicalProcess', 'https://bioschemas.org/terms/isInvolvedInBiologicalProcess', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL

@dataclass(frozen=True)
class hasBioChemEntityPart(RdfProperty):
    term = RdfTerm('hasBioChemEntityPart', 'https://bioschemas.org/terms/hasBioChemEntityPart', [])
    object: bioschemas.BioChemEntity

@dataclass(frozen=True)
class potentialUse(RdfProperty):
    term = RdfTerm('potentialUse', 'https://bioschemas.org/terms/potentialUse', [])
    object: schemaorg.DefinedTerm

@dataclass(frozen=True)
class output(RdfProperty):
    term = RdfTerm('output', 'https://bioschemas.org/terms/output', [])
    object: bioschemas.FormalParameter

@dataclass(frozen=True)
class isEncodedByBioChemEntity(RdfProperty):
    term = RdfTerm('isEncodedByBioChemEntity', 'https://bioschemas.org/terms/isEncodedByBioChemEntity', [])
    object: bioschemas.Gene

@dataclass(frozen=True)
class hasMolecularFunction(RdfProperty):
    term = RdfTerm('hasMolecularFunction', 'https://bioschemas.org/terms/hasMolecularFunction', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL

@dataclass(frozen=True)
class softwareRequirements(RdfProperty):
    term = RdfTerm('softwareRequirements', 'https://bioschemas.org/terms/softwareRequirements', [])
    object: schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class chemicalComposition(RdfProperty):
    term = RdfTerm('chemicalComposition', 'https://bioschemas.org/terms/chemicalComposition', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class collector(RdfProperty):
    term = RdfTerm('collector', 'https://bioschemas.org/terms/collector', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class isPartOfBioChemEntity(RdfProperty):
    term = RdfTerm('isPartOfBioChemEntity', 'https://bioschemas.org/terms/isPartOfBioChemEntity', [])
    object: bioschemas.BioChemEntity

@dataclass(frozen=True)
class itemLocation(RdfProperty):
    term = RdfTerm('itemLocation', 'https://bioschemas.org/terms/itemLocation', [])
    object: schemaorg.Place | schemaorg.PostalAddress | schemaorg.Text

@dataclass(frozen=True)
class alternativeOf(RdfProperty):
    term = RdfTerm('alternativeOf', 'https://bioschemas.org/terms/alternativeOf', [])
    object: schemaorg.Gene

@dataclass(frozen=True)
class gender(RdfProperty):
    term = RdfTerm('gender', 'https://bioschemas.org/terms/gender', [])
    object: schemaorg.Text | schemaorg.GenderType

@dataclass(frozen=True)
class encodesBioChemEntity(RdfProperty):
    term = RdfTerm('encodesBioChemEntity', 'https://bioschemas.org/terms/encodesBioChemEntity', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class encodingFormat(RdfProperty):
    term = RdfTerm('encodingFormat', 'https://bioschemas.org/terms/encodingFormat', [])
    object: schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class input(RdfProperty):
    term = RdfTerm('input', 'https://bioschemas.org/terms/input', [])
    object: bioschemas.FormalParameter

@dataclass(frozen=True)
class associatedDisease(RdfProperty):
    term = RdfTerm('associatedDisease', 'https://bioschemas.org/terms/associatedDisease', [])
    object: schemaorg.MedicalCondition | schemaorg.URL | schemaorg.PropertyValue

@dataclass(frozen=True)
class isControl(RdfProperty):
    term = RdfTerm('isControl', 'https://bioschemas.org/terms/isControl', [])
    object: schemaorg.Boolean

@dataclass(frozen=True)
class bioChemInteraction(RdfProperty):
    term = RdfTerm('bioChemInteraction', 'https://bioschemas.org/terms/bioChemInteraction', [])
    object: bioschemas.BioChemEntity

@dataclass(frozen=True)
class valueRequired(RdfProperty):
    term = RdfTerm('valueRequired', 'https://bioschemas.org/terms/valueRequired', [])
    object: schemaorg.Boolean

@dataclass(frozen=True)
class molecularWeight(RdfProperty):
    term = RdfTerm('molecularWeight', 'https://bioschemas.org/terms/molecularWeight', [])
    object: schemaorg.QuantitativeValue | schemaorg.Text

@dataclass(frozen=True)
class hasStatus(RdfProperty):
    term = RdfTerm('hasStatus', 'https://bioschemas.org/terms/hasStatus', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class chemicalRole(RdfProperty):
    term = RdfTerm('chemicalRole', 'https://bioschemas.org/terms/chemicalRole', [])
    object: schemaorg.DefinedTerm

@dataclass(frozen=True)
class bioChemSimilarity(RdfProperty):
    term = RdfTerm('bioChemSimilarity', 'https://bioschemas.org/terms/bioChemSimilarity', [])
    object: bioschemas.BioChemEntity

@dataclass(frozen=True)
class childTaxon(RdfProperty):
    term = RdfTerm('childTaxon', 'https://bioschemas.org/terms/childTaxon', [])
    object: schemaorg.Taxon | schemaorg.Text | schemaorg.URL

@dataclass(frozen=True)
class isLocatedInSubcellularLocation(RdfProperty):
    term = RdfTerm('isLocatedInSubcellularLocation', 'https://bioschemas.org/terms/isLocatedInSubcellularLocation', [])
    object: schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL

@dataclass(frozen=True)
class hasRepresentation(RdfProperty):
    term = RdfTerm('hasRepresentation', 'https://bioschemas.org/terms/hasRepresentation', [])
    object: bioschemas.BioChemEntity

@dataclass(frozen=True)
class hasBioPolymerSequence(RdfProperty):
    term = RdfTerm('hasBioPolymerSequence', 'https://bioschemas.org/terms/hasBioPolymerSequence', [])
    object: schemaorg.Text

@dataclass(frozen=True)
class inChI(RdfProperty):
    term = RdfTerm('inChI', 'https://bioschemas.org/terms/inChI', [])
    object: schemaorg.Text