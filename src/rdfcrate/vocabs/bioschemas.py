from __future__ import annotations
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import schemaorg
from rdfcrate.vocabs import bioschemas


class Protein(schemaorg.BioChemEntity):
    term = RdfTerm("Protein", "https://bioschemas.org/terms/Protein", [])


class ChemicalSubstance(schemaorg.BioChemEntity):
    term = RdfTerm(
        "ChemicalSubstance", "https://bioschemas.org/terms/ChemicalSubstance", []
    )


class MolecularEntity(schemaorg.BioChemEntity):
    term = RdfTerm(
        "MolecularEntity", "https://bioschemas.org/terms/MolecularEntity", []
    )


class BioSample(schemaorg.BioChemEntity):
    term = RdfTerm("BioSample", "https://bioschemas.org/terms/BioSample", [])


class Gene(schemaorg.BioChemEntity):
    term = RdfTerm("Gene", "https://bioschemas.org/terms/Gene", [])


class ComputationalWorkflow(schemaorg.SoftwareSourceCode):
    term = RdfTerm(
        "ComputationalWorkflow",
        "https://bioschemas.org/terms/ComputationalWorkflow",
        [],
    )


class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm("TaxonName", "https://bioschemas.org/terms/TaxonName", [])


class FormalParameter(schemaorg.Intangible):
    term = RdfTerm(
        "FormalParameter", "https://bioschemas.org/terms/FormalParameter", []
    )


class Taxon(schemaorg.Thing):
    term = RdfTerm("Taxon", "https://bioschemas.org/terms/Taxon", [])


class BioChemEntity(schemaorg.Thing):
    term = RdfTerm("BioChemEntity", "https://bioschemas.org/terms/BioChemEntity", [])


class bioChemInteraction(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "bioChemInteraction", "https://bioschemas.org/terms/bioChemInteraction", []
    )


class childTaxon(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.Taxon]):
    term = RdfTerm("childTaxon", "https://bioschemas.org/terms/childTaxon", [])


class samplingAge(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("samplingAge", "https://bioschemas.org/terms/samplingAge", [])


class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm("hasStatus", "https://bioschemas.org/terms/hasStatus", [])


class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm(
        "additionalProperty", "https://bioschemas.org/terms/additionalProperty", []
    )


class monoisotopicMolecularWeight(
    RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]
):
    term = RdfTerm(
        "monoisotopicMolecularWeight",
        "https://bioschemas.org/terms/monoisotopicMolecularWeight",
        [],
    )


class parentTaxon(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.Taxon]):
    term = RdfTerm("parentTaxon", "https://bioschemas.org/terms/parentTaxon", [])


class collector(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("collector", "https://bioschemas.org/terms/collector", [])


class gender(RdfProperty[schemaorg.GenderType | schemaorg.Text]):
    term = RdfTerm("gender", "https://bioschemas.org/terms/gender", [])


class associatedDisease(
    RdfProperty[schemaorg.MedicalCondition | schemaorg.PropertyValue | schemaorg.URL]
):
    term = RdfTerm(
        "associatedDisease", "https://bioschemas.org/terms/associatedDisease", []
    )


class inChI(RdfProperty[schemaorg.Text]):
    term = RdfTerm("inChI", "https://bioschemas.org/terms/inChI", [])


class molecularWeight(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm(
        "molecularWeight", "https://bioschemas.org/terms/molecularWeight", []
    )


class custodian(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("custodian", "https://bioschemas.org/terms/custodian", [])


class potentialUse(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("potentialUse", "https://bioschemas.org/terms/potentialUse", [])


class molecularFormula(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "molecularFormula", "https://bioschemas.org/terms/molecularFormula", []
    )


class chemicalComposition(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "chemicalComposition", "https://bioschemas.org/terms/chemicalComposition", []
    )


class expressedIn(
    RdfProperty[
        schemaorg.BioChemEntity
        | schemaorg.DefinedTerm
        | schemaorg.AnatomicalSystem
        | schemaorg.AnatomicalStructure
    ]
):
    term = RdfTerm("expressedIn", "https://bioschemas.org/terms/expressedIn", [])


class isInvolvedInBiologicalProcess(
    RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm]
):
    term = RdfTerm(
        "isInvolvedInBiologicalProcess",
        "https://bioschemas.org/terms/isInvolvedInBiologicalProcess",
        [],
    )


class smiles(RdfProperty[schemaorg.Text]):
    term = RdfTerm("smiles", "https://bioschemas.org/terms/smiles", [])


class isEncodedByBioChemEntity(RdfProperty[bioschemas.Gene]):
    term = RdfTerm(
        "isEncodedByBioChemEntity",
        "https://bioschemas.org/terms/isEncodedByBioChemEntity",
        [],
    )


class dateCreated(RdfProperty[schemaorg.Date]):
    term = RdfTerm("dateCreated", "https://bioschemas.org/terms/dateCreated", [])


class documentation(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("documentation", "https://bioschemas.org/terms/documentation", [])


class isPartOfBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "isPartOfBioChemEntity",
        "https://bioschemas.org/terms/isPartOfBioChemEntity",
        [],
    )


class isLocatedInSubcellularLocation(
    RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm]
):
    term = RdfTerm(
        "isLocatedInSubcellularLocation",
        "https://bioschemas.org/terms/isLocatedInSubcellularLocation",
        [],
    )


class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "hasBioPolymerSequence",
        "https://bioschemas.org/terms/hasBioPolymerSequence",
        [],
    )


class hasMolecularFunction(
    RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.DefinedTerm]
):
    term = RdfTerm(
        "hasMolecularFunction", "https://bioschemas.org/terms/hasMolecularFunction", []
    )


