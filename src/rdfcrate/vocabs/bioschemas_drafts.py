from __future__ import annotations
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import schemaorg
from rdfcrate.vocabs import bioschemas
from rdfcrate.vocabs import bioschemas_drafts


class LabProtocol(schemaorg.HowTo):
    term = RdfTerm("https://bioschemas.org/draft_terms/LabProtocol", "LabProtocol")


class BioChemEntity(schemaorg.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/draft_terms/BioChemEntity", "BioChemEntity")


class Enzyme(schemaorg.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/draft_terms/Enzyme", "Enzyme")


class DNA(schemaorg.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/draft_terms/DNA", "DNA")


class BioChemStructure(schemaorg.BioChemEntity):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/BioChemStructure", "BioChemStructure"
    )


class Study(schemaorg.CreativeWork):
    term = RdfTerm("https://bioschemas.org/draft_terms/Study", "Study")


class SequenceMatchingModel(schemaorg.CreativeWork):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/SequenceMatchingModel",
        "SequenceMatchingModel",
    )


class TaxonName(schemaorg.CreativeWork):
    term = RdfTerm("https://bioschemas.org/draft_terms/TaxonName", "TaxonName")


class RNA(bioschemas.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/draft_terms/RNA", "RNA")


class SequenceAnnotation(bioschemas.BioChemEntity):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/SequenceAnnotation", "SequenceAnnotation"
    )


class SequenceRange(bioschemas.BioChemEntity):
    term = RdfTerm("https://bioschemas.org/draft_terms/SequenceRange", "SequenceRange")


class Taxon(schemaorg.Thing):
    term = RdfTerm("https://bioschemas.org/draft_terms/Taxon", "Taxon")


class Phenotype(schemaorg.Thing):
    term = RdfTerm("https://bioschemas.org/draft_terms/Phenotype", "Phenotype")


class Sample(schemaorg.Thing):
    term = RdfTerm("https://bioschemas.org/draft_terms/Sample", "Sample")


class Gene(BioChemEntity):
    term = RdfTerm("https://bioschemas.org/draft_terms/Gene", "Gene")


class Protein(BioChemEntity):
    term = RdfTerm("https://bioschemas.org/draft_terms/Protein", "Protein")


class reagent(
    RdfProperty[
        schemaorg.DefinedTerm
        | schemaorg.PropertyValue
        | schemaorg.URL
        | schemaorg.ChemicalSubstance
        | schemaorg.Text
        | schemaorg.BioChemEntity
        | schemaorg.MolecularEntity
    ]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/reagent", "reagent")


class labEquipment(
    RdfProperty[
        schemaorg.Text | schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL
    ]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/labEquipment", "labEquipment")


class scientificName(
    RdfProperty[schemaorg.URL | bioschemas_drafts.TaxonName | schemaorg.Text]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/scientificName", "scientificName"
    )


class taxonomicRange(
    RdfProperty[
        schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Text | schemaorg.Taxon
    ]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/taxonomicRange", "taxonomicRange"
    )


class hasAssociatedBioChemEntity(
    RdfProperty[bioschemas_drafts.RNA | schemaorg.Protein]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/hasAssociatedBioChemEntity",
        "hasAssociatedBioChemEntity",
    )


class studyProcess(
    RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.PropertyValue]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/studyProcess", "studyProcess")


class protocolAdvantage(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/protocolAdvantage", "protocolAdvantage"
    )


class optimalTemperature(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/optimalTemperature", "optimalTemperature"
    )


class hasStatus(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/draft_terms/hasStatus", "hasStatus")


class protocolOutcome(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/protocolOutcome", "protocolOutcome"
    )


class intendedUse(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/draft_terms/intendedUse", "intendedUse")


class anatomicalLocation(
    RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/anatomicalLocation", "anatomicalLocation"
    )


class bioSample(
    RdfProperty[
        schemaorg.URL
        | schemaorg.Text
        | schemaorg.BioChemEntity
        | bioschemas.BioSample
        | schemaorg.Taxon
        | schemaorg.PropertyValue
        | schemaorg.DefinedTerm
    ]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/bioSample", "bioSample")


class studyLocation(RdfProperty[schemaorg.AdministrativeArea | schemaorg.Place]):
    term = RdfTerm("https://bioschemas.org/draft_terms/studyLocation", "studyLocation")


class isCodingRNA(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("https://bioschemas.org/draft_terms/isCodingRNA", "isCodingRNA")


class hasKineticRate(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/hasKineticRate", "hasKineticRate"
    )


class hasSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/draft_terms/hasSequence", "hasSequence")


class studySubject(RdfProperty[schemaorg.MedicalEntity | schemaorg.BioChemEntity]):
    term = RdfTerm("https://bioschemas.org/draft_terms/studySubject", "studySubject")


class protocolApplication(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/protocolApplication", "protocolApplication"
    )


class startDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("https://bioschemas.org/draft_terms/startDate", "startDate")


class hasSequenceAnnotation(
    RdfProperty[bioschemas_drafts.SequenceAnnotation | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/hasSequenceAnnotation",
        "hasSequenceAnnotation",
    )


class isLocatedInSubcellularLocation(
    RdfProperty[schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/isLocatedInSubcellularLocation",
        "isLocatedInSubcellularLocation",
    )


class expressedIn(
    RdfProperty[
        schemaorg.DefinedTerm
        | schemaorg.BioChemEntity
        | schemaorg.AnatomicalStructure
        | schemaorg.AnatomicalSystem
    ]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/expressedIn", "expressedIn")


class protocolLimitation(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/protocolLimitation", "protocolLimitation"
    )


class hasCofactor(RdfProperty[schemaorg.ChemicalSubstance]):
    term = RdfTerm("https://bioschemas.org/draft_terms/hasCofactor", "hasCofactor")


class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/additionalProperty", "additionalProperty"
    )


class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm("https://bioschemas.org/draft_terms/alternativeOf", "alternativeOf")


class isInvolvedInBiologicalProcess(
    RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/isInvolvedInBiologicalProcess",
        "isInvolvedInBiologicalProcess",
    )


class creationMethod(
    RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/creationMethod", "creationMethod"
    )


class match(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm("https://bioschemas.org/draft_terms/match", "match")


class startUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/startUncertainty", "startUncertainty"
    )


class childTaxon(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.Taxon]):
    term = RdfTerm("https://bioschemas.org/draft_terms/childTaxon", "childTaxon")


class sequenceValue(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("https://bioschemas.org/draft_terms/sequenceValue", "sequenceValue")


class massResolution(RdfProperty[schemaorg.Quantity]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/massResolution", "massResolution"
    )


class rangeStart(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("https://bioschemas.org/draft_terms/rangeStart", "rangeStart")


class isMatchedBy(RdfProperty[bioschemas_drafts.SequenceMatchingModel]):
    term = RdfTerm("https://bioschemas.org/draft_terms/isMatchedBy", "isMatchedBy")


class associatedDisease(
    RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.MedicalCondition]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/associatedDisease", "associatedDisease"
    )


class biologicalType(
    RdfProperty[
        schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Text | schemaorg.BioChemEntity
    ]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/biologicalType", "biologicalType"
    )


class encodesBioChemEntity(RdfProperty[bioschemas.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/encodesBioChemEntity",
        "encodesBioChemEntity",
    )


class ethicalLegalSocial(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/ethicalLegalSocial", "ethicalLegalSocial"
    )


class modelSignature(RdfProperty[schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/modelSignature", "modelSignature"
    )


class taxonRank(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm("https://bioschemas.org/draft_terms/taxonRank", "taxonRank")


class hasMolecularFunction(
    RdfProperty[schemaorg.DefinedTerm | schemaorg.PropertyValue | schemaorg.URL]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/hasMolecularFunction",
        "hasMolecularFunction",
    )


class modelDataset(RdfProperty[schemaorg.Dataset]):
    term = RdfTerm("https://bioschemas.org/draft_terms/modelDataset", "modelDataset")


class studyDomain(
    RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.Text]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/studyDomain", "studyDomain")


class optimalPH(RdfProperty[schemaorg.Number]):
    term = RdfTerm("https://bioschemas.org/draft_terms/optimalPH", "optimalPH")


class computationalTool(
    RdfProperty[
        bioschemas.ComputationalWorkflow
        | schemaorg.PropertyValue
        | schemaorg.DefinedTerm
        | schemaorg.SoftwareApplication
        | schemaorg.SoftwareSourceCode
    ]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/computationalTool", "computationalTool"
    )


class valueReference(
    RdfProperty[
        schemaorg.Text
        | schemaorg.QuantitativeValue
        | schemaorg.Enumeration
        | schemaorg.QualitativeValue
        | schemaorg.StructuredValue
        | schemaorg.PropertyValue
        | schemaorg.DefinedTerm
        | schemaorg.URL
    ]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/valueReference", "valueReference"
    )


class sample(
    RdfProperty[schemaorg.PropertyValue | schemaorg.Thing | schemaorg.DefinedTerm]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/sample", "sample")


class endDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("https://bioschemas.org/draft_terms/endDate", "endDate")


class alternateScientificName(
    RdfProperty[schemaorg.URL | bioschemas_drafts.TaxonName | schemaorg.Text]
):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/alternateScientificName",
        "alternateScientificName",
    )


class rangeEnd(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("https://bioschemas.org/draft_terms/rangeEnd", "rangeEnd")


class hasCoenzyme(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm("https://bioschemas.org/draft_terms/hasCoenzyme", "hasCoenzyme")


class sequenceOrientation(RdfProperty[schemaorg.Integer]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/sequenceOrientation", "sequenceOrientation"
    )


class relatedStudy(RdfProperty[bioschemas_drafts.Study]):
    term = RdfTerm("https://bioschemas.org/draft_terms/relatedStudy", "relatedStudy")


class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/hasBioPolymerSequence",
        "hasBioPolymerSequence",
    )


class sequenceLocation(RdfProperty[bioschemas_drafts.SequenceRange]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/sequenceLocation", "sequenceLocation"
    )


class boundMolecule(
    RdfProperty[
        schemaorg.DefinedTerm
        | schemaorg.URL
        | schemaorg.BioChemEntity
        | schemaorg.ChemicalSubstance
        | schemaorg.MolecularEntity
    ]
):
    term = RdfTerm("https://bioschemas.org/draft_terms/boundMolecule", "boundMolecule")


class bioChemAssociation(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/bioChemAssociation", "bioChemAssociation"
    )


class endUncertainty(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "https://bioschemas.org/draft_terms/endUncertainty", "endUncertainty"
    )


class parentTaxon(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.Taxon]):
    term = RdfTerm("https://bioschemas.org/draft_terms/parentTaxon", "parentTaxon")
