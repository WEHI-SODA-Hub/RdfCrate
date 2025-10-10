from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfType
from . import reproduce


class ExperimentalData(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#ExperimentalData", "ExperimentalData")


class Algorithm(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Algorithm", "Algorithm")


class Aliquotsreceiver(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#AliquotsReceiver", "Aliquotsreceiver")


class Setting(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Setting", "Setting")


class Antisensesequence(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#AntisenseSequence", "Antisensesequence"
    )


class Argument(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Argument", "Argument")


class Author(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Author", "Author")


class ExperimentMaterial(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ExperimentMaterial", "ExperimentMaterial"
    )


class Bio_Formats(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#BioFormats", "Bio_Formats")


class Casnumber(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#CASNumber", "Casnumber")


class CausalEffect(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#CausalEffect", "CausalEffect")


class ComputationalStep(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ComputationalStep", "ComputationalStep"
    )


class NotebookCellExecution(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#CellExecution", "NotebookCellExecution"
    )


class Channel(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Channel", "Channel")


class Method(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Method", "Method")


class ExperimentSetup(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#ExperimentSetup", "ExperimentSetup")


class Contactperson(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#ContactPerson", "Contactperson")


class Controlcomments(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#ControlComments", "Controlcomments")


class CopyrightHolder(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#CopyrightHolder", "CopyrightHolder")


class Datatype(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#DataType", "Datatype")


class Dataset(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Dataset", "Dataset")


class Description(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Description", "Description")


class Instrument(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Instrument", "Instrument")


class Developmentalstage(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#DevelopmentalStage", "Developmentalstage"
    )


class Distributor(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Distributor", "Distributor")


class Event(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Event", "Event")


class Experiment(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Experiment", "Experiment")


class ExperimentEnvironmentSetup(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ExperimentEnvironmentSetup",
        "ExperimentEnvironmentSetup",
    )


class ExperimentMaterialPreparation(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ExperimentMaterialPreparation",
        "ExperimentMaterialPreparation",
    )


class Experimenter(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Experimenter", "Experimenter")


class ExperimenterGroupConfig(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ExperimenterGroupConfig",
        "ExperimenterGroupConfig",
    )


class FinalStep(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#FinalStep", "FinalStep")


class Function(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Function", "Function")


class FunctionActivation(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#FunctionActivation", "FunctionActivation"
    )


class FundingAgency(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#FundingAgency", "FundingAgency")


class Geneidentifier(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#GeneIdentifier", "Geneidentifier")


class Genesymbol(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#GeneSymbol", "Genesymbol")


class HighContentScreening(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#HighContentScreening", "HighContentScreening"
    )


class IntermediateStep(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#IntermediateStep", "IntermediateStep")


class Job(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Job", "Job")


class License(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#License", "License")


class LightPath(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#LightPath", "LightPath")


class LogicalChannel(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#LogicalChannel", "LogicalChannel")


class Manufacturer(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Manufacturer", "Manufacturer")


class Module(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Module", "Module")


class MolecularFormula(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#MolecularFormula", "MolecularFormula")


class MolecularWeight(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#MolecularWeight", "MolecularWeight")


class Non_ComputationalStep(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#Non-computationalStep", "Non_ComputationalStep"
    )


class OriginalCreator(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#OriginalCreator", "OriginalCreator")


class Output(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Output", "Output")


class Owner(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Owner", "Owner")


class Phenotype(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Phenotype", "Phenotype")


class Precondition(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Precondition", "Precondition")


class PrincipalInvestigator(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#PrincipalInvestigator", "PrincipalInvestigator"
    )


class Protocol(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Protocol", "Protocol")


class Purity(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Purity", "Purity")


class Qualitycontrol(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#QualityControl", "Qualitycontrol")


class Rating(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Rating", "Rating")


class ResearchGroup(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#ResearchGroup", "ResearchGroup")


class ResearchProject(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#ResearchProject", "ResearchProject")


class Sensesequence(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#SenseSequence", "Sensesequence")


class Session(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Session", "Session")


class Solvent(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Solvent", "Solvent")


class Source(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Source", "Source")


class StandardOperatingProcedure(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#StandardOperatingProcedure",
        "StandardOperatingProcedure",
    )


class StructuralFormula(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#StructuralFormula", "StructuralFormula"
    )


class Study(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Study", "Study")


class Subexperiment(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#SubExperiment", "Subexperiment")


class Trial(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#Trial", "Trial")


class Ph(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#pH", "Ph")


class Sirnaidentifier(RdfClass):
    term = RdfTerm("https://w3id.org/reproduceme#siRNAIdentifier", "Sirnaidentifier")


class Sirnapoolidentifier(RdfClass):
    term = RdfTerm(
        "https://w3id.org/reproduceme#siRNAPoolIdentifier", "Sirnapoolidentifier"
    )


class AdditionalInformation(ExperimentalData):
    term = RdfTerm(
        "https://w3id.org/reproduceme#AdditionalInformation", "AdditionalInformation"
    )


class Annotation(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Annotation", "Annotation")


class Assay(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Assay", "Assay")


class File(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#File", "File")


class Image(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Image", "Image")


class InputData(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#InputData", "InputData")


class Library(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Library", "Library")


class Log(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Log", "Log")


class MaterialTransferAgreement(ExperimentalData):
    term = RdfTerm(
        "https://w3id.org/reproduceme#MaterialTransferAgreement",
        "MaterialTransferAgreement",
    )


class Measurement(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Measurement", "Measurement")


class Metadata(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Metadata", "Metadata")


class ModifiedVersion(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#ModifiedVersion", "ModifiedVersion")


class Note(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Note", "Note")


class Notebok(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Notebook", "Notebok")


class Parameter(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Parameter", "Parameter")


class ProcessedData(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#ProcessedData", "ProcessedData")


class ProspectiveProvenance(ExperimentalData):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ProspectiveProvenance", "ProspectiveProvenance"
    )


class Publication(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Publication", "Publication")


class RawData(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#RawData", "RawData")


class Reagent(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Reagent", "Reagent")


class Result(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Result", "Result")


class RetrospectiveProvenance(ExperimentalData):
    term = RdfTerm(
        "https://w3id.org/reproduceme#RetrospectiveProvenance",
        "RetrospectiveProvenance",
    )


class Script(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Script", "Script")


class Tag(ExperimentalData):
    term = RdfTerm("https://w3id.org/reproduceme#Tag", "Tag")


class Amplificationlevel(Setting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#AmplificationLevel", "Amplificationlevel"
    )


class Channelsetting(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#ChannelSetting", "Channelsetting")


class ComputationalTool(Setting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ComputationalTool", "ComputationalTool"
    )


class Configuration(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Configuration", "Configuration")


class Context(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Context", "Context")


class EnvironmentSetupSetting(Setting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#EnvironmentSetupSetting",
        "EnvironmentSetupSetting",
    )


class ExperimentalCondition(Setting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ExperimentalCondition", "ExperimentalCondition"
    )


class ImageSetting(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#ImageSetting", "ImageSetting")


class InstrumentSetting(Setting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#InstrumentSetting", "InstrumentSetting"
    )


class Kernel(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Kernel", "Kernel")


class Modification(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Modification", "Modification")


class OperatingSystem(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#OperatingSystem", "OperatingSystem")


class Package(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Package", "Package")


class ProgrammingLanguage(Setting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ProgrammingLanguage", "ProgrammingLanguage"
    )


class SessionSetting(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#SessionSetting", "SessionSetting")


class Size(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Size", "Size")


class Software(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Software", "Software")


class Unit(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Unit", "Unit")


class Version(Setting):
    term = RdfTerm("https://w3id.org/reproduceme#Version", "Version")


class BacterialResistance(ExperimentMaterial):
    term = RdfTerm(
        "https://w3id.org/reproduceme#BacterialResistance", "BacterialResistance"
    )


class BacterialStrain(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#BacterialStrain", "BacterialStrain")


class CellLine(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#CellLine", "CellLine")


class Chemical(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Chemical", "Chemical")


class Dna(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#DNA", "Dna")


class EukaryoticCellResistance(ExperimentMaterial):
    term = RdfTerm(
        "https://w3id.org/reproduceme#EukaryoticCellResistance",
        "EukaryoticCellResistance",
    )


class ExpressionSystem(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#ExpressionSystem", "ExpressionSystem")


class FluoroscentProtein(ExperimentMaterial):
    term = RdfTerm(
        "https://w3id.org/reproduceme#FluorescentProtein", "FluoroscentProtein"
    )


class Oligonucleotide(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Oligonucleotide", "Oligonucleotide")


class Organism(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Organism", "Organism")


class Plasmid(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Plasmid", "Plasmid")


class Protein(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Protein", "Protein")


class Rna(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#RNA", "Rna")


class RestrictionEnzyme(ExperimentMaterial):
    term = RdfTerm(
        "https://w3id.org/reproduceme#RestrictionEnzyme", "RestrictionEnzyme"
    )


class Solution(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Solution", "Solution")


class Specimen(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Specimen", "Specimen")


class Vector(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#Vector", "Vector")


class CdnaSource(ExperimentMaterial):
    term = RdfTerm("https://w3id.org/reproduceme#cDNASource", "CdnaSource")


class SupportedFileFormat(Bio_Formats):
    term = RdfTerm(
        "https://w3id.org/reproduceme#SupportedFileFormat", "SupportedFileFormat"
    )


class NotebokCell(ComputationalStep):
    term = RdfTerm("https://w3id.org/reproduceme#Cell", "NotebokCell")


class ChecksumAlgorithm(Method):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ChecksumAlgorithm", "ChecksumAlgorithm"
    )


class ImagingMethod(Method):
    term = RdfTerm("https://w3id.org/reproduceme#ImagingMethod", "ImagingMethod")


class Opticaltransferfunction(Method):
    term = RdfTerm(
        "https://w3id.org/reproduceme#OpticalTransferFunction",
        "Opticaltransferfunction",
    )


class MicroscopeConfiguration(ExperimentSetup):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ConfigureMicroscope", "MicroscopeConfiguration"
    )


class Describe(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#Describe", "Describe")


class EnvironmentSetup(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#EnvironmentSetup", "EnvironmentSetup")


class ImageAcquisition(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#ImageAcquisition", "ImageAcquisition")


class ImagingStudy(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#ImagingStudy", "ImagingStudy")


class MaterialPreparationStep(ExperimentSetup):
    term = RdfTerm(
        "https://w3id.org/reproduceme#MaterialPreparationStep",
        "MaterialPreparationStep",
    )


class MicrobeamManipulation(ExperimentSetup):
    term = RdfTerm(
        "https://w3id.org/reproduceme#MicrobeamManipulation", "MicrobeamManipulation"
    )


class Noting(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#Noting", "Noting")


class OriginInformationCollection(ExperimentSetup):
    term = RdfTerm(
        "https://w3id.org/reproduceme#OriginInformationCollection",
        "OriginInformationCollection",
    )


class PlateAcquisition(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#PlateAcquisition", "PlateAcquisition")


class Tagging(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#Tagging", "Tagging")


class Treatment(ExperimentSetup):
    term = RdfTerm("https://w3id.org/reproduceme#Treatment", "Treatment")


class Format(Datatype):
    term = RdfTerm("https://w3id.org/reproduceme#ImageFormat", "Format")


class Detector(Instrument):
    term = RdfTerm("https://w3id.org/reproduceme#Detector", "Detector")


class Dichroic(Instrument):
    term = RdfTerm("https://w3id.org/reproduceme#Dichroic", "Dichroic")


class Filter(Instrument):
    term = RdfTerm("https://w3id.org/reproduceme#Filter", "Filter")


class Filterset(Instrument):
    term = RdfTerm("https://w3id.org/reproduceme#Filterset", "Filterset")


class LightSource(Instrument):
    term = RdfTerm("https://w3id.org/reproduceme#LightSource", "LightSource")


class Microscope(Instrument):
    term = RdfTerm("https://w3id.org/reproduceme#Microscope", "Microscope")


class Objective(Instrument):
    term = RdfTerm("https://w3id.org/reproduceme#Objective", "Objective")


class ExperimentType(Experiment):
    term = RdfTerm("https://w3id.org/reproduceme#ExperimentType", "ExperimentType")


class LicenseDocument(File):
    term = RdfTerm("https://w3id.org/reproduceme#LicenseDocument", "LicenseDocument")


class RightsAndPermissionsDocument(File):
    term = RdfTerm(
        "https://w3id.org/reproduceme#RightsandPermissionsDocument",
        "RightsAndPermissionsDocument",
    )


class Plate(Image):
    term = RdfTerm("https://w3id.org/reproduceme#Plate", "Plate")


class Screen(Image):
    term = RdfTerm("https://w3id.org/reproduceme#Screen", "Screen")


class Well(Image):
    term = RdfTerm("https://w3id.org/reproduceme#Well", "Well")


class WellSample(Image):
    term = RdfTerm("https://w3id.org/reproduceme#WellSample", "WellSample")


class FinalResult(Result):
    term = RdfTerm("https://w3id.org/reproduceme#FinalResult", "FinalResult")


class IntermediateResult(Result):
    term = RdfTerm(
        "https://w3id.org/reproduceme#IntermediateResult", "IntermediateResult"
    )


class NegativeResult(Result):
    term = RdfTerm("https://w3id.org/reproduceme#NegativeResult", "NegativeResult")


class PositiveResult(Result):
    term = RdfTerm("https://w3id.org/reproduceme#PositiveResult", "PositiveResult")


class ChannelFluorophore(Channelsetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ChannelFluorophore", "ChannelFluorophore"
    )


class EmissionWavelength(Channelsetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#EmissionWavelength", "EmissionWavelength"
    )


class ExcitationWavelength(Channelsetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ExcitationWavelength", "ExcitationWavelength"
    )


class NeutralDensityFilter(Channelsetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#NeutralDensityFilter", "NeutralDensityFilter"
    )


class PinholeSize(Channelsetting):
    term = RdfTerm("https://w3id.org/reproduceme#PinholeSize", "PinholeSize")


class PockelcellSetting(Channelsetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#PockelCellSetting", "PockelcellSetting"
    )


class SamplesPerPixel(Channelsetting):
    term = RdfTerm("https://w3id.org/reproduceme#SamplesPerPixel", "SamplesPerPixel")


class EnvironmentAttribute(ExperimentalCondition):
    term = RdfTerm(
        "https://w3id.org/reproduceme#EnvironmentAttribute", "EnvironmentAttribute"
    )


class GrowthCondition(ExperimentalCondition):
    term = RdfTerm("https://w3id.org/reproduceme#GrowthCondition", "GrowthCondition")


class LogicalChannelSetting(ImageSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#LogicalChannelSetting", "LogicalChannelSetting"
    )


class Pixels(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Pixels", "Pixels")


class PixelsSetting(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PixelsSetting", "PixelsSetting")


class PlaneInformation(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Plane", "PlaneInformation")


class PlaneSetting(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PlaneSetting", "PlaneSetting")


class PlateSetting(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PlateSetting", "PlateSetting")


class RegionOfInterest(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#ROI", "RegionOfInterest")


class RenderingModel(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#RenderingModel", "RenderingModel")


class ScreenSetting(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#ScreenSetting", "ScreenSetting")


class Shape(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Shape", "Shape")


class StageLabel(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#StageLabel", "StageLabel")


class Thumbnail(ImageSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Thumbnail", "Thumbnail")


class DetectorSetting(InstrumentSetting):
    term = RdfTerm("https://w3id.org/reproduceme#DetectorSetting", "DetectorSetting")


class FilterSetting(InstrumentSetting):
    term = RdfTerm("https://w3id.org/reproduceme#FilterSetting", "FilterSetting")


class LaserSetting(InstrumentSetting):
    term = RdfTerm("https://w3id.org/reproduceme#LaserSetting", "LaserSetting")


class LightSettings(InstrumentSetting):
    term = RdfTerm("https://w3id.org/reproduceme#LightSettings", "LightSettings")


class Manufactuerspec(InstrumentSetting):
    term = RdfTerm("https://w3id.org/reproduceme#ManufactuerSpec", "Manufactuerspec")


class ObjectiveSettings(InstrumentSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ObjectiveSettings", "ObjectiveSettings"
    )


class BathSolution(Solution):
    term = RdfTerm("https://w3id.org/reproduceme#BathSolution", "BathSolution")


class PipetteSolution(Solution):
    term = RdfTerm("https://w3id.org/reproduceme#PipetteSolution", "PipetteSolution")


class StockSolution(Solution):
    term = RdfTerm("https://w3id.org/reproduceme#StockSolution", "StockSolution")


class AcquistionMode(ImagingMethod):
    term = RdfTerm("https://w3id.org/reproduceme#AcquisitionMode", "AcquistionMode")


class ContrastMethod(ImagingMethod):
    term = RdfTerm("https://w3id.org/reproduceme#ContrastMethod", "ContrastMethod")


class Illumination(ImagingMethod):
    term = RdfTerm("https://w3id.org/reproduceme#Illumination", "Illumination")


class MicrobeamManipulationType(ImagingMethod):
    term = RdfTerm(
        "https://w3id.org/reproduceme#MicrobeamManipulationType",
        "MicrobeamManipulationType",
    )


class Amplification(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Amplification", "Amplification")


class Cloning(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Cloning", "Cloning")


class Concentration(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Concentration", "Concentration")


class Expression(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Expression", "Expression")


class Fixation(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Fixation", "Fixation")


class Incubation(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Incubation", "Incubation")


class IsolationOfProtein(MaterialPreparationStep):
    term = RdfTerm(
        "https://w3id.org/reproduceme#IsolationOfProtein", "IsolationOfProtein"
    )


class Preparation(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Preparation", "Preparation")


class PurificationOfProtein(MaterialPreparationStep):
    term = RdfTerm(
        "https://w3id.org/reproduceme#PurificationOfProtein", "PurificationOfProtein"
    )


class RnaInjection(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#RNAInjection", "RnaInjection")


class Sequencing(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Sequencing", "Sequencing")


class Transfection(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Transfection", "Transfection")


class Verification(MaterialPreparationStep):
    term = RdfTerm("https://w3id.org/reproduceme#Verification", "Verification")


class DetectorType(Detector):
    term = RdfTerm("https://w3id.org/reproduceme#DetectorType", "DetectorType")


class FilterType(Filter):
    term = RdfTerm("https://w3id.org/reproduceme#FilterType", "FilterType")


class Arc(LightSource):
    term = RdfTerm("https://w3id.org/reproduceme#Arc", "Arc")


class Filament(LightSource):
    term = RdfTerm("https://w3id.org/reproduceme#Filament", "Filament")


class GenericExcitationSource(LightSource):
    term = RdfTerm(
        "https://w3id.org/reproduceme#GenericExcitationSource",
        "GenericExcitationSource",
    )


class Laser(LightSource):
    term = RdfTerm("https://w3id.org/reproduceme#Laser", "Laser")


class LightEmittingDiode(LightSource):
    term = RdfTerm(
        "https://w3id.org/reproduceme#LightEmittingDiode", "LightEmittingDiode"
    )


class MicroscopeType(Microscope):
    term = RdfTerm("https://w3id.org/reproduceme#MicroscopeType", "MicroscopeType")


class HeatInactivation(EnvironmentAttribute):
    term = RdfTerm("https://w3id.org/reproduceme#HeatInactivation", "HeatInactivation")


class ImagingEnvironment(EnvironmentAttribute):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ImagingEnvironment", "ImagingEnvironment"
    )


class MethylationSensitivity(EnvironmentAttribute):
    term = RdfTerm(
        "https://w3id.org/reproduceme#MethylationSensitivity", "MethylationSensitivity"
    )


class ReactionCondition(EnvironmentAttribute):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ReactionCondition", "ReactionCondition"
    )


class Restrictionsite(EnvironmentAttribute):
    term = RdfTerm("https://w3id.org/reproduceme#RestrictionSite", "Restrictionsite")


class PhotometricInterpretation(LogicalChannelSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#PhotometricInterpretation",
        "PhotometricInterpretation",
    )


class ChannelBinding(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#ChannelBinding", "ChannelBinding")


class DimensionOrder(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#DimensionOrder", "DimensionOrder")


class Physicalsizex(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PhysicalSizeX", "Physicalsizex")


class Physicalsizey(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PhysicalSizeY", "Physicalsizey")


class Physicalsizez(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PhysicalSizeZ", "Physicalsizez")


class PixelsType(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PixelsType", "PixelsType")


class RenderingDef(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#RenderingDef", "RenderingDef")


class SignificantBits(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#SignificantBits", "SignificantBits")


class Sizec(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#SizeC", "Sizec")


class Sizet(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#SizeT", "Sizet")


class Sizex(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#SizeX", "Sizex")


class Sizey(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#SizeY", "Sizey")


class Sizez(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#SizeZ", "Sizez")


class Timeincrement(PixelsSetting):
    term = RdfTerm("https://w3id.org/reproduceme#TimeIncrement", "Timeincrement")


class Deltat(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#DeltaT", "Deltat")


class ExposureTime(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#ExposureTime", "ExposureTime")


class Positionx(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PositionX", "Positionx")


class Positiony(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PositionY", "Positiony")


class Positionz(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PositionZ", "Positionz")


class Thec(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#TheC", "Thec")


class Thet(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#TheT", "Thet")


class Thez(PlaneSetting):
    term = RdfTerm("https://w3id.org/reproduceme#TheZ", "Thez")


class ColumnNamingConvention(PlateSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ColumnNamingConvention", "ColumnNamingConvention"
    )


class Columns(PlateSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Columns", "Columns")


class Externalidentifier(PlateSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ExternalIdentifier", "Externalidentifier"
    )


class FieldIndex(PlateSetting):
    term = RdfTerm("https://w3id.org/reproduceme#FieldIndex", "FieldIndex")


class RownamingConvention(PlateSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#RowNamingConvention", "RownamingConvention"
    )


class Rows(PlateSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Rows", "Rows")


class PlateStatus(PlateSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Status", "PlateStatus")


class Welloriginx(PlateSetting):
    term = RdfTerm("https://w3id.org/reproduceme#WellOriginX", "Welloriginx")


class Welloriginy(PlateSetting):
    term = RdfTerm("https://w3id.org/reproduceme#WellOriginY", "Welloriginy")


class ProtocolDescription(ScreenSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ProtocolDescription", "ProtocolDescription"
    )


class ProtocolIdentifier(ScreenSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ProtocolIdentifier", "ProtocolIdentifier"
    )


class ReagentsetDescription(ScreenSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ReagentSetDescription", "ReagentsetDescription"
    )


class Reagentsetidentifier(ScreenSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#ReagentSetIdentifier", "Reagentsetidentifier"
    )


class Amplificationgain(DetectorSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#AmplificationGain", "Amplificationgain"
    )


class Binning(DetectorSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Binning", "Binning")


class Electronicgain(DetectorSetting):
    term = RdfTerm("https://w3id.org/reproduceme#ElectronicGain", "Electronicgain")


class Integration(DetectorSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Integration", "Integration")


class Offset(DetectorSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Offset", "Offset")


class ReadoutRate(DetectorSetting):
    term = RdfTerm("https://w3id.org/reproduceme#ReadOutRate", "ReadoutRate")


class Voltage(DetectorSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Voltage", "Voltage")


class Zoom(DetectorSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Zoom", "Zoom")


class FilterWheel(FilterSetting):
    term = RdfTerm("https://w3id.org/reproduceme#FilterWheel", "FilterWheel")


class TransmittanceRange(FilterSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#TransmittanceRange", "TransmittanceRange"
    )


class FrequencyMultiplication(LaserSetting):
    term = RdfTerm(
        "https://w3id.org/reproduceme#FrequencyMultiplication",
        "FrequencyMultiplication",
    )


class LaserTuneable(LaserSetting):
    term = RdfTerm("https://w3id.org/reproduceme#LaserTuneable", "LaserTuneable")


class Pockelcell(LaserSetting):
    term = RdfTerm("https://w3id.org/reproduceme#PockelCell", "Pockelcell")


class Pulse(LaserSetting):
    term = RdfTerm("https://w3id.org/reproduceme#Pulse", "Pulse")


class RepetitionRate(LaserSetting):
    term = RdfTerm("https://w3id.org/reproduceme#RepetitionRate", "RepetitionRate")


class Attenuation(LightSettings):
    term = RdfTerm("https://w3id.org/reproduceme#Attenuation", "Attenuation")


class Wavelength(LaserSetting, LightSettings):
    term = RdfTerm("https://w3id.org/reproduceme#Wavelength", "Wavelength")


class Power(LightSettings):
    term = RdfTerm("https://w3id.org/reproduceme#Power", "Power")


class LotNumber(Manufactuerspec):
    term = RdfTerm("https://w3id.org/reproduceme#LotNumber", "LotNumber")


class Model(Manufactuerspec):
    term = RdfTerm("https://w3id.org/reproduceme#Model", "Model")


class SerialNumber(Manufactuerspec):
    term = RdfTerm("https://w3id.org/reproduceme#SerialNumber", "SerialNumber")


class CalibratedMagnification(ObjectiveSettings):
    term = RdfTerm(
        "https://w3id.org/reproduceme#CalibratedMagnification",
        "CalibratedMagnification",
    )


class Correction(ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#Correction", "Correction")


class CorrectionCollar(ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#CorrectionCollar", "CorrectionCollar")


class Immersion(ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#Immersion", "Immersion")


class Medium(LaserSetting, ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#Medium", "Medium")


class Iris(ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#Iris", "Iris")


class LensNumericalAperture(ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#LensNA", "LensNumericalAperture")


class NominalMagnification(ObjectiveSettings):
    term = RdfTerm(
        "https://w3id.org/reproduceme#NominalMagnification", "NominalMagnification"
    )


class RefractiveIndex(ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#RefractiveIndex", "RefractiveIndex")


class WorkingDistance(ObjectiveSettings):
    term = RdfTerm("https://w3id.org/reproduceme#WorkingDistance", "WorkingDistance")


class ArcType(Arc):
    term = RdfTerm("https://w3id.org/reproduceme#ArcType", "ArcType")


class FilamentType(Filament):
    term = RdfTerm("https://w3id.org/reproduceme#FilamentType", "FilamentType")


class LaserType(Laser):
    term = RdfTerm("https://w3id.org/reproduceme#LaserType", "LaserType")


class AirPressure(ImagingEnvironment):
    term = RdfTerm("https://w3id.org/reproduceme#AirPressure", "AirPressure")


class Co2Percent(ImagingEnvironment):
    term = RdfTerm("https://w3id.org/reproduceme#CO2Percent", "Co2Percent")


class Humidity(ImagingEnvironment):
    term = RdfTerm("https://w3id.org/reproduceme#Humidity", "Humidity")


class Temperature(ImagingEnvironment):
    term = RdfTerm("https://w3id.org/reproduceme#Temperature", "Temperature")


class Family(ChannelBinding):
    term = RdfTerm("https://w3id.org/reproduceme#Family", "Family")


class Cutin(TransmittanceRange):
    term = RdfTerm("https://w3id.org/reproduceme#CutIn", "Cutin")


class CutinTolerance(TransmittanceRange):
    term = RdfTerm("https://w3id.org/reproduceme#CutInTolerance", "CutinTolerance")


class Cutout(TransmittanceRange):
    term = RdfTerm("https://w3id.org/reproduceme#CutOut", "Cutout")


class CutoutTolerance(TransmittanceRange):
    term = RdfTerm("https://w3id.org/reproduceme#CutOutTolerance", "CutoutTolerance")


class Transmittance(TransmittanceRange):
    term = RdfTerm("https://w3id.org/reproduceme#Transmittance", "Transmittance")


class creator(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/dc/terms/creator", "creator")


class Orcid(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#ORCID", "Orcid")


class Address(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#address", "Address")


class Description(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#description", "Description")


class Doi(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#doi", "Doi")


class Id(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#id", "Id")


class Modifiedattime(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#modifiedAtTime", "Modifiedattime")


class Name(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#name", "Name")


class PubmedCentralId(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#pmcid", "PubmedCentralId")


class PubmedId(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#pubmedid", "PubmedId")


class Receivedattime(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#receivedAtTime", "Receivedattime")


class Hasexperimentalmaterial(RdfProperty[reproduce.ExperimentMaterial]):
    term = RdfTerm(
        "https://w3id.org/reproduceme#hasExperimentMaterial", "Hasexperimentalmaterial"
    )


class Hasexperimentalcondition(RdfProperty[reproduce.ExperimentalCondition]):
    term = RdfTerm(
        "https://w3id.org/reproduceme#hasExperimentalCondition",
        "Hasexperimentalcondition",
    )


class Hasexperimentaldata(RdfProperty[reproduce.ExperimentalData]):
    term = RdfTerm(
        "https://w3id.org/reproduceme#hasExperimentalData", "Hasexperimentaldata"
    )


class Haspart(RdfProperty[reproduce.Instrument]):
    term = RdfTerm("https://w3id.org/reproduceme#hasPart", "Haspart")


class Hassetting(RdfProperty[reproduce.Setting]):
    term = RdfTerm("https://w3id.org/reproduceme#hasSetting", "Hassetting")


class Isaccessibleto(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#isAccessibleTo", "Isaccessibleto")


class Ispartof(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#isPartOf", "Ispartof")


class Issettingof(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#isSettingOf", "Issettingof")


class Reference(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#reference", "Reference")


class Storedat(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#storedAt", "Storedat")


class Usedmethod(RdfProperty[reproduce.Method]):
    term = RdfTerm("https://w3id.org/reproduceme#usedMethod", "Usedmethod")


class Wascreatedby(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#wasCreatedBy", "Wascreatedby")


class Wasdistributedby(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#wasDistributedBy", "Wasdistributedby")


class Wasextractedfrom(RdfProperty[reproduce.ExperimentMaterial]):
    term = RdfTerm("https://w3id.org/reproduceme#wasExtractedFrom", "Wasextractedfrom")


class Wasupdatedby(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/reproduceme#wasUpdatedBy", "Wasupdatedby")
