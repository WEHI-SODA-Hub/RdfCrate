from __future__ import annotations
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import schemaorg
from rdfcrate.vocabs import bioschemas


class ChemicalSubstance(schemaorg.BioChemEntity):
    term = RdfTerm(
        "https://bioschemas.org/terms/ChemicalSubstance", "ChemicalSubstance"
    )


class Protein(schemaorg.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/terms/Protein", "Protein")


class Gene(schemaorg.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/terms/Gene", "Gene")


class MolecularEntity(schemaorg.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/terms/MolecularEntity", "MolecularEntity")


class BioSample(schemaorg.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/terms/BioSample", "BioSample")


class FormalParameter(schemaorg.Intangible):
    term = RdfTerm("https://bioschemas.org/terms/FormalParameter", "FormalParameter")


class ComputationalWorkflow(schemaorg.SoftwareSourceCode):
    term = RdfTerm(
        "https://bioschemas.org/terms/ComputationalWorkflow", "ComputationalWorkflow"
    )


class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm("https://bioschemas.org/terms/TaxonName", "TaxonName")


class BioChemEntity(schemaorg.Thing):
    term = RdfTerm("https://bioschemas.org/terms/BioChemEntity", "BioChemEntity")


class Taxon(schemaorg.Thing):
    term = RdfTerm("https://bioschemas.org/terms/Taxon", "Taxon")


class bioChemInteraction(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/terms/bioChemInteraction", "bioChemInteraction"
    )


class childTaxon(RdfProperty[schemaorg.Text | schemaorg.Taxon | schemaorg.URL]):
    term = RdfTerm("https://bioschemas.org/terms/childTaxon", "childTaxon")


class samplingAge(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("https://bioschemas.org/terms/samplingAge", "samplingAge")


class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/hasStatus", "hasStatus")


class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm(
        "https://bioschemas.org/terms/additionalProperty", "additionalProperty"
    )


class monoisotopicMolecularWeight(
    RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]
):
    term = RdfTerm(
        "https://bioschemas.org/terms/monoisotopicMolecularWeight",
        "monoisotopicMolecularWeight",
    )


class parentTaxon(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.Taxon]):
    term = RdfTerm("https://bioschemas.org/terms/parentTaxon", "parentTaxon")


class collector(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("https://bioschemas.org/terms/collector", "collector")


class gender(RdfProperty[schemaorg.GenderType | schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/gender", "gender")


class associatedDisease(
    RdfProperty[schemaorg.PropertyValue | schemaorg.MedicalCondition | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/terms/associatedDisease", "associatedDisease"
    )


class inChI(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/inChI", "inChI")


class molecularWeight(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm("https://bioschemas.org/terms/molecularWeight", "molecularWeight")


class custodian(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("https://bioschemas.org/terms/custodian", "custodian")


class potentialUse(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("https://bioschemas.org/terms/potentialUse", "potentialUse")


class molecularFormula(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/molecularFormula", "molecularFormula")


class chemicalComposition(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/terms/chemicalComposition", "chemicalComposition"
    )


class expressedIn(
    RdfProperty[
        schemaorg.AnatomicalSystem
        | schemaorg.BioChemEntity
        | schemaorg.AnatomicalStructure
        | schemaorg.DefinedTerm
    ]
):
    term = RdfTerm("https://bioschemas.org/terms/expressedIn", "expressedIn")


class isInvolvedInBiologicalProcess(
    RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm]
):
    term = RdfTerm(
        "https://bioschemas.org/terms/isInvolvedInBiologicalProcess",
        "isInvolvedInBiologicalProcess",
    )


class smiles(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/smiles", "smiles")


class isEncodedByBioChemEntity(RdfProperty[bioschemas.Gene]):
    term = RdfTerm(
        "https://bioschemas.org/terms/isEncodedByBioChemEntity",
        "isEncodedByBioChemEntity",
    )


class dateCreated(RdfProperty[schemaorg.Date]):
    term = RdfTerm("https://bioschemas.org/terms/dateCreated", "dateCreated")


class documentation(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("https://bioschemas.org/terms/documentation", "documentation")


class isPartOfBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/terms/isPartOfBioChemEntity", "isPartOfBioChemEntity"
    )


class isLocatedInSubcellularLocation(
    RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.PropertyValue]
):
    term = RdfTerm(
        "https://bioschemas.org/terms/isLocatedInSubcellularLocation",
        "isLocatedInSubcellularLocation",
    )


class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/terms/hasBioPolymerSequence", "hasBioPolymerSequence"
    )


class hasMolecularFunction(
    RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/terms/hasMolecularFunction", "hasMolecularFunction"
    )


class taxonomicRange(
    RdfProperty[
        schemaorg.URL
        | schemaorg.PropertyValue
        | schemaorg.DefinedTerm
        | bioschemas.Taxon
    ]
):
    term = RdfTerm("https://bioschemas.org/terms/taxonomicRange", "taxonomicRange")


class hasBioChemEntityPart(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/terms/hasBioChemEntityPart", "hasBioChemEntityPart"
    )


class scientificName(
    RdfProperty[schemaorg.URL | schemaorg.Text | bioschemas.TaxonName]
):
    term = RdfTerm("https://bioschemas.org/terms/scientificName", "scientificName")


class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm("https://bioschemas.org/terms/alternativeOf", "alternativeOf")


class taxonRank(RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/taxonRank", "taxonRank")


class encodingFormat(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("https://bioschemas.org/terms/encodingFormat", "encodingFormat")


class valueRequired(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("https://bioschemas.org/terms/valueRequired", "valueRequired")


class locationCreated(RdfProperty[schemaorg.Place]):
    term = RdfTerm("https://bioschemas.org/terms/locationCreated", "locationCreated")


class bioChemSimilarity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/terms/bioChemSimilarity", "bioChemSimilarity"
    )


class alternateScientificName(
    RdfProperty[schemaorg.Text | bioschemas.TaxonName | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/terms/alternateScientificName",
        "alternateScientificName",
    )


class encodesBioChemEntity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/terms/encodesBioChemEntity", "encodesBioChemEntity"
    )


class isControl(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("https://bioschemas.org/terms/isControl", "isControl")


class defaultValue(RdfProperty[schemaorg.Text | schemaorg.Thing]):
    term = RdfTerm("https://bioschemas.org/terms/defaultValue", "defaultValue")


class softwareRequirements(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm(
        "https://bioschemas.org/terms/softwareRequirements", "softwareRequirements"
    )


class chemicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("https://bioschemas.org/terms/chemicalRole", "chemicalRole")


class funding(RdfProperty[schemaorg.Grant]):
    term = RdfTerm("https://bioschemas.org/terms/funding", "funding")


class iupacName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/iupacName", "iupacName")


class itemLocation(
    RdfProperty[schemaorg.Place | schemaorg.Text | schemaorg.PostalAddress]
):
    term = RdfTerm("https://bioschemas.org/terms/itemLocation", "itemLocation")


class output(RdfProperty[bioschemas.FormalParameter]):
    term = RdfTerm("https://bioschemas.org/terms/output", "output")


class input(RdfProperty[bioschemas.FormalParameter]):
    term = RdfTerm("https://bioschemas.org/terms/input", "input")


class hasRepresentation(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/terms/hasRepresentation", "hasRepresentation"
    )


class biologicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("https://bioschemas.org/terms/biologicalRole", "biologicalRole")


class inChIKey(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/terms/inChIKey", "inChIKey")