class taxonomicRange(
    RdfProperty[
        schemaorg.PropertyValue
        | schemaorg.URL
        | schemaorg.DefinedTerm
        | bioschemas.Taxon
    ]
):
    term = RdfTerm("taxonomicRange", "https://bioschemas.org/terms/taxonomicRange", [])


class hasBioChemEntityPart(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "hasBioChemEntityPart", "https://bioschemas.org/terms/hasBioChemEntityPart", []
    )


class scientificName(
    RdfProperty[bioschemas.TaxonName | schemaorg.URL | schemaorg.Text]
):
    term = RdfTerm("scientificName", "https://bioschemas.org/terms/scientificName", [])


class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm("alternativeOf", "https://bioschemas.org/terms/alternativeOf", [])


class taxonRank(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("taxonRank", "https://bioschemas.org/terms/taxonRank", [])


class encodingFormat(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("encodingFormat", "https://bioschemas.org/terms/encodingFormat", [])


class valueRequired(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("valueRequired", "https://bioschemas.org/terms/valueRequired", [])


class locationCreated(RdfProperty[schemaorg.Place]):
    term = RdfTerm(
        "locationCreated", "https://bioschemas.org/terms/locationCreated", []
    )


class bioChemSimilarity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "bioChemSimilarity", "https://bioschemas.org/terms/bioChemSimilarity", []
    )


class alternateScientificName(
    RdfProperty[bioschemas.TaxonName | schemaorg.URL | schemaorg.Text]
):
    term = RdfTerm(
        "alternateScientificName",
        "https://bioschemas.org/terms/alternateScientificName",
        [],
    )


class encodesBioChemEntity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm(
        "encodesBioChemEntity", "https://bioschemas.org/terms/encodesBioChemEntity", []
    )


class isControl(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("isControl", "https://bioschemas.org/terms/isControl", [])


class defaultValue(RdfProperty[schemaorg.Text | schemaorg.Thing]):
    term = RdfTerm("defaultValue", "https://bioschemas.org/terms/defaultValue", [])


class softwareRequirements(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm(
        "softwareRequirements", "https://bioschemas.org/terms/softwareRequirements", []
    )


class chemicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("chemicalRole", "https://bioschemas.org/terms/chemicalRole", [])


class funding(RdfProperty[schemaorg.Grant]):
    term = RdfTerm("funding", "https://bioschemas.org/terms/funding", [])


class iupacName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("iupacName", "https://bioschemas.org/terms/iupacName", [])


class itemLocation(
    RdfProperty[schemaorg.Place | schemaorg.Text | schemaorg.PostalAddress]
):
    term = RdfTerm("itemLocation", "https://bioschemas.org/terms/itemLocation", [])


class output(RdfProperty[bioschemas.FormalParameter]):
    term = RdfTerm("output", "https://bioschemas.org/terms/output", [])


class input(RdfProperty[bioschemas.FormalParameter]):
    term = RdfTerm("input", "https://bioschemas.org/terms/input", [])


class hasRepresentation(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "hasRepresentation", "https://bioschemas.org/terms/hasRepresentation", []
    )


class biologicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("biologicalRole", "https://bioschemas.org/terms/biologicalRole", [])


class inChIKey(RdfProperty[schemaorg.Text]):
    term = RdfTerm("inChIKey", "https://bioschemas.org/terms/inChIKey", [])
