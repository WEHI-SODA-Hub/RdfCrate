from __future__ import annotations
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from . import owl
from rdfcrate.rdftype import RdfType
from . import obi


class Entity(owl.Thing):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000001", "Entity")


class ObsoleteClass(owl.Thing):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#ObsoleteClass", "ObsoleteClass"
    )


class Continuant(Entity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000002", "Continuant")


class Occurrent(Entity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000003", "Occurrent")


class ObsoletePlatform(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000050", "ObsoletePlatform")


class ObsoleteRoleOfBeingFirstSubjectTreated(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000100",
        "ObsoleteRoleOfBeingFirstSubjectTreated",
    )


class ObsoleteBiologicalVectorRole(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000109", "ObsoleteBiologicalVectorRole"
    )


class ObsoleteLabelRole(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000140", "ObsoleteLabelRole")


class ObsoleteDropoutRole(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000205", "ObsoleteDropoutRole")


class ObsoleteHealthCareProviderRole(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000207", "ObsoleteHealthCareProviderRole"
    )


class ObsoleteBlindedMedicationRole(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000223", "ObsoleteBlindedMedicationRole"
    )


class ObsoleteDefinedMaterial(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000233", "ObsoleteDefinedMaterial"
    )


class ObsoleteSamplePopulation(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000264", "ObsoleteSamplePopulation"
    )


class ObsoleteEnrollment(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000296", "ObsoleteEnrollment")


class ObsoletePeritoneum(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000323", "ObsoletePeritoneum")


class ObsoleteDocumenting(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000340", "ObsoleteDocumenting")


class ObsoleteTrypsinizedMaterial(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000420", "ObsoleteTrypsinizedMaterial"
    )


class ObsoleteHeart(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000442", "ObsoleteHeart")


class ObsoleteIdentification(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000446", "ObsoleteIdentification"
    )


class ObsoleteDefinedOutput(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000449", "ObsoleteDefinedOutput"
    )


class ObsoleteMolecularConcentration(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000577", "ObsoleteMolecularConcentration"
    )


class ObsoleteIntracellularCytokineStainingAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000665",
        "ObsoleteIntracellularCytokineStainingAssay",
    )


class ObsoleteMhcMultimerStainingAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000667", "ObsoleteMhcMultimerStainingAssay"
    )


class ObsoleteStudyResult(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000682", "ObsoleteStudyResult")


class ObsoleteDnaLigase(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000698", "ObsoleteDnaLigase")


class ObsoleteTranscriptionFactorBindingSite(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000794",
        "ObsoleteTranscriptionFactorBindingSite",
    )


class ObsoletePrimaryStructureOfProtein(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000797",
        "ObsoletePrimaryStructureOfProtein",
    )


class ObsoletePrimaryStructureOfSequenceMacromolecule(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000830",
        "ObsoletePrimaryStructureOfSequenceMacromolecule",
    )


class ObsoleteHospital(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000844", "ObsoleteHospital")


class ObsoleteDiethylPyrocarbonate(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000851", "ObsoleteDiethylPyrocarbonate"
    )


class ObsoleteIntracellularMaterialDetectionByFlowCytometryAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000856",
        "ObsoleteIntracellularMaterialDetectionByFlowCytometryAssay",
    )


class ObsoleteAmbidexteriousHandedness(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000926", "ObsoleteAmbidexteriousHandedness"
    )


class ObsoleteTrainingServiceProviderRole(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000929",
        "ObsoleteTrainingServiceProviderRole",
    )


class ObsoleteMaterialAccessProviderRole(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000936",
        "ObsoleteMaterialAccessProviderRole",
    )


class ObsoleteLeftHandedness(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000937", "ObsoleteLeftHandedness"
    )


class ObsoleteHandedness(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000956", "ObsoleteHandedness")


class ObsoleteElectricallyPoweredDevice(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000972",
        "ObsoleteElectricallyPoweredDevice",
    )


class ObsoleteRightHandedness(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000974", "ObsoleteRightHandedness"
    )


class ObsoleteProtocolServiceProviderRole(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000980",
        "ObsoleteProtocolServiceProviderRole",
    )


class ObsoleteDnaSequencingTrainingService(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000986",
        "ObsoleteDnaSequencingTrainingService",
    )


class ObsoleteGeneralScalarMeasurementDatum(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000987",
        "ObsoleteGeneralScalarMeasurementDatum",
    )


class ObsoletePerformingADiagnosis(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000988", "ObsoletePerformingADiagnosis"
    )


class ObsoleteQualitativeBindingDetectionAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001009",
        "ObsoleteQualitativeBindingDetectionAssay",
    )


class ObsoleteSpecimenFixationFunction(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001037", "ObsoleteSpecimenFixationFunction"
    )


class ObsoleteIntracellularMaterialDetectionByFlowCytometryAssayOfEpitopeSpecificCytotoxicTCellDegranulation(
    ObsoleteClass
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001250",
        "ObsoleteIntracellularMaterialDetectionByFlowCytometryAssayOfEpitopeSpecificCytotoxicTCellDegranulation",
    )


class ObsoleteTCellRecognitionOfElutedMhcLigandAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001540",
        "ObsoleteTCellRecognitionOfElutedMhcLigandAssay",
    )


class ObsoleteCellLysateMhcBindingConstantDeterminationAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001560",
        "ObsoleteCellLysateMhcBindingConstantDeterminationAssay",
    )


class ObsoleteCellBoundMhcBindingConstantDeterminationAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001572",
        "ObsoleteCellBoundMhcBindingConstantDeterminationAssay",
    )


class ObsoleteCellLysateMhcCompetitiveBindingAssayUsingRadioactivityDetection(
    ObsoleteClass
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001574",
        "ObsoleteCellLysateMhcCompetitiveBindingAssayUsingRadioactivityDetection",
    )


class ObsoletePurifiedMhcBindingConstantDeterminationAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001576",
        "ObsoletePurifiedMhcBindingConstantDeterminationAssay",
    )


class ObsoleteCellBoundMhcDirectBindingAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001582",
        "ObsoleteCellBoundMhcDirectBindingAssay",
    )


class ObsoletePurifiedMhcDirectBindingAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001611",
        "ObsoletePurifiedMhcDirectBindingAssay",
    )


class ObsoleteBCellEpitopeDirectBindingAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001712",
        "ObsoleteBCellEpitopeDirectBindingAssay",
    )


class ObsoleteBCellEpitopeCompetitiveBindingAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001715",
        "ObsoleteBCellEpitopeCompetitiveBindingAssay",
    )


class ObsoleteBCellEpitopeSpecificXRayCrystallographyAssay(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001737",
        "ObsoleteBCellEpitopeSpecificXRayCrystallographyAssay",
    )


class ObsoleteUpperRespiratorySpecimen(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002782", "ObsoleteUpperRespiratorySpecimen"
    )


class ObsoleteAnatomicalEntity(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100015", "ObsoleteAnatomicalEntity"
    )


class ObsoleteImmortalCell(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100035", "ObsoleteImmortalCell")


class ObsoleteFragmentDerivedFromProtein(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100039",
        "ObsoleteFragmentDerivedFromProtein",
    )


class ObsoleteCellLineCell(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100055", "ObsoleteCellLineCell")


class ObsoleteImmortalCellLineCulture(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100056", "ObsoleteImmortalCellLineCulture"
    )


class ObsoleteCellLine(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100062", "ObsoleteCellLine")


class ObsoletePolymer(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100069", "ObsoletePolymer")


class ObsoleteTandemMassSpectrometry(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200198", "ObsoleteTandemMassSpectrometry"
    )


class ObsoleteCollectionOfEntitiesOfOrganismalOrigin(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0302714",
        "ObsoleteCollectionOfEntitiesOfOrganismalOrigin",
    )


class ObsoleteLiver(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302743", "ObsoleteLiver")


class ObsoleteAdiposeTissue(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0302745", "ObsoleteAdiposeTissue"
    )


class ObsoleteActivation(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302901", "ObsoleteActivation")


class ObsoletePerformingAClinicalAssessment(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600003",
        "ObsoletePerformingAClinicalAssessment",
    )


class ObsoleteDefinedProcesses(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600065", "ObsoleteDefinedProcesses"
    )


class ObsoleteOccurrenceOfDisease(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110002", "ObsoleteOccurrenceOfDisease"
    )


class ObsoleteDisease(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110055", "ObsoleteDisease")


class ObsoleteCd8Receptor(ObsoleteClass):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110132", "ObsoleteCd8Receptor")


class ObsoleteMolecularLabelRole(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/REO_0000171", "ObsoleteMolecularLabelRole"
    )


class ObsoleteMolecularLabel(ObsoleteClass):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/REO_0000280", "ObsoleteMolecularLabel"
    )


class IndependentContinuant(Continuant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000004", "IndependentContinuant"
    )


class SpecificallyDependentContinuant(Continuant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000020", "SpecificallyDependentContinuant"
    )


class GenericallyDependentContinuant(Continuant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000031", "GenericallyDependentContinuant"
    )


class TemporalRegion(Occurrent):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000008", "TemporalRegion")


class SpatiotemporalRegion(Occurrent):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000011", "SpatiotemporalRegion")


class Process(Occurrent):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000015", "Process")


class ProcessBoundary(Occurrent):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000035", "ProcessBoundary")


class MaterialEntity(IndependentContinuant):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000040", "MaterialEntity")


class ImmaterialEntity(IndependentContinuant):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000141", "ImmaterialEntity")


class RealizableEntity(SpecificallyDependentContinuant):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000017", "RealizableEntity")


class Quality(SpecificallyDependentContinuant):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000019", "Quality")


class Quality(SpecificallyDependentContinuant):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000001", "Quality")


class InformationContentEntity(GenericallyDependentContinuant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000030", "InformationContentEntity"
    )


class Region(GenericallyDependentContinuant):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000001", "Region")


class OneDimensionalTemporalRegion(TemporalRegion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000038", "OneDimensionalTemporalRegion"
    )


class ZeroDimensionalTemporalRegion(TemporalRegion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000148", "ZeroDimensionalTemporalRegion"
    )


class ProcessProfile(Process):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000144", "ProcessProfile")


class History(Process):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000182", "History")


class MolecularFunction(Process):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0003674", "MolecularFunction")


class BiologicalProcess(Process):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0008150", "BiologicalProcess")


class PlannedProcess(Process):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000011", "PlannedProcess")


class UnplannedOccurrenceEffectingAnInvestigation(Process):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000076",
        "UnplannedOccurrenceEffectingAnInvestigation",
    )


class Planning(Process):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000339", "Planning")


class Scratching(Process):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003575", "Scratching")


class FiatObject(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000024", "FiatObject")


class ObjectAggregate(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000027", "ObjectAggregate")


class Object(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000030", "Object")


class MolecularEntity(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_23367", "MolecularEntity")


class RacLacticAcid(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_28358", "RacLacticAcid")


class Atom(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33250", "Atom")


class Cell(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000000", "Cell")


class ComplexOfMolecules(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/COB_0000080", "ComplexOfMolecules")


class Soil(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/ENVO_00001998", "Soil")


class EnvironmentalMaterial(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/ENVO_00010483", "EnvironmentalMaterial"
    )


class CellularComponent(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0005575", "CellularComponent")


class ProteinContainingComplex(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032991", "ProteinContainingComplex"
    )


class MaterialInformationBearer(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000178", "MaterialInformationBearer"
    )


class Pathogen(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IDO_0000528", "Pathogen")


class Antibacterial(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IDO_0000562", "Antibacterial")


class Infection(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IDO_0000586", "Infection")


class ProcessedMaterial(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000047", "ProcessedMaterial")


class Population(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000181", "Population")


class Organization(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000245", "Organization")


class Enzyme(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000427", "Enzyme")


class ScatteredMolecularAggregate(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000576", "ScatteredMolecularAggregate"
    )


class CapsuleShell(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000798", "CapsuleShell")


class GuarGum(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000814", "GuarGum")


class Manufacturer(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000835", "Manufacturer")


class GrowthEnvironment(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000997", "GrowthEnvironment")


class SequenceAnnotationProvider(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001947", "SequenceAnnotationProvider"
    )


class CollectionOfSpecimens(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002076", "CollectionOfSpecimens"
    )


class MaterialSupplier(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002989", "MaterialSupplier")


class MagneticResonanceImagingParticipant(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003329",
        "MagneticResonanceImagingParticipant",
    )


class Organism(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100026", "Organism")


class Specimen(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100051", "Specimen")


class GlucoseInSolution(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100086", "GlucoseInSolution")


class ChemicalSolution(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302729", "ChemicalSolution")


class Epitope(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110001", "Epitope")


class Immunogen(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110023", "Immunogen")


class Antigen(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110034", "Antigen")


class MaterialToBeAdded(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110108", "MaterialToBeAdded")


class TargetOfMaterialAddition(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110109", "TargetOfMaterialAddition"
    )


class Allergen(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110201", "Allergen")


class MaterialAnatomicalEntity(MaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0000465", "MaterialAnatomicalEntity"
    )


class AnatomicalCluster(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000477", "AnatomicalCluster")


class Vaccine(MaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/VO_0000001", "Vaccine")


class SpatialRegion(ImmaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000006", "SpatialRegion")


class Site(ImmaterialEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000029", "Site")


class ContinuantFiatBoundary(ImmaterialEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000140", "ContinuantFiatBoundary"
    )


class Disposition(RealizableEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000016", "Disposition")


class Role(RealizableEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000023", "Role")


class Plan(RealizableEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000260", "Plan")


class RelationalQuality(Quality):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000145", "RelationalQuality")


class BiologicalAttribute(Quality):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBA_0000001", "BiologicalAttribute")


class DeviceSetting(Quality):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000654", "DeviceSetting")


class Phenotype(Quality):
    term = RdfTerm("http://purl.obolibrary.org/obo/OGMS_0000023", "Phenotype")


class PhysicalObjectQuality(Quality):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0001241", "PhysicalObjectQuality"
    )


class Quantitative(Quality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0103000", "Quantitative")


class NarrativeObject(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000006", "NarrativeObject")


class DatumLabel(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000009", "DatumLabel")


class DataItem(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000027", "DataItem")


class Symbol(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000028", "Symbol")


class DirectiveInformationEntity(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000033", "DirectiveInformationEntity"
    )


class TextualEntity(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000300", "TextualEntity")


class Figure(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000308", "Figure")


class Document(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000310", "Document")


class EmailAddress(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000429", "EmailAddress")


class CentrallyRegisteredIdentifierRegistry(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000579",
        "CentrallyRegisteredIdentifierRegistry",
    )


class ListModeDataFile(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000021", "ListModeDataFile")


class EmedicalRecord(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000078", "EmedicalRecord")


class ElectronicCaseReportTabulation(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000083", "ElectronicCaseReportTabulation"
    )


class EsourceDocument(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000158", "EsourceDocument")


class ElectronicCaseReportForm(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000167", "ElectronicCaseReportForm"
    )


class AnalyticalCytologyDataFile(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000210", "AnalyticalCytologyDataFile"
    )


class FluorescenceCompensationMatrix(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000213", "FluorescenceCompensationMatrix"
    )


class RecordOfMissingKnowledge(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000852", "RecordOfMissingKnowledge"
    )


class SequenceFeatureAnnotation(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000905", "SequenceFeatureAnnotation"
    )


class TestableHypothesis(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001908", "TestableHypothesis")


class ConclusionBasedOnData(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001909", "ConclusionBasedOnData"
    )


class ValueSpecification(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001933", "ValueSpecification")


class PredictedValue(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001934", "PredictedValue")


class ReasonForLackOfDataItem(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002199", "ReasonForLackOfDataItem"
    )


class HormonalBirthControlUseHistory(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002401", "HormonalBirthControlUseHistory"
    )


class MenopausalStatus(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002410", "MenopausalStatus")


class ExposureToEnvironmentalAndWorkplaceCarcinogensHistory(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002415",
        "ExposureToEnvironmentalAndWorkplaceCarcinogensHistory",
    )


class IndicatorOfWhetherAnInclusionCriterionWasMet(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002421",
        "IndicatorOfWhetherAnInclusionCriterionWasMet",
    )


class IndicatorOfWhetherAllInclusionCriteriaWereMet(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002422",
        "IndicatorOfWhetherAllInclusionCriteriaWereMet",
    )


class NationalRegistry(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002617", "NationalRegistry")


class MinimumResolvedUnitOfMeasurement(InformationContentEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003657", "MinimumResolvedUnitOfMeasurement"
    )


class ValidatedInformation(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302838", "ValidatedInformation")


class CuratedInformation(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302840", "CuratedInformation")


class ClinicalHistory(InformationContentEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OGMS_0000015", "ClinicalHistory")


class PrimaryStructureOfDnaMacromolecule(Region):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000811",
        "PrimaryStructureOfDnaMacromolecule",
    )


class PrimaryStructureOfRnaMolecule(Region):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000845", "PrimaryStructureOfRnaMolecule"
    )


class Polypeptide(Region):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000104", "Polypeptide")


class Mirna(Region):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000276", "Mirna")


class ExperimentalFeature(Region):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0001410", "ExperimentalFeature")


class RegulatoryRegion(Region):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0005836", "RegulatoryRegion")


class AntigenBinding(MolecularFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0003823", "AntigenBinding")


class CatalyticActivity(MolecularFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0003824", "CatalyticActivity")


class ActionPotential(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0001508", "ActionPotential")


class AntibodyDependentCellularCytotoxicity(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0001788",
        "AntibodyDependentCellularCytotoxicity",
    )


class CytokineProduction(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0001816", "CytokineProduction")


class CellKilling(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0001906", "CellKilling")


class RegulationOfHeartRate(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0002027", "RegulationOfHeartRate")


class ToleranceInduction(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0002507", "ToleranceInduction")


class Hypersensitivity(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0002524", "Hypersensitivity")


class RespiratorySystemProcess(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0003016", "RespiratorySystemProcess"
    )


class GlomerularFiltration(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0003094", "GlomerularFiltration")


class GlucoseMetabolicProcess(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0006006", "GlucoseMetabolicProcess"
    )


class DnaReplication(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0006260", "DnaReplication")


class Phagocytosis(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0006909", "Phagocytosis")


class CellCycle(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0007049", "CellCycle")


class BloodCoagulation(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0007596", "BloodCoagulation")


class LearningOrMemory(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0007611", "LearningOrMemory")


class RegulationOfBloodPressure(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0008217", "RegulationOfBloodPressure"
    )


class CellPopulationProliferation(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0008283", "CellPopulationProliferation"
    )


class Fertilization(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0009566", "Fertilization")


class CellularProcess(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0009987", "CellularProcess")


class GeneExpression(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0010467", "GeneExpression")


class ImmunoglobulinMediatedImmuneResponse(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0016064",
        "ImmunoglobulinMediatedImmuneResponse",
    )


class AntigenProcessingAndPresentation(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0019882", "AntigenProcessingAndPresentation"
    )


class DevelopmentalMaturation(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0021700", "DevelopmentalMaturation"
    )


class ReproductiveProcess(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0022414", "ReproductiveProcess")


class ActinFilamentPolymerization(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0030041", "ActinFilamentPolymerization"
    )


class Hemopoiesis(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0030097", "Hemopoiesis")


class MacromoleculeLocalization(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0033036", "MacromoleculeLocalization"
    )


class GranzymeAProduction(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0035746", "GranzymeAProduction")


class PerforinProduction(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0035944", "PerforinProduction")


class GranulysinProduction(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0036262", "GranulysinProduction")


class TCellActivation(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0042110", "TCellActivation")


class CellularDevelopmentalProcess(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0048869", "CellularDevelopmentalProcess"
    )


class MulticellularOrganismalLevelHomeostasis(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0048871",
        "MulticellularOrganismalLevelHomeostasis",
    )


class ResponseToStimulus(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0050896", "ResponseToStimulus")


class NeuromuscularProcess(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0050905", "NeuromuscularProcess")


class ChromosomeOrganization(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0051276", "ChromosomeOrganization"
    )


class ActinPolymerizationDependentCellMotility(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0070358",
        "ActinPolymerizationDependentCellMotility",
    )


class GranzymeBProduction(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0071613", "GranzymeBProduction")


class DiseaseStage(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000278", "DiseaseStage")


class Binding(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001588", "Binding")


class ImmunoglobulinMediatedHistamineRelease(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001707",
        "ImmunoglobulinMediatedHistamineRelease",
    )


class HostExposureToInfectiousAgent(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110003", "HostExposureToInfectiousAgent"
    )


class EpitopeBindingByAdaptiveImmuneReceptor(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110014",
        "EpitopeBindingByAdaptiveImmuneReceptor",
    )


class EnvironmentalExposureToInfectiousAgent(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110024",
        "EnvironmentalExposureToInfectiousAgent",
    )


class ExposureResultingInImmuneReactivity(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110061",
        "ExposureResultingInImmuneReactivity",
    )


class Immunization(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110094", "Immunization")


class EnvironmentalProximityToInfectiousAgent(BiologicalProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110111",
        "EnvironmentalProximityToInfectiousAgent",
    )


class PathologicProcess(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110122", "PathologicProcess")


class DiseaseCourse(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OGMS_0000063", "DiseaseCourse")


class LifeCycleStage(BiologicalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000105", "LifeCycleStage")


class Documenting(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000572", "Documenting")


class AssigningACentrallyRegisteredIdentifier(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000574",
        "AssigningACentrallyRegisteredIdentifier",
    )


class Investigation(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000066", "Investigation")


class Assay(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000070", "Assay")


class MaterialProcessing(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000094", "MaterialProcessing")


class DrawingAConclusionBasedOnData(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000338", "DrawingAConclusionBasedOnData"
    )


class StudyDesignExecution(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000471", "StudyDesignExecution")


class SpecimenCollectionProcess(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000659", "SpecimenCollectionProcess"
    )


class AnimalFeeding(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000694", "AnimalFeeding")


class LaboratoryAnimalCare(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000708", "LaboratoryAnimalCare")


class InformingInvestigatorOfSubjectStudyArm(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000804",
        "InformingInvestigatorOfSubjectStudyArm",
    )


class PresentationOfStimulus(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000807", "PresentationOfStimulus"
    )


class InformedConsentProcess(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000810", "InformedConsentProcess"
    )


class Calibration(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000818", "Calibration")


class TreatmentPortionOfStudyExecution(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000826", "TreatmentPortionOfStudyExecution"
    )


class MaterialMaintenance(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000838", "MaterialMaintenance")


class UnblindingProcess(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000840", "UnblindingProcess")


class SubjectAgreesTheyUnderstandInformedConsentDocument(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000841",
        "SubjectAgreesTheyUnderstandInformedConsentDocument",
    )


class InformingSubjectOfStudyArm(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000842", "InformingSubjectOfStudyArm"
    )


class Supplying(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000907", "Supplying")


class StudyIntervention(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000931", "StudyIntervention")


class TrainingProcess(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000939", "TrainingProcess")


class ImageCreation(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001007", "ImageCreation")


class Service(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001173", "Service")


class DrawingAConclusion(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001834", "DrawingAConclusion")


class Selection(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001928", "Selection")


class ComparingPredictionToMeasurement(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001932", "ComparingPredictionToMeasurement"
    )


class SequenceAnnotation(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001944", "SequenceAnnotation")


class Freezing(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001953", "Freezing")


class DeterminationIfAssayWillProvideReliableResults(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002201",
        "DeterminationIfAssayWillProvideReliableResults",
    )


class MachineLearning(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002587", "MachineLearning")


class Fasting(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003653", "Fasting")


class DataTransformation(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200000", "DataTransformation")


class DataVisualization(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200111", "DataVisualization")


class DocumentEditing(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302908", "DocumentEditing")


class Prediction(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302910", "Prediction")


class Validation(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302911", "Validation")


class ExposureOfMaterialToEnvironment(PlannedProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600009", "ExposureOfMaterialToEnvironment"
    )


class GroupAssignment(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600015", "GroupAssignment")


class Treatment(PlannedProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OGMS_0000090", "Treatment")


class Water(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_15377", "Water")


class Atp(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_15422", "Atp")


class Cholesterol(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16113", "Cholesterol")


class Ammonia(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16134", "Ammonia")


class Phospholipid(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16247", "Phospholipid")


class Nitrite(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16301", "Nitrite")


class CarbonDioxide(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16526", "CarbonDioxide")


class Creatinine(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16737", "Creatinine")


class MycophenolicAcid(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_168396", "MycophenolicAcid")


class Creatine(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16919", "Creatine")


class BilirubinIxalpha(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16990", "BilirubinIxalpha")


class Progesterone(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17026", "Progesterone")


class Hydrogensulfite(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17137", "Hydrogensulfite")


class Glucose(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17234", "Glucose")


class Testosterone(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17347", "Testosterone")


class Hydrogencarbonate(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17544", "Hydrogencarbonate")


class Cortisol(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17650", "Cortisol")


class _5AdenylylSulfate(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17709", "_5AdenylylSulfate")


class Triglyceride(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17855", "Triglyceride")


class Chloride(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17996", "Chloride")


class BileSalt(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_22868", "BileSalt")


class Cytochalasin(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_23528", "Cytochalasin")


class Estradiol(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_23965", "Estradiol")


class NEthylNNitrosourea(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_23995", "NEthylNNitrosourea")


class Proton(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_24636", "Proton")


class IronCation(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_24875", "IronCation")


class Luciferin(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_25078", "Luciferin")


class Amikacin(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_2637", "Amikacin")


class SodiumChloride(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_26710", "SodiumChloride")


class UricAcid(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_27226", "UricAcid")


class Lead0(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_27889", "Lead0")


class Acrylamide(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_28619", "Acrylamide")


class Dehydroepiandrosterone(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_28689", "Dehydroepiandrosterone"
    )


class Tobramycin(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_28864", "Tobramycin")


class Sodium1(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_29101", "Sodium1")


class Potassium1(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_29103", "Potassium1")


class Hydroxyl(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_29191", "Hydroxyl")


class RutheniumAtom(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_30682", "RutheniumAtom")


class GadodiamideHydrate(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_31642", "GadodiamideHydrate")


class Gadoteridol(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_31643", "Gadoteridol")


class PhenolRed(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_31991", "PhenolRed")


class SodiumCitrateDihydrate(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_32142", "SodiumCitrateDihydrate"
    )


class MethylGroup(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_32875", "MethylGroup")


class ElementalOxygen(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33262", "ElementalOxygen")


class RhodiumAtom(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33359", "RhodiumAtom")


class GadoliniumAtom(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33375", "GadoliniumAtom")


class TerbiumAtom(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33376", "TerbiumAtom")


class AminoAcid(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33709", "AminoAcid")


class Macromolecule(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33839", "Macromolecule")


class FattyAcid(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_35366", "FattyAcid")


class GadoliniumMolecularEntity(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_35729", "GadoliniumMolecularEntity"
    )


class PhosphateIon(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_35780", "PhosphateIon")


class Gadodiamide(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_37333", "Gadodiamide")


class FolicAcids(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_37445", "FolicAcids")


class SodiumPhosphate(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_37586", "SodiumPhosphate")


class CalciumIon(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_39124", "CalciumIon")


class MagnesiumCation(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_39127", "MagnesiumCation")


class Edta4(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_42191", "Edta4")


class Deoxyribonucleotide(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_4431", "Deoxyribonucleotide")


class Digoxin(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_4551", "Digoxin")


class _5Bromo2Deoxyuridine(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_472552", "_5Bromo2Deoxyuridine"
    )


class LowDensityLipoproteinCholesterol(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_47774", "LowDensityLipoproteinCholesterol"
    )


class HighDensityLipoproteinCholesterol(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_47775",
        "HighDensityLipoproteinCholesterol",
    )


class Chromium51(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_50076", "Chromium51")


class TritiatedThymidine(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_53526", "TritiatedThymidine")


class DimethylSulfate(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_59050", "DimethylSulfate")


class DiethylPyrocarbonate(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_59051", "DiethylPyrocarbonate")


class _11Dihydroxy3Ethoxy2Butanone(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_59052", "_11Dihydroxy3Ethoxy2Butanone"
    )


class NCyclohexylN24MorpholinylEthylCarbodiimide(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_59053",
        "NCyclohexylN24MorpholinylEthylCarbodiimide",
    )


class NMethylisatoicAnhydride(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_59054", "NMethylisatoicAnhydride"
    )


class S14BromoacetamidobenzylEdta(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_59055", "S14BromoacetamidobenzylEdta"
    )


class EdtaMethidiumpropylamide(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_59056", "EdtaMethidiumpropylamide"
    )


class BromophenolBlue(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_59424", "BromophenolBlue")


class TacrolimusHydrate(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_61057", "TacrolimusHydrate")


class OxygenRadical(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_61073", "OxygenRadical")


class LuteinizingHormone(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_81568", "LuteinizingHormone")


class FollicleStimulatingHormone(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_81569", "FollicleStimulatingHormone"
    )


class _25HydroxyvitaminD2(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_86319", "_25HydroxyvitaminD2")


class Tris(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_9754", "Tris")


class PolyethyleneGlycolP1133TetramethylbutylPhenylEther(MolecularEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000065",
        "PolyethyleneGlycolP1133TetramethylbutylPhenylEther",
    )


class Fucoidan(MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000817", "Fucoidan")


class DeuteriumAtom(MolecularEntity, Atom):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_29237", "DeuteriumAtom")


class RareEarthMetalAtom(Atom):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33321", "RareEarthMetalAtom")


class ObsoleteNativeCell(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000003", "ObsoleteNativeCell")


class Sperm(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000019", "Sperm")


class Fibroblast(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000057", "Fibroblast")


class EpithelialCell(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000066", "EpithelialCell")


class MastCell(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000097", "MastCell")


class Erythrocyte(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000232", "Erythrocyte")


class Platelet(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000233", "Platelet")


class Macrophage(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000235", "Macrophage")


class DendriticCell(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000451", "DendriticCell")


class Megakaryocyte(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000556", "Megakaryocyte")


class Reticulocyte(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000558", "Reticulocyte")


class Leukocyte(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000738", "Leukocyte")


class Basophil(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000767", "Basophil")


class Promyelocyte(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000836", "Promyelocyte")


class MononuclearCell(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000842", "MononuclearCell")


class MalignantCell(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0001064", "MalignantCell")


class Metamyelocyte(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0002192", "Metamyelocyte")


class Myelocyte(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0002193", "Myelocyte")


class NeuralCell(Cell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0002319", "NeuralCell")


class AntigenAntibodyComplex(ComplexOfMolecules):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003119", "AntigenAntibodyComplex"
    )


class EpitopeMhcTcrComplex(ComplexOfMolecules):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003120", "EpitopeMhcTcrComplex")


class MhcLigandComplex(ComplexOfMolecules):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003121", "MhcLigandComplex")


class Podzol(Soil):
    term = RdfTerm("http://purl.obolibrary.org/obo/ENVO_00002257", "Podzol")


class Chromatin(CellularComponent):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0000785", "Chromatin")


class Chromosome(CellularComponent):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0005694", "Chromosome")


class MembraneBoundedOrganelle(CellularComponent):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0043227", "MembraneBoundedOrganelle"
    )


class FibrinogenComplex(ProteinContainingComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0005577", "FibrinogenComplex")


class ImmunoglobulinComplex(ProteinContainingComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0019814", "ImmunoglobulinComplex")


class MhcProteinComplex(ProteinContainingComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0042611", "MhcProteinComplex")


class FerritinComplex(ProteinContainingComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0070288", "FerritinComplex")


class AdaptiveImmuneReceptor(ProteinContainingComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110022", "AdaptiveImmuneReceptor"
    )


class CytosolicCreatineKinaseComplexMbType(ProteinContainingComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000027247",
        "CytosolicCreatineKinaseComplexMbType",
    )


class LactateDehydrogenaseComplex(ProteinContainingComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000050331", "LactateDehydrogenaseComplex"
    )


class HemoglobinA1C(ProteinContainingComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000050469", "HemoglobinA1C")


class RandomAccessMemory(MaterialInformationBearer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001877", "RandomAccessMemory")


class ExperimentallyModifiedCellInVitro(Cell, ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CL_0000578", "ExperimentallyModifiedCellInVitro"
    )


class PhysicalDocument(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000044", "PhysicalDocument")


class CultureMedium(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000079", "CultureMedium")


class Precipitate(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000286", "Precipitate")


class Eluate(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000318", "Eluate")


class Extract(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000423", "Extract")


class PolyacrylamideGel(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000432", "PolyacrylamideGel")


class AgaroseGel(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000439", "AgaroseGel")


class PairedEndLibrary(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000722", "PairedEndLibrary")


class RecombinantVector(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000731", "RecombinantVector")


class Ntp2000(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000735", "Ntp2000")


class SingleFragmentLibrary(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000736", "SingleFragmentLibrary"
    )


class BerichromRAntithrombinIiiAKit(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000815", "BerichromRAntithrombinIiiAKit"
    )


class Pill(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000827", "Pill")


class Device(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000968", "Device")


class GeneticallyModifiedMaterial(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001151", "GeneticallyModifiedMaterial"
    )


class PurifiedMaterial(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001633", "PurifiedMaterial")


class CellCulture(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001876", "CellCulture")


class Reagent(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001879", "Reagent")


class CellFreezingMedium(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001912", "CellFreezingMedium")


class MolecularLabeledMaterial(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001936", "MolecularLabeledMaterial"
    )


class MultiplexedSequencingLibrary(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001970", "MultiplexedSequencingLibrary"
    )


class EnzymeLinkedAntibody(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002047", "EnzymeLinkedAntibody")


class DeliveryFormForHormonalReplacementTherapy(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002406",
        "DeliveryFormForHormonalReplacementTherapy",
    )


class ErccRnaSpikeIn(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002462", "ErccRnaSpikeIn")


class SirvRnaSpikeIn(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002463", "SirvRnaSpikeIn")


class CdnaLibrary(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002754", "CdnaLibrary")


class EpsteinBarrVirusTransformedBCell(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100010", "EpsteinBarrVirusTransformedBCell"
    )


class Xenograft(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100058", "Xenograft")


class CulturedCellPopulation(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100060", "CulturedCellPopulation"
    )


class ScreeningLibrary(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100064", "ScreeningLibrary")


class OrganSection(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100066", "OrganSection")


class DecapitatedOrganism(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302837", "DecapitatedOrganism")


class ParticleDeliveryVessel(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400081", "ParticleDeliveryVessel"
    )


class PiezoElectricCrystal(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400085", "PiezoElectricCrystal")


class CellCultureSupernatant(ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1000023", "CellCultureSupernatant"
    )


class CellPellet(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1000024", "CellPellet")


class CellLysate(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1000036", "CellLysate")


class PeptideConstruct(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1000042", "PeptideConstruct")


class AssayBead(ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1000207", "AssayBead")


class LaboratoryBasedPopulation(Population):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003086", "LaboratoryBasedPopulation"
    )


class StudyArmPopulation(Population):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003706", "StudyArmPopulation")


class RegulatoryAgency(Organization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000450", "RegulatoryAgency")


class ResearchOrganization(Organization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000828", "ResearchOrganization")


class BioinformaticsResourceCenter(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001626", "BioinformaticsResourceCenter"
    )


class OrganizationOfSpecimenProviderPrincipalInvestigator(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001880",
        "OrganizationOfSpecimenProviderPrincipalInvestigator",
    )


class OrganizationOfBioinformaticsResourceCenterContactPerson(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001881",
        "OrganizationOfBioinformaticsResourceCenterContactPerson",
    )


class SpecimenRepositoryOrganization(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001885", "SpecimenRepositoryOrganization"
    )


class OrganizationOfSpecimenCollector(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001893", "OrganizationOfSpecimenCollector"
    )


class OrganizationOfSequencingFacilityContactPerson(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001897",
        "OrganizationOfSequencingFacilityContactPerson",
    )


class GrantAgency(Organization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001942", "GrantAgency")


class CourierOrganization(Organization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002190", "CourierOrganization")


class MolecularAnalysisFacilityOrganization(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002198",
        "MolecularAnalysisFacilityOrganization",
    )


class ClinicalStudyCenter(Organization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003068", "ClinicalStudyCenter")


class BiomedicalLaboratoryOrganization(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003250", "BiomedicalLaboratoryOrganization"
    )


class HospitalOrganization(Organization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OMRSE_00000056", "HospitalOrganization"
    )


class DnaPolymeraseComplex(ProteinContainingComplex, Enzyme):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0042575", "DnaPolymeraseComplex")


class ReverseTranscriptase(Enzyme):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000419", "ReverseTranscriptase")


class DissolvedMaterialEntity(ScatteredMolecularAggregate):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0302876", "DissolvedMaterialEntity"
    )


class Atmosphere(GrowthEnvironment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001498", "Atmosphere")


class SpecimensDerivedFromSharedAncestor(CollectionOfSpecimens):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002077",
        "SpecimensDerivedFromSharedAncestor",
    )


class SpecimensCollectedInOneEncounter(CollectionOfSpecimens):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002079", "SpecimensCollectedInOneEncounter"
    )


class SpecimensCollectedLongitudinally(CollectionOfSpecimens):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002081", "SpecimensCollectedLongitudinally"
    )


class Viruses(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_10239", "Viruses")


class Bacteria(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_2", "Bacteria")


class Archaea(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_2157", "Archaea")


class Eukaryota(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_2759", "Eukaryota")


class InfectiousAgent(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000925", "InfectiousAgent")


class SelectivelyMaintainedOrganism(Organism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001185", "SelectivelyMaintainedOrganism"
    )


class BloodMealSourceOrganism(Organism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002995", "BloodMealSourceOrganism"
    )


class Chimera(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100014", "Chimera")


class HostOfImmuneResponse(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110026", "HostOfImmuneResponse")


class ParasiteOrganism(Organism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OPL_0000232", "ParasiteOrganism")


class ProcessedSpecimen(ProcessedMaterial, Specimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000953", "ProcessedSpecimen")


class WholeOrganismPreparation(Specimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000680", "WholeOrganismPreparation"
    )


class MaterialSample(Specimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000747", "MaterialSample")


class SpecimenWithKnownStorageState(Specimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001472", "SpecimenWithKnownStorageState"
    )


class SpecimenFromOrganism(Specimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001479", "SpecimenFromOrganism")


class SwabSpecimen(Specimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002599", "SwabSpecimen")


class IndividualOrganismSpecimen(Specimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002648", "IndividualOrganismSpecimen"
    )


class PhosphateBufferedSalineSolution(ChemicalSolution):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100046", "PhosphateBufferedSalineSolution"
    )


class Neoplasm(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/HP_0002664", "Neoplasm")


class UterineCervix(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000002", "UterineCervix")


class PituitaryGland(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000007", "PituitaryGland")


class PeripheralNervousSystem(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0000010", "PeripheralNervousSystem"
    )


class LymphNode(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000029", "LymphNode")


class Urethra(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000057", "Urethra")


class Cloaca(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000162", "Cloaca")


class Mouth(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000165", "Mouth")


class Amnion(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000305", "Amnion")


class Breast(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000310", "Breast")


class Throat(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000341", "Throat")


class OrganismSubstance(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000463", "OrganismSubstance")


class Testis(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000473", "Testis")


class Tissue(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000479", "Tissue")


class MultiTissueStructure(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0000481", "MultiTissueStructure"
    )


class Stomach(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000945", "Stomach")


class Aorta(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000947", "Aorta")


class Heart(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000948", "Heart")


class Brain(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000955", "Brain")


class CerebralCortex(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000956", "CerebralCortex")


class Eye(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000970", "Eye")


class Leg(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000978", "Leg")


class Ovary(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000992", "Ovary")


class Uterus(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000995", "Uterus")


class Vagina(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000996", "Vagina")


class RespiratorySystem(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001004", "RespiratorySystem")


class StrandOfHair(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001037", "StrandOfHair")


class Rectum(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001052", "Rectum")


class Diaphragm(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001103", "Diaphragm")


class Colon(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001155", "Colon")


class SigmoidColon(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001159", "SigmoidColon")


class CortexOfKidney(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001225", "CortexOfKidney")


class UrinaryBladder(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001255", "UrinaryBladder")


class Pancreas(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001264", "Pancreas")


class TibialNerve(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001323", "TibialNerve")


class Arm(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001460", "Arm")


class KneeJoint(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001485", "KneeJoint")


class AnkleJoint(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001488", "AnkleJoint")


class DigestiveTract(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001555", "DigestiveTract")


class UpperRespiratoryTract(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0001557", "UpperRespiratoryTract"
    )


class LowerRespiratoryTract(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0001558", "LowerRespiratoryTract"
    )


class Cheek(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001567", "Cheek")


class FacialMuscle(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001577", "FacialMuscle")


class Artery(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001637", "Artery")


class Vein(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001638", "Vein")


class Tongue(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001723", "Tongue")


class Nasopharynx(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001728", "Nasopharynx")


class Oropharynx(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001729", "Oropharynx")


class Conjunctiva(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001811", "Conjunctiva")


class NasalCavityMucosa(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001826", "NasalCavityMucosa")


class MinorSalivaryGland(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0001830", "MinorSalivaryGland"
    )


class CaudateNucleus(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001873", "CaudateNucleus")


class Putamen(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001874", "Putamen")


class Placenta(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001987", "Placenta")


class Areola(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002032", "Areola")


class ThyroidGland(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002046", "ThyroidGland")


class Lung(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002048", "Lung")


class Dermis(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002067", "Dermis")


class Hypodermis(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002072", "Hypodermis")


class SkinOfBody(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002097", "SkinOfBody")


class Spleen(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002106", "Spleen")


class Liver(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002107", "Liver")


class Ileum(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002116", "Ileum")


class Integument(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002199", "Integument")


class ProstateGland(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002367", "ProstateGland")


class AdrenalGland(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002369", "AdrenalGland")


class ForelimbZeugopod(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002386", "ForelimbZeugopod")


class ManualDigit(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002389", "ManualDigit")


class Tail(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002415", "Tail")


class LymphoidSystem(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002465", "LymphoidSystem")


class EsophagusMucosa(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002469", "EsophagusMucosa")


class LeftCerebralHemisphere(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0002812", "LeftCerebralHemisphere"
    )


class RightCerebralHemisphere(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0002813", "RightCerebralHemisphere"
    )


class Trachea(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0003126", "Trachea")


class Cranium(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0003128", "Cranium")


class Omentum(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0003688", "Omentum")


class MucosaOfNasopharynx(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0005022", "MucosaOfNasopharynx"
    )


class MucosaOfOropharynx(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0005023", "MucosaOfOropharynx"
    )


class MiddleNasalConcha(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0005921", "MiddleNasalConcha")


class ChorionicVillus(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0007106", "ChorionicVillus")


class EsophagogastricJunction(MaterialAnatomicalEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0007650", "EsophagogastricJunction"
    )


class Brachioradialis(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0011011", "Brachioradialis")


class SuprapubicSkin(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0036149", "SuprapubicSkin")


class AnteriorNasalWall(MaterialAnatomicalEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_3000016", "AnteriorNasalWall")


class TwoDimensionalSpatialRegion(SpatialRegion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000009", "TwoDimensionalSpatialRegion"
    )


class ZeroDimensionalSpatialRegion(SpatialRegion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000018", "ZeroDimensionalSpatialRegion"
    )


class OneDimensionalSpatialRegion(SpatialRegion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000026", "OneDimensionalSpatialRegion"
    )


class ThreeDimensionalSpatialRegion(SpatialRegion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000028", "ThreeDimensionalSpatialRegion"
    )


class GeographicLocation(Site):
    term = RdfTerm("http://purl.obolibrary.org/obo/GAZ_00000448", "GeographicLocation")


class InterrogationPoint(Site):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400059", "InterrogationPoint")


class JetInAirFlowChamber(Site):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400061", "JetInAirFlowChamber")


class OneDimensionalContinuantFiatBoundary(ContinuantFiatBoundary):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000142",
        "OneDimensionalContinuantFiatBoundary",
    )


class TwoDimensionalContinuantFiatBoundary(ContinuantFiatBoundary):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000146",
        "TwoDimensionalContinuantFiatBoundary",
    )


class ZeroDimensionalContinuantFiatBoundary(ContinuantFiatBoundary):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000147",
        "ZeroDimensionalContinuantFiatBoundary",
    )


class Function(Disposition):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000034", "Function")


class InsulinResistance(Disposition):
    term = RdfTerm("http://purl.obolibrary.org/obo/HP_0000855", "InsulinResistance")


class PathogenicDisposition(Disposition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IDO_0000450", "PathogenicDisposition"
    )


class DispositionToBeBoundByAnMhcProteinComplex(Disposition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001486",
        "DispositionToBeBoundByAnMhcProteinComplex",
    )


class DispositionToBeAProductOfAntigenProcessingAndPresentation(Disposition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001511",
        "DispositionToBeAProductOfAntigenProcessingAndPresentation",
    )


class DispositionToCauseAnAllergicReaction(Disposition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110010",
        "DispositionToCauseAnAllergicReaction",
    )


class DispositionToBeBoundByAnAdaptiveImmuneReceptor(Disposition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110045",
        "DispositionToBeBoundByAnAdaptiveImmuneReceptor",
    )


class DispositionToInfectAnOrganism(Disposition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110093", "DispositionToInfectAnOrganism"
    )


class Disease(Disposition):
    term = RdfTerm("http://purl.obolibrary.org/obo/OGMS_0000031", "Disease")


class RegulatoryRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000017", "RegulatoryRole")


class ReferenceSubstanceRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000025", "ReferenceSubstanceRole"
    )


class CentrifugePelletRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000029", "CentrifugePelletRole")


class SupernatantRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000034", "SupernatantRole")


class DrugRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000040", "DrugRole")


class EvaluantRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000067", "EvaluantRole")


class DetectorReagentRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000091", "DetectorReagentRole")


class PatientRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000093", "PatientRole")


class ParticipantUnderInvestigationRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000097",
        "ParticipantUnderInvestigationRole",
    )


class SpecimenRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000112", "SpecimenRole")


class StudyGroupRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000174", "StudyGroupRole")


class InvestigationAgentRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000202", "InvestigationAgentRole"
    )


class NutrientRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000204", "NutrientRole")


class AntigenRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000237", "AntigenRole")


class MaterialToBeAddedRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000319", "MaterialToBeAddedRole"
    )


class CloningInsertRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000416", "CloningInsertRole")


class TargetOfMaterialAdditionRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000444", "TargetOfMaterialAdditionRole"
    )


class ManufacturerRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000571", "ManufacturerRole")


class PathogenRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000718", "PathogenRole")


class HostRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000725", "HostRole")


class TestSubstanceRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000847", "TestSubstanceRole")


class ComplementaryNucleotideProbeRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000857", "ComplementaryNucleotideProbeRole"
    )


class ServiceConsumerRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000941", "ServiceConsumerRole")


class ServiceProviderRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000947", "ServiceProviderRole")


class AccessedMaterialRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000949", "AccessedMaterialRole")


class ContactRepresentativeRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001687", "ContactRepresentativeRole"
    )


class MeasurandRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002444", "MeasurandRole")


class BloodMealSourceRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002996", "BloodMealSourceRole")


class ArthropodAttractorRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002997", "ArthropodAttractorRole"
    )


class ReactantRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003610", "ReactantRole")


class BufferRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302731", "BufferRole")


class SoluteRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302733", "SoluteRole")


class RandomizedGroupParticipantRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0302846", "RandomizedGroupParticipantRole"
    )


class ImmunogenRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110082", "ImmunogenRole")


class HostOfImmuneResponseRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110083", "HostOfImmuneResponseRole"
    )


class RestrictingMhcRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110086", "RestrictingMhcRole")


class DonorRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110087", "DonorRole")


class ImmuneEpitopeCarrierRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110091", "ImmuneEpitopeCarrierRole"
    )


class AdjuvantRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110092", "AdjuvantRole")


class HealthCareProviderRole(Role):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OMRSE_00000012", "HealthCareProviderRole"
    )


class HospitalRole(Role):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMRSE_00000054", "HospitalRole")


class LimbCoordinationEfficacy(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060180", "LimbCoordinationEfficacy"
    )


class WholeOrganismStability(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060184", "WholeOrganismStability"
    )


class FacialMusclePerformance(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060185", "FacialMusclePerformance"
    )


class PeripheralNervousSystemFunction(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060186", "PeripheralNervousSystemFunction"
    )


class KneeJointFunctionality(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060187", "KneeJointFunctionality"
    )


class AnkleJointFunctionality(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060188", "AnkleJointFunctionality"
    )


class TendonOfBicepsBrachiiFunctionality(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060189",
        "TendonOfBicepsBrachiiFunctionality",
    )


class BrachioradialisFunctionality(BiologicalAttribute):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060190", "BrachioradialisFunctionality"
    )


class DnaResidueMethylation(PhysicalObjectQuality):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000831", "DnaResidueMethylation"
    )


class SecondaryStructureOfSequenceMacromolecule(PhysicalObjectQuality):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000885",
        "SecondaryStructureOfSequenceMacromolecule",
    )


class Morphology(PhysicalObjectQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000051", "Morphology")


class PhysicalQuality(PhysicalObjectQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001018", "PhysicalQuality")


class OrganismalQuality(PhysicalObjectQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001995", "OrganismalQuality")


class PopulationQuality(PhysicalObjectQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0002003", "PopulationQuality")


class AnatomicalStructureQuality(PhysicalObjectQuality):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0070044", "AnatomicalStructureQuality"
    )


class Circular(PhysicalObjectQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000988", "Circular")


class Amount(Quantitative):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000070", "Amount")


class MeasurementUnitLabel(DatumLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000003", "MeasurementUnitLabel")


class CategoricalLabel(DatumLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000963", "CategoricalLabel")


class DataSet(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000100", "DataSet")


class DataAboutAnOntologyPart(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000102", "DataAboutAnOntologyPart"
    )


class MeasurementDatum(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000109", "MeasurementDatum")


class OneDimensionalCartesianSpatialCoordinateDatum(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000401",
        "OneDimensionalCartesianSpatialCoordinateDatum",
    )


class QuantitativeConfidenceValue(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000071", "QuantitativeConfidenceValue"
    )


class CenterValue(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000674", "CenterValue")


class AverageValue(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000679", "AverageValue")


class BindingDatum(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001181", "BindingDatum")


class GeneticCharacteristicsInformation(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001404",
        "GeneticCharacteristicsInformation",
    )


class GenomeCoverage(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001939", "GenomeCoverage")


class OperationalTaxonomicUnitMatrix(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001968", "OperationalTaxonomicUnitMatrix"
    )


class DateProcessStarted(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002471", "DateProcessStarted")


class NumberOfPcrCyclesDuringLibraryConstruction(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002475",
        "NumberOfPcrCyclesDuringLibraryConstruction",
    )


class NumberOfRoundsOfAmplification(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002476", "NumberOfRoundsOfAmplification"
    )


class SpikeInDilutionFactor(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002483", "SpikeInDilutionFactor"
    )


class PassageHistoryRecord(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002748", "PassageHistoryRecord")


class PrevalenceOfPathogenInSpecimens(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002992", "PrevalenceOfPathogenInSpecimens"
    )


class PrevalenceOfBloodMealSpecimensFromAHostOrganism(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002993",
        "PrevalenceOfBloodMealSpecimensFromAHostOrganism",
    )


class PresenceOfBloodFromHostOrganismInBloodMealSpecimen(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002994",
        "PresenceOfBloodFromHostOrganismInBloodMealSpecimen",
    )


class InsecticideResistanceDatum(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003063", "InsecticideResistanceDatum"
    )


class OrganismDetectionDatum(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003064", "OrganismDetectionDatum"
    )


class EntomologicalDataItem(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003077", "EntomologicalDataItem"
    )


class BloodAssayDatum(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003243", "BloodAssayDatum")


class FecesAssayDatum(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003245", "FecesAssayDatum")


class UrineAssayDatum(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003247", "UrineAssayDatum")


class InducedSputumAssayDatum(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003249", "InducedSputumAssayDatum"
    )


class CerebrospinalFluidAssayDatum(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003252", "CerebrospinalFluidAssayDatum"
    )


class EndotrachealAspirateAssayDatum(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003254", "EndotrachealAspirateAssayDatum"
    )


class MilkAssayDatum(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003365", "MilkAssayDatum")


class AntigenSpecificAntibodiesAssayDatum(DataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003417",
        "AntigenSpecificAntibodiesAssayDatum",
    )


class PredictedDataItem(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302867", "PredictedDataItem")


class Diagnosis(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OGMS_0000073", "Diagnosis")


class ClinicalDataItem(DataItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OGMS_0000123", "ClinicalDataItem")


class CentrallyRegisteredIdentifierSymbol(Symbol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000577",
        "CentrallyRegisteredIdentifierSymbol",
    )


class ParticipantIdentifier(Symbol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003071", "ParticipantIdentifier"
    )


class ConditionalSpecification(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000001", "ConditionalSpecification"
    )


class ObjectiveSpecification(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000005", "ObjectiveSpecification"
    )


class DataFormatSpecification(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000098", "DataFormatSpecification"
    )


class PlanSpecification(DirectiveInformationEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000104", "PlanSpecification")


class DataRepresentationalModel(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000658", "DataRepresentationalModel"
    )


class StudyDesignIndependentVariable(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000750", "StudyDesignIndependentVariable"
    )


class StudyDesignDependentVariable(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000751", "StudyDesignDependentVariable"
    )


class StudyDesignControlledVariable(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000785", "StudyDesignControlledVariable"
    )


class DoseSpecification(DirectiveInformationEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000969", "DoseSpecification")


class SelectionCriterion(DirectiveInformationEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001755", "SelectionCriterion")


class TargetGeneSpecification(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001962", "TargetGeneSpecification"
    )


class TargetSubfragmentSpecification(DirectiveInformationEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001963", "TargetSubfragmentSpecification"
    )


class Table(TextualEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000306", "Table")


class PostalAddress(TextualEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000422", "PostalAddress")


class DiagnosisTextualEntity(TextualEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000075", "DiagnosisTextualEntity"
    )


class CountryName(TextualEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001627", "CountryName")


class CommentOnInvestigation(TextualEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001898", "CommentOnInvestigation"
    )


class SequenceAssemblyName(TextualEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001948", "SequenceAssemblyName")


class CommonNameOfOrganism(TextualEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003074", "CommonNameOfOrganism")


class Graph(Figure):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000038", "Graph")


class Image(Figure):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000101", "Image")


class Report(Document):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000088", "Report")


class Publication(Document):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000311", "Publication")


class Questionnaire(Document):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001000", "Questionnaire")


class GenealogicalRecord(Document):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002616", "GenealogicalRecord")


class EditedDocument(Document):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302874", "EditedDocument")


class EmailAddressOfBioinformaticsResourceCenterContactPerson(EmailAddress):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001887",
        "EmailAddressOfBioinformaticsResourceCenterContactPerson",
    )


class EmailAddressOfSpecimenCollector(EmailAddress):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001890", "EmailAddressOfSpecimenCollector"
    )


class EmailAddressOfSequencingFacilityContactPerson(EmailAddress):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001894",
        "EmailAddressOfSequencingFacilityContactPerson",
    )


class EmailAddressOfSpecimenProviderPrincipalInvestigator(EmailAddress):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001903",
        "EmailAddressOfSpecimenProviderPrincipalInvestigator",
    )


class RecordOfUnknownSex(RecordOfMissingKnowledge):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000858", "RecordOfUnknownSex")


class ConclusionTextualEntity(ConclusionBasedOnData, TextualEntity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000144", "ConclusionTextualEntity"
    )


class DiagnosisOfAnOrganism(ConclusionBasedOnData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003367", "DiagnosisOfAnOrganism"
    )


class NumberOfErrors(DataItem, ValueSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001873", "NumberOfErrors")


class CategoricalValueSpecification(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001930", "CategoricalValueSpecification"
    )


class ScalarValueSpecification(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001931", "ScalarValueSpecification"
    )


class RnaIntegrityNumberValueSpecification(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002137",
        "RnaIntegrityNumberValueSpecification",
    )


class TemperatureValueSpecification(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002138", "TemperatureValueSpecification"
    )


class VolumeValueSpecification(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002139", "VolumeValueSpecification"
    )


class MinimumAgeValueSpecification(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002556", "MinimumAgeValueSpecification"
    )


class MaximumAgeValueSpecification(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002557", "MaximumAgeValueSpecification"
    )


class UpperLimitOfDetection(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003548", "UpperLimitOfDetection"
    )


class LowerLimitOfDetection(ValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003549", "LowerLimitOfDetection"
    )


class PredictedMassValue(PredictedValue):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001935", "PredictedMassValue")


class CannotBeAssessedDetermination(ReasonForLackOfDataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002200", "CannotBeAssessedDetermination"
    )


class HormonalBirthControlFormerUseHistory(HormonalBirthControlUseHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002402",
        "HormonalBirthControlFormerUseHistory",
    )


class HormonalBirthControlCurrentUseHistory(HormonalBirthControlUseHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002403",
        "HormonalBirthControlCurrentUseHistory",
    )


class NoHormonalBirthControlUseHistory(HormonalBirthControlUseHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002404", "NoHormonalBirthControlUseHistory"
    )


class IndeterminateMenopausalStatus(MenopausalStatus):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002411", "IndeterminateMenopausalStatus"
    )


class PremenopausalStatus(MenopausalStatus):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002412", "PremenopausalStatus")


class PerimenopausalStatus(MenopausalStatus):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002413", "PerimenopausalStatus")


class PostmenopausalStatus(MenopausalStatus):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002414", "PostmenopausalStatus")


class ExposureToArsenicHistory(ExposureToEnvironmentalAndWorkplaceCarcinogensHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002416", "ExposureToArsenicHistory"
    )


class ExposureToAsbestosHistory(ExposureToEnvironmentalAndWorkplaceCarcinogensHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002417", "ExposureToAsbestosHistory"
    )


class ExposureToDieselExhaustHistory(
    ExposureToEnvironmentalAndWorkplaceCarcinogensHistory
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002418", "ExposureToDieselExhaustHistory"
    )


class ExposureToChromiumHistory(ExposureToEnvironmentalAndWorkplaceCarcinogensHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002419", "ExposureToChromiumHistory"
    )


class ExposureToSilicaHistory(ExposureToEnvironmentalAndWorkplaceCarcinogensHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002420", "ExposureToSilicaHistory"
    )


class NationalBiomedicalRegistry(NationalRegistry):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002618", "NationalBiomedicalRegistry"
    )


class ClinicalHistoryOfCancer(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002368", "ClinicalHistoryOfCancer"
    )


class ClinicalHistoryDevoidOfCancer(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002369", "ClinicalHistoryDevoidOfCancer"
    )


class UnknownClinicalHistoryOfCancer(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002370", "UnknownClinicalHistoryOfCancer"
    )


class FamilyClinicalHistoryOfCancer(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002372", "FamilyClinicalHistoryOfCancer"
    )


class ClinicalHistoryOfRepeatedHivAssays(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002389",
        "ClinicalHistoryOfRepeatedHivAssays",
    )


class ExposureToSecondHandSmoke(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002390", "ExposureToSecondHandSmoke"
    )


class PregnancyHistory(ClinicalHistory):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002393", "PregnancyHistory")


class GynecologicSurgeryHistory(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002397", "GynecologicSurgeryHistory"
    )


class HormonalReplacementTherapyHistory(ClinicalHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002405",
        "HormonalReplacementTherapyHistory",
    )


class Assembly(ExperimentalFeature):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0001248", "Assembly")


class TfBindingSite(RegulatoryRegion):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000235", "TfBindingSite")


class PeptideAntigenBinding(AntigenBinding):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0042605", "PeptideAntigenBinding")


class LIditol2DehydrogenaseNadActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0003939", "LIditol2DehydrogenaseNadActivity"
    )


class RnaDirectedDnaPolymeraseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0003964", "RnaDirectedDnaPolymeraseActivity"
    )


class AcetylcholinesteraseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0003990", "AcetylcholinesteraseActivity"
    )


class AcylCoaOxidaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0003997", "AcylCoaOxidaseActivity"
    )


class LAlanine2OxoglutarateAminotransferaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004021",
        "LAlanine2OxoglutarateAminotransferaseActivity",
    )


class AlkalinePhosphataseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004035", "AlkalinePhosphataseActivity"
    )


class LAspartate2OxoglutarateAminotransferaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004069",
        "LAspartate2OxoglutarateAminotransferaseActivity",
    )


class CholinesteraseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004104", "CholinesteraseActivity"
    )


class CreatineKinaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004111", "CreatineKinaseActivity"
    )


class GlutamateDehydrogenaseNadPActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004353",
        "GlutamateDehydrogenaseNadPActivity",
    )


class GlutathioneTransferaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004364", "GlutathioneTransferaseActivity"
    )


class IsocitrateDehydrogenaseNadPActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004448",
        "IsocitrateDehydrogenaseNadPActivity",
    )


class LactateDehydrogenaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0004457", "LactateDehydrogenaseActivity"
    )


class RnaNucleaseActivity(CatalyticActivity):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0004540", "RnaNucleaseActivity")


class _5NucleotidaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0008253", "_5NucleotidaseActivity"
    )


class GalactosidaseActivity(CatalyticActivity):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0015925", "GalactosidaseActivity")


class AmylaseActivity(CatalyticActivity):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0016160", "AmylaseActivity")


class BetaNAcetylglucosaminidaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0016231",
        "BetaNAcetylglucosaminidaseActivity",
    )


class HydrolaseActivityActingOnEsterBonds(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0016788",
        "HydrolaseActivityActingOnEsterBonds",
    )


class DnaPolymeraseActivity(CatalyticActivity):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0034061", "DnaPolymeraseActivity")


class DGlutamyltransferaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0047823", "DGlutamyltransferaseActivity"
    )


class CarboxylicEsterHydrolaseActivity(CatalyticActivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0052689", "CarboxylicEsterHydrolaseActivity"
    )


class BCellEpitopeSpecificAntibodyDependentCellularCytotoxicity(
    AntibodyDependentCellularCytotoxicity
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001717",
        "BCellEpitopeSpecificAntibodyDependentCellularCytotoxicity",
    )


class CytokineProductionInvolvedInImmuneResponse(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0002367",
        "CytokineProductionInvolvedInImmuneResponse",
    )


class GO_0002390(CytokineProduction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0002390", "GO_0002390")


class CytokineProductionInvolvedInInflammatoryResponse(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0002534",
        "CytokineProductionInvolvedInInflammatoryResponse",
    )


class VascularEndothelialGrowthFactorProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0010573",
        "VascularEndothelialGrowthFactorProduction",
    )


class ConnectiveTissueGrowthFactorProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032601",
        "ConnectiveTissueGrowthFactorProduction",
    )


class ChemokineProduction(CytokineProduction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0032602", "ChemokineProduction")


class GranulocyteMacrophageColonyStimulatingFactorProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032604",
        "GranulocyteMacrophageColonyStimulatingFactorProduction",
    )


class HepatocyteGrowthFactorProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032605", "HepatocyteGrowthFactorProduction"
    )


class TypeIInterferonProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032606", "TypeIInterferonProduction"
    )


class InterferonBetaProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032608", "InterferonBetaProduction"
    )


class TypeIiInterferonProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032609", "TypeIiInterferonProduction"
    )


class Interleukin1Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032612", "Interleukin1Production"
    )


class Interleukin10Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032613", "Interleukin10Production"
    )


class Interleukin11Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032614", "Interleukin11Production"
    )


class Interleukin12Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032615", "Interleukin12Production"
    )


class Interleukin13Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032616", "Interleukin13Production"
    )


class ObsoleteInterleukin14Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032617", "ObsoleteInterleukin14Production"
    )


class Interleukin15Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032618", "Interleukin15Production"
    )


class Interleukin16Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032619", "Interleukin16Production"
    )


class Interleukin17Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032620", "Interleukin17Production"
    )


class Interleukin18Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032621", "Interleukin18Production"
    )


class Interleukin19Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032622", "Interleukin19Production"
    )


class Interleukin2Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032623", "Interleukin2Production"
    )


class Interleukin20Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032624", "Interleukin20Production"
    )


class Interleukin21Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032625", "Interleukin21Production"
    )


class Interleukin22Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032626", "Interleukin22Production"
    )


class Interleukin23Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032627", "Interleukin23Production"
    )


class Interleukin24Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032628", "Interleukin24Production"
    )


class Interleukin25Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032629", "Interleukin25Production"
    )


class Interleukin26Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032630", "Interleukin26Production"
    )


class Interleukin27Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032631", "Interleukin27Production"
    )


class Interleukin3Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032632", "Interleukin3Production"
    )


class Interleukin4Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032633", "Interleukin4Production"
    )


class Interleukin5Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032634", "Interleukin5Production"
    )


class Interleukin6Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032635", "Interleukin6Production"
    )


class Interleukin7Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032636", "Interleukin7Production"
    )


class Interleukin8Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032637", "Interleukin8Production"
    )


class Interleukin9Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032638", "Interleukin9Production"
    )


class TrailProduction(CytokineProduction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0032639", "TrailProduction")


class TransformingGrowthFactorBeta1Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032905",
        "TransformingGrowthFactorBeta1Production",
    )


class TransformingGrowthFactorBeta2Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032906",
        "TransformingGrowthFactorBeta2Production",
    )


class TransformingGrowthFactorBeta3Production(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032907",
        "TransformingGrowthFactorBeta3Production",
    )


class TypeIiiInterferonProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0034343", "TypeIiiInterferonProduction"
    )


class MacrophageMigrationInhibitoryFactorProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0044807",
        "MacrophageMigrationInhibitoryFactorProduction",
    )


class OncostatinMProduction(CytokineProduction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0044808", "OncostatinMProduction")


class TransformingGrowthFactorBetaProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071604",
        "TransformingGrowthFactorBetaProduction",
    )


class GranulocyteColonyStimulatingFactorProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071611",
        "GranulocyteColonyStimulatingFactorProduction",
    )


class TumorNecrosisFactorSuperfamilyCytokineProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071706",
        "TumorNecrosisFactorSuperfamilyCytokineProduction",
    )


class AmphiregulinProduction(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0140730", "AmphiregulinProduction"
    )


class Xcl1Production(CytokineProduction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0140779", "Xcl1Production")


class EpitopeSpecificCytokineProductionByTCells(CytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001193",
        "EpitopeSpecificCytokineProductionByTCells",
    )


class TCellMediatedCytotoxicity(CellKilling):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0001913", "TCellMediatedCytotoxicity"
    )


class CytotoxicTCellDegranulation(CellKilling):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0043316", "CytotoxicTCellDegranulation"
    )


class ComplementDependentCytotoxicity(CellKilling):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097278", "ComplementDependentCytotoxicity"
    )


class BCellToleranceInduction(ToleranceInduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0002514", "BCellToleranceInduction"
    )


class TCellToleranceInduction(ToleranceInduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0002517", "TCellToleranceInduction"
    )


class EpitopeSpecificToleranceInductionByTCells(ToleranceInduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001201",
        "EpitopeSpecificToleranceInductionByTCells",
    )


class TypeIvHypersensitivity(Hypersensitivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0001806", "TypeIvHypersensitivity"
    )


class BCellEpitopeSpecificHypersensitivity(Hypersensitivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001722",
        "BCellEpitopeSpecificHypersensitivity",
    )


class Opsonization(Phagocytosis):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0008228", "Opsonization")


class TCellProliferation(CellPopulationProliferation):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0042098", "TCellProliferation")


class RnaTemplatedTranscription(CellularProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0001172", "RnaTemplatedTranscription"
    )


class MonoatomicIonChannelActivity(CellularProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0005216", "MonoatomicIonChannelActivity"
    )


class ChromatinRemodeling(CellularProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0006338", "ChromatinRemodeling")


class ImmuneComplexFormation(ImmunoglobulinMediatedImmuneResponse):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097281", "ImmuneComplexFormation"
    )


class ImmunoglobulinMediatedNeutralization(ImmunoglobulinMediatedImmuneResponse):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097282",
        "ImmunoglobulinMediatedNeutralization",
    )


class Spermatogenesis(ReproductiveProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0007283", "Spermatogenesis")


class EpitopeSpecificGranzymeAProductionByTCells(GranzymeAProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001678",
        "EpitopeSpecificGranzymeAProductionByTCells",
    )


class GranzymeAReleaseDuringTCellDegranulation(GranzymeAProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003318",
        "GranzymeAReleaseDuringTCellDegranulation",
    )


class EpitopeSpecificPerforinProductionByTCells(PerforinProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001502",
        "EpitopeSpecificPerforinProductionByTCells",
    )


class PerforinReleaseDuringTCellDegranulation(PerforinProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003317",
        "PerforinReleaseDuringTCellDegranulation",
    )


class EpitopeSpecificGranulysinProductionByTCells(GranulysinProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001677",
        "EpitopeSpecificGranulysinProductionByTCells",
    )


class GranulysinReleaseDuringTCellDegranulation(GranulysinProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003320",
        "GranulysinReleaseDuringTCellDegranulation",
    )


class EpitopeSpecificTCellActivation(TCellActivation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001208", "EpitopeSpecificTCellActivation"
    )


class CellDifferentiation(CellularDevelopmentalProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0030154", "CellDifferentiation")


class ImmuneResponse(ResponseToStimulus):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0006955", "ImmuneResponse")


class DnaDamageResponse(ResponseToStimulus):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0006974", "DnaDamageResponse")


class StartleResponse(ResponseToStimulus, NeuromuscularProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0001964", "StartleResponse")


class EpitopeSpecificGranzymeBProductionByTCells(GranzymeBProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001371",
        "EpitopeSpecificGranzymeBProductionByTCells",
    )


class GranzymeBReleaseDuringTCellDegranulation(GranzymeBProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003319",
        "GranzymeBReleaseDuringTCellDegranulation",
    )


class GO_0001047(Binding):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0001047", "GO_0001047")


class ProteinDomainSpecificBinding(Binding):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0019904", "ProteinDomainSpecificBinding"
    )


class SequenceSpecificDnaBinding(Binding):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0043565", "SequenceSpecificDnaBinding"
    )


class MhcProteinComplexBindingToLigand(Binding):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001503", "MhcProteinComplexBindingToLigand"
    )


class ImmunoglobulinBindingToEpitope(Binding, EpitopeBindingByAdaptiveImmuneReceptor):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001702", "ImmunoglobulinBindingToEpitope"
    )


class MhcEpitopeComplexBindingToTcr(Binding, EpitopeBindingByAdaptiveImmuneReceptor):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110057", "MhcEpitopeComplexBindingToTcr"
    )


class ImmunizationInVivo(Immunization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110015", "ImmunizationInVivo")


class LivingWithInfectedHouseholdContact(EnvironmentalProximityToInfectiousAgent):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110017",
        "LivingWithInfectedHouseholdContact",
    )


class LivingInEndemicArea(EnvironmentalProximityToInfectiousAgent):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110018", "LivingInEndemicArea")


class PathogenReleaseInLaboratoryAccident(EnvironmentalProximityToInfectiousAgent):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110019",
        "PathogenReleaseInLaboratoryAccident",
    )


class ContactToPathogenCarryingBiologicalVector(
    EnvironmentalProximityToInfectiousAgent
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110114",
        "ContactToPathogenCarryingBiologicalVector",
    )


class AllergicReaction(PathologicProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110011", "AllergicReaction")


class InfectionProcess(PathologicProcess):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110021", "InfectionProcess")


class OccurrenceOfInfectiousDisease(DiseaseCourse):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110008", "OccurrenceOfInfectiousDisease"
    )


class OccurrenceOfAllergy(DiseaseCourse):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110012", "OccurrenceOfAllergy")


class DataEncoding(Documenting):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000227", "DataEncoding")


class DigitalCuration(Documenting):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302914", "DigitalCuration")


class HypothesisDrivenInvestigation(Investigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000355", "HypothesisDrivenInvestigation"
    )


class HypothesisGeneratingInvestigation(Investigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000356",
        "HypothesisGeneratingInvestigation",
    )


class SurveillanceProcess(Investigation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002897", "SurveillanceProcess")


class CaseControlInvestigation(Investigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003692", "CaseControlInvestigation"
    )


class ObservationalInvestigation(Investigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003693", "ObservationalInvestigation"
    )


class LongitudinalInvestigation(Investigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003694", "LongitudinalInvestigation"
    )


class AnimalInvestigation(Investigation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003696", "AnimalInvestigation")


class ClinicalInvestigation(Investigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003697", "ClinicalInvestigation"
    )


class BernoulliTrial(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000117", "BernoulliTrial")


class ImagingAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000185", "ImagingAssay")


class RadioactivityDetection(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000201", "RadioactivityDetection"
    )


class ProteinProteinInteractionDetectionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000288",
        "ProteinProteinInteractionDetectionAssay",
    )


class MetaboliteProfilingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000366", "MetaboliteProfilingAssay"
    )


class TranscriptionProfilingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000424", "TranscriptionProfilingAssay"
    )


class DnaSequenceFeatureDetectionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000433", "DnaSequenceFeatureDetectionAssay"
    )


class DnaSequenceVariationDetectionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000438",
        "DnaSequenceVariationDetectionAssay",
    )


class AnalyteAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000443", "AnalyteAssay")


class MassMeasurementAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000445", "MassMeasurementAssay")


class MassSpectrometryAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000470", "MassSpectrometryAssay"
    )


class CopyNumberVariationProfilingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000537",
        "CopyNumberVariationProfilingAssay",
    )


class ProteinExpressionProfilingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000615", "ProteinExpressionProfilingAssay"
    )


class NmrSpectroscopyAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000623", "NmrSpectroscopyAssay")


class HematologyAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000630", "HematologyAssay")


class SurvivalAssessmentAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000699", "SurvivalAssessmentAssay"
    )


class ImmuneResponseAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000743", "ImmuneResponseAssay")


class ProthrombinTimeAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000802", "ProthrombinTimeAssay")


class SpectrolyseHeparinAntifactorXaAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000808",
        "SpectrolyseHeparinAntifactorXaAssay",
    )


class ThrombinTimeAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000823", "ThrombinTimeAssay")


class SingleNucleotideResolutionNucleicAcidStructureMappingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000870",
        "SingleNucleotideResolutionNucleicAcidStructureMappingAssay",
    )


class ViralHemagglutinationInhibitionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000875",
        "ViralHemagglutinationInhibitionAssay",
    )


class RadioImmunoAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000910", "RadioImmunoAssay")


class PromoterActivityDetectionByReporterGeneAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000913",
        "PromoterActivityDetectionByReporterGeneAssay",
    )


class HandednessAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000944", "HandednessAssay")


class InLiveCellAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000964", "InLiveCellAssay")


class InLiveOrganismAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000966", "InLiveOrganismAssay")


class InContainerAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000978", "InContainerAssay")


class GeneDosageAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001022", "GeneDosageAssay")


class BindingAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001146", "BindingAssay")


class AgeDeterminationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001158", "AgeDeterminationAssay"
    )


class EfficacyOfEpitopeInterventionExperiment(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001178",
        "EfficacyOfEpitopeInterventionExperiment",
    )


class InfectiousAgentDetectionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001187", "InfectiousAgentDetectionAssay"
    )


class FluorescenceDetectionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001501", "FluorescenceDetectionAssay"
    )


class RnaProtectionAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001670", "RnaProtectionAssay")


class MethylationSpecificPolymeraseChainReactionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001684",
        "MethylationSpecificPolymeraseChainReactionAssay",
    )


class InSituHybridizationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001686", "InSituHybridizationAssay"
    )


class CytochalasinInducedInhibitionOfActinPolymerizationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001689",
        "CytochalasinInducedInhibitionOfActinPolymerizationAssay",
    )


class ChipAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001954", "ChipAssay")


class CytometryAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001977", "CytometryAssay")


class InVivoInterventionExperiment(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001980", "InVivoInterventionExperiment"
    )


class EpigeneticModificationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002020", "EpigeneticModificationAssay"
    )


class ArrayBasedNucleicAcidStructureMappingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002036",
        "ArrayBasedNucleicAcidStructureMappingAssay",
    )


class ReporterGeneAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002082", "ReporterGeneAssay")


class CarboxyfluoresceinSuccinimidylEsterStainingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002106",
        "CarboxyfluoresceinSuccinimidylEsterStainingAssay",
    )


class PulseStableIsotopeLabelingByAminoAcidsInCellCulture(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002132",
        "PulseStableIsotopeLabelingByAminoAcidsInCellCulture",
    )


class TemperatureMeasurementAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002140", "TemperatureMeasurementAssay"
    )


class VolumeMeasurementAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002141", "VolumeMeasurementAssay"
    )


class FootprintingAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002162", "FootprintingAssay")


class ProteinLocalizationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002165", "ProteinLocalizationAssay"
    )


class ElectrophysiologyAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002176", "ElectrophysiologyAssay"
    )


class RnaInteractomeCapture(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002436", "RnaInteractomeCapture"
    )


class NuclearLigationAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002438", "NuclearLigationAssay")


class PhysicalExaminationOfAnOrganism(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002441", "PhysicalExaminationOfAnOrganism"
    )


class PolymeraseChainReactionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002692", "PolymeraseChainReactionAssay"
    )


class RestrictionFragmentLengthPolymorphismAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002693",
        "RestrictionFragmentLengthPolymorphismAssay",
    )


class DnaFingerprintingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002694", "DnaFingerprintingAssay"
    )


class InsecticideResistanceAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002695", "InsecticideResistanceAssay"
    )


class BloodMealAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002732", "BloodMealAssay")


class SingleValueBindingOfAntibodyWithReporterToAntigenAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002773",
        "SingleValueBindingOfAntibodyWithReporterToAntigenAssay",
    )


class ProteinStateAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002953", "ProteinStateAssay")


class KinaseInhibitorAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002962", "KinaseInhibitorAssay")


class FerritinAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003009", "FerritinAssay")


class FibrinogenAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003010", "FibrinogenAssay")


class BloodAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003040", "BloodAssay")


class UrineAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003043", "UrineAssay")


class CerebrospinalFluidAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003232", "CerebrospinalFluidAssay"
    )


class EndotrachealAspirateAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003233", "EndotrachealAspirateAssay"
    )


class InducedSputumAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003234", "InducedSputumAssay")


class LungAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003235", "LungAssay")


class MilkAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003236", "MilkAssay")


class FecesAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003237", "FecesAssay")


class SalivaAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003239", "SalivaAssay")


class MosquitoMembraneFeedingAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003290", "MosquitoMembraneFeedingAssay"
    )


class DnaAdenineMethyltransferaseIdentificationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003298",
        "DnaAdenineMethyltransferaseIdentificationAssay",
    )


class DetectionTechnique(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003368", "DetectionTechnique")


class EnzymaticActivityLevelAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003422", "EnzymaticActivityLevelAssay"
    )


class OrganismDetectionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003498", "OrganismDetectionAssay"
    )


class CellCultureAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003587", "CellCultureAssay")


class QuartzCrystalMicrobalanceAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003601", "QuartzCrystalMicrobalanceAssay"
    )


class ChromatinAccessibilityAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003686", "ChromatinAccessibilityAssay"
    )


class VitalSignAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003715", "VitalSignAssay")


class SurveyAdministrationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003725", "SurveyAdministrationAssay"
    )


class TumorGrading(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600002", "TumorGrading")


class AssayDetectingAMolecularLabel(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600017", "AssayDetectingAMolecularLabel"
    )


class HistologicalAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600020", "HistologicalAssay")


class SubstanceDetectionAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600025", "SubstanceDetectionAssay"
    )


class LongitudinalMassMeasurementAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600026", "LongitudinalMassMeasurementAssay"
    )


class _3DStructureDeterminationAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600045", "_3DStructureDeterminationAssay"
    )


class SequencingAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600047", "SequencingAssay")


class ImmuneEpitopeAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110128", "ImmuneEpitopeAssay")


class AssayDetectingIfnGammaProduction(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110207", "AssayDetectingIfnGammaProduction"
    )


class LactateDehydrogenaseComplexAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100028", "LactateDehydrogenaseComplexAssay"
    )


class OsmolalityAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100039", "OsmolalityAssay")


class CytosolicCreatineKinaseComplexMbTypeAssay(Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100041",
        "CytosolicCreatineKinaseComplexMbTypeAssay",
    )


class RacLacticAcidAssay(Assay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100042", "RacLacticAcidAssay")


class SamplePreparationForAssay(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000073", "SamplePreparationForAssay"
    )


class Transplantation(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000105", "Transplantation")


class CellCoCulturing(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000153", "CellCoCulturing")


class EnzymaticCleavage(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000231", "EnzymaticCleavage")


class ArtificiallyInducedNucleicAcidHybridization(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000253",
        "ArtificiallyInducedNucleicAcidHybridization",
    )


class IonizeProcess(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000373", "IonizeProcess")


class CellCycleSynchronization(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000413", "CellCycleSynchronization"
    )


class Manufacturing(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000457", "Manufacturing")


class MaterialCombination(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000652", "MaterialCombination")


class LibraryPreparation(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000711", "LibraryPreparation")


class VaccineProduction(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000719", "VaccineProduction")


class CrossLinking(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000800", "CrossLinking")


class Denaturing(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000803", "Denaturing")


class InducedHemagglutination(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000906", "InducedHemagglutination"
    )


class ChemicalCleavage(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000943", "ChemicalCleavage")


class CellCultureExpansion(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001147", "CellCultureExpansion")


class PhageDisplayLibraryPanning(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001480", "PhageDisplayLibraryPanning"
    )


class Dissection(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001504", "Dissection")


class MultiplexedNucleotideLibrarySequencing(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001959",
        "MultiplexedNucleotideLibrarySequencing",
    )


class SpecimenFamilyCreation(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002095", "SpecimenFamilyCreation"
    )


class PassageProcess(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002747", "PassageProcess")


class Staining(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302887", "Staining")


class Washing(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302888", "Washing")


class PlannedIrradiation(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302889", "PlannedIrradiation")


class Polymerization(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302890", "Polymerization")


class EnzymaticLigation(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302892", "EnzymaticLigation")


class Immobilization(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302902", "Immobilization")


class NucleicAcidHybridization(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0302903", "NucleicAcidHybridization"
    )


class Elution(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302905", "Elution")


class Killing(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600006", "Killing")


class MaterialComponentSeparation(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600014", "MaterialComponentSeparation"
    )


class CellFixation(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600021", "CellFixation")


class ArtificiallyInducedCellMembraneLysis(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600027",
        "ArtificiallyInducedCellMembraneLysis",
    )


class ArtificiallyInducedReverseTranscription(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600028",
        "ArtificiallyInducedReverseTranscription",
    )


class ExperimentalDiseaseInduction(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600030", "ExperimentalDiseaseInduction"
    )


class ArtificiallyInducedDnaRepair(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600032", "ArtificiallyInducedDnaRepair"
    )


class CellPermeabilization(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600033", "CellPermeabilization")


class EstablishingCellCulture(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600036", "EstablishingCellCulture"
    )


class AdditionOfMolecularLabel(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600038", "AdditionOfMolecularLabel"
    )


class ArtificiallyInducedMethylation(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600039", "ArtificiallyInducedMethylation"
    )


class Synthesis(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600040", "Synthesis")


class GeneticTransformation(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600043", "GeneticTransformation"
    )


class SelectionBySurvival(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600054", "SelectionBySurvival")


class EnzymaticAmplification(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600058", "EnzymaticAmplification"
    )


class RecombinantVectorCloning(MaterialProcessing):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600064", "RecombinantVectorCloning"
    )


class ImmunizationInVitro(MaterialProcessing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110020", "ImmunizationInVitro")


class InductiveReasoning(DrawingAConclusionBasedOnData):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000343", "InductiveReasoning")


class AssigningGenePropertyBasedOnPhenotypicAssessment(DrawingAConclusionBasedOnData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001575",
        "AssigningGenePropertyBasedOnPhenotypicAssessment",
    )


class OrganismDiagnosticProcess(DrawingAConclusionBasedOnData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003366", "OrganismDiagnosticProcess"
    )


class ReconstitutionAssay(Assay, StudyDesignExecution):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002621", "ReconstitutionAssay")


class HistologicalSamplePreparation(MaterialProcessing, SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000341", "HistologicalSamplePreparation"
    )


class MaterialSamplingProcess(SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000744", "MaterialSamplingProcess"
    )


class SpecimenSetCollectionProcess(SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002078", "SpecimenSetCollectionProcess"
    )


class CollectingSpecimenWithSwab(SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002600", "CollectingSpecimenWithSwab"
    )


class AspirationSpecimenCollection(SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002785", "AspirationSpecimenCollection"
    )


class ArthropodSpecimenCollectionProcess(SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002913",
        "ArthropodSpecimenCollectionProcess",
    )


class CollectingSpecimenFromOrganism(SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600005", "CollectingSpecimenFromOrganism"
    )


class EnvironmentalMaterialCollectionProcess(SpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600012",
        "EnvironmentalMaterialCollectionProcess",
    )


class RodentCare(LaboratoryAnimalCare):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000728", "RodentCare")


class SingleBlindStudyExecution(TreatmentPortionOfStudyExecution):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000822", "SingleBlindStudyExecution"
    )


class Storage(MaterialMaintenance):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302893", "Storage")


class MaintainingCellCulture(MaterialMaintenance):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600024", "MaintainingCellCulture"
    )


class ArrayImageCreation(ImageCreation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001031", "ArrayImageCreation")


class SupportService(Service):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001527", "SupportService")


class MaterialService(Service):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001528", "MaterialService")


class DataService(Service):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001530", "DataService")


class TrainingService(Service):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001538", "TrainingService")


class AccessService(Service):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001551", "AccessService")


class ComparativePhenotypicAssessment(
    DrawingAConclusionBasedOnData, DrawingAConclusion
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001546", "ComparativePhenotypicAssessment"
    )


class HumanSubjectEnrollment(Selection):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600004", "HumanSubjectEnrollment"
    )


class Acquisition(Selection):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600008", "Acquisition")


class FlashFreezing(Freezing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001952", "FlashFreezing")


class SupervisedMachineLearning(MachineLearning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002588", "SupervisedMachineLearning"
    )


class UnsupervisedMachineLearning(MachineLearning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002589", "UnsupervisedMachineLearning"
    )


class OvernightFasting(Fasting):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003654", "OvernightFasting")


class DifferentialExpressionAnalysisDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000650",
        "DifferentialExpressionAnalysisDataTransformation",
    )


class ClassPredictionDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000663",
        "ClassPredictionDataTransformation",
    )


class BackgroundCorrectionDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000666",
        "BackgroundCorrectionDataTransformation",
    )


class ErrorCorrectionDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000668",
        "ErrorCorrectionDataTransformation",
    )


class StatisticalHypothesisTest(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000673", "StatisticalHypothesisTest"
    )


class DecisionTreeBuildingDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000707",
        "DecisionTreeBuildingDataTransformation",
    )


class PeakMatching(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000726", "PeakMatching")


class LikelihoodRatioTest(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000861", "LikelihoodRatioTest")


class FeatureExtraction(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001028", "FeatureExtraction")


class SequenceAssemblyProcess(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001872", "SequenceAssemblyProcess"
    )


class RnaIntegrityNumberCalculation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002136", "RnaIntegrityNumberCalculation"
    )


class FileMerge(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002566", "FileMerge")


class SequenceTrimming(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002585", "SequenceTrimming")


class ImageDataSetAnalysis(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003355", "ImageDataSetAnalysis")


class SplitScaleTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200014", "SplitScaleTransformation"
    )


class ProbabilisticAlgorithm(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200052", "ProbabilisticAlgorithm"
    )


class DataImputation(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200061", "DataImputation")


class CurveFittingDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200072", "CurveFittingDataTransformation"
    )


class NetworkAnalysis(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200080", "NetworkAnalysis")


class LongitudinalDataAnalysis(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200082", "LongitudinalDataAnalysis"
    )


class MassSpectrometryAnalysis(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200085", "MassSpectrometryAnalysis"
    )


class SpreadCalculationDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200086",
        "SpreadCalculationDataTransformation",
    )


class PolynomialTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200093", "PolynomialTransformation"
    )


class NonNegativeMatrixFactorization(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200097", "NonNegativeMatrixFactorization"
    )


class RegressionAnalysisMethod(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200102", "RegressionAnalysisMethod"
    )


class DiscriminantAnalysis(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200106", "DiscriminantAnalysis")


class DataCombination(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200125", "DataCombination")


class MathematicalFeature(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200140", "MathematicalFeature")


class MaTransformation(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200150", "MaTransformation")


class DataPartitioning(DataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200156", "DataPartitioning")


class NormalizationDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200169", "NormalizationDataTransformation"
    )


class AveragingDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200170", "AveragingDataTransformation"
    )


class PartitioningDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200171", "PartitioningDataTransformation"
    )


class ClassDiscoveryDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200175", "ClassDiscoveryDataTransformation"
    )


class CenterCalculationDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200181",
        "CenterCalculationDataTransformation",
    )


class DescriptiveStatisticalCalculationDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200184",
        "DescriptiveStatisticalCalculationDataTransformation",
    )


class ScalingDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200185", "ScalingDataTransformation"
    )


class SequenceAnalysisDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200187",
        "SequenceAnalysisDataTransformation",
    )


class SurvivalAnalysisDataTransformation(DataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200194",
        "SurvivalAnalysisDataTransformation",
    )


class ClusteredDataVisualization(DataVisualization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200190", "ClusteredDataVisualization"
    )


class GeneListVisualization(DataVisualization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200191", "GeneListVisualization"
    )


class ClassifiedDataVisualization(DataVisualization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200192", "ClassifiedDataVisualization"
    )


class BackgroundCorrectedDataVisualization(DataVisualization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200193",
        "BackgroundCorrectedDataVisualization",
    )


class Waiting(ExposureOfMaterialToEnvironment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000045", "Waiting")


class Acclimatization(ExposureOfMaterialToEnvironment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600011", "Acclimatization")


class GroupRandomization(GroupAssignment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302900", "GroupRandomization")


class Homocysteine(AminoAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17230", "Homocysteine")


class _335Triiodothyronine(AminoAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_28774", "_335Triiodothyronine")


class Thyroxine(AminoAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_30660", "Thyroxine")


class Peptide(Macromolecule):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16670", "Peptide")


class GlobulinType(Macromolecule):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_166899", "GlobulinType")


class Methemoglobin(Macromolecule):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_17423", "Methemoglobin")


class NucleicAcid(Macromolecule):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33696", "NucleicAcid")


class Hemoglobin(Macromolecule):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_35143", "Hemoglobin")


class Lipoprotein(Macromolecule):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_6495", "Lipoprotein")


class ThyroidStimulatingHormone(Macromolecule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_81567", "ThyroidStimulatingHormone"
    )


class DenaturedPolymer(Macromolecule, ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302835", "DenaturedPolymer")


class MethylatedPolymer(Macromolecule, ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302847", "MethylatedPolymer")


class _3HydroxybutyricAcid(FattyAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_20067", "_3HydroxybutyricAcid")


class ValproicAcid(FattyAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_39867", "ValproicAcid")


class CalciumCation(CalciumIon):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_39123", "CalciumCation")


class MesothelialCell(EpithelialCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000077", "MesothelialCell")


class Hepatocyte(EpithelialCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000182", "Hepatocyte")


class NucleateErythrocyte(Erythrocyte):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000562", "NucleateErythrocyte")


class Eosinophil(Leukocyte):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000771", "Eosinophil")


class Neutrophil(Leukocyte):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000775", "Neutrophil")


class Monocyte(Leukocyte, MononuclearCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000576", "Monocyte")


class Lymphocyte(MononuclearCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000542", "Lymphocyte")


class PeripheralBloodMononuclearCell(MononuclearCell):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CL_2000001", "PeripheralBloodMononuclearCell"
    )


class Neuron(NeuralCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000540", "Neuron")


class Mitochondrion(MembraneBoundedOrganelle):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0005739", "Mitochondrion")


class IggImmunoglobulinComplex(ImmunoglobulinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071735", "IggImmunoglobulinComplex"
    )


class IgeImmunoglobulinComplex(ImmunoglobulinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071742", "IgeImmunoglobulinComplex"
    )


class IgaImmunoglobulinComplex(ImmunoglobulinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071745", "IgaImmunoglobulinComplex"
    )


class IgmImmunoglobulinComplex(ImmunoglobulinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071753", "IgmImmunoglobulinComplex"
    )


class MhcClassIProteinComplex(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001355", "MhcClassIProteinComplex"
    )


class MhcClassIiProteinComplex(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001356", "MhcClassIiProteinComplex"
    )


class MouseMhcProteinComplexWithH2PHaplotype(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001498",
        "MouseMhcProteinComplexWithH2PHaplotype",
    )


class HlaProteinComplexWithA2Serotype(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001530", "HlaProteinComplexWithA2Serotype"
    )


class HlaProteinComplexWithA24Serotype(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001533", "HlaProteinComplexWithA24Serotype"
    )


class HlaProteinComplexWithA28Serotype(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001537", "HlaProteinComplexWithA28Serotype"
    )


class HlaProteinComplexWithA29Serotype(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001538", "HlaProteinComplexWithA29Serotype"
    )


class HlaProteinComplexWithB27Serotype(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001557", "HlaProteinComplexWithB27Serotype"
    )


class HlaProteinComplexWithDq3Serotype(MhcProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001622", "HlaProteinComplexWithDq3Serotype"
    )


class ImmunoglobulinComplexCirculating(ImmunoglobulinComplex, AdaptiveImmuneReceptor):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0042571", "ImmunoglobulinComplexCirculating"
    )


class BCellReceptorComplex(AdaptiveImmuneReceptor):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0019815", "BCellReceptorComplex")


class TCellReceptorComplex(AdaptiveImmuneReceptor):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0042101", "TCellReceptorComplex")


class CulturedCell(ExperimentallyModifiedCellInVitro):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000010", "CulturedCell")


class DulbeccoSModifiedEagleMedium(CultureMedium):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000918", "DulbeccoSModifiedEagleMedium"
    )


class EnrichmentCultureMedium(CultureMedium):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002673", "EnrichmentCultureMedium"
    )


class ProteinExtract(Extract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000894", "ProteinExtract")


class ClonalCdnaLibrary(RecombinantVector):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000164", "ClonalCdnaLibrary")


class PhageDisplayLibrary(RecombinantVector):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1000029", "PhageDisplayLibrary")


class FilledCapsule(Pill):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000821", "FilledCapsule")


class PumpValveSwitch(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000041", "PumpValveSwitch")


class IonSource(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000361", "IonSource")


class BlotModule(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000394", "BlotModule")


class Syringe(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000422", "Syringe")


class Needle(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000436", "Needle")


class NmrSampleHolder(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000484", "NmrSampleHolder")


class NmrTubeWashingSystem(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000498", "NmrTubeWashingSystem")


class NmrConsole(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000499", "NmrConsole")


class NmrMagnet(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000517", "NmrMagnet")


class MagicAngleSpinningRotor(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000523", "MagicAngleSpinningRotor"
    )


class BrukerSamplerailSystem(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000544", "BrukerSamplerailSystem"
    )


class Autosampler(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000555", "Autosampler")


class MeasurementDevice(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000832", "MeasurementDevice")


class MaterialSeparationDevice(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000932", "MaterialSeparationDevice"
    )


class Micromanipulator(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000935", "Micromanipulator")


class ElectrodePuller(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000955", "ElectrodePuller")


class Container(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000967", "Container")


class LightEmissionDevice(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001032", "LightEmissionDevice")


class PerturbationDevice(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001033", "PerturbationDevice")


class EnvironmentalControlDevice(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001034", "EnvironmentalControlDevice"
    )


class CapillaryBlotter(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001045", "CapillaryBlotter")


class ChipSpottingDevice(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001049", "ChipSpottingDevice")


class PetSynthesizer(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001054", "PetSynthesizer")


class SpotCutter(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001060", "SpotCutter")


class MicrowaveSynthesisSystem(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001061", "MicrowaveSynthesisSystem"
    )


class AutomaticStainingMachine(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001063", "AutomaticStainingMachine"
    )


class AutomaticTissueProcessor(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001064", "AutomaticTissueProcessor"
    )


class PerfusionStation(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001067", "PerfusionStation")


class MicrotomeKnifeMaker(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001073", "MicrotomeKnifeMaker")


class CryofixationDevice(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001074", "CryofixationDevice")


class VitrificationApparatus(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001084", "VitrificationApparatus"
    )


class Lyophilizer(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001087", "Lyophilizer")


class MicrotomeKnifeSharpener(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001093", "MicrotomeKnifeSharpener"
    )


class PlateShaker(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001094", "PlateShaker")


class Rocker(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001103", "Rocker")


class TissueEmbeddingStation(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001107", "TissueEmbeddingStation"
    )


class MicroplateWasher(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001113", "MicroplateWasher")


class VacuumManifold(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001116", "VacuumManifold")


class CellHarvester(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001119", "CellHarvester")


class MicrodissectionInstrument(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001123", "MicrodissectionInstrument"
    )


class MicropipettePuller(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001124", "MicropipettePuller")


class FreezeSubstitutionSystem(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001127", "FreezeSubstitutionSystem"
    )


class XRaySource(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001138", "XRaySource")


class AssayArray(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001865", "AssayArray")


class SurfacePlasmonResonanceSensorChip(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002046",
        "SurfacePlasmonResonanceSensorChip",
    )


class MicrotomeBlade(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002195", "MicrotomeBlade")


class Pipette(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002488", "Pipette")


class DigitalAcquisitionCard(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002586", "DigitalAcquisitionCard"
    )


class PersonalProtectiveDevice(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002786", "PersonalProtectiveDevice"
    )


class Apron(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002797", "Apron")


class TransparentDropletBarrier(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002805", "TransparentDropletBarrier"
    )


class SpecimenCollectionDevice(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002814", "SpecimenCollectionDevice"
    )


class CottonSwab(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002821", "CottonSwab")


class Catheter(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002830", "Catheter")


class ArthropodTrap(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002920", "ArthropodTrap")


class BgCounter(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002924", "BgCounter")


class DipperForArthropodImmatures(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002927", "DipperForArthropodImmatures"
    )


class DeviceForCollectionOfRestingAdultArthropods(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003005",
        "DeviceForCollectionOfRestingAdultArthropods",
    )


class WellNetForArthropodImmatures(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003006", "WellNetForArthropodImmatures"
    )


class BgLureScentDispenser(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003048", "BgLureScentDispenser")


class HandHeldSweepNet(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003049", "HandHeldSweepNet")


class MosquitoMembraneFeedingDevice(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003289", "MosquitoMembraneFeedingDevice"
    )


class AssayKit(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003369", "AssayKit")


class CowBaitedArthropodTrap(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003481", "CowBaitedArthropodTrap"
    )


class MortarAndPestleDevice(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003707", "MortarAndPestleDevice"
    )


class AnalogToDigitalConverter(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400007", "AnalogToDigitalConverter"
    )


class ChargePlate(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400019", "ChargePlate")


class OpticalSubsystem(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400080", "OpticalSubsystem")


class PlateLoader(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400086", "PlateLoader")


class VoltageAmplifier(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400101", "VoltageAmplifier")


class Arrayer(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400105", "Arrayer")


class Computer(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400107", "Computer")


class LiquidHandler(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400112", "LiquidHandler")


class PowerSupply(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400142", "PowerSupply")


class DigitalToAnalogConverter(Device):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400158", "DigitalToAnalogConverter"
    )


class MicroscopeSlide(Device):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400170", "MicroscopeSlide")


class GeneticallyModifiedOrganism(GeneticallyModifiedMaterial, Organism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0302859", "GeneticallyModifiedOrganism"
    )


class PurifiedMhcMoleculePreparation(PurifiedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001485", "PurifiedMhcMoleculePreparation"
    )


class PrimaryCellCulture(CellCulture):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001910", "PrimaryCellCulture")


class CellLineCulture(CellCulture):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001911", "CellLineCulture")


class MolecularLabel(Reagent, MolecularEntity):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002744", "MolecularLabel")


class Phosphorus32Atom(Reagent, Atom):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_37972", "Phosphorus32Atom")


class Phosphorus33Atom(Reagent, Atom):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_37973", "Phosphorus33Atom")


class FluorescentlyLabeledMhcMultimer(MolecularLabeledMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000788", "FluorescentlyLabeledMhcMultimer"
    )


class LabeledOligonucleotide(MolecularLabeledMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000839", "LabeledOligonucleotide"
    )


class PillDeliveryFormForHormonalReplacementTherapy(
    DeliveryFormForHormonalReplacementTherapy
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002407",
        "PillDeliveryFormForHormonalReplacementTherapy",
    )


class PatchDeliveryFormForHormonalReplacementTherapy(
    DeliveryFormForHormonalReplacementTherapy
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002408",
        "PatchDeliveryFormForHormonalReplacementTherapy",
    )


class CreamDeliveryFormForHormonalReplacementTherapy(
    DeliveryFormForHormonalReplacementTherapy
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002409",
        "CreamDeliveryFormForHormonalReplacementTherapy",
    )


class SingleEndLibrary(CdnaLibrary):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002481", "SingleEndLibrary")


class CulturedImmuneCellPopulation(CulturedCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001875", "CulturedImmuneCellPopulation"
    )


class SecondaryCulturedCellPopulation(CulturedCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001905", "SecondaryCulturedCellPopulation"
    )


class PrimaryCulturedCellPopulation(CulturedCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100061", "PrimaryCulturedCellPopulation"
    )


class CulturedClonalCellPopulation(CulturedCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100063", "CulturedClonalCellPopulation"
    )


class CulturedAdherentCellPopulation(CulturedCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110043", "CulturedAdherentCellPopulation"
    )


class MultiWellPlate(ParticleDeliveryVessel):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400076", "MultiWellPlate")


class SequencingFacilityOrganization(MolecularAnalysisFacilityOrganization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001891", "SequencingFacilityOrganization"
    )


class HumanSpecimenSet(SpecimensCollectedInOneEncounter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002080", "HumanSpecimenSet")


class Riboviria(Viruses):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_2559587", "Riboviria")


class Orthoherpesviridae(Viruses):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_3044472", "Orthoherpesviridae"
    )


class TreponemaPallidum(Bacteria):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_160", "TreponemaPallidum")


class OrientiaTsutsugamushi(Bacteria):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_784", "OrientiaTsutsugamushi"
    )


class Opisthokonta(Eukaryota):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_33154", "Opisthokonta")


class ArabidopsisThaliana(Eukaryota):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_3702", "ArabidopsisThaliana"
    )


class DictyosteliumDiscoideum(Eukaryota):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_44689", "DictyosteliumDiscoideum"
    )


class Plasmodium(Eukaryota):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_5820", "Plasmodium")


class LabeledSpecimen(ProcessedSpecimen, MolecularLabeledMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000924", "LabeledSpecimen")


class NucleicAcidExtract(ProcessedSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001010", "NucleicAcidExtract")


class PoolOfSpecimens(ProcessedSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302716", "PoolOfSpecimens")


class FixedTissueSpecimen(ProcessedSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OMIABIS_0000050", "FixedTissueSpecimen"
    )


class WholeMountTissue(WholeOrganismPreparation, ProcessedSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1000049", "WholeMountTissue")


class FrozenSpecimen(SpecimenWithKnownStorageState):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000922", "FrozenSpecimen")


class ParaffinSpecimen(SpecimenWithKnownStorageState):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000950", "ParaffinSpecimen")


class LyophilizedSpecimen(SpecimenWithKnownStorageState):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000965", "LyophilizedSpecimen")


class FreshSpecimen(SpecimenWithKnownStorageState):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000971", "FreshSpecimen")


class AgarStabSpecimen(SpecimenWithKnownStorageState):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000981", "AgarStabSpecimen")


class LavageFluidSpecimen(ProcessedSpecimen, SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003666", "LavageFluidSpecimen")


class SampleFromOrganism(MaterialSample, SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000671", "SampleFromOrganism")


class CloacalSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000909", "CloacalSpecimen")


class CellSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001468", "CellSpecimen")


class SpecimenWithPreOrPostMortemStatus(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001506",
        "SpecimenWithPreOrPostMortemStatus",
    )


class FecesSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002503", "FecesSpecimen")


class BoneMarrowSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002512", "BoneMarrowSpecimen")


class PlacentaSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002513", "PlacentaSpecimen")


class BrainSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002516", "BrainSpecimen")


class HairSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002517", "HairSpecimen")


class ProstateGlandSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002518", "ProstateGlandSpecimen"
    )


class SkeletalMuscleTissueSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002519", "SkeletalMuscleTissueSpecimen"
    )


class HeartSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002520", "HeartSpecimen")


class RenalMedullaSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002521", "RenalMedullaSpecimen")


class AdrenalGlandSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002522", "AdrenalGlandSpecimen")


class BreastSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002523", "BreastSpecimen")


class UrinaryBladderSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002524", "UrinaryBladderSpecimen"
    )


class TibialArterySpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002525", "TibialArterySpecimen")


class SkinOfBodySpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002526", "SkinOfBodySpecimen")


class PancreasSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002527", "PancreasSpecimen")


class PituitaryGlandSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002529", "PituitaryGlandSpecimen"
    )


class AdiposeTissueSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002530", "AdiposeTissueSpecimen"
    )


class CortexOfKidneySpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002531", "CortexOfKidneySpecimen"
    )


class ThyroidGlandSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002537", "ThyroidGlandSpecimen")


class TibialNerveSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002539", "TibialNerveSpecimen")


class CoronaryArterySpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002540", "CoronaryArterySpecimen"
    )


class SpleenSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002541", "SpleenSpecimen")


class AortaSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002542", "AortaSpecimen")


class AtrialAppendageSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002543", "AtrialAppendageSpecimen"
    )


class LiverSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002546", "LiverSpecimen")


class MinorSalivaryGlandSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002547", "MinorSalivaryGlandSpecimen"
    )


class OmentumSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002548", "OmentumSpecimen")


class OvarySpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002549", "OvarySpecimen")


class TestisSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002552", "TestisSpecimen")


class UterusSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002553", "UterusSpecimen")


class VaginaSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002554", "VaginaSpecimen")


class DigestiveTractSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003483", "DigestiveTractSpecimen"
    )


class UrethraSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000001", "UrethraSpecimen")


class ThroatSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000003", "ThroatSpecimen")


class EyeSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000004", "EyeSpecimen")


class RespiratorySystemSpecimen(SpecimenFromOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000005", "RespiratorySystemSpecimen"
    )


class BodilyFluidSpecimen(SpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000009", "BodilyFluidSpecimen")


class OralSwabSpecimen(SpecimenFromOrganism, SwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002607", "OralSwabSpecimen")


class EnvironmentalSwabSpecimen(SwabSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002613", "EnvironmentalSwabSpecimen"
    )


class AmnioticFluid(OrganismSubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000173", "AmnioticFluid")


class Urine(OrganismSubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001088", "Urine")


class VitreousHumor(OrganismSubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001797", "VitreousHumor")


class Saliva(OrganismSubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001836", "Saliva")


class Semen(OrganismSubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001968", "Semen")


class Feces(OrganismSubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001988", "Feces")


class BodilyFluid(OrganismSubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0006314", "BodilyFluid")


class RespiratorySystemFluidSecretion(OrganismSubstance):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0006538",
        "RespiratorySystemFluidSecretion",
    )


class DigestiveSystemSecretedSubstance(OrganismSubstance):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0006911",
        "DigestiveSystemSecretedSubstance",
    )


class Epithelium(Tissue):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000483", "Epithelium")


class AdiposeTissue(Tissue):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001013", "AdiposeTissue")


class SkeletalMuscleTissue(Tissue):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0001134", "SkeletalMuscleTissue"
    )


class BoneMarrow(Tissue):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002371", "BoneMarrow")


class EsophagusMuscularisMucosa(Tissue):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0004648", "EsophagusMuscularisMucosa"
    )


class TendonOfBicepsBrachii(Tissue):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0008188", "TendonOfBicepsBrachii"
    )


class RenalMedulla(MultiTissueStructure):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000362", "RenalMedulla")


class Telencephalon(MultiTissueStructure):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001893", "Telencephalon")


class Cerebellum(MultiTissueStructure):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002037", "Cerebellum")


class Peritoneum(MultiTissueStructure):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002358", "Peritoneum")


class AtriumAuricularRegion(MultiTissueStructure):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0006618", "AtriumAuricularRegion"
    )


class CommonCarotidArteryPlusBranches(Artery):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0001530",
        "CommonCarotidArteryPlusBranches",
    )


class CoronaryArtery(Artery):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001621", "CoronaryArtery")


class TibialArtery(Artery):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0007610", "TibialArtery")


class RecordFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000368", "RecordFunction")


class MagnifyFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000369", "MagnifyFunction")


class ContainFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000370", "ContainFunction")


class HeatFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000371", "HeatFunction")


class MaterialSeparationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000372", "MaterialSeparationFunction"
    )


class ExcitationFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000374", "ExcitationFunction")


class FreezeFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000375", "FreezeFunction")


class SynthesizingFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000376", "SynthesizingFunction")


class PerturbFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000377", "PerturbFunction")


class MechanicalFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000379", "MechanicalFunction")


class TransferFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000383", "TransferFunction")


class IonizationFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000385", "IonizationFunction")


class CoolFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000387", "CoolFunction")


class ConnectionFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000388", "ConnectionFunction")


class EnergySupplyFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000391", "EnergySupplyFunction")


class InformationProcessorFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000392", "InformationProcessorFunction"
    )


class SolidSupportFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000399", "SolidSupportFunction")


class EnvironmentControlFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000401", "EnvironmentControlFunction"
    )


class MeasureFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000453", "MeasureFunction")


class ConsumeDataFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000455", "ConsumeDataFunction")


class MaterialCombinationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000928", "MaterialCombinationFunction"
    )


class SterilizationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000946", "SterilizationFunction"
    )


class ReagentApplicationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000960", "ReagentApplicationFunction"
    )


class SpecimenFixationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001036", "SpecimenFixationFunction"
    )


class CurrentAmplificationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001040", "CurrentAmplificationFunction"
    )


class StabilizationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001041", "StabilizationFunction"
    )


class InjectionFunction(Function):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0005246", "InjectionFunction")


class AdaptiveImmuneEffectorFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110016", "AdaptiveImmuneEffectorFunction"
    )


class AntigenPresentationFunction(Function):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110085", "AntigenPresentationFunction"
    )


class HumanPathogenicityDisposition(PathogenicDisposition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IDO_0000666", "HumanPathogenicityDisposition"
    )


class InfectiousDisease(Disease):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110040", "InfectiousDisease")


class Allergy(Disease):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110049", "Allergy")


class Cancer(Disease):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110053", "Cancer")


class AutoimmuneDisease(Disease):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110054", "AutoimmuneDisease")


class RegulatorRole(RegulatoryRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000014", "RegulatorRole")


class RegulationAssignedRole(RegulatoryRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000016", "RegulationAssignedRole"
    )


class PositiveReferenceSubstanceRole(ReferenceSubstanceRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000064", "PositiveReferenceSubstanceRole"
    )


class CalibrationSubstanceRole(ReferenceSubstanceRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000129", "CalibrationSubstanceRole"
    )


class NegativeReferenceSubstanceRole(ReferenceSubstanceRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000214", "NegativeReferenceSubstanceRole"
    )


class NucleicAcidTemplateRole(ReferenceSubstanceRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000409", "NucleicAcidTemplateRole"
    )


class SpikeInQualityControlRole(ReferenceSubstanceRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001140", "SpikeInQualityControlRole"
    )


class DyeSwapQualityControlRole(ReferenceSubstanceRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001142", "DyeSwapQualityControlRole"
    )


class ReferenceGenomeRole(ReferenceSubstanceRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002477", "ReferenceGenomeRole")


class BarcodeTargetLocusRole(EvaluantRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003029", "BarcodeTargetLocusRole"
    )


class MagneticResonanceImagingEvaluantRole(EvaluantRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003330",
        "MagneticResonanceImagingEvaluantRole",
    )


class ReferenceSubjectRole(ParticipantUnderInvestigationRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000220", "ReferenceSubjectRole")


class ToBeTreatedWithActiveIngredientRole(ParticipantUnderInvestigationRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000813",
        "ToBeTreatedWithActiveIngredientRole",
    )


class ToBeTreatedWithPlaceboRole(ParticipantUnderInvestigationRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000825", "ToBeTreatedWithPlaceboRole"
    )


class CaseRoleInCaseControlStudy(ParticipantUnderInvestigationRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002492", "CaseRoleInCaseControlStudy"
    )


class ControlRoleInCaseControlStudy(ParticipantUnderInvestigationRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002493", "ControlRoleInCaseControlStudy"
    )


class MaterialSampleRole(SpecimenRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000740", "MaterialSampleRole")


class ClusterStudyGroupRole(StudyGroupRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002898", "ClusterStudyGroupRole"
    )


class CompoundStudyGroupRole(StudyGroupRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002899", "CompoundStudyGroupRole"
    )


class ReportingPartyRole(InvestigationAgentRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000068", "ReportingPartyRole")


class ResponsiblePartyRole(InvestigationAgentRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000102", "ResponsiblePartyRole")


class WorkerRole(InvestigationAgentRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000116", "WorkerRole")


class SpecimenCollectorRole(InvestigationAgentRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001769", "SpecimenCollectorRole"
    )


class CompleteNutrientRole(NutrientRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000162", "CompleteNutrientRole")


class AssayAntigenRole(AntigenRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110120", "AssayAntigenRole")


class CloningVectorRole(MaterialToBeAddedRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000411", "CloningVectorRole")


class ArrayManufacturerRole(ManufacturerRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001069", "ArrayManufacturerRole"
    )


class PrimerRole(ComplementaryNucleotideProbeRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000405", "PrimerRole")


class MaterialSupplierRole(ServiceProviderRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000018", "MaterialSupplierRole")


class AnalyteRole(MeasurandRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000275", "AnalyteRole")


class ReagentRole(ReactantRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000086", "ReagentRole")


class PrecursorRole(ReactantRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003611", "PrecursorRole")


class SolventRole(ReactantRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302732", "SolventRole")


class ImmunologicAdjuvantRole(AdjuvantRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000720", "ImmunologicAdjuvantRole"
    )


class UpperLimbCoordinationEfficacy(LimbCoordinationEfficacy):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060181", "UpperLimbCoordinationEfficacy"
    )


class LowerLimbCoordinationEfficacy(LimbCoordinationEfficacy):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBA_2060182", "LowerLimbCoordinationEfficacy"
    )


class SecondaryStructureOfRnaMolecule(SecondaryStructureOfSequenceMacromolecule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000896", "SecondaryStructureOfRnaMolecule"
    )


class Size(Morphology):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000117", "Size")


class Structure(Morphology):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000141", "Structure")


class Mass(PhysicalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000125", "Mass")


class Position(PhysicalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000140", "Position")


class Temperature(PhysicalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000146", "Temperature")


class Time(PhysicalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000165", "Time")


class Pressure(PhysicalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001025", "Pressure")


class MovementQuality(PhysicalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001906", "MovementQuality")


class QualityOfASubstance(PhysicalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0002198", "QualityOfASubstance")


class Fasted(OrganismalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003655", "Fasted")


class BiologicalSex(OrganismalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000047", "BiologicalSex")


class Viability(OrganismalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000169", "Viability")


class BehavioralQuality(OrganismalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000186", "BehavioralQuality")


class MixedSex(PopulationQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001338", "MixedSex")


class CellularQuality(AnatomicalStructureQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001396", "CellularQuality")


class ConcentrationOf(Amount):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000033", "ConcentrationOf")


class LengthUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000001", "LengthUnit")


class MassUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000002", "MassUnit")


class TimeUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000003", "TimeUnit")


class TemperatureUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000005", "TemperatureUnit")


class SubstanceUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000006", "SubstanceUnit")


class ConcentrationUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000051", "ConcentrationUnit")


class VolumeUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000095", "VolumeUnit")


class FrequencyUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000105", "FrequencyUnit")


class PressureUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000109", "PressureUnit")


class VolumetricFlowRateUnit(MeasurementUnitLabel):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UO_0000270", "VolumetricFlowRateUnit"
    )


class RateUnit(MeasurementUnitLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/UO_0000280", "RateUnit")


class ClassifiedDataSet(DataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000023", "ClassifiedDataSet")


class GeneList(DataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000118", "GeneList")


class Cluster(DataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000251", "Cluster")


class NormalizedDataSet(DataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000451", "NormalizedDataSet")


class ClusteredDataSet(DataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000648", "ClusteredDataSet")


class DataSetOfFeatures(DataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000649", "DataSetOfFeatures")


class DataSetOfPredictedValuesAccordingToFittedCurve(DataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000656",
        "DataSetOfPredictedValuesAccordingToFittedCurve",
    )


class BackgroundCorrectedDataSet(DataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000660", "BackgroundCorrectedDataSet"
    )


class ErrorCorrectedDataSet(DataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000662", "ErrorCorrectedDataSet"
    )


class ReducedDimensionDataSet(DataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000676", "ReducedDimensionDataSet"
    )


class SequenceLibraryFeatureCountData(DataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002582", "SequenceLibraryFeatureCountData"
    )


class DifferentialExpressionAnalysisData(DataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002584",
        "DifferentialExpressionAnalysisData",
    )


class ImageDataSet(DataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003327", "ImageDataSet")


class CurationStatusSpecification(DataAboutAnOntologyPart):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000078", "CurationStatusSpecification"
    )


class ObsolescenceReasonSpecification(DataAboutAnOntologyPart):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000225", "ObsolescenceReasonSpecification"
    )


class DenotatorType(DataAboutAnOntologyPart):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000409", "DenotatorType")


class OntologyModule(DataAboutAnOntologyPart):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_8000000", "OntologyModule")


class ScalarMeasurementDatum(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000032", "ScalarMeasurementDatum"
    )


class FluorescentReporterIntensity(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000010", "FluorescentReporterIntensity"
    )


class RatioOfCollectedToEmittedLight(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000054", "RatioOfCollectedToEmittedLight"
    )


class MeasuredExpressionLevel(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000101", "MeasuredExpressionLevel"
    )


class NumberOfParticlesInSubset(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000119", "NumberOfParticlesInSubset"
    )


class NumberOfLostEventsElectronic(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000125", "NumberOfLostEventsElectronic"
    )


class ParameterThreshold(MeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000172", "ParameterThreshold")


class NumberOfLostEventsComputer(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000269", "NumberOfLostEventsComputer"
    )


class SurvivalRate(MeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000789", "SurvivalRate")


class SpikeTrainDatum(MeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000801", "SpikeTrainDatum")


class CategoricalMeasurementDatum(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000938", "CategoricalMeasurementDatum"
    )


class ScalarScoreFromCompositeInputs(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000970", "ScalarScoreFromCompositeInputs"
    )


class SequenceData(MeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000973", "SequenceData")


class Dose(MeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000984", "Dose")


class _3DStructuralOrganizationDatum(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001155", "_3DStructuralOrganizationDatum"
    )


class LatitudeCoordinateMeasurementDatum(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001620",
        "LatitudeCoordinateMeasurementDatum",
    )


class LongitudeCoordinateMeasurementDatum(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001621",
        "LongitudeCoordinateMeasurementDatum",
    )


class NumberOfPregnancies(MeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002394", "NumberOfPregnancies")


class NumberOfLiveBirths(MeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002395", "NumberOfLiveBirths")


class SequenceReadLengthMeasurementDatum(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002479",
        "SequenceReadLengthMeasurementDatum",
    )


class SpecimenHarvestQuantity(MeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002482", "SpecimenHarvestQuantity"
    )


class EastingCoordinateMeasurementDatum(OneDimensionalCartesianSpatialCoordinateDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003066",
        "EastingCoordinateMeasurementDatum",
    )


class NorthingCoordinateMeasurementDatum(OneDimensionalCartesianSpatialCoordinateDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003067",
        "NorthingCoordinateMeasurementDatum",
    )


class PValue(QuantitativeConfidenceValue):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000175", "PValue")


class StandardError(QuantitativeConfidenceValue):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000235", "StandardError")


class FwerAdjustedPValue(QuantitativeConfidenceValue):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001265", "FwerAdjustedPValue")


class QValue(QuantitativeConfidenceValue):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001442", "QValue")


class AverageDepthOfSequenceCoverage(AverageValue):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001618", "AverageDepthOfSequenceCoverage"
    )


class CategoricalBindingDatum(BindingDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003141", "CategoricalBindingDatum"
    )


class QuantitativeBindingDatum(BindingDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003142", "QuantitativeBindingDatum"
    )


class GeneticPopulationBackgroundInformation(GeneticCharacteristicsInformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001225",
        "GeneticPopulationBackgroundInformation",
    )


class GenotypeInformation(GeneticCharacteristicsInformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001305", "GenotypeInformation")


class GeneticAlterationInformation(GeneticCharacteristicsInformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001364", "GeneticAlterationInformation"
    )


class KaryotypeInformation(GeneticCharacteristicsInformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002769", "KaryotypeInformation")


class HumanLeukocyteAntigenMismatchCount(GeneticCharacteristicsInformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003594",
        "HumanLeukocyteAntigenMismatchCount",
    )


class LungMicrobiologyDatum(OrganismDetectionDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003256", "LungMicrobiologyDatum"
    )


class NasopharyngealOrOropharyngealSwabMicrobiologyDatum(OrganismDetectionDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003257",
        "NasopharyngealOrOropharyngealSwabMicrobiologyDatum",
    )


class PleuralFluidMicrobiologyDatum(OrganismDetectionDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003258", "PleuralFluidMicrobiologyDatum"
    )


class SkinOfBodyMicrobiologyDatum(OrganismDetectionDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003577", "SkinOfBodyMicrobiologyDatum"
    )


class BoneMarrowMicrobiologyDatum(OrganismDetectionDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003579", "BoneMarrowMicrobiologyDatum"
    )


class NasalAspirateMicrobiologyDatum(OrganismDetectionDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003581", "NasalAspirateMicrobiologyDatum"
    )


class BloodMicrobiologyDatum(OrganismDetectionDatum, BloodAssayDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003244", "BloodMicrobiologyDatum"
    )


class UmbilicalCordBloodAssayDatum(BloodAssayDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003259", "UmbilicalCordBloodAssayDatum"
    )


class FecesMicrobiologyDatum(OrganismDetectionDatum, FecesAssayDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003246", "FecesMicrobiologyDatum"
    )


class UrineMicrobiologyDatum(OrganismDetectionDatum, UrineAssayDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003248", "UrineMicrobiologyDatum"
    )


class InducedSputumMicrobiologyDatum(OrganismDetectionDatum, InducedSputumAssayDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003251", "InducedSputumMicrobiologyDatum"
    )


class CerebrospinalFluidMicrobiologyDatum(
    OrganismDetectionDatum, CerebrospinalFluidAssayDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003253",
        "CerebrospinalFluidMicrobiologyDatum",
    )


class EndotrachealTubeAspirateMicrobiologyDatum(
    OrganismDetectionDatum, EndotrachealAspirateAssayDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003255",
        "EndotrachealTubeAspirateMicrobiologyDatum",
    )


class AntigenSpecificAntibodiesInBloodAssayDatum(
    BloodAssayDatum, AntigenSpecificAntibodiesAssayDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003420",
        "AntigenSpecificAntibodiesInBloodAssayDatum",
    )


class AntigenSpecificAntibodiesInMilkAssayDatum(
    MilkAssayDatum, AntigenSpecificAntibodiesAssayDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003421",
        "AntigenSpecificAntibodiesInMilkAssayDatum",
    )


class DiagnosisOfCancer(Diagnosis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002371", "DiagnosisOfCancer")


class DiagnosisOfInfectiousDisease(Diagnosis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002385", "DiagnosisOfInfectiousDisease"
    )


class ChronicAllograftDamageIndexScore(ClinicalDataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003591", "ChronicAllograftDamageIndexScore"
    )


class SequentialOrganFailureAssessmentScore(ClinicalDataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003592",
        "SequentialOrganFailureAssessmentScore",
    )


class PhysicianSGlobalAssessmentOfDiseaseActivity(ClinicalDataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003593",
        "PhysicianSGlobalAssessmentOfDiseaseActivity",
    )


class MultidimensionalFatigueInventoryScore(ClinicalDataItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003651",
        "MultidimensionalFatigueInventoryScore",
    )


class IndividualOrganismIdentifier(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001141", "IndividualOrganismIdentifier"
    )


class GenbankId(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001614", "GenbankId")


class SpecimenIdentifier(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001616", "SpecimenIdentifier")


class PubmedId(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001617", "PubmedId")


class InvestigationIdentifier(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001628", "InvestigationIdentifier"
    )


class GrantIdentifier(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001629", "GrantIdentifier")


class DigitalObjectIdentifier(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002110", "DigitalObjectIdentifier"
    )


class CourierTrackingNumber(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002191", "CourierTrackingNumber"
    )


class SrsIdentifier(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002464", "SrsIdentifier")


class DbgapStudyIdentifier(CentrallyRegisteredIdentifierSymbol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002472", "DbgapStudyIdentifier")


class Rule(ConditionalSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000055", "Rule")


class AdverseEventTrigger(ConditionalSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000310", "AdverseEventTrigger")


class BiologicalFeatureIdentificationObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000015",
        "BiologicalFeatureIdentificationObjective",
    )


class MethodologyTestingObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000208", "MethodologyTestingObjective"
    )


class AssayObjective(ObjectiveSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000441", "AssayObjective")


class MaterialTransformationObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000456", "MaterialTransformationObjective"
    )


class SpecimenCollectionObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000684", "SpecimenCollectionObjective"
    )


class MaterialMaintenanceObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000806", "MaterialMaintenanceObjective"
    )


class TrainingObjective(ObjectiveSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000962", "TrainingObjective")


class ServiceProvisionObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000993", "ServiceProvisionObjective"
    )


class AssayValidationObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001160", "AssayValidationObjective"
    )


class SelectiveOrganismCreationObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001175",
        "SelectiveOrganismCreationObjective",
    )


class SpecificationOfDataToBeGeneratedInAnInvestigation(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001892",
        "SpecificationOfDataToBeGeneratedInAnInvestigation",
    )


class DecisionTheoreticAnalysisObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001964",
        "DecisionTheoreticAnalysisObjective",
    )


class DiseaseCausationObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003607", "DiseaseCausationObjective"
    )


class DiseaseSeverityReductionObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003608",
        "DiseaseSeverityReductionObjective",
    )


class DiseasePreventionObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003609", "DiseasePreventionObjective"
    )


class DiseasePrevalenceReductionObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003614",
        "DiseasePrevalenceReductionObjective",
    )


class DataTransformationObjective(ObjectiveSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200166", "DataTransformationObjective"
    )


class BclFormat(DataFormatSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002461", "BclFormat")


class Software(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000010", "Software")


class Algorithm(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000064", "Algorithm")


class Protocol(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000272", "Protocol")


class Grant(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001636", "Grant")


class TargetMaterialInSpecimenSpecification(PlanSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001882",
        "TargetMaterialInSpecimenSpecification",
    )


class SpecimenBasedScopeOfInvestigationSpecification(PlanSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001884",
        "SpecimenBasedScopeOfInvestigationSpecification",
    )


class InvestigationAssaySpecification(PlanSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001896", "InvestigationAssaySpecification"
    )


class TargetCaptureSpecification(PlanSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001899", "TargetCaptureSpecification"
    )


class SoftwarePipeline(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001943", "SoftwarePipeline")


class PcrProgram(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001961", "PcrProgram")


class StudyArmDesign(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003705", "StudyArmDesign")


class StudyDesign(PlanSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500000", "StudyDesign")


class EligibilityCriterion(SelectionCriterion):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500026", "EligibilityCriterion")


class LaboratoryPostalAddress(PostalAddress):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003085", "LaboratoryPostalAddress"
    )


class InvestigationDescription(CommentOnInvestigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001615", "InvestigationDescription"
    )


class InvestigationTitle(CommentOnInvestigation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001622", "InvestigationTitle")


class DotPlot(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000037", "DotPlot")


class DensityPlot(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000079", "DensityPlot")


class Histogram(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000179", "Histogram")


class Heatmap(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000180", "Heatmap")


class Dendrogram(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000183", "Dendrogram")


class ScatterPlot(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000184", "ScatterPlot")


class LineGraph(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000573", "LineGraph")


class GraphOfVertices(Graph):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000714", "GraphOfVertices")


class InvestigationResultsReport(Report):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000218", "InvestigationResultsReport"
    )


class DirectSubmissionToIedb(Report):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110300", "DirectSubmissionToIedb"
    )


class PublicationAboutAnInvestigation(Publication):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000312", "PublicationAboutAnInvestigation"
    )


class HistologicGradeAccordingToAjcc7ThEdition(CategoricalValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002205",
        "HistologicGradeAccordingToAjcc7ThEdition",
    )


class HistologicGradeAccordingToTheFuhrmanNuclearGradingSystem(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002210",
        "HistologicGradeAccordingToTheFuhrmanNuclearGradingSystem",
    )


class HistologicGradeForOvarianTumor(CategoricalValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002215", "HistologicGradeForOvarianTumor"
    )


class PathologicPrimaryTumorStageForColonAndRectumAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002224",
        "PathologicPrimaryTumorStageForColonAndRectumAccordingToAjcc7ThEdition",
    )


class PathologicPrimaryTumorStageForLungAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002232",
        "PathologicPrimaryTumorStageForLungAccordingToAjcc7ThEdition",
    )


class PathologicPrimaryTumorStageForKidneyAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002243",
        "PathologicPrimaryTumorStageForKidneyAccordingToAjcc7ThEdition",
    )


class PathologicPrimaryTumorStageForOvaryAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002256",
        "PathologicPrimaryTumorStageForOvaryAccordingToAjcc7ThEdition",
    )


class PathologicLymphNodeStageForColonAndRectumAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002270",
        "PathologicLymphNodeStageForColonAndRectumAccordingToAjcc7ThEdition",
    )


class PathologicLymphNodeStageForLungAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002279",
        "PathologicLymphNodeStageForLungAccordingToAjcc7ThEdition",
    )


class PathologicLymphNodeStageForKidneyAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002284",
        "PathologicLymphNodeStageForKidneyAccordingToAjcc7ThEdition",
    )


class PathologicLymphNodeStageForOvaryAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002287",
        "PathologicLymphNodeStageForOvaryAccordingToAjcc7ThEdition",
    )


class PathologicDistantMetastasesStageForColonAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002290",
        "PathologicDistantMetastasesStageForColonAccordingToAjcc7ThEdition",
    )


class PathologicDistantMetastasesStageForLungAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002298",
        "PathologicDistantMetastasesStageForLungAccordingToAjcc7ThEdition",
    )


class PathologicDistantMetastasesStageForKidneyAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002306",
        "PathologicDistantMetastasesStageForKidneyAccordingToAjcc7ThEdition",
    )


class PathologicDistantMetastasesStageForOvaryAccordingToAjcc7ThEdition(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002310",
        "PathologicDistantMetastasesStageForOvaryAccordingToAjcc7ThEdition",
    )


class ClinicalTumorStageGroupAccordingToAjcc7ThEdition(CategoricalValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002314",
        "ClinicalTumorStageGroupAccordingToAjcc7ThEdition",
    )


class InternationalFederationOfGynecologyAndObstetricsCervicalCancerStageValueSpecification(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002326",
        "InternationalFederationOfGynecologyAndObstetricsCervicalCancerStageValueSpecification",
    )


class InternationalFederationOfGynecologyAndObstetricsOvarianCancerStageValueSpecification(
    CategoricalValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002341",
        "InternationalFederationOfGynecologyAndObstetricsOvarianCancerStageValueSpecification",
    )


class PerformanceStatusValueSpecification(CategoricalValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002356",
        "PerformanceStatusValueSpecification",
    )


class OrdinalValueSpecification(CategoricalValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002756", "OrdinalValueSpecification"
    )


class HypertensionGrade(CategoricalValueSpecification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003600", "HypertensionGrade")


class MassValueSpecification(ScalarValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001929", "MassValueSpecification"
    )


class MedicationTimeValueSpecification(ScalarValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002490", "MedicationTimeValueSpecification"
    )


class MedicationDoseValueSpecification(ScalarValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002491", "MedicationDoseValueSpecification"
    )


class Gx(CannotBeAssessedDetermination):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002202", "Gx")


class Ptx(CannotBeAssessedDetermination):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002203", "Ptx")


class Pnx(CannotBeAssessedDetermination):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002204", "Pnx")


class AuntClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002373", "AuntClinicalHistoryOfCancer"
    )


class BrotherClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002374", "BrotherClinicalHistoryOfCancer"
    )


class DaughterClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002375", "DaughterClinicalHistoryOfCancer"
    )


class FatherClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002376", "FatherClinicalHistoryOfCancer"
    )


class MotherClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002377", "MotherClinicalHistoryOfCancer"
    )


class SisterClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002378", "SisterClinicalHistoryOfCancer"
    )


class SonClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002379", "SonClinicalHistoryOfCancer"
    )


class UncleClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002380", "UncleClinicalHistoryOfCancer"
    )


class GrandmotherClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002381",
        "GrandmotherClinicalHistoryOfCancer",
    )


class GrandfatherClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002382",
        "GrandfatherClinicalHistoryOfCancer",
    )


class NephewClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002383", "NephewClinicalHistoryOfCancer"
    )


class NieceClinicalHistoryOfCancer(FamilyClinicalHistoryOfCancer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002384", "NieceClinicalHistoryOfCancer"
    )


class ExposureToSecondHandSmokeInHouseholdDuringChildhood(ExposureToSecondHandSmoke):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002391",
        "ExposureToSecondHandSmokeInHouseholdDuringChildhood",
    )


class ExposureToSecondHandSmokeInCurrentHousehold(ExposureToSecondHandSmoke):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002392",
        "ExposureToSecondHandSmokeInCurrentHousehold",
    )


class HysterectomyHistory(GynecologicSurgeryHistory):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002398", "HysterectomyHistory")


class UnilateralOophorectomyHistory(GynecologicSurgeryHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002399", "UnilateralOophorectomyHistory"
    )


class NeitherHysterectomyNorOophorectomyHistory(GynecologicSurgeryHistory):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002400",
        "NeitherHysterectomyNorOophorectomyHistory",
    )


class SequenceAssembly(Assembly):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000353", "SequenceAssembly")


class ChemokineCXCMotifLigand9Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0035393",
        "ChemokineCXCMotifLigand9Production",
    )


class ChemokineCCMotifLigand20Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0036392",
        "ChemokineCCMotifLigand20Production",
    )


class ChemokineCCMotifLigand17Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0044809",
        "ChemokineCCMotifLigand17Production",
    )


class MonocyteChemotacticProtein1Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071605",
        "MonocyteChemotacticProtein1Production",
    )


class ChemokineCCMotifLigand4Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071606", "ChemokineCCMotifLigand4Production"
    )


class MacrophageInflammatoryProtein1GammaProduction(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071607",
        "MacrophageInflammatoryProtein1GammaProduction",
    )


class MacrophageInflammatoryProtein1AlphaProduction(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071608",
        "MacrophageInflammatoryProtein1AlphaProduction",
    )


class ChemokineCCMotifLigand5Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071609", "ChemokineCCMotifLigand5Production"
    )


class ChemokineCCMotifLigand1Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071610", "ChemokineCCMotifLigand1Production"
    )


class Ip10Production(ChemokineProduction):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0071612", "Ip10Production")


class ChemokineCCMotifLigand22Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0071924",
        "ChemokineCCMotifLigand22Production",
    )


class ChemokineCCMotifLigand19Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097388",
        "ChemokineCCMotifLigand19Production",
    )


class ChemokineCCMotifLigand21Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097389",
        "ChemokineCCMotifLigand21Production",
    )


class ChemokineCXCMotifLigand12Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097390",
        "ChemokineCXCMotifLigand12Production",
    )


class ChemokineCXCMotifLigand13Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097391",
        "ChemokineCXCMotifLigand13Production",
    )


class ChemokineCXCMotifLigand16Production(ChemokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097392",
        "ChemokineCXCMotifLigand16Production",
    )


class InterferonAlphaProduction(TypeIInterferonProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032607", "InterferonAlphaProduction"
    )


class Interleukin1AlphaProduction(Interleukin1Production):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032610", "Interleukin1AlphaProduction"
    )


class Interleukin1BetaProduction(Interleukin1Production):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032611", "Interleukin1BetaProduction"
    )


class Interleukin17AProduction(Interleukin17Production):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097087", "Interleukin17AProduction"
    )


class Interleukin17FProduction(Interleukin17Production):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097088", "Interleukin17FProduction"
    )


class TumorNecrosisFactorProduction(TumorNecrosisFactorSuperfamilyCytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032640", "TumorNecrosisFactorProduction"
    )


class LymphotoxinAProduction(TumorNecrosisFactorSuperfamilyCytokineProduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0032641", "LymphotoxinAProduction"
    )


class TumorNecrosisFactorLigandSuperfamilyMember11Production(
    TumorNecrosisFactorSuperfamilyCytokineProduction
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0072535",
        "TumorNecrosisFactorLigandSuperfamilyMember11Production",
    )


class EpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells(
    VascularEndothelialGrowthFactorProduction, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001612",
        "EpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells",
    )


class EpitopeSpecificGmCsfReleaseByTCells(
    GranulocyteMacrophageColonyStimulatingFactorProduction,
    EpitopeSpecificCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110184",
        "EpitopeSpecificGmCsfReleaseByTCells",
    )


class EpitopeSpecificInterferonBetaProductionByTCells(
    InterferonBetaProduction, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001421",
        "EpitopeSpecificInterferonBetaProductionByTCells",
    )


class EpitopeSpecificIfnGReleaseByTCells(
    TypeIiInterferonProduction, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110185",
        "EpitopeSpecificIfnGReleaseByTCells",
    )


class EpitopeSpecificIl10ReleaseByTCells(
    Interleukin10Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110187",
        "EpitopeSpecificIl10ReleaseByTCells",
    )


class EpitopeSpecificIl12ReleaseByTCells(
    Interleukin12Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110190",
        "EpitopeSpecificIl12ReleaseByTCells",
    )


class EpitopeSpecificIl13ReleaseByTCells(
    Interleukin13Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110191",
        "EpitopeSpecificIl13ReleaseByTCells",
    )


class EpitopeSpecificInterleukin15ProductionByTCells(
    Interleukin15Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001446",
        "EpitopeSpecificInterleukin15ProductionByTCells",
    )


class EpitopeSpecificInterleukin16ProductionByTCells(
    Interleukin16Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001275",
        "EpitopeSpecificInterleukin16ProductionByTCells",
    )


class EpitopeSpecificIl17ReleaseByTCells(
    Interleukin17Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110193",
        "EpitopeSpecificIl17ReleaseByTCells",
    )


class EpitopeSpecificIl18ReleaseByTCells(
    Interleukin18Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110195",
        "EpitopeSpecificIl18ReleaseByTCells",
    )


class EpitopeSpecificIl2ReleaseByTCells(
    Interleukin2Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110056",
        "EpitopeSpecificIl2ReleaseByTCells",
    )


class EpitopeSpecificInterleukin21ProductionByTCells(
    Interleukin21Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001316",
        "EpitopeSpecificInterleukin21ProductionByTCells",
    )


class EpitopeSpecificInterleukin22ProductionByTCells(
    Interleukin22Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001399",
        "EpitopeSpecificInterleukin22ProductionByTCells",
    )


class EpitopeSpecificInterleukin23ProductionByTCells(
    Interleukin23Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001381",
        "EpitopeSpecificInterleukin23ProductionByTCells",
    )


class EpitopeSpecificInterleukin27ProductionByTCells(
    Interleukin27Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001262",
        "EpitopeSpecificInterleukin27ProductionByTCells",
    )


class EpitopeSpecificInterleukin3ProductionByTCells(
    Interleukin3Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001254",
        "EpitopeSpecificInterleukin3ProductionByTCells",
    )


class EpitopeSpecificIl4ReleaseByTCells(
    Interleukin4Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110199",
        "EpitopeSpecificIl4ReleaseByTCells",
    )


class EpitopeSpecificIl5ReleaseByTCells(
    Interleukin5Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110202",
        "EpitopeSpecificIl5ReleaseByTCells",
    )


class EpitopeSpecificIl6ReleaseByTCells(
    Interleukin6Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110203",
        "EpitopeSpecificIl6ReleaseByTCells",
    )


class EpitopeSpecificInterleukin7ProductionByTCells(
    Interleukin7Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001535",
        "EpitopeSpecificInterleukin7ProductionByTCells",
    )


class EpitopeSpecificInterleukin8ProductionByTCells(
    Interleukin8Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001373",
        "EpitopeSpecificInterleukin8ProductionByTCells",
    )


class EpitopeSpecificInterleukin9ProductionByTCells(
    Interleukin9Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001415",
        "EpitopeSpecificInterleukin9ProductionByTCells",
    )


class EpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    TransformingGrowthFactorBetaProduction, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001267",
        "EpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class EpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells(
    GranulocyteColonyStimulatingFactorProduction,
    EpitopeSpecificCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001334",
        "EpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells",
    )


class EpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    TumorNecrosisFactorSuperfamilyCytokineProduction,
    EpitopeSpecificCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001351",
        "EpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class EpitopeSpecificXcl1ReleaseByTCells(
    Xcl1Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003371",
        "EpitopeSpecificXcl1ReleaseByTCells",
    )


class EpitopeSpecificKillingByTCells(TCellMediatedCytotoxicity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110204", "EpitopeSpecificKillingByTCells"
    )


class EpitopeSpecificCytotoxicTCellDegranulation(CytotoxicTCellDegranulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001394",
        "EpitopeSpecificCytotoxicTCellDegranulation",
    )


class BCellEpitopeSpecificComplementDependentCytotoxicity(
    ComplementDependentCytotoxicity
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001716",
        "BCellEpitopeSpecificComplementDependentCytotoxicity",
    )


class EpitopeSpecificTCellToleranceInduction(
    TCellToleranceInduction, EpitopeSpecificToleranceInductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001249",
        "EpitopeSpecificTCellToleranceInduction",
    )


class EpitopeSpecificTypeIvHypersensitivityByTCells(TypeIvHypersensitivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001212",
        "EpitopeSpecificTypeIvHypersensitivityByTCells",
    )


class BCellEpitopeSpecificOpsonization(Opsonization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001713", "BCellEpitopeSpecificOpsonization"
    )


class EpitopeSpecificTCellProliferation(TCellProliferation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110182",
        "EpitopeSpecificTCellProliferation",
    )


class BCellEpitopeSpecificImmunoglobulinMediatedNeutralization(
    ImmunoglobulinMediatedNeutralization
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001714",
        "BCellEpitopeSpecificImmunoglobulinMediatedNeutralization",
    )


class AdaptiveImmuneResponse(ImmuneResponse):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0002250", "AdaptiveImmuneResponse"
    )


class InnateImmuneResponse(ImmuneResponse):
    term = RdfTerm("http://purl.obolibrary.org/obo/GO_0045087", "InnateImmuneResponse")


class HistamineSecretionMediatedByImmunoglobulin(ImmuneResponse):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0097280",
        "HistamineSecretionMediatedByImmunoglobulin",
    )


class CorePromoterSequenceSpecificDnaBinding(
    SequenceSpecificDnaBinding, MolecularFunction
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0001046",
        "CorePromoterSequenceSpecificDnaBinding",
    )


class BCellEpitopeSpecificImmuneComplexFormation(
    ImmunoglobulinBindingToEpitope, ImmuneComplexFormation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001720",
        "BCellEpitopeSpecificImmuneComplexFormation",
    )


class IndividualEpitopeImmunizationInVivo(ImmunizationInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001176",
        "IndividualEpitopeImmunizationInVivo",
    )


class NestedCaseControlInvestigation(CaseControlInvestigation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003695", "NestedCaseControlInvestigation"
    )


class ObservationalClinicalInvestigation(
    ClinicalInvestigation, ObservationalInvestigation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003698",
        "ObservationalClinicalInvestigation",
    )


class ClinicalTrial(ClinicalInvestigation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003699", "ClinicalTrial")


class MicroscopyAssay(ImagingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002119", "MicroscopyAssay")


class MagneticResonanceImagingAssay(ImagingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002985", "MagneticResonanceImagingAssay"
    )


class ComputedTomographyImagingAssay(ImagingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002986", "ComputedTomographyImagingAssay"
    )


class PositronEmissionTomographyImagingAssay(ImagingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002987",
        "PositronEmissionTomographyImagingAssay",
    )


class MultiplexedFluorescentAntibodyImagingAssay(ImagingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003091",
        "MultiplexedFluorescentAntibodyImagingAssay",
    )


class PositiveNegativeIonSwitchingMetaboliteProfilingAssay(MetaboliteProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002968",
        "PositiveNegativeIonSwitchingMetaboliteProfilingAssay",
    )


class TranscriptionProfilingByArrayAssay(TranscriptionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001463",
        "TranscriptionProfilingByArrayAssay",
    )


class NanoCapAnalysisOfGeneExpressionAssay(TranscriptionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001673",
        "NanoCapAnalysisOfGeneExpressionAssay",
    )


class MicrornaProfilingAssay(TranscriptionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001926", "MicrornaProfilingAssay"
    )


class TranscriptionProfilingByMpssAssay(TranscriptionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002015",
        "TranscriptionProfilingByMpssAssay",
    )


class SerialAnalysisOfGeneExpressionAssay(TranscriptionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002029",
        "SerialAnalysisOfGeneExpressionAssay",
    )


class TranscriptionStartSiteMappingByPrimerExtensionAssay(TranscriptionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002445",
        "TranscriptionStartSiteMappingByPrimerExtensionAssay",
    )


class LandmarkTranscriptProfilingAssay(TranscriptionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002965", "LandmarkTranscriptProfilingAssay"
    )


class GenotypingAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000435", "GenotypingAssay")


class ClinicalChemistryAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000520", "ClinicalChemistryAssay"
    )


class EnzymeLinkedImmunosorbentAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000661", "EnzymeLinkedImmunosorbentAssay"
    )


class HumanAntithrombinIiiInBloodAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000787", "HumanAntithrombinIiiInBloodAssay"
    )


class NorthernBlotAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000860", "NorthernBlotAssay")


class ViralHemagglutinationAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000871", "ViralHemagglutinationAssay"
    )


class DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000874",
        "DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes",
    )


class SouthernBlotAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000892", "SouthernBlotAssay")


class CytometricBeadArrayAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000920", "CytometricBeadArrayAssay"
    )


class TranslationProfilingAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001282", "TranslationProfilingAssay"
    )


class AnalyticalChromatography(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001630", "AnalyticalChromatography"
    )


class ImmunoprecipitationAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001700", "ImmunoprecipitationAssay"
    )


class ImmunoblotAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001978", "ImmunoblotAssay")


class MicroarrayAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001985", "MicroarrayAssay")


class AntigenSpecificAntibodiesAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002145", "AntigenSpecificAntibodiesAssay"
    )


class VenerealDiseaseResearchLaboratoryTest(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002155",
        "VenerealDiseaseResearchLaboratoryTest",
    )


class RapidPlasmaReaginTest(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002156", "RapidPlasmaReaginTest"
    )


class HbvSurfaceAntigenAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002157", "HbvSurfaceAntigenAssay"
    )


class Hiv1NucleicAcidTesting(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002158", "Hiv1NucleicAcidTesting"
    )


class HcvNucleicAcidTesting(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002159", "HcvNucleicAcidTesting"
    )


class DotBlotAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002171", "DotBlotAssay")


class AtpBioluminescenceAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002175", "AtpBioluminescenceAssay"
    )


class LipidProfilingAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002761", "LipidProfilingAssay")


class CytokineAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002766", "CytokineAssay")


class IronAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003011", "IronAssay")


class IonizedCalciumAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003012", "IonizedCalciumAssay")


class UricAcidAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003014", "UricAcidAssay")


class GlobulinAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003015", "GlobulinAssay")


class SomascanAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003111", "SomascanAssay")


class CreatineAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003194", "CreatineAssay")


class EstradiolAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003196", "EstradiolAssay")


class LipoproteinConcentrationAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003204", "LipoproteinConcentrationAssay"
    )


class LuteinizingHormoneAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003208", "LuteinizingHormoneAssay"
    )


class NitriteAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003210", "NitriteAssay")


class PhospholipidAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003212", "PhospholipidAssay")


class ProgesteroneAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003214", "ProgesteroneAssay")


class TestosteroneAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003216", "TestosteroneAssay")


class BileSaltAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003218", "BileSaltAssay")


class FattyAcidAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003220", "FattyAcidAssay")


class InsulinAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003222", "InsulinAssay")


class FollicleStimulatingHormoneAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003224", "FollicleStimulatingHormoneAssay"
    )


class CarbonDioxideAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100001", "CarbonDioxideAssay")


class Sodium1Assay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100002", "Sodium1Assay")


class CreatinineAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100003", "CreatinineAssay")


class Potassium1Assay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100004", "Potassium1Assay")


class ChlorideAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100010", "ChlorideAssay")


class HemoglobinAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100014", "HemoglobinAssay")


class PhosphateIonAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100015", "PhosphateIonAssay")


class BilirubinIxalphaAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100018", "BilirubinIxalphaAssay"
    )


class GlucoseAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100020", "GlucoseAssay")


class MagnesiumCationAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100021", "MagnesiumCationAssay")


class ProteinAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100023", "ProteinAssay")


class TriglycerideAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100029", "TriglycerideAssay")


class HighDensityLipoproteinCholesterolAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100030",
        "HighDensityLipoproteinCholesterolAssay",
    )


class CholesterolAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100031", "CholesterolAssay")


class LowDensityLipoproteinCholesterolAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100032",
        "LowDensityLipoproteinCholesterolAssay",
    )


class ThyroidStimulatingHormoneAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100033", "ThyroidStimulatingHormoneAssay"
    )


class ThyroxineAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100035", "ThyroxineAssay")


class ElementalOxygenAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100036", "ElementalOxygenAssay")


class FolicAcidsAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100037", "FolicAcidsAssay")


class MethemoglobinAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100040", "MethemoglobinAssay")


class HydrogencarbonateAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100043", "HydrogencarbonateAssay"
    )


class VancomycinAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100044", "VancomycinAssay")


class TobramycinAssay(AnalyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100045", "TobramycinAssay")


class _335TriiodothyronineAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100046", "_335TriiodothyronineAssay"
    )


class _3HydroxybutyricAcidAssay(AnalyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100051", "_3HydroxybutyricAcidAssay"
    )


class PeptideMassFingerprintingAssay(MassSpectrometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002035", "PeptideMassFingerprintingAssay"
    )


class LiquidChromatographyMassSpectrometryAssay(MassSpectrometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003097",
        "LiquidChromatographyMassSpectrometryAssay",
    )


class MatrixAssistedLaserDesorptionIonizationImagingMassSpectrometryAssay(
    MassSpectrometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003099",
        "MatrixAssistedLaserDesorptionIonizationImagingMassSpectrometryAssay",
    )


class NanosprayDesorptionElectrosprayIonizationAssay(MassSpectrometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003101",
        "NanosprayDesorptionElectrosprayIonizationAssay",
    )


class GasChromatographyMassSpectrometryAssay(MassSpectrometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003110",
        "GasChromatographyMassSpectrometryAssay",
    )


class TandemMassSpectrometryAssay(MassSpectrometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003540", "TandemMassSpectrometryAssay"
    )


class MicrobiomeProteinExpressionProfilingAssay(ProteinExpressionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002765",
        "MicrobiomeProteinExpressionProfilingAssay",
    )


class SwathMsProteinProfilingAssay(ProteinExpressionProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002958", "SwathMsProteinProfilingAssay"
    )


class NanodropletProcessingInOnePotForTraceSamplesAssay(
    ProteinExpressionProfilingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003102",
        "NanodropletProcessingInOnePotForTraceSamplesAssay",
    )


class SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001014",
        "SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing",
    )


class SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001017",
        "SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing",
    )


class SelfReportedHandednessAssessment(HandednessAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000957", "SelfReportedHandednessAssessment"
    )


class EdinburghHandednessAssay(HandednessAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001001", "EdinburghHandednessAssay"
    )


class TranscriptionFactorBindingSiteAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000291",
        "TranscriptionFactorBindingSiteAssay",
    )


class SurfacePlasmonResonanceBindingAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000923",
        "SurfacePlasmonResonanceBindingAssay",
    )


class BindingConstantDeterminationAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001025",
        "BindingConstantDeterminationAssay",
    )


class PhageDisplayBindingAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001476", "PhageDisplayBindingAssay"
    )


class BindingAssayUsingRadioactivityDetection(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001491",
        "BindingAssayUsingRadioactivityDetection",
    )


class BindingAssayUsingFluorescenceDetection(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001499",
        "BindingAssayUsingFluorescenceDetection",
    )


class DirectBindingAssay(BindingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001591", "DirectBindingAssay")


class CompetitiveInhibitionOfBindingAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001593",
        "CompetitiveInhibitionOfBindingAssay",
    )


class CalorimetricBindingAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001634", "CalorimetricBindingAssay"
    )


class SplitUbiquitinAssay(BindingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001668", "SplitUbiquitinAssay")


class FarWesternBlotAssay(BindingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001669", "FarWesternBlotAssay")


class ElectrophoreticMobilityShiftAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001671",
        "ElectrophoreticMobilityShiftAssay",
    )


class Yeast2HybridAssay(BindingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001679", "Yeast2HybridAssay")


class SosRecruitmentAssay(BindingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001680", "SosRecruitmentAssay")


class YeastOneHybridAssay(BindingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001681", "YeastOneHybridAssay")


class BioLayerInterferometryAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002107", "BioLayerInterferometryAssay"
    )


class SystematicEvolutionOfLigandsByExponentialEnrichmentAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002161",
        "SystematicEvolutionOfLigandsByExponentialEnrichmentAssay",
    )


class Mammalian2HybridAssay(BindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002164", "Mammalian2HybridAssay"
    )


class EpitopeProtectionExperiment(EfficacyOfEpitopeInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001184", "EpitopeProtectionExperiment"
    )


class EpitopeDiseaseExacerbationExperiment(EfficacyOfEpitopeInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001188",
        "EpitopeDiseaseExacerbationExperiment",
    )


class EpitopeTreatmentExperiment(EfficacyOfEpitopeInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001190", "EpitopeTreatmentExperiment"
    )


class EpitopeToleranceInductionExperiment(EfficacyOfEpitopeInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001488",
        "EpitopeToleranceInductionExperiment",
    )


class PseudovirusEntryAssay(InfectiousAgentDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002680", "PseudovirusEntryAssay"
    )


class AutofluorescenceAssay(FluorescenceDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003087", "AutofluorescenceAssay"
    )


class ChromosomeOrganizationAssayByFluorescenceInSituHybridization(
    InSituHybridizationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001683",
        "ChromosomeOrganizationAssayByFluorescenceInSituHybridization",
    )


class TranscriptExpressionLocationDetectionByHybridizationChainReactionAssay(
    InSituHybridizationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002085",
        "TranscriptExpressionLocationDetectionByHybridizationChainReactionAssay",
    )


class FluorescenceInSituHybridizationAssay(InSituHybridizationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003094",
        "FluorescenceInSituHybridizationAssay",
    )


class ChipSeqAssay(ChipAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000716", "ChipSeqAssay")


class ChipChipAssay(ChipAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001248", "ChipChipAssay")


class CometAssay(FluorescenceDetectionAssay, CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302736", "CometAssay")


class CellCellKillingAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000882", "CellCellKillingAssay")


class CellProliferationAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000891", "CellProliferationAssay"
    )


class FlowCytometryAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000916", "FlowCytometryAssay")


class CellCellBindingDetectionByFlowCytometryAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000975",
        "CellCellBindingDetectionByFlowCytometryAssay",
    )


class CytometryTimeOfFlightAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002115", "CytometryTimeOfFlightAssay"
    )


class MixedLymphocyteReactionAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002120", "MixedLymphocyteReactionAssay"
    )


class GiemsaStainAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002647", "GiemsaStainAssay")


class FluorescenceImagingBasedApoptosisAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002946",
        "FluorescenceImagingBasedApoptosisAssay",
    )


class FluorescenceImagingBasedCellCycleStateAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002948",
        "FluorescenceImagingBasedCellCycleStateAssay",
    )


class FluorescenceImagingBasedCellViabilityAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002949",
        "FluorescenceImagingBasedCellViabilityAssay",
    )


class FluorescenceImagingBasedDrugSynergyAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002950",
        "FluorescenceImagingBasedDrugSynergyAssay",
    )


class FluorescenceImagingBasedCellMorphologyAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002951",
        "FluorescenceImagingBasedCellMorphologyAssay",
    )


class FluorescenceImagingMultiplexCytologicalProfiling(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002952",
        "FluorescenceImagingMultiplexCytologicalProfiling",
    )


class MicroenvironmentMicroarrayAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002966", "MicroenvironmentMicroarrayAssay"
    )


class MyelocyteAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003016", "MyelocyteAssay")


class MetamyelocyteAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003017", "MetamyelocyteAssay")


class HematocritAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003018", "HematocritAssay")


class PromyelocyteAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003019", "PromyelocyteAssay")


class BasophilAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003021", "BasophilAssay")


class NeutrophilAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003022", "NeutrophilAssay")


class EosinophilAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003023", "EosinophilAssay")


class LymphocyteAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003024", "LymphocyteAssay")


class MonocyteAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003025", "MonocyteAssay")


class ReticulocyteAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003026", "ReticulocyteAssay")


class MacrophageAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003027", "MacrophageAssay")


class PlateletAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003028", "PlateletAssay")


class FluorescentImmunospotAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003228", "FluorescentImmunospotAssay"
    )


class CellViabilityAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003583", "CellViabilityAssay")


class InVitroCrisprScreenAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003659", "InVitroCrisprScreenAssay"
    )


class CellDifferentiationAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003720", "CellDifferentiationAssay"
    )


class CellBasedDnaDamageAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003721", "CellBasedDnaDamageAssay"
    )


class NaturalKillerCellCountAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003722", "NaturalKillerCellCountAssay"
    )


class NaturalKillerCellPercentageAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003723", "NaturalKillerCellPercentageAssay"
    )


class SpermCountAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003724", "SpermCountAssay")


class LeukocyteCountAssay(CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100013", "LeukocyteCountAssay")


class MegakaryocyteCountAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100048", "MegakaryocyteCountAssay"
    )


class MesothelialCellCountAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100049", "MesothelialCellCountAssay"
    )


class CountBodilyFluidCellCountAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100330", "CountBodilyFluidCellCountAssay"
    )


class ManualDifferentialBodilyFluidMesothelialCellCountAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100332",
        "ManualDifferentialBodilyFluidMesothelialCellCountAssay",
    )


class BodilyFluidCellCountAssay(CytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100345", "BodilyFluidCellCountAssay"
    )


class DiseaseExacerbationInVivoInterventionExperiment(InVivoInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001981",
        "DiseaseExacerbationInVivoInterventionExperiment",
    )


class ProtectionFromChallengeInVivoInterventionExperiment(InVivoInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001982",
        "ProtectionFromChallengeInVivoInterventionExperiment",
    )


class ToleranceInductionInterventionExperiment(InVivoInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001983",
        "ToleranceInductionInterventionExperiment",
    )


class TreatmentInterventionExperiment(InVivoInterventionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001984", "TreatmentInterventionExperiment"
    )


class DnaMethylationProfilingAssay(EpigeneticModificationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000634", "DnaMethylationProfilingAssay"
    )


class GlobalChromatinProfilingByMassSpectrometryAssay(EpigeneticModificationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002961",
        "GlobalChromatinProfilingByMassSpectrometryAssay",
    )


class MicrococcalNucleaseDigestionFollowedByTilingArrayAssay(
    ArrayBasedNucleicAcidStructureMappingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002037",
        "MicrococcalNucleaseDigestionFollowedByTilingArrayAssay",
    )


class EnhancerActivityDetectionByReporterGeneAssay(ReporterGeneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002083",
        "EnhancerActivityDetectionByReporterGeneAssay",
    )


class MassivelyParallelReporterAssay(ReporterGeneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002675", "MassivelyParallelReporterAssay"
    )


class FluorescenceImagingBasedReporterGeneAssay(ReporterGeneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002960",
        "FluorescenceImagingBasedReporterGeneAssay",
    )


class OrganismalBodyTemperatureMeasurementAssay(TemperatureMeasurementAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003080",
        "OrganismalBodyTemperatureMeasurementAssay",
    )


class HydrogenDeuteriumExchangeFootprintingAssay(FootprintingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001976",
        "HydrogenDeuteriumExchangeFootprintingAssay",
    )


class DnaseFootprintingAssay(FootprintingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002163", "DnaseFootprintingAssay"
    )


class HydroxylRadicalFootprintingAssay(FootprintingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002442", "HydroxylRadicalFootprintingAssay"
    )


class MethidiumpropylEdtaIronIiFootprintingAssay(FootprintingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002443",
        "MethidiumpropylEdtaIronIiFootprintingAssay",
    )


class TissueBasedProteinLocalizationAssay(ProteinLocalizationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002166",
        "TissueBasedProteinLocalizationAssay",
    )


class SubcellularProteinLocalizationAssay(ProteinLocalizationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002167",
        "SubcellularProteinLocalizationAssay",
    )


class IntracellularElectrophysiologyRecordingAssay(ElectrophysiologyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000447",
        "IntracellularElectrophysiologyRecordingAssay",
    )


class ExtracellularElectrophysiologyRecordingAssay(ElectrophysiologyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000454",
        "ExtracellularElectrophysiologyRecordingAssay",
    )


class ChromosomeConformationCaptureAssay(NuclearLigationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002439",
        "ChromosomeConformationCaptureAssay",
    )


class MappingRnaGenomeInteractionsAssay(NuclearLigationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003314",
        "MappingRnaGenomeInteractionsAssay",
    )


class ComaSeverityAssay(PhysicalExaminationOfAnOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003035", "ComaSeverityAssay")


class FunctionalAssessmentOfIndividual(PhysicalExaminationOfAnOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003501", "FunctionalAssessmentOfIndividual"
    )


class ObservationalAssessmentOfIndividual(PhysicalExaminationOfAnOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003536",
        "ObservationalAssessmentOfIndividual",
    )


class AssayOfOrganismalBehavior(PhysicalExaminationOfAnOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003712", "AssayOfOrganismalBehavior"
    )


class OrganismDevelopmentAssay(PhysicalExaminationOfAnOrganism):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003713", "OrganismDevelopmentAssay"
    )


class ReproductiveAssay(PhysicalExaminationOfAnOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003714", "ReproductiveAssay")


class TranscriptionProfilingByRtPcrAssay(
    TranscriptionProfilingAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001361",
        "TranscriptionProfilingByRtPcrAssay",
    )


class ProximityExtensionAssay(AnalyteAssay, PolymeraseChainReactionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003113", "ProximityExtensionAssay"
    )


class ChipQpcrAssay(ChipAssay, PolymeraseChainReactionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002169", "ChipQpcrAssay")


class ChromosomeConformationCaptureOnChipAssay(
    NuclearLigationAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002458",
        "ChromosomeConformationCaptureOnChipAssay",
    )


class RealTimePolymeraseChainReactionAssay(PolymeraseChainReactionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000893",
        "RealTimePolymeraseChainReactionAssay",
    )


class RealTimeReverseTranscriptionPolymeraseChainReactionAssay(
    PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000911",
        "RealTimeReverseTranscriptionPolymeraseChainReactionAssay",
    )


class ReverseTranscriptionPolymeraseChainReactionAssay(PolymeraseChainReactionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001170",
        "ReverseTranscriptionPolymeraseChainReactionAssay",
    )


class DnaReplicationTimingByArrayAssay(PolymeraseChainReactionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001915", "DnaReplicationTimingByArrayAssay"
    )


class FluorogenicPcrAssay(PolymeraseChainReactionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003031", "FluorogenicPcrAssay")


class InsecticideResistanceByMonitoringKnownMutationsAssay(InsecticideResistanceAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002696",
        "InsecticideResistanceByMonitoringKnownMutationsAssay",
    )


class InsecticideResistanceByDetectingEnzymeActivityAssay(InsecticideResistanceAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002697",
        "InsecticideResistanceByDetectingEnzymeActivityAssay",
    )


class InsecticideResistanceBioassay(InsecticideResistanceAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002698", "InsecticideResistanceBioassay"
    )


class DnaBasedBloodMealFingerPrintingAssay(DnaFingerprintingAssay, BloodMealAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002734",
        "DnaBasedBloodMealFingerPrintingAssay",
    )


class BloodMealByCounterCurrentImmunoelectrophoresisAssay(BloodMealAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002733",
        "BloodMealByCounterCurrentImmunoelectrophoresisAssay",
    )


class FluorescenceImagingBasedProteinPhosphorylationStateAssay(ProteinStateAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002954",
        "FluorescenceImagingBasedProteinPhosphorylationStateAssay",
    )


class MassSpectrometryBasedProteinStateAssay(ProteinStateAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002955",
        "MassSpectrometryBasedProteinStateAssay",
    )


class ReversePhaseProteinArrayProfilingAssay(ProteinStateAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002957",
        "ReversePhaseProteinArrayProfilingAssay",
    )


class MultiplexBeadBasedProteinStateImmunoassay(ProteinStateAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002970",
        "MultiplexBeadBasedProteinStateImmunoassay",
    )


class KinomescanAssay(KinaseInhibitorAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002963", "KinomescanAssay")


class KinativAssay(KinaseInhibitorAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002964", "KinativAssay")


class FibrinogenConcentrationAssay(FibrinogenAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003175", "FibrinogenConcentrationAssay"
    )


class SerumNeutralizationOfViralInfectivityAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000872",
        "SerumNeutralizationOfViralInfectivityAssay",
    )


class VenousBloodTacrolimusAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100171", "VenousBloodTacrolimusAssay"
    )


class VenousBloodMycophenolicAcidAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100173", "VenousBloodMycophenolicAcidAssay"
    )


class VenousBlood25HydroxyvitaminD2Assay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100203",
        "VenousBlood25HydroxyvitaminD2Assay",
    )


class VenousBloodDigoxinAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100204", "VenousBloodDigoxinAssay"
    )


class RandomVenousBloodAmikacinAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100221", "RandomVenousBloodAmikacinAssay"
    )


class VenousBloodAmmoniaAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100222", "VenousBloodAmmoniaAssay"
    )


class VenousBloodDehydroepiandrosteroneAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100269",
        "VenousBloodDehydroepiandrosteroneAssay",
    )


class VenousBloodCortisolAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100270", "VenousBloodCortisolAssay"
    )


class VenousBloodValproicAcidAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100309", "VenousBloodValproicAcidAssay"
    )


class TotalVenousBloodHomocysteineAssay(AnalyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100369",
        "TotalVenousBloodHomocysteineAssay",
    )


class CbcWithAutomatedDifferentialVenousBloodWbcCountAssay(CytometryAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100064",
        "CbcWithAutomatedDifferentialVenousBloodWbcCountAssay",
    )


class CbcVenousBloodWbcCountAssay(CytometryAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100075", "CbcVenousBloodWbcCountAssay"
    )


class CorrectedVenousBloodLeukocyteCountAssay(CytometryAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100079",
        "CorrectedVenousBloodLeukocyteCountAssay",
    )


class CbcWithManualDifferentialVenousBloodWbcCountAssay(CytometryAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100100",
        "CbcWithManualDifferentialVenousBloodWbcCountAssay",
    )


class CbcWithManualDifferentialVenousBloodCellCountAssay(CytometryAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100124",
        "CbcWithManualDifferentialVenousBloodCellCountAssay",
    )


class CbcWithManualDifferentialVenousBloodMegakaryocyteCountAssay(
    CytometryAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100324",
        "CbcWithManualDifferentialVenousBloodMegakaryocyteCountAssay",
    )


class VenousBloodMegakaryocyteCountAssay(CytometryAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100365",
        "VenousBloodMegakaryocyteCountAssay",
    )


class VenousBloodWbcCountAssay(CytometryAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100367", "VenousBloodWbcCountAssay"
    )


class VenousBloodFerritinAssay(FerritinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100096", "VenousBloodFerritinAssay"
    )


class VenousBloodFibrinogenAssay(FibrinogenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100147", "VenousBloodFibrinogenAssay"
    )


class GlucoseToleranceTest(BloodAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000721", "GlucoseToleranceTest")


class ActivatedPartialThromboplastinTimeAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000820",
        "ActivatedPartialThromboplastinTimeAssay",
    )


class UmbilicalCordBloodAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003238", "UmbilicalCordBloodAssay"
    )


class AntibodiesFromLymphocyteSecretionsAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003296",
        "AntibodiesFromLymphocyteSecretionsAssay",
    )


class VenousBloodHemoglobinA1CAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100116", "VenousBloodHemoglobinA1CAssay"
    )


class QuantitativeVenousBloodIggAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100177", "QuantitativeVenousBloodIggAssay"
    )


class QuantitativeVenousBloodIgmAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100178", "QuantitativeVenousBloodIgmAssay"
    )


class QuantitativeVenousBloodIgaAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100179", "QuantitativeVenousBloodIgaAssay"
    )


class EstimatedVenousBloodGlomerularFiltrationAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100218",
        "EstimatedVenousBloodGlomerularFiltrationAssay",
    )


class TotalVenousBloodIgeAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100234", "TotalVenousBloodIgeAssay"
    )


class Abl90PanelArterialBloodTemperatureAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100280",
        "Abl90PanelArterialBloodTemperatureAssay",
    )


class Gem4000AnlcooxArterialBloodTemperatureAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100315",
        "Gem4000AnlcooxArterialBloodTemperatureAssay",
    )


class VenousBloodTemperatureAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100356", "VenousBloodTemperatureAssay"
    )


class Gem4ArterialBloodTemperatureAssay(BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100376",
        "Gem4ArterialBloodTemperatureAssay",
    )


class _24HourTotalUrineVolumeAssay(UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100121", "_24HourTotalUrineVolumeAssay"
    )


class Tube4CountCerebrospinalFluidCellCountAssay(
    CytometryAssay, CerebrospinalFluidAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100265",
        "Tube4CountCerebrospinalFluidCellCountAssay",
    )


class Tube1CountCerebrospinalFluidCellCountAssay(
    CytometryAssay, CerebrospinalFluidAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100268",
        "Tube1CountCerebrospinalFluidCellCountAssay",
    )


class CerebrospinalFluidMesothelialCellCountAssay(
    CytometryAssay, CerebrospinalFluidAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100392",
        "CerebrospinalFluidMesothelialCellCountAssay",
    )


class DamidSeq(DnaAdenineMethyltransferaseIdentificationAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003299", "DamidSeq")


class _5NucleotidaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003423", "_5NucleotidaseActivityLevelAssay"
    )


class AlanineAminotransferaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003424",
        "AlanineAminotransferaseActivityLevelAssay",
    )


class AlkalinePhosphataseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003425",
        "AlkalinePhosphataseActivityLevelAssay",
    )


class AmylaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003426", "AmylaseActivityLevelAssay"
    )


class AspartateAminotransferaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003427",
        "AspartateAminotransferaseActivityLevelAssay",
    )


class CholinesteraseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003428", "CholinesteraseActivityLevelAssay"
    )


class CreatineKinaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003429", "CreatineKinaseActivityLevelAssay"
    )


class GammaGlutamyltransferaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003430",
        "GammaGlutamyltransferaseActivityLevelAssay",
    )


class GlutamateDehydrogenaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003431",
        "GlutamateDehydrogenaseActivityLevelAssay",
    )


class IsocitrateDehydrogenaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003432",
        "IsocitrateDehydrogenaseActivityLevelAssay",
    )


class LactateDehydrogenaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003433",
        "LactateDehydrogenaseActivityLevelAssay",
    )


class SorbitolDehydrogenaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003434",
        "SorbitolDehydrogenaseActivityLevelAssay",
    )


class AcylCoaOxidaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003435", "AcylCoaOxidaseActivityLevelAssay"
    )


class NAcetylBetaGlucosaminidaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003436",
        "NAcetylBetaGlucosaminidaseActivityLevelAssay",
    )


class RibonucleaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003437", "RibonucleaseActivityLevelAssay"
    )


class GalactosidaseActivityLevelAssay(EnzymaticActivityLevelAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003438", "GalactosidaseActivityLevelAssay"
    )


class OrganismDetectionByPcrAssay(OrganismDetectionAssay, PolymeraseChainReactionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002740", "OrganismDetectionByPcrAssay"
    )


class BloodMicrobiologyAssay(OrganismDetectionAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002649", "BloodMicrobiologyAssay"
    )


class UrineMicrobiologyAssay(OrganismDetectionAssay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003286", "UrineMicrobiologyAssay"
    )


class CerebrospinalFluidMicrobiologyAssay(
    OrganismDetectionAssay, CerebrospinalFluidAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003240",
        "CerebrospinalFluidMicrobiologyAssay",
    )


class EndotrachealTubeAspirateMicrobiologyAssay(
    OrganismDetectionAssay, EndotrachealAspirateAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003241",
        "EndotrachealTubeAspirateMicrobiologyAssay",
    )


class InducedSputumMicrobiologyAssay(OrganismDetectionAssay, InducedSputumAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003242", "InducedSputumMicrobiologyAssay"
    )


class LungMicrobiologyAssay(OrganismDetectionAssay, LungAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003282", "LungMicrobiologyAssay"
    )


class FecesMicrobiologyAssay(OrganismDetectionAssay, FecesAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003039", "FecesMicrobiologyAssay"
    )


class OrganismSpeciesDetectionAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001624", "OrganismSpeciesDetectionAssay"
    )


class DifferentialMediumAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002489", "DifferentialMediumAssay"
    )


class PathogenDetectionAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002728", "PathogenDetectionAssay"
    )


class OrganismDetectionBySizeAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002735", "OrganismDetectionBySizeAssay"
    )


class OrganismDetectionByCrossMatingAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002736",
        "OrganismDetectionByCrossMatingAssay",
    )


class OrganismDetectionByCytologicalChromosomeExaminationAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002737",
        "OrganismDetectionByCytologicalChromosomeExaminationAssay",
    )


class OrganismDetectionByIsoenzymeElectrophoresisAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002738",
        "OrganismDetectionByIsoenzymeElectrophoresisAssay",
    )


class OrganismDetectionByMorphologicalExaminationAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002739",
        "OrganismDetectionByMorphologicalExaminationAssay",
    )


class OrganismDetectionBySpecificDnaHybridizationAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002741",
        "OrganismDetectionBySpecificDnaHybridizationAssay",
    )


class OrganismDetectionBySalinityToleranceAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002742",
        "OrganismDetectionBySalinityToleranceAssay",
    )


class ParasiteDetectionAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003038", "ParasiteDetectionAssay"
    )


class PleuralFluidMicrobiologyAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003283", "PleuralFluidMicrobiologyAssay"
    )


class NasopharyngealOrOropharyngealSwabMicrobiologyAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003285",
        "NasopharyngealOrOropharyngealSwabMicrobiologyAssay",
    )


class GramStainAssay(OrganismDetectionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003480", "GramStainAssay")


class SkinOfBodyMicrobiologyAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003576", "SkinOfBodyMicrobiologyAssay"
    )


class BoneMarrowMicrobiologyAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003578", "BoneMarrowMicrobiologyAssay"
    )


class NasalAspirateMicrobiologyAssay(OrganismDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003580", "NasalAspirateMicrobiologyAssay"
    )


class ReporterCellLineAnalyteDetectionBioassay(AnalyteAssay, CellCultureAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000904",
        "ReporterCellLineAnalyteDetectionBioassay",
    )


class EnzymeLinkedImmunospotAssay(CytometryAssay, CellCultureAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600031", "EnzymeLinkedImmunospotAssay"
    )


class GeneKnockDownAssay(CellCultureAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001672", "GeneKnockDownAssay")


class AssayForTransposaseAccessibleChromatinUsingSequencing(
    ChromatinAccessibilityAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002039",
        "AssayForTransposaseAccessibleChromatinUsingSequencing",
    )


class M6AMtaseSequencingAssay(ChromatinAccessibilityAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003687", "M6AMtaseSequencingAssay"
    )


class BloodPressureAssay(VitalSignAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003716", "BloodPressureAssay")


class PulseRateAssay(VitalSignAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003718", "PulseRateAssay")


class RespiratoryAssay(VitalSignAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003719", "RespiratoryAssay")


class ImmunoStainingAssay(AssayDetectingAMolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001632", "ImmunoStainingAssay")


class HistopathologyAssay(HistologicalAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002564", "HistopathologyAssay")


class PeriodicAcidSchiffStainingAssay(HistologicalAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003103", "PeriodicAcidSchiffStainingAssay"
    )


class _3DCellStructureDeterminationAssay(
    CytometryAssay, _3DStructureDeterminationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003122",
        "_3DCellStructureDeterminationAssay",
    )


class _3DMolecularStructureDeterminationAssay(_3DStructureDeterminationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003117",
        "_3DMolecularStructureDeterminationAssay",
    )


class CapAnalysisOfGeneExpressionAssay(
    TranscriptionProfilingAssay, PolymeraseChainReactionAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001674", "CapAnalysisOfGeneExpressionAssay"
    )


class TranscriptAnalysisByPairedEndTagSequencingAssay(
    TranscriptionProfilingAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001850",
        "TranscriptAnalysisByPairedEndTagSequencingAssay",
    )


class RnaAnnotationAndMappingOfPromotersForTheAnalysisOfGeneExpressionAssay(
    TranscriptionProfilingAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001864",
        "RnaAnnotationAndMappingOfPromotersForTheAnalysisOfGeneExpressionAssay",
    )


class RnpRibonuclearParticleImmunoprecipitationHighThroughputSequencingAssay(
    AnalyteAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001857",
        "RnpRibonuclearParticleImmunoprecipitationHighThroughputSequencingAssay",
    )


class CrossLinkingImmunoprecipitationHighThroughputSequencingAssay(
    AnalyteAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001858",
        "CrossLinkingImmunoprecipitationHighThroughputSequencingAssay",
    )


class ProteinSequencingByTandemMassSpectrometryAssay(
    MassSpectrometryAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001923",
        "ProteinSequencingByTandemMassSpectrometryAssay",
    )


class ChromatinInteractionAnalysisByPairedEndTagSequencingAssay(
    NuclearLigationAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001848",
        "ChromatinInteractionAnalysisByPairedEndTagSequencingAssay",
    )


class DnaSequencingAssay(SequencingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000626", "DnaSequencingAssay")


class EdmanDegradation(SequencingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000705", "EdmanDegradation")


class RnaSequencingAssay(SequencingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001177", "RnaSequencingAssay")


class FormaldehydeAssistedIsolationOfRegulatoryElementsAssay(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001859",
        "FormaldehydeAssistedIsolationOfRegulatoryElementsAssay",
    )


class DnaReplicationTimingBySequencingAssay(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001920",
        "DnaReplicationTimingBySequencingAssay",
    )


class TaxonomicDiversityAssessmentByTargetedGeneSurvey(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001960",
        "TaxonomicDiversityAssessmentByTargetedGeneSurvey",
    )


class TranscriptAnalysisBySingleEndSequencingAssay(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002485",
        "TranscriptAnalysisBySingleEndSequencingAssay",
    )


class AmpliconSequencingAssay(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002767", "AmpliconSequencingAssay"
    )


class TCellReceptorRepertoireSequencingAssay(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002990",
        "TCellReceptorRepertoireSequencingAssay",
    )


class BCellReceptorRepertoireSequencingAssay(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002991",
        "BCellReceptorRepertoireSequencingAssay",
    )


class SplitPoolRecognitionOfInteractionsAndTagExtensionAssay(SequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003310",
        "SplitPoolRecognitionOfInteractionsAndTagExtensionAssay",
    )


class MhcLigandAssay(ImmuneEpitopeAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002075", "MhcLigandAssay")


class BCellEpitopeAssay(ImmuneEpitopeAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003127", "BCellEpitopeAssay")


class TCellEpitopeAssay(ImmuneEpitopeAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003128", "TCellEpitopeAssay")


class VenousBloodLactateDehydrogenaseAssay(
    BloodAssay, LactateDehydrogenaseComplexAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100110",
        "VenousBloodLactateDehydrogenaseAssay",
    )


class VenousBloodLdhAssay(BloodAssay, LactateDehydrogenaseComplexAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100161", "VenousBloodLdhAssay")


class VenousBloodOsmolalityAssay(BloodAssay, OsmolalityAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100359", "VenousBloodOsmolalityAssay"
    )


class UrineOsmolalityAssay(UrineAssay, OsmolalityAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100140", "UrineOsmolalityAssay")


class BiositeCardiacPanelArterialBloodCreatineKinaseMbAssay(
    BloodAssay, CytosolicCreatineKinaseComplexMbTypeAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100146",
        "BiositeCardiacPanelArterialBloodCreatineKinaseMbAssay",
    )


class VenousBloodCreatineKinaseMbAssay(
    BloodAssay, CytosolicCreatineKinaseComplexMbTypeAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100162", "VenousBloodCreatineKinaseMbAssay"
    )


class VenousBloodLacticAcidAssay(BloodAssay, RacLacticAcidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100163", "VenousBloodLacticAcidAssay"
    )


class GemPremierBloodGasVenousBloodLacticAcidAssay(BloodAssay, RacLacticAcidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100197",
        "GemPremierBloodGasVenousBloodLacticAcidAssay",
    )


class ArterialBloodLacticAcidAssay(BloodAssay, RacLacticAcidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100202", "ArterialBloodLacticAcidAssay"
    )


class Abl90PanelArterialBloodLacticAcidAssay(BloodAssay, RacLacticAcidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100274",
        "Abl90PanelArterialBloodLacticAcidAssay",
    )


class Abl90PanelVenousBloodLacticAcidAssay(BloodAssay, RacLacticAcidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100292",
        "Abl90PanelVenousBloodLacticAcidAssay",
    )


class Gem4ArterialBloodLacticAcidAssay(BloodAssay, RacLacticAcidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100372", "Gem4ArterialBloodLacticAcidAssay"
    )


class SamplePreparationForSequencingAssay(SamplePreparationForAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001902",
        "SamplePreparationForSequencingAssay",
    )


class Xenotransplantation(Transplantation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000043", "Xenotransplantation")


class Allotransplantation(Transplantation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000057", "Allotransplantation")


class Autotransplantation(Transplantation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000171", "Autotransplantation")


class NonSpecificEnzymaticCleavage(EnzymaticCleavage):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600023", "NonSpecificEnzymaticCleavage"
    )


class SpecificEnzymaticCleavage(EnzymaticCleavage):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600050", "SpecificEnzymaticCleavage"
    )


class ProteaseCleavage(EnzymaticCleavage):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600056", "ProteaseCleavage")


class SuppressionSubtractiveHybridization(ArtificiallyInducedNucleicAcidHybridization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002447",
        "SuppressionSubtractiveHybridization",
    )


class DifferentialScreeningHybridization(ArtificiallyInducedNucleicAcidHybridization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002448",
        "DifferentialScreeningHybridization",
    )


class AddingAMaterialEntityIntoATarget(MaterialCombination):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000274", "AddingAMaterialEntityIntoATarget"
    )


class CreatingAMixtureOfMoleculesInSolution(MaterialCombination):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000685",
        "CreatingAMixtureOfMoleculesInSolution",
    )


class PoolingSpecimens(MaterialCombination):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600016", "PoolingSpecimens")


class PairedEndLibraryPreparation(LibraryPreparation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001852", "PairedEndLibraryPreparation"
    )


class SageDitagLibraryPreparation(LibraryPreparation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002028", "SageDitagLibraryPreparation"
    )


class IhcSlideStaining(Staining):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002123", "IhcSlideStaining")


class HESlideStaining(Staining):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002124", "HESlideStaining")


class CarboxyfluoresceinSuccinimidylEsterStaining(Staining):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003585",
        "CarboxyfluoresceinSuccinimidylEsterStaining",
    )


class AnnexinVStaining(Staining):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003586", "AnnexinVStaining")


class AnimalEuthanization(Killing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000919", "AnimalEuthanization")


class CellLysis(Killing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302894", "CellLysis")


class IsolationOfCellPopulation(MaterialComponentSeparation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000512", "IsolationOfCellPopulation"
    )


class Immunoprecipitation(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000690", "Immunoprecipitation")


class CellCollecting(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001483", "CellCollecting")


class Purification(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001505", "Purification")


class PlateletPoorPlasmaPreparationProcess(MaterialComponentSeparation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002775",
        "PlateletPoorPlasmaPreparationProcess",
    )


class SynaptosomePreparationProcess(MaterialComponentSeparation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003384", "SynaptosomePreparationProcess"
    )


class Extraction(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302884", "Extraction")


class Filtration(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302885", "Filtration")


class Centrifugation(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302886", "Centrifugation")


class DnaSubtraction(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302906", "DnaSubtraction")


class MaterialPortioning(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600018", "MaterialPortioning")


class Excision(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600022", "Excision")


class IsolationOfCellCultureSupernatant(MaterialComponentSeparation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600029",
        "IsolationOfCellCultureSupernatant",
    )


class Precipitation(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600034", "Precipitation")


class CellCultureSplitting(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600037", "CellCultureSplitting")


class Concentrate(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600041", "Concentrate")


class PreparativeChromatography(MaterialComponentSeparation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600046", "PreparativeChromatography"
    )


class GradientSeparation(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600051", "GradientSeparation")


class Dialysis(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600052", "Dialysis")


class Electrophoresis(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600053", "Electrophoresis")


class OrganHarvesting(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110046", "OrganHarvesting")


class BloodHarvesting(MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110095", "BloodHarvesting")


class Electroporation(CellPermeabilization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302912", "Electroporation")


class EstablishingCellLine(EstablishingCellCulture):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001867", "EstablishingCellLine")


class EstablishingPrimaryCellCulture(EstablishingCellCulture):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001878", "EstablishingPrimaryCellCulture"
    )


class RandomPrimedDnaLabeling(AdditionOfMolecularLabel):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000879", "RandomPrimedDnaLabeling"
    )


class NonSpecificLabeling(AdditionOfMolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600019", "NonSpecificLabeling")


class SpecificLabeling(AdditionOfMolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600067", "SpecificLabeling")


class GeneKnockOut(GeneticTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001148", "GeneKnockOut")


class GeneKnockIn(GeneticTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001149", "GeneKnockIn")


class ChromosomalSubstitution(GeneticTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001150", "ChromosomalSubstitution"
    )


class Transfection(GeneticTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001152", "Transfection")


class InducedMutagenesis(GeneticTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001154", "InducedMutagenesis")


class ImmortalizingCellLineTransformation(GeneticTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001907",
        "ImmortalizingCellLineTransformation",
    )


class GeneKnockdown(GeneticTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002625", "GeneKnockdown")


class DnaTransduction(GeneticTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600059", "DnaTransduction")


class PolymeraseChainReaction(EnzymaticAmplification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000415", "PolymeraseChainReaction"
    )


class ReverseTranscribedPolymeraseChainReaction(EnzymaticAmplification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000552",
        "ReverseTranscribedPolymeraseChainReaction",
    )


class LinearAmplification(EnzymaticAmplification):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001494", "LinearAmplification")


class LoopMediatedIsothermalAmplification(EnzymaticAmplification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002688",
        "LoopMediatedIsothermalAmplification",
    )


class DnaPolymeraseAmplification(EnzymaticAmplification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600049", "DnaPolymeraseAmplification"
    )


class EnzymaticDnaReplication(EnzymaticAmplification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600057", "EnzymaticDnaReplication"
    )


class NucleotideOverhangCloning(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000687", "NucleotideOverhangCloning"
    )


class RecombinationEnzymeBasedCloning(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000692", "RecombinationEnzymeBasedCloning"
    )


class RestrictionEnzymeBasedCloning(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000738", "RestrictionEnzymeBasedCloning"
    )


class RecombinantBacCloning(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000790", "RecombinantBacCloning"
    )


class RecombinantPhageCloning(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000799", "RecombinantPhageCloning"
    )


class RecombinantYacCloning(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000824", "RecombinantYacCloning"
    )


class RecombinantPlasmidCloning(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600042", "RecombinantPlasmidCloning"
    )


class VectorMediatedAmplification(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600048", "VectorMediatedAmplification"
    )


class VectorMediatedExpression(RecombinantVectorCloning):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600063", "VectorMediatedExpression"
    )


class RemotePatientAssessment(OrganismDiagnosticProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003374", "RemotePatientAssessment"
    )


class InVitroTranscriptionReconstitutionAssay(ReconstitutionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002622",
        "InVitroTranscriptionReconstitutionAssay",
    )


class AquaticArthropodSpecimenCollectionProcess(ArthropodSpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002907",
        "AquaticArthropodSpecimenCollectionProcess",
    )


class LiveArthropodSpecimenCollectionProcess(ArthropodSpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002919",
        "LiveArthropodSpecimenCollectionProcess",
    )


class ArthropodCollectionProcessWithAutomatedIdentification(
    ArthropodSpecimenCollectionProcess
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002998",
        "ArthropodCollectionProcessWithAutomatedIdentification",
    )


class GravidFemaleArthropodSpecimenCollectionProcess(
    ArthropodSpecimenCollectionProcess
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002999",
        "GravidFemaleArthropodSpecimenCollectionProcess",
    )


class RestingFlightCapableArthropodSpecimenCollectionProcess(
    ArthropodSpecimenCollectionProcess
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003000",
        "RestingFlightCapableArthropodSpecimenCollectionProcess",
    )


class Lavage(CollectingSpecimenFromOrganism, MaterialComponentSeparation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600044", "Lavage")


class Biopsy(CollectingSpecimenFromOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002650", "Biopsy")


class DoubleBlindStudyExecution(SingleBlindStudyExecution):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000793", "DoubleBlindStudyExecution"
    )


class AnticoagulantTubeStorageOfBloodSpecimen(Storage):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000819",
        "AnticoagulantTubeStorageOfBloodSpecimen",
    )


class FreezingStorage(Storage):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000915", "FreezingStorage")


class LyophilizationStorage(Storage):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000927", "LyophilizationStorage"
    )


class ParaffinStorage(Storage):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000977", "ParaffinStorage")


class AgarStabStorage(Storage):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001003", "AgarStabStorage")


class MaterialMaintenanceService(MaterialService):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001515", "MaterialMaintenanceService"
    )


class MaterialAnalysisService(MaterialService):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001547", "MaterialAnalysisService"
    )


class MaterialProcessingService(MaterialService):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001563", "MaterialProcessingService"
    )


class MaterialTransportService(MaterialService):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001580", "MaterialTransportService"
    )


class DataAnalysisService(DataService):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001529", "DataAnalysisService")


class DataStorageService(DataService):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001533", "DataStorageService")


class DataMaintenanceService(DataService):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001598", "DataMaintenanceService"
    )


class MaterialAcquisition(Acquisition):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600010", "MaterialAcquisition")


class InformationAcquisition(Acquisition):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600013", "InformationAcquisition"
    )


class SupportVectorMachine(ClassPredictionDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000700", "SupportVectorMachine")


class MultipleTestingCorrectionMethod(ErrorCorrectionDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200089", "MultipleTestingCorrectionMethod"
    )


class StudentSTTest(StatisticalHypothesisTest):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000739", "StudentSTTest")


class FisherSExactTest(StatisticalHypothesisTest):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200176", "FisherSExactTest")


class ChiSquareTest(StatisticalHypothesisTest):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200200", "ChiSquareTest")


class Anova(StatisticalHypothesisTest):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200201", "Anova")


class Cart(DecisionTreeBuildingDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000749", "Cart")


class DataVectorReductionDataTransformation(DecisionTreeBuildingDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200182",
        "DataVectorReductionDataTransformation",
    )


class AdapterSequenceTrimming(SequenceTrimming):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002565", "AdapterSequenceTrimming"
    )


class RawMagneticResonanceImageDataSetReconstruction(ImageDataSetAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003356",
        "RawMagneticResonanceImageDataSetReconstruction",
    )


class ExpectationMaximization(ProbabilisticAlgorithm):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200053", "ExpectationMaximization"
    )


class LogisticLogCurveFitting(CurveFittingDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200002", "LogisticLogCurveFitting"
    )


class LogitLogCurveFitting(CurveFittingDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200003", "LogitLogCurveFitting")


class LogLogCurveFitting(CurveFittingDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200004", "LogLogCurveFitting")


class LoessFitting(CurveFittingDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200116", "LoessFitting")


class ModularDecomposition(NetworkAnalysis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200040", "ModularDecomposition")


class EdgeWeighting(NetworkAnalysis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200070", "EdgeWeighting")


class NetworkGraphConstruction(NetworkAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200126", "NetworkGraphConstruction"
    )


class NodeQualityCalculation(NetworkAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200129", "NodeQualityCalculation"
    )


class EdgeQualityCalculation(NetworkAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200135", "EdgeQualityCalculation"
    )


class NetworkSubgraphQualityCalculation(NetworkAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200137",
        "NetworkSubgraphQualityCalculation",
    )


class NetworkGraphQualityCalculation(NetworkAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200147", "NetworkGraphQualityCalculation"
    )


class TandemMassSpectrometryAnalysis(MassSpectrometryAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003647", "TandemMassSpectrometryAnalysis"
    )


class LiquidChromatrographyMassSpectrometryAnalysis(MassSpectrometryAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003648",
        "LiquidChromatrographyMassSpectrometryAnalysis",
    )


class ContinuumMassSpectrumAnalysis(MassSpectrometryAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200062", "ContinuumMassSpectrumAnalysis"
    )


class CharacteristicPathLengthCalculation(MassSpectrometryAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200063",
        "CharacteristicPathLengthCalculation",
    )


class CentroidMassSpectrumAnalysis(MassSpectrometryAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200064", "CentroidMassSpectrumAnalysis"
    )


class GasChromatographyMassSpectrometry(MassSpectrometryAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200199",
        "GasChromatographyMassSpectrometry",
    )


class HomogeneousPolynomialTransformation(PolynomialTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200020",
        "HomogeneousPolynomialTransformation",
    )


class MultipleLinearRegressionAnalysis(RegressionAnalysisMethod):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200103", "MultipleLinearRegressionAnalysis"
    )


class PartialLeastSquareRegressionAnalysis(RegressionAnalysisMethod):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200105",
        "PartialLeastSquareRegressionAnalysis",
    )


class PartialLeastSquareDiscriminantAnalysis(DiscriminantAnalysis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200107",
        "PartialLeastSquareDiscriminantAnalysis",
    )


class LogBase(MathematicalFeature):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200141", "LogBase")


class ExponentialBase(MathematicalFeature):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200151", "ExponentialBase")


class PolynomialDegree(MathematicalFeature):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200152", "PolynomialDegree")


class NumberOfVariables(MathematicalFeature):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200153", "NumberOfVariables")


class BiexponentialTransformation(
    CurveFittingDataTransformation, NormalizationDataTransformation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200006", "BiexponentialTransformation"
    )


class LowessTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001477", "LowessTransformation")


class BoxCoxTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200007", "BoxCoxTransformation")


class HyperlogTransformation(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200008", "HyperlogTransformation"
    )


class LogicalTransformation(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200011", "LogicalTransformation"
    )


class SineTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200016", "SineTransformation")


class CosineTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200017", "CosineTransformation")


class LinlogTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200021", "LinlogTransformation")


class VarianceStabilizingTransformation(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200022",
        "VarianceStabilizingTransformation",
    )


class TotalIntensityTransformationSingle(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200026",
        "TotalIntensityTransformationSingle",
    )


class TotalIntensityTransformationPaired(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200027",
        "TotalIntensityTransformationPaired",
    )


class MeanCentering(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200029", "MeanCentering")


class MedianCentering(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200030", "MedianCentering")


class ParetoScaling(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200037", "ParetoScaling")


class ReplicateAnalysis(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200057", "ReplicateAnalysis")


class LoessTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200071", "LoessTransformation")


class LogarithmicTransformation(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200094", "LogarithmicTransformation"
    )


class ExponentialTransformation(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200095", "ExponentialTransformation"
    )


class SoftIndependentModelingOfClassAnalogyAnalysis(NormalizationDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200098",
        "SoftIndependentModelingOfClassAnalogyAnalysis",
    )


class EhTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200108", "EhTransformation")


class BTransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200109", "BTransformation")


class STransformation(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200110", "STransformation")


class UnitVarianceScaling(NormalizationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200149", "UnitVarianceScaling")


class MovingAverage(AveragingDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200056", "MovingAverage")


class CanonicalVariateAnalysis(DiscriminantAnalysis, PartitioningDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200100", "CanonicalVariateAnalysis"
    )


class StatisticalModelValidation(PartitioningDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000792", "StatisticalModelValidation"
    )


class DiscriminantFunctionAnalysis(
    ClassPredictionDataTransformation,
    DiscriminantAnalysis,
    ClassDiscoveryDataTransformation,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200099", "DiscriminantFunctionAnalysis"
    )


class LinearDiscriminantFunctionalAnalysis(
    ClassPredictionDataTransformation,
    DiscriminantAnalysis,
    ClassDiscoveryDataTransformation,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200101",
        "LinearDiscriminantFunctionalAnalysis",
    )


class SimilarityCalculation(
    ClassPredictionDataTransformation, ClassDiscoveryDataTransformation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200113", "SimilarityCalculation"
    )


class PrincipalComponentRegression(
    RegressionAnalysisMethod, ClassDiscoveryDataTransformation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200104", "PrincipalComponentRegression"
    )


class KNearestNeighbors(
    PartitioningDataTransformation, ClassDiscoveryDataTransformation
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000727", "KNearestNeighbors")


class KMeansClustering(
    PartitioningDataTransformation, ClassDiscoveryDataTransformation
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200041", "KMeansClustering")


class SelfOrganizingMap(ClassDiscoveryDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000701", "SelfOrganizingMap")


class HierarchicalClustering(ClassDiscoveryDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200042", "HierarchicalClustering"
    )


class DimensionalityReduction(ClassDiscoveryDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200050", "DimensionalityReduction"
    )


class QuantileTransformation(
    NormalizationDataTransformation, CenterCalculationDataTransformation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200028", "QuantileTransformation"
    )


class VarianceCalculation(
    SpreadCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200120", "VarianceCalculation")


class StandardDeviationCalculation(
    SpreadCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200121", "StandardDeviationCalculation"
    )


class InterquartileRangeCalculation(
    SpreadCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200122", "InterquartileRangeCalculation"
    )


class KurtosisCalculation(
    SpreadCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200124", "KurtosisCalculation")


class ArithmeticMeanCalculation(
    AveragingDataTransformation,
    CenterCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200079", "ArithmeticMeanCalculation"
    )


class GeometricMeanCalculation(
    CenterCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200001", "GeometricMeanCalculation"
    )


class ModeCalculation(
    CenterCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200117", "ModeCalculation")


class MedianCalculation(
    CenterCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200119", "MedianCalculation")


class SkewnessCalculation(
    CenterCalculationDataTransformation,
    DescriptiveStatisticalCalculationDataTransformation,
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200123", "SkewnessCalculation")


class QuantileCalculation(DescriptiveStatisticalCalculationDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200118", "QuantileCalculation")


class LoessScaleGroupTransformation(ScalingDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200025", "LoessScaleGroupTransformation"
    )


class SequenceLibraryDataDemultiplexing(SequenceAnalysisDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001966",
        "SequenceLibraryDataDemultiplexing",
    )


class SequenceAlignment(SequenceAnalysisDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002567", "SequenceAlignment")


class SequenceDataFeatureCountTabulation(SequenceAnalysisDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002568",
        "SequenceDataFeatureCountTabulation",
    )


class BCellEpitopePrediction(SequenceAnalysisDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200058", "BCellEpitopePrediction"
    )


class MhcBindingPrediction(SequenceAnalysisDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200059", "MhcBindingPrediction")


class TCellEpitopePrediction(SequenceAnalysisDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200060", "TCellEpitopePrediction"
    )


class KaplanMeier(SurvivalAnalysisDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200088", "KaplanMeier")


class ProportionalHazardsModelEstimation(SurvivalAnalysisDataTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200195",
        "ProportionalHazardsModelEstimation",
    )


class Insulin(Peptide):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_145810", "Insulin")


class Vancomycin(Peptide):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_28001", "Vancomycin")


class SyntheticPeptide(Peptide, ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100065", "SyntheticPeptide")


class Protein(Peptide):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000000001", "Protein")


class DeoxyribonucleicAcid(NucleicAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_16991", "DeoxyribonucleicAcid")


class RibonucleicAcid(NucleicAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_33697", "RibonucleicAcid")


class CloningVector(NucleicAcid, ProcessedMaterial, MaterialToBeAdded):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000737", "CloningVector")


class NucleicAcidRestrictionEnzymeDigest(NucleicAcid, ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000742",
        "NucleicAcidRestrictionEnzymeDigest",
    )


class GeneticMaterial(NucleicAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001868", "GeneticMaterial")


class OligonucleotidePrimerSet(NucleicAcid, ProcessedMaterial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003030", "OligonucleotidePrimerSet"
    )


class HighDensityLipoprotein(Lipoprotein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_39025", "HighDensityLipoprotein"
    )


class LowDensityLipoprotein(Lipoprotein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_39026", "LowDensityLipoprotein"
    )


class VeryLowDensityLipoprotein(Lipoprotein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_39027", "VeryLowDensityLipoprotein"
    )


class BandFormNeutrophil(Neutrophil):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000560", "BandFormNeutrophil")


class ImmatureNeutrophil(Neutrophil):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000776", "ImmatureNeutrophil")


class SegmentedNeutrophilOfBoneMarrow(Neutrophil):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CL_0011114", "SegmentedNeutrophilOfBoneMarrow"
    )


class TCell(Lymphocyte):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000084", "TCell")


class BCell(Lymphocyte):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000236", "BCell")


class NaturalKillerCell(Lymphocyte):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000623", "NaturalKillerCell")


class CattleMhcClassIProteinComplex(MhcClassIProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001434", "CattleMhcClassIProteinComplex"
    )


class HumanMhcClassIProteinComplex(MhcClassIProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001454", "HumanMhcClassIProteinComplex"
    )


class MouseMhcClassIProteinComplex(MhcClassIProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001460", "MouseMhcClassIProteinComplex"
    )


class PigMhcClassIProteinComplex(MhcClassIProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001465", "PigMhcClassIProteinComplex"
    )


class RatMhcClassIProteinComplex(MhcClassIProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001790", "RatMhcClassIProteinComplex"
    )


class CattleMhcClassIiProteinComplex(MhcClassIiProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001435", "CattleMhcClassIiProteinComplex"
    )


class HumanMhcClassIiProteinComplex(MhcClassIiProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001455", "HumanMhcClassIiProteinComplex"
    )


class MouseMhcClassIiProteinComplex(MhcClassIiProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001461", "MouseMhcClassIiProteinComplex"
    )


class RatMhcClassIiProteinComplexWithRt1AHaplotype(MhcClassIiProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001793",
        "RatMhcClassIiProteinComplexWithRt1AHaplotype",
    )


class PrimaryCulturedCell(CulturedCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000001", "PrimaryCulturedCell")


class SecondaryCulturedCell(CulturedCell):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001866", "SecondaryCulturedCell"
    )


class VacuumAssistedBiopsyNeedle(Needle):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002679", "VacuumAssistedBiopsyNeedle"
    )


class BrukerMatchTubeHolderSystem(NmrSampleHolder):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000612", "BrukerMatchTubeHolderSystem"
    )


class BrukerAutocleanSystem(NmrTubeWashingSystem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000475", "BrukerAutocleanSystem"
    )


class TecmagNmrConsole(NmrConsole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000599", "TecmagNmrConsole")


class BrukerNmrMagnet(NmrMagnet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000597", "BrukerNmrMagnet")


class BrukerAutosampler(Autosampler):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000464", "BrukerAutosampler")


class MassSpectrometer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000049", "MassSpectrometer")


class GammaCounter(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000059", "GammaCounter")


class IonDetector(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000364", "IonDetector")


class ImageCreationDevice(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000398", "ImageCreationDevice")


class ColumnChromatographyDetector(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000463", "ColumnChromatographyDetector"
    )


class VariableWavelengthDetector(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000501", "VariableWavelengthDetector"
    )


class MultipleWavelengthDetector(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000505", "MultipleWavelengthDetector"
    )


class NmrProbe(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000516", "NmrProbe")


class EvaporativeLightScatteringDetector(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000547",
        "EvaporativeLightScatteringDetector",
    )


class FluoresceneDetector(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000563", "FluoresceneDetector")


class ElectricalConductivityDetector(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000565", "ElectricalConductivityDetector"
    )


class NmrInstrument(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000566", "NmrInstrument")


class RefractiveIndexDetector(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000583", "RefractiveIndexDetector"
    )


class PulsedAmperometricDetector(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000595", "PulsedAmperometricDetector"
    )


class Glucometer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000795", "Glucometer")


class MicroElectrode(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000816", "MicroElectrode")


class SysmexCa6000CoagulationAnalyzer(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000843", "SysmexCa6000CoagulationAnalyzer"
    )


class Calorimeter(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000930", "Calorimeter")


class Oscilloscope(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000948", "Oscilloscope")


class Angiograph(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001044", "Angiograph")


class PhMeter(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001047", "PhMeter")


class MicroplateReader(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001058", "MicroplateReader")


class Densitometer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001062", "Densitometer")


class ScintillationCounter(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001070", "ScintillationCounter")


class PatchClampDevice(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001080", "PatchClampDevice")


class RadiationMeasurementDevice(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001086", "RadiationMeasurementDevice"
    )


class MicrohardnessTester(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001089", "MicrohardnessTester")


class CoagulationAnalyzer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001095", "CoagulationAnalyzer")


class NucleicAcidSequencer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001108", "NucleicAcidSequencer")


class MultichannelPipette(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001118", "MultichannelPipette")


class Diffractometer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001122", "Diffractometer")


class Micropipette(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001128", "Micropipette")


class VoltageClampDevice(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001129", "VoltageClampDevice")


class Balance(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001135", "Balance")


class SurfacePlasmonResonanceInstrument(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001136",
        "SurfacePlasmonResonanceInstrument",
    )


class ProteinSequencer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001137", "ProteinSequencer")


class InfraredGasAnalyzer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003708", "InfraredGasAnalyzer")


class DifferentialPressureGauge(MeasurementDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400032", "DifferentialPressureGauge"
    )


class Photodetector(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400082", "Photodetector")


class DnaSequencer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400103", "DnaSequencer")


class Spectrophotometer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400115", "Spectrophotometer")


class Cytometer(MeasurementDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400137", "Cytometer")


class LiquidChromatographyMassSpectrometryPlatform(
    MeasurementDevice, MaterialSeparationDevice
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000051",
        "LiquidChromatographyMassSpectrometryPlatform",
    )


class MassAnalyzer(MeasurementDevice, MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000345", "MassAnalyzer")


class Centrifuge(MeasurementDevice, MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400106", "Centrifuge")


class ChromatographyColumn(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000038", "ChromatographyColumn")


class FilterPaper(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000151", "FilterPaper")


class ChromatographyInstrument(MaterialSeparationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000485", "ChromatographyInstrument"
    )


class RapidResolutionColumn(MaterialSeparationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000493", "RapidResolutionColumn"
    )


class Vibrotome(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000959", "Vibrotome")


class ElectrophoresisSystem(MaterialSeparationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001053", "ElectrophoresisSystem"
    )


class ProteinSeparationApparatus(MaterialSeparationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001082", "ProteinSeparationApparatus"
    )


class NucleicAcidExtractionPurificationInstrument(MaterialSeparationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001114",
        "NucleicAcidExtractionPurificationInstrument",
    )


class DenaturingHighPerformanceLiquidChromatographyInstrument(MaterialSeparationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001133",
        "DenaturingHighPerformanceLiquidChromatographyInstrument",
    )


class Microraft(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002487", "Microraft")


class ObscurationBar(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400078", "ObscurationBar")


class OpticalFilter(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400079", "OpticalFilter")


class DropletSorter(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400153", "DropletSorter")


class Microtome(MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400168", "Microtome")


class PhotomultiplierTube(MeasurementDevice, Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400084", "PhotomultiplierTube")


class SupernatantCollectionSystemHarvestingFrame(Container):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000146",
        "SupernatantCollectionSystemHarvestingFrame",
    )


class MicrotiterPlate(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000192", "MicrotiterPlate")


class Vial(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000522", "Vial")


class SpecimenContainer(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002088", "SpecimenContainer")


class GlassBottle(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002681", "GlassBottle")


class FlowCell(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400043", "FlowCell")


class SyringePump(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400100", "SyringePump")


class WasteTank(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400102", "WasteTank")


class AnimalCage(Container):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400171", "AnimalCage")


class LightSource(LightEmissionDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400065", "LightSource")


class Homogenizer(PerturbationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400109", "Homogenizer")


class Sonicator(PerturbationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400114", "Sonicator")


class Vortexer(PerturbationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400118", "Vortexer")


class FluidPressureRegulator(MeasurementDevice, EnvironmentalControlDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400045", "FluidPressureRegulator"
    )


class Cryostat(Container, EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001072", "Cryostat")


class ParaffinOven(Container, EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001111", "ParaffinOven")


class VacuumOven(Container, EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001130", "VacuumOven")


class ContainerWithEnvironmentalControl(Container, EnvironmentalControlDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002089",
        "ContainerWithEnvironmentalControl",
    )


class MolecularCrosslinker(LightEmissionDevice, EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400121", "MolecularCrosslinker")


class MicroarrayPlatform(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000052", "MicroarrayPlatform")


class Incubator(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000136", "Incubator")


class VibrationIsolationTable(EnvironmentalControlDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000945", "VibrationIsolationTable"
    )


class FaradayCage(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001002", "FaradayCage")


class Bioreactor(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001046", "Bioreactor")


class Autoclave(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001112", "Autoclave")


class SlideWarmer(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001131", "SlideWarmer")


class HeatingBlock(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400108", "HeatingBlock")


class HybridizationStation(EnvironmentalControlDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400111", "HybridizationStation")


class OligonucleotideSynthesizer(EnvironmentalControlDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400113", "OligonucleotideSynthesizer"
    )


class MicroarrayWashStation(EnvironmentalControlDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400119", "MicroarrayWashStation"
    )


class LeicaPelorisRapidTissueProcessor(AutomaticTissueProcessor):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002192", "LeicaPelorisRapidTissueProcessor"
    )


class ElisaMicroplateWasher(MicroplateWasher):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001115", "ElisaMicroplateWasher"
    )


class IlluminaBeadchip(AssayArray):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001869", "IlluminaBeadchip")


class NcounterHumanMirnaExpressionArray(AssayArray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002013",
        "NcounterHumanMirnaExpressionArray",
    )


class NcounterMouseMirnaExpressionArray(AssayArray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002570",
        "NcounterMouseMirnaExpressionArray",
    )


class Microarray(AssayArray):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400147", "Microarray")


class SakuraLowProfileAccuEdgeMicrotomeBlade(MicrotomeBlade):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002196",
        "SakuraLowProfileAccuEdgeMicrotomeBlade",
    )


class FaceMask(PersonalProtectiveDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002787", "FaceMask")


class FaceShield(PersonalProtectiveDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002791", "FaceShield")


class PersonalProtectiveClothingItem(PersonalProtectiveDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002800", "PersonalProtectiveClothingItem"
    )


class SpecimenPad(SpecimenCollectionDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002819", "SpecimenPad")


class SpecimenCollectionSwabStick(SpecimenCollectionDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002820", "SpecimenCollectionSwabStick"
    )


class DragSwab(SpecimenCollectionDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002822", "DragSwab")


class SurfaceWipe(SpecimenCollectionDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002824", "SurfaceWipe")


class BaitedNetTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002922", "BaitedNetTrap")


class BarrierTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002923", "BarrierTrap")


class BgSentinelTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002925", "BgSentinelTrap")


class GravidTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002929", "GravidTrap")


class LightTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002930", "LightTrap")


class MosquitoMagnetProTrap(ArthropodTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002933", "MosquitoMagnetProTrap"
    )


class OnderstepoortVeterinaryInstituteLightSuctionTrap(ArthropodTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002936",
        "OnderstepoortVeterinaryInstituteLightSuctionTrap",
    )


class OutletWindowTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002937", "OutletWindowTrap")


class Ovitrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002938", "Ovitrap")


class RestingArthropodTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002939", "RestingArthropodTrap")


class ShannonTrap(ArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002942", "ShannonTrap")


class ArthropodTrapContainingSmallNonHumanAnimalBait(ArthropodTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003007",
        "ArthropodTrapContainingSmallNonHumanAnimalBait",
    )


class TrapForEmergingAdultArthropods(ArthropodTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003008", "TrapForEmergingAdultArthropods"
    )


class FreeStandingWindowTrap(ArthropodTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003046", "FreeStandingWindowTrap"
    )


class MosquitoMagnetLibertyPlusTrap(ArthropodTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003454", "MosquitoMagnetLibertyPlusTrap"
    )


class ScrubTyphusDetectIgmElisaKit(AssayKit):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003489", "ScrubTyphusDetectIgmElisaKit"
    )


class PanbioDengueIgmCaptureElisaKit(AssayKit):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003490", "PanbioDengueIgmCaptureElisaKit"
    )


class PanbioDengueEarlyElisaKit(AssayKit):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003491", "PanbioDengueEarlyElisaKit"
    )


class SdBiolineChikungunyaIgmRdtKit(AssayKit):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003492", "SdBiolineChikungunyaIgmRdtKit"
    )


class SdBiolineChikungunyaIgmCaptureElisaKit(AssayKit):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003493",
        "SdBiolineChikungunyaIgmCaptureElisaKit",
    )


class AdvantageChikungunyaIgmCardKit(AssayKit):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003494", "AdvantageChikungunyaIgmCardKit"
    )


class LogarithmicVoltageAmplifier(VoltageAmplifier):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400066", "LogarithmicVoltageAmplifier"
    )


class Preamplifier(VoltageAmplifier):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400087", "Preamplifier")


class AcquisitionComputer(Computer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000636", "AcquisitionComputer")


class ComputerCluster(Computer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001092", "ComputerCluster")


class LiquidExtractionRobot(LiquidHandler):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001097", "LiquidExtractionRobot"
    )


class TransgenicOrganism(GeneticallyModifiedOrganism):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1000048", "TransgenicOrganism")


class Biotin(MolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_15956", "Biotin")


class FluoresceinLactoneForm(MolecularLabel):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHEBI_31624", "FluoresceinLactoneForm"
    )


class Cy3Dye(MolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_37987", "Cy3Dye")


class Cy5Dye(MolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_37989", "Cy5Dye")


class Digoxigenin(MolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_42098", "Digoxigenin")


class AlexaFluor532(MolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_51756", "AlexaFluor532")


class AlexaFluor546(MolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_51760", "AlexaFluor546")


class AlexaFluor555(MolecularLabel):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_52673", "AlexaFluor555")


class CulturedPbmcCellPopulation(CulturedImmuneCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110044", "CulturedPbmcCellPopulation"
    )


class CulturedCd3TCellPopulation(CulturedImmuneCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110047", "CulturedCd3TCellPopulation"
    )


class CulturedCd3TCellPopulation(CulturedImmuneCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110048", "CulturedCd3TCellPopulation"
    )


class CulturedCd4TCellPopulation(CulturedImmuneCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110050", "CulturedCd4TCellPopulation"
    )


class CulturedCd8TCellPopulation(CulturedImmuneCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110051", "CulturedCd8TCellPopulation"
    )


class CulturedAntigenPresentingCellPopulation(CulturedImmuneCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110106",
        "CulturedAntigenPresentingCellPopulation",
    )


class CulturedEffectorTCellPopulation(CulturedImmuneCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110107", "CulturedEffectorTCellPopulation"
    )


class CellLine(SecondaryCulturedCellPopulation):
    term = RdfTerm("http://purl.obolibrary.org/obo/CLO_0000031", "CellLine")


class Kitrinoviricota(Riboviria):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_2732406", "Kitrinoviricota"
    )


class Revtraviricetes(Riboviria):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_2732514", "Revtraviricetes"
    )


class Cytomegalovirus(Orthoherpesviridae):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_10358", "Cytomegalovirus")


class HumanGammaherpesvirus4(Orthoherpesviridae):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_10376", "HumanGammaherpesvirus4"
    )


class Metazoa(Opisthokonta):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_33208", "Metazoa")


class Ascomycota(Opisthokonta):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_4890", "Ascomycota")


class PlasmodiumGametocyte(Plasmodium):
    term = RdfTerm("http://purl.obolibrary.org/obo/OPL_0000267", "PlasmodiumGametocyte")


class LabeledNucleicAcidExtract(LabeledSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001143", "LabeledNucleicAcidExtract"
    )


class RnaExtract(NucleicAcidExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000880", "RnaExtract")


class DnaExtract(NucleicAcidExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001051", "DnaExtract")


class FixedTissueSlideSpecimen(FixedTissueSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OMIABIS_0000052", "FixedTissueSlideSpecimen"
    )


class FfpeSpecimen(ParaffinSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1200000", "FfpeSpecimen")


class NasalLavageFluid(LavageFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003595", "NasalLavageFluid")


class OralLavageFluid(LavageFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003667", "OralLavageFluid")


class BronchialAlveolarLavage(LavageFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0100067", "BronchialAlveolarLavage"
    )


class LymphNodeCellSpecimen(ProcessedSpecimen, CellSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110041", "LymphNodeCellSpecimen"
    )


class SplenocyteSpecimen(ProcessedSpecimen, CellSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110116", "SplenocyteSpecimen")


class SingleCellSpecimen(CellSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002127", "SingleCellSpecimen")


class ErythrocyteSpecimen(CellSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000016", "ErythrocyteSpecimen")


class ReticulocyteSpecimen(CellSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000017", "ReticulocyteSpecimen")


class LeukocyteSpecimen(CellSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000018", "LeukocyteSpecimen")


class PreMortemSpecimen(SpecimenWithPreOrPostMortemStatus):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000873", "PreMortemSpecimen")


class PostMortemSpecimen(SpecimenWithPreOrPostMortemStatus):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000902", "PostMortemSpecimen")


class FecalSwabSpecimen(FecesSpecimen, SwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002612", "FecalSwabSpecimen")


class MeconiumSpecimen(FecesSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000011", "MeconiumSpecimen")


class ChorionicVillusSpecimen(PlacentaSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000010", "ChorionicVillusSpecimen"
    )


class CerebralCortexSpecimen(BrainSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002536", "CerebralCortexSpecimen"
    )


class CerebellumSpecimen(BrainSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002538", "CerebellumSpecimen")


class BreastSwabSpecimen(BreastSpecimen, SwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002604", "BreastSwabSpecimen")


class SuprapubicSkinSpecimen(SkinOfBodySpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002551", "SuprapubicSkinSpecimen"
    )


class UterineCervixSpecimen(UterusSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000000", "UterineCervixSpecimen"
    )


class VaginaSwabSpecimen(VaginaSpecimen, SwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002611", "VaginaSwabSpecimen")


class StomachSpecimen(DigestiveTractSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002528", "StomachSpecimen")


class EsophagusMucosaSpecimen(DigestiveTractSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002532", "EsophagusMucosaSpecimen"
    )


class ColonSpecimen(DigestiveTractSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002533", "ColonSpecimen")


class EsophagusMuscularisMucosaSpecimen(DigestiveTractSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002535",
        "EsophagusMuscularisMucosaSpecimen",
    )


class EsophagogastricJunctionSpecimen(DigestiveTractSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002544", "EsophagogastricJunctionSpecimen"
    )


class IleumSpecimen(DigestiveTractSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002545", "IleumSpecimen")


class SigmoidColonSpecimen(DigestiveTractSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002550", "SigmoidColonSpecimen")


class RectalSwabSpecimen(DigestiveTractSpecimen, SwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002609", "RectalSwabSpecimen")


class VitreousHumorSpecimen(EyeSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002511", "VitreousHumorSpecimen"
    )


class LowerRespiratoryTractSpecimen(RespiratorySystemSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002783", "LowerRespiratoryTractSpecimen"
    )


class UpperRespiratoryTractSpecimen(RespiratorySystemSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000006", "UpperRespiratoryTractSpecimen"
    )


class UrineSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000651", "UrineSpecimen")


class BloodSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000655", "BloodSpecimen")


class AmnioticFluidSpecimen(BodilyFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002500", "AmnioticFluidSpecimen"
    )


class CerebrospinalFluidSpecimen(BodilyFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002502", "CerebrospinalFluidSpecimen"
    )


class DigestiveSystemFluidOrSecretionSpecimen(BodilyFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002504",
        "DigestiveSystemFluidOrSecretionSpecimen",
    )


class MilkSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002505", "MilkSpecimen")


class PericardialFluidSpecimen(BodilyFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002506", "PericardialFluidSpecimen"
    )


class SalivaSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002507", "SalivaSpecimen")


class SputumSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002508", "SputumSpecimen")


class SweatSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002509", "SweatSpecimen")


class SynovialFluidSpecimen(BodilyFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002510", "SynovialFluidSpecimen"
    )


class PeritonealFluidSpecimen(BodilyFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002514", "PeritonealFluidSpecimen"
    )


class PleuralFluidSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002515", "PleuralFluidSpecimen")


class LymphSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003482", "LymphSpecimen")


class CervicalMucusSpecimen(BodilyFluidSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000002", "CervicalMucusSpecimen"
    )


class SemenSpecimen(BodilyFluidSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000008", "SemenSpecimen")


class CheekSwabSpecimen(OralSwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002605", "CheekSwabSpecimen")


class TongueSwabSpecimen(OralSwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002610", "TongueSwabSpecimen")


class Meconium(Feces):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0007109", "Meconium")


class Blood(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000178", "Blood")


class CervicalMucus(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0000316", "CervicalMucus")


class PleuralFluid(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001087", "PleuralFluid")


class Sweat(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001089", "Sweat")


class SynovialFluid(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001090", "SynovialFluid")


class PeritonealFluid(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001268", "PeritonealFluid")


class CerebrospinalFluid(BodilyFluid):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0001359", "CerebrospinalFluid"
    )


class Milk(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001913", "Milk")


class Bile(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001970", "Bile")


class Lymph(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002391", "Lymph")


class PericardialFluid(BodilyFluid):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0002409", "PericardialFluid")


class Sputum(RespiratorySystemFluidSecretion):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0007311", "Sputum")


class SkinEpidermis(Epithelium):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0001003", "SkinEpidermis")


class OmentalFatPad(AdiposeTissue):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0010414", "OmentalFatPad")


class ContainingASpecimenFunction(ContainFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002087", "ContainingASpecimenFunction"
    )


class FilterFunction(MaterialSeparationFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000378", "FilterFunction")


class SortFunction(MaterialSeparationFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000403", "SortFunction")


class LightEmissionFunction(ExcitationFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000367", "LightEmissionFunction"
    )


class PumpFunction(TransferFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001042", "PumpFunction")


class CellTransferFunction(TransferFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001043", "CellTransferFunction")


class ElectricitySupplyFunction(EnergySupplyFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000384", "ElectricitySupplyFunction"
    )


class SignalConversionFunction(InformationProcessorFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000393", "SignalConversionFunction"
    )


class DisplayFunction(InformationProcessorFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000400", "DisplayFunction")


class ImageAcquisitionFunction(MeasureFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000397", "ImageAcquisitionFunction"
    )


class AdditionOfMolecularTracerFunction(ReagentApplicationFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000961",
        "AdditionOfMolecularTracerFunction",
    )


class EffectorTCellFunction(AdaptiveImmuneEffectorFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110084", "EffectorTCellFunction"
    )


class RoleOfRegulatorOfChemicalManufacturer(RegulatorRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000089",
        "RoleOfRegulatorOfChemicalManufacturer",
    )


class RoleOfInstitutionalReviewBoard(RegulatorRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000154", "RoleOfInstitutionalReviewBoard"
    )


class RoleOfRegulatorOfConsumablesAndMedicalDevices(RegulatorRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000273",
        "RoleOfRegulatorOfConsumablesAndMedicalDevices",
    )


class RoleOfCertifiedIrbProfessional(RegulationAssignedRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000092", "RoleOfCertifiedIrbProfessional"
    )


class RoleOfImpartialWitness(RegulationAssignedRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000196", "RoleOfImpartialWitness"
    )


class RoleOfLegallyAcceptableRepresentative(RegulationAssignedRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000215",
        "RoleOfLegallyAcceptableRepresentative",
    )


class CompetitiveBindingReferenceLigandRole(PositiveReferenceSubstanceRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001955",
        "CompetitiveBindingReferenceLigandRole",
    )


class PlaceboRole(NegativeReferenceSubstanceRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000169", "PlaceboRole")


class BaselineParticipantRole(ReferenceSubjectRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000143", "BaselineParticipantRole"
    )


class CrossoverPopulationRole(ReferenceSubjectRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000161", "CrossoverPopulationRole"
    )


class BiologicalReplicateRole(ReferenceSubjectRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000198", "BiologicalReplicateRole"
    )


class TechnicalReplicateRole(ReferenceSubjectRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000249", "TechnicalReplicateRole"
    )


class SequenceAnnotationReportingRole(ReportingPartyRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001949", "SequenceAnnotationReportingRole"
    )


class TrialMonitorRole(ResponsiblePartyRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000060", "TrialMonitorRole")


class PrincipalInvestigatorRole(ResponsiblePartyRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000103", "PrincipalInvestigatorRole"
    )


class SponsorRole(ResponsiblePartyRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000243", "SponsorRole")


class ContractResearchOrganizationRole(WorkerRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000020", "ContractResearchOrganizationRole"
    )


class ClinicalResearchCoordinatorRole(WorkerRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000032", "ClinicalResearchCoordinatorRole"
    )


class PathologistRole(WorkerRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000145", "PathologistRole")


class RoleOfPathologyReviewBoard(WorkerRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000188", "RoleOfPathologyReviewBoard"
    )


class ProxyRespondentRole(WorkerRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000211", "ProxyRespondentRole")


class SubInvestigatorRole(WorkerRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000224", "SubInvestigatorRole")


class TrialStatisticianRole(WorkerRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000234", "TrialStatisticianRole"
    )


class MaterialAmplificationRole(WorkerRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002473", "MaterialAmplificationRole"
    )


class MaterialSequencingLibraryPreparationRole(WorkerRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002474",
        "MaterialSequencingLibraryPreparationRole",
    )


class FeedRole(CompleteNutrientRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000248", "FeedRole")


class MolecularLabelRole(ReagentRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002743", "MolecularLabelRole")


class _1DExtent(Size):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001708", "_1DExtent")


class _3DExtent(Size):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001710", "_3DExtent")


class Composition(Structure):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000025", "Composition")


class Damage(Structure):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001020", "Damage")


class LateralTo(Position):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001193", "LateralTo")


class VentralTo(Position):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001196", "VentralTo")


class DorsalTo(Position):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001233", "DorsalTo")


class AnteriorTo(Position):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001632", "AnteriorTo")


class LeftSideOf(Position):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001792", "LeftSideOf")


class RightSideOf(Position):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001793", "RightSideOf")


class Frozen(Temperature):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001985", "Frozen")


class Age(Time):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000011", "Age")


class FlowRate(MovementQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001574", "FlowRate")


class QualityOfASolid(QualityOfASubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001546", "QualityOfASolid")


class QualityOfAGas(QualityOfASubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001547", "QualityOfAGas")


class QualityOfALiquid(QualityOfASubstance):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001548", "QualityOfALiquid")


class ActivityOfARadionuclide(QualityOfASubstance):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0001740", "ActivityOfARadionuclide"
    )


class QualityOfInteractionOfASubstanceWithElectromagneticRadiation(QualityOfASubstance):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0070060",
        "QualityOfInteractionOfASubstanceWithElectromagneticRadiation",
    )


class PhenotypicSex(BiologicalSex):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001894", "PhenotypicSex")


class MatingType(BiologicalSex):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001895", "MatingType")


class Alive(Viability):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001421", "Alive")


class Dead(Viability):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001422", "Dead")


class Handedness(BehavioralQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0002201", "Handedness")


class Ploidy(CellularQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001374", "Ploidy")


class Diluted(ConcentrationOf):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001161", "Diluted")


class Osmolality(ConcentrationOf):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0002027", "Osmolality")


class MeanCenteredData(NormalizedDataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302868", "MeanCenteredData")


class TopologicallyPreservedClusteredDataSet(ClusteredDataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000741",
        "TopologicallyPreservedClusteredDataSet",
    )


class MagneticResonanceImageDataSet(ImageDataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003328", "MagneticResonanceImageDataSet"
    )


class RawImageDataSet(ImageDataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003331", "RawImageDataSet")


class ComputedImageDataSet(ImageDataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003333", "ComputedImageDataSet")


class BaseOntologyModule(OntologyModule):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_8000001", "BaseOntologyModule")


class EditorsOntologyModule(OntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000002", "EditorsOntologyModule"
    )


class MainReleaseOntologyModule(OntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000003", "MainReleaseOntologyModule"
    )


class BridgeOntologyModule(OntologyModule):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_8000004", "BridgeOntologyModule")


class SubsetOntologyModule(OntologyModule):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_8000006", "SubsetOntologyModule")


class ReasonedOntologyModule(OntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000013", "ReasonedOntologyModule"
    )


class GeneratedOntologyModule(OntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000014", "GeneratedOntologyModule"
    )


class LengthMeasurementDatum(ScalarMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000408", "LengthMeasurementDatum"
    )


class MassMeasurementDatum(ScalarMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000414", "MassMeasurementDatum")


class TimeMeasurementDatum(ScalarMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000416", "TimeMeasurementDatum")


class HalfMaximalEffectiveConcentrationEc50(ScalarMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001180",
        "HalfMaximalEffectiveConcentrationEc50",
    )


class HalfMaximalInhibitoryConcentrationIc50(ScalarMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001191",
        "HalfMaximalInhibitoryConcentrationIc50",
    )


class MinimalInhibitoryConcentration(ScalarMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001514", "MinimalInhibitoryConcentration"
    )


class RateMeasurementDatum(ScalarMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001554", "RateMeasurementDatum")


class RandomAccessMemorySize(ScalarMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001874", "RandomAccessMemorySize"
    )


class N50(ScalarMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001940", "N50")


class SequencingLibraryInputQuantityMeasurementDatum(ScalarMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002480",
        "SequencingLibraryInputQuantityMeasurementDatum",
    )


class TemperatureMeasurementDatum(ScalarMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003079", "TemperatureMeasurementDatum"
    )


class HandednessCategoricalMeasurementDatum(CategoricalMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000976",
        "HandednessCategoricalMeasurementDatum",
    )


class EdinburghScore(ScalarScoreFromCompositeInputs):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000991", "EdinburghScore")


class DnaSequenceData(SequenceData):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001573", "DnaSequenceData")


class TrimmedSequenceData(SequenceData):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002569", "TrimmedSequenceData")


class AdapterSequenceData(SequenceData):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002578", "AdapterSequenceData")


class AdapterTrimmedSequenceData(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002579", "AdapterTrimmedSequenceData"
    )


class AlignedSequenceData(SequenceData):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002580", "AlignedSequenceData")


class MergedAlignedSequenceData(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002581", "MergedAlignedSequenceData"
    )


class DnaMethylationProfilingData(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002583", "DnaMethylationProfilingData"
    )


class DemultiplexedSequenceData(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002601", "DemultiplexedSequenceData"
    )


class MultiplexedSequenceData(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002602", "MultiplexedSequenceData"
    )


class InputProteinSequenceStartSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002975", "InputProteinSequenceStartSite"
    )


class InputProteinSequenceStopSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002976", "InputProteinSequenceStopSite"
    )


class InputGeneSequenceStartSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002977", "InputGeneSequenceStartSite"
    )


class InputGeneSequenceStopSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002978", "InputGeneSequenceStopSite"
    )


class ReferenceProteinSequenceStartSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002979",
        "ReferenceProteinSequenceStartSite",
    )


class ReferenceProteinSequenceStopSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002980", "ReferenceProteinSequenceStopSite"
    )


class ReferenceGeneSequenceStartSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002981", "ReferenceGeneSequenceStartSite"
    )


class ReferenceGeneSequenceStopSite(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002982", "ReferenceGeneSequenceStopSite"
    )


class ProportionMappedReads(SequenceData):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003056", "ProportionMappedReads"
    )


class PdbFile(_3DStructuralOrganizationDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001525", "PdbFile")


class PdbFileChain(_3DStructuralOrganizationDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001596", "PdbFileChain")


class NegativeBindingDatum(CategoricalBindingDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001182", "NegativeBindingDatum")


class PositiveBindingDatum(CategoricalBindingDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003295", "PositiveBindingDatum")


class BindingConstant(QuantitativeBindingDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001144", "BindingConstant")


class _50DissociationOfBindingTemperatureTm(QuantitativeBindingDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001566",
        "_50DissociationOfBindingTemperatureTm",
    )


class WildTypeOrganismGenotypeInformation(GenotypeInformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001294",
        "WildTypeOrganismGenotypeInformation",
    )


class AlleleInformation(GeneticAlterationInformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001352", "AlleleInformation")


class PartialKaryotypeInformation(KaryotypeInformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002770", "PartialKaryotypeInformation"
    )


class FullKaryotypeInformation(KaryotypeInformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002771", "FullKaryotypeInformation"
    )


class BacteriaInLungDatum(LungMicrobiologyDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003272", "BacteriaInLungDatum")


class EukaryotaInLungDatum(LungMicrobiologyDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003273", "EukaryotaInLungDatum")


class VirusInLungDatum(LungMicrobiologyDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003274", "VirusInLungDatum")


class BacteriaInNasopharyngealOrOropharyngealSwabDatum(
    NasopharyngealOrOropharyngealSwabMicrobiologyDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003275",
        "BacteriaInNasopharyngealOrOropharyngealSwabDatum",
    )


class EukaryotaInNasopharyngealOrOropharyngealSwabDatum(
    NasopharyngealOrOropharyngealSwabMicrobiologyDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003276",
        "EukaryotaInNasopharyngealOrOropharyngealSwabDatum",
    )


class VirusInNasopharyngealOrOropharyngealSwabDatum(
    NasopharyngealOrOropharyngealSwabMicrobiologyDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003277",
        "VirusInNasopharyngealOrOropharyngealSwabDatum",
    )


class BacteriaInPleuralFluidDatum(PleuralFluidMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003278", "BacteriaInPleuralFluidDatum"
    )


class EukaryotaInPleuralFluidDatum(PleuralFluidMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003279", "EukaryotaInPleuralFluidDatum"
    )


class VirusInPleuralFluidDatum(PleuralFluidMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003280", "VirusInPleuralFluidDatum"
    )


class BacteriaInBloodDatum(BloodMicrobiologyDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003261", "BacteriaInBloodDatum")


class VirusInBloodDatum(BloodMicrobiologyDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003262", "VirusInBloodDatum")


class EukaryotaInBloodDatum(BloodMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003263", "EukaryotaInBloodDatum"
    )


class PlacentalBloodMicrobiologyDatum(BloodMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003382", "PlacentalBloodMicrobiologyDatum"
    )


class UmbilicalCordBloodMicrobiologyDatum(
    BloodMicrobiologyDatum, UmbilicalCordBloodAssayDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003260",
        "UmbilicalCordBloodMicrobiologyDatum",
    )


class BacteriaInFecesDatum(FecesMicrobiologyDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003264", "BacteriaInFecesDatum")


class EukaryotaInFecesDatum(FecesMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003265", "EukaryotaInFecesDatum"
    )


class VirusInFecesDatum(FecesMicrobiologyDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003266", "VirusInFecesDatum")


class EukaryotaInUrineDatum(UrineMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003267", "EukaryotaInUrineDatum"
    )


class BacteriaInInducedSputumDatum(InducedSputumMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003268", "BacteriaInInducedSputumDatum"
    )


class EukaryotaInInducedSputumDatum(InducedSputumMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003269", "EukaryotaInInducedSputumDatum"
    )


class VirusInInducedSputumDatum(InducedSputumMicrobiologyDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003270", "VirusInInducedSputumDatum"
    )


class BacteriaInEndotrachealTubeAspirateDatum(
    EndotrachealTubeAspirateMicrobiologyDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003271",
        "BacteriaInEndotrachealTubeAspirateDatum",
    )


class DiagnosisOfHepatitisB(DiagnosisOfInfectiousDisease):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002386", "DiagnosisOfHepatitisB"
    )


class DiagnosisOfHepatitisC(DiagnosisOfInfectiousDisease):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002387", "DiagnosisOfHepatitisC"
    )


class DiagnosisOfHiv(DiagnosisOfInfectiousDisease):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002388", "DiagnosisOfHiv")


class SpecimenIdentifierAssignedBySpecimenRepository(SpecimenIdentifier):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001900",
        "SpecimenIdentifierAssignedBySpecimenRepository",
    )


class SpecimenIdentifierAssignedBySequencingFacility(SpecimenIdentifier):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001901",
        "SpecimenIdentifierAssignedBySequencingFacility",
    )


class StoppingRule(Rule):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500022", "StoppingRule")


class ComplianceRule(Rule):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500023", "ComplianceRule")


class SequenceFeatureIdentificationObjective(BiologicalFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000113",
        "SequenceFeatureIdentificationObjective",
    )


class MolecularFeatureIdentificationObjective(BiologicalFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000131",
        "MolecularFeatureIdentificationObjective",
    )


class CellularFeatureIdentificationObjective(BiologicalFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000219",
        "CellularFeatureIdentificationObjective",
    )


class OrganismFeatureIdentificationObjective(BiologicalFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000268",
        "OrganismFeatureIdentificationObjective",
    )


class OrganismSpeciesDetectionObjective(BiologicalFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001623",
        "OrganismSpeciesDetectionObjective",
    )


class MolecularFunctionIdentificationObjective(
    BiologicalFeatureIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001690",
        "MolecularFunctionIdentificationObjective",
    )


class CellularStructureFeatureIdentificationObjective(
    BiologicalFeatureIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001691",
        "CellularStructureFeatureIdentificationObjective",
    )


class BiodiversityAssessmentObjective(BiologicalFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001969", "BiodiversityAssessmentObjective"
    )


class ProtocolTestingObjective(MethodologyTestingObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000096", "ProtocolTestingObjective"
    )


class HardwareTestingObjective(MethodologyTestingObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000134", "HardwareTestingObjective"
    )


class SoftwareTestingObjective(MethodologyTestingObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000242", "SoftwareTestingObjective"
    )


class AnalyteMeasurementObjective(AssayObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000437", "AnalyteMeasurementObjective"
    )


class ManufacturingObjective(MaterialTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000458", "ManufacturingObjective"
    )


class MaterialSeparationObjective(MaterialTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000639", "MaterialSeparationObjective"
    )


class MaterialCombinationObjective(MaterialTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000686", "MaterialCombinationObjective"
    )


class DeviceCreationObjective(MaterialTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000996", "DeviceCreationObjective"
    )


class GeneticTransformationObjective(MaterialTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001153", "GeneticTransformationObjective"
    )


class AveragingObjective(DataTransformationObjective):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000425", "AveragingObjective")


class FuzzyClusteringObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000653", "FuzzyClusteringObjective"
    )


class StatisticalHypothesisTestObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000675",
        "StatisticalHypothesisTestObjective",
    )


class DecisionTreeInductionObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000704", "DecisionTreeInductionObjective"
    )


class PatternMatchingObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000868", "PatternMatchingObjective"
    )


class FeatureExtractionObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200005", "FeatureExtractionObjective"
    )


class DifferentialExpressionAnalysisObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200031",
        "DifferentialExpressionAnalysisObjective",
    )


class DescriptiveStatisticalCalculationObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200078",
        "DescriptiveStatisticalCalculationObjective",
    )


class SequenceAnalysisObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200081", "SequenceAnalysisObjective"
    )


class SurvivalAnalysisObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200083", "SurvivalAnalysisObjective"
    )


class InterRaterReliabilityObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200091", "InterRaterReliabilityObjective"
    )


class DataVectorReductionObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200157", "DataVectorReductionObjective"
    )


class DataNormalizationObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200167", "DataNormalizationObjective"
    )


class CorrectionObjective(DataTransformationObjective):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200168", "CorrectionObjective")


class PartitioningObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200172", "PartitioningObjective"
    )


class CurveFittingObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200174", "CurveFittingObjective"
    )


class CenterCalculationObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200177", "CenterCalculationObjective"
    )


class ClassDiscoveryObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200178", "ClassDiscoveryObjective"
    )


class ClassPredictionObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200179", "ClassPredictionObjective"
    )


class SpreadCalculationObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200180", "SpreadCalculationObjective"
    )


class ScalingObjective(DataTransformationObjective):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200183", "ScalingObjective")


class MergingObjective(DataTransformationObjective):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200189", "MergingObjective")


class CorrelationStudyObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200196", "CorrelationStudyObjective"
    )


class SpectrumAnalysisObjective(DataTransformationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200197", "SpectrumAnalysisObjective"
    )


class SoftwareApplication(Software):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000594", "SoftwareApplication")


class GenepatternSoftware(Software):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000713", "GenepatternSoftware")


class SequenceAssemblyAlgorithm(Algorithm):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001522", "SequenceAssemblyAlgorithm"
    )


class SequenceAnnotationAlgorithm(Algorithm):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001625", "SequenceAnnotationAlgorithm"
    )


class AlignmentCountingAlgorithm(Algorithm):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002466", "AlignmentCountingAlgorithm"
    )


class BaseCallingAlgorithm(Algorithm):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002468", "BaseCallingAlgorithm")


class ReferenceGenomeTranscriptomeAlignmentAlgorithm(Algorithm):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002478",
        "ReferenceGenomeTranscriptomeAlignmentAlgorithm",
    )


class AnimalCareProtocol(Protocol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000715", "AnimalCareProtocol")


class SequencingProtocol(Protocol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003069", "SequencingProtocol")


class SpecimenCollectionProtocol(Protocol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003070", "SpecimenCollectionProtocol"
    )


class MagneticResonancePulseSequenceProtocol(Protocol):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003332",
        "MagneticResonancePulseSequenceProtocol",
    )


class InterventionDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000115", "InterventionDesign")


class ValidationByReverseTranscriptionPcrDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001162",
        "ValidationByReverseTranscriptionPcrDesign",
    )


class ValidationByRealTimePcrDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001166", "ValidationByRealTimePcrDesign"
    )


class OperatorVariationDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001195", "OperatorVariationDesign"
    )


class ComparativeGenomeHybridizationByArrayDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001197",
        "ComparativeGenomeHybridizationByArrayDesign",
    )


class InVivoDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001199", "InVivoDesign")


class InnateBehaviorDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001202", "InnateBehaviorDesign")


class CellComponentComparisonDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001205", "CellComponentComparisonDesign"
    )


class ExVivoDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001211", "ExVivoDesign")


class NormalizationTestingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001214", "NormalizationTestingDesign"
    )


class EnvironmentalHistoryDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001226", "EnvironmentalHistoryDesign"
    )


class TranscriptionProfilingByHighThroughputSequencingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001239",
        "TranscriptionProfilingByHighThroughputSequencingDesign",
    )


class ArrayPlatformVariationDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001252", "ArrayPlatformVariationDesign"
    )


class TranslationalBiasDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001259", "TranslationalBiasDesign"
    )


class DnaMethylationProfilingByArrayDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001278",
        "DnaMethylationProfilingByArrayDesign",
    )


class InVitroDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001285", "InVitroDesign")


class RnaiProfilingByArrayDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001286", "RnaiProfilingByArrayDesign"
    )


class TranscriptionProfilingByArrayDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001290",
        "TranscriptionProfilingByArrayDesign",
    )


class DiseaseStateDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001293", "DiseaseStateDesign")


class RnaStabilityDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001306", "RnaStabilityDesign")


class SpeciesComparisonDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001310", "SpeciesComparisonDesign"
    )


class TranscriptionProfilingByRtPcrDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001313",
        "TranscriptionProfilingByRtPcrDesign",
    )


class MicrornaProfilingByArrayDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001323", "MicrornaProfilingByArrayDesign"
    )


class OrganismDevelopmentDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001328", "OrganismDevelopmentDesign"
    )


class FamilyHistoryDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001329", "FamilyHistoryDesign")


class QualityControlTestingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001336", "QualityControlTestingDesign"
    )


class ClinicalHistoryDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001337", "ClinicalHistoryDesign"
    )


class CellularProcessDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001365", "CellularProcessDesign"
    )


class InjuryDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001374", "InjuryDesign")


class OrganismStatusComparisonDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001377", "OrganismStatusComparisonDesign"
    )


class ProtocolOptimizationDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001401", "ProtocolOptimizationDesign"
    )


class ImprintingDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001408", "ImprintingDesign")


class CellCycleDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001409", "CellCycleDesign")


class TranslationProfilingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001410", "TranslationProfilingDesign"
    )


class CellTypeComparisonDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001411", "CellTypeComparisonDesign"
    )


class OrganismPartComparisonDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001422", "OrganismPartComparisonDesign"
    )


class ProteinBindingSiteIdentificationDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001425",
        "ProteinBindingSiteIdentificationDesign",
    )


class SexComparisonDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001426", "SexComparisonDesign")


class TranscriptionProfilingByTilingArrayDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001427",
        "TranscriptionProfilingByTilingArrayDesign",
    )


class CellDifferentiationDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001429", "CellDifferentiationDesign"
    )


class TranscriptionProfilingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001430", "TranscriptionProfilingDesign"
    )


class OperonIdentificationDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001432", "OperonIdentificationDesign"
    )


class DnaMethylationProfilingByHighThroughputSequencingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001435",
        "DnaMethylationProfilingByHighThroughputSequencingDesign",
    )


class AllPairsDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001440", "AllPairsDesign")


class ProteomicProfilingByArrayDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001441", "ProteomicProfilingByArrayDesign"
    )


class GenotypingDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001444", "GenotypingDesign")


class IndividualGeneticCharacteristicsComparisonDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001448",
        "IndividualGeneticCharacteristicsComparisonDesign",
    )


class PathogenicityDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001454", "PathogenicityDesign")


class StrainComparisonDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001464", "StrainComparisonDesign"
    )


class HardwareTestingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001957", "HardwareTestingDesign"
    )


class SystematicReviewStudyDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001958", "SystematicReviewStudyDesign"
    )


class DecisionAnalysisStudyDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001965", "DecisionAnalysisStudyDesign"
    )


class ProteomicProfilingDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002446", "ProteomicProfilingDesign"
    )


class MolecularInteractionIdentificationDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002590",
        "MolecularInteractionIdentificationDesign",
    )


class BirthCohortStudyDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002614", "BirthCohortStudyDesign"
    )


class DiseaseSpecificStudyDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002615", "DiseaseSpecificStudyDesign"
    )


class CaseControlStudyDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002624", "CaseControlStudyDesign"
    )


class CaseSeriesDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002674", "CaseSeriesDesign")


class PopulationBasedDesign(StudyDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002945", "PopulationBasedDesign"
    )


class InSilicoDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003291", "InSilicoDesign")


class RingTrialDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003658", "RingTrialDesign")


class ObservationDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0300311", "ObservationDesign")


class ClinicalStudyDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500001", "ClinicalStudyDesign")


class MatchedPairsDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500005", "MatchedPairsDesign")


class ParallelGroupDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500006", "ParallelGroupDesign")


class LoopDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500009", "LoopDesign")


class ReferenceDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500010", "ReferenceDesign")


class FactorialDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500014", "FactorialDesign")


class DyeSwapDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500017", "DyeSwapDesign")


class ReplicateDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500018", "ReplicateDesign")


class SelfVsSelfDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500019", "SelfVsSelfDesign")


class TimeSeriesDesign(StudyDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500020", "TimeSeriesDesign")


class InclusionCriterion(EligibilityCriterion):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500027", "InclusionCriterion")


class ExclusionCriterion(EligibilityCriterion):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500028", "ExclusionCriterion")


class SurvivalCurve(LineGraph):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000889", "SurvivalCurve")


class DoseResponseCurve(LineGraph):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001172", "DoseResponseCurve")


class HistologicGradeForOvarianTumorAccordingToATwoTierGradingSystem(
    HistologicGradeForOvarianTumor
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002216",
        "HistologicGradeForOvarianTumorAccordingToATwoTierGradingSystem",
    )


class HistologicGradeForOvarianTumorAccordingToTheWorldHealthOrganization(
    HistologicGradeForOvarianTumor
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002219",
        "HistologicGradeForOvarianTumorAccordingToTheWorldHealthOrganization",
    )


class EasternCooperativeOncologyGroupScoreValueSpecification(
    PerformanceStatusValueSpecification
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002357",
        "EasternCooperativeOncologyGroupScoreValueSpecification",
    )


class KarnofskyScoreVaueSpecification(PerformanceStatusValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002363", "KarnofskyScoreVaueSpecification"
    )


class PresenceOrOverThresholdValueSpecification(OrdinalValueSpecification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002772",
        "PresenceOrOverThresholdValueSpecification",
    )


class Supercontig(SequenceAssembly):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000148", "Supercontig")


class Contig(SequenceAssembly):
    term = RdfTerm("http://purl.obolibrary.org/obo/SO_0000149", "Contig")


class EpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells(
    ChemokineCXCMotifLigand9Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001439",
        "EpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells",
    )


class EpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells(
    MonocyteChemotacticProtein1Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001386",
        "EpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells",
    )


class EpitopeSpecificChemokineCCMotifLigand4ProductionByTCells(
    ChemokineCCMotifLigand4Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001362",
        "EpitopeSpecificChemokineCCMotifLigand4ProductionByTCells",
    )


class EpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells(
    MacrophageInflammatoryProtein1GammaProduction,
    EpitopeSpecificCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001447",
        "EpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells",
    )


class EpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells(
    MacrophageInflammatoryProtein1AlphaProduction,
    EpitopeSpecificCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001207",
        "EpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells",
    )


class EpitopeSpecificRantesProductionByTCells(
    ChemokineCCMotifLigand5Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001366",
        "EpitopeSpecificRantesProductionByTCells",
    )


class EpitopeSpecificChemokineCCMotifLigand1ProductionByTCells(
    ChemokineCCMotifLigand1Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001219",
        "EpitopeSpecificChemokineCCMotifLigand1ProductionByTCells",
    )


class EpitopeSpecificIp10ProductionByTCells(
    Ip10Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001462",
        "EpitopeSpecificIp10ProductionByTCells",
    )


class EpitopeSpecificChemokineCCMotifLigand22ProductionByTCells(
    ChemokineCCMotifLigand22Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001819",
        "EpitopeSpecificChemokineCCMotifLigand22ProductionByTCells",
    )


class EpitopeSpecificChemokineCCMotifLigand19ProductionByTCells(
    ChemokineCCMotifLigand19Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001825",
        "EpitopeSpecificChemokineCCMotifLigand19ProductionByTCells",
    )


class EpitopeSpecificChemokineCCMotifLigand21ProductionByTCells(
    ChemokineCCMotifLigand21Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001823",
        "EpitopeSpecificChemokineCCMotifLigand21ProductionByTCells",
    )


class EpitopeSpecificChemokineCXCMotifLigand12ProductionByTCells(
    ChemokineCXCMotifLigand12Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001818",
        "EpitopeSpecificChemokineCXCMotifLigand12ProductionByTCells",
    )


class EpitopeSpecificChemokineCXCMotifLigand13ProductionByTCells(
    ChemokineCXCMotifLigand13Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001816",
        "EpitopeSpecificChemokineCXCMotifLigand13ProductionByTCells",
    )


class EpitopeSpecificChemokineCXCMotifLigand16ProductionByTCells(
    ChemokineCXCMotifLigand16Production, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001820",
        "EpitopeSpecificChemokineCXCMotifLigand16ProductionByTCells",
    )


class EpitopeSpecificInterleukin1AlphaProductionByTCells(
    Interleukin1AlphaProduction, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001257",
        "EpitopeSpecificInterleukin1AlphaProductionByTCells",
    )


class EpitopeSpecificIl1BReleaseByTCells(
    Interleukin1BetaProduction, EpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110196",
        "EpitopeSpecificIl1BReleaseByTCells",
    )


class EpitopeSpecificInterleukin17AProductionByTCells(
    EpitopeSpecificIl17ReleaseByTCells, Interleukin17AProduction
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001526",
        "EpitopeSpecificInterleukin17AProductionByTCells",
    )


class EpitopeSpecificInterleukin17FProductionByTCells(
    EpitopeSpecificIl17ReleaseByTCells, Interleukin17FProduction
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001470",
        "EpitopeSpecificInterleukin17FProductionByTCells",
    )


class EpitopeSpecificTnfReleaseByTCells(
    EpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    TumorNecrosisFactorProduction,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110206",
        "EpitopeSpecificTnfReleaseByTCells",
    )


class EpitopeSpecificLymphotoxinAProductionByTCells(
    EpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    LymphotoxinAProduction,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001256",
        "EpitopeSpecificLymphotoxinAProductionByTCells",
    )


class EpitopeSpecificTumorNecrosisFactorLigandSuperfamilyMember11ProductionByTCells(
    EpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    TumorNecrosisFactorLigandSuperfamilyMember11Production,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001518",
        "EpitopeSpecificTumorNecrosisFactorLigandSuperfamilyMember11ProductionByTCells",
    )


class HelperTCellEnhancementOfAdaptiveImmuneResponse(AdaptiveImmuneResponse):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0035397",
        "HelperTCellEnhancementOfAdaptiveImmuneResponse",
    )


class BCellEpitopeSpecificHistamineSecretionMediatedByImmunoglobulin(
    HistamineSecretionMediatedByImmunoglobulin
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001725",
        "BCellEpitopeSpecificHistamineSecretionMediatedByImmunoglobulin",
    )


class PhaseIClinicalTrial(ClinicalTrial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003700", "PhaseIClinicalTrial")


class PhaseIiClinicalTrial(ClinicalTrial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003701", "PhaseIiClinicalTrial")


class PhaseIiiClinicalTrial(ClinicalTrial):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003702", "PhaseIiiClinicalTrial"
    )


class ConfocalFluorescenceMicroscopyAssay(MicroscopyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHMO_0000089",
        "ConfocalFluorescenceMicroscopyAssay",
    )


class LightMicroscopyAssay(MicroscopyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHMO_0000102", "LightMicroscopyAssay"
    )


class ElectronMicroscopyImagingAssay(MicroscopyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001631", "ElectronMicroscopyImagingAssay"
    )


class CyclicImmunofluoroescenceAssay(MicroscopyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002969", "CyclicImmunofluoroescenceAssay"
    )


class ModifiedAcidFastStainMicroscopyAssay(MicroscopyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003294",
        "ModifiedAcidFastStainMicroscopyAssay",
    )


class CellDiveMultiplexedImagingAssay(MultiplexedFluorescentAntibodyImagingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003092", "CellDiveMultiplexedImagingAssay"
    )


class CoDetectionByIndexingAssay(MultiplexedFluorescentAntibodyImagingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003093", "CoDetectionByIndexingAssay"
    )


class TranscriptionProfilingByTilingArrayAssay(TranscriptionProfilingByArrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001235",
        "TranscriptionProfilingByTilingArrayAssay",
    )


class MicrornaProfilingByArrayAssay(MicrornaProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001335", "MicrornaProfilingByArrayAssay"
    )


class MicrornaProfilingByHighThroughputSequencingAssay(MicrornaProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001922",
        "MicrornaProfilingByHighThroughputSequencingAssay",
    )


class NanostringNcounterMirnaExpressionAssay(MicrornaProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002142",
        "NanostringNcounterMirnaExpressionAssay",
    )


class GenotypingByHighThroughputSequencingAssay(GenotypingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001247",
        "GenotypingByHighThroughputSequencingAssay",
    )


class KillerCellImmunoglobulinLikeReceptorTypingAssay(GenotypingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002121",
        "KillerCellImmunoglobulinLikeReceptorTypingAssay",
    )


class MajorHistocompatibilityTypingAssay(GenotypingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002122",
        "MajorHistocompatibilityTypingAssay",
    )


class GenotypePhasingByHiCAssay(GenotypingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002459", "GenotypePhasingByHiCAssay"
    )


class GenotypingByPcrAssay(GenotypingAssay, PolymeraseChainReactionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003032", "GenotypingByPcrAssay")


class PcrSscpAssay(GenotypingAssay, PolymeraseChainReactionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302737", "PcrSscpAssay")


class ElisaMeasuringOrientiaTsutsugamushiIgmAntibody(EnzymeLinkedImmunosorbentAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003541",
        "ElisaMeasuringOrientiaTsutsugamushiIgmAntibody",
    )


class ElisaMeasuringChikungunyaIgmAntibody(EnzymeLinkedImmunosorbentAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003545",
        "ElisaMeasuringChikungunyaIgmAntibody",
    )


class MicroarrayElisaMeasuringChikungunyaIgmAntibody(EnzymeLinkedImmunosorbentAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003546",
        "MicroarrayElisaMeasuringChikungunyaIgmAntibody",
    )


class AntithrombinIiiBerichromeAssay(HumanAntithrombinIiiInBloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000805", "AntithrombinIiiBerichromeAssay"
    )


class ChromatinIsolationByRnaPurificationSequencingAssay(
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002040",
        "ChromatinIsolationByRnaPurificationSequencingAssay",
    )


class AntigenDetectionByCytometricBeadArrayAssay(CytometricBeadArrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003115",
        "AntigenDetectionByCytometricBeadArrayAssay",
    )


class AntibodyDetectionByCytometricBeadArrayAssay(CytometricBeadArrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003116",
        "AntibodyDetectionByCytometricBeadArrayAssay",
    )


class HighPerformanceLiquidChromotographyAssay(AnalyticalChromatography):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002116",
        "HighPerformanceLiquidChromotographyAssay",
    )


class AnalyticalChromatographyMeasuringChikungunyaIgmAntibody(AnalyticalChromatography):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003544",
        "AnalyticalChromatographyMeasuringChikungunyaIgmAntibody",
    )


class AssayUsingChromatinImmunoprecipitation(ImmunoprecipitationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001956",
        "AssayUsingChromatinImmunoprecipitation",
    )


class WesternBlotAssay(ImmunoblotAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000854", "WesternBlotAssay")


class GenotypingByArrayAssay(GenotypingAssay, MicroarrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001274", "GenotypingByArrayAssay"
    )


class ComparativeGenomicHybridizationByArrayAssay(GenotypingAssay, MicroarrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001393",
        "ComparativeGenomicHybridizationByArrayAssay",
    )


class RnaiProfilingByArrayAssay(MicroarrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001304", "RnaiProfilingByArrayAssay"
    )


class RnaBindingProteinImmunoprecipitationArrayProfilingAssay(MicroarrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001918",
        "RnaBindingProteinImmunoprecipitationArrayProfilingAssay",
    )


class MicroarrayAssayMeasuringDengueIgmAntibody(MicroarrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003542",
        "MicroarrayAssayMeasuringDengueIgmAntibody",
    )


class HivAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002146", "HivAntibodyAssay")


class HivGroupOAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002147", "HivGroupOAntibodyAssay"
    )


class SurfaceHbvAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002148", "SurfaceHbvAntibodyAssay"
    )


class CoreHbvAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002149", "CoreHbvAntibodyAssay")


class CoreHbvIgmAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002150", "CoreHbvIgmAntibodyAssay"
    )


class HcvAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002151", "HcvAntibodyAssay")


class EbvIggAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002152", "EbvIggAntibodyAssay")


class EbvIgmAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002153", "EbvIgmAntibodyAssay")


class CmvAntibodyAssay(AntigenSpecificAntibodiesAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002154", "CmvAntibodyAssay")


class AntigenSpecificAntibodiesInBloodAssay(AntigenSpecificAntibodiesAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003418",
        "AntigenSpecificAntibodiesInBloodAssay",
    )


class AntigenSpecificAntibodiesInMilkAssay(AntigenSpecificAntibodiesAssay, MilkAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003419",
        "AntigenSpecificAntibodiesInMilkAssay",
    )


class SerumAntiEpsteinBarrVirusAntibodyLevelAssay(
    AntigenSpecificAntibodiesAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003589",
        "SerumAntiEpsteinBarrVirusAntibodyLevelAssay",
    )


class IronConcentrationAssay(IronAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003158", "IronConcentrationAssay"
    )


class VenousBloodIronAssay(IronAssay, BloodAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100098", "VenousBloodIronAssay")


class CalciumCationAssay(IonizedCalciumAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100024", "CalciumCationAssay")


class VenousBloodUricAcidAssay(UricAcidAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100117", "VenousBloodUricAcidAssay"
    )


class GlobulinConcentrationAssay(GlobulinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003155", "GlobulinConcentrationAssay"
    )


class LiverEvaluationVenousBloodGlobulinAssay(GlobulinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100081",
        "LiverEvaluationVenousBloodGlobulinAssay",
    )


class CreatineConcentrationAssay(CreatineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003195", "CreatineConcentrationAssay"
    )


class EstradiolConcentrationAssay(EstradiolAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003197", "EstradiolConcentrationAssay"
    )


class HighDensityLipoproteinConcentrationAssay(LipoproteinConcentrationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003205",
        "HighDensityLipoproteinConcentrationAssay",
    )


class LowDensityLipoproteinConcentrationAssay(LipoproteinConcentrationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003206",
        "LowDensityLipoproteinConcentrationAssay",
    )


class VeryLowDensityLipoproteinConcentrationAssay(LipoproteinConcentrationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003207",
        "VeryLowDensityLipoproteinConcentrationAssay",
    )


class LuteinizingHormoneConcentrationAssay(LuteinizingHormoneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003209",
        "LuteinizingHormoneConcentrationAssay",
    )


class NitriteConcentrationAssay(NitriteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003211", "NitriteConcentrationAssay"
    )


class PhospholipidConcentrationAssay(PhospholipidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003213", "PhospholipidConcentrationAssay"
    )


class ProgesteroneConcentrationAssay(ProgesteroneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003215", "ProgesteroneConcentrationAssay"
    )


class TestosteroneConcentrationAssay(TestosteroneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003217", "TestosteroneConcentrationAssay"
    )


class BileSaltConcentrationAssay(BileSaltAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003219", "BileSaltConcentrationAssay"
    )


class FreeFattyAcidConcentrationAssay(FattyAcidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003221", "FreeFattyAcidConcentrationAssay"
    )


class InsulinConcentrationAssay(InsulinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003223", "InsulinConcentrationAssay"
    )


class FollicleStimulatingHormoneConcentrationAssay(FollicleStimulatingHormoneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003225",
        "FollicleStimulatingHormoneConcentrationAssay",
    )


class Panel5VenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100052",
        "Panel5VenousBloodCarbonDioxideAssay",
    )


class BasicMetabolicPanelVenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100093",
        "BasicMetabolicPanelVenousBloodCarbonDioxideAssay",
    )


class InpatientProfileVenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100130",
        "InpatientProfileVenousBloodCarbonDioxideAssay",
    )


class VenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100134", "VenousBloodCarbonDioxideAssay"
    )


class ComprehensiveMetabolicPanelVenousBloodCarbonDioxideAssay(
    CarbonDioxideAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100148",
        "ComprehensiveMetabolicPanelVenousBloodCarbonDioxideAssay",
    )


class BloodGasVenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100168",
        "BloodGasVenousBloodCarbonDioxideAssay",
    )


class NonVentedBloodGasArterialBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100174",
        "NonVentedBloodGasArterialBloodCarbonDioxideAssay",
    )


class VentedBloodGasArterialBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100185",
        "VentedBloodGasArterialBloodCarbonDioxideAssay",
    )


class GemPremierBloodGasVenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100198",
        "GemPremierBloodGasVenousBloodCarbonDioxideAssay",
    )


class Chem11VenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100228",
        "Chem11VenousBloodCarbonDioxideAssay",
    )


class Chem16VenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100238",
        "Chem16VenousBloodCarbonDioxideAssay",
    )


class Abl90PanelArterialBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100277",
        "Abl90PanelArterialBloodCarbonDioxideAssay",
    )


class Abl90PanelVenousBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100287",
        "Abl90PanelVenousBloodCarbonDioxideAssay",
    )


class AbgElectrolytesArterialBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100303",
        "AbgElectrolytesArterialBloodCarbonDioxideAssay",
    )


class Gem4000AnlcooxArterialBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100320",
        "Gem4000AnlcooxArterialBloodCarbonDioxideAssay",
    )


class Gem4ArterialBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100381",
        "Gem4ArterialBloodCarbonDioxideAssay",
    )


class BloodGasArterialBloodCarbonDioxideAssay(CarbonDioxideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100388",
        "BloodGasArterialBloodCarbonDioxideAssay",
    )


class Sodium1ConcentrationAssay(Sodium1Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003171", "Sodium1ConcentrationAssay"
    )


class Panel5VenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100053", "Panel5VenousBloodSodiumAssay"
    )


class BasicMetabolicPanelVenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100089",
        "BasicMetabolicPanelVenousBloodSodiumAssay",
    )


class InpatientProfileVenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100127",
        "InpatientProfileVenousBloodSodiumAssay",
    )


class VenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100136", "VenousBloodSodiumAssay"
    )


class RandomElectrolytesUrineSodiumAssay(Sodium1Assay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100137",
        "RandomElectrolytesUrineSodiumAssay",
    )


class ElectrolytesUrineSodiumAssay(Sodium1Assay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100144", "ElectrolytesUrineSodiumAssay"
    )


class ComprehensiveMetabolicPanelVenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100151",
        "ComprehensiveMetabolicPanelVenousBloodSodiumAssay",
    )


class ArterialBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100180", "ArterialBloodSodiumAssay"
    )


class GemPremierBloodGasVenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100196",
        "GemPremierBloodGasVenousBloodSodiumAssay",
    )


class Chem11VenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100230", "Chem11VenousBloodSodiumAssay"
    )


class Chem16VenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100242", "Chem16VenousBloodSodiumAssay"
    )


class PocChem8ArterialBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100253", "PocChem8ArterialBloodSodiumAssay"
    )


class Abl90PanelArterialBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100271",
        "Abl90PanelArterialBloodSodiumAssay",
    )


class Abl90PanelVenousBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100289", "Abl90PanelVenousBloodSodiumAssay"
    )


class UrineSodiumAssay(Sodium1Assay, UrineAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100297", "UrineSodiumAssay")


class Gem4000AnlcooxArterialBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100321",
        "Gem4000AnlcooxArterialBloodSodiumAssay",
    )


class Gem4ArterialBloodSodiumAssay(Sodium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100374", "Gem4ArterialBloodSodiumAssay"
    )


class CreatinineConcentrationAssay(CreatinineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003153", "CreatinineConcentrationAssay"
    )


class Panel5VenousBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100054", "Panel5VenousBloodCreatinineAssay"
    )


class BasicMetabolicPanelVenousBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100090",
        "BasicMetabolicPanelVenousBloodCreatinineAssay",
    )


class InpatientProfileVenousBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100128",
        "InpatientProfileVenousBloodCreatinineAssay",
    )


class UrineCreatinineAssay(CreatinineAssay, UrineAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100139", "UrineCreatinineAssay")


class ComprehensiveMetabolicPanelVenousBloodCreatinineAssay(
    CreatinineAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100159",
        "ComprehensiveMetabolicPanelVenousBloodCreatinineAssay",
    )


class VenousBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100165", "VenousBloodCreatinineAssay"
    )


class ArterialBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100170", "ArterialBloodCreatinineAssay"
    )


class Dt60VenousBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100219", "Dt60VenousBloodCreatinineAssay"
    )


class Chem11VenousBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100232", "Chem11VenousBloodCreatinineAssay"
    )


class Chem16VenousBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100236", "Chem16VenousBloodCreatinineAssay"
    )


class PocChem8ArterialBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100254",
        "PocChem8ArterialBloodCreatinineAssay",
    )


class _24HourUrineCreatinineAssay(CreatinineAssay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100258", "_24HourUrineCreatinineAssay"
    )


class PocArterialBloodCreatinineAssay(CreatinineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100311", "PocArterialBloodCreatinineAssay"
    )


class CreatinineClearanceUrineCreatinineAssay(CreatinineAssay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100363",
        "CreatinineClearanceUrineCreatinineAssay",
    )


class Potassium1ConcentrationAssay(Potassium1Assay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003168", "Potassium1ConcentrationAssay"
    )


class Panel5VenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100055", "Panel5VenousBloodPotassiumAssay"
    )


class BasicMetabolicPanelVenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100088",
        "BasicMetabolicPanelVenousBloodPotassiumAssay",
    )


class InpatientProfileVenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100129",
        "InpatientProfileVenousBloodPotassiumAssay",
    )


class VenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100133", "VenousBloodPotassiumAssay"
    )


class RandomElectrolytesUrinePotassiumAssay(Potassium1Assay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100138",
        "RandomElectrolytesUrinePotassiumAssay",
    )


class ElectrolytesUrinePotassiumAssay(Potassium1Assay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100145", "ElectrolytesUrinePotassiumAssay"
    )


class ComprehensiveMetabolicPanelVenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100150",
        "ComprehensiveMetabolicPanelVenousBloodPotassiumAssay",
    )


class ArterialBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100181", "ArterialBloodPotassiumAssay"
    )


class GemPremierBloodGasVenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100191",
        "GemPremierBloodGasVenousBloodPotassiumAssay",
    )


class Chem11VenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100225", "Chem11VenousBloodPotassiumAssay"
    )


class Chem16VenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100249", "Chem16VenousBloodPotassiumAssay"
    )


class PocChem8ArterialBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100252",
        "PocChem8ArterialBloodPotassiumAssay",
    )


class Abl90PanelArterialBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100282",
        "Abl90PanelArterialBloodPotassiumAssay",
    )


class Abl90PanelVenousBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100296",
        "Abl90PanelVenousBloodPotassiumAssay",
    )


class Gem4000AnlcooxArterialBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100317",
        "Gem4000AnlcooxArterialBloodPotassiumAssay",
    )


class Gem4ArterialBloodPotassiumAssay(Potassium1Assay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100375", "Gem4ArterialBloodPotassiumAssay"
    )


class ChlorideConcentrationAssay(ChlorideAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003151", "ChlorideConcentrationAssay"
    )


class VenousBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100061", "VenousBloodChlorideAssay"
    )


class BasicMetabolicPanelVenousBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100087",
        "BasicMetabolicPanelVenousBloodChlorideAssay",
    )


class ComprehensiveMetabolicPanelVenousBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100156",
        "ComprehensiveMetabolicPanelVenousBloodChlorideAssay",
    )


class ArterialBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100187", "ArterialBloodChlorideAssay"
    )


class Chem11VenousBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100233", "Chem11VenousBloodChlorideAssay"
    )


class Chem16VenousBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100247", "Chem16VenousBloodChlorideAssay"
    )


class PocChem8ArterialBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100256",
        "PocChem8ArterialBloodChlorideAssay",
    )


class Abl90PanelArterialBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100276",
        "Abl90PanelArterialBloodChlorideAssay",
    )


class Abl90PanelVenousBloodChlorideAssay(ChlorideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100293",
        "Abl90PanelVenousBloodChlorideAssay",
    )


class HemoglobinConcentrationAssay(HemoglobinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003156", "HemoglobinConcentrationAssay"
    )


class MeanCellHemoglobinAssay(HemoglobinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003183", "MeanCellHemoglobinAssay"
    )


class MeanCellHemoglobinConcentrationAssay(HemoglobinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003184",
        "MeanCellHemoglobinConcentrationAssay",
    )


class CbcWithAutomatedDifferentialVenousBloodHemoglobinAssay(
    HemoglobinAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100066",
        "CbcWithAutomatedDifferentialVenousBloodHemoglobinAssay",
    )


class CbcVenousBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100078", "CbcVenousBloodHemoglobinAssay"
    )


class HemoglobinOxygenSaturationArterialBloodHemoglobinAssay(
    HemoglobinAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100126",
        "HemoglobinOxygenSaturationArterialBloodHemoglobinAssay",
    )


class CooximiteryArterialBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100142",
        "CooximiteryArterialBloodHemoglobinAssay",
    )


class ArterialBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100188", "ArterialBloodHemoglobinAssay"
    )


class GemPremierBloodGasVenousBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100193",
        "GemPremierBloodGasVenousBloodHemoglobinAssay",
    )


class Abl90PanelArterialBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100275",
        "Abl90PanelArterialBloodHemoglobinAssay",
    )


class Abl90PanelVenousBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100285",
        "Abl90PanelVenousBloodHemoglobinAssay",
    )


class Gem4000AnlcooxArterialBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100316",
        "Gem4000AnlcooxArterialBloodHemoglobinAssay",
    )


class VenousBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100323", "VenousBloodHemoglobinAssay"
    )


class HemoglobinAndHematocritVenousBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100354",
        "HemoglobinAndHematocritVenousBloodHemoglobinAssay",
    )


class Gem4ArterialBloodHemoglobinAssay(HemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100373", "Gem4ArterialBloodHemoglobinAssay"
    )


class PhosphateIonConcentrationAssay(PhosphateIonAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003167", "PhosphateIonConcentrationAssay"
    )


class VenousBloodPhosphateAssay(PhosphateIonAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100067", "VenousBloodPhosphateAssay"
    )


class Chem11VenousBloodPhosphateAssay(PhosphateIonAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100224", "Chem11VenousBloodPhosphateAssay"
    )


class Chem16VenousBloodPhosphateAssay(PhosphateIonAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100243", "Chem16VenousBloodPhosphateAssay"
    )


class BoneProfileVenousBloodPhosphateAssay(PhosphateIonAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100302",
        "BoneProfileVenousBloodPhosphateAssay",
    )


class DirectBilirubinConcentrationAssay(BilirubinIxalphaAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003180",
        "DirectBilirubinConcentrationAssay",
    )


class IndirectBilirubinConcentrationAssay(BilirubinIxalphaAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003181",
        "IndirectBilirubinConcentrationAssay",
    )


class TotalBilirubinConcentrationAssay(BilirubinIxalphaAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003182", "TotalBilirubinConcentrationAssay"
    )


class LiverInjuryVenousBloodBilirubinAssay(BilirubinIxalphaAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100070",
        "LiverInjuryVenousBloodBilirubinAssay",
    )


class LiverEvaluationVenousBloodBilirubinAssay(BilirubinIxalphaAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100080",
        "LiverEvaluationVenousBloodBilirubinAssay",
    )


class ComprehensiveMetabolicPanelVenousBloodBilirubinAssay(
    BilirubinIxalphaAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100155",
        "ComprehensiveMetabolicPanelVenousBloodBilirubinAssay",
    )


class HepaticPanelVenousBloodBilirubinAssay(BilirubinIxalphaAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100213",
        "HepaticPanelVenousBloodBilirubinAssay",
    )


class Chem16VenousBloodBilirubinAssay(BilirubinIxalphaAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100246", "Chem16VenousBloodBilirubinAssay"
    )


class LiverFunctionVenousBloodBilirubinAssay(BilirubinIxalphaAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100338",
        "LiverFunctionVenousBloodBilirubinAssay",
    )


class DirectVenousBloodBilirubinAssay(BilirubinIxalphaAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100349", "DirectVenousBloodBilirubinAssay"
    )


class MeasuringGlucoseConcentrationInBloodSerumAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000418",
        "MeasuringGlucoseConcentrationInBloodSerumAssay",
    )


class VenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100072", "VenousBloodGlucoseAssay"
    )


class BasicMetabolicPanelVenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100091",
        "BasicMetabolicPanelVenousBloodGlucoseAssay",
    )


class ArterialBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100123", "ArterialBloodGlucoseAssay"
    )


class ComprehensiveMetabolicPanelVenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100152",
        "ComprehensiveMetabolicPanelVenousBloodGlucoseAssay",
    )


class GemPremierBloodGasVenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100195",
        "GemPremierBloodGasVenousBloodGlucoseAssay",
    )


class FastingVenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100220", "FastingVenousBloodGlucoseAssay"
    )


class Chem11VenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100227", "Chem11VenousBloodGlucoseAssay"
    )


class Chem16VenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100239", "Chem16VenousBloodGlucoseAssay"
    )


class PocChem8ArterialBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100250",
        "PocChem8ArterialBloodGlucoseAssay",
    )


class CerebrospinalFluidGlucoseAssay(GlucoseAssay, CerebrospinalFluidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100267", "CerebrospinalFluidGlucoseAssay"
    )


class Abl90PanelArterialBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100273",
        "Abl90PanelArterialBloodGlucoseAssay",
    )


class Abl90PanelVenousBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100284",
        "Abl90PanelVenousBloodGlucoseAssay",
    )


class Gem4000AnlcooxArterialBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100318",
        "Gem4000AnlcooxArterialBloodGlucoseAssay",
    )


class BodilyFluidGlucoseAssay(GlucoseAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100329", "BodilyFluidGlucoseAssay"
    )


class Gem4ArterialBloodGlucoseAssay(GlucoseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100377", "Gem4ArterialBloodGlucoseAssay"
    )


class VenousBloodMagnesiumAssay(MagnesiumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100073", "VenousBloodMagnesiumAssay"
    )


class Chem11VenousBloodMagnesiumAssay(MagnesiumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100231", "Chem11VenousBloodMagnesiumAssay"
    )


class Chem16VenousBloodMagnesiumAssay(MagnesiumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100237", "Chem16VenousBloodMagnesiumAssay"
    )


class ProteomicProfilingByArrayAssay(MicroarrayAssay, ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001318", "ProteomicProfilingByArrayAssay"
    )


class MicroarrayAssayMeasuringNs1(MicroarrayAssay, ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003543", "MicroarrayAssayMeasuringNs1"
    )


class TransferrinAssay(ProteinAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003013", "TransferrinAssay")


class AdiponectinAssay(ProteinAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003192", "AdiponectinAssay")


class LeptinAssay(ProteinAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003202", "LeptinAssay")


class AlanineAminotransferaseAssay(ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100016", "AlanineAminotransferaseAssay"
    )


class AlkalinePhosphataseHumanAssay(ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100017", "AlkalinePhosphataseHumanAssay"
    )


class AspartateAminotransferaseHumanAssay(ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100019",
        "AspartateAminotransferaseHumanAssay",
    )


class AlbuminAssay(ProteinAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100022", "AlbuminAssay")


class CreatineKinaseAssay(ProteinAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100025", "CreatineKinaseAssay")


class ProstateSpecificAntigenAssay(ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100034", "ProstateSpecificAntigenAssay"
    )


class CReactiveProteinAssay(ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100047", "CReactiveProteinAssay"
    )


class LiverEvaluationVenousBloodProteinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100086",
        "LiverEvaluationVenousBloodProteinAssay",
    )


class VenousBloodHaptoglobinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100109", "VenousBloodHaptoglobinAssay"
    )


class VenousBloodPrealbuninAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100111", "VenousBloodPrealbuninAssay"
    )


class TotalVenousBloodProteinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100118", "TotalVenousBloodProteinAssay"
    )


class ComprehensiveMetabolicPanelVenousBloodProteinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100158",
        "ComprehensiveMetabolicPanelVenousBloodProteinAssay",
    )


class UrineProteinAssay(ProteinAssay, UrineAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100205", "UrineProteinAssay")


class SpepProteinElectrophoresisVenousBloodBetaGlobinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100208",
        "SpepProteinElectrophoresisVenousBloodBetaGlobinAssay",
    )


class SpepProteinElectrophoresisVenousBloodProteinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100210",
        "SpepProteinElectrophoresisVenousBloodProteinAssay",
    )


class HepaticPanelVenousBloodProteinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100212",
        "HepaticPanelVenousBloodProteinAssay",
    )


class VenousBloodGgtAssay(ProteinAssay, BloodAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100223", "VenousBloodGgtAssay")


class _24HourUrineProteinAssay(ProteinAssay, UrineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100262", "_24HourUrineProteinAssay"
    )


class CerebrospinalFluidProteinAssay(ProteinAssay, CerebrospinalFluidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100266", "CerebrospinalFluidProteinAssay"
    )


class BoneProfileVenousBloodProteinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100301",
        "BoneProfileVenousBloodProteinAssay",
    )


class VenousBloodParathyroidHormoneAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100327",
        "VenousBloodParathyroidHormoneAssay",
    )


class TotalBodilyFluidProteinAssay(ProteinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100328", "TotalBodilyFluidProteinAssay"
    )


class LiverFunctionVenousBloodProteinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100342",
        "LiverFunctionVenousBloodProteinAssay",
    )


class VenousBloodCeruloplasminAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100370", "VenousBloodCeruloplasminAssay"
    )


class VenousBloodErythropoietinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100385", "VenousBloodErythropoietinAssay"
    )


class VenousBloodBeta2MicroglobulinAssay(ProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100397",
        "VenousBloodBeta2MicroglobulinAssay",
    )


class TriglycerideConcentrationAssay(TriglycerideAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003173", "TriglycerideConcentrationAssay"
    )


class LipidPanelVenousBloodTriglycerideAssay(TriglycerideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100112",
        "LipidPanelVenousBloodTriglycerideAssay",
    )


class Chem16VenousBloodTriglycerideAssay(TriglycerideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100241",
        "Chem16VenousBloodTriglycerideAssay",
    )


class VenousBloodTriglycerideAssay(TriglycerideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100264", "VenousBloodTriglycerideAssay"
    )


class BodilyFluidTriglycerideAssay(TriglycerideAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100352", "BodilyFluidTriglycerideAssay"
    )


class LipidPanelReflexDirectVenousBloodTriglycerideAssay(TriglycerideAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100399",
        "LipidPanelReflexDirectVenousBloodTriglycerideAssay",
    )


class HighDensityLipoproteinCholesterolConcentrationAssay(
    HighDensityLipoproteinCholesterolAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003157",
        "HighDensityLipoproteinCholesterolConcentrationAssay",
    )


class LipidPanelVenousBloodHighDensityLipoproteinAssay(
    HighDensityLipoproteinCholesterolAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100113",
        "LipidPanelVenousBloodHighDensityLipoproteinAssay",
    )


class LipidPanelReflexDirectVenousBloodHighDensityLipoproteinAssay(
    HighDensityLipoproteinCholesterolAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100401",
        "LipidPanelReflexDirectVenousBloodHighDensityLipoproteinAssay",
    )


class CholesterolConcentrationAssay(CholesterolAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003152", "CholesterolConcentrationAssay"
    )


class LipidPanelVenousBloodCholesterolAssay(CholesterolAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100114",
        "LipidPanelVenousBloodCholesterolAssay",
    )


class TotalVenousBloodCholesterolAssay(CholesterolAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100263", "TotalVenousBloodCholesterolAssay"
    )


class BodilyFluidCholesterolAssay(CholesterolAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100347", "BodilyFluidCholesterolAssay"
    )


class LipidPanelReflexDirectVenousBloodCholesterolAssay(CholesterolAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100400",
        "LipidPanelReflexDirectVenousBloodCholesterolAssay",
    )


class LowDensityLipoproteinCholesterolConcentrationAssay(
    LowDensityLipoproteinCholesterolAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003159",
        "LowDensityLipoproteinCholesterolConcentrationAssay",
    )


class LipidPanelVenousBloodLowDensityLipoproteinAssay(
    LowDensityLipoproteinCholesterolAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100115",
        "LipidPanelVenousBloodLowDensityLipoproteinAssay",
    )


class LipidPanelReflexDirectVenousBloodLowDensityLipoproteinAssay(
    LowDensityLipoproteinCholesterolAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100398",
        "LipidPanelReflexDirectVenousBloodLowDensityLipoproteinAssay",
    )


class ThyroidStimulatingHormoneConcentrationAssay(ThyroidStimulatingHormoneAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003172",
        "ThyroidStimulatingHormoneConcentrationAssay",
    )


class VenousBloodThyroidStimulatingHormoneAssay(
    ThyroidStimulatingHormoneAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100119",
        "VenousBloodThyroidStimulatingHormoneAssay",
    )


class TshReflexFreeT4VenousBloodThyroidStimulatingHormoneAssay(
    ThyroidStimulatingHormoneAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100348",
        "TshReflexFreeT4VenousBloodThyroidStimulatingHormoneAssay",
    )


class FreeThyroxineConcentrationAssay(ThyroxineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003176", "FreeThyroxineConcentrationAssay"
    )


class TotalThyroxineConcentrationAssay(ThyroxineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003177", "TotalThyroxineConcentrationAssay"
    )


class T4UptakeVenousBloodT4Assay(ThyroxineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100122", "T4UptakeVenousBloodT4Assay"
    )


class VenousBloodT4Assay(ThyroxineAssay, BloodAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100294", "VenousBloodT4Assay")


class FreeVenousBloodT4Assay(ThyroxineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100295", "FreeVenousBloodT4Assay"
    )


class HemoglobinOxygenSaturationArterialBloodOxygenAssay(
    ElementalOxygenAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100125",
        "HemoglobinOxygenSaturationArterialBloodOxygenAssay",
    )


class CooximiteryArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100141",
        "CooximiteryArterialBloodOxygenAssay",
    )


class BloodGasVenousBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100166", "BloodGasVenousBloodOxygenAssay"
    )


class NonVentedBloodGasArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100175",
        "NonVentedBloodGasArterialBloodOxygenAssay",
    )


class VentedBloodGasArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100184",
        "VentedBloodGasArterialBloodOxygenAssay",
    )


class GemPremierBloodGasVenousBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100192",
        "GemPremierBloodGasVenousBloodOxygenAssay",
    )


class Abl90PanelArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100272",
        "Abl90PanelArterialBloodOxygenAssay",
    )


class Abl90PanelVenousBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100290", "Abl90PanelVenousBloodOxygenAssay"
    )


class AbgElectrolytesArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100304",
        "AbgElectrolytesArterialBloodOxygenAssay",
    )


class Gem4000AnlcooxArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100313",
        "Gem4000AnlcooxArterialBloodOxygenAssay",
    )


class VenousBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100358", "VenousBloodOxygenAssay"
    )


class Gem4ArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100378", "Gem4ArterialBloodOxygenAssay"
    )


class BloodGasArterialBloodOxygenAssay(ElementalOxygenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100386", "BloodGasArterialBloodOxygenAssay"
    )


class VenousBloodFolicAcidAssay(FolicAcidsAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100131", "VenousBloodFolicAcidAssay"
    )


class VitaminB12AndFolateVenousBloodFolicAcidAssay(FolicAcidsAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100344",
        "VitaminB12AndFolateVenousBloodFolicAcidAssay",
    )


class MethemoglobinPercentageAssay(MethemoglobinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003163", "MethemoglobinPercentageAssay"
    )


class CooximiteryArterialBloodMethemoglobinAssay(MethemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100143",
        "CooximiteryArterialBloodMethemoglobinAssay",
    )


class Abl90PanelVenousBloodMethemoglobinAssay(MethemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100307",
        "Abl90PanelVenousBloodMethemoglobinAssay",
    )


class Abl90PanelArterialBloodMethemoglobinAssay(MethemoglobinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100308",
        "Abl90PanelArterialBloodMethemoglobinAssay",
    )


class BloodGasVenousBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100169",
        "BloodGasVenousBloodBicarbonateAssay",
    )


class NonVentedBloodGasArterialBloodBicarbonateAssay(
    HydrogencarbonateAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100176",
        "NonVentedBloodGasArterialBloodBicarbonateAssay",
    )


class VentedBloodGasArterialBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100183",
        "VentedBloodGasArterialBloodBicarbonateAssay",
    )


class GemPremierBloodGasVenousBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100194",
        "GemPremierBloodGasVenousBloodBicarbonateAssay",
    )


class Abl90PanelArterialBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100281",
        "Abl90PanelArterialBloodBicarbonateAssay",
    )


class Abl90PanelVenousBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100291",
        "Abl90PanelVenousBloodBicarbonateAssay",
    )


class Gem4000AnlcooxArterialBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100312",
        "Gem4000AnlcooxArterialBloodBicarbonateAssay",
    )


class VenousBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100357", "VenousBloodBicarbonateAssay"
    )


class Gem4ArterialBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100371",
        "Gem4ArterialBloodBicarbonateAssay",
    )


class BloodGasArterialBloodBicarbonateAssay(HydrogencarbonateAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100387",
        "BloodGasArterialBloodBicarbonateAssay",
    )


class RandomVenousBloodVancomycinAssay(VancomycinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100172", "RandomVenousBloodVancomycinAssay"
    )


class TroughVenousBloodVancomycinAssay(VancomycinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100211", "TroughVenousBloodVancomycinAssay"
    )


class TroughVenousBloodTobramycinAssay(TobramycinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100199", "TroughVenousBloodTobramycinAssay"
    )


class RandomVenousBloodTobramycinAssay(TobramycinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100200", "RandomVenousBloodTobramycinAssay"
    )


class VenousBloodTobramycinAssay(TobramycinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100206", "VenousBloodTobramycinAssay"
    )


class PeakVenousBloodTobramycinAssay(TobramycinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100257", "PeakVenousBloodTobramycinAssay"
    )


class _335TriiodothyronineConcentrationAssay(_335TriiodothyronineAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003174",
        "_335TriiodothyronineConcentrationAssay",
    )


class TotalVenousBloodT3Assay(_335TriiodothyronineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100261", "TotalVenousBloodT3Assay"
    )


class FreeVenousBloodT3Assay(_335TriiodothyronineAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100350", "FreeVenousBloodT3Assay"
    )


class VenousBloodT3Assay(_335TriiodothyronineAssay, BloodAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100361", "VenousBloodT3Assay")


class VenousBloodBetaHydroxybutryicAcidAssay(_3HydroxybutyricAcidAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100364",
        "VenousBloodBetaHydroxybutryicAcidAssay",
    )


class VenousBloodBetaHydroxybutricAcidAssay(_3HydroxybutyricAcidAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100383",
        "VenousBloodBetaHydroxybutricAcidAssay",
    )


class LiquidChromatographyTandemMassSpectrometry(
    LiquidChromatographyMassSpectrometryAssay, TandemMassSpectrometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHMO_0000701",
        "LiquidChromatographyTandemMassSpectrometry",
    )


class TandemMassTagMassSpectrometryAssay(TandemMassSpectrometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002959",
        "TandemMassTagMassSpectrometryAssay",
    )


class RnaseCl3StructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001005", "RnaseCl3StructureMappingAssay"
    )


class RnaseV1StructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001012", "RnaseV1StructureMappingAssay"
    )


class Dnase1StructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001016", "Dnase1StructureMappingAssay"
    )


class RnaAdaIRnaStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001019", "RnaAdaIRnaStructureMappingAssay"
    )


class RnaseT2StructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001021", "RnaseT2StructureMappingAssay"
    )


class RnaseU2StructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001024", "RnaseU2StructureMappingAssay"
    )


class RnaseT1StructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001030", "RnaseT1StructureMappingAssay"
    )


class NucleaseS1StructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001035", "NucleaseS1StructureMappingAssay"
    )


class ParallelAnalysisOfRnaStructureAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingEnzymaticProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002032",
        "ParallelAnalysisOfRnaStructureAssay",
    )


class DepcStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000897", "DepcStructureMappingAssay"
    )


class CmctStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001006", "CmctStructureMappingAssay"
    )


class MpeFeIiStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001008", "MpeFeIiStructureMappingAssay"
    )


class EnuStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001011", "EnuStructureMappingAssay"
    )


class KethoxalStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001013", "KethoxalStructureMappingAssay"
    )


class DmsStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001015", "DmsStructureMappingAssay"
    )


class RhodiumDnaStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001018", "RhodiumDnaStructureMappingAssay"
    )


class LeadStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001020", "LeadStructureMappingAssay"
    )


class FeBabeRnaStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001023", "FeBabeRnaStructureMappingAssay"
    )


class NmiaRnaStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001026", "NmiaRnaStructureMappingAssay"
    )


class TerbiumRnaStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001027", "TerbiumRnaStructureMappingAssay"
    )


class OhRadicalStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001029", "OhRadicalStructureMappingAssay"
    )


class RutheniumStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001038", "RutheniumStructureMappingAssay"
    )


class InlineProbingRnaStructureMappingAssay(
    SingleNucleotideResolutionNucleicAcidStructureMappingAssayUsingChemicalProbing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001039",
        "InlineProbingRnaStructureMappingAssay",
    )


class FluorescenceQuenchingBindingAssay(BindingAssayUsingFluorescenceDetection):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001979",
        "FluorescenceQuenchingBindingAssay",
    )


class NorthwesternBlotAssay(DirectBindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002172", "NorthwesternBlotAssay"
    )


class SouthwesternBlotAssay(DirectBindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002173", "SouthwesternBlotAssay"
    )


class AntibodyCrossBlockingAssay(CompetitiveInhibitionOfBindingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001699", "AntibodyCrossBlockingAssay"
    )


class BacterialOneHybridAssay(YeastOneHybridAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001682", "BacterialOneHybridAssay"
    )


class GenomicSelex(SystematicEvolutionOfLigandsByExponentialEnrichmentAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002170", "GenomicSelex")


class EpitopeProtectionFromInfectiousChallengeExperiment(EpitopeProtectionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001179",
        "EpitopeProtectionFromInfectiousChallengeExperiment",
    )


class EpitopeProtectionFromTumorChallengeExperiment(EpitopeProtectionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001183",
        "EpitopeProtectionFromTumorChallengeExperiment",
    )


class EpitopeProtectionExperimentBasedOnSurvival(EpitopeProtectionExperiment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001189",
        "EpitopeProtectionExperimentBasedOnSurvival",
    )


class AutofluorescenceMicroscopyAssay(AutofluorescenceAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003088", "AutofluorescenceMicroscopyAssay"
    )


class DecodingAmplifiedTargetedTranscriptsWithFluorescenceInSituHybridizationAssay(
    FluorescenceInSituHybridizationAssay, TranscriptionProfilingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003095",
        "DecodingAmplifiedTargetedTranscriptsWithFluorescenceInSituHybridizationAssay",
    )


class SequentialFluorescenceInSituHybridizationAssay(
    FluorescenceInSituHybridizationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003106",
        "SequentialFluorescenceInSituHybridizationAssay",
    )


class MultiplexedErrorRobustFluorescenceInSituHybridizationAssay(
    FluorescenceInSituHybridizationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003604",
        "MultiplexedErrorRobustFluorescenceInSituHybridizationAssay",
    )


class SingleMoleculeFluorescenceInSituHybridization(
    FluorescenceInSituHybridizationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003605",
        "SingleMoleculeFluorescenceInSituHybridization",
    )


class TranscriptionFactorBindingSiteIdentificationByChipSeqAssay(
    TranscriptionFactorBindingSiteAssay, ChipSeqAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002019",
        "TranscriptionFactorBindingSiteIdentificationByChipSeqAssay",
    )


class ChromatinImmunoprecipitationWithExonucleaseSequencingAssay(ChipSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001925",
        "ChromatinImmunoprecipitationWithExonucleaseSequencingAssay",
    )


class HistoneModificationIdentificationByChipSeqAssay(
    ChipSeqAssay, EpigeneticModificationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002017",
        "HistoneModificationIdentificationByChipSeqAssay",
    )


class TranscriptionCofactorActivityRegionIdentificationByChipSeqAssay(ChipSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002084",
        "TranscriptionCofactorActivityRegionIdentificationByChipSeqAssay",
    )


class MultiplexedIndexedT7ChipSeqAssay(ChipSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002160", "MultiplexedIndexedT7ChipSeqAssay"
    )


class TranscriptionFactorBindingSiteIdentificationByChipChipAssay(
    TranscriptionFactorBindingSiteAssay, ChipChipAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002018",
        "TranscriptionFactorBindingSiteIdentificationByChipChipAssay",
    )


class ChipChipBySnpArrayAssay(ChipChipAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001221", "ChipChipBySnpArrayAssay"
    )


class ChipChipByTilingArrayAssay(ChipChipAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001419", "ChipChipByTilingArrayAssay"
    )


class DnaMethylationProfilingByChipChipAssay(
    ChipChipAssay, EpigeneticModificationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002014",
        "DnaMethylationProfilingByChipChipAssay",
    )


class HistoneModificationIdentificationByChipChipAssay(
    ChipChipAssay, EpigeneticModificationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002016",
        "HistoneModificationIdentificationByChipChipAssay",
    )


class InVivoCellKillingAssay(CellCellKillingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000883", "InVivoCellKillingAssay"
    )


class InVitroCellKillingAssay(CellCellKillingAssay, CellCultureAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000903", "InVitroCellKillingAssay"
    )


class BrduIncorporationAssay(CellProliferationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000664", "BrduIncorporationAssay"
    )


class TritiatedThymidineIncorporationAssay(CellProliferationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000669",
        "TritiatedThymidineIncorporationAssay",
    )


class FluorescenceImagingBasedCellProliferationAssay(CellProliferationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002947",
        "FluorescenceImagingBasedCellProliferationAssay",
    )


class CellProliferationAssayUsingCarboxyfluoresceinSuccinimidylEsterStaining(
    CellProliferationAssay, CarboxyfluoresceinSuccinimidylEsterStainingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003582",
        "CellProliferationAssayUsingCarboxyfluoresceinSuccinimidylEsterStaining",
    )


class TCellActivationInducedMarkerAssay(FlowCytometryAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003230",
        "TCellActivationInducedMarkerAssay",
    )


class ImagingMassCytometryAssay(CytometryTimeOfFlightAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003096", "ImagingMassCytometryAssay"
    )


class MultiplexedIonBeamImagingAssay(CytometryTimeOfFlightAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003100", "MultiplexedIonBeamImagingAssay"
    )


class MyelocyteCountAssay(MyelocyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003165", "MyelocyteCountAssay")


class MetamyelocyteCountAssay(MetamyelocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003161", "MetamyelocyteCountAssay"
    )


class MetamyelocytePercentageAssay(MetamyelocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003162", "MetamyelocytePercentageAssay"
    )


class CbcWithManualDifferentialVenousBloodMetamyelocyteCountAssay(
    MetamyelocyteAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100201",
        "CbcWithManualDifferentialVenousBloodMetamyelocyteCountAssay",
    )


class ErythrocyteAssay(HematocritAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003190", "ErythrocyteAssay")


class ManualHematocritAssay(HematocritAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003191", "ManualHematocritAssay"
    )


class ErythrocyteCountAssay(HematocritAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100011", "ErythrocyteCountAssay"
    )


class NucleateErythrocyteCountAssay(HematocritAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100026", "NucleateErythrocyteCountAssay"
    )


class CbcWithAutomatedDifferentialVenousBloodRbcCountAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100062",
        "CbcWithAutomatedDifferentialVenousBloodRbcCountAssay",
    )


class CbcWithAutomatedDifferentialVenousBloodHematocritAssay(
    HematocritAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100065",
        "CbcWithAutomatedDifferentialVenousBloodHematocritAssay",
    )


class CbcVenousBloodRbcCountAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100074", "CbcVenousBloodRbcCountAssay"
    )


class CbcVenousBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100076", "CbcVenousBloodHematocritAssay"
    )


class CbcWithManualDifferentialVenousBloodNucleatedRbcCountAssay(
    HematocritAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100103",
        "CbcWithManualDifferentialVenousBloodNucleatedRbcCountAssay",
    )


class VenousBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100164", "VenousBloodHematocritAssay"
    )


class ArterialBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100186", "ArterialBloodHematocritAssay"
    )


class GemPremierBloodGasVenousBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100189",
        "GemPremierBloodGasVenousBloodHematocritAssay",
    )


class PocChem8ArterialBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100255",
        "PocChem8ArterialBloodHematocritAssay",
    )


class Abl90PanelArterialBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100278",
        "Abl90PanelArterialBloodHematocritAssay",
    )


class Abl90PanelVenousBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100288",
        "Abl90PanelVenousBloodHematocritAssay",
    )


class CbcWithAutomatedDifferentialVenousBloodNucleatedRbcCountAssay(
    HematocritAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100306",
        "CbcWithAutomatedDifferentialVenousBloodNucleatedRbcCountAssay",
    )


class Gem4000AnlcooxArterialBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100314",
        "Gem4000AnlcooxArterialBloodHematocritAssay",
    )


class HemoglobinAndHematocritVenousBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100353",
        "HemoglobinAndHematocritVenousBloodHematocritAssay",
    )


class VenousBloodNucleatedRbcCountAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100366",
        "VenousBloodNucleatedRbcCountAssay",
    )


class Gem4ArterialBloodHematocritAssay(HematocritAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100379", "Gem4ArterialBloodHematocritAssay"
    )


class CbcWithManualDifferentialVenousBloodPromyelocyteCountAssay(
    PromyelocyteAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100283",
        "CbcWithManualDifferentialVenousBloodPromyelocyteCountAssay",
    )


class BasophilPercentageAssay(BasophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003149", "BasophilPercentageAssay"
    )


class BasophilCountAssay(BasophilAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100005", "BasophilCountAssay")


class AutomatedDifferentialVenousBloodBasophilCountAssay(BasophilAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100056",
        "AutomatedDifferentialVenousBloodBasophilCountAssay",
    )


class CbcWithManualDifferentialVenousBloodBasophilCountAssay(BasophilAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100106",
        "CbcWithManualDifferentialVenousBloodBasophilCountAssay",
    )


class ManualDifferentialBodilyFluidBasophilCountAssay(BasophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100336",
        "ManualDifferentialBodilyFluidBasophilCountAssay",
    )


class CerebrospinalFluidBasophilCountAssay(BasophilAssay, CerebrospinalFluidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100394",
        "CerebrospinalFluidBasophilCountAssay",
    )


class NeutrophilPercentageAssay(NeutrophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003166", "NeutrophilPercentageAssay"
    )


class ImmatureNeutrophilCountAssay(NeutrophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003186", "ImmatureNeutrophilCountAssay"
    )


class ImmatureNeutrophilPercentageAssay(NeutrophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003187",
        "ImmatureNeutrophilPercentageAssay",
    )


class NeutrophilCountAssay(NeutrophilAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100006", "NeutrophilCountAssay")


class SegmentedNeutrophilOfBoneMarrowCountAssay(NeutrophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100027",
        "SegmentedNeutrophilOfBoneMarrowCountAssay",
    )


class AutomatedDifferentialVenousBloodNeutrophilCountAssay(NeutrophilAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100057",
        "AutomatedDifferentialVenousBloodNeutrophilCountAssay",
    )


class CbcWithManualDifferentialVenousBloodBandNeutrophilCountAssay(
    NeutrophilAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100099",
        "CbcWithManualDifferentialVenousBloodBandNeutrophilCountAssay",
    )


class CbcWithManualDifferentialVenousBloodSegmentedNeutrophilCountAssay(
    NeutrophilAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100105",
        "CbcWithManualDifferentialVenousBloodSegmentedNeutrophilCountAssay",
    )


class ManualDifferentialBodilyFluidSegmentedNeutrophilCountAssay(NeutrophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100331",
        "ManualDifferentialBodilyFluidSegmentedNeutrophilCountAssay",
    )


class CbcWithManualDifferentialVenousBloodNeutrophilCountAssay(
    NeutrophilAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100362",
        "CbcWithManualDifferentialVenousBloodNeutrophilCountAssay",
    )


class CerebrospinalFluidSegmentedNeutrophilCountAssay(
    NeutrophilAssay, CerebrospinalFluidAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100391",
        "CerebrospinalFluidSegmentedNeutrophilCountAssay",
    )


class EosinophilPercentageAssay(EosinophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003154", "EosinophilPercentageAssay"
    )


class EosinophilCountAssay(EosinophilAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100007", "EosinophilCountAssay")


class AutomatedDifferentialVenousBloodEosinophilCountAssay(EosinophilAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100058",
        "AutomatedDifferentialVenousBloodEosinophilCountAssay",
    )


class CbcWithManualDifferentialVenousBloodEosinophilCountAssay(
    EosinophilAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100101",
        "CbcWithManualDifferentialVenousBloodEosinophilCountAssay",
    )


class ManualDifferentialBodilyFluidEosinophilCountAssay(EosinophilAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100337",
        "ManualDifferentialBodilyFluidEosinophilCountAssay",
    )


class CerebrospinalFluidEosinophilCountAssay(EosinophilAssay, CerebrospinalFluidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100396",
        "CerebrospinalFluidEosinophilCountAssay",
    )


class LymphocytePercentageAssay(LymphocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003160", "LymphocytePercentageAssay"
    )


class TotalLymphocyteCountAssay(LymphocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003226", "TotalLymphocyteCountAssay"
    )


class TotalLymphocytePercentageAssay(LymphocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003227", "TotalLymphocytePercentageAssay"
    )


class LymphocyteCountAssay(LymphocyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100008", "LymphocyteCountAssay")


class AutomatedDifferentialVenousBloodLymphocyteCountAssay(LymphocyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100059",
        "AutomatedDifferentialVenousBloodLymphocyteCountAssay",
    )


class CbcWithManualDifferentialVenousBloodLymphocyteCountAssay(
    LymphocyteAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100102",
        "CbcWithManualDifferentialVenousBloodLymphocyteCountAssay",
    )


class ManualDifferentialBodilyFluidLymphocyteCountAssay(LymphocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100334",
        "ManualDifferentialBodilyFluidLymphocyteCountAssay",
    )


class CbcWithManualDifferentialVenousBloodPlasmaCellCountAssay(
    LymphocyteAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100384",
        "CbcWithManualDifferentialVenousBloodPlasmaCellCountAssay",
    )


class CerebrospinalFluidLymphocyteCountAssay(LymphocyteAssay, CerebrospinalFluidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100390",
        "CerebrospinalFluidLymphocyteCountAssay",
    )


class MonocytePercentageAssay(MonocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003164", "MonocytePercentageAssay"
    )


class MonocyteCountAssay(MonocyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100009", "MonocyteCountAssay")


class AutomatedDifferentialVenousBloodMonocyteCountAssay(MonocyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100060",
        "AutomatedDifferentialVenousBloodMonocyteCountAssay",
    )


class CbcWithManualDifferentialVenousBloodMonocyteCountAssay(MonocyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100104",
        "CbcWithManualDifferentialVenousBloodMonocyteCountAssay",
    )


class ManualDifferentialBodilyFluidMonocyteCountAssay(MonocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100333",
        "ManualDifferentialBodilyFluidMonocyteCountAssay",
    )


class CerebrospinalFluidMonocyteCountAssay(MonocyteAssay, CerebrospinalFluidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100395",
        "CerebrospinalFluidMonocyteCountAssay",
    )


class ReticulocytePercentageAssay(ReticulocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003170", "ReticulocytePercentageAssay"
    )


class ReticulocyteCountAssay(ReticulocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100038", "ReticulocyteCountAssay"
    )


class CountVenousBloodReticulocyteCountAssay(ReticulocyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100132",
        "CountVenousBloodReticulocyteCountAssay",
    )


class VenousBloodReticulocyteCountAssay(ReticulocyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100346",
        "VenousBloodReticulocyteCountAssay",
    )


class AutomatedCountVenousBloodReticulocyteCountAssay(ReticulocyteAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100368",
        "AutomatedCountVenousBloodReticulocyteCountAssay",
    )


class MacrophageCountAssay(MacrophageAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100050", "MacrophageCountAssay")


class ManualDifferentialBodilyFluidMacrophageCountAssay(MacrophageAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100335",
        "ManualDifferentialBodilyFluidMacrophageCountAssay",
    )


class CerebrospinalFluidMacrophageCountAssay(MacrophageAssay, CerebrospinalFluidAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100393",
        "CerebrospinalFluidMacrophageCountAssay",
    )


class MeanPlateletVolumeAssay(PlateletAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003185", "MeanPlateletVolumeAssay"
    )


class PlateletCountAssay(PlateletAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2100012", "PlateletCountAssay")


class CbcWithAutomatedDifferentialVenousBloodPlateletCountAssay(
    PlateletAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100063",
        "CbcWithAutomatedDifferentialVenousBloodPlateletCountAssay",
    )


class CbcVenousBloodPlateletCountAssay(PlateletAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100077", "CbcVenousBloodPlateletCountAssay"
    )


class LiverFibrosisChronicViralHepatitisVenousBloodPlateletCountAssay(
    PlateletAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100360",
        "LiverFibrosisChronicViralHepatitisVenousBloodPlateletCountAssay",
    )


class LiverFibrosisNafldVenousBloodPlateletCountAssay(PlateletAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100382",
        "LiverFibrosisNafldVenousBloodPlateletCountAssay",
    )


class CellViabilityAssayUsingAnnexinVStaining(CellViabilityAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003584",
        "CellViabilityAssayUsingAnnexinVStaining",
    )


class InVitroCrisprScreenUsingSingleCellRnaSeq(InVitroCrisprScreenAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003660",
        "InVitroCrisprScreenUsingSingleCellRnaSeq",
    )


class InVitroCrisprScreenUsingFlowCytometry(InVitroCrisprScreenAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003661",
        "InVitroCrisprScreenUsingFlowCytometry",
    )


class MedipSeqAssay(DnaMethylationProfilingAssay, ChipAssay, SequencingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000693", "MedipSeqAssay")


class DnaMethylationProfilingByHighThroughputSequencingAssay(
    DnaMethylationProfilingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001266",
        "DnaMethylationProfilingByHighThroughputSequencingAssay",
    )


class DnaMethylationProfilingByArrayAssay(DnaMethylationProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001332",
        "DnaMethylationProfilingByArrayAssay",
    )


class AmplificationOfIntermethylatedSitesAssay(DnaMethylationProfilingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001685",
        "AmplificationOfIntermethylatedSitesAssay",
    )


class PatchClampAssay(IntracellularElectrophysiologyRecordingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002177", "PatchClampAssay")


class VoltageClampAssay(IntracellularElectrophysiologyRecordingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002182", "VoltageClampAssay")


class CurrentClampAssay(IntracellularElectrophysiologyRecordingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002185", "CurrentClampAssay")


class SingleUnitRecording(ExtracellularElectrophysiologyRecordingAssay, CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002187", "SingleUnitRecording")


class MeasuringNeuralActivityInTheCaudateNucleusAssay(
    ExtracellularElectrophysiologyRecordingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000812",
        "MeasuringNeuralActivityInTheCaudateNucleusAssay",
    )


class Electroencephalography(ExtracellularElectrophysiologyRecordingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002186", "Electroencephalography"
    )


class MultiUnitRecording(ExtracellularElectrophysiologyRecordingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002188", "MultiUnitRecording")


class LocalFieldPotentialRecording(ExtracellularElectrophysiologyRecordingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002189", "LocalFieldPotentialRecording"
    )


class HiCAssay(ChromosomeConformationCaptureAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002440", "HiCAssay")


class ProximityLigationAssistedChipSeq(ChromosomeConformationCaptureAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003552", "ProximityLigationAssistedChipSeq"
    )


class ForcedCoughAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003504", "ForcedCoughAssessment"
    )


class SpeechTestAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003505", "SpeechTestAssessment")


class FingerToFingerAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003506", "FingerToFingerAssessment"
    )


class NoseToFingerAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003507", "NoseToFingerAssessment"
    )


class DysmetriaAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003508", "DysmetriaAssessment")


class RapidAlternatingHandsAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003509", "RapidAlternatingHandsAssessment"
    )


class FingerTapsAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003510", "FingerTapsAssessment")


class HeelAlongShinAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003511", "HeelAlongShinAssessment"
    )


class HeelToShinAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003512", "HeelToShinAssessment")


class MuscleWeaknessAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003514", "MuscleWeaknessAssessment"
    )


class VibratorySenseAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003515", "VibratorySenseAssessment"
    )


class PositionSenseAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003516", "PositionSenseAssessment"
    )


class DeepTendonReflexAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003517", "DeepTendonReflexAssessment"
    )


class LimitsOfStabilityAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003518", "LimitsOfStabilityAssessment"
    )


class BulbarAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003528", "BulbarAssessment")


class SpontaneousSpeechAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003529", "SpontaneousSpeechAssessment"
    )


class LimbCoordinationAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003530", "LimbCoordinationAssessment"
    )


class NervousSystemFunctionalityAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003533",
        "NervousSystemFunctionalityAssessment",
    )


class UprightStabilityAssessment(FunctionalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003534", "UprightStabilityAssessment"
    )


class FacialAtrophyAssessment(ObservationalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003502", "FacialAtrophyAssessment"
    )


class TongueAtrophyAssessment(ObservationalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003503", "TongueAtrophyAssessment"
    )


class MuscleAtrophyAssessment(ObservationalAssessmentOfIndividual):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003513", "MuscleAtrophyAssessment"
    )


class OlinkAssay(ProximityExtensionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003112", "OlinkAssay")


class ChromosomeConformationCaptureSequencingAssay(
    ChromosomeConformationCaptureOnChipAssay, SequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002597",
        "ChromosomeConformationCaptureSequencingAssay",
    )


class MultiplexRealTimePolymeraseChainReactionAssay(
    RealTimePolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003287",
        "MultiplexRealTimePolymeraseChainReactionAssay",
    )


class MultiplexRealTimeReverseTranscriptionPolymeraseChainReactionAssay(
    RealTimeReverseTranscriptionPolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003288",
        "MultiplexRealTimeReverseTranscriptionPolymeraseChainReactionAssay",
    )


class InsecticideResistanceByAmplificationRefractoryMutationSystemAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002719",
        "InsecticideResistanceByAmplificationRefractoryMutationSystemAssay",
    )


class InsecticideResistanceByPrimerIntroducedRestrictionAnalysisPcrAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002720",
        "InsecticideResistanceByPrimerIntroducedRestrictionAnalysisPcrAssay",
    )


class InsecticideResistanceByNestedPolymeraseChainReactionAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002721",
        "InsecticideResistanceByNestedPolymeraseChainReactionAssay",
    )


class InsecticideResistanceByPcrAmplificationOfSpecificAllelesAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002724",
        "InsecticideResistanceByPcrAmplificationOfSpecificAllelesAssay",
    )


class InsecticideResistanceByFluorogenicPcrAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002725",
        "InsecticideResistanceByFluorogenicPcrAssay",
    )


class InsecticideResistanceByPcrRflpAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002726",
        "InsecticideResistanceByPcrRflpAssay",
    )


class InsecticideResistanceByShortInterspersedElementsPcrAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002727",
        "InsecticideResistanceByShortInterspersedElementsPcrAssay",
    )


class InsecticideResistanceByLigaseDetectionReactionAssay(
    InsecticideResistanceByMonitoringKnownMutationsAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002722",
        "InsecticideResistanceByLigaseDetectionReactionAssay",
    )


class InsecticideResistanceByDetectingAlphaEsteraseActivityAssay(
    InsecticideResistanceByDetectingEnzymeActivityAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002699",
        "InsecticideResistanceByDetectingAlphaEsteraseActivityAssay",
    )


class InsecticideResistanceByDetectingBetaEsteraseActivityAssay(
    InsecticideResistanceByDetectingEnzymeActivityAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002700",
        "InsecticideResistanceByDetectingBetaEsteraseActivityAssay",
    )


class InsecticideResistanceByDetectingAcetylcholinesteraseActivityAssay(
    InsecticideResistanceByDetectingEnzymeActivityAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002701",
        "InsecticideResistanceByDetectingAcetylcholinesteraseActivityAssay",
    )


class InsecticideResistanceByDetectingGlutathioneSTransferaseActivityAssay(
    InsecticideResistanceByDetectingEnzymeActivityAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002702",
        "InsecticideResistanceByDetectingGlutathioneSTransferaseActivityAssay",
    )


class InsecticideResistanceByDetectingCarboxylicEsterHydrolaseActivityAssay(
    InsecticideResistanceByDetectingEnzymeActivityAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002703",
        "InsecticideResistanceByDetectingCarboxylicEsterHydrolaseActivityAssay",
    )


class InsecticideResistanceByDetectingMixedFunctionOxidaseAssay(
    InsecticideResistanceByDetectingEnzymeActivityAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002704",
        "InsecticideResistanceByDetectingMixedFunctionOxidaseAssay",
    )


class DirectInsecticideResistanceBioassay(InsecticideResistanceBioassay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002705",
        "DirectInsecticideResistanceBioassay",
    )


class TopicalApplicationInsecticideResistanceBioassay(InsecticideResistanceBioassay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002706",
        "TopicalApplicationInsecticideResistanceBioassay",
    )


class TargetedDrugModulatedMassSpectrometryBasedProteinPhoshporylationStateAssay(
    MassSpectrometryBasedProteinStateAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002956",
        "TargetedDrugModulatedMassSpectrometryBasedProteinPhoshporylationStateAssay",
    )


class _96WellNeutralizationAssay(SerumNeutralizationOfViralInfectivityAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000865", "_96WellNeutralizationAssay"
    )


class UmbilicalCordBloodMicrobiologyAssay(
    BloodMicrobiologyAssay, UmbilicalCordBloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003284",
        "UmbilicalCordBloodMicrobiologyAssay",
    )


class VenousBloodMicrobiologyAssay(BloodMicrobiologyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003321", "VenousBloodMicrobiologyAssay"
    )


class PlacentalBloodMicrobiologyAssay(BloodMicrobiologyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003381", "PlacentalBloodMicrobiologyAssay"
    )


class VectortestAssay(PathogenDetectionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002729", "VectortestAssay")


class PathogenDetectionByRapidAnalyteMeasurementPlatformAssay(PathogenDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002730",
        "PathogenDetectionByRapidAnalyteMeasurementPlatformAssay",
    )


class PathogenDetectionByLoopMediatedIsothermalAmplificationAssay(
    PathogenDetectionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002731",
        "PathogenDetectionByLoopMediatedIsothermalAmplificationAssay",
    )


class ParasiteDetectionByPcrAssay(ParasiteDetectionAssay, PolymeraseChainReactionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003045", "ParasiteDetectionByPcrAssay"
    )


class MalariaRapidDiagnosisAssay(ParasiteDetectionAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003037", "MalariaRapidDiagnosisAssay"
    )


class FalcivaxRapidDiagnosticTest(ParasiteDetectionAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003041", "FalcivaxRapidDiagnosticTest"
    )


class OptimalItRapidDiagnosticTest(ParasiteDetectionAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003042", "OptimalItRapidDiagnosticTest"
    )


class PlasmodiumGametocyteDetectionAssay(ParasiteDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003036",
        "PlasmodiumGametocyteDetectionAssay",
    )


class RnaiKnockdownAssay(GeneKnockDownAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002628", "RnaiKnockdownAssay")


class SingleNucleusAtacSeq(AssayForTransposaseAccessibleChromatinUsingSequencing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002762", "SingleNucleusAtacSeq")


class SingleCellAtacSeq(AssayForTransposaseAccessibleChromatinUsingSequencing):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002764", "SingleCellAtacSeq")


class BulkAssayForTransposaseAccessibleChromatinUsingSequencing(
    AssayForTransposaseAccessibleChromatinUsingSequencing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003089",
        "BulkAssayForTransposaseAccessibleChromatinUsingSequencing",
    )


class SingleCellCombinatorialIndexingAssayForTransposaseAccessessableChromatinUsingSequencing(
    AssayForTransposaseAccessibleChromatinUsingSequencing
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003104",
        "SingleCellCombinatorialIndexingAssayForTransposaseAccessessableChromatinUsingSequencing",
    )


class HeartRateVariabilityAssay(PulseRateAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003717", "HeartRateVariabilityAssay"
    )


class Immunocytochemistry(ImmunoStainingAssay, CytometryAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002174", "Immunocytochemistry")


class Immunohistochemistry(ImmunoStainingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001986", "Immunohistochemistry")


class _3DNeuralCellStructureDeterminationAssay(_3DCellStructureDeterminationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003123",
        "_3DNeuralCellStructureDeterminationAssay",
    )


class Nmr3DMolecularStructureDeterminationAssay(
    _3DMolecularStructureDeterminationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000182",
        "Nmr3DMolecularStructureDeterminationAssay",
    )


class XRayCrystallography3DMolecularStructureDeterminationAssay(
    _3DMolecularStructureDeterminationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000912",
        "XRayCrystallography3DMolecularStructureDeterminationAssay",
    )


class _3DStructureDeterminationOfBoundMolecularComplexAssay(
    _3DMolecularStructureDeterminationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001145",
        "_3DStructureDeterminationOfBoundMolecularComplexAssay",
    )


class SmallAngleScattering3DMolecularStructureDeterminationAssay(
    _3DMolecularStructureDeterminationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002108",
        "SmallAngleScattering3DMolecularStructureDeterminationAssay",
    )


class ElectronMicroscopy3DMolecularStructureDeterminationAssay(
    _3DMolecularStructureDeterminationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003118",
        "ElectronMicroscopy3DMolecularStructureDeterminationAssay",
    )


class IndividualNucleotideResolutionCrossLinkingAndImmunoprecipitationSequencingAssay(
    CrossLinkingImmunoprecipitationHighThroughputSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002043",
        "IndividualNucleotideResolutionCrossLinkingAndImmunoprecipitationSequencingAssay",
    )


class BisulfiteSequencingAssay(DnaMethylationProfilingAssay, DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000748", "BisulfiteSequencingAssay"
    )


class CarbonCopyChromosomeConformationCaptureAssay(
    DnaSequencingAssay, PolymeraseChainReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001919",
        "CarbonCopyChromosomeConformationCaptureAssay",
    )


class DnaSequencingByLigationAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000723", "DnaSequencingByLigationAssay"
    )


class DnaSequencingBySynthesisAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000734", "DnaSequencingBySynthesisAssay"
    )


class StructuralAnalysisByPairedEndTagSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001849",
        "StructuralAnalysisByPairedEndTagSequencingAssay",
    )


class DnaseIHypersensitiveSitesSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001853",
        "DnaseIHypersensitiveSitesSequencingAssay",
    )


class MicrococcalNucleaseDigestionFollowedByHighThroughputSequencingAssay(
    DnaSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001924",
        "MicrococcalNucleaseDigestionFollowedByHighThroughputSequencingAssay",
    )


class WholeGenomeSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002117", "WholeGenomeSequencingAssay"
    )


class ExomeSequencingAssay(DnaSequencingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002118", "ExomeSequencingAssay")


class ExtrachromosomalCircularDnaSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002144",
        "ExtrachromosomalCircularDnaSequencingAssay",
    )


class WholeMetagenomeSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002623", "WholeMetagenomeSequencingAssay"
    )


class CleavageUnderTargetsAndReleaseUsingNucleaseAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003033",
        "CleavageUnderTargetsAndReleaseUsingNucleaseAssay",
    )


class CleavageUnderTargetsAndTagmentation(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003034",
        "CleavageUnderTargetsAndTagmentation",
    )


class TyramideSignalAmplificationSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003297",
        "TyramideSignalAmplificationSequencingAssay",
    )


class NucleolusAssociatedDomainSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003300",
        "NucleolusAssociatedDomainSequencingAssay",
    )


class TransposaseMediatedAnalysisOfChromatinLoopingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003309",
        "TransposaseMediatedAnalysisOfChromatinLoopingAssay",
    )


class GenomeArchitectureMappingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003313", "GenomeArchitectureMappingAssay"
    )


class LinkedReadSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003412", "LinkedReadSequencingAssay"
    )


class PooledCloneSequencingAssay(DnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100402", "PooledCloneSequencingAssay"
    )


class ProCap(RnaSequencingAssay, PolymeraseChainReactionAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002753", "ProCap")


class RnaSeqAssay(RnaSequencingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001271", "RnaSeqAssay")


class DirectRnaSequencingAssay(RnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002629", "DirectRnaSequencingAssay"
    )


class _16SRibosomalGeneSequencingAssay(
    AmpliconSequencingAssay, TaxonomicDiversityAssessmentByTargetedGeneSurvey
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002763", "_16SRibosomalGeneSequencingAssay"
    )


class SingleCellTCellReceptorRepertoireSequencingAssay(
    TCellReceptorRepertoireSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003599",
        "SingleCellTCellReceptorRepertoireSequencingAssay",
    )


class SingleCellBCellReceptorRepertoireSequencingAssay(
    BCellReceptorRepertoireSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003598",
        "SingleCellBCellReceptorRepertoireSequencingAssay",
    )


class DnaSplitPoolRecognitionOfInteractionsAndTagExtensionAssay(
    SplitPoolRecognitionOfInteractionsAndTagExtensionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003311",
        "DnaSplitPoolRecognitionOfInteractionsAndTagExtensionAssay",
    )


class RnaDnaSplitPoolRecognitionOfInteractionsAndTagExtensionAssay(
    SplitPoolRecognitionOfInteractionsAndTagExtensionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003312",
        "RnaDnaSplitPoolRecognitionOfInteractionsAndTagExtensionAssay",
    )


class AssayMeasuringMhcLigandProcessingAndPresentation(MhcLigandAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110125",
        "AssayMeasuringMhcLigandProcessingAndPresentation",
    )


class AssayMeasuringBindingOfAMhcLigandComplex(MhcLigandAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110126",
        "AssayMeasuringBindingOfAMhcLigandComplex",
    )


class AssayMeasuringBiologicalActivityResultingFromBCellEpitopeAntibodyBinding(
    BCellEpitopeAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001706",
        "AssayMeasuringBiologicalActivityResultingFromBCellEpitopeAntibodyBinding",
    )


class AssayMeasuringBindingOfABCellEpitopeAntibodyComplex(BCellEpitopeAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110127",
        "AssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding(
    TCellEpitopeAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002055",
        "AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding",
    )


class AssayMeasuringBindingOfATCellEpitopeMhcTcrComplex(TCellEpitopeAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110037",
        "AssayMeasuringBindingOfATCellEpitopeMhcTcrComplex",
    )


class DnaRestrictionEnzymeDigestion(SpecificEnzymaticCleavage):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600055", "DnaRestrictionEnzymeDigestion"
    )


class Trypsination(ProteaseCleavage):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302891", "Trypsination")


class Injection(AddingAMaterialEntityIntoATarget):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000426", "Injection")


class AdministrationOfMaterialToSpecimen(AddingAMaterialEntityIntoATarget):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000995",
        "AdministrationOfMaterialToSpecimen",
    )


class AddingSubstanceToCellCulture(AddingAMaterialEntityIntoATarget):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600000", "AddingSubstanceToCellCulture"
    )


class AdministeringSubstanceInVivo(AddingAMaterialEntityIntoATarget):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0600007", "AdministeringSubstanceInVivo"
    )


class Electrocution(AnimalEuthanization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302895", "Electrocution")


class CervicalDislocation(AnimalEuthanization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302896", "CervicalDislocation")


class Asphyxiation(AnimalEuthanization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302897", "Asphyxiation")


class IntentionalOverdosing(AnimalEuthanization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0302898", "IntentionalOverdosing"
    )


class Decapitation(AnimalEuthanization):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0302899", "Decapitation")


class IsolationOfAdherentCells(IsolationOfCellPopulation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000540", "IsolationOfAdherentCells"
    )


class IsolationOfPbmcs(IsolationOfCellPopulation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000548", "IsolationOfPbmcs")


class ChromatinImmunoprecipitation(Immunoprecipitation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_00001975", "ChromatinImmunoprecipitation"
    )


class AntibodyPurificationOfMhcProteinComplex(Purification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003615",
        "AntibodyPurificationOfMhcProteinComplex",
    )


class NucleicAcidExtraction(Extraction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0666667", "NucleicAcidExtraction"
    )


class WaterFiltration(Filtration):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003656", "WaterFiltration")


class LiquidChromatography(PreparativeChromatography):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003547", "LiquidChromatography")


class Immunoelectrophoresis(Electrophoresis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002685", "Immunoelectrophoresis"
    )


class CounterCurrentImmunoelectrophoresis(Electrophoresis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002686",
        "CounterCurrentImmunoelectrophoresis",
    )


class Leukapheresis(BloodHarvesting):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003231", "Leukapheresis")


class EstablishingCancerCellLine(EstablishingCellLine):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000867", "EstablishingCancerCellLine"
    )


class CellLineImmortalization(EstablishingCellLine):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000877", "CellLineImmortalization"
    )


class DnaTransfection(Transfection):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0600060", "DnaTransfection")


class SiteDirectedMutagenesis(InducedMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002619", "SiteDirectedMutagenesis"
    )


class RandomMutagenesis(InducedMutagenesis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002620", "RandomMutagenesis")


class DirectedMutagenesis(InducedMutagenesis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003131", "DirectedMutagenesis")


class RnaiGeneKnockdown(GeneKnockdown):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002626", "RnaiGeneKnockdown")


class MultiplexLigationMediatedAmplification(PolymeraseChainReaction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001914",
        "MultiplexLigationMediatedAmplification",
    )


class InversePolymeraseChainReaction(PolymeraseChainReaction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002598", "InversePolymeraseChainReaction"
    )


class ShortInterspersedNuclearElementsPolymeraseChainReaction(PolymeraseChainReaction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002683",
        "ShortInterspersedNuclearElementsPolymeraseChainReaction",
    )


class NestedPolymeraseChainReaction(PolymeraseChainReaction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002684", "NestedPolymeraseChainReaction"
    )


class RapidAmplificationOfCdnaEnds(ReverseTranscribedPolymeraseChainReaction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002090", "RapidAmplificationOfCdnaEnds"
    )


class LigaseDetectionReaction(LinearAmplification):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002687", "LigaseDetectionReaction"
    )


class EggSpecimenCollectionProcess(AquaticArthropodSpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003051", "EggSpecimenCollectionProcess"
    )


class LarvalSpecimenCollectionProcess(AquaticArthropodSpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003052", "LarvalSpecimenCollectionProcess"
    )


class PupalSpecimenCollectionProcess(AquaticArthropodSpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003053", "PupalSpecimenCollectionProcess"
    )


class AdultArthropodSpecimenCollectionProcess(LiveArthropodSpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002904",
        "AdultArthropodSpecimenCollectionProcess",
    )


class KnockdownArthropodSpecimenCollectionProcess(
    LiveArthropodSpecimenCollectionProcess
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002918",
        "KnockdownArthropodSpecimenCollectionProcess",
    )


class NeedleBiopsy(Biopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002654", "NeedleBiopsy")


class SurgicalBiopsy(Biopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002657", "SurgicalBiopsy")


class AbdominalWallFatPadBiopsy(Biopsy):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002660", "AbdominalWallFatPadBiopsy"
    )


class TailBiopsy(Biopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002661", "TailBiopsy")


class BoneMarrowBiopsy(Biopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002662", "BoneMarrowBiopsy")


class SkinpunchBiopsy(Biopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002663", "SkinpunchBiopsy")


class MaterialStorageService(MaterialMaintenanceService):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001557", "MaterialStorageService"
    )


class SequencingService(MaterialAnalysisService):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001904", "SequencingService")


class FamilyWiseErrorRateCorrectionMethod(MultipleTestingCorrectionMethod):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200073",
        "FamilyWiseErrorRateCorrectionMethod",
    )


class GeneralizedFamilyWiseErrorRateCorrectionMethod(MultipleTestingCorrectionMethod):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200160",
        "GeneralizedFamilyWiseErrorRateCorrectionMethod",
    )


class QuantileNumberOfFalsePositivesCorrectionMethod(MultipleTestingCorrectionMethod):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200161",
        "QuantileNumberOfFalsePositivesCorrectionMethod",
    )


class TailProbabilityForTheProportionOfFalsePositivesCorrectionMethod(
    MultipleTestingCorrectionMethod
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200162",
        "TailProbabilityForTheProportionOfFalsePositivesCorrectionMethod",
    )


class FalseDiscoveryRateCorrectionMethod(MultipleTestingCorrectionMethod):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200163",
        "FalseDiscoveryRateCorrectionMethod",
    )


class ProportionOfExpectedFalsePositivesCorrectionMethod(
    MultipleTestingCorrectionMethod
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200164",
        "ProportionOfExpectedFalsePositivesCorrectionMethod",
    )


class QuantileProportionOfFalsePositivesCorrectionMethod(
    MultipleTestingCorrectionMethod
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200165",
        "QuantileProportionOfFalsePositivesCorrectionMethod",
    )


class Gating(DataVectorReductionDataTransformation, PartitioningDataTransformation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200077", "Gating")


class WeightedNetworkGraphConstruction(NetworkGraphConstruction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200127", "WeightedNetworkGraphConstruction"
    )


class DirectedNetworkGraphConstruction(NetworkGraphConstruction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200128", "DirectedNetworkGraphConstruction"
    )


class NodeDegreeCalculation(NodeQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200130", "NodeDegreeCalculation"
    )


class QuantitativeNodeDegreeCalculation(NodeQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200131",
        "QuantitativeNodeDegreeCalculation",
    )


class NodeInDegreeCalculation(NodeQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200132", "NodeInDegreeCalculation"
    )


class NodeOutDegreeCalculation(NodeQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200133", "NodeOutDegreeCalculation"
    )


class NodeShortestPathIdentification(NodeQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200134", "NodeShortestPathIdentification"
    )


class EdgeBetweennessCalculation(EdgeQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200136", "EdgeBetweennessCalculation"
    )


class SubgraphDegreeCalculation(NetworkSubgraphQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200138", "SubgraphDegreeCalculation"
    )


class QuantitativeSubgraphDegreeCalculation(NetworkSubgraphQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200139",
        "QuantitativeSubgraphDegreeCalculation",
    )


class SubgraphInDegreeCalculation(NetworkSubgraphQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200143", "SubgraphInDegreeCalculation"
    )


class SubgraphOutDegreeCalculation(NetworkSubgraphQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200144", "SubgraphOutDegreeCalculation"
    )


class IntraSubgraphConnectivityCalculation(NetworkSubgraphQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200145",
        "IntraSubgraphConnectivityCalculation",
    )


class SubgraphModularityCalculation(NetworkSubgraphQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200146", "SubgraphModularityCalculation"
    )


class GlobalModularityCalculation(NetworkGraphQualityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200054", "GlobalModularityCalculation"
    )


class LiquidChromatographyTandemMassSpectrometryAnalysis(
    TandemMassSpectrometryAnalysis, LiquidChromatrographyMassSpectrometryAnalysis
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003649",
        "LiquidChromatographyTandemMassSpectrometryAnalysis",
    )


class LowessGroupTransformation(LowessTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001474", "LowessGroupTransformation"
    )


class LowessGlobalTransformation(LowessTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001481", "LowessGlobalTransformation"
    )


class DyeSwapMerge(ReplicateAnalysis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200055", "DyeSwapMerge")


class LoessGlobalTransformation(LoessTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200023", "LoessGlobalTransformation"
    )


class LoessGroupTransformation(LoessTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200024", "LoessGroupTransformation"
    )


class KFoldCrossValidationMethod(StatisticalModelValidation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200032", "KFoldCrossValidationMethod"
    )


class LeaveOneOutCrossValidationMethod(StatisticalModelValidation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200033", "LeaveOneOutCrossValidationMethod"
    )


class JackknifingMethod(StatisticalModelValidation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200034", "JackknifingMethod")


class Boostrapping(StatisticalModelValidation):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200035", "Boostrapping")


class EuclideanDistanceCalculation(SimilarityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200114", "EuclideanDistanceCalculation"
    )


class PearsonCorrelationCoefficientCalculation(SimilarityCalculation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200115",
        "PearsonCorrelationCoefficientCalculation",
    )


class AgglomerativeHierarchicalClustering(HierarchicalClustering):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200154",
        "AgglomerativeHierarchicalClustering",
    )


class DivisiveHierarchicalClustering(HierarchicalClustering):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200155", "DivisiveHierarchicalClustering"
    )


class PrincipalComponentsAnalysisDimensionalityReduction(DimensionalityReduction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200051",
        "PrincipalComponentsAnalysisDimensionalityReduction",
    )


class SubmatrixExtraction(DimensionalityReduction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0200074", "SubmatrixExtraction")


class LoessScaleGroupTransformationOneChannel(LoessScaleGroupTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200010",
        "LoessScaleGroupTransformationOneChannel",
    )


class LoessScaleGroupTransformationTwoChannel(LoessScaleGroupTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200012",
        "LoessScaleGroupTransformationTwoChannel",
    )


class RestrictionEnzyme(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000732", "RestrictionEnzyme")


class Cd4Molecule(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000001004", "Cd4Molecule")


class Cd3SubunitWithImmunoglobulinDomain(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000001018",
        "Cd3SubunitWithImmunoglobulinDomain",
    )


class ProstateSpecificAntigen(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000003015", "ProstateSpecificAntigen"
    )


class AntithrombinIii(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000003252", "AntithrombinIii")


class DoubleStrandedRnaSpecificAdenosineDeaminase(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000003745",
        "DoubleStrandedRnaSpecificAdenosineDeaminase",
    )


class Adiponectin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000003777", "Adiponectin")


class Albumin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000003918", "Albumin")


class Beta2Microglobulin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000004580", "Beta2Microglobulin")


class Ceruloplasmin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000005794", "Ceruloplasmin")


class CReactiveProtein(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000005897", "CReactiveProtein")


class Deoxyribonuclease1(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000006592", "Deoxyribonuclease1")


class Erythropoietin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000007141", "Erythropoietin")


class GlialCellLineDerivedNeurotrophicFactor(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000007928",
        "GlialCellLineDerivedNeurotrophicFactor",
    )


class BetaGlobin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000008457", "BetaGlobin")


class Haptoglobin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000008725", "Haptoglobin")


class Leptin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000009758", "Leptin")


class ParathyroidHormone(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000013429", "ParathyroidHormone")


class RibonucleaseT2(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000014060", "RibonucleaseT2")


class Serotransferrin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000016261", "Serotransferrin")


class Transthyretin(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000016801", "Transthyretin")


class DnaLigase(Protein, Enzyme):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000023089", "DnaLigase")


class TCellReceptorCoReceptorCd8(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000025402", "TCellReceptorCoReceptorCd8"
    )


class GuanylSpecificRibonucleaseT1(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000025467", "GuanylSpecificRibonucleaseT1"
    )


class NucleaseS1(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000025471", "NucleaseS1")


class RibonucleaseU2(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000025475", "RibonucleaseU2")


class RibonucleaseV1Cobra(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000025477", "RibonucleaseV1Cobra")


class RibonucleaseCl3Chicken(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000025478", "RibonucleaseCl3Chicken"
    )


class CreatineKinase(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000029971", "CreatineKinase")


class ProteinGlutamineGammaGlutamyltransferase(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000029983",
        "ProteinGlutamineGammaGlutamyltransferase",
    )


class Ns1(Protein):
    term = RdfTerm("http://purl.obolibrary.org/obo/PR_000036824", "Ns1")


class AlanineAminotransferase(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000050219", "AlanineAminotransferase"
    )


class AlkalinePhosphataseHuman(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000050343", "AlkalinePhosphataseHuman"
    )


class AspartateAminotransferaseHuman(Protein):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PR_000050353", "AspartateAminotransferaseHuman"
    )


class DoubleStrandedDna(DeoxyribonucleicAcid):
    term = RdfTerm("http://purl.obolibrary.org/obo/CHEBI_4705", "DoubleStrandedDna")


class AmplifiedDna(DeoxyribonucleicAcid, ProcessedMaterial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000809", "AmplifiedDna")


class ForwardPcrPrimer(DeoxyribonucleicAcid, Reagent):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001946", "ForwardPcrPrimer")


class ReversePcrPrimer(DeoxyribonucleicAcid, Reagent):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001951", "ReversePcrPrimer")


class MultiplexingSequenceIdentifier(DeoxyribonucleicAcid):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001967", "MultiplexingSequenceIdentifier"
    )


class AlphaBetaTCell(TCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000789", "AlphaBetaTCell")


class PlasmaCell(BCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000786", "PlasmaCell")


class HlaCProteinComplex(HumanMhcClassIProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0001149", "HlaCProteinComplex")


class H2DdProteinComplex(MouseMhcClassIProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000967", "H2DdProteinComplex")


class H2KdProteinComplex(MouseMhcClassIProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000992", "H2KdProteinComplex")


class H2KsProteinComplex(MouseMhcClassIProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000994", "H2KsProteinComplex")


class H2LdProteinComplex(MouseMhcClassIProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000997", "H2LdProteinComplex")


class MouseMhcClassIProteinComplexWithH2BHaplotype(MouseMhcClassIProteinComplex):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/MRO_0001759",
        "MouseMhcClassIProteinComplexWithH2BHaplotype",
    )


class H2DqProteinComplex(MouseMhcClassIProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0002026", "H2DqProteinComplex")


class H2KqProteinComplex(MouseMhcClassIProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0002027", "H2KqProteinComplex")


class HlaDrProteinComplex(HumanMhcClassIiProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000013", "HlaDrProteinComplex")


class HlaDpProteinComplex(HumanMhcClassIiProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0001167", "HlaDpProteinComplex")


class H2IaProteinComplex(MouseMhcClassIiProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000971", "H2IaProteinComplex")


class CellLineCell(SecondaryCulturedCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CLO_0000001", "CellLineCell")


class ApolloConsole(TecmagNmrConsole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000483", "ApolloConsole")


class DiscoveryConsole(TecmagNmrConsole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000513", "DiscoveryConsole")


class BrukerUs2NmrMagnet(BrukerNmrMagnet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000467", "BrukerUs2NmrMagnet")


class BrukerUltrashieldPlusNmrMagnet(BrukerNmrMagnet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000530", "BrukerUltrashieldPlusNmrMagnet"
    )


class BrukerUltrashieldNmrMagnet(BrukerNmrMagnet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000567", "BrukerUltrashieldNmrMagnet"
    )


class BrukerUltrastabilizedNmrMagnet(BrukerNmrMagnet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000575", "BrukerUltrastabilizedNmrMagnet"
    )


class BrukerNmrCaseSampleChanger(BrukerAutosampler):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000473", "BrukerNmrCaseSampleChanger"
    )


class BrukerBAcsSystem(BrukerAutosampler):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000492", "BrukerBAcsSystem")


class BrukerBestNmrSystem(BrukerAutosampler):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000591", "BrukerBestNmrSystem")


class BrukerSamplejetSystem(BrukerAutosampler):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000624", "BrukerSamplejetSystem"
    )


class TandemMassSpectrometer(MassSpectrometer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001088", "TandemMassSpectrometer"
    )


class IonSemiconductorChip(IonDetector):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001973", "IonSemiconductorChip")


class PositronEmissionTomographyScanner(ImageCreationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000933",
        "PositronEmissionTomographyScanner",
    )


class ComputedTomographyScanner(ImageCreationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000982", "ComputedTomographyScanner"
    )


class DigitalCamera(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001048", "DigitalCamera")


class SpectScanner(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001068", "SpectScanner")


class SmallAnimalImageAcquisitionDevice(ImageCreationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001077",
        "SmallAnimalImageAcquisitionDevice",
    )


class InfraredImageAcquisitionDevice(ImageCreationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001078", "InfraredImageAcquisitionDevice"
    )


class GelImagingSystem(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001081", "GelImagingSystem")


class RadiographyInstrument(ImageCreationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001085", "RadiographyInstrument"
    )


class UltrasoundMachine(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001098", "UltrasoundMachine")


class ImmunoblotScanner(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001099", "ImmunoblotScanner")


class BeadArrayReader(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001109", "BeadArrayReader")


class ArrayScanner(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400104", "ArrayScanner")


class ImageCytometer(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400135", "ImageCytometer")


class MultispectralImagingFlowCytometer(ImageCreationDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400146",
        "MultispectralImagingFlowCytometer",
    )


class Microscope(ImageCreationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400169", "Microscope")


class SolidNmrProbe(NmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000479", "SolidNmrProbe")


class DirectDetectionNmrProbe(NmrProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000491", "DirectDetectionNmrProbe"
    )


class FlowProbe(NmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000519", "FlowProbe")


class JeolNmrProbe(NmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000529", "JeolNmrProbe")


class ImagingNmrProbe(NmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000539", "ImagingNmrProbe")


class LiquidNmrProbe(NmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000559", "LiquidNmrProbe")


class BrukerNmrProbe(NmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000561", "BrukerNmrProbe")


class IndirectDetectionProbe(NmrProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000640", "IndirectDetectionProbe"
    )


class ContinuousWaveNmrInstrument(NmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000486", "ContinuousWaveNmrInstrument"
    )


class FourierTransformationNmrInstrument(NmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000487",
        "FourierTransformationNmrInstrument",
    )


class TecmagNmrInstrument(NmrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000534", "TecmagNmrInstrument")


class BrukerNmrInstrument(NmrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000596", "BrukerNmrInstrument")


class JeolNmrInstrument(NmrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000600", "JeolNmrInstrument")


class VarianNmrInstrument(NmrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000611", "VarianNmrInstrument")


class ElisaMicroplateReader(MicroplateReader):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001059", "ElisaMicroplateReader"
    )


class MultimodeMicroplateReader(MicroplateReader):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001090", "MultimodeMicroplateReader"
    )


class MultichannelElectronicPipette(MultichannelPipette):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001083", "MultichannelElectronicPipette"
    )


class ElectronicRepeaterPipette(Micropipette):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001101", "ElectronicRepeaterPipette"
    )


class TopLoadingBalance(Balance):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001066", "TopLoadingBalance")


class MechanicalBalance(Balance):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001091", "MechanicalBalance")


class AnalyticalBalance(Balance):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001104", "AnalyticalBalance")


class Photodiode(Photodetector):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400083", "Photodiode")


class _454GenomeSequence20(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000689", "_454GenomeSequence20")


class Abi377AutomatedSequencer(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000691", "Abi377AutomatedSequencer"
    )


class AbSolidSystem(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000696", "AbSolidSystem")


class _454GenomeSequencerFlx(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000702", "_454GenomeSequencerFlx"
    )


class IlluminaGenomeAnalyzerIi(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000703", "IlluminaGenomeAnalyzerIi"
    )


class LiCor4300DnaAnalysisSystem(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000710", "LiCor4300DnaAnalysisSystem"
    )


class HeliscopeSingleMoleculeSequencer(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000717", "HeliscopeSingleMoleculeSequencer"
    )


class IlluminaMiseq(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002003", "IlluminaMiseq")


class PacbioRsIi(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002012", "PacbioRsIi")


class IlluminaGenomeAnalyzer(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002128", "IlluminaGenomeAnalyzer"
    )


class PacbioSequel(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002632", "PacbioSequel")


class PacbioSequelIi(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002633", "PacbioSequelIi")


class OxfordNanoporeMinion(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002750", "OxfordNanoporeMinion")


class OxfordNanoporeGridionMk1(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002751", "OxfordNanoporeGridionMk1"
    )


class OxfordNanoporePromethion(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002752", "OxfordNanoporePromethion"
    )


class IlluminaMiniseq(DnaSequencer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003114", "IlluminaMiniseq")


class IlluminaHiseqSeriesInstrument(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003683", "IlluminaHiseqSeriesInstrument"
    )


class IlluminaNextseqSeriesInstrument(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003684", "IlluminaNextseqSeriesInstrument"
    )


class IlluminaNovaseqSeriesInstrument(DnaSequencer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003685", "IlluminaNovaseqSeriesInstrument"
    )


class ElectronParamagneticResonanceSpectrometer(Spectrophotometer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001102",
        "ElectronParamagneticResonanceSpectrometer",
    )


class LactoscopeC4(Spectrophotometer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400063", "LactoscopeC4")


class Fluorometer(Spectrophotometer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400143", "Fluorometer")


class FlowCytometer(Cytometer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400044", "FlowCytometer")


class Microcentrifuge(Centrifuge):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001100", "Microcentrifuge")


class PackedColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000448", "PackedColumn")


class OrganicAcidColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000465", "OrganicAcidColumn")


class ProteinColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000468", "ProteinColumn")


class NormalPhaseColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000482", "NormalPhaseColumn")


class CapillaryColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000496", "CapillaryColumn")


class ReversedPhaseColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000510", "ReversedPhaseColumn")


class ChromatofocusingColumn(ChromatographyColumn):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000515", "ChromatofocusingColumn"
    )


class TrapColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000518", "TrapColumn")


class AffinityColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000533", "AffinityColumn")


class IonExchangeColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000560", "IonExchangeColumn")


class SpinColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000570", "SpinColumn")


class HighTemperatureColumn(ChromatographyColumn):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000574", "HighTemperatureColumn"
    )


class PlungerColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000586", "PlungerColumn")


class LiquidChromatographyColumn(ChromatographyColumn):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000603", "LiquidChromatographyColumn"
    )


class OpenTubularColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000606", "OpenTubularColumn")


class GlassColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000609", "GlassColumn")


class SizeExclusionColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000618", "SizeExclusionColumn")


class CustomMadeColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000621", "CustomMadeColumn")


class GelPermeationColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000622", "GelPermeationColumn")


class CarbonNanotubeColumn(ChromatographyColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000628", "CarbonNanotubeColumn")


class SolventMixer(ChromatographyInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000469", "SolventMixer")


class ChromatographyDetector(ChromatographyInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000481", "ChromatographyDetector"
    )


class LiquidChromatographyAutosampler(ChromatographyInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000494", "LiquidChromatographyAutosampler"
    )


class FractionCollector(ChromatographyInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000536", "FractionCollector")


class ColumnCartridger(ChromatographyInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000549", "ColumnCartridger")


class ChromatographyPumpSystem(ChromatographyInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000589", "ChromatographyPumpSystem"
    )


class ColumnHeater(ChromatographyInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000633", "ColumnHeater")


class GelElectrophoresisSystem(ElectrophoresisSystem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001121", "GelElectrophoresisSystem"
    )


class CapillaryElectrophoresisInstrument(ElectrophoresisSystem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001132",
        "CapillaryElectrophoresisInstrument",
    )


class RnaExtractionPurificationInstrument(NucleicAcidExtractionPurificationInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001050",
        "RnaExtractionPurificationInstrument",
    )


class DnaExtractionPurificationInstrument(NucleicAcidExtractionPurificationInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001117",
        "DnaExtractionPurificationInstrument",
    )


class BandPassFilter(OpticalFilter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400013", "BandPassFilter")


class DichroicFilter(OpticalFilter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400030", "DichroicFilter")


class DichroicMirror(OpticalFilter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400031", "DichroicMirror")


class LongPassFilter(OpticalFilter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400067", "LongPassFilter")


class ShortPassFilter(OpticalFilter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400095", "ShortPassFilter")


class MicromErgostarHm200(Microtome):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002194", "MicromErgostarHm200")


class TestTube(Vial):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000836", "TestTube")


class GlassBottleCoatedWithInsecticides(GlassBottle):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002682",
        "GlassBottleCoatedWithInsecticides",
    )


class QuartzCuvetteFlowChamber(FlowCell):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400088", "QuartzCuvetteFlowChamber"
    )


class TwoPhotonLaserDetector(LightSource):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001052", "TwoPhotonLaserDetector"
    )


class UltravioletLightSource(LightSource):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002900", "UltravioletLightSource"
    )


class VisibleLightSource(LightSource):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002901", "VisibleLightSource")


class SolarLightSource(LightSource):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002902", "SolarLightSource")


class ArcLamp(LightSource):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400009", "ArcLamp")


class Laser(LightSource):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400064", "Laser")


class ChromatographyDevice(
    ContainerWithEnvironmentalControl, MeasurementDevice, MaterialSeparationDevice
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000048", "ChromatographyDevice")


class IsoelectricFocusingDevice(ContainerWithEnvironmentalControl):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000389", "IsoelectricFocusingDevice"
    )


class ThermostaticCirculator(ContainerWithEnvironmentalControl):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000390", "ThermostaticCirculator"
    )


class GelDryer(ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000404", "GelDryer")


class IncubatorShaker(ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001076", "IncubatorShaker")


class SheathTank(ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400094", "SheathTank")


class HybridizationChamber(ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400110", "HybridizationChamber")


class ThermalCycler(ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400116", "ThermalCycler")


class VacuumDryer(ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400117", "VacuumDryer")


class TemperatureControlBath(ContainerWithEnvironmentalControl):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400120", "TemperatureControlBath"
    )


class GelTank(ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400140", "GelTank")


class HybridizationOven(Incubator, ContainerWithEnvironmentalControl):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001075", "HybridizationOven")


class DnaSynthesizer(OligonucleotideSynthesizer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001056", "DnaSynthesizer")


class IlluminaMethylationBeadchip(IlluminaBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001870", "IlluminaMethylationBeadchip"
    )


class _1MDuoInfiniumHdBeadchip(IlluminaBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002006", "_1MDuoInfiniumHdBeadchip"
    )


class IlluminaInfiniumOmni5Exome4Kit(IlluminaBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002130", "IlluminaInfiniumOmni5Exome4Kit"
    )


class IlluminaHumanht12V40ExpressionBeadchip(IlluminaBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003401",
        "IlluminaHumanht12V40ExpressionBeadchip",
    )


class IlluminaMouseref8V20Beadchip(IlluminaBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003402", "IlluminaMouseref8V20Beadchip"
    )


class DnaMicroarray(Microarray):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400148", "DnaMicroarray")


class ProteinMicroarray(Microarray):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400149", "ProteinMicroarray")


class NonMedicalMask(FaceMask):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002788", "NonMedicalMask")


class MedicalMask(FaceMask):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002789", "MedicalMask")


class N95Respirator(FaceMask):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002790", "N95Respirator")


class PatientGown(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002792", "PatientGown")


class Scrubs(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002793", "Scrubs")


class MedicalGown(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002796", "MedicalGown")


class PersonalProtectiveGlove(PersonalProtectiveClothingItem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002799", "PersonalProtectiveGlove"
    )


class LaboratoryCoat(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002802", "LaboratoryCoat")


class FootwearCover(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002806", "FootwearCover")


class ProtectiveCoverall(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002810", "ProtectiveCoverall")


class ProtectiveSleeve(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002811", "ProtectiveSleeve")


class ProtectiveApron(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002812", "ProtectiveApron")


class MedicalCap(PersonalProtectiveClothingItem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002813", "MedicalCap")


class PreMoistenedSwabStick(SpecimenCollectionSwabStick):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002823", "PreMoistenedSwabStick"
    )


class Mosquitrap(GravidTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002934", "Mosquitrap")


class CentersForDiseaseControlAndPreventionGravidTrap(GravidTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003050",
        "CentersForDiseaseControlAndPreventionGravidTrap",
    )


class CentersForDiseaseControlAndPreventionLightTrap(LightTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002926",
        "CentersForDiseaseControlAndPreventionLightTrap",
    )


class EncephalitisVirusSurveillanceTrap(LightTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002928",
        "EncephalitisVirusSurveillanceTrap",
    )


class LightTrapForIndoorUse(LightTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002931", "LightTrapForIndoorUse"
    )


class LightTrapForOutdoorUse(LightTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002932", "LightTrapForOutdoorUse"
    )


class NewJerseyLightTrap(LightTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002935", "NewJerseyLightTrap")


class ArtificialPitShelter(RestingArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002921", "ArtificialPitShelter")


class RestingBoxTrap(RestingArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002940", "RestingBoxTrap")


class RestingBucket(RestingArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002941", "RestingBucket")


class StickyRestingBucket(RestingArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002943", "StickyRestingBucket")


class StickyTrap(RestingArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002944", "StickyTrap")


class RestingClayPotTrap(RestingArthropodTrap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003551", "RestingClayPotTrap")


class CulturedCd4Cd8TCellPopulation(
    CulturedCd4TCellPopulation, CulturedCd8TCellPopulation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110052", "CulturedCd4Cd8TCellPopulation"
    )


class ImmortalCellLine(CellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/CLO_0009828", "ImmortalCellLine")


class MortalCellLine(CellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/CLO_0009829", "MortalCellLine")


class Flaviviridae(Kitrinoviricota):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_11050", "Flaviviridae")


class ChikungunyaVirus(Kitrinoviricota):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_37124", "ChikungunyaVirus")


class HepatitisBVirus(Revtraviricetes):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_10407", "HepatitisBVirus")


class Lentivirus(Revtraviricetes):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_11646", "Lentivirus")


class Bilateria(Metazoa):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_33213", "Bilateria")


class SchizosaccharomycesPombe(Ascomycota):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_4896", "SchizosaccharomycesPombe"
    )


class Saccharomyceta(Ascomycota):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_716545", "Saccharomyceta")


class LabeledDnaExtract(LabeledNucleicAcidExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000908", "LabeledDnaExtract")


class LabeledRnaExtract(LabeledNucleicAcidExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000921", "LabeledRnaExtract")


class NuclearRnaExtract(RnaExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000862", "NuclearRnaExtract")


class PolyaRnaExtract(RnaExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000869", "PolyaRnaExtract")


class CytoplasmicRnaExtract(RnaExtract):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000876", "CytoplasmicRnaExtract"
    )


class TotalRnaExtract(RnaExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000895", "TotalRnaExtract")


class OrganellarRnaExtract(RnaExtract):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000899", "OrganellarRnaExtract")


class PolyaDepletedRnaExtract(RnaExtract):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002573", "PolyaDepletedRnaExtract"
    )


class RibosomalRnaDepletedRnaExtract(RnaExtract):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002627", "RibosomalRnaDepletedRnaExtract"
    )


class HighMolecularWeightDnaExtract(DnaExtract):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000834", "HighMolecularWeightDnaExtract"
    )


class HEStainedFixedTissueSlideSpecimen(FixedTissueSlideSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002125",
        "HEStainedFixedTissueSlideSpecimen",
    )


class IhcStainedFixedTissueSlideSpecimen(FixedTissueSlideSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002126",
        "IhcStainedFixedTissueSlideSpecimen",
    )


class AreolarSwabSpecimen(BreastSwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002603", "AreolarSwabSpecimen")


class LungSpecimen(LowerRespiratoryTractSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002534", "LungSpecimen")


class LowerRespiratoryTractAspirateSpecimen(LowerRespiratoryTractSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002781",
        "LowerRespiratoryTractAspirateSpecimen",
    )


class EndotrachealTubeSpecimen(LowerRespiratoryTractSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002971", "EndotrachealTubeSpecimen"
    )


class NasalSwabSpecimen(UpperRespiratoryTractSpecimen, SwabSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000917", "NasalSwabSpecimen")


class OropharyngealSwabSpecimen(UpperRespiratoryTractSpecimen, SwabSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002608", "OropharyngealSwabSpecimen"
    )


class NasalAspirateSpecimen(UpperRespiratoryTractSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002780", "NasalAspirateSpecimen"
    )


class NasopharynxSpecimen(UpperRespiratoryTractSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000007", "NasopharynxSpecimen")


class BloodPlasmaSpecimen(BloodSpecimen, ProcessedSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100016", "BloodPlasmaSpecimen")


class ArthropodMealOfBloodSpecimen(BloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002691", "ArthropodMealOfBloodSpecimen"
    )


class BloodSpecimenInVacutainer(BloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003054", "BloodSpecimenInVacutainer"
    )


class BloodSpecimenOnFilterPaper(BloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003055", "BloodSpecimenOnFilterPaper"
    )


class PlacentalBloodSpecimen(BloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003380", "PlacentalBloodSpecimen"
    )


class PeripheralBloodMononuclearCellSpecimen(BloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003415",
        "PeripheralBloodMononuclearCellSpecimen",
    )


class ArterialBloodSpecimen(BloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000013", "ArterialBloodSpecimen"
    )


class VenousBloodSpecimen(BloodSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_2000014", "VenousBloodSpecimen")


class CapillaryBloodSpecimen(BloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000015", "CapillaryBloodSpecimen"
    )


class BileSpecimen(DigestiveSystemFluidOrSecretionSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002501", "BileSpecimen")


class InducedSputumSpecimen(SputumSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002746", "InducedSputumSpecimen"
    )


class ArterialBlood(Blood):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0013755", "ArterialBlood")


class VenousBlood(Blood):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0013756", "VenousBlood")


class CapillaryBlood(Blood):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_0013757", "CapillaryBlood")


class PlacentalBlood(Blood):
    term = RdfTerm("http://purl.obolibrary.org/obo/UBERON_8470000", "PlacentalBlood")


class GasFilterFunction(FilterFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000380", "GasFilterFunction")


class LiquidFilterFunction(FilterFunction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000381", "LiquidFilterFunction")


class SignalAmplificationFunction(SignalConversionFunction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000395", "SignalAmplificationFunction"
    )


class RoleOfBeingConsumerSafetyOfficer(RoleOfRegulatorOfConsumablesAndMedicalDevices):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000006", "RoleOfBeingConsumerSafetyOfficer"
    )


class NotifiedBodyRole(RoleOfRegulatorOfConsumablesAndMedicalDevices):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000056", "NotifiedBodyRole")


class CohortRole(BiologicalReplicateRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000252", "CohortRole")


class RoleOfIndependentDataMonitoringCommittee(TrialMonitorRole):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000144",
        "RoleOfIndependentDataMonitoringCommittee",
    )


class RadiolabelRole(MolecularLabelRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000163", "RadiolabelRole")


class DyeRole(MolecularLabelRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000250", "DyeRole")


class Length(_1DExtent):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000122", "Length")


class Volume(_3DExtent):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000918", "Volume")


class BiomaterialPurity(Composition):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001339", "BiomaterialPurity")


class Damaged(Damage):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001167", "Damaged")


class FluidFlowRate(FlowRate):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0002243", "FluidFlowRate")


class Radioactive(ActivityOfARadionuclide):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001741", "Radioactive")


class OpticalQuality(QualityOfInteractionOfASubstanceWithElectromagneticRadiation):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001300", "OpticalQuality")


class Female(PhenotypicSex):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000383", "Female")


class Male(PhenotypicSex):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000384", "Male")


class Hermaphrodite(PhenotypicSex):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001340", "Hermaphrodite")


class BacterialMatingType(MatingType):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001335", "BacterialMatingType")


class YeastMatingType(MatingType):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001337", "YeastMatingType")


class LeftHandedness(Handedness):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0002202", "LeftHandedness")


class RightHandedness(Handedness):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0002203", "RightHandedness")


class AmbidextrousHandedness(Handedness):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0002204", "AmbidextrousHandedness"
    )


class Aneuploid(Ploidy):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001385", "Aneuploid")


class Euploid(Ploidy):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001393", "Euploid")


class RawMagneticResonanceImageDataSet(MagneticResonanceImageDataSet, RawImageDataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003354", "RawMagneticResonanceImageDataSet"
    )


class ReconstructedMagneticResonanceImageDataSet(
    MagneticResonanceImageDataSet, ComputedImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003334",
        "ReconstructedMagneticResonanceImageDataSet",
    )


class BrainRegionAtlasImageDataSet(ComputedImageDataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003357", "BrainRegionAtlasImageDataSet"
    )


class ImageSegmentationMap(ComputedImageDataSet):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003360", "ImageSegmentationMap")


class TaxonomicBridgeOntologyModule(BridgeOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000016", "TaxonomicBridgeOntologyModule"
    )


class ImportOntologyModule(SubsetOntologyModule):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_8000005", "ImportOntologyModule")


class CurationSubsetOntologyModule(SubsetOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000007", "CurationSubsetOntologyModule"
    )


class AnalysisSubsetOntologyModule(SubsetOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000008", "AnalysisSubsetOntologyModule"
    )


class SingleLayerSubsetOntologyModule(SubsetOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000009", "SingleLayerSubsetOntologyModule"
    )


class ExclusionSubsetOntologyModule(SubsetOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000010", "ExclusionSubsetOntologyModule"
    )


class SpeciesSubsetOntologyModule(SubsetOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000012", "SpeciesSubsetOntologyModule"
    )


class OntologyModuleSubsettedByExpressivity(SubsetOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000017",
        "OntologyModuleSubsettedByExpressivity",
    )


class TemplateGeneratedOntologyModule(GeneratedOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000015", "TemplateGeneratedOntologyModule"
    )


class TissueSectionThickness(LengthMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002197", "TissueSectionThickness"
    )


class AltitudeMeasurementDatum(LengthMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002983", "AltitudeMeasurementDatum"
    )


class MidUpperArmCircumferenceDatum(LengthMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003416", "MidUpperArmCircumferenceDatum"
    )


class AgeMeasurementDatum(TimeMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001167", "AgeMeasurementDatum")


class HalfLifeDatumT12(TimeMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001171", "HalfLifeDatumT12")


class SamplingTimeMeasurementDatum(TimeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001508", "SamplingTimeMeasurementDatum"
    )


class SpecimenCollectionTimeMeasurementDatum(TimeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001619",
        "SpecimenCollectionTimeMeasurementDatum",
    )


class ComputationRunTime(TimeMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001913", "ComputationRunTime")


class SpecimenCollectionDuration(TimeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002988", "SpecimenCollectionDuration"
    )


class ExtractionDate(TimeMeasurementDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003081", "ExtractionDate")


class ExtractionDurationTime(TimeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003082", "ExtractionDurationTime"
    )


class Ec50BindingDatum(HalfMaximalEffectiveConcentrationEc50, QuantitativeBindingDatum):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003143", "Ec50BindingDatum")


class Ic50BindingDatum(
    HalfMaximalInhibitoryConcentrationIc50, QuantitativeBindingDatum
):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003144", "Ic50BindingDatum")


class ContigN50(N50):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001941", "ContigN50")


class ScaffoldN50(N50):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001945", "ScaffoldN50")


class AxillaryTemperatureMeasurementDatum(TemperatureMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003072",
        "AxillaryTemperatureMeasurementDatum",
    )


class OrganismalBodyTemperatureMeasurementDatum(TemperatureMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003073",
        "OrganismalBodyTemperatureMeasurementDatum",
    )


class BindingOffRateMeasurementDatumKoff(RateMeasurementDatum, BindingConstant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001603",
        "BindingOffRateMeasurementDatumKoff",
    )


class BindingOnRateMeasurementDatumKon(RateMeasurementDatum, BindingConstant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001605", "BindingOnRateMeasurementDatumKon"
    )


class EquilibriumDissociationConstantKd(BindingConstant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001536",
        "EquilibriumDissociationConstantKd",
    )


class EquilibriumAssociationConstantKa(BindingConstant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001548", "EquilibriumAssociationConstantKa"
    )


class WildTypeAlleleInformation(AlleleInformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001369", "WildTypeAlleleInformation"
    )


class EukaryotaInPlacentalBloodDatum(
    EukaryotaInBloodDatum, PlacentalBloodMicrobiologyDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003383", "EukaryotaInPlacentalBloodDatum"
    )


class EukaryotaInUmbilicalCordBloodDatum(
    UmbilicalCordBloodMicrobiologyDatum, EukaryotaInBloodDatum
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003281",
        "EukaryotaInUmbilicalCordBloodDatum",
    )


class StandardComplianceRule(ComplianceRule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500024", "StandardComplianceRule"
    )


class ProteinAndDnaInteractionIdentificationObjective(
    SequenceFeatureIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001398",
        "ProteinAndDnaInteractionIdentificationObjective",
    )


class ProteinAndRnaInteractionIdentificationObjective(
    SequenceFeatureIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001854",
        "ProteinAndRnaInteractionIdentificationObjective",
    )


class EpigeneticModificationIdentificationObjective(
    MolecularFeatureIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001234",
        "EpigeneticModificationIdentificationObjective",
    )


class TranscriptionProfilingIdentificationObjective(
    MolecularFeatureIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001331",
        "TranscriptionProfilingIdentificationObjective",
    )


class DnaReplicationIdentificationObjective(MolecularFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001916",
        "DnaReplicationIdentificationObjective",
    )


class ChromosomeConformationIdentificationObjective(
    MolecularFeatureIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001917",
        "ChromosomeConformationIdentificationObjective",
    )


class DetectionOfPathogenicOrganismsObjective(OrganismFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002689",
        "DetectionOfPathogenicOrganismsObjective",
    )


class InsecticideResistanceDetectionObjective(OrganismFeatureIdentificationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002690",
        "InsecticideResistanceDetectionObjective",
    )


class ProtocolOptimizationObjective(ProtocolTestingObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000186", "ProtocolOptimizationObjective"
    )


class HardwareOptimizationObjective(HardwareTestingObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000232", "HardwareOptimizationObjective"
    )


class SoftwareOptimizationObjective(SoftwareTestingObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000055", "SoftwareOptimizationObjective"
    )


class PortioningObjective(MaterialSeparationObjective):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000678", "PortioningObjective")


class SeparationIntoDifferentCompositionObjective(MaterialSeparationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000681",
        "SeparationIntoDifferentCompositionObjective",
    )


class AddingMaterialObjective(MaterialCombinationObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000434", "AddingMaterialObjective"
    )


class BackgroundCorrectionObjective(CorrectionObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200173", "BackgroundCorrectionObjective"
    )


class ErrorCorrectionObjective(CorrectionObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200186", "ErrorCorrectionObjective"
    )


class CrossValidationObjective(PartitioningObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200188", "CrossValidationObjective"
    )


class AlignmentCountingApplication(SoftwareApplication):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002467", "AlignmentCountingApplication"
    )


class BaseCallingApplication(SoftwareApplication):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002469", "BaseCallingApplication"
    )


class VerseAlgorithm(AlignmentCountingAlgorithm):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002486", "VerseAlgorithm")


class StarAlgorithm(ReferenceGenomeTranscriptomeAlignmentAlgorithm):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002484", "StarAlgorithm")


class RodentCareProtocol(AnimalCareProtocol):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000688", "RodentCareProtocol")


class CompoundTreatmentDesign(InterventionDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000951", "CompoundTreatmentDesign"
    )


class GrowthConditionInterventionDesign(InterventionDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000985",
        "GrowthConditionInterventionDesign",
    )


class PostTranscriptionalModificationDesign(InterventionDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001358",
        "PostTranscriptionalModificationDesign",
    )


class StimulusOrStressDesign(InterventionDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001396", "StimulusOrStressDesign"
    )


class GeneticModificationDesign(InterventionDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001460", "GeneticModificationDesign"
    )


class SequentialDesign(InterventionDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0300310", "SequentialDesign")


class RepeatedMeasureDesign(InterventionDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500002", "RepeatedMeasureDesign"
    )


class RandomizedCompleteBlockDesign(InterventionDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500007", "RandomizedCompleteBlockDesign"
    )


class ChipSeqDesign(ProteinBindingSiteIdentificationDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001258", "ChipSeqDesign")


class ChipChipDesign(ProteinBindingSiteIdentificationDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001403", "ChipChipDesign")


class GenotypingByHighThroughputSequencingDesign(GenotypingDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001200",
        "GenotypingByHighThroughputSequencingDesign",
    )


class GenotypingByArrayDesign(GenotypingDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001387", "GenotypingByArrayDesign"
    )


class ColocalizationIdentificationDesign(MolecularInteractionIdentificationDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002591",
        "ColocalizationIdentificationDesign",
    )


class GeneticInteractionIdentificationDesign(MolecularInteractionIdentificationDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002592",
        "GeneticInteractionIdentificationDesign",
    )


class FunctionalAssociationIdentificationDesign(
    MolecularInteractionIdentificationDesign
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002593",
        "FunctionalAssociationIdentificationDesign",
    )


class DirectInteractionIdentificationDesign(MolecularInteractionIdentificationDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002594",
        "DirectInteractionIdentificationDesign",
    )


class SelfInteractionIdentificationDesign(MolecularInteractionIdentificationDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002596",
        "SelfInteractionIdentificationDesign",
    )


class BalancedIncompleteBlockDesign(FactorialDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500008", "BalancedIncompleteBlockDesign"
    )


class _2X2FactorialDesign(FactorialDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500015", "_2X2FactorialDesign")


class FractionalFactorialDesign(FactorialDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500016", "FractionalFactorialDesign"
    )


class AgeOfMajorityInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002423", "AgeOfMajorityInclusionCriterion"
    )


class BmiRangeInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002428", "BmiRangeInclusionCriterion"
    )


class HealthStatusInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002453", "HealthStatusInclusionCriterion"
    )


class ClinicallyRelevantLifestyleInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002454",
        "ClinicallyRelevantLifestyleInclusionCriterion",
    )


class ClinicallyRelevantExposureInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002455",
        "ClinicallyRelevantExposureInclusionCriterion",
    )


class GravidityInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002456", "GravidityInclusionCriterion"
    )


class DefinedPopulationInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002460",
        "DefinedPopulationInclusionCriterion",
    )


class AgeGroupInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002555", "AgeGroupInclusionCriterion"
    )


class UseOfMedicationInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002558",
        "UseOfMedicationInclusionCriterion",
    )


class HospitalPatientInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002559",
        "HospitalPatientInclusionCriterion",
    )


class FamilyStatusInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002560", "FamilyStatusInclusionCriterion"
    )


class SexInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002561", "SexInclusionCriterion"
    )


class CountryOfResidenceInclusionCriteria(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002562",
        "CountryOfResidenceInclusionCriteria",
    )


class EthnicityInclusionCriterion(InclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002563", "EthnicityInclusionCriterion"
    )


class ChemotherapyTreatmentExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002424",
        "ChemotherapyTreatmentExclusionCriterion",
    )


class RadiationTreatmentExclusionCriteria(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002425",
        "RadiationTreatmentExclusionCriteria",
    )


class ChemotherapyTreatmentWithinTheRecentPastExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002426",
        "ChemotherapyTreatmentWithinTheRecentPastExclusionCriterion",
    )


class RadiationTreatmentWithinTheRecentPastExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002427",
        "RadiationTreatmentWithinTheRecentPastExclusionCriterion",
    )


class BloodTransfusionExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002429",
        "BloodTransfusionExclusionCriterion",
    )


class HistoryOfMetastaticCancerExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002430",
        "HistoryOfMetastaticCancerExclusionCriterion",
    )


class IntravenousDrugUseExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002431",
        "IntravenousDrugUseExclusionCriterion",
    )


class HistoryOfSexWithSomeoneWithAHistoryOfBloodBorneInfectionExclusionCriterion(
    ExclusionCriterion
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002432",
        "HistoryOfSexWithSomeoneWithAHistoryOfBloodBorneInfectionExclusionCriterion",
    )


class HistoryOfSexWithSomeoneWithAHistoryOfIntravenousDrugsExclusionCriterion(
    ExclusionCriterion
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002433",
        "HistoryOfSexWithSomeoneWithAHistoryOfIntravenousDrugsExclusionCriterion",
    )


class HivExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002434", "HivExclusionCriterion"
    )


class ExposureToBloodBorneInfectiousDiseaseExclusionCriterion(ExclusionCriterion):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002435",
        "ExposureToBloodBorneInfectiousDiseaseExclusionCriterion",
    )


class HelperTCellEnhancementOfTCellMediatedImmuneResponse(
    HelperTCellEnhancementOfAdaptiveImmuneResponse
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0035398",
        "HelperTCellEnhancementOfTCellMediatedImmuneResponse",
    )


class HelperTCellEnhancementOfBCellMediatedImmuneResponse(
    HelperTCellEnhancementOfAdaptiveImmuneResponse
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/GO_0035399",
        "HelperTCellEnhancementOfBCellMediatedImmuneResponse",
    )


class FluorescenceMicroscopyAssay(LightMicroscopyAssay, FluorescenceDetectionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CHMO_0000087", "FluorescenceMicroscopyAssay"
    )


class MicrowesternMesoScaleQuantitativeWesternBlotAssay(WesternBlotAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002967",
        "MicrowesternMesoScaleQuantitativeWesternBlotAssay",
    )


class GenotypingByTilingArrayAssay(GenotypingByArrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002030", "GenotypingByTilingArrayAssay"
    )


class GenotypingBySnpArrayAssay(GenotypingByArrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002031", "GenotypingBySnpArrayAssay"
    )


class RnaBindingProteinImmunoprecipitationTilingArrayProfilingAssay(
    RnaBindingProteinImmunoprecipitationArrayProfilingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001921",
        "RnaBindingProteinImmunoprecipitationTilingArrayProfilingAssay",
    )


class SerumAntiCytomegalovirusAntibodyLevelAssay(CmvAntibodyAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003590",
        "SerumAntiCytomegalovirusAntibodyLevelAssay",
    )


class CalciumCationConcentrationAssay(CalciumCationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003150", "CalciumCationConcentrationAssay"
    )


class BasicMetabolicPanelVenousBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100092",
        "BasicMetabolicPanelVenousBloodCalciumAssay",
    )


class VenousBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100095", "VenousBloodCalciumAssay"
    )


class TotalVenousBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100097", "TotalVenousBloodCalciumAssay"
    )


class ComprehensiveMetabolicPanelVenousBloodCalciumAssay(
    CalciumCationAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100149",
        "ComprehensiveMetabolicPanelVenousBloodCalciumAssay",
    )


class IonizedVenousBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100167",
        "IonizedVenousBloodIonizedCalciumAssay",
    )


class IonizedArterialBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100182", "IonizedArterialBloodCalciumAssay"
    )


class GemPremierBloodGasVenousBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100190",
        "GemPremierBloodGasVenousBloodIonizedCalciumAssay",
    )


class Chem11VenousBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100226", "Chem11VenousBloodCalciumAssay"
    )


class Chem16VenousBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100240", "Chem16VenousBloodCalciumAssay"
    )


class PocChem8ArterialBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100251",
        "PocChem8ArterialBloodIonizedCalciumAssay",
    )


class Abl90PanelArterialBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100279",
        "Abl90PanelArterialBloodCalciumAssay",
    )


class Abl90PanelVenousBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100286",
        "Abl90PanelVenousBloodIonizedCalciumAssay",
    )


class BoneProfileVenousBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100299",
        "BoneProfileVenousBloodCalciumAssay",
    )


class AbgElectrolytesArterialBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100305",
        "AbgElectrolytesArterialBloodIonizedCalciumAssay",
    )


class Gem4000AnlcooxArterialBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100319",
        "Gem4000AnlcooxArterialBloodIonizedCalciumAssay",
    )


class IonizedVenousBloodCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100322", "IonizedVenousBloodCalciumAssay"
    )


class VenousBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100355", "VenousBloodIonizedCalciumAssay"
    )


class Gem4ArterialBloodIonizedCalciumAssay(CalciumCationAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100380",
        "Gem4ArterialBloodIonizedCalciumAssay",
    )


class PlasmaProteomicsAssay(ProteomicProfilingByArrayAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003229", "PlasmaProteomicsAssay"
    )


class VenousBloodTransferrinAssay(TransferrinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100135", "VenousBloodTransferrinAssay"
    )


class AdiponectinConcentrationAssay(AdiponectinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003193", "AdiponectinConcentrationAssay"
    )


class LeptinConcentrationAssay(LeptinAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003203", "LeptinConcentrationAssay"
    )


class LiverInjuryVenousBloodAlanineAminotransferaseAssay(
    AlanineAminotransferaseAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100068",
        "LiverInjuryVenousBloodAlanineAminotransferaseAssay",
    )


class LiverEvaluationVenousBloodAlanineAminotransferaseAssay(
    AlanineAminotransferaseAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100084",
        "LiverEvaluationVenousBloodAlanineAminotransferaseAssay",
    )


class ComprehensiveMetabolicPanelVenousBloodAlanineAminotransferaseAssay(
    AlanineAminotransferaseAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100160",
        "ComprehensiveMetabolicPanelVenousBloodAlanineAminotransferaseAssay",
    )


class HepaticPanelVenousBloodAlanineAminotransferaseAssay(
    AlanineAminotransferaseAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100214",
        "HepaticPanelVenousBloodAlanineAminotransferaseAssay",
    )


class Chem16VenousBloodAlanineAminotransferaseAssay(
    AlanineAminotransferaseAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100248",
        "Chem16VenousBloodAlanineAminotransferaseAssay",
    )


class LiverFunctionVenousBloodAlanineAminotransferaseAssay(
    AlanineAminotransferaseAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100339",
        "LiverFunctionVenousBloodAlanineAminotransferaseAssay",
    )


class LiverInjuryVenousBloodHumanAlkalinePhosphataseAssay(
    AlkalinePhosphataseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100069",
        "LiverInjuryVenousBloodHumanAlkalinePhosphataseAssay",
    )


class LiverEvaluationVenousBloodHumanAlkalinePhosphataseAssay(
    AlkalinePhosphataseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100085",
        "LiverEvaluationVenousBloodHumanAlkalinePhosphataseAssay",
    )


class ComprehensiveMetabolicPanelVenousBloodHumanAlkalinePhosphataseAssay(
    AlkalinePhosphataseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100154",
        "ComprehensiveMetabolicPanelVenousBloodHumanAlkalinePhosphataseAssay",
    )


class HepaticPanelVenousBloodHumanAlkalinePhosphataseAssay(
    AlkalinePhosphataseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100217",
        "HepaticPanelVenousBloodHumanAlkalinePhosphataseAssay",
    )


class Chem16VenousBloodHumanAlkalinePhosphataseAssay(
    AlkalinePhosphataseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100244",
        "Chem16VenousBloodHumanAlkalinePhosphataseAssay",
    )


class BoneProfileVenousBloodHumanAlkalinePhosphataseAssay(
    AlkalinePhosphataseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100300",
        "BoneProfileVenousBloodHumanAlkalinePhosphataseAssay",
    )


class LiverFunctionVenousBloodHumanAlkalinePhosphataseAssay(
    AlkalinePhosphataseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100343",
        "LiverFunctionVenousBloodHumanAlkalinePhosphataseAssay",
    )


class LiverInjuryVenousBloodHumanAspartateAminotransferaseAssay(
    AspartateAminotransferaseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100071",
        "LiverInjuryVenousBloodHumanAspartateAminotransferaseAssay",
    )


class LiverEvaluationVenousBloodHumanAspartateAminotransferaseAssay(
    AspartateAminotransferaseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100083",
        "LiverEvaluationVenousBloodHumanAspartateAminotransferaseAssay",
    )


class ComprehensiveMetabolicPanelVenousBloodHumanAspartateAminotransferaseAssay(
    AspartateAminotransferaseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100157",
        "ComprehensiveMetabolicPanelVenousBloodHumanAspartateAminotransferaseAssay",
    )


class HepaticPanelVenousBloodHumanAspartateAminotransferaseAssay(
    AspartateAminotransferaseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100215",
        "HepaticPanelVenousBloodHumanAspartateAminotransferaseAssay",
    )


class Chem16VenousBloodHumanAspartateAminotransferaseAssay(
    AspartateAminotransferaseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100235",
        "Chem16VenousBloodHumanAspartateAminotransferaseAssay",
    )


class LiverFunctionVenousBloodHumanAspartateAminotransferaseAssay(
    AspartateAminotransferaseHumanAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100340",
        "LiverFunctionVenousBloodHumanAspartateAminotransferaseAssay",
    )


class AlbuminConcentrationAssay(AlbuminAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003148", "AlbuminConcentrationAssay"
    )


class LiverEvaluationVenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100082",
        "LiverEvaluationVenousBloodAlbuminAssay",
    )


class VenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100107", "VenousBloodAlbuminAssay"
    )


class ComprehensiveMetabolicPanelVenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100153",
        "ComprehensiveMetabolicPanelVenousBloodAlbuminAssay",
    )


class SpepProteinElectrophoresisVenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100209",
        "SpepProteinElectrophoresisVenousBloodAlbuminAssay",
    )


class HepaticPanelVenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100216",
        "HepaticPanelVenousBloodAlbuminAssay",
    )


class Chem11VenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100229", "Chem11VenousBloodAlbuminAssay"
    )


class Chem16VenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100245", "Chem16VenousBloodAlbuminAssay"
    )


class BoneProfileVenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100298",
        "BoneProfileVenousBloodAlbuminAssay",
    )


class LiverFunctionVenousBloodAlbuminAssay(AlbuminAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100341",
        "LiverFunctionVenousBloodAlbuminAssay",
    )


class BodilyFluidAlbuminAssay(AlbuminAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100351", "BodilyFluidAlbuminAssay"
    )


class VenousBloodCreatineKinaseAssay(CreatineKinaseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100094", "VenousBloodCreatineKinaseAssay"
    )


class CardiacEnzymesVenousBloodCreatineKinaseAssay(CreatineKinaseAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100108",
        "CardiacEnzymesVenousBloodCreatineKinaseAssay",
    )


class VenousBloodProstateSpecificAntigenAssay(ProstateSpecificAntigenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100120",
        "VenousBloodProstateSpecificAntigenAssay",
    )


class IntactVenousBloodPthAssay(ProstateSpecificAntigenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100259", "IntactVenousBloodPthAssay"
    )


class TotalVenousBloodPsaAssay(ProstateSpecificAntigenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100260", "TotalVenousBloodPsaAssay"
    )


class IntraoperativeVenousBloodPthAssay(ProstateSpecificAntigenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100326",
        "IntraoperativeVenousBloodPthAssay",
    )


class FreeTotalVenousBloodPsaAssay(ProstateSpecificAntigenAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100389", "FreeTotalVenousBloodPsaAssay"
    )


class HighSensitivityCardiacNeonatalVenousBloodCReactiveProteinAssay(
    CReactiveProteinAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100310",
        "HighSensitivityCardiacNeonatalVenousBloodCReactiveProteinAssay",
    )


class NonCardiacVenousBloodCReactiveProteinAssay(CReactiveProteinAssay, BloodAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100325",
        "NonCardiacVenousBloodCReactiveProteinAssay",
    )


class AntibodyBindingDetectionByFluorescenceQuenching(
    FluorescenceQuenchingBindingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001635",
        "AntibodyBindingDetectionByFluorescenceQuenching",
    )


class EpitopeProtectionFromInfectiousChallengeExperimentBasedOnPathogenBurden(
    EpitopeProtectionFromInfectiousChallengeExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001186",
        "EpitopeProtectionFromInfectiousChallengeExperimentBasedOnPathogenBurden",
    )


class EpitopeProtectionFromInfectiousChallengeExperimentBasedOnSurvival(
    EpitopeProtectionFromInfectiousChallengeExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003457",
        "EpitopeProtectionFromInfectiousChallengeExperimentBasedOnSurvival",
    )


class EpitopeProtectionFromTumorChallengeExperimentBasedOnBurden(
    EpitopeProtectionFromTumorChallengeExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003458",
        "EpitopeProtectionFromTumorChallengeExperimentBasedOnBurden",
    )


class EpitopeProtectionFromTumorChallengeExperimentBasedOnSurvival(
    EpitopeProtectionFromTumorChallengeExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003459",
        "EpitopeProtectionFromTumorChallengeExperimentBasedOnSurvival",
    )


class ChromiumReleaseAssay(InVitroCellKillingAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_9999994", "ChromiumReleaseAssay")


class CbcWithManualDifferentialVenousBloodMyelocyteCountAssay(
    MyelocyteCountAssay, BloodAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2100207",
        "CbcWithManualDifferentialVenousBloodMyelocyteCountAssay",
    )


class NucleatedErythrocytePercentageAssay(ErythrocyteAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003188",
        "NucleatedErythrocytePercentageAssay",
    )


class MeanCellVolumeAssay(ErythrocyteAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003189", "MeanCellVolumeAssay")


class MethylationSensitiveRestrictionEnzymeSequencingAssay(
    DnaMethylationProfilingByHighThroughputSequencingAssay, DnaSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001861",
        "MethylationSensitiveRestrictionEnzymeSequencingAssay",
    )


class SingleNucleusMethylcytosineAndTranscriptomeSequencingAssay(
    DnaMethylationProfilingByHighThroughputSequencingAssay, RnaSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003662",
        "SingleNucleusMethylcytosineAndTranscriptomeSequencingAssay",
    )


class WholeCellPatchClampAssay(PatchClampAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002178", "WholeCellPatchClampAssay"
    )


class CellAttachedPatchClampAssay(PatchClampAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002179", "CellAttachedPatchClampAssay"
    )


class InsideOutPatchClampAssay(PatchClampAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002180", "InsideOutPatchClampAssay"
    )


class OutsideOutPatchClampAssay(PatchClampAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002181", "OutsideOutPatchClampAssay"
    )


class TwoElectrodeVoltageClampAssay(VoltageClampAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002183", "TwoElectrodeVoltageClampAssay"
    )


class CutOpenOocyteVoltageClampAssay(VoltageClampAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002184", "CutOpenOocyteVoltageClampAssay"
    )


class CaptureHiCAssay(HiCAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002984", "CaptureHiCAssay")


class DnaseHiCAssay(HiCAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003301", "DnaseHiCAssay")


class MicroCAssay(HiCAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003302", "MicroCAssay")


class SingleCellCombinatorialIndexingHiCAssay(HiCAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003303",
        "SingleCellCombinatorialIndexingHiCAssay",
    )


class SingleNucleusHiCAssay(HiCAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003304", "SingleNucleusHiCAssay"
    )


class SingleCellHiCAssay(HiCAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003305", "SingleCellHiCAssay")


class BulkHiCAssay(HiCAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003306", "BulkHiCAssay")


class MultiContactHiCAssay(HiCAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003307", "MultiContactHiCAssay")


class DeepTendonReflexAssessmentOfTheKneeJoint(DeepTendonReflexAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003535",
        "DeepTendonReflexAssessmentOfTheKneeJoint",
    )


class DeepTendonReflexAssessmentOfTheAnkleJoint(DeepTendonReflexAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003537",
        "DeepTendonReflexAssessmentOfTheAnkleJoint",
    )


class DeepTendonReflexAssessmentOfTheTendonOfBicepsBrachii(DeepTendonReflexAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003538",
        "DeepTendonReflexAssessmentOfTheTendonOfBicepsBrachii",
    )


class DeepTendonReflexAssessmentOfTheBrachioradialis(DeepTendonReflexAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003539",
        "DeepTendonReflexAssessmentOfTheBrachioradialis",
    )


class SittingPostureAssessment(LimitsOfStabilityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003519", "SittingPostureAssessment"
    )


class StanceFeetApartAssessment(LimitsOfStabilityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003520", "StanceFeetApartAssessment"
    )


class StanceFeetApartAssessmentWithEyesClosed(LimitsOfStabilityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003521",
        "StanceFeetApartAssessmentWithEyesClosed",
    )


class StanceFeetTogetherAssessment(LimitsOfStabilityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003522", "StanceFeetTogetherAssessment"
    )


class StanceFeetTogetherAssessmentWithEyesClosed(LimitsOfStabilityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003523",
        "StanceFeetTogetherAssessmentWithEyesClosed",
    )


class TandemStanceAssessment(LimitsOfStabilityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003524", "TandemStanceAssessment"
    )


class StanceOnOneFootAssessment(LimitsOfStabilityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003525", "StanceOnOneFootAssessment"
    )


class TandemWalkAssessment(LimitsOfStabilityAssessment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003526", "TandemWalkAssessment")


class GaitAssessment(LimitsOfStabilityAssessment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003527", "GaitAssessment")


class UpperLimbCoordinationAssessment(LimbCoordinationAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003531", "UpperLimbCoordinationAssessment"
    )


class LowerLimbCoordinationAssessment(LimbCoordinationAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003532", "LowerLimbCoordinationAssessment"
    )


class AssessmentOfLearningAndOrMemoryResponseInAnOrganism(
    NervousSystemFunctionalityAssessment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003709",
        "AssessmentOfLearningAndOrMemoryResponseInAnOrganism",
    )


class AssessmentOfStartleResponseInAnOrganism(NervousSystemFunctionalityAssessment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003710",
        "AssessmentOfStartleResponseInAnOrganism",
    )


class GripStrengthAssay(NervousSystemFunctionalityAssessment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003711", "GripStrengthAssay")


class InsecticideResistanceByLigaseDetectionReactionFluorescentMicrosphereAssay(
    InsecticideResistanceByLigaseDetectionReactionAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002723",
        "InsecticideResistanceByLigaseDetectionReactionFluorescentMicrosphereAssay",
    )


class DirectInsecticideResistanceDiagnosticAssay(DirectInsecticideResistanceBioassay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002707",
        "DirectInsecticideResistanceDiagnosticAssay",
    )


class InsecticideResistanceDoseResponseAssay(DirectInsecticideResistanceBioassay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002708",
        "InsecticideResistanceDoseResponseAssay",
    )


class InsecticideResistanceTimeResponseAssay(DirectInsecticideResistanceBioassay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002709",
        "InsecticideResistanceTimeResponseAssay",
    )


class ParasiteSpeciesIdentificationByPcrAssay(ParasiteDetectionByPcrAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003044",
        "ParasiteSpeciesIdentificationByPcrAssay",
    )


class SubcellularProteinImmunohistochemistryAssay(Immunohistochemistry):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002168",
        "SubcellularProteinImmunohistochemistryAssay",
    )


class NeuronMorphologyAssay(_3DNeuralCellStructureDeterminationAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003124", "NeuronMorphologyAssay"
    )


class MosaicismWithRepeatFrameshiftGeneticSparseLabeling(
    _3DNeuralCellStructureDeterminationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003125",
        "MosaicismWithRepeatFrameshiftGeneticSparseLabeling",
    )


class _3DMolecularStructureDeterminationAssayOfAnAntigenAntibodyComplex(
    _3DStructureDeterminationOfBoundMolecularComplexAssay, BCellEpitopeAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001721",
        "_3DMolecularStructureDeterminationAssayOfAnAntigenAntibodyComplex",
    )


class _3DMolecularStructureDeterminationAssayOfATCellEpitopeMhcTcrComplex(
    _3DStructureDeterminationOfBoundMolecularComplexAssay, TCellEpitopeAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001999",
        "_3DMolecularStructureDeterminationAssayOfATCellEpitopeMhcTcrComplex",
    )


class _3DMolecularStructureDeterminationAssayOfAMhcLigandComplex(
    _3DStructureDeterminationOfBoundMolecularComplexAssay, MhcLigandAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002050",
        "_3DMolecularStructureDeterminationAssayOfAMhcLigandComplex",
    )


class EnhancedCrossLinkingImmunoprecipitationHighThroughputSequencingAssay(
    IndividualNucleotideResolutionCrossLinkingAndImmunoprecipitationSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002111",
        "EnhancedCrossLinkingImmunoprecipitationHighThroughputSequencingAssay",
    )


class ReducedRepresentationBisulfiteSequencingAssay(BisulfiteSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001862",
        "ReducedRepresentationBisulfiteSequencingAssay",
    )


class ShotgunBisulfiteSeqAssay(BisulfiteSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001863", "ShotgunBisulfiteSeqAssay"
    )


class TetAssistedBisulfiteSequencingAssay(BisulfiteSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002086",
        "TetAssistedBisulfiteSequencingAssay",
    )


class MethylcCaptureSequencingAssay(BisulfiteSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002094", "MethylcCaptureSequencingAssay"
    )


class CarbonCopyChromosomeConformationCaptureAssayFollowedBySequencingAssay(
    CarbonCopyChromosomeConformationCaptureAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002042",
        "CarbonCopyChromosomeConformationCaptureAssayFollowedBySequencingAssay",
    )


class SolidSequencingAssay(DnaSequencingByLigationAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000706", "SolidSequencingAssay")


class ChainTerminationSequencingAssay(DnaSequencingBySynthesisAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000695", "ChainTerminationSequencingAssay"
    )


class HelicosSequencingAssay(DnaSequencingBySynthesisAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000697", "HelicosSequencingAssay"
    )


class SolexaSequencingAssay(DnaSequencingBySynthesisAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000724", "SolexaSequencingAssay"
    )


class PyrosequencingAssay(DnaSequencingBySynthesisAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000730", "PyrosequencingAssay")


class WholeViromeSequencingAssay(WholeMetagenomeSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002768", "WholeViromeSequencingAssay"
    )


class PrecisionNuclearRunOnSequencingAssay(RnaSeqAssay, PolymeraseChainReactionAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002457",
        "PrecisionNuclearRunOnSequencingAssay",
    )


class TranslationAssociatedTranscriptLeaderSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002033",
        "TranslationAssociatedTranscriptLeaderSequencingAssay",
    )


class TranscriptLeaderSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002034", "TranscriptLeaderSequencingAssay"
    )


class RibosomalProfilingBySequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002038",
        "RibosomalProfilingBySequencingAssay",
    )


class SelfTranscribingActiveRegulatoryRegionSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002041",
        "SelfTranscribingActiveRegulatoryRegionSequencingAssay",
    )


class RnaBindNSeqAssay(RnaSeqAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002044", "RnaBindNSeqAssay")


class PolyaSiteSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002045", "PolyaSiteSequencingAssay"
    )


class SmallRnaSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002112", "SmallRnaSequencingAssay"
    )


class BromouridineLabelingAndSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002113",
        "BromouridineLabelingAndSequencingAssay",
    )


class BromouridinePulseChaseAndSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002114",
        "BromouridinePulseChaseAndSequencingAssay",
    )


class BromourideLabelingAndSequencingAfterUvExposure(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002143",
        "BromourideLabelingAndSequencingAfterUvExposure",
    )


class PolyaSelectedRnaSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002571", "PolyaSelectedRnaSequencingAssay"
    )


class PolyaDepletedRnaSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002572", "PolyaDepletedRnaSequencingAssay"
    )


class IsoformSequencing(RnaSeqAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002575", "IsoformSequencing")


class SingleCellRnaSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002631", "SingleCellRnaSequencingAssay"
    )


class RibosomalRnaDepletedRnaSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002759",
        "RibosomalRnaDepletedRnaSequencingAssay",
    )


class MetatranscriptomeSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002760", "MetatranscriptomeSequencingAssay"
    )


class BulkRnaSeqAssay(RnaSeqAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003090", "BulkRnaSeqAssay")


class SlideSeqAssay(RnaSeqAssay):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003107", "SlideSeqAssay")


class SingleNucleusRnaSequencingAssay(RnaSeqAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003109", "SingleNucleusRnaSequencingAssay"
    )


class MonospecificTCellRecognitionAssayMeasuringMhcLigandProcessingAndPresentation(
    AssayMeasuringMhcLigandProcessingAndPresentation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001469",
        "MonospecificTCellRecognitionAssayMeasuringMhcLigandProcessingAndPresentation",
    )


class MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentation(
    AssayMeasuringMhcLigandProcessingAndPresentation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001478",
        "MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentation",
    )


class CoelutionAssayMeasuringMhcLigandProcessingAndPresentationUsingTCellRecognitionOfHplcFractionatedEluateComparedToSyntheticLigand(
    AssayMeasuringMhcLigandProcessingAndPresentation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001500",
        "CoelutionAssayMeasuringMhcLigandProcessingAndPresentationUsingTCellRecognitionOfHplcFractionatedEluateComparedToSyntheticLigand",
    )


class EdmanDegradationAssayMeasuringMhcLigandProcessingAndPresentation(
    AssayMeasuringMhcLigandProcessingAndPresentation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001509",
        "EdmanDegradationAssayMeasuringMhcLigandProcessingAndPresentation",
    )


class HighThroughputMultiplexedAssayMeasuringMhcLigandProcessingAndPresentation(
    AssayMeasuringMhcLigandProcessingAndPresentation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003326",
        "HighThroughputMultiplexedAssayMeasuringMhcLigandProcessingAndPresentation",
    )


class AssayMeasuringQualitativeBindingOfAMhcLigandComplex(
    AssayMeasuringBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002072",
        "AssayMeasuringQualitativeBindingOfAMhcLigandComplex",
    )


class AssayMeasuringQuantitativeBindingOfAMhcLigandComplex(
    AssayMeasuringBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003145",
        "AssayMeasuringQuantitativeBindingOfAMhcLigandComplex",
    )


class HighThroughputMultiplexedAssayMeasuringBindingOfAMhcLigandComplex(
    AssayMeasuringBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003325",
        "HighThroughputMultiplexedAssayMeasuringBindingOfAMhcLigandComplex",
    )


class AssayMeasuringEpitopeSpecificImmunoglobulinMediatedAntigenActivation(
    AssayMeasuringBiologicalActivityResultingFromBCellEpitopeAntibodyBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001640",
        "AssayMeasuringEpitopeSpecificImmunoglobulinMediatedAntigenActivation",
    )


class AssayMeasuringEpitopeSpecificImmunoglobulinMediatedNeutralization(
    AssayMeasuringBiologicalActivityResultingFromBCellEpitopeAntibodyBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001643",
        "AssayMeasuringEpitopeSpecificImmunoglobulinMediatedNeutralization",
    )


class AssayMeasuringBCellEpitopeSpecificInVivoActivity(
    AssayMeasuringBiologicalActivityResultingFromBCellEpitopeAntibodyBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001698",
        "AssayMeasuringBCellEpitopeSpecificInVivoActivity",
    )


class AssayMeasuringEpitopeSpecificActivationOfAdditionalImmuneResponseInVitro(
    AssayMeasuringBiologicalActivityResultingFromBCellEpitopeAntibodyBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001704",
        "AssayMeasuringEpitopeSpecificActivationOfAdditionalImmuneResponseInVitro",
    )


class AssayMeasuringEpitopeSpecificAntigenInhibitionOfAntibodyActivity(
    AssayMeasuringBiologicalActivityResultingFromBCellEpitopeAntibodyBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001705",
        "AssayMeasuringEpitopeSpecificAntigenInhibitionOfAntibodyActivity",
    )


class AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringBindingOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001703",
        "AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringQuantitativeBindingOfAnAntigenAntibodyComplex(
    AssayMeasuringBindingOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003146",
        "AssayMeasuringQuantitativeBindingOfAnAntigenAntibodyComplex",
    )


class HighThroughputMultiplexedAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringBindingOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003323",
        "HighThroughputMultiplexedAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringEpitopeSpecificTCellKilling(
    AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding,
    CellCellKillingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110130",
        "AssayMeasuringEpitopeSpecificTCellKilling",
    )


class AssayMeasuringEpitopeSpecificCytotoxicTCellDegranulation(
    AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001269",
        "AssayMeasuringEpitopeSpecificCytotoxicTCellDegranulation",
    )


class AssayMeasuringEpitopeSpecificTCellActivation(
    AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001407",
        "AssayMeasuringEpitopeSpecificTCellActivation",
    )


class AssayMeasuringTCellEpitopeSpecificInVivoActivity(
    AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001484",
        "AssayMeasuringTCellEpitopeSpecificInVivoActivity",
    )


class AssayMeasuringTCellEpitopeSpecificSuppressionInVitro(
    AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002074",
        "AssayMeasuringTCellEpitopeSpecificSuppressionInVitro",
    )


class AssayMeasuringEpitopeSpecificCytokineProductionByTCells(
    AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110129",
        "AssayMeasuringEpitopeSpecificCytokineProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificProliferationOfTCells(
    AssayMeasuringBiologicalActivityResultingFromTCellEpitopeMhcTcrBinding
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110131",
        "AssayMeasuringEpitopeSpecificProliferationOfTCells",
    )


class AssayMeasuringQuantitativeBindingOfAnEpitopeMhcTcrComplex(
    AssayMeasuringBindingOfATCellEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003147",
        "AssayMeasuringQuantitativeBindingOfAnEpitopeMhcTcrComplex",
    )


class HighThroughputMultiplexedAssayMeasuringBindingOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringBindingOfATCellEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003324",
        "HighThroughputMultiplexedAssayMeasuringBindingOfATCellEpitopeMhcTcrComplex",
    )


class AssayMeasuringQualitativeBindingOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringBindingOfATCellEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110124",
        "AssayMeasuringQualitativeBindingOfATCellEpitopeMhcTcrComplex",
    )


class InjectionIntoOrganSection(Injection):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000431", "InjectionIntoOrganSection"
    )


class ExperimentalInfectionOfCellCulture(AddingSubstanceToCellCulture):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110030",
        "ExperimentalInfectionOfCellCulture",
    )


class IntramuscularInjection(AdministeringSubstanceInVivo, Injection):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000934", "IntramuscularInjection"
    )


class IntradermalInjection(AdministeringSubstanceInVivo, Injection):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000942", "IntradermalInjection")


class SubcutaneousInjection(AdministeringSubstanceInVivo, Injection):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000954", "SubcutaneousInjection"
    )


class IntravenousInjection(AdministeringSubstanceInVivo, Injection):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000994", "IntravenousInjection")


class IntraperitonealAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000429", "IntraperitonealAdministration"
    )


class OralAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000952", "OralAdministration")


class IntranasalMucosalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000983", "IntranasalMucosalAdministration"
    )


class PassiveImmunization(AdministeringSubstanceInVivo):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001174", "PassiveImmunization")


class AntibioticAdministrationProcess(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003057", "AntibioticAdministrationProcess"
    )


class AdministeringSubstanceInVivoToCauseDisease(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003413",
        "AdministeringSubstanceInVivoToCauseDisease",
    )


class AdministeringSubstanceInVivoToReduceOrPreventDisease(
    AdministeringSubstanceInVivo
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003414",
        "AdministeringSubstanceInVivoToReduceOrPreventDisease",
    )


class InVivoChallenge(AdministeringSubstanceInVivo):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003456", "InVivoChallenge")


class IntragastricAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003553", "IntragastricAdministration"
    )


class IntracolonicAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003554", "IntracolonicAdministration"
    )


class VaginalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003555", "VaginalAdministration"
    )


class TopicalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003556", "TopicalAdministration"
    )


class CervicalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003557", "CervicalAdministration"
    )


class ConjunctivalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003558", "ConjunctivalAdministration"
    )


class IntratrachealAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003559", "IntratrachealAdministration"
    )


class IntraAmnioticAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003560", "IntraAmnioticAdministration"
    )


class IntraArterialAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003561", "IntraArterialAdministration"
    )


class IntracerebralAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003562", "IntracerebralAdministration"
    )


class IntracranialAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003563", "IntracranialAdministration"
    )


class IntraepidermalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003564", "IntraepidermalAdministration"
    )


class IntralymphaticAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003565", "IntralymphaticAdministration"
    )


class UrethralAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003567", "UrethralAdministration"
    )


class IntrauteralAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003569", "IntrauteralAdministration"
    )


class IntraocularAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003571", "IntraocularAdministration"
    )


class IntraplacentalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003572", "IntraplacentalAdministration"
    )


class IntrarectalAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003573", "IntrarectalAdministration"
    )


class IntrasplenicAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003574", "IntrasplenicAdministration"
    )


class IntratumoralAdministration(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003603", "IntratumoralAdministration"
    )


class AdministrationInVivoWithInfectiousAgent(AdministeringSubstanceInVivo):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110007",
        "AdministrationInVivoWithInfectiousAgent",
    )


class Vaccination(AdministeringSubstanceInVivo):
    term = RdfTerm("http://purl.obolibrary.org/obo/VO_0000002", "Vaccination")


class AntibodyPurificationOfMhcClassIProteinComplex(
    AntibodyPurificationOfMhcProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003616",
        "AntibodyPurificationOfMhcClassIProteinComplex",
    )


class AntibodyPurificationOfMhcClassIiProteinComplex(
    AntibodyPurificationOfMhcProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003636",
        "AntibodyPurificationOfMhcClassIiProteinComplex",
    )


class DnaExtraction(NucleicAcidExtraction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000257", "DnaExtraction")


class RnaExtraction(NucleicAcidExtraction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0666666", "RnaExtraction")


class ChemicalMutagenesis(RandomMutagenesis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003129", "ChemicalMutagenesis")


class IrradiationMutagenesis(RandomMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003130", "IrradiationMutagenesis"
    )


class TransgenicMutagenesis(RandomMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003136", "TransgenicMutagenesis"
    )


class TransposonInducedMutagenesis(RandomMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003140", "TransposonInducedMutagenesis"
    )


class EndonucleaseMediatedMutagenesis(DirectedMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003132", "EndonucleaseMediatedMutagenesis"
    )


class TargetedMutagenesis(DirectedMutagenesis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003139", "TargetedMutagenesis")


class _5RapidAmplificationOfCdnaEnds(RapidAmplificationOfCdnaEnds):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002091", "_5RapidAmplificationOfCdnaEnds"
    )


class _3RapidAmplificationOfCdnaEnds(RapidAmplificationOfCdnaEnds):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002092", "_3RapidAmplificationOfCdnaEnds"
    )


class ArthropodSpecimenCollectionByAspiration(AdultArthropodSpecimenCollectionProcess):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002912",
        "ArthropodSpecimenCollectionByAspiration",
    )


class LandingArthropodSpecimenCollectionProcess(
    AdultArthropodSpecimenCollectionProcess
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003003",
        "LandingArthropodSpecimenCollectionProcess",
    )


class FlyingAdultArthropodCollectionProcessByPassiveInterception(
    AdultArthropodSpecimenCollectionProcess
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003004",
        "FlyingAdultArthropodCollectionProcessByPassiveInterception",
    )


class KnockdownArthropodSpecimenCollectionByPyrethrumSpray(
    KnockdownArthropodSpecimenCollectionProcess
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002917",
        "KnockdownArthropodSpecimenCollectionByPyrethrumSpray",
    )


class ImageGuidedBiopsy(NeedleBiopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002651", "ImageGuidedBiopsy")


class FineNeedleAspirationBiopsy(NeedleBiopsy):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002655", "FineNeedleAspirationBiopsy"
    )


class CoreNeedleBiopsy(NeedleBiopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002656", "CoreNeedleBiopsy")


class VacuumAssistedBiopsy(NeedleBiopsy):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002745", "VacuumAssistedBiopsy")


class DnaSequencingService(SequencingService):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000992", "DnaSequencingService")


class HolmBonferroniFamilyWiseErrorRateCorrectionMethod(
    FamilyWiseErrorRateCorrectionMethod
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200066",
        "HolmBonferroniFamilyWiseErrorRateCorrectionMethod",
    )


class WestfallAndYoungFamilyWiseErrorRateCorrection(
    FamilyWiseErrorRateCorrectionMethod
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200092",
        "WestfallAndYoungFamilyWiseErrorRateCorrection",
    )


class BenjaminiAndHochbergFalseDiscoveryRateCorrectionMethod(
    FalseDiscoveryRateCorrectionMethod
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200036",
        "BenjaminiAndHochbergFalseDiscoveryRateCorrectionMethod",
    )


class BenjaminiAndYekutieliFalseDiscoveryRateCorrectionMethod(
    FalseDiscoveryRateCorrectionMethod
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200049",
        "BenjaminiAndYekutieliFalseDiscoveryRateCorrectionMethod",
    )


class CytometryAnalysisByAutomatedGating(Gating):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002776",
        "CytometryAnalysisByAutomatedGating",
    )


class CytometryAnalysisByManualGating(Gating):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002777", "CytometryAnalysisByManualGating"
    )


class LoessGlobalTransformationOneChannel(LoessGlobalTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200013",
        "LoessGlobalTransformationOneChannel",
    )


class LoessGlobalTransformationTwoChannel(LoessGlobalTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200015",
        "LoessGlobalTransformationTwoChannel",
    )


class LoessGroupTransformationOneChannel(LoessGroupTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200018",
        "LoessGroupTransformationOneChannel",
    )


class LoessGroupTransformationTwoChannel(LoessGroupTransformation):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200019",
        "LoessGroupTransformationTwoChannel",
    )


class AverageLinkageHierarchicalClustering(AgglomerativeHierarchicalClustering):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200043",
        "AverageLinkageHierarchicalClustering",
    )


class CompleteLinkageHierarchicalClustering(AgglomerativeHierarchicalClustering):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200044",
        "CompleteLinkageHierarchicalClustering",
    )


class SingleLinkageHierarchicalClustering(AgglomerativeHierarchicalClustering):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200045",
        "SingleLinkageHierarchicalClustering",
    )


class RowSubmatrixExtraction(SubmatrixExtraction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200075", "RowSubmatrixExtraction"
    )


class ColumnSubmatrixExtraction(SubmatrixExtraction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0200076", "ColumnSubmatrixExtraction"
    )


class Plasmid(DoubleStrandedDna):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000430", "Plasmid")


class YeastArtificialChromosomeVector(CloningVector, DoubleStrandedDna):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000709", "YeastArtificialChromosomeVector"
    )


class PcrProduct(AmplifiedDna, DoubleStrandedDna):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000406", "PcrProduct")


class Cd4PositiveAlphaBetaTCell(AlphaBetaTCell):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CL_0000624", "Cd4PositiveAlphaBetaTCell"
    )


class Cd8PositiveAlphaBetaTCell(AlphaBetaTCell):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CL_0000625", "Cd8PositiveAlphaBetaTCell"
    )


class MatureNkTCell(AlphaBetaTCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CL_0000814", "MatureNkTCell")


class H2DbProteinComplex(MouseMhcClassIProteinComplexWithH2BHaplotype):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000966", "H2DbProteinComplex")


class H2KbProteinComplex(MouseMhcClassIProteinComplexWithH2BHaplotype):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000991", "H2KbProteinComplex")


class H2IadProteinComplex(H2IaProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000973", "H2IadProteinComplex")


class H2Iag7ProteinComplex(H2IaProteinComplex):
    term = RdfTerm("http://purl.obolibrary.org/obo/MRO_0000975", "H2Iag7ProteinComplex")


class MortalCellLineCell(CellLineCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CLO_0000018", "MortalCellLineCell")


class ImmortalCellLineCell(CellLineCell):
    term = RdfTerm("http://purl.obolibrary.org/obo/CLO_0000019", "ImmortalCellLineCell")


class Ion316ChipV2(IonSemiconductorChip):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001971", "Ion316ChipV2")


class Ion318ChipV2(IonSemiconductorChip):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001972", "Ion318ChipV2")


class Ion314ChipV2(IonSemiconductorChip):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001974", "Ion314ChipV2")


class AmnisImagestream(MultispectralImagingFlowCytometer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400054", "AmnisImagestream")


class OpticalMicroscope(Microscope):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000940", "OpticalMicroscope")


class ElectronMicroscope(Microscope):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000990", "ElectronMicroscope")


class ConfocalMicroscope(Microscope):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001079", "ConfocalMicroscope")


class LaserCaptureMicrodissectionMicroscope(Microscope):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001096",
        "LaserCaptureMicrodissectionMicroscope",
    )


class ScanningForceMicroscope(Microscope):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001105", "ScanningForceMicroscope"
    )


class DigitalMicroscope(Microscope):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001126", "DigitalMicroscope")


class TecmagEagleProbe(SolidNmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000564", "TecmagEagleProbe")


class JeolCapnmrProbe(JeolNmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000635", "JeolCapnmrProbe")


class BrukerHighResolutionProbe(BrukerNmrProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000480", "BrukerHighResolutionProbe"
    )


class BrukerCryoprobe(BrukerNmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000531", "BrukerCryoprobe")


class Bruker1MmMicroprobe(BrukerNmrProbe):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000590", "Bruker1MmMicroprobe")


class BrukerMicroImagingProbe(BrukerNmrProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000620", "BrukerMicroImagingProbe"
    )


class BrukerSolidMagicAngleSpinningProbe(BrukerNmrProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000629",
        "BrukerSolidMagicAngleSpinningProbe",
    )


class BrukerLcNmrPlatform(BrukerNmrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000503", "BrukerLcNmrPlatform")


class BrukerAmxSeriesNmrInstrument(BrukerNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000514", "BrukerAmxSeriesNmrInstrument"
    )


class BrukerAcSeriesNmrInstrument(BrukerNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000541", "BrukerAcSeriesNmrInstrument"
    )


class BrukerCapillaryLcNmrPlatform(BrukerNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000553", "BrukerCapillaryLcNmrPlatform"
    )


class AvanceIiSpectrometer(BrukerNmrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000580", "AvanceIiSpectrometer")


class BrukerLcNmrMsPlatform(BrukerNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000582", "BrukerLcNmrMsPlatform"
    )


class BrukerSpeNmrPlatform(BrukerNmrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000613", "BrukerSpeNmrPlatform")


class BrukerMetabolicProfiler(BrukerNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000632", "BrukerMetabolicProfiler"
    )


class JeolEcxNmrSpectrometer(JeolNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000625", "JeolEcxNmrSpectrometer"
    )


class JeolEcaNmrSpectrometer(JeolNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000641", "JeolEcaNmrSpectrometer"
    )


class VarianGeminiSpectrometer(VarianNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000477", "VarianGeminiSpectrometer"
    )


class VarianVxrSpectrometer(VarianNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000524", "VarianVxrSpectrometer"
    )


class VarianUnityInovaSpectrometer(VarianNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000558", "VarianUnityInovaSpectrometer"
    )


class VarianUnitySpectrometer(VarianNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000579", "VarianUnitySpectrometer"
    )


class VarianMercurySpectrometer(VarianNmrInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000631", "VarianMercurySpectrometer"
    )


class AvalanchePhotodiode(Photodiode):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400011", "AvalanchePhotodiode")


class Solid3PlusSystem(AbSolidSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002007", "Solid3PlusSystem")


class Solid4System(AbSolidSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002024", "Solid4System")


class IlluminaGenomeAnalyzerIix(IlluminaGenomeAnalyzerIi):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002000", "IlluminaGenomeAnalyzerIix"
    )


class IlluminaGenomeAnalyzerIie(IlluminaGenomeAnalyzerIi):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002027", "IlluminaGenomeAnalyzerIie"
    )


class IlluminaHiseq2000(IlluminaHiseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002001", "IlluminaHiseq2000")


class IlluminaHiseq2500(IlluminaHiseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002002", "IlluminaHiseq2500")


class IlluminaHiseq1000(IlluminaHiseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002022", "IlluminaHiseq1000")


class IlluminaHiseq3000(IlluminaHiseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002048", "IlluminaHiseq3000")


class IlluminaHiseq4000(IlluminaHiseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002049", "IlluminaHiseq4000")


class IlluminaHiseqXTen(IlluminaHiseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002129", "IlluminaHiseqXTen")


class IlluminaHiseq1500(IlluminaHiseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003386", "IlluminaHiseq1500")


class IlluminaNextseq500(IlluminaNextseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002021", "IlluminaNextseq500")


class IlluminaNextseq550(IlluminaNextseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003387", "IlluminaNextseq550")


class IlluminaNextseq1000(IlluminaNextseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003606", "IlluminaNextseq1000")


class IlluminaNovaseq6000(IlluminaNovaseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002630", "IlluminaNovaseq6000")


class IlluminaNovaseqX(IlluminaNovaseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003663", "IlluminaNovaseqX")


class IlluminaNovaseqXPlus(IlluminaNovaseqSeriesInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003664", "IlluminaNovaseqXPlus")


class PortableFluorometer(Fluorometer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001120", "PortableFluorometer")


class FlowCytometerAnalyzer(FlowCytometer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400008", "FlowCytometerAnalyzer"
    )


class FlowCytometerSorter(FlowCytometer, MaterialSeparationDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400099", "FlowCytometerSorter")


class AnionTrapColumn(TrapColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000562", "AnionTrapColumn")


class CationTrapColumn(TrapColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000593", "CationTrapColumn")


class CationExchangeColumn(IonExchangeColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000490", "CationExchangeColumn")


class AnionExchangeColumn(IonExchangeColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000584", "AnionExchangeColumn")


class GelFiltrationColumn(SizeExclusionColumn):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000535", "GelFiltrationColumn")


class GasChromatographyDetector(ChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000637", "GasChromatographyDetector"
    )


class DualLoopAutosampler(LiquidChromatographyAutosampler):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000500", "DualLoopAutosampler")


class PreparativeAutosampler(LiquidChromatographyAutosampler):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000526", "PreparativeAutosampler"
    )


class NanoPumpSystem(ChromatographyPumpSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000474", "NanoPumpSystem")


class VacuumDegasser(ChromatographyPumpSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000495", "VacuumDegasser")


class CapillaryPumpSystem(ChromatographyPumpSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000546", "CapillaryPumpSystem")


class IsocraticPumpSystem(ChromatographyPumpSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000556", "IsocraticPumpSystem")


class FlashPumpSystem(ChromatographyPumpSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000557", "FlashPumpSystem")


class GradientPumpSystem(ChromatographyPumpSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000573", "GradientPumpSystem")


class QuaternaryPumpSystem(ChromatographyPumpSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000627", "QuaternaryPumpSystem")


class PulsedFieldGelElectrophoresisSystem(GelElectrophoresisSystem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001106",
        "PulsedFieldGelElectrophoresisSystem",
    )


class AgaroseGelElectrophoresisSystem(GelElectrophoresisSystem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001134", "AgaroseGelElectrophoresisSystem"
    )


class PolystyreneTube(TestTube):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000084", "PolystyreneTube")


class NmrSampleTube(TestTube):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000578", "NmrSampleTube")


class AnticoagulantContainingTestTube(TestTube):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000784", "AnticoagulantContainingTestTube"
    )


class CellSorterCollectionTube(TestTube):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400020", "CellSorterCollectionTube"
    )


class CytometerSampleTube(TestTube):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400091", "CytometerSampleTube")


class DiodeLaser(Laser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400033", "DiodeLaser")


class DyeLaser(Laser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400034", "DyeLaser")


class GasLaser(Laser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400047", "GasLaser")


class SolidStateLaser(Laser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400096", "SolidStateLaser")


class ColumnConnector(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000478", "ColumnConnector")


class SampleInlet(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000497", "SampleInlet")


class SampleInjectionSystem(ChromatographyDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000504", "SampleInjectionSystem"
    )


class ColumnJacket(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000508", "ColumnJacket")


class LiquidChromatographyValve(ChromatographyDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000528", "LiquidChromatographyValve"
    )


class ColumnCartridge(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000532", "ColumnCartridge")


class GasChromatographyEquipment(ChromatographyDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000542", "GasChromatographyEquipment"
    )


class ColumnCompartment(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000545", "ColumnCompartment")


class NeedleAssembly(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000551", "NeedleAssembly")


class TransferLine(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000572", "TransferLine")


class ColumnAdapter(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000594", "ColumnAdapter")


class ChromatographyConsumable(ChromatographyDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000601", "ChromatographyConsumable"
    )


class ColumnFrit(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000602", "ColumnFrit")


class ChartRecorder(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000605", "ChartRecorder")


class GuardColumn(ChromatographyDevice):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000614", "GuardColumn")


class ChromatographySplitter(ChromatographyDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000619", "ChromatographySplitter"
    )


class LiquidChromatographyInstrument(ChromatographyDevice):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001139", "LiquidChromatographyInstrument"
    )


class PcrInstrument(ThermalCycler):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000989", "PcrInstrument")


class SandBath(TemperatureControlBath):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003688", "SandBath")


class IceBath(TemperatureControlBath):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003689", "IceBath")


class DryIceBath(TemperatureControlBath):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003690", "DryIceBath")


class LiquidNitrogenBath(TemperatureControlBath):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003691", "LiquidNitrogenBath")


class WaterBath(TemperatureControlBath):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400155", "WaterBath")


class OilBath(TemperatureControlBath):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400157", "OilBath")


class Methylation450KBeadchip(IlluminaMethylationBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002004", "Methylation450KBeadchip"
    )


class Methylation27KBeadchip(IlluminaMethylationBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002005", "Methylation27KBeadchip"
    )


class IlluminaInfiniumMethylationepicV10Beadchip(IlluminaMethylationBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002131",
        "IlluminaInfiniumMethylationepicV10Beadchip",
    )


class IlluminaInfiniumMethylationepicV20Beadchip(IlluminaMethylationBeadchip):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003650",
        "IlluminaInfiniumMethylationepicV20Beadchip",
    )


class SnpMicroarray(DnaMicroarray):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001204", "SnpMicroarray")


class TilingMicroarray(DnaMicroarray):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001307", "TilingMicroarray")


class Agilent026655WholeMouseGenomeMicroarray4X44KV2(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003388",
        "Agilent026655WholeMouseGenomeMicroarray4X44KV2",
    )


class Agilent030493SureprintG3MouseExon4X180KMicroarray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003389",
        "Agilent030493SureprintG3MouseExon4X180KMicroarray",
    )


class Agilent074809SureprintG3MouseGeV28X60KMicroarray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003390",
        "Agilent074809SureprintG3MouseGeV28X60KMicroarray",
    )


class AffymetrixMouseGenome43020Array(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003391", "AffymetrixMouseGenome43020Array"
    )


class AffymetrixMouseGenome430A20Array(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003392", "AffymetrixMouseGenome430A20Array"
    )


class AffymetrixMouseGene10StArray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003393", "AffymetrixMouseGene10StArray"
    )


class AffymetrixMouseGene21StArray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003394", "AffymetrixMouseGene21StArray"
    )


class AffymetrixRhesusMacaqueGenomeArray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003395",
        "AffymetrixRhesusMacaqueGenomeArray",
    )


class AffymetrixHumanTranscriptomeArray20(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003396",
        "AffymetrixHumanTranscriptomeArray20",
    )


class AffymetrixHumanGenomeU219Array(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003397", "AffymetrixHumanGenomeU219Array"
    )


class AffymetrixHumanGene20StArray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003398", "AffymetrixHumanGene20StArray"
    )


class AffymetrixClariomSAssayHuman(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003399", "AffymetrixClariomSAssayHuman"
    )


class AffymetrixClariomSAssayMouse(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003400", "AffymetrixClariomSAssayMouse"
    )


class AffymetrixMouseExonJunctionArray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003403", "AffymetrixMouseExonJunctionArray"
    )


class AffymetrixHumanExonJunctionArray(DnaMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003404", "AffymetrixHumanExonJunctionArray"
    )


class SurgicalN95Respirator(N95Respirator):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002809", "SurgicalN95Respirator"
    )


class ReusablePatientGown(PatientGown):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002794", "ReusablePatientGown")


class DisposablePatientGown(PatientGown):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002795", "DisposablePatientGown"
    )


class SurgicalGown(MedicalGown):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002798", "SurgicalGown")


class MedicalGlove(PersonalProtectiveGlove):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002803", "MedicalGlove")


class NitrileGlove(PersonalProtectiveGlove):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002804", "NitrileGlove")


class DisposableFootwearCover(FootwearCover):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002807", "DisposableFootwearCover"
    )


class ReusableFootwearCover(FootwearCover):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002808", "ReusableFootwearCover"
    )


class OdorBaitedCdcLightTrap(CentersForDiseaseControlAndPreventionLightTrap):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003550", "OdorBaitedCdcLightTrap"
    )


class CancerCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001906", "CancerCellLine")


class _293TCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110028", "_293TCellLine")


class C1RCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110029", "C1RCellLine")


class El4CellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110031", "El4CellLine")


class HelaCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110032", "HelaCellLine")


class JawsIiCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110033", "JawsIiCellLine")


class JurkatCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110035", "JurkatCellLine")


class JyCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110036", "JyCellLine")


class RmaCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110038", "RmaCellLine")


class T2CellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110039", "T2CellLine")


class LCellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110099", "LCellLine")


class P815CellLine(ImmortalCellLine):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110118", "P815CellLine")


class DengueVirus(Flaviviridae):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_12637", "DengueVirus")


class HepacivirusHominis(Flaviviridae):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_3052230", "HepacivirusHominis"
    )


class HumanImmunodeficiencyVirus1(Lentivirus):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_11676", "HumanImmunodeficiencyVirus1"
    )


class HumanImmunodeficiencyVirus2(Lentivirus):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_11709", "HumanImmunodeficiencyVirus2"
    )


class Ecdysozoa(Bilateria):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_1206794", "Ecdysozoa")


class VertebrataVertebrates(Bilateria):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_7742", "VertebrataVertebrates"
    )


class SaccharomycesCerevisiae(Saccharomyceta):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_4932", "SaccharomycesCerevisiae"
    )


class Neurospora(Saccharomyceta):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_5140", "Neurospora")


class TrachealAspirateSpecimen(LowerRespiratoryTractAspirateSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002778", "TrachealAspirateSpecimen"
    )


class EndotrachealAspirateSpecimen(LowerRespiratoryTractAspirateSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002972", "EndotrachealAspirateSpecimen"
    )


class MidTurbinateNasalSwabSpecimen(NasalSwabSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002779", "MidTurbinateNasalSwabSpecimen"
    )


class AnteriorNasalSwabSpecimen(NasalSwabSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002784", "AnteriorNasalSwabSpecimen"
    )


class NasopharyngealAspirateSpecimen(NasopharynxSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000914", "NasopharyngealAspirateSpecimen"
    )


class NasopharyngealSwabSpecimen(NasopharynxSpecimen, SwabSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002606", "NasopharyngealSwabSpecimen"
    )


class PlateletPoorPlasmaSpecimen(BloodPlasmaSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002774", "PlateletPoorPlasmaSpecimen"
    )


class BloodSerumSpecimen(BloodPlasmaSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0100017", "BloodSerumSpecimen")


class UmbilicalCordBloodSpecimen(ArterialBloodSpecimen):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_2000012", "UmbilicalCordBloodSpecimen"
    )


class UmbilicalCordBlood(ArterialBlood):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/UBERON_0012168", "UmbilicalCordBlood"
    )


class CytologicalStainRole(DyeRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000026", "CytologicalStainRole")


class PhIndicatorDyeRole(DyeRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000110", "PhIndicatorDyeRole")


class VitalDyeRole(DyeRole):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000221", "VitalDyeRole")


class LuminousFlux(OpticalQuality):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001296", "LuminousFlux")


class FMatingType(BacterialMatingType):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001347", "FMatingType")


class FMinusMatingType(BacterialMatingType):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001348", "FMinusMatingType")


class SaccharomycesCerevisiaeMatingType(YeastMatingType):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0001342",
        "SaccharomycesCerevisiaeMatingType",
    )


class SchizosaccharomycesPombeMatingType(YeastMatingType):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0001343",
        "SchizosaccharomycesPombeMatingType",
    )


class Haploid(Euploid):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001375", "Haploid")


class Polyploid(Euploid):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001377", "Polyploid")


class Diploid(Euploid):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001394", "Diploid")


class DiffusionWeightedMagneticResonanceImageDataSet(
    ReconstructedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003335",
        "DiffusionWeightedMagneticResonanceImageDataSet",
    )


class FunctionalMagneticResonanceImageDataSet(
    ReconstructedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003336",
        "FunctionalMagneticResonanceImageDataSet",
    )


class PerfusionWeightedMagneticResonanceImageDataSet(
    ReconstructedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003339",
        "PerfusionWeightedMagneticResonanceImageDataSet",
    )


class ProtonDensityMagneticResonanceImageDataSet(
    ReconstructedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003340",
        "ProtonDensityMagneticResonanceImageDataSet",
    )


class T1WeightedMagneticResonanceImageDataSet(
    ReconstructedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003341",
        "T1WeightedMagneticResonanceImageDataSet",
    )


class T2WeightedMagneticResonanceImageDataSet(
    ReconstructedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003348",
        "T2WeightedMagneticResonanceImageDataSet",
    )


class ProbabilisticBrainRegionAtlasImageDataset(BrainRegionAtlasImageDataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003358",
        "ProbabilisticBrainRegionAtlasImageDataset",
    )


class DeterministicBrainRegionAtlasImageDataSet(BrainRegionAtlasImageDataSet):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003359",
        "DeterministicBrainRegionAtlasImageDataSet",
    )


class LesionMask(ImageSegmentationMap):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003361", "LesionMask")


class ExternalImportOntologyModule(ImportOntologyModule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000011", "ExternalImportOntologyModule"
    )


class OboBasicSubsetOntologyModule(OntologyModuleSubsettedByExpressivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000018", "OboBasicSubsetOntologyModule"
    )


class OntologyModuleSubsettedByOwlProfile(OntologyModuleSubsettedByExpressivity):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_8000019",
        "OntologyModuleSubsettedByOwlProfile",
    )


class AgeSincePlantingMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001156", "AgeSincePlantingMeasurementDatum"
    )


class AgeSinceHatchingMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001157", "AgeSinceHatchingMeasurementDatum"
    )


class AgeSinceEggLayingMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001159",
        "AgeSinceEggLayingMeasurementDatum",
    )


class AgeSinceGerminationMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001161",
        "AgeSinceGerminationMeasurementDatum",
    )


class AgeSinceEclosionMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001163", "AgeSinceEclosionMeasurementDatum"
    )


class AgeSinceSowingMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001164", "AgeSinceSowingMeasurementDatum"
    )


class AgeSinceCoitusMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001165", "AgeSinceCoitusMeasurementDatum"
    )


class AgeSinceFertilizationMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001168",
        "AgeSinceFertilizationMeasurementDatum",
    )


class AgeSinceBirthMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001169", "AgeSinceBirthMeasurementDatum"
    )


class AgeWhenGaveBirthToFirstChild(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002396", "AgeWhenGaveBirthToFirstChild"
    )


class AgeSinceCultureSeedingMeasurementDatum(AgeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002465",
        "AgeSinceCultureSeedingMeasurementDatum",
    )


class HalfLifeOfBindingDatum(HalfLifeDatumT12, BindingConstant):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001583", "HalfLifeOfBindingDatum"
    )


class SpecimenCollectionTimePostDiseaseOnset(SpecimenCollectionTimeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003083",
        "SpecimenCollectionTimePostDiseaseOnset",
    )


class SpecimenCollectionTimePostInfection(SpecimenCollectionTimeMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003084",
        "SpecimenCollectionTimePostInfection",
    )


class EquilibriumDissociationConstantKdApproximatedByEc50(
    Ec50BindingDatum, EquilibriumDissociationConstantKd
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001581",
        "EquilibriumDissociationConstantKdApproximatedByEc50",
    )


class EquilibriumDissociationConstantKdApproximatedByIc50(
    Ic50BindingDatum, EquilibriumDissociationConstantKd
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001571",
        "EquilibriumDissociationConstantKdApproximatedByIc50",
    )


class EthicalStandardComplianceRule(StandardComplianceRule):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500025", "EthicalStandardComplianceRule"
    )


class TranscriptionStartSiteIdentificationObjective(
    TranscriptionProfilingIdentificationObjective
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001851",
        "TranscriptionStartSiteIdentificationObjective",
    )


class PurificationObjective(SeparationIntoDifferentCompositionObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000796", "PurificationObjective"
    )


class MultipleTestingCorrectionObjective(ErrorCorrectionObjective):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000791",
        "MultipleTestingCorrectionObjective",
    )


class Bcl2FastqSoftwareApplication(BaseCallingApplication):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002470", "Bcl2FastqSoftwareApplication"
    )


class DoseResponseDesign(CompoundTreatmentDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001418", "DoseResponseDesign")


class CrossOverDesign(RepeatedMeasureDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500003", "CrossOverDesign")


class LatinSquareDesign(RandomizedCompleteBlockDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500011", "LatinSquareDesign")


class GraecoLatinSquareDesign(RandomizedCompleteBlockDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500012", "GraecoLatinSquareDesign"
    )


class HyperGraecoLatinSquareDesign(RandomizedCompleteBlockDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0500013", "HyperGraecoLatinSquareDesign"
    )


class ChipChipByTilingArrayDesign(ChipChipDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001417", "ChipChipByTilingArrayDesign"
    )


class EnzymaticReactionIdentificationDesign(DirectInteractionIdentificationDesign):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002595",
        "EnzymaticReactionIdentificationDesign",
    )


class EpitopeSpecificHelperTCellEnhancementOfTCellMediatedImmuneResponse(
    HelperTCellEnhancementOfTCellMediatedImmuneResponse
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001420",
        "EpitopeSpecificHelperTCellEnhancementOfTCellMediatedImmuneResponse",
    )


class EpitopeSpecificTCellEnhancementOfBCellMediatedImmuneResponse(
    HelperTCellEnhancementOfBCellMediatedImmuneResponse
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001314",
        "EpitopeSpecificTCellEnhancementOfBCellMediatedImmuneResponse",
    )


class WidefieldMicroscopyAssay(FluorescenceMicroscopyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002437", "WidefieldMicroscopyAssay"
    )


class LightsheetFluorescenceMicroscopyAssay(FluorescenceMicroscopyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003098",
        "LightsheetFluorescenceMicroscopyAssay",
    )


class CentreForDiseaseControlAndPreventionBottleBioassay(
    DirectInsecticideResistanceDiagnosticAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002710",
        "CentreForDiseaseControlAndPreventionBottleBioassay",
    )


class WhoConeKitDiagnosticAssay(DirectInsecticideResistanceDiagnosticAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002711", "WhoConeKitDiagnosticAssay"
    )


class WhoPaperKitDiagnosticAssay(DirectInsecticideResistanceDiagnosticAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002712", "WhoPaperKitDiagnosticAssay"
    )


class WhoLarvicideDiagnosticAssay(DirectInsecticideResistanceDiagnosticAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002713", "WhoLarvicideDiagnosticAssay"
    )


class InsecticideResistanceDoseResponseByBottleAssay(
    InsecticideResistanceDoseResponseAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002714",
        "InsecticideResistanceDoseResponseByBottleAssay",
    )


class InsecticideResistanceDoseResponseBySurvivalOfLarvaeAssay(
    InsecticideResistanceDoseResponseAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002715",
        "InsecticideResistanceDoseResponseBySurvivalOfLarvaeAssay",
    )


class InsecticideResistanceDoseResponseByWhoPaperKitAssay(
    InsecticideResistanceDoseResponseAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002716",
        "InsecticideResistanceDoseResponseByWhoPaperKitAssay",
    )


class InsecticideResistanceTimeResponseByBottleAssay(
    InsecticideResistanceTimeResponseAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002717",
        "InsecticideResistanceTimeResponseByBottleAssay",
    )


class InsecticideResistanceTimeResponseByWhoPaperKitAssay(
    InsecticideResistanceTimeResponseAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002718",
        "InsecticideResistanceTimeResponseByWhoPaperKitAssay",
    )


class NeuronMorphologyReconstructionAssay(NeuronMorphologyAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003126",
        "NeuronMorphologyReconstructionAssay",
    )


class NmrAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex(
    _3DMolecularStructureDeterminationAssayOfAnAntigenAntibodyComplex,
    Nmr3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001647",
        "NmrAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex",
    )


class XRayCrystallographyAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex(
    _3DMolecularStructureDeterminationAssayOfAnAntigenAntibodyComplex,
    XRayCrystallography3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001738",
        "XRayCrystallographyAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex",
    )


class ElectronMicroscopyAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex(
    _3DMolecularStructureDeterminationAssayOfAnAntigenAntibodyComplex,
    ElectronMicroscopy3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001646",
        "ElectronMicroscopyAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex",
    )


class SmallAngleScatteringAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex(
    _3DMolecularStructureDeterminationAssayOfAnAntigenAntibodyComplex,
    SmallAngleScattering3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002101",
        "SmallAngleScatteringAssayDeterminingThe3DStructureOfABCellEpitopeAntibodyComplex",
    )


class XRayCrystallographyAssayDeterminingThe3DStructureOfATCellEpitopeMhcTcrComplex(
    _3DMolecularStructureDeterminationAssayOfATCellEpitopeMhcTcrComplex,
    XRayCrystallography3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001311",
        "XRayCrystallographyAssayDeterminingThe3DStructureOfATCellEpitopeMhcTcrComplex",
    )


class ElectronMicroscopyAssayDeterminingThe3DStructureOfATCellEpitopeMhcTcrComplex(
    _3DMolecularStructureDeterminationAssayOfATCellEpitopeMhcTcrComplex,
    ElectronMicroscopy3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003612",
        "ElectronMicroscopyAssayDeterminingThe3DStructureOfATCellEpitopeMhcTcrComplex",
    )


class XRayCrystallographyAssayDeterminingThe3DStructureOfAMhcLigandComplex(
    _3DMolecularStructureDeterminationAssayOfAMhcLigandComplex,
    XRayCrystallography3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001595",
        "XRayCrystallographyAssayDeterminingThe3DStructureOfAMhcLigandComplex",
    )


class ElectronMicroscopyAssayDeterminingThe3DStructureOfAMhcLigandComplex(
    _3DMolecularStructureDeterminationAssayOfAMhcLigandComplex,
    ElectronMicroscopy3DMolecularStructureDeterminationAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003613",
        "ElectronMicroscopyAssayDeterminingThe3DStructureOfAMhcLigandComplex",
    )


class SingleCellCombinatorialIndexingRnaSequencingAssay(SingleCellRnaSequencingAssay):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003105",
        "SingleCellCombinatorialIndexingRnaSequencingAssay",
    )


class SingleNucleusChromatinAccessibilityAndMrnaExpressionSequencingAssay(
    SingleNucleusRnaSequencingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003108",
        "SingleNucleusChromatinAccessibilityAndMrnaExpressionSequencingAssay",
    )


class MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentationOfMhcLigandsElutedFromCellularMhc(
    MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001489",
        "MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentationOfMhcLigandsElutedFromCellularMhc",
    )


class MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentationOfMhcLigandsElutedFromSecretedMhc(
    MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001510",
        "MassSpectrometryAssayMeasuringMhcLigandProcessingAndPresentationOfMhcLigandsElutedFromSecretedMhc",
    )


class AssayMeasuringBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringQualitativeBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001550",
        "AssayMeasuringBindingOfACellBoundMhcLigandComplex",
    )


class AssayMeasuringBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringQualitativeBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001555",
        "AssayMeasuringBindingOfAPurifiedMhcLigandComplex",
    )


class AssayMeasuringBindingOfACellLysateMhcLigandComplex(
    AssayMeasuringQualitativeBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001579",
        "AssayMeasuringBindingOfACellLysateMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuring50DissociationOfBindingTemperatureTmOfAPurifiedMhcLigandComplex(
    BindingAssayUsingFluorescenceDetection,
    AssayMeasuringQuantitativeBindingOfAMhcLigandComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001604",
        "FluorescenceDetectionAssayMeasuring50DissociationOfBindingTemperatureTmOfAPurifiedMhcLigandComplex",
    )


class AssayMeasuringABindingConstantOfAMhcLigandComplex(
    AssayMeasuringQuantitativeBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001553",
        "AssayMeasuringABindingConstantOfAMhcLigandComplex",
    )


class AssayMeasuringTheHalfMaximalEffectiveConcentrationEc50OfAMhcLigandComplex(
    AssayMeasuringQuantitativeBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001991",
        "AssayMeasuringTheHalfMaximalEffectiveConcentrationEc50OfAMhcLigandComplex",
    )


class AssayMeasuringTheHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplex(
    AssayMeasuringQuantitativeBindingOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001992",
        "AssayMeasuringTheHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplex",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallenge(
    AssayMeasuringBCellEpitopeSpecificInVivoActivity, EpitopeProtectionExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001710",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallenge",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificDiseaseExacerbation(
    AssayMeasuringBCellEpitopeSpecificInVivoActivity,
    EpitopeDiseaseExacerbationExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001711",
        "InVivoAssayMeasuringBCellEpitopeSpecificDiseaseExacerbation",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificTreatmentOfDisease(
    AssayMeasuringBCellEpitopeSpecificInVivoActivity, EpitopeTreatmentExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001697",
        "InVivoAssayMeasuringBCellEpitopeSpecificTreatmentOfDisease",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificToleranceInduction(
    AssayMeasuringBCellEpitopeSpecificInVivoActivity,
    EpitopeToleranceInductionExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001693",
        "InVivoAssayMeasuringBCellEpitopeSpecificToleranceInduction",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromFertility(
    AssayMeasuringBCellEpitopeSpecificInVivoActivity,
    EfficacyOfEpitopeInterventionExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001692",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromFertility",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificInductionOfHypersensitivity(
    AssayMeasuringBCellEpitopeSpecificInVivoActivity,
    EfficacyOfEpitopeInterventionExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001694",
        "InVivoAssayMeasuringBCellEpitopeSpecificInductionOfHypersensitivity",
    )


class InVivoAssayMeasuringABCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    AssayMeasuringBCellEpitopeSpecificInVivoActivity
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002677",
        "InVivoAssayMeasuringABCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class AssayMeasuringEpitopeSpecificIgMediatedHistamineRelease(
    AssayMeasuringEpitopeSpecificActivationOfAdditionalImmuneResponseInVitro
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001639",
        "AssayMeasuringEpitopeSpecificIgMediatedHistamineRelease",
    )


class AssayMeasuringEpitopeSpecificComplementDependentCytotoxicity(
    AssayMeasuringEpitopeSpecificActivationOfAdditionalImmuneResponseInVitro
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001641",
        "AssayMeasuringEpitopeSpecificComplementDependentCytotoxicity",
    )


class AssayMeasuringEpitopeSpecificAntibodyDependentCellularCytotoxicity(
    AssayMeasuringEpitopeSpecificActivationOfAdditionalImmuneResponseInVitro
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001642",
        "AssayMeasuringEpitopeSpecificAntibodyDependentCellularCytotoxicity",
    )


class AssayMeasuringEpitopeSpecificOpsonization(
    AssayMeasuringEpitopeSpecificActivationOfAdditionalImmuneResponseInVitro
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001644",
        "AssayMeasuringEpitopeSpecificOpsonization",
    )


class AssayMeasuringEpitopeSpecificImmuneComplexFormation(
    AssayMeasuringEpitopeSpecificActivationOfAdditionalImmuneResponseInVitro
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001695",
        "AssayMeasuringEpitopeSpecificImmuneComplexFormation",
    )


class ElectronMicroscopyAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    ElectronMicroscopyImagingAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001656",
        "ElectronMicroscopyAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ElisaMeasuringBindingOfABCellEpitopeAntibodyComplex(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001657",
        "ElisaMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ChromatographyAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AnalyticalChromatography,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001661",
        "ChromatographyAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ImmunoprecipitationAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    ImmunoprecipitationAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001653",
        "ImmunoprecipitationAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ImmunoblotAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    ImmunoblotAssay, AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001650",
        "ImmunoblotAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class MicroarrayAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex, MicroarrayAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002053",
        "MicroarrayAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class MassSpectrometryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
    MassSpectrometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001654",
        "MassSpectrometryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ViralHemagglutinationInhibitionAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
    ViralHemagglutinationInhibitionAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001724",
        "ViralHemagglutinationInhibitionAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class RiaMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex, RadioImmunoAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001649",
        "RiaMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class PlasmonResonanceAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    SurfacePlasmonResonanceBindingAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001651",
        "PlasmonResonanceAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class PhageDisplayAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    PhageDisplayBindingAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001655",
        "PhageDisplayAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class QuenchingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AntibodyBindingDetectionByFluorescenceQuenching,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001726",
        "QuenchingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class CrossBlockingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AntibodyCrossBlockingAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001648",
        "CrossBlockingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class CalorimetryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    CalorimetricBindingAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001645",
        "CalorimetryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class BioLayerInterferometryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
    BioLayerInterferometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002104",
        "BioLayerInterferometryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class FlowCytometryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001659",
        "FlowCytometryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ElispotAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    EnzymeLinkedImmunospotAssay,
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001658",
        "ElispotAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class FootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex, FootprintingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002449",
        "FootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ImmunoStainingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    ImmunoStainingAssay, AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001652",
        "ImmunoStainingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class NmrAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001662",
        "NmrAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class AntigenInhibitionAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQualitativeBindingOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001701",
        "AntigenInhibitionAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringABindingConstantOfABCellEpitopeAntibodyComplex(
    AssayMeasuringQuantitativeBindingOfAnAntigenAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001709",
        "AssayMeasuringABindingConstantOfABCellEpitopeAntibodyComplex",
    )


class InVitroAssayMeasuringEpitopeSpecificTCellKilling(
    AssayMeasuringEpitopeSpecificTCellKilling, InVitroCellKillingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002062",
        "InVitroAssayMeasuringEpitopeSpecificTCellKilling",
    )


class AssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells(
    AssayMeasuringEpitopeSpecificCytotoxicTCellDegranulation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001436",
        "AssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells",
    )


class AssayMeasuringEpitopeSpecificPerforinReleaseByTCells(
    AssayMeasuringEpitopeSpecificCytotoxicTCellDegranulation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001497",
        "AssayMeasuringEpitopeSpecificPerforinReleaseByTCells",
    )


class AssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells(
    AssayMeasuringEpitopeSpecificCytotoxicTCellDegranulation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001809",
        "AssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells",
    )


class AssayMeasuringEpitopeSpecificGranulysinReleaseByTCells(
    AssayMeasuringEpitopeSpecificCytotoxicTCellDegranulation
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001810",
        "AssayMeasuringEpitopeSpecificGranulysinReleaseByTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallenge(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity, EpitopeProtectionExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002073",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallenge",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificDiseaseExacerbation(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity,
    EpitopeDiseaseExacerbationExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001467",
        "InVivoAssayMeasuringTCellEpitopeSpecificDiseaseExacerbation",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificTreatmentOfDisease(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity, EpitopeTreatmentExperiment
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001507",
        "InVivoAssayMeasuringTCellEpitopeSpecificTreatmentOfDisease",
    )


class InVivoSkinTestAssayMeasuringTCellEpitopeSpecificTypeIvHypersensitivity(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity,
    EfficacyOfEpitopeInterventionExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001348",
        "InVivoSkinTestAssayMeasuringTCellEpitopeSpecificTypeIvHypersensitivity",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificToleranceInduction(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity,
    EpitopeToleranceInductionExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001324",
        "InVivoAssayMeasuringTCellEpitopeSpecificToleranceInduction",
    )


class InVivoAssayMeasuringEpitopeSpecificTCellKilling(
    AssayMeasuringEpitopeSpecificTCellKilling,
    AssayMeasuringTCellEpitopeSpecificInVivoActivity,
    InVivoCellKillingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001392",
        "InVivoAssayMeasuringEpitopeSpecificTCellKilling",
    )


class InVivoAssayMeasuringEpitopeSpecificTCellHelperActivity(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001495",
        "InVivoAssayMeasuringEpitopeSpecificTCellHelperActivity",
    )


class InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002676",
        "InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001198",
        "AssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001209",
        "AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001217",
        "AssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001218",
        "AssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001230",
        "AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificRantesProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001232",
        "AssayMeasuringEpitopeSpecificRantesProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001233",
        "AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001237",
        "AssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001251",
        "AssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells",
    )


class AssayMeasuringInterleukin9ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001253",
        "AssayMeasuringInterleukin9ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001264",
        "AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001276",
        "AssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001280",
        "AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001292",
        "AssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001295",
        "AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificIp10ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001308",
        "AssayMeasuringEpitopeSpecificIp10ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001333",
        "AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001345",
        "AssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001363",
        "AssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001380",
        "AssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001388",
        "AssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001390",
        "AssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001391",
        "AssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001400",
        "AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001406",
        "AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001414",
        "AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001445",
        "AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001449",
        "AssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001450",
        "AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001451",
        "AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001456",
        "AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001459",
        "AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001465",
        "AssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001570",
        "AssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001587",
        "AssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001600",
        "AssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCCMotifLigand21ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001774",
        "AssayMeasuringEpitopeSpecificChemokineCCMotifLigand21ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCCMotifLigand19ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001775",
        "AssayMeasuringEpitopeSpecificChemokineCCMotifLigand19ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand12ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001776",
        "AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand12ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001777",
        "AssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand16ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001778",
        "AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand16ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand13ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001779",
        "AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand13ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCCMotifLigand17ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002056",
        "AssayMeasuringEpitopeSpecificChemokineCCMotifLigand17ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificMacrophageMigrationInhibitoryFactorMifProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002057",
        "AssayMeasuringEpitopeSpecificMacrophageMigrationInhibitoryFactorMifProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificOncostatinMProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002058",
        "AssayMeasuringEpitopeSpecificOncostatinMProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificChemokineCCMotifLigand20ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002134",
        "AssayMeasuringEpitopeSpecificChemokineCCMotifLigand20ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterferonAlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002452",
        "AssayMeasuringEpitopeSpecificInterferonAlphaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificAmphiregulinProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003315",
        "AssayMeasuringEpitopeSpecificAmphiregulinProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificLymphotactinProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003372",
        "AssayMeasuringEpitopeSpecificLymphotactinProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells(
    AssayMeasuringEpitopeSpecificCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003484",
        "AssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells",
    )


class InVivoAssayMeasuringEpitopeSpecificProliferationOfTCells(
    AssayMeasuringTCellEpitopeSpecificInVivoActivity,
    AssayMeasuringEpitopeSpecificProliferationOfTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002070",
        "InVivoAssayMeasuringEpitopeSpecificProliferationOfTCells",
    )


class InVitroAssayMeasuringEpitopeSpecificProliferationOfTCells(
    AssayMeasuringEpitopeSpecificProliferationOfTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002071",
        "InVitroAssayMeasuringEpitopeSpecificProliferationOfTCells",
    )


class AssayMeasuringABindingConstantOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringQuantitativeBindingOfAnEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002059",
        "AssayMeasuringABindingConstantOfATCellEpitopeMhcTcrComplex",
    )


class MhcTetramerMultimerAssayMeasuringBindingOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringQualitativeBindingOfATCellEpitopeMhcTcrComplex,
    FlowCytometryAssay,
    FluorescenceDetectionAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110179",
        "MhcTetramerMultimerAssayMeasuringBindingOfATCellEpitopeMhcTcrComplex",
    )


class FlowCytometryAssayMeasuringCellCellBindingOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringQualitativeBindingOfATCellEpitopeMhcTcrComplex, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001317",
        "FlowCytometryAssayMeasuringCellCellBindingOfATCellEpitopeMhcTcrComplex",
    )


class IntraperitonealInjection(IntraperitonealAdministration, Injection):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000281", "IntraperitonealInjection"
    )


class OralIngestionOfPill(OralAdministration):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000837", "OralIngestionOfPill")


class EpitopeSpecificImmuneIntervention(PassiveImmunization):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001192",
        "EpitopeSpecificImmuneIntervention",
    )


class PathogenChallenge(InVivoChallenge):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000712", "PathogenChallenge")


class TumorChallenge(InVivoChallenge):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003455", "TumorChallenge")


class IntracarotidAdministration(IntraArterialAdministration):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003570", "IntracarotidAdministration"
    )


class SkinScarificationAdministration(IntraepidermalAdministration):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003568", "SkinScarificationAdministration"
    )


class LymphNodeAdministration(IntralymphaticAdministration):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003566", "LymphNodeAdministration"
    )


class AntibodyPurificationOfRatMhcClassIProteinComplex(
    AntibodyPurificationOfMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003626",
        "AntibodyPurificationOfRatMhcClassIProteinComplex",
    )


class AntibodyPurificationOfMouseMhcClassIProteinComplex(
    AntibodyPurificationOfMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003627",
        "AntibodyPurificationOfMouseMhcClassIProteinComplex",
    )


class AntibodyPurificationOfPigMhcClassIProteinComplexCattleMhcClassIProteinComplexAndOrHumanMhcClassIProteinComplex(
    AntibodyPurificationOfMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003635",
        "AntibodyPurificationOfPigMhcClassIProteinComplexCattleMhcClassIProteinComplexAndOrHumanMhcClassIProteinComplex",
    )


class AntibodyPurificationOfCattleMhcClassIiProteinComplex(
    AntibodyPurificationOfMhcClassIiProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003637",
        "AntibodyPurificationOfCattleMhcClassIiProteinComplex",
    )


class AntibodyPurificationOfHumanMhcClassIiProteinComplex(
    AntibodyPurificationOfMhcClassIiProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003638",
        "AntibodyPurificationOfHumanMhcClassIiProteinComplex",
    )


class AntibodyPurificationOfMouseMhcClassIiProteinComplexAndOrRatMhcClassIiProteinComplexWithRt1AHaplotype(
    AntibodyPurificationOfMhcClassIiProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003646",
        "AntibodyPurificationOfMouseMhcClassIiProteinComplexAndOrRatMhcClassIiProteinComplexWithRt1AHaplotype",
    )


class ViralRnaExtraction(RnaExtraction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000407", "ViralRnaExtraction")


class PolyaRnaExtraction(RnaExtraction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000848", "PolyaRnaExtraction")


class OrganellarRnaExtraction(RnaExtraction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000849", "OrganellarRnaExtraction"
    )


class TotalRnaExtraction(RnaExtraction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000855", "TotalRnaExtraction")


class CytoplasmicRnaExtraction(RnaExtraction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000859", "CytoplasmicRnaExtraction"
    )


class NuclearRnaExtraction(RnaExtraction):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000888", "NuclearRnaExtraction")


class RnaExtractionWithPolyaDepletion(RnaExtraction):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002574", "RnaExtractionWithPolyaDepletion"
    )


class GeneTrapMutagenesis(TransgenicMutagenesis):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003137", "GeneTrapMutagenesis")


class EnhancerTrapMutagenesis(TransgenicMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003138", "EnhancerTrapMutagenesis"
    )


class CasMediatedMutagenesis(EndonucleaseMediatedMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003133", "CasMediatedMutagenesis"
    )


class TalenMediatedMutagenesis(EndonucleaseMediatedMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003134", "TalenMediatedMutagenesis"
    )


class ZincFingerMediatedMutagenesis(EndonucleaseMediatedMutagenesis):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003135", "ZincFingerMediatedMutagenesis"
    )


class _5RnaLigaseMediatedRapidAmplificationOfCdnaEnds(_5RapidAmplificationOfCdnaEnds):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002093",
        "_5RnaLigaseMediatedRapidAmplificationOfCdnaEnds",
    )


class AnimalBitingArthropodSpecimenCollectionByAspiration(
    ArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002905",
        "AnimalBitingArthropodSpecimenCollectionByAspiration",
    )


class ArthropodRestingInAnimalHouseSpecimenCollectionByAspiration(
    ArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002908",
        "ArthropodRestingInAnimalHouseSpecimenCollectionByAspiration",
    )


class HumanBitingArthropodSpecimenCollectionByAspiration(
    ArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002914",
        "HumanBitingArthropodSpecimenCollectionByAspiration",
    )


class DaytimeArthropodSpecimenCollectionByAspiration(
    ArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003001",
        "DaytimeArthropodSpecimenCollectionByAspiration",
    )


class ArthropodRestingInHumanHouseSpecimenCollectionByAspiration(
    ArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003002",
        "ArthropodRestingInHumanHouseSpecimenCollectionByAspiration",
    )


class ComputedTomographyAssistedBiopsy(ImageGuidedBiopsy):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002652", "ComputedTomographyAssistedBiopsy"
    )


class UltrasoundGuidedNeedleBiopsy(ImageGuidedBiopsy):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002653", "UltrasoundGuidedNeedleBiopsy"
    )


class RecombinantPlasmid(Plasmid, RecombinantVector):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000410", "RecombinantPlasmid")


class CloningPlasmid(CloningVector, Plasmid):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000729", "CloningPlasmid")


class Cd8PositiveAlphaBetaCytotoxicTCell(Cd8PositiveAlphaBetaTCell):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/CL_0000794",
        "Cd8PositiveAlphaBetaCytotoxicTCell",
    )


class StereoMicroscope(OpticalMicroscope):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001065", "StereoMicroscope")


class SpinningDiskConfocalMicroscope(ConfocalMicroscope):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001055", "SpinningDiskConfocalMicroscope"
    )


class ProgrammableArrayMicroscope(ConfocalMicroscope):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001071", "ProgrammableArrayMicroscope"
    )


class LaserScanningConfocalMicroscope(ConfocalMicroscope):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001125", "LaserScanningConfocalMicroscope"
    )


class FlowHighResolutionProbe(BrukerHighResolutionProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000527", "FlowHighResolutionProbe"
    )


class HighResolutionMagicAngleSpinProbe(BrukerHighResolutionProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000607",
        "HighResolutionMagicAngleSpinProbe",
    )


class HighResolutionProbeWithAutomaticTuningAndMatching(BrukerHighResolutionProbe):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000616",
        "HighResolutionProbeWithAutomaticTuningAndMatching",
    )


class LsrfortessaX20(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001871", "LsrfortessaX20")


class A10Analyzer(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400005", "A10Analyzer")


class A40Minifcm(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400006", "A40Minifcm")


class Bactiflow(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400012", "Bactiflow")


class CellLabQuantaSc(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400018", "CellLabQuantaSc")


class Cyan(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400022", "Cyan")


class CyflowMl(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400023", "CyflowMl")


class CyflowSl(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400024", "CyflowSl")


class CyflowSl3(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400025", "CyflowSl3")


class CytobuoyFlowCytometerAnalyzer(FlowCytometerAnalyzer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400027", "CytobuoyFlowCytometerAnalyzer"
    )


class Cytosence(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400028", "Cytosence")


class Cytosub(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400029", "Cytosub")


class FacsCanto(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400037", "FacsCanto")


class FacsCanto2(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400038", "FacsCanto2")


class FacsScan(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400039", "FacsScan")


class Fc500(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400042", "Fc500")


class GuavaEasycyteMini(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400048", "GuavaEasycyteMini")


class GuavaEasycytePlus(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400049", "GuavaEasycytePlus")


class GuavaPersonalCellAnalysis(FlowCytometerAnalyzer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400050", "GuavaPersonalCellAnalysis"
    )


class GuavaPersonalCellAnalysis96(FlowCytometerAnalyzer):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400051", "GuavaPersonalCellAnalysis96"
    )


class InfluxAnalyzer(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400055", "InfluxAnalyzer")


class Luminex100(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400069", "Luminex100")


class Luminex200(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400070", "Luminex200")


class MacsQuant(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400071", "MacsQuant")


class Somacount(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400097", "Somacount")


class Somascope(FlowCytometerAnalyzer):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400098", "Somascope")


class Biosorter1000(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400014", "Biosorter1000")


class Biosorter2000(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400015", "Biosorter2000")


class Biosorter250(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400016", "Biosorter250")


class Biosorter500(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400017", "Biosorter500")


class CyflowSpace(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400026", "CyflowSpace")


class FacsCalibur(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400036", "FacsCalibur")


class Facsaria(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400040", "Facsaria")


class Facsvantage(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400041", "Facsvantage")


class InfluxCellSorter(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400056", "InfluxCellSorter")


class Lsr2(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400068", "Lsr2")


class Moflo(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400075", "Moflo")


class Reflection(FlowCytometerSorter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400089", "Reflection")


class ThermalConductivityDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000466", "ThermalConductivityDetector"
    )


class NitrogenPhosphorousDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000489", "NitrogenPhosphorousDetector"
    )


class PhotoionizationDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000506", "PhotoionizationDetector"
    )


class ElectronCaptureDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000509", "ElectronCaptureDetector"
    )


class FlameIonizationDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000521", "FlameIonizationDetector"
    )


class MassSelectiveDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000569", "MassSelectiveDetector"
    )


class FlamePhotometricDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000588", "FlamePhotometricDetector"
    )


class OzoneInducedChemiluminescenceDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000598",
        "OzoneInducedChemiluminescenceDetector",
    )


class FluorineInducedChemiluminescenceDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000617",
        "FluorineInducedChemiluminescenceDetector",
    )


class AtomicEmissionDetector(GasChromatographyDetector):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000642", "AtomicEmissionDetector"
    )


class IonLaser(GasLaser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400060", "IonLaser")


class MetalVaporLaser(GasLaser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400073", "MetalVaporLaser")


class NeodymiumYagLaser(SolidStateLaser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400077", "NeodymiumYagLaser")


class YColumnConnector(ColumnConnector):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000581", "YColumnConnector")


class ManualInjectionSystem(SampleInjectionSystem):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000476", "ManualInjectionSystem"
    )


class SplitlessGcInjector(SampleInjectionSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000525", "SplitlessGcInjector")


class AutoInjector(SampleInjectionSystem):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000610", "AutoInjector")


class GasGenerator(GasChromatographyEquipment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000507", "GasGenerator")


class GasChromatographyOven(GasChromatographyEquipment):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000554", "GasChromatographyOven"
    )


class GasPurifier(GasChromatographyEquipment):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000638", "GasPurifier")


class InjectorLubricant(ChromatographyConsumable):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000511", "InjectorLubricant")


class PistonSeal(ChromatographyConsumable):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000568", "PistonSeal")


class ChromatographyDetectorFilter(ChromatographyConsumable):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000592", "ChromatographyDetectorFilter"
    )


class DetectorLamp(ChromatographyConsumable):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000604", "DetectorLamp")


class ChromatographyVial(ChromatographyConsumable):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002816", "ChromatographyVial")


class HighPerformanceLiquidChromatographyInstrument(LiquidChromatographyInstrument):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001057",
        "HighPerformanceLiquidChromatographyInstrument",
    )


class RealTimePcrMachine(PcrInstrument):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001110", "RealTimePcrMachine")


class Mouse385KWholeGenomeCghTilingArray(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002008",
        "Mouse385KWholeGenomeCghTilingArray",
    )


class Mouse3X720KWholeGenomeCghTilingArray(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002009",
        "Mouse3X720KWholeGenomeCghTilingArray",
    )


class Human3X720KWholeGenomeCghTilingArray(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002010",
        "Human3X720KWholeGenomeCghTilingArray",
    )


class Human21MWholeGenomeCghTilingArrayV20(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002011",
        "Human21MWholeGenomeCghTilingArrayV20",
    )


class HumanGenomeU133Plus20TilingArray(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002023", "HumanGenomeU133Plus20TilingArray"
    )


class HumanExon10StTillingArray(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002025", "HumanExon10StTillingArray"
    )


class HumanGenomeU133TilingArray(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002026", "HumanGenomeU133TilingArray"
    )


class Human6X630KCghWholeGenomeTilingArray(TilingMicroarray):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002109",
        "Human6X630KCghWholeGenomeTilingArray",
    )


class Hiv1GroupO(HumanImmunodeficiencyVirus1):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_388799", "Hiv1GroupO")


class CaenorhabditisElegans(Ecdysozoa):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_6239", "CaenorhabditisElegans"
    )


class Arthropoda(Ecdysozoa):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_6656", "Arthropoda")


class Euteleostomi(VertebrataVertebrates):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_117571", "Euteleostomi")


class AlbuminFreeSerum(BloodSerumSpecimen):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003652", "AlbuminFreeSerum")


class Fluorescence(LuminousFlux):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0000018", "Fluorescence")


class AMatingTypeYeast(SaccharomycesCerevisiaeMatingType):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001341", "AMatingTypeYeast")


class AlphaMatingTypeYeast(SaccharomycesCerevisiaeMatingType):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/PATO_0001344", "AlphaMatingTypeYeast"
    )


class HMinus(SchizosaccharomycesPombeMatingType):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001345", "HMinus")


class HPlus(SchizosaccharomycesPombeMatingType):
    term = RdfTerm("http://purl.obolibrary.org/obo/PATO_0001346", "HPlus")


class RestingStateFunctionalMagneticResonanceImageDataSet(
    FunctionalMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003337",
        "RestingStateFunctionalMagneticResonanceImageDataSet",
    )


class TaskBasedFunctionalMagneticResonanceImageDataSet(
    FunctionalMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003338",
        "TaskBasedFunctionalMagneticResonanceImageDataSet",
    )


class PostGdT1WeightedMagneticResonanceImageDataSet(
    T1WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003342",
        "PostGdT1WeightedMagneticResonanceImageDataSet",
    )


class T1WeightedGreMagneticResonanceImageDataSet(
    T1WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003343",
        "T1WeightedGreMagneticResonanceImageDataSet",
    )


class T1WeightedSeMagneticResonanceImageDataSet(
    T1WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003347",
        "T1WeightedSeMagneticResonanceImageDataSet",
    )


class T2WeightedFlairMagneticResonanceImageDataSet(
    T2WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003349",
        "T2WeightedFlairMagneticResonanceImageDataSet",
    )


class T2WeightedFseMagneticResonanceImageDataSet(
    T2WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003350",
        "T2WeightedFseMagneticResonanceImageDataSet",
    )


class T2WeightedSeMagneticResonanceImageDataSet(
    T2WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003351",
        "T2WeightedSeMagneticResonanceImageDataSet",
    )


class T2WeightedStirMagneticResonanceImageDataSet(
    T2WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003352",
        "T2WeightedStirMagneticResonanceImageDataSet",
    )


class T2WeightedGreMagneticResonanceImageDataSet(
    T2WeightedMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003353",
        "T2WeightedGreMagneticResonanceImageDataSet",
    )


class T1LesionMask(LesionMask):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003362", "T1LesionMask")


class T2FlairLesionMask(LesionMask):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003363", "T2FlairLesionMask")


class ElOntologyModule(OntologyModuleSubsettedByOwlProfile):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_8000020", "ElOntologyModule")


class AgeSinceBirthAtTimeOfEnrollment(AgeSinceBirthMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003075", "AgeSinceBirthAtTimeOfEnrollment"
    )


class AgeSinceBirthAtTimeOfVisit(AgeSinceBirthMeasurementDatum):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003076", "AgeSinceBirthAtTimeOfVisit"
    )


class NTo1Design(CrossOverDesign):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0500004", "NTo1Design")


class RadioactivityDetectionAssayMeasuringCompetitiveBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringBindingOfACellBoundMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001599",
        "RadioactivityDetectionAssayMeasuringCompetitiveBindingOfACellBoundMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringBindingOfACellBoundMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001602",
        "RadioactivityDetectionAssayMeasuringDirectBindingOfACellBoundMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringCompetitiveBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringBindingOfACellBoundMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001594",
        "FluorescenceDetectionAssayMeasuringCompetitiveBindingOfACellBoundMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringBindingOfACellBoundMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001606",
        "FluorescenceDetectionAssayMeasuringDirectBindingOfACellBoundMhcLigandComplex",
    )


class CellBoundMhcCompetitiveBindingAssayOfAMhcLigandComplexUsingTCellEpitopeRecognition(
    AssayMeasuringBindingOfACellBoundMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001493",
        "CellBoundMhcCompetitiveBindingAssayOfAMhcLigandComplexUsingTCellEpitopeRecognition",
    )


class PhageDisplayBindingAssayMeasuringBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringBindingOfAPurifiedMhcLigandComplex, PhageDisplayBindingAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001584",
        "PhageDisplayBindingAssayMeasuringBindingOfAPurifiedMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringCompetitiveBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringBindingOfAPurifiedMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001513",
        "RadioactivityDetectionAssayMeasuringCompetitiveBindingOfAPurifiedMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringDirectBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringBindingOfAPurifiedMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001608",
        "RadioactivityDetectionAssayMeasuringDirectBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringCompetitiveBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringBindingOfAPurifiedMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001534",
        "FluorescenceDetectionAssayMeasuringCompetitiveBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringDirectBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringBindingOfAPurifiedMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001590",
        "FluorescenceDetectionAssayMeasuringDirectBindingOfAPurifiedMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringDirectBindingOfACellLysateMhcLigandComplex(
    AssayMeasuringBindingOfACellLysateMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001556",
        "RadioactivityDetectionAssayMeasuringDirectBindingOfACellLysateMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringDirectBindingOfACellLysateMhcLigandComplex(
    AssayMeasuringBindingOfACellLysateMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001519",
        "FluorescenceDetectionAssayMeasuringDirectBindingOfACellLysateMhcLigandComplex",
    )


class AssayMeasuringTheAssociationConstantKaOfAMhcLigandComplex(
    AssayMeasuringABindingConstantOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001987",
        "AssayMeasuringTheAssociationConstantKaOfAMhcLigandComplex",
    )


class AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex(
    AssayMeasuringABindingConstantOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001988",
        "AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex",
    )


class AssayMeasuringTheHalfLifeOfAMhcLigandComplex(
    AssayMeasuringABindingConstantOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001990",
        "AssayMeasuringTheHalfLifeOfAMhcLigandComplex",
    )


class AssayMeasuringTheOffRateMeasurementKoffOfAMhcLigandComplex(
    AssayMeasuringABindingConstantOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001993",
        "AssayMeasuringTheOffRateMeasurementKoffOfAMhcLigandComplex",
    )


class AssayMeasuringTheMhcLigandBindingOnRateKonOfAMhcLigandComplex(
    AssayMeasuringABindingConstantOfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001994",
        "AssayMeasuringTheMhcLigandBindingOnRateKonOfAMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringHalfMaximalEffectiveConcentrationEc50ToDetermineDirectBindingOfACellLysateMhcLigandComplex(
    AssayMeasuringTheHalfMaximalEffectiveConcentrationEc50OfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001516",
        "RadioactivityDetectionAssayMeasuringHalfMaximalEffectiveConcentrationEc50ToDetermineDirectBindingOfACellLysateMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringHalfMaximalEffectiveConcentrationEc50ToDetermineDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheHalfMaximalEffectiveConcentrationEc50OfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001561",
        "FluorescenceDetectionAssayMeasuringHalfMaximalEffectiveConcentrationEc50ToDetermineDirectBindingOfACellBoundMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringHalfMaximalEffectiveConcentrationEc50ToDetermineDirectBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheHalfMaximalEffectiveConcentrationEc50OfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001592",
        "FluorescenceDetectionAssayMeasuringHalfMaximalEffectiveConcentrationEc50ToDetermineDirectBindingOfAPurifiedMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001517",
        "RadioactivityDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001568",
        "RadioactivityDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001520",
        "FluorescenceDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001613",
        "FluorescenceDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex",
    )


class CellBoundMhcCompetitiveBindingAssayMeasuringHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplexUsingTCellEpitopeRecognition(
    AssayMeasuringTheHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001597",
        "CellBoundMhcCompetitiveBindingAssayMeasuringHalfMaximalInhibitoryConcentrationIc50OfAMhcLigandComplexUsingTCellEpitopeRecognition",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallenge(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallenge,
    EpitopeProtectionFromInfectiousChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003465",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallenge",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallenge(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallenge,
    EpitopeProtectionFromTumorChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003466",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallenge",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallenge(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallenge
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003467",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallenge",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallenge,
    InVivoAssayMeasuringABCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002638",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificDiseaseExacerbationResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificDiseaseExacerbation,
    InVivoAssayMeasuringABCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002634",
        "InVivoAssayMeasuringBCellEpitopeSpecificDiseaseExacerbationResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificDiseaseReductionResultingFromAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificTreatmentOfDisease,
    InVivoAssayMeasuringABCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002636",
        "InVivoAssayMeasuringBCellEpitopeSpecificDiseaseReductionResultingFromAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificToleranceInductionResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificToleranceInduction,
    InVivoAssayMeasuringABCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002646",
        "InVivoAssayMeasuringBCellEpitopeSpecificToleranceInductionResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificInductionOfHypersensitivityResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificInductionOfHypersensitivity,
    InVivoAssayMeasuringABCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002666",
        "InVivoAssayMeasuringBCellEpitopeSpecificInductionOfHypersensitivityResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class HydrogenDeuteriumExchangeFootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    FootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex,
    HydrogenDeuteriumExchangeFootprintingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001997",
        "HydrogenDeuteriumExchangeFootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class HydroxylRadicalFootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    FootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex,
    HydroxylRadicalFootprintingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002450",
        "HydroxylRadicalFootprintingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class ImmunohistochemistryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex(
    ImmunoStainingAssayMeasuringBindingOfABCellEpitopeAntibodyComplex,
    Immunohistochemistry,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001998",
        "ImmunohistochemistryAssayMeasuringBindingOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringABindingConstantOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001708",
        "AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex(
    AssayMeasuringABindingConstantOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001718",
        "AssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex(
    AssayMeasuringABindingConstantOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001719",
        "AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex",
    )


class AssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex(
    AssayMeasuringABindingConstantOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001723",
        "AssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex",
    )


class _51ChromiumAssayMeasuringEpitopeSpecificTCellKilling(
    InVitroAssayMeasuringEpitopeSpecificTCellKilling, ChromiumReleaseAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110150",
        "_51ChromiumAssayMeasuringEpitopeSpecificTCellKilling",
    )


class ElisaMeasuringEpitopeSpecificGranzymeBReleaseByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001461",
        "ElisaMeasuringEpitopeSpecificGranzymeBReleaseByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells(
    AssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002066",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002065",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells",
    )


class IntracellularMaterialDetectionMeasuringEpitopeSpecificGranzymeBReleaseByTCells(
    AssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001423",
        "IntracellularMaterialDetectionMeasuringEpitopeSpecificGranzymeBReleaseByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells(
    AssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells, EnzymeLinkedImmunospotAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001322",
        "ElispotAssayMeasuringEpitopeSpecificGranzymeBReleaseByTCells",
    )


class ElisaMeasuringEpitopeSpecificPerforinReleaseByTCells(
    EnzymeLinkedImmunosorbentAssay, AssayMeasuringEpitopeSpecificPerforinReleaseByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002672",
        "ElisaMeasuringEpitopeSpecificPerforinReleaseByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificPerforinRelease(
    AssayMeasuringEpitopeSpecificPerforinReleaseByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001245",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificPerforinRelease",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificPerforinReleaseByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificPerforinReleaseByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003293",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificPerforinReleaseByTCells",
    )


class IntracellularMaterialDetectionAssayMeasuringEpitopeSpecificPerforinRelease(
    AssayMeasuringEpitopeSpecificPerforinReleaseByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001215",
        "IntracellularMaterialDetectionAssayMeasuringEpitopeSpecificPerforinRelease",
    )


class ElispotAssayMeasuringEpitopeSpecificPerforinReleaseByTCells(
    AssayMeasuringEpitopeSpecificPerforinReleaseByTCells, EnzymeLinkedImmunospotAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002069",
        "ElispotAssayMeasuringEpitopeSpecificPerforinReleaseByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells(
    AssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002064",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002063",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells",
    )


class IntracellularMaterialDetectionAssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells(
    AssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001660",
        "IntracellularMaterialDetectionAssayMeasuringEpitopeSpecificGranzymeAReleaseByTCells",
    )


class ElisaMeasuringEpitopeSpecificGranulysinReleaseByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificGranulysinReleaseByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001663",
        "ElisaMeasuringEpitopeSpecificGranulysinReleaseByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificGranulysinReleaseByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificGranulysinReleaseByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003292",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificGranulysinReleaseByTCells",
    )


class IntracellularMaterialDetectionAssayMeasuringEpitopeSpecificGranulysinReleaseByTCells(
    AssayMeasuringEpitopeSpecificGranulysinReleaseByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001664",
        "IntracellularMaterialDetectionAssayMeasuringEpitopeSpecificGranulysinReleaseByTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallenge(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallenge,
    EpitopeProtectionFromInfectiousChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003460",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallenge",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallenge(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallenge,
    EpitopeProtectionFromTumorChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003461",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallenge",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallenge(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallenge
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003462",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallenge",
    )


class InVivoAssayMeasuringEpitopeSpecificHelperTCellEnhancementOfABCellMediatedImmuneResponse(
    InVivoAssayMeasuringEpitopeSpecificTCellHelperActivity
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001228",
        "InVivoAssayMeasuringEpitopeSpecificHelperTCellEnhancementOfABCellMediatedImmuneResponse",
    )


class InVivoAssayMeasuringEpitopeSpecificHelperTCellEnhancementOfATCellMediatedImmuneResponse(
    InVivoAssayMeasuringEpitopeSpecificTCellHelperActivity
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001263",
        "InVivoAssayMeasuringEpitopeSpecificHelperTCellEnhancementOfATCellMediatedImmuneResponse",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallenge,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002637",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificDiseaseExacerbationResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringTCellEpitopeSpecificDiseaseExacerbation,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002678",
        "InVivoAssayMeasuringTCellEpitopeSpecificDiseaseExacerbationResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificDiseaseReductionResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringTCellEpitopeSpecificTreatmentOfDisease,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002635",
        "InVivoAssayMeasuringTCellEpitopeSpecificDiseaseReductionResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoSkinTestAssayMeasuringTCellEpitopeSpecificTypeIvHypersensitivityResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoSkinTestAssayMeasuringTCellEpitopeSpecificTypeIvHypersensitivity,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002667",
        "InVivoSkinTestAssayMeasuringTCellEpitopeSpecificTypeIvHypersensitivityResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificToleranceInductionResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringTCellEpitopeSpecificToleranceInduction,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002645",
        "InVivoAssayMeasuringTCellEpitopeSpecificToleranceInductionResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoAssayMeasuringEpitopeSpecificTCellKillingResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringEpitopeSpecificTCellKilling,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002671",
        "InVivoAssayMeasuringEpitopeSpecificTCellKillingResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin27ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001814",
        "ElisaMeasuringEpitopeSpecificInterleukin27ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001382",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001811",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001806",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001813",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin27ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin10ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110156",
        "ElisaMeasuringEpitopeSpecificInterleukin10ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001367",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin10ProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001220",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin10ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001297",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110177",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110170",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin10ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin22ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001236",
        "ElisaMeasuringEpitopeSpecificInterleukin22ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001279",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificIntracellularCytokineStainingIcsIl22ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001577",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificIntracellularCytokineStainingIcsIl22ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001496",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001821",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin22ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin8ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001359",
        "ElisaMeasuringEpitopeSpecificInterleukin8ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001801",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001457",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001609",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001800",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin8ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin5ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110154",
        "ElisaMeasuringEpitopeSpecificInterleukin5ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001255",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin5ProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001273",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin5ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001289",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001299",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001455",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin5ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificRantesProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificRantesProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001222",
        "ElisaMeasuringEpitopeSpecificRantesProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificRantesProductionByTCells(
    AssayMeasuringEpitopeSpecificRantesProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001325",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificRantesProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificRantesProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificRantesProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001412",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificRantesProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificRantesProductionByTCells(
    AssayMeasuringEpitopeSpecificRantesProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001789",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificRantesProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificRantesProductionByTCells(
    AssayMeasuringEpitopeSpecificRantesProductionByTCells, EnzymeLinkedImmunospotAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001790",
        "ElispotAssayMeasuringEpitopeSpecificRantesProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110157",
        "ElisaMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001357",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001341",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells",
    )


class CytometricBeadArrayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001490",
        "CytometricBeadArrayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001303",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001206",
        "ElispotAssayMeasuringEpitopeSpecificGranulocyteMacrophageColonyStimulatingFactorProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin21ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001346",
        "ElisaMeasuringEpitopeSpecificInterleukin21ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001298",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificIntracellularCytokineStainingIcsIl21ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001601",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificIntracellularCytokineStainingIcsIl21ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001342",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001826",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin21ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin13ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110159",
        "ElisaMeasuringEpitopeSpecificInterleukin13ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001542",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001349",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001309",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110171",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin13ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin9ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay, AssayMeasuringInterleukin9ProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001238",
        "ElisaMeasuringEpitopeSpecificInterleukin9ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells(
    AssayMeasuringInterleukin9ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001799",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringInterleukin9ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001532",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells(
    AssayMeasuringInterleukin9ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001798",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells(
    AssayMeasuringInterleukin9ProductionByTCells, EnzymeLinkedImmunospotAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001797",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin9ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001231",
        "ElisaMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001203",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001270",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001210",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001482",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001194",
        "ElispotAssayMeasuringEpitopeSpecificTransformingGrowthFactorBetaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001315",
        "ElisaMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001827",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001828",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001768",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001829",
        "ElispotAssayMeasuringEpitopeSpecificChemokineCCMotifLigand1ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin16ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001837",
        "ElisaMeasuringEpitopeSpecificInterleukin16ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001836",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin16ProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001301",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin16ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002665",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001839",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001838",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin16ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin15ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001283",
        "ElisaMeasuringEpitopeSpecificInterleukin15ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesMeasuringEpitopeSpecificInterleukin15ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001843",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesMeasuringEpitopeSpecificInterleukin15ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002664",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001845",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001846",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin15ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin17ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110162",
        "ElisaMeasuringEpitopeSpecificInterleukin17ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001291",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001296",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110178",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001354",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001772",
        "AssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001773",
        "AssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificIp10ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay, AssayMeasuringEpitopeSpecificIp10ProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001281",
        "ElisaMeasuringEpitopeSpecificIp10ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificIp10ProductionByTCells(
    AssayMeasuringEpitopeSpecificIp10ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001383",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificIp10ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificIp10ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificIp10ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001196",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificIp10ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificIp10ProductionByTCells(
    AssayMeasuringEpitopeSpecificIp10ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001796",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificIp10ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificIp10ProductionByTCells(
    AssayMeasuringEpitopeSpecificIp10ProductionByTCells, EnzymeLinkedImmunospotAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001795",
        "ElispotAssayMeasuringEpitopeSpecificIp10ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001302",
        "ElisaMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001792",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001405",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001545",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001780",
        "ElispotAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1AlphaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001378",
        "ElisaMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001765",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001764",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001370",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001758",
        "ElispotAssayMeasuringEpitopeSpecificChemokineCCMotifLigand4ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin23ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001244",
        "ElisaMeasuringEpitopeSpecificInterleukin23ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001395",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificIntracellularCytokineStainingIcsIl23ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001610",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificIntracellularCytokineStainingIcsIl23ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001812",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001822",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin23ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin18ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110163",
        "ElisaMeasuringEpitopeSpecificInterleukin18ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001815",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001835",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001824",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001817",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin18ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001261",
        "ElisaMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001746",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001747",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001744",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001745",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin1AlphaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterferonBetaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001751",
        "ElisaMeasuringEpitopeSpecificInterferonBetaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001356",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001749",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001748",
        "ElispotAssayMeasuringEpitopeSpecificInterferonBetaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin12ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110160",
        "ElisaMeasuringEpitopeSpecificInterleukin12ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001268",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001284",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001466",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001844",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin12ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001246",
        "ElisaMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001788",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003488",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001368",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001385",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells(
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001272",
        "ElispotAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells(
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001327",
        "AssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells(
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001416",
        "AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells",
    )


class AssayMeasuringEpitopeSpecificTumorNecrosisFactorLigandSuperfamilyMember11ProductionByTCells(
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001607",
        "AssayMeasuringEpitopeSpecificTumorNecrosisFactorLigandSuperfamilyMember11ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin3ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001260",
        "ElisaMeasuringEpitopeSpecificInterleukin3ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001808",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin3ProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001384",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin3ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001807",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001376",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001802",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin3ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110151",
        "ElisaMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001350",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001319",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001379",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class RadioImmunoAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells, RadioImmunoAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001433",
        "RadioImmunoAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110172",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110059",
        "ElispotAssayMeasuringEpitopeSpecificInterferonGammaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110152",
        "ElisaMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001277",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001216",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001300",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class PromoterActivityDetectionByReporterGeneAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells,
    PromoterActivityDetectionByReporterGeneAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001402",
        "PromoterActivityDetectionByReporterGeneAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110173",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110013",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin2ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110161",
        "ElisaMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001743",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001223",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001841",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001842",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin1BetaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin4ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110153",
        "ElisaMeasuringEpitopeSpecificInterleukin4ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001339",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin4ProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001241",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin4ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001326",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110175",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110167",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin4ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin6ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110158",
        "ElisaMeasuringEpitopeSpecificInterleukin6ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001389",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin6ProductionByTCells(
    ReporterCellLineAnalyteDetectionBioassay,
    AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001413",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificInterleukin6ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001360",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001240",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001227",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin6ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001438",
        "ElisaMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells(
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001782",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001781",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells(
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001785",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells(
    AssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001786",
        "ElispotAssayMeasuringEpitopeSpecificMacrophageInflammatoryProtein1GammaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001330",
        "ElisaMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001757",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001754",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001437",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001756",
        "ElispotAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand9ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001344",
        "ElisaMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells(
    AssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001343",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001243",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells(
    AssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001783",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells(
    AssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001784",
        "ElispotAssayMeasuringEpitopeSpecificMonocyteChemotacticProtein1ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001578",
        "ElisaMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001766",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001787",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001770",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001771",
        "ElispotAssayMeasuringEpitopeSpecificVascularEndothelialGrowthFactorProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin7ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001803",
        "ElisaMeasuringEpitopeSpecificInterleukin7ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001676",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001585",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001805",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001804",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin7ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001521",
        "ElisaMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001752",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001397",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells,
    FlowCytometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001750",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells(
    AssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells,
    EnzymeLinkedImmunospotAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001753",
        "ElispotAssayMeasuringEpitopeSpecificGranulocyteColonyStimulatingFactorProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand21ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand21ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001762",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand21ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand19ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand19ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001767",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand19ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand12ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand12ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001759",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand12ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001763",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002061",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand22ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand16ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand16ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001761",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand16ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand13ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCXCMotifLigand13ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001760",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCXCMotifLigand13ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand17ProductionByTCells(
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand17ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002060",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificChemokineCCMotifLigand17ProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificMacrophageMigrationInhibitoryFactorMifProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificMacrophageMigrationInhibitoryFactorMifProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002067",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificMacrophageMigrationInhibitoryFactorMifProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificOncostatinMProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificOncostatinMProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002068",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificOncostatinMProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand20ProductionByTCells(
    AntigenDetectionByCytometricBeadArrayAssay,
    AssayMeasuringEpitopeSpecificChemokineCCMotifLigand20ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002133",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificChemokineCCMotifLigand20ProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterferonAlphaProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterferonAlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002451",
        "ElisaMeasuringEpitopeSpecificInterferonAlphaProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificAmphiregulinProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificAmphiregulinProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003316",
        "ElisaMeasuringEpitopeSpecificAmphiregulinProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificLymphotactinProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificLymphotactinProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003373",
        "ElisaMeasuringEpitopeSpecificLymphotactinProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin25ProductionByTCells(
    EnzymeLinkedImmunosorbentAssay,
    AssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003487",
        "ElisaMeasuringEpitopeSpecificInterleukin25ProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells,
    DetectionOfSpecificNucleicAcidPolymersWithComplementaryProbes,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003485",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells(
    AssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells, FlowCytometryAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003486",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin25ProductionByTCells",
    )


class InVivoAssayMeasuringEpitopeSpecificProliferationOfTCellsResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringEpitopeSpecificProliferationOfTCells,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002668",
        "InVivoAssayMeasuringEpitopeSpecificProliferationOfTCellsResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class BrduAssayMeasuringEpitopeSpecificProliferationOfTCells(
    InVitroAssayMeasuringEpitopeSpecificProliferationOfTCells, BrduIncorporationAssay
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110181",
        "BrduAssayMeasuringEpitopeSpecificProliferationOfTCells",
    )


class _3HThymidineAssayMeasuringEpitopeSpecificProliferationOfTCells(
    TritiatedThymidineIncorporationAssay,
    InVitroAssayMeasuringEpitopeSpecificProliferationOfTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110180",
        "_3HThymidineAssayMeasuringEpitopeSpecificProliferationOfTCells",
    )


class CarboxyfluoresceinSuccinimidylEsterStainingAssayMeasuringEpitopeSpecificProliferationOfTCells(
    InVitroAssayMeasuringEpitopeSpecificProliferationOfTCells,
    CarboxyfluoresceinSuccinimidylEsterStainingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002096",
        "CarboxyfluoresceinSuccinimidylEsterStainingAssayMeasuringEpitopeSpecificProliferationOfTCells",
    )


class AssayMeasuringTheDissociationConstantKdOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringABindingConstantOfATCellEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002097",
        "AssayMeasuringTheDissociationConstantKdOfATCellEpitopeMhcTcrComplex",
    )


class AssayMeasuringTheOnRateKonOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringABindingConstantOfATCellEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002098",
        "AssayMeasuringTheOnRateKonOfATCellEpitopeMhcTcrComplex",
    )


class AssayMeasuringTheOffRateKoffOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringABindingConstantOfATCellEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002099",
        "AssayMeasuringTheOffRateKoffOfATCellEpitopeMhcTcrComplex",
    )


class AssayMeasuringTheAssociationConstantKaOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringABindingConstantOfATCellEpitopeMhcTcrComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002100",
        "AssayMeasuringTheAssociationConstantKaOfATCellEpitopeMhcTcrComplex",
    )


class TCellEpitopeSpecificImmuneIntervention(EpitopeSpecificImmuneIntervention):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001471",
        "TCellEpitopeSpecificImmuneIntervention",
    )


class BCellEpitopeSpecificImmuneIntervention(EpitopeSpecificImmuneIntervention):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001487",
        "BCellEpitopeSpecificImmuneIntervention",
    )


class AntibodyPurificationOfH2LdProteinComplexH2DbProteinComplexAndOrH2DqProteinComplex(
    AntibodyPurificationOfMouseMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003631",
        "AntibodyPurificationOfH2LdProteinComplexH2DbProteinComplexAndOrH2DqProteinComplex",
    )


class AntibodyPurificationOfH2DdProteinComplexAndOrH2KdProteinComplex(
    AntibodyPurificationOfMouseMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003632",
        "AntibodyPurificationOfH2DdProteinComplexAndOrH2KdProteinComplex",
    )


class AntibodyPurificationOfMouseMhcClassIProteinComplexWithH2BHaplotypeAndOrMouseMhcProteinComplexWithH2PHaplotype(
    AntibodyPurificationOfMouseMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003633",
        "AntibodyPurificationOfMouseMhcClassIProteinComplexWithH2BHaplotypeAndOrMouseMhcProteinComplexWithH2PHaplotype",
    )


class AntibodyPurificationOfH2KbProteinComplexH2KsProteinComplexAndOrH2KqProteinComplex(
    AntibodyPurificationOfMouseMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003634",
        "AntibodyPurificationOfH2KbProteinComplexH2KsProteinComplexAndOrH2KqProteinComplex",
    )


class AntibodyPurificationOfHumanMhcClassIProteinComplex(
    AntibodyPurificationOfPigMhcClassIProteinComplexCattleMhcClassIProteinComplexAndOrHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003617",
        "AntibodyPurificationOfHumanMhcClassIProteinComplex",
    )


class AntibodyPurificationOfPigMhcClassIProteinComplex(
    AntibodyPurificationOfPigMhcClassIProteinComplexCattleMhcClassIProteinComplexAndOrHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003624",
        "AntibodyPurificationOfPigMhcClassIProteinComplex",
    )


class AntibodyPurificationOfCattleMhcClassIProteinComplex(
    AntibodyPurificationOfPigMhcClassIProteinComplexCattleMhcClassIProteinComplexAndOrHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003625",
        "AntibodyPurificationOfCattleMhcClassIProteinComplex",
    )


class AntibodyPurificationOfHlaDpProteinComplex(
    AntibodyPurificationOfHumanMhcClassIiProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003639",
        "AntibodyPurificationOfHlaDpProteinComplex",
    )


class AntibodyPurificationOfHlaDrProteinComplex(
    AntibodyPurificationOfHumanMhcClassIiProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003640",
        "AntibodyPurificationOfHlaDrProteinComplex",
    )


class AntibodyPurificationOfHlaProteinComplexWithDq3Serotype(
    AntibodyPurificationOfHumanMhcClassIiProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003641",
        "AntibodyPurificationOfHlaProteinComplexWithDq3Serotype",
    )


class AntibodyPurificationOfMouseMhcClassIiProteinComplex(
    AntibodyPurificationOfMouseMhcClassIiProteinComplexAndOrRatMhcClassIiProteinComplexWithRt1AHaplotype
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003642",
        "AntibodyPurificationOfMouseMhcClassIiProteinComplex",
    )


class AnimalBitingOutdoorArthropodSpecimenCollectionByAspiration(
    AnimalBitingArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002906",
        "AnimalBitingOutdoorArthropodSpecimenCollectionByAspiration",
    )


class ArthropodRestingOutdoorsSpecimenCollectionByAspiration(
    AnimalBitingArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002911",
        "ArthropodRestingOutdoorsSpecimenCollectionByAspiration",
    )


class HumanBitingIndoorArthropodSpecimenCollectionByAspiration(
    HumanBitingArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002915",
        "HumanBitingIndoorArthropodSpecimenCollectionByAspiration",
    )


class HumanBitingOutdoorArthropodSpecimenCollectionByAspiration(
    HumanBitingArthropodSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002916",
        "HumanBitingOutdoorArthropodSpecimenCollectionByAspiration",
    )


class ArgonIonLaser(IonLaser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400010", "ArgonIonLaser")


class HeliumNeonIonLaser(IonLaser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400053", "HeliumNeonIonLaser")


class KryptonIonLaser(IonLaser):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0400062", "KryptonIonLaser")


class MixedArgonKryptonGasLaser(IonLaser):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400074", "MixedArgonKryptonGasLaser"
    )


class HeliumCadmiumIonLaser(MetalVaporLaser):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0400052", "HeliumCadmiumIonLaser"
    )


class NitrogenGenerator(GasGenerator):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000550", "NitrogenGenerator")


class HydrogenGenerator(GasGenerator):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000608", "HydrogenGenerator")


class InLineFilter(ChromatographyDetectorFilter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000538", "InLineFilter")


class SyringeFilter(ChromatographyDetectorFilter):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000543", "SyringeFilter")


class Pancrustacea(Arthropoda):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_197562", "Pancrustacea")


class Tetrapoda(Euteleostomi):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_32523", "Tetrapoda")


class DanioRerio(Euteleostomi):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_7955", "DanioRerio")


class HighResolutionT1WeightedMagneticResonanceImageDataSet(
    T1WeightedGreMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003344",
        "HighResolutionT1WeightedMagneticResonanceImageDataSet",
    )


class BaselineHighResolutionT1WeightedMagneticResonanceImageDataSet(
    T1WeightedGreMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003345",
        "BaselineHighResolutionT1WeightedMagneticResonanceImageDataSet",
    )


class FollowUpHighResolutionT1WeightedMagneticResonanceImageDataSet(
    T1WeightedGreMagneticResonanceImageDataSet
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003346",
        "FollowUpHighResolutionT1WeightedMagneticResonanceImageDataSet",
    )


class FluorescenceDetectionAssayMeasuringEquilibriumAssociationConstantKaToDetermineDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheAssociationConstantKaOfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001524",
        "FluorescenceDetectionAssayMeasuringEquilibriumAssociationConstantKaToDetermineDirectBindingOfACellBoundMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfACellLysateMhcLigandComplex(
    AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001544",
        "RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfACellLysateMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001549",
        "RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001989",
        "RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001537",
        "FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001539",
        "FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfACellBoundMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheHalfLifeOfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001558",
        "RadioactivityDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfACellBoundMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfACellLysateMhcLigandComplex(
    AssayMeasuringTheHalfLifeOfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001565",
        "RadioactivityDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfACellLysateMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheHalfLifeOfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001586",
        "RadioactivityDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheHalfLifeOfAMhcLigandComplex, BindingAssayUsingFluorescenceDetection
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001531",
        "FluorescenceDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheHalfLifeOfAMhcLigandComplex, BindingAssayUsingFluorescenceDetection
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001559",
        "FluorescenceDetectionAssayMeasuringHalfLifeToDetermineDirectBindingOfACellBoundMhcLigandComplex",
    )


class RadioactivityDetectionAssayMeasuringBindingOffRateKoffToDetermineDirectBindingOfACellLysateMhcLigandComplex(
    AssayMeasuringTheOffRateMeasurementKoffOfAMhcLigandComplex,
    BindingAssayUsingRadioactivityDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001567",
        "RadioactivityDetectionAssayMeasuringBindingOffRateKoffToDetermineDirectBindingOfACellLysateMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringBindingOffRateKoffToDetermineDirectBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheOffRateMeasurementKoffOfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001569",
        "FluorescenceDetectionAssayMeasuringBindingOffRateKoffToDetermineDirectBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringBindingOffRateKoffToDetermineDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheOffRateMeasurementKoffOfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001665",
        "FluorescenceDetectionAssayMeasuringBindingOffRateKoffToDetermineDirectBindingOfACellBoundMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringBindingOnRateKonToDetermineDirectBindingOfAPurifiedMhcLigandComplex(
    AssayMeasuringTheMhcLigandBindingOnRateKonOfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001541",
        "FluorescenceDetectionAssayMeasuringBindingOnRateKonToDetermineDirectBindingOfAPurifiedMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringBindingOnRateKonToDetermineDirectBindingOfACellBoundMhcLigandComplex(
    AssayMeasuringTheMhcLigandBindingOnRateKonOfAMhcLigandComplex,
    BindingAssayUsingFluorescenceDetection,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001666",
        "FluorescenceDetectionAssayMeasuringBindingOnRateKonToDetermineDirectBindingOfACellBoundMhcLigandComplex",
    )


class FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineDirectBindingOfAPurifiedMhcLigandComplexApproximatedByEc50(
    FluorescenceDetectionAssayMeasuringHalfMaximalEffectiveConcentrationEc50ToDetermineDirectBindingOfAPurifiedMhcLigandComplex,
    AssayMeasuringTheDissociationConstantKdOfAMhcLigandComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001543",
        "FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineDirectBindingOfAPurifiedMhcLigandComplexApproximatedByEc50",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromInfectiousChallengeBasedOnPathogenBurden(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallenge,
    EpitopeProtectionFromInfectiousChallengeExperimentBasedOnPathogenBurden,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002051",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromInfectiousChallengeBasedOnPathogenBurden",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificSurvivalAfterPathogenChallenge(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallenge,
    EpitopeProtectionFromInfectiousChallengeExperimentBasedOnSurvival,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003468",
        "InVivoAssayMeasuringBCellEpitopeSpecificSurvivalAfterPathogenChallenge",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionAfterTumorBurdenChallenge(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallenge,
    EpitopeProtectionFromTumorChallengeExperimentBasedOnBurden,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002052",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionAfterTumorBurdenChallenge",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificSurvivalAfterTumorChallenge(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallenge,
    EpitopeProtectionFromTumorChallengeExperimentBasedOnSurvival,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003469",
        "InVivoAssayMeasuringBCellEpitopeSpecificSurvivalAfterTumorChallenge",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionBasedOnSurvival(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallenge,
    EpitopeProtectionExperimentBasedOnSurvival,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001696",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionBasedOnSurvival",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
    EpitopeProtectionFromInfectiousChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003475",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
    EpitopeProtectionFromTumorChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003477",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003479",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells",
    )


class ElisaMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
    EnzymeLinkedImmunosorbentAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001728",
        "ElisaMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class ChromatographyAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
    AnalyticalChromatography,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001996",
        "ChromatographyAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class RiaMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
    RadioImmunoAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001727",
        "RiaMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class SurfacePlasmonResonanceAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
    SurfacePlasmonResonanceBindingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001731",
        "SurfacePlasmonResonanceAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class QuenchingAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AntibodyBindingDetectionByFluorescenceQuenching,
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001729",
        "QuenchingAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class CalorimetryAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
    CalorimetricBindingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001734",
        "CalorimetryAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class BioLayerInterferometryAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
    BioLayerInterferometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002105",
        "BioLayerInterferometryAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class QuartzCrystalMicrobalanceAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex,
    QuartzCrystalMicrobalanceAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003602",
        "QuartzCrystalMicrobalanceAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class AntigenInhibitionAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplexApproximatedByIc50(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001638",
        "AntigenInhibitionAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplexApproximatedByIc50",
    )


class NmrAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002054",
        "NmrAssayMeasuringTheDissociationConstantKdOfABCellEpitopeAntibodyComplex",
    )


class SurfacePlasmonResonanceAssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex,
    SurfacePlasmonResonanceBindingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001741",
        "SurfacePlasmonResonanceAssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex",
    )


class QuenchingAssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex(
    AntibodyBindingDetectionByFluorescenceQuenching,
    AssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001742",
        "QuenchingAssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex",
    )


class BioLayerInterferometryAssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex,
    BioLayerInterferometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002102",
        "BioLayerInterferometryAssayMeasuringTheOnRateKonOfABCellEpitopeAntibodyComplex",
    )


class ElisaMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex,
    EnzymeLinkedImmunosorbentAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001735",
        "ElisaMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex",
    )


class ChromatographyAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex,
    AnalyticalChromatography,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001995",
        "ChromatographyAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex",
    )


class RiaMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex,
    RadioImmunoAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001736",
        "RiaMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex",
    )


class SurfacePlasmonResonanceAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex,
    SurfacePlasmonResonanceBindingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001730",
        "SurfacePlasmonResonanceAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex",
    )


class QuenchingAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex(
    AntibodyBindingDetectionByFluorescenceQuenching,
    AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001732",
        "QuenchingAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex",
    )


class CalorimetryAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex,
    CalorimetricBindingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001733",
        "CalorimetryAssayMeasuringTheAssociationConstantKaOfABCellEpitopeAntibodyComplex",
    )


class SurfacePlasmonResonanceAssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex,
    SurfacePlasmonResonanceBindingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001739",
        "SurfacePlasmonResonanceAssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex",
    )


class QuenchingAssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex(
    AntibodyBindingDetectionByFluorescenceQuenching,
    AssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001740",
        "QuenchingAssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex",
    )


class BioLayerInterferometryAssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex(
    AssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex,
    BioLayerInterferometryAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002103",
        "BioLayerInterferometryAssayMeasuringTheOffRateKoffOfABCellEpitopeAntibodyComplex",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromInfectiousChallengeBasedOnPathogenBurden(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallenge,
    EpitopeProtectionFromInfectiousChallengeExperimentBasedOnPathogenBurden,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001475",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromInfectiousChallengeBasedOnPathogenBurden",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificSurvivalAfterPathogenChallenge(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallenge,
    EpitopeProtectionFromInfectiousChallengeExperimentBasedOnSurvival,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003464",
        "InVivoAssayMeasuringTCellEpitopeSpecificSurvivalAfterPathogenChallenge",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionAfterTumorBurdenChallenge(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallenge,
    EpitopeProtectionFromTumorChallengeExperimentBasedOnBurden,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001473",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionAfterTumorBurdenChallenge",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificSurvivalAfterTumorChallenge(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallenge,
    EpitopeProtectionFromTumorChallengeExperimentBasedOnSurvival,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003463",
        "InVivoAssayMeasuringTCellEpitopeSpecificSurvivalAfterTumorChallenge",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionBasedOnSurvival(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallenge,
    EpitopeProtectionExperimentBasedOnSurvival,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001492",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionBasedOnSurvival",
    )


class AssayMeasuringEpitopeSpecificHelperTCellEnhancementOfABCellMediatedImmuneResponseResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringEpitopeSpecificHelperTCellEnhancementOfABCellMediatedImmuneResponse,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002669",
        "AssayMeasuringEpitopeSpecificHelperTCellEnhancementOfABCellMediatedImmuneResponseResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class AssayMeasuringEpitopeSpecificHelperTCellEnhancementOfATCellMediatedImmuneResponseResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringEpitopeSpecificHelperTCellEnhancementOfATCellMediatedImmuneResponse,
    InVivoAssayMeasuringATCellEpitopeSpecificResponseAfterAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002670",
        "AssayMeasuringEpitopeSpecificHelperTCellEnhancementOfATCellMediatedImmuneResponseResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells,
    EpitopeProtectionFromInfectiousChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003470",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells,
    EpitopeProtectionFromTumorChallengeExperiment,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003472",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003474",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin17FProductionByTCells(
    ElisaMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001831",
        "ElisaMeasuringEpitopeSpecificInterleukin17FProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells(
    DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001832",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells(
    CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001523",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells(
    IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001562",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells(
    ElispotAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001830",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin17FProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificInterleukin17AProductionByTCells(
    ElisaMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001675",
        "ElisaMeasuringEpitopeSpecificInterleukin17AProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells(
    DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001840",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells(
    CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001512",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells(
    IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001589",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells(
    ElispotAssayMeasuringEpitopeSpecificInterleukin17ProductionByTCells,
    AssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001833",
        "ElispotAssayMeasuringEpitopeSpecificInterleukin17AProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificLymphotoxinAProductionByTCells(
    ElisaMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001288",
        "ElisaMeasuringEpitopeSpecificLymphotoxinAProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells(
    DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001794",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells(
    CytometricBeadArrayAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001793",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells(
    IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001453",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells(
    ElispotAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001791",
        "ElispotAssayMeasuringEpitopeSpecificLymphotoxinAProductionByTCells",
    )


class ElisaMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells(
    ElisaMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110155",
        "ElisaMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells",
    )


class DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells(
    DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001242",
        "DetectionOfSpecificNucleicAcidsWithComplementaryProbesAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells",
    )


class CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells(
    CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001452",
        "CellCultureAnalyteDetectionBioassayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells",
    )


class CytometricBeadArrayAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells(
    CytometricBeadArrayAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001353",
        "CytometricBeadArrayAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells(
    IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110174",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells",
    )


class ElispotAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells(
    ElispotAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110168",
        "ElispotAssayMeasuringEpitopeSpecificTumorNecrosisFactorAlphaProductionByTCells",
    )


class IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorLigandSuperfamilyMember11ProductionByTCells(
    IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorSuperfamilyCytokineProductionByTCells,
    AssayMeasuringEpitopeSpecificTumorNecrosisFactorLigandSuperfamilyMember11ProductionByTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001552",
        "IntracellularCytokineStainingAssayMeasuringEpitopeSpecificTumorNecrosisFactorLigandSuperfamilyMember11ProductionByTCells",
    )


class PlasmonResonanceAssayMeasuringTheDissociationConstantKdOfATCellEpitopeMhcTcrComplex(
    AssayMeasuringTheDissociationConstantKdOfATCellEpitopeMhcTcrComplex,
    SurfacePlasmonResonanceBindingAssay,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001229",
        "PlasmonResonanceAssayMeasuringTheDissociationConstantKdOfATCellEpitopeMhcTcrComplex",
    )


class AntibodyPurificationOfH2DdProteinComplex(
    AntibodyPurificationOfH2DdProteinComplexAndOrH2KdProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003628",
        "AntibodyPurificationOfH2DdProteinComplex",
    )


class AntibodyPurificationOfH2KdProteinComplex(
    AntibodyPurificationOfH2DdProteinComplexAndOrH2KdProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003630",
        "AntibodyPurificationOfH2KdProteinComplex",
    )


class AntibodyPurificationOfH2DbProteinComplex(
    AntibodyPurificationOfH2LdProteinComplexH2DbProteinComplexAndOrH2DqProteinComplex,
    AntibodyPurificationOfMouseMhcClassIProteinComplexWithH2BHaplotypeAndOrMouseMhcProteinComplexWithH2PHaplotype,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003629",
        "AntibodyPurificationOfH2DbProteinComplex",
    )


class AntibodyPurificationOfHlaProteinComplexWithA24Serotype(
    AntibodyPurificationOfHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003619",
        "AntibodyPurificationOfHlaProteinComplexWithA24Serotype",
    )


class AntibodyPurificationOfHlaProteinComplexWithA2SerotypeAndOrHlaProteinComplexWithA28Serotype(
    AntibodyPurificationOfHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003620",
        "AntibodyPurificationOfHlaProteinComplexWithA2SerotypeAndOrHlaProteinComplexWithA28Serotype",
    )


class AntibodyPurificationOfHlaProteinComplexWithA29Serotype(
    AntibodyPurificationOfHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003621",
        "AntibodyPurificationOfHlaProteinComplexWithA29Serotype",
    )


class AntibodyPurificationOfHlaProteinComplexWithB27Serotype(
    AntibodyPurificationOfHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003622",
        "AntibodyPurificationOfHlaProteinComplexWithB27Serotype",
    )


class AntibodyPurificationOfHlaCProteinComplex(
    AntibodyPurificationOfHumanMhcClassIProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003623",
        "AntibodyPurificationOfHlaCProteinComplex",
    )


class AntibodyPurificationOfH2IaProteinComplex(
    AntibodyPurificationOfMouseMhcClassIiProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003643",
        "AntibodyPurificationOfH2IaProteinComplex",
    )


class ArthropodRestingOutdoorsOnArtificialSupportSpecimenCollectionByAspiration(
    ArthropodRestingOutdoorsSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002909",
        "ArthropodRestingOutdoorsOnArtificialSupportSpecimenCollectionByAspiration",
    )


class ArthropodRestingOutdoorsOnNaturalSupportSpecimenCollectionByAspiration(
    ArthropodRestingOutdoorsSpecimenCollectionByAspiration
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002910",
        "ArthropodRestingOutdoorsOnNaturalSupportSpecimenCollectionByAspiration",
    )


class Daphnia(Pancrustacea):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_6668", "Daphnia")


class Diptera(Pancrustacea):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_7147", "Diptera")


class Amniota(Tetrapoda):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_32524", "Amniota")


class XenopusGenus(Tetrapoda):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_8353", "XenopusGenus")


class RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplexApproximatedByIc50(
    RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex,
    RadioactivityDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001564",
        "RadioactivityDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplexApproximatedByIc50",
    )


class FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplexApproximatedByIc50(
    FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex,
    FluorescenceDetectionAssayMeasuringHalfMaximalInhibitoryConcentrationIc50ToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplex,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001667",
        "FluorescenceDetectionAssayMeasuringEquilibriumDissociationConstantKdToDetermineCompetitiveBindingOfAPurifiedMhcLigandComplexApproximatedByIc50",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnPathogenBurden(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromInfectiousChallengeBasedOnPathogenBurden,
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002640",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnPathogenBurden",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificPathogenProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnSurvival(
    InVivoAssayMeasuringBCellEpitopeSpecificSurvivalAfterPathogenChallenge,
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003476",
        "InVivoAssayMeasuringBCellEpitopeSpecificPathogenProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnSurvival",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnTumorBurden(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionAfterTumorBurdenChallenge,
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002644",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnTumorBurden",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnSurvival(
    InVivoAssayMeasuringBCellEpitopeSpecificSurvivalAfterTumorChallenge,
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003478",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnSurvival",
    )


class InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnSurvival(
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionBasedOnSurvival,
    InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002642",
        "InVivoAssayMeasuringBCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificAntibodiesOrBCellsBasedOnSurvival",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnPathogenBurden(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromInfectiousChallengeBasedOnPathogenBurden,
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002639",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnPathogenBurden",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificPathogenProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnSurvival(
    InVivoAssayMeasuringTCellEpitopeSpecificSurvivalAfterPathogenChallenge,
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromPathogenChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003471",
        "InVivoAssayMeasuringTCellEpitopeSpecificPathogenProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnSurvival",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnTumorBurden(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionAfterTumorBurdenChallenge,
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002643",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnTumorBurden",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnSurvival(
    InVivoAssayMeasuringTCellEpitopeSpecificSurvivalAfterTumorChallenge,
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003473",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromTumorChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnSurvival",
    )


class InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnSurvival(
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionBasedOnSurvival,
    InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCells,
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0002641",
        "InVivoAssayMeasuringTCellEpitopeSpecificProtectionFromOtherChallengeResultingFromTheAdoptiveTransferOfEpitopeSpecificTCellsBasedOnSurvival",
    )


class AntibodyPurificationOfHlaProteinComplexWithA2Serotype(
    AntibodyPurificationOfHlaProteinComplexWithA2SerotypeAndOrHlaProteinComplexWithA28Serotype
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003618",
        "AntibodyPurificationOfHlaProteinComplexWithA2Serotype",
    )


class AntibodyPurificationOfH2Iag7ProteinComplex(
    AntibodyPurificationOfH2IaProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003644",
        "AntibodyPurificationOfH2Iag7ProteinComplex",
    )


class AntibodyPurificationOfH2IadProteinComplex(
    AntibodyPurificationOfH2IaProteinComplex
):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003645",
        "AntibodyPurificationOfH2IadProteinComplex",
    )


class Culicidae(Diptera):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_7157", "Culicidae")


class DrosophilaMelanogaster(Diptera):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_7227", "DrosophilaMelanogaster"
    )


class Mammalia(Amniota):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_40674", "Mammalia")


class GallusGallus(Amniota):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_9031", "GallusGallus")


class Euarchontoglires(Mammalia):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/NCBITaxon_314146", "Euarchontoglires"
    )


class HomoSapiens(Euarchontoglires):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_9606", "HomoSapiens")


class Rodentia(Euarchontoglires):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_9989", "Rodentia")


class BioinformaticsResourceCenterContactPerson(HomoSapiens):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001883",
        "BioinformaticsResourceCenterContactPerson",
    )


class SequencingFacilityContactPerson(HomoSapiens):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001888", "SequencingFacilityContactPerson"
    )


class SpecimenProviderPrincipalInvestigator(HomoSapiens):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001889",
        "SpecimenProviderPrincipalInvestigator",
    )


class SpecimenCollector(HomoSapiens):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001895", "SpecimenCollector")


class Murinae(Rodentia):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_39107", "Murinae")


class MusMusculus(Murinae):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_10090", "MusMusculus")


class RattusNorvegicus(Murinae):
    term = RdfTerm("http://purl.obolibrary.org/obo/NCBITaxon_10116", "RattusNorvegicus")


class defaultLanguage(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://protege.stanford.edu/plugins/owl/protege#defaultLanguage",
        "defaultLanguage",
    )


class bfoOwlSpecificationLabel(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000179", "bfoOwlSpecificationLabel"
    )


class bfoClifSpecificationLabel(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/BFO_0000180", "bfoClifSpecificationLabel"
    )


class editorPreferredLabel(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000111", "editorPreferredLabel")


class exampleOfUsage(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000112", "exampleOfUsage")


class inBranch(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000113", "inBranch")


class hasCurationStatus(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000114", "hasCurationStatus")


class definition(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000115", "definition")


class editorNote(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000116", "editorNote")


class termEditor(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000117", "termEditor")


class alternativeLabel(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000118", "alternativeLabel")


class definitionSource(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000119", "definitionSource")


class hasObsolescenceReason(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000231", "hasObsolescenceReason"
    )


class curatorNote(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000232", "curatorNote")


class termTrackerItem(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000233", "termTrackerItem")


class ontologyTermRequester(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000234", "ontologyTermRequester"
    )


class isDenotatorType(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000411", "isDenotatorType")


class importedFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000412", "importedFrom")


class expandExpressionTo(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000424", "expandExpressionTo")


class expandAssertionTo(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000425", "expandAssertionTo")


class firstOrderLogicExpression(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000426", "firstOrderLogicExpression"
    )


class antisymmetricProperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000427", "antisymmetricProperty"
    )


class oboFoundryUniqueLabel(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000589", "oboFoundryUniqueLabel"
    )


class hasIdDigitCount(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000596", "hasIdDigitCount")


class hasIdRangeAllocatedTo(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000597", "hasIdRangeAllocatedTo"
    )


class hasIdPolicyFor(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000598", "hasIdPolicyFor")


class hasIdPrefix(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000599", "hasIdPrefix")


class elucidation(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000600", "elucidation")


class hasAssociatedAxiomNl(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000601", "hasAssociatedAxiomNl")


class hasAssociatedAxiomFol(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000602", "hasAssociatedAxiomFol"
    )


class isAllocatedIdRange(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000603", "isAllocatedIdRange")


class hasOntologyRootTerm(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000700", "hasOntologyRootTerm")


class mayBeIdenticalTo(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0006011", "mayBeIdenticalTo")


class scheduledForObsoletionOnOrAfter(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0006012", "scheduledForObsoletionOnOrAfter"
    )


class hasAxiomLabel(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0010000", "hasAxiomLabel")


class termReplacedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0100001", "termReplacedBy")


class isaAlternativeTerm(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001847", "isaAlternativeTerm")


class niaidGscidBrcAlternativeTerm(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001886", "niaidGscidBrcAlternativeTerm"
    )


class iedbAlternativeTerm(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_9991118", "iedbAlternativeTerm")


class fgedAlternativeTerm(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_9991119", "fgedAlternativeTerm")


class logicalCharacteristicOfObjectProperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OMO_0001001",
        "logicalCharacteristicOfObjectProperty",
    )


class definedByConstruct(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0002000", "definedByConstruct")


class abbreviation(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003000", "abbreviation")


class ambiguousSynonym(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003001", "ambiguousSynonym")


class dubiousSynonym(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003002", "dubiousSynonym")


class laypersonSynonym(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003003", "laypersonSynonym")


class pluralForm(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003004", "pluralForm")


class ukSpellingSynonym(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003005", "ukSpellingSynonym")


class misspelling(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003006", "misspelling")


class misnomer(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003007", "misnomer")


class previousName(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003008", "previousName")


class legalName(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003009", "legalName")


class internationalNonproprietaryName(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OMO_0003010", "internationalNonproprietaryName"
    )


class latinTerm(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003011", "latinTerm")


class acronym(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0003012", "acronym")


class hasSymbol(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OMO_0004000", "hasSymbol")


class RO_0001900(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0001900", "RO_0001900")


class contributor(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/contributor", "contributor")


class coverage(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/coverage", "coverage")


class creator(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/creator", "creator")


class date(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/date", "date")


class description(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/description", "description")


class format(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/format", "format")


class resourceIdentifier(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/identifier", "resourceIdentifier")


class language(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/language", "language")


class member(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/member", "member")


class publisher(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/publisher", "publisher")


class relation(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/relation", "relation")


class rightsManagement(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/rights", "rightsManagement")


class source(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/source", "source")


class subjectAndKeywords(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/subject", "subjectAndKeywords")


class title(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/title", "title")


class resourceType(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/elements/1.1/type", "resourceType")


class contributor(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/contributor", "contributor")


class created(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/created", "created")


class license(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/license", "license")


class source(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/source", "source")


class title(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/title", "title")


class SynonymTypeProperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#SynonymTypeProperty",
        "SynonymTypeProperty",
    )


class created_by(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#created_by", "created_by"
    )


class creation_date(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#creation_date", "creation_date"
    )


class hasBroadSynonym(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym",
        "hasBroadSynonym",
    )


class hasCrossReference(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#hasDbXref", "hasCrossReference"
    )


class hasExactSynonym(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#hasExactSynonym",
        "hasExactSynonym",
    )


class hasNarrowSynonym(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#hasNarrowSynonym",
        "hasNarrowSynonym",
    )


class hasRelatedSynonym(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym",
        "hasRelatedSynonym",
    )


class comment(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#comment", "comment")


class isDefinedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#isDefinedBy", "isDefinedBy")


class label(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#label", "label")


class seeAlso(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/2000/01/rdf-schema#seeAlso", "seeAlso")


class homepage(RdfProperty[RdfType]):
    term = RdfTerm("http://xmlns.com/foaf/0.1/homepage", "homepage")


class hasMeasurementValue(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000004", "hasMeasurementValue")


class hasFeatureValue(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000292", "hasFeatureValue")


class hasSpecifiedNumericValue(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001937", "hasSpecifiedNumericValue"
    )


class hasSpecifiedValue(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002135", "hasSpecifiedValue")


class hasRepresentation(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0002815", "hasRepresentation")


class hasMeasurementUnitLabel(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000039", "hasMeasurementUnitLabel"
    )


class hasCoordinateUnitLabel(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000407", "hasCoordinateUnitLabel"
    )


class characteristicOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000052", "characteristicOf")


class partOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000050", "partOf")


class hasPart(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000051", "hasPart")


class realizedIn(RdfProperty[obi.Process]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000054", "realizedIn")


class realizes(RdfProperty[obi.RealizableEntity]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000055", "realizes")


class precededBy(RdfProperty[obi.Occurrent]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000062", "precededBy")


class precedes(RdfProperty[obi.Occurrent]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000063", "precedes")


class occursIn(RdfProperty[obi.IndependentContinuant]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000066", "occursIn")


class containsProcess(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/BFO_0000067", "containsProcess")


class isAbout(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000136", "isAbout")


class denotes(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000219", "denotes")


class isQualityMeasurementOf(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/IAO_0000221", "isQualityMeasurementOf"
    )


class denotedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000235", "denotedBy")


class isDurationOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/IAO_0000413", "isDurationOf")


class providesServiceConsumerWith(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000107", "providesServiceConsumerWith"
    )


class isSupportedByData(RdfProperty[obi.DataItem]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000124", "isSupportedByData")


class hasSpecifiedInput(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000293", "hasSpecifiedInput")


class obsoleteIsConcretizationOf(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000294", "obsoleteIsConcretizationOf"
    )


class isSpecifiedInputOf(RdfProperty[obi.PlannedProcess]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000295", "isSpecifiedInputOf")


class obsoleteIsConcretizedAs(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000297", "obsoleteIsConcretizedAs"
    )


class obsoleteHasQuality(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000298", "obsoleteHasQuality")


class hasSpecifiedOutput(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000299", "hasSpecifiedOutput")


class obsoleteIsRealizedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000300", "obsoleteIsRealizedBy")


class obsoletedHasSpecifiedOutputInformation(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000301",
        "obsoletedHasSpecifiedOutputInformation",
    )


class isManufacturedBy(RdfProperty[obi.Manufacturer]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000304", "isManufacturedBy")


class obsoleteHasFunction(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000306", "obsoleteHasFunction")


class obsoletedIsReagentIn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000307", "obsoletedIsReagentIn")


class obsoleteRealizes(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000308", "obsoleteRealizes")


class obsoletedUtilizesReagent(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000309", "obsoletedUtilizesReagent"
    )


class obsoletedIsDeviceFor(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000311", "obsoletedIsDeviceFor")


class isSpecifiedOutputOf(RdfProperty[obi.PlannedProcess]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000312", "isSpecifiedOutputOf")


class obsoletedUtilizesDevice(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000313", "obsoletedUtilizesDevice"
    )


class isProxyFor(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000314", "isProxyFor")


class obsoletedHasSpecifiedInputInformation(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000315",
        "obsoletedHasSpecifiedInputInformation",
    )


class obsoleteHasRole(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000316", "obsoleteHasRole")


class obsoleteResultsFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000365", "obsoleteResultsFrom")


class achievesPlannedObjective(RdfProperty[obi.ObjectiveSpecification]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000417", "achievesPlannedObjective"
    )


class obsoletedIsSpecifiedInformationOutputOf(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000459",
        "obsoletedIsSpecifiedInformationOutputOf",
    )


class hasGrain(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000643", "hasGrain")


class obsoletedIsSpecifiedInformationIntputOf(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000644",
        "obsoletedIsSpecifiedInformationIntputOf",
    )


class isGrainOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000645", "isGrainOf")


class provisions(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000646", "provisions")


class hasSupplier(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000647", "hasSupplier")


class objectiveAchievedBy(RdfProperty[obi.PlannedProcess]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000833", "objectiveAchievedBy")


class isMemberOfOrganization(RdfProperty[obi.Organization]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0000846", "isMemberOfOrganization"
    )


class hasCategoryLabel(RdfProperty[obi.CategoricalLabel]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0000999", "hasCategoryLabel")


class hasDispositionToBind(RdfProperty[obi.MaterialEntity]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001637", "hasDispositionToBind")


class hasOrganizationMember(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001688", "hasOrganizationMember"
    )


class specifiesValueOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001927", "specifiesValueOf")


class hasValueSpecification(RdfProperty[obi.ValueSpecification]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0001938", "hasValueSpecification"
    )


class hasPerformer(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0001950", "hasPerformer")


class hasAssayTargetContext(RdfProperty[obi.MaterialEntity]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_0003385", "hasAssayTargetContext"
    )


class hasStudyDesign(RdfProperty[obi.StudyDesign]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003703", "hasStudyDesign")


class isStudyDesignOf(RdfProperty[obi.Investigation]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_0003704", "isStudyDesignOf")


class processIsResultOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110060", "processIsResultOf")


class obsoleteIsDescribedBy(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://purl.obolibrary.org/obo/OBI_1110112", "obsoleteIsDescribedBy"
    )


class boundTo(RdfProperty[obi.MaterialEntity]):
    term = RdfTerm("http://purl.obolibrary.org/obo/OBI_1110119", "boundTo")


class hasCharacteristic(RdfProperty[obi.SpecificallyDependentContinuant]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000053", "hasCharacteristic")


class participatesIn(RdfProperty[obi.Occurrent]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000056", "participatesIn")


class hasParticipant(RdfProperty[obi.Continuant]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000057", "hasParticipant")


class isConcretizedAs(RdfProperty[obi.SpecificallyDependentContinuant]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000058", "isConcretizedAs")


class concretizes(RdfProperty[obi.GenericallyDependentContinuant]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000059", "concretizes")


class functionOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000079", "functionOf")


class qualityOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000080", "qualityOf")


class roleOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000081", "roleOf")


class hasFunction(RdfProperty[obi.Function]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000085", "hasFunction")


class hasQuality(RdfProperty[obi.Quality]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000086", "hasQuality")


class hasRole(RdfProperty[obi.Role]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000087", "hasRole")


class hasDisposition(RdfProperty[obi.Disposition]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000091", "hasDisposition")


class dispositionOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0000092", "dispositionOf")


class derivesFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0001000", "derivesFrom")


class derivesInto(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0001001", "derivesInto")


class locationOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0001015", "locationOf")


class locatedIn(RdfProperty[obi.IndependentContinuant]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0001025", "locatedIn")


class _2DBoundaryOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002000", "_2DBoundaryOf")


class has2DBoundary(RdfProperty[obi.ImmaterialEntity]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002002", "has2DBoundary")


class immediatelyPrecededBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002087", "immediatelyPrecededBy")


class immediatelyPrecedes(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002090", "immediatelyPrecedes")


class hasComponent(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002180", "hasComponent")


class capableOf(RdfProperty[obi.Process]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002215", "capableOf")


class surroundedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002219", "surroundedBy")


class adjacentTo(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002220", "adjacentTo")


class temporalRelation(RdfProperty[obi.Occurrent]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002222", "temporalRelation")


class starts(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002223", "starts")


class memberOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002350", "memberOf")


class hasMember(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0002351", "hasMember")


class deprecatedInheresIn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0004096", "deprecatedInheresIn")


class deprecatedBearerOf(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.obolibrary.org/obo/RO_0004097", "deprecatedBearerOf")


class ObsoleteProperty(RdfProperty[RdfType]):
    term = RdfTerm(
        "http://www.geneontology.org/formats/oboInOwl#ObsoleteProperty",
        "ObsoleteProperty",
    )
