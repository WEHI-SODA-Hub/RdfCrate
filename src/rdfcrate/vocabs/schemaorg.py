from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import schemaorg


class DataType(rdfs.Class):
    term = RdfTerm(
        "DataType", "http://schema.org/DataType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Thing(RdfClass):
    term = RdfTerm(
        "Thing", "http://schema.org/Thing", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Event(Thing):
    term = RdfTerm(
        "Event", "http://schema.org/Event", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Action(Thing):
    term = RdfTerm(
        "Action", "http://schema.org/Action", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BioChemEntity(Thing):
    term = RdfTerm("BioChemEntity", "http://schema.org/BioChemEntity", ["1.2-DRAFT"])


class MedicalEntity(Thing):
    term = RdfTerm(
        "MedicalEntity",
        "http://schema.org/MedicalEntity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CreativeWork(Thing):
    term = RdfTerm(
        "CreativeWork",
        "http://schema.org/CreativeWork",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Product(Thing):
    term = RdfTerm(
        "Product", "http://schema.org/Product", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class StupidType(Thing):
    term = RdfTerm(
        "StupidType", "http://schema.org/StupidType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Intangible(Thing):
    term = RdfTerm(
        "Intangible", "http://schema.org/Intangible", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Taxon(Thing):
    term = RdfTerm("Taxon", "http://schema.org/Taxon", ["1.2-DRAFT"])


class Place(Thing):
    term = RdfTerm(
        "Place", "http://schema.org/Place", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Person(Thing):
    term = RdfTerm(
        "Person", "http://schema.org/Person", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Organization(Thing):
    term = RdfTerm(
        "Organization",
        "http://schema.org/Organization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CourseInstance(Event):
    term = RdfTerm(
        "CourseInstance",
        "http://schema.org/CourseInstance",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Hackathon(Event):
    term = RdfTerm("Hackathon", "http://schema.org/Hackathon", ["1.1", "1.2-DRAFT"])


class LiteraryEvent(Event):
    term = RdfTerm(
        "LiteraryEvent",
        "http://schema.org/LiteraryEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EducationEvent(Event):
    term = RdfTerm(
        "EducationEvent",
        "http://schema.org/EducationEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UserInteraction(Event):
    term = RdfTerm(
        "UserInteraction",
        "http://schema.org/UserInteraction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DeliveryEvent(Event):
    term = RdfTerm(
        "DeliveryEvent",
        "http://schema.org/DeliveryEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ComedyEvent(Event):
    term = RdfTerm(
        "ComedyEvent",
        "http://schema.org/ComedyEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Festival(Event):
    term = RdfTerm(
        "Festival", "http://schema.org/Festival", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PublicationEvent(Event):
    term = RdfTerm(
        "PublicationEvent",
        "http://schema.org/PublicationEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SportsEvent(Event):
    term = RdfTerm(
        "SportsEvent",
        "http://schema.org/SportsEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TheaterEvent(Event):
    term = RdfTerm(
        "TheaterEvent",
        "http://schema.org/TheaterEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DanceEvent(Event):
    term = RdfTerm(
        "DanceEvent", "http://schema.org/DanceEvent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ExhibitionEvent(Event):
    term = RdfTerm(
        "ExhibitionEvent",
        "http://schema.org/ExhibitionEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FoodEvent(Event):
    term = RdfTerm(
        "FoodEvent", "http://schema.org/FoodEvent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MusicEvent(Event):
    term = RdfTerm(
        "MusicEvent", "http://schema.org/MusicEvent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class SaleEvent(Event):
    term = RdfTerm(
        "SaleEvent", "http://schema.org/SaleEvent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ScreeningEvent(Event):
    term = RdfTerm(
        "ScreeningEvent",
        "http://schema.org/ScreeningEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SocialEvent(Event):
    term = RdfTerm(
        "SocialEvent",
        "http://schema.org/SocialEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ChildrensEvent(Event):
    term = RdfTerm(
        "ChildrensEvent",
        "http://schema.org/ChildrensEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BusinessEvent(Event):
    term = RdfTerm(
        "BusinessEvent",
        "http://schema.org/BusinessEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class VisualArtsEvent(Event):
    term = RdfTerm(
        "VisualArtsEvent",
        "http://schema.org/VisualArtsEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TransferAction(Action):
    term = RdfTerm(
        "TransferAction",
        "http://schema.org/TransferAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SolveMathAction(Action):
    term = RdfTerm(
        "SolveMathAction", "http://schema.org/SolveMathAction", ["1.2-DRAFT"]
    )


class AssessAction(Action):
    term = RdfTerm(
        "AssessAction",
        "http://schema.org/AssessAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SeekToAction(Action):
    term = RdfTerm("SeekToAction", "http://schema.org/SeekToAction", ["1.2-DRAFT"])


class SearchAction(Action):
    term = RdfTerm(
        "SearchAction",
        "http://schema.org/SearchAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ConsumeAction(Action):
    term = RdfTerm(
        "ConsumeAction",
        "http://schema.org/ConsumeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PlayAction(Action):
    term = RdfTerm(
        "PlayAction", "http://schema.org/PlayAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OrganizeAction(Action):
    term = RdfTerm(
        "OrganizeAction",
        "http://schema.org/OrganizeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MoveAction(Action):
    term = RdfTerm(
        "MoveAction", "http://schema.org/MoveAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CreateAction(Action):
    term = RdfTerm(
        "CreateAction",
        "http://schema.org/CreateAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AchieveAction(Action):
    term = RdfTerm(
        "AchieveAction",
        "http://schema.org/AchieveAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FindAction(Action):
    term = RdfTerm(
        "FindAction", "http://schema.org/FindAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TradeAction(Action):
    term = RdfTerm(
        "TradeAction",
        "http://schema.org/TradeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ControlAction(Action):
    term = RdfTerm(
        "ControlAction",
        "http://schema.org/ControlAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UpdateAction(Action):
    term = RdfTerm(
        "UpdateAction",
        "http://schema.org/UpdateAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InteractAction(Action):
    term = RdfTerm(
        "InteractAction",
        "http://schema.org/InteractAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ChemicalSubstance(BioChemEntity):
    term = RdfTerm(
        "ChemicalSubstance", "http://schema.org/ChemicalSubstance", ["1.2-DRAFT"]
    )


class Gene(BioChemEntity):
    term = RdfTerm("Gene", "http://schema.org/Gene", ["1.2-DRAFT"])


class Protein(BioChemEntity):
    term = RdfTerm("Protein", "http://schema.org/Protein", ["1.2-DRAFT"])


class MolecularEntity(BioChemEntity):
    term = RdfTerm(
        "MolecularEntity", "http://schema.org/MolecularEntity", ["1.2-DRAFT"]
    )


class MedicalIndication(MedicalEntity):
    term = RdfTerm(
        "MedicalIndication",
        "http://schema.org/MedicalIndication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalRiskEstimator(MedicalEntity):
    term = RdfTerm(
        "MedicalRiskEstimator",
        "http://schema.org/MedicalRiskEstimator",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalDevice(MedicalEntity):
    term = RdfTerm(
        "MedicalDevice",
        "http://schema.org/MedicalDevice",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalRiskFactor(MedicalEntity):
    term = RdfTerm(
        "MedicalRiskFactor",
        "http://schema.org/MedicalRiskFactor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrugCost(MedicalEntity):
    term = RdfTerm(
        "DrugCost", "http://schema.org/DrugCost", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MedicalStudy(MedicalEntity):
    term = RdfTerm(
        "MedicalStudy",
        "http://schema.org/MedicalStudy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AnatomicalSystem(MedicalEntity):
    term = RdfTerm(
        "AnatomicalSystem",
        "http://schema.org/AnatomicalSystem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrugClass(MedicalEntity):
    term = RdfTerm(
        "DrugClass", "http://schema.org/DrugClass", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Substance(MedicalEntity):
    term = RdfTerm(
        "Substance", "http://schema.org/Substance", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MedicalCause(MedicalEntity):
    term = RdfTerm(
        "MedicalCause",
        "http://schema.org/MedicalCause",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalProcedure(MedicalEntity):
    term = RdfTerm(
        "MedicalProcedure",
        "http://schema.org/MedicalProcedure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalIntangible(MedicalEntity):
    term = RdfTerm(
        "MedicalIntangible",
        "http://schema.org/MedicalIntangible",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalCondition(MedicalEntity):
    term = RdfTerm(
        "MedicalCondition",
        "http://schema.org/MedicalCondition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AnatomicalStructure(MedicalEntity):
    term = RdfTerm(
        "AnatomicalStructure",
        "http://schema.org/AnatomicalStructure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalTest(MedicalEntity):
    term = RdfTerm(
        "MedicalTest",
        "http://schema.org/MedicalTest",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LifestyleModification(MedicalEntity):
    term = RdfTerm(
        "LifestyleModification",
        "http://schema.org/LifestyleModification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalGuideline(MedicalEntity):
    term = RdfTerm(
        "MedicalGuideline",
        "http://schema.org/MedicalGuideline",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalContraindication(MedicalEntity):
    term = RdfTerm(
        "MedicalContraindication",
        "http://schema.org/MedicalContraindication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SuperficialAnatomy(MedicalEntity):
    term = RdfTerm(
        "SuperficialAnatomy",
        "http://schema.org/SuperficialAnatomy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Sculpture(CreativeWork):
    term = RdfTerm(
        "Sculpture", "http://schema.org/Sculpture", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Quotation(CreativeWork):
    term = RdfTerm(
        "Quotation", "http://schema.org/Quotation", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Legislation(CreativeWork):
    term = RdfTerm(
        "Legislation",
        "http://schema.org/Legislation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Dataset(CreativeWork):
    term = RdfTerm(
        "Dataset", "http://schema.org/Dataset", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Blog(CreativeWork):
    term = RdfTerm("Blog", "http://schema.org/Blog", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class MusicPlaylist(CreativeWork):
    term = RdfTerm(
        "MusicPlaylist",
        "http://schema.org/MusicPlaylist",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HowTo(CreativeWork):
    term = RdfTerm(
        "HowTo", "http://schema.org/HowTo", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Manuscript(CreativeWork):
    term = RdfTerm(
        "Manuscript", "http://schema.org/Manuscript", ["1.0", "1.1", "1.2-DRAFT"]
    )


class Conversation(CreativeWork):
    term = RdfTerm(
        "Conversation",
        "http://schema.org/Conversation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ShortStory(CreativeWork):
    term = RdfTerm(
        "ShortStory", "http://schema.org/ShortStory", ["1.0", "1.1", "1.2-DRAFT"]
    )


class Thesis(CreativeWork):
    term = RdfTerm(
        "Thesis", "http://schema.org/Thesis", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Article(CreativeWork):
    term = RdfTerm(
        "Article", "http://schema.org/Article", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Drawing(CreativeWork):
    term = RdfTerm("Drawing", "http://schema.org/Drawing", ["1.0", "1.1", "1.2-DRAFT"])


class WebContent(CreativeWork):
    term = RdfTerm(
        "WebContent", "http://schema.org/WebContent", ["1.0", "1.1", "1.2-DRAFT"]
    )


class Game(CreativeWork):
    term = RdfTerm("Game", "http://schema.org/Game", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class ComicStory(CreativeWork):
    term = RdfTerm(
        "ComicStory", "http://schema.org/ComicStory", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Season(CreativeWork):
    term = RdfTerm(
        "Season", "http://schema.org/Season", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Atlas(CreativeWork):
    term = RdfTerm(
        "Atlas", "http://schema.org/Atlas", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Clip(CreativeWork):
    term = RdfTerm("Clip", "http://schema.org/Clip", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class WebSite(CreativeWork):
    term = RdfTerm(
        "WebSite", "http://schema.org/WebSite", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WebPageElement(CreativeWork):
    term = RdfTerm(
        "WebPageElement",
        "http://schema.org/WebPageElement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MediaObject(CreativeWork):
    term = RdfTerm(
        "MediaObject",
        "http://schema.org/MediaObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Painting(CreativeWork):
    term = RdfTerm(
        "Painting", "http://schema.org/Painting", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class SoftwareApplication(CreativeWork):
    term = RdfTerm(
        "SoftwareApplication",
        "http://schema.org/SoftwareApplication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Claim(CreativeWork):
    term = RdfTerm("Claim", "http://schema.org/Claim", ["1.0", "1.1", "1.2-DRAFT"])


class PublicationIssue(CreativeWork):
    term = RdfTerm(
        "PublicationIssue",
        "http://schema.org/PublicationIssue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ArchiveComponent(CreativeWork):
    term = RdfTerm(
        "ArchiveComponent",
        "http://schema.org/ArchiveComponent",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class DataCatalog(CreativeWork):
    term = RdfTerm(
        "DataCatalog",
        "http://schema.org/DataCatalog",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Play(CreativeWork):
    term = RdfTerm("Play", "http://schema.org/Play", ["1.0", "1.1", "1.2-DRAFT"])


class MenuSection(CreativeWork):
    term = RdfTerm(
        "MenuSection",
        "http://schema.org/MenuSection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class VisualArtwork(CreativeWork):
    term = RdfTerm(
        "VisualArtwork",
        "http://schema.org/VisualArtwork",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LearningResource(CreativeWork):
    term = RdfTerm(
        "LearningResource", "http://schema.org/LearningResource", ["1.1", "1.2-DRAFT"]
    )


class MusicRecording(CreativeWork):
    term = RdfTerm(
        "MusicRecording",
        "http://schema.org/MusicRecording",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class WebPage(CreativeWork):
    term = RdfTerm(
        "WebPage", "http://schema.org/WebPage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class HyperTocEntry(CreativeWork):
    term = RdfTerm("HyperTocEntry", "http://schema.org/HyperTocEntry", ["1.2-DRAFT"])


class Statement(CreativeWork):
    term = RdfTerm("Statement", "http://schema.org/Statement", ["1.2-DRAFT"])


class Book(CreativeWork):
    term = RdfTerm("Book", "http://schema.org/Book", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Review(CreativeWork):
    term = RdfTerm(
        "Review", "http://schema.org/Review", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Chapter(CreativeWork):
    term = RdfTerm(
        "Chapter", "http://schema.org/Chapter", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Menu(CreativeWork):
    term = RdfTerm("Menu", "http://schema.org/Menu", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class SpecialAnnouncement(CreativeWork):
    term = RdfTerm(
        "SpecialAnnouncement",
        "http://schema.org/SpecialAnnouncement",
        ["1.1", "1.2-DRAFT"],
    )


class Collection(CreativeWork):
    term = RdfTerm(
        "Collection", "http://schema.org/Collection", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Certification(CreativeWork):
    term = RdfTerm("Certification", "http://schema.org/Certification", [])


class DigitalDocument(CreativeWork):
    term = RdfTerm(
        "DigitalDocument",
        "http://schema.org/DigitalDocument",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Message(CreativeWork):
    term = RdfTerm(
        "Message", "http://schema.org/Message", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DefinedTermSet(CreativeWork):
    term = RdfTerm(
        "DefinedTermSet",
        "http://schema.org/DefinedTermSet",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class Guide(CreativeWork):
    term = RdfTerm("Guide", "http://schema.org/Guide", ["1.1", "1.2-DRAFT"])


class EducationalOccupationalCredential(CreativeWork):
    term = RdfTerm(
        "EducationalOccupationalCredential",
        "http://schema.org/EducationalOccupationalCredential",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class Map(CreativeWork):
    term = RdfTerm("Map", "http://schema.org/Map", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Episode(CreativeWork):
    term = RdfTerm(
        "Episode", "http://schema.org/Episode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Photograph(CreativeWork):
    term = RdfTerm(
        "Photograph", "http://schema.org/Photograph", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MusicComposition(CreativeWork):
    term = RdfTerm(
        "MusicComposition",
        "http://schema.org/MusicComposition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Code(CreativeWork):
    term = RdfTerm("Code", "http://schema.org/Code", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class SoftwareSourceCode(CreativeWork):
    term = RdfTerm(
        "SoftwareSourceCode",
        "http://schema.org/SoftwareSourceCode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MathSolver(CreativeWork):
    term = RdfTerm("MathSolver", "http://schema.org/MathSolver", ["1.2-DRAFT"])


class SheetMusic(CreativeWork):
    term = RdfTerm(
        "SheetMusic", "http://schema.org/SheetMusic", ["1.0", "1.1", "1.2-DRAFT"]
    )


class MediaReviewItem(CreativeWork):
    term = RdfTerm(
        "MediaReviewItem", "http://schema.org/MediaReviewItem", ["1.2-DRAFT"]
    )


class Comment(CreativeWork):
    term = RdfTerm(
        "Comment", "http://schema.org/Comment", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Poster(CreativeWork):
    term = RdfTerm("Poster", "http://schema.org/Poster", ["1.0", "1.1", "1.2-DRAFT"])


class Movie(CreativeWork):
    term = RdfTerm(
        "Movie", "http://schema.org/Movie", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class HyperToc(CreativeWork):
    term = RdfTerm("HyperToc", "http://schema.org/HyperToc", ["1.2-DRAFT"])


class CreativeWorkSeason(CreativeWork):
    term = RdfTerm(
        "CreativeWorkSeason",
        "http://schema.org/CreativeWorkSeason",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PublicationVolume(CreativeWork):
    term = RdfTerm(
        "PublicationVolume",
        "http://schema.org/PublicationVolume",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ProductGroup(Product):
    term = RdfTerm(
        "ProductGroup", "http://schema.org/ProductGroup", ["1.1", "1.2-DRAFT"]
    )


class ProductModel(Product):
    term = RdfTerm(
        "ProductModel",
        "http://schema.org/ProductModel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class IndividualProduct(Product):
    term = RdfTerm(
        "IndividualProduct",
        "http://schema.org/IndividualProduct",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SomeProducts(Product):
    term = RdfTerm(
        "SomeProducts",
        "http://schema.org/SomeProducts",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Vehicle(Product):
    term = RdfTerm(
        "Vehicle", "http://schema.org/Vehicle", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Invoice(Intangible):
    term = RdfTerm(
        "Invoice", "http://schema.org/Invoice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MediaSubscription(Intangible):
    term = RdfTerm(
        "MediaSubscription",
        "http://schema.org/MediaSubscription",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class MerchantReturnPolicy(Intangible):
    term = RdfTerm(
        "MerchantReturnPolicy",
        "http://schema.org/MerchantReturnPolicy",
        ["1.1", "1.2-DRAFT"],
    )


class Class(Intangible):
    term = RdfTerm(
        "Class", "http://schema.org/Class", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Quantity(Intangible):
    term = RdfTerm(
        "Quantity", "http://schema.org/Quantity", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class FinancialIncentive(Intangible):
    term = RdfTerm("FinancialIncentive", "http://schema.org/FinancialIncentive", [])


class MemberProgram(Intangible):
    term = RdfTerm("MemberProgram", "http://schema.org/MemberProgram", [])


class Enumeration(Intangible):
    term = RdfTerm(
        "Enumeration",
        "http://schema.org/Enumeration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Occupation(Intangible):
    term = RdfTerm(
        "Occupation", "http://schema.org/Occupation", ["1.0", "1.1", "1.2-DRAFT"]
    )


class StatisticalPopulation(Intangible):
    term = RdfTerm(
        "StatisticalPopulation",
        "http://schema.org/StatisticalPopulation",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class Demand(Intangible):
    term = RdfTerm(
        "Demand", "http://schema.org/Demand", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Role(Intangible):
    term = RdfTerm("Role", "http://schema.org/Role", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class BroadcastFrequencySpecification(Intangible):
    term = RdfTerm(
        "BroadcastFrequencySpecification",
        "http://schema.org/BroadcastFrequencySpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HealthInsurancePlan(Intangible):
    term = RdfTerm(
        "HealthInsurancePlan",
        "http://schema.org/HealthInsurancePlan",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Permit(Intangible):
    term = RdfTerm(
        "Permit", "http://schema.org/Permit", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class GameServer(Intangible):
    term = RdfTerm(
        "GameServer", "http://schema.org/GameServer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PaymentMethod(Intangible):
    term = RdfTerm(
        "PaymentMethod",
        "http://schema.org/PaymentMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MemberProgramTier(Intangible):
    term = RdfTerm("MemberProgramTier", "http://schema.org/MemberProgramTier", [])


class HealthPlanFormulary(Intangible):
    term = RdfTerm(
        "HealthPlanFormulary",
        "http://schema.org/HealthPlanFormulary",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GeospatialGeometry(Intangible):
    term = RdfTerm(
        "GeospatialGeometry",
        "http://schema.org/GeospatialGeometry",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Property(Intangible):
    term = RdfTerm(
        "Property", "http://schema.org/Property", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Reservation(Intangible):
    term = RdfTerm(
        "Reservation",
        "http://schema.org/Reservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DigitalDocumentPermission(Intangible):
    term = RdfTerm(
        "DigitalDocumentPermission",
        "http://schema.org/DigitalDocumentPermission",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HealthPlanNetwork(Intangible):
    term = RdfTerm(
        "HealthPlanNetwork",
        "http://schema.org/HealthPlanNetwork",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AlignmentObject(Intangible):
    term = RdfTerm(
        "AlignmentObject",
        "http://schema.org/AlignmentObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MenuItem(Intangible):
    term = RdfTerm(
        "MenuItem", "http://schema.org/MenuItem", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DataFeedItem(Intangible):
    term = RdfTerm(
        "DataFeedItem",
        "http://schema.org/DataFeedItem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ParcelDelivery(Intangible):
    term = RdfTerm(
        "ParcelDelivery",
        "http://schema.org/ParcelDelivery",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EntryPoint(Intangible):
    term = RdfTerm(
        "EntryPoint", "http://schema.org/EntryPoint", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PropertyValueSpecification(Intangible):
    term = RdfTerm(
        "PropertyValueSpecification",
        "http://schema.org/PropertyValueSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ListItem(Intangible):
    term = RdfTerm(
        "ListItem", "http://schema.org/ListItem", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Seat(Intangible):
    term = RdfTerm("Seat", "http://schema.org/Seat", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Audience(Intangible):
    term = RdfTerm(
        "Audience", "http://schema.org/Audience", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ProgramMembership(Intangible):
    term = RdfTerm(
        "ProgramMembership",
        "http://schema.org/ProgramMembership",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Schedule(Intangible):
    term = RdfTerm(
        "Schedule", "http://schema.org/Schedule", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ConstraintNode(Intangible):
    term = RdfTerm("ConstraintNode", "http://schema.org/ConstraintNode", ["1.2-DRAFT"])


class Offer(Intangible):
    term = RdfTerm(
        "Offer", "http://schema.org/Offer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Language(Intangible):
    term = RdfTerm(
        "Language", "http://schema.org/Language", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OrderItem(Intangible):
    term = RdfTerm(
        "OrderItem", "http://schema.org/OrderItem", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Series(Intangible):
    term = RdfTerm(
        "Series", "http://schema.org/Series", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ComputerLanguage(Intangible):
    term = RdfTerm(
        "ComputerLanguage",
        "http://schema.org/ComputerLanguage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MerchantReturnPolicySeasonalOverride(Intangible):
    term = RdfTerm(
        "MerchantReturnPolicySeasonalOverride",
        "http://schema.org/MerchantReturnPolicySeasonalOverride",
        ["1.2-DRAFT"],
    )


class SpeakableSpecification(Intangible):
    term = RdfTerm(
        "SpeakableSpecification",
        "http://schema.org/SpeakableSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FloorPlan(Intangible):
    term = RdfTerm("FloorPlan", "http://schema.org/FloorPlan", ["1.1", "1.2-DRAFT"])


class Brand(Intangible):
    term = RdfTerm(
        "Brand", "http://schema.org/Brand", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class EducationalOccupationalProgram(Intangible):
    term = RdfTerm(
        "EducationalOccupationalProgram",
        "http://schema.org/EducationalOccupationalProgram",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class HealthPlanCostSharingSpecification(Intangible):
    term = RdfTerm(
        "HealthPlanCostSharingSpecification",
        "http://schema.org/HealthPlanCostSharingSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class JobPosting(Intangible):
    term = RdfTerm(
        "JobPosting", "http://schema.org/JobPosting", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Ticket(Intangible):
    term = RdfTerm(
        "Ticket", "http://schema.org/Ticket", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BedDetails(Intangible):
    term = RdfTerm(
        "BedDetails", "http://schema.org/BedDetails", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ProductReturnPolicy(Intangible):
    term = RdfTerm(
        "ProductReturnPolicy",
        "http://schema.org/ProductReturnPolicy",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class BroadcastChannel(Intangible):
    term = RdfTerm(
        "BroadcastChannel",
        "http://schema.org/BroadcastChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Trip(Intangible):
    term = RdfTerm("Trip", "http://schema.org/Trip", ["1.0", "1.1", "1.2-DRAFT"])


class VirtualLocation(Intangible):
    term = RdfTerm(
        "VirtualLocation", "http://schema.org/VirtualLocation", ["1.1", "1.2-DRAFT"]
    )


class Grant(Intangible):
    term = RdfTerm("Grant", "http://schema.org/Grant", ["1.0", "1.1", "1.2-DRAFT"])


class ServiceChannel(Intangible):
    term = RdfTerm(
        "ServiceChannel",
        "http://schema.org/ServiceChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Service(Intangible):
    term = RdfTerm(
        "Service", "http://schema.org/Service", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ItemList(Intangible):
    term = RdfTerm(
        "ItemList", "http://schema.org/ItemList", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OccupationalExperienceRequirements(Intangible):
    term = RdfTerm(
        "OccupationalExperienceRequirements",
        "http://schema.org/OccupationalExperienceRequirements",
        ["1.2-DRAFT"],
    )


class StructuredValue(Intangible):
    term = RdfTerm(
        "StructuredValue",
        "http://schema.org/StructuredValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Order(Intangible):
    term = RdfTerm(
        "Order", "http://schema.org/Order", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DefinedTerm(Intangible):
    term = RdfTerm(
        "DefinedTerm", "http://schema.org/DefinedTerm", ["1.0", "1.1", "1.2-DRAFT"]
    )


class ActionAccessSpecification(Intangible):
    term = RdfTerm(
        "ActionAccessSpecification",
        "http://schema.org/ActionAccessSpecification",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class EnergyConsumptionDetails(Intangible):
    term = RdfTerm(
        "EnergyConsumptionDetails",
        "http://schema.org/EnergyConsumptionDetails",
        ["1.1", "1.2-DRAFT"],
    )


class Rating(Intangible):
    term = RdfTerm(
        "Rating", "http://schema.org/Rating", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Residence(Place):
    term = RdfTerm(
        "Residence", "http://schema.org/Residence", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TouristDestination(Place):
    term = RdfTerm(
        "TouristDestination",
        "http://schema.org/TouristDestination",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class TouristAttraction(Place):
    term = RdfTerm(
        "TouristAttraction",
        "http://schema.org/TouristAttraction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LandmarksOrHistoricalBuildings(Place):
    term = RdfTerm(
        "LandmarksOrHistoricalBuildings",
        "http://schema.org/LandmarksOrHistoricalBuildings",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Accommodation(Place):
    term = RdfTerm(
        "Accommodation",
        "http://schema.org/Accommodation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AdministrativeArea(Place):
    term = RdfTerm(
        "AdministrativeArea",
        "http://schema.org/AdministrativeArea",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CivicStructure(Place):
    term = RdfTerm(
        "CivicStructure",
        "http://schema.org/CivicStructure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Landform(Place):
    term = RdfTerm(
        "Landform", "http://schema.org/Landform", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Project(Organization):
    term = RdfTerm("Project", "http://schema.org/Project", ["1.0", "1.1", "1.2-DRAFT"])


class MedicalOrganization(Organization):
    term = RdfTerm(
        "MedicalOrganization",
        "http://schema.org/MedicalOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SearchRescueOrganization(Organization):
    term = RdfTerm(
        "SearchRescueOrganization",
        "http://schema.org/SearchRescueOrganization",
        ["1.2-DRAFT"],
    )


class PoliticalParty(Organization):
    term = RdfTerm("PoliticalParty", "http://schema.org/PoliticalParty", ["1.2-DRAFT"])


class LocalBusiness(Place, Organization):
    term = RdfTerm(
        "LocalBusiness",
        "http://schema.org/LocalBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ResearchOrganization(Organization):
    term = RdfTerm(
        "ResearchOrganization", "http://schema.org/ResearchOrganization", ["1.2-DRAFT"]
    )


class SportsOrganization(Organization):
    term = RdfTerm(
        "SportsOrganization",
        "http://schema.org/SportsOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LibrarySystem(Organization):
    term = RdfTerm(
        "LibrarySystem",
        "http://schema.org/LibrarySystem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PerformingGroup(Organization):
    term = RdfTerm(
        "PerformingGroup",
        "http://schema.org/PerformingGroup",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Corporation(Organization):
    term = RdfTerm(
        "Corporation",
        "http://schema.org/Corporation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Consortium(Organization):
    term = RdfTerm(
        "Consortium", "http://schema.org/Consortium", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WorkersUnion(Organization):
    term = RdfTerm(
        "WorkersUnion",
        "http://schema.org/WorkersUnion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class NewsMediaOrganization(Organization):
    term = RdfTerm(
        "NewsMediaOrganization",
        "http://schema.org/NewsMediaOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class NGO(Organization):
    term = RdfTerm("NGO", "http://schema.org/NGO", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class OnlineBusiness(Organization):
    term = RdfTerm("OnlineBusiness", "http://schema.org/OnlineBusiness", ["1.2-DRAFT"])


class GovernmentOrganization(Organization):
    term = RdfTerm(
        "GovernmentOrganization",
        "http://schema.org/GovernmentOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FundingScheme(Organization):
    term = RdfTerm(
        "FundingScheme", "http://schema.org/FundingScheme", ["1.0", "1.1", "1.2-DRAFT"]
    )


class Airline(Organization):
    term = RdfTerm(
        "Airline", "http://schema.org/Airline", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class UserBlocks(UserInteraction):
    term = RdfTerm(
        "UserBlocks", "http://schema.org/UserBlocks", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class UserDownloads(UserInteraction):
    term = RdfTerm(
        "UserDownloads",
        "http://schema.org/UserDownloads",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UserTweets(UserInteraction):
    term = RdfTerm(
        "UserTweets", "http://schema.org/UserTweets", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class UserCheckins(UserInteraction):
    term = RdfTerm(
        "UserCheckins",
        "http://schema.org/UserCheckins",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UserPlays(UserInteraction):
    term = RdfTerm(
        "UserPlays", "http://schema.org/UserPlays", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class UserPageVisits(UserInteraction):
    term = RdfTerm(
        "UserPageVisits",
        "http://schema.org/UserPageVisits",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UserLikes(UserInteraction):
    term = RdfTerm(
        "UserLikes", "http://schema.org/UserLikes", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class UserComments(UserInteraction):
    term = RdfTerm(
        "UserComments",
        "http://schema.org/UserComments",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UserPlusOnes(UserInteraction):
    term = RdfTerm(
        "UserPlusOnes",
        "http://schema.org/UserPlusOnes",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OnDemandEvent(PublicationEvent):
    term = RdfTerm(
        "OnDemandEvent",
        "http://schema.org/OnDemandEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BroadcastEvent(PublicationEvent):
    term = RdfTerm(
        "BroadcastEvent",
        "http://schema.org/BroadcastEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DownloadAction(TransferAction):
    term = RdfTerm(
        "DownloadAction",
        "http://schema.org/DownloadAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReturnAction(TransferAction):
    term = RdfTerm(
        "ReturnAction",
        "http://schema.org/ReturnAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DonateAction(TransferAction):
    term = RdfTerm(
        "DonateAction",
        "http://schema.org/DonateAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GiveAction(TransferAction):
    term = RdfTerm(
        "GiveAction", "http://schema.org/GiveAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class LendAction(TransferAction):
    term = RdfTerm(
        "LendAction", "http://schema.org/LendAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TakeAction(TransferAction):
    term = RdfTerm(
        "TakeAction", "http://schema.org/TakeAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MoneyTransfer(TransferAction):
    term = RdfTerm(
        "MoneyTransfer",
        "http://schema.org/MoneyTransfer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BorrowAction(TransferAction):
    term = RdfTerm(
        "BorrowAction",
        "http://schema.org/BorrowAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReceiveAction(TransferAction):
    term = RdfTerm(
        "ReceiveAction",
        "http://schema.org/ReceiveAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SendAction(TransferAction):
    term = RdfTerm(
        "SendAction", "http://schema.org/SendAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class IgnoreAction(AssessAction):
    term = RdfTerm(
        "IgnoreAction",
        "http://schema.org/IgnoreAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReactAction(AssessAction):
    term = RdfTerm(
        "ReactAction",
        "http://schema.org/ReactAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ChooseAction(AssessAction):
    term = RdfTerm(
        "ChooseAction",
        "http://schema.org/ChooseAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReviewAction(AssessAction):
    term = RdfTerm(
        "ReviewAction",
        "http://schema.org/ReviewAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UseAction(ConsumeAction):
    term = RdfTerm(
        "UseAction", "http://schema.org/UseAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ViewAction(ConsumeAction):
    term = RdfTerm(
        "ViewAction", "http://schema.org/ViewAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class InstallAction(ConsumeAction):
    term = RdfTerm(
        "InstallAction",
        "http://schema.org/InstallAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ListenAction(ConsumeAction):
    term = RdfTerm(
        "ListenAction",
        "http://schema.org/ListenAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReadAction(ConsumeAction):
    term = RdfTerm(
        "ReadAction", "http://schema.org/ReadAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DrinkAction(ConsumeAction):
    term = RdfTerm(
        "DrinkAction",
        "http://schema.org/DrinkAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PlayGameAction(ConsumeAction):
    term = RdfTerm("PlayGameAction", "http://schema.org/PlayGameAction", ["1.2-DRAFT"])


class WatchAction(ConsumeAction):
    term = RdfTerm(
        "WatchAction",
        "http://schema.org/WatchAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EatAction(ConsumeAction):
    term = RdfTerm(
        "EatAction", "http://schema.org/EatAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PerformAction(PlayAction):
    term = RdfTerm(
        "PerformAction",
        "http://schema.org/PerformAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ExerciseAction(PlayAction):
    term = RdfTerm(
        "ExerciseAction",
        "http://schema.org/ExerciseAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AllocateAction(OrganizeAction):
    term = RdfTerm(
        "AllocateAction",
        "http://schema.org/AllocateAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BookmarkAction(OrganizeAction):
    term = RdfTerm(
        "BookmarkAction",
        "http://schema.org/BookmarkAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PlanAction(OrganizeAction):
    term = RdfTerm(
        "PlanAction", "http://schema.org/PlanAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ApplyAction(OrganizeAction):
    term = RdfTerm(
        "ApplyAction",
        "http://schema.org/ApplyAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TravelAction(MoveAction):
    term = RdfTerm(
        "TravelAction",
        "http://schema.org/TravelAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ArriveAction(MoveAction):
    term = RdfTerm(
        "ArriveAction",
        "http://schema.org/ArriveAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DepartAction(MoveAction):
    term = RdfTerm(
        "DepartAction",
        "http://schema.org/DepartAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CookAction(CreateAction):
    term = RdfTerm(
        "CookAction", "http://schema.org/CookAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WriteAction(CreateAction):
    term = RdfTerm(
        "WriteAction",
        "http://schema.org/WriteAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FilmAction(CreateAction):
    term = RdfTerm(
        "FilmAction", "http://schema.org/FilmAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PhotographAction(CreateAction):
    term = RdfTerm(
        "PhotographAction",
        "http://schema.org/PhotographAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrawAction(CreateAction):
    term = RdfTerm(
        "DrawAction", "http://schema.org/DrawAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PaintAction(CreateAction):
    term = RdfTerm(
        "PaintAction",
        "http://schema.org/PaintAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LoseAction(AchieveAction):
    term = RdfTerm(
        "LoseAction", "http://schema.org/LoseAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WinAction(AchieveAction):
    term = RdfTerm(
        "WinAction", "http://schema.org/WinAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TieAction(AchieveAction):
    term = RdfTerm(
        "TieAction", "http://schema.org/TieAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TrackAction(FindAction):
    term = RdfTerm(
        "TrackAction",
        "http://schema.org/TrackAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CheckAction(FindAction):
    term = RdfTerm(
        "CheckAction",
        "http://schema.org/CheckAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DiscoverAction(FindAction):
    term = RdfTerm(
        "DiscoverAction",
        "http://schema.org/DiscoverAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OrderAction(TradeAction):
    term = RdfTerm(
        "OrderAction",
        "http://schema.org/OrderAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class QuoteAction(TradeAction):
    term = RdfTerm(
        "QuoteAction",
        "http://schema.org/QuoteAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SellAction(TradeAction):
    term = RdfTerm(
        "SellAction", "http://schema.org/SellAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class RentAction(TradeAction):
    term = RdfTerm(
        "RentAction", "http://schema.org/RentAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PreOrderAction(TradeAction):
    term = RdfTerm(
        "PreOrderAction",
        "http://schema.org/PreOrderAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PayAction(TradeAction):
    term = RdfTerm(
        "PayAction", "http://schema.org/PayAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BuyAction(TradeAction):
    term = RdfTerm(
        "BuyAction", "http://schema.org/BuyAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TipAction(TradeAction):
    term = RdfTerm(
        "TipAction", "http://schema.org/TipAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ActivateAction(ControlAction):
    term = RdfTerm(
        "ActivateAction",
        "http://schema.org/ActivateAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DeactivateAction(ControlAction):
    term = RdfTerm(
        "DeactivateAction",
        "http://schema.org/DeactivateAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ResumeAction(ControlAction):
    term = RdfTerm(
        "ResumeAction",
        "http://schema.org/ResumeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SuspendAction(ControlAction):
    term = RdfTerm(
        "SuspendAction",
        "http://schema.org/SuspendAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReplaceAction(UpdateAction):
    term = RdfTerm(
        "ReplaceAction",
        "http://schema.org/ReplaceAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AddAction(UpdateAction):
    term = RdfTerm(
        "AddAction", "http://schema.org/AddAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DeleteAction(UpdateAction):
    term = RdfTerm(
        "DeleteAction",
        "http://schema.org/DeleteAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SubscribeAction(InteractAction):
    term = RdfTerm(
        "SubscribeAction",
        "http://schema.org/SubscribeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BefriendAction(InteractAction):
    term = RdfTerm(
        "BefriendAction",
        "http://schema.org/BefriendAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RegisterAction(InteractAction):
    term = RdfTerm(
        "RegisterAction",
        "http://schema.org/RegisterAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FollowAction(InteractAction):
    term = RdfTerm(
        "FollowAction",
        "http://schema.org/FollowAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MarryAction(InteractAction):
    term = RdfTerm(
        "MarryAction",
        "http://schema.org/MarryAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LeaveAction(InteractAction):
    term = RdfTerm(
        "LeaveAction",
        "http://schema.org/LeaveAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class JoinAction(InteractAction):
    term = RdfTerm(
        "JoinAction", "http://schema.org/JoinAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class UnRegisterAction(InteractAction):
    term = RdfTerm(
        "UnRegisterAction",
        "http://schema.org/UnRegisterAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CommunicateAction(InteractAction):
    term = RdfTerm(
        "CommunicateAction",
        "http://schema.org/CommunicateAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TreatmentIndication(MedicalIndication):
    term = RdfTerm(
        "TreatmentIndication",
        "http://schema.org/TreatmentIndication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ApprovedIndication(MedicalIndication):
    term = RdfTerm(
        "ApprovedIndication",
        "http://schema.org/ApprovedIndication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PreventionIndication(MedicalIndication):
    term = RdfTerm(
        "PreventionIndication",
        "http://schema.org/PreventionIndication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalRiskScore(MedicalRiskEstimator):
    term = RdfTerm(
        "MedicalRiskScore",
        "http://schema.org/MedicalRiskScore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalRiskCalculator(MedicalRiskEstimator):
    term = RdfTerm(
        "MedicalRiskCalculator",
        "http://schema.org/MedicalRiskCalculator",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalTrial(MedicalStudy):
    term = RdfTerm(
        "MedicalTrial",
        "http://schema.org/MedicalTrial",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalObservationalStudy(MedicalStudy):
    term = RdfTerm(
        "MedicalObservationalStudy",
        "http://schema.org/MedicalObservationalStudy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DietarySupplement(Product, Substance):
    term = RdfTerm(
        "DietarySupplement",
        "http://schema.org/DietarySupplement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Drug(Substance, Product):
    term = RdfTerm("Drug", "http://schema.org/Drug", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class SurgicalProcedure(MedicalProcedure):
    term = RdfTerm(
        "SurgicalProcedure",
        "http://schema.org/SurgicalProcedure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DiagnosticProcedure(MedicalProcedure):
    term = RdfTerm(
        "DiagnosticProcedure",
        "http://schema.org/DiagnosticProcedure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TherapeuticProcedure(MedicalProcedure):
    term = RdfTerm(
        "TherapeuticProcedure",
        "http://schema.org/TherapeuticProcedure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrugLegalStatus(MedicalIntangible):
    term = RdfTerm(
        "DrugLegalStatus",
        "http://schema.org/DrugLegalStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrugStrength(MedicalIntangible):
    term = RdfTerm(
        "DrugStrength",
        "http://schema.org/DrugStrength",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DDxElement(MedicalIntangible):
    term = RdfTerm(
        "DDxElement", "http://schema.org/DDxElement", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DoseSchedule(MedicalIntangible):
    term = RdfTerm(
        "DoseSchedule",
        "http://schema.org/DoseSchedule",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalConditionStage(MedicalIntangible):
    term = RdfTerm(
        "MedicalConditionStage",
        "http://schema.org/MedicalConditionStage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalSignOrSymptom(MedicalCondition):
    term = RdfTerm(
        "MedicalSignOrSymptom",
        "http://schema.org/MedicalSignOrSymptom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InfectiousDisease(MedicalCondition):
    term = RdfTerm(
        "InfectiousDisease",
        "http://schema.org/InfectiousDisease",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Nerve(AnatomicalStructure):
    term = RdfTerm(
        "Nerve", "http://schema.org/Nerve", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BrainStructure(AnatomicalStructure):
    term = RdfTerm(
        "BrainStructure",
        "http://schema.org/BrainStructure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Ligament(AnatomicalStructure):
    term = RdfTerm(
        "Ligament", "http://schema.org/Ligament", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Vessel(AnatomicalStructure):
    term = RdfTerm(
        "Vessel", "http://schema.org/Vessel", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Joint(AnatomicalStructure):
    term = RdfTerm(
        "Joint", "http://schema.org/Joint", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Muscle(AnatomicalStructure):
    term = RdfTerm(
        "Muscle", "http://schema.org/Muscle", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Bone(AnatomicalStructure):
    term = RdfTerm("Bone", "http://schema.org/Bone", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class PathologyTest(MedicalTest):
    term = RdfTerm(
        "PathologyTest",
        "http://schema.org/PathologyTest",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BloodTest(MedicalTest):
    term = RdfTerm(
        "BloodTest", "http://schema.org/BloodTest", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ImagingTest(MedicalTest):
    term = RdfTerm(
        "ImagingTest",
        "http://schema.org/ImagingTest",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalTestPanel(MedicalTest):
    term = RdfTerm(
        "MedicalTestPanel",
        "http://schema.org/MedicalTestPanel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PhysicalActivity(LifestyleModification):
    term = RdfTerm(
        "PhysicalActivity",
        "http://schema.org/PhysicalActivity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Diet(LifestyleModification, CreativeWork):
    term = RdfTerm("Diet", "http://schema.org/Diet", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class MedicalGuidelineRecommendation(MedicalGuideline):
    term = RdfTerm(
        "MedicalGuidelineRecommendation",
        "http://schema.org/MedicalGuidelineRecommendation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalGuidelineContraindication(MedicalGuideline):
    term = RdfTerm(
        "MedicalGuidelineContraindication",
        "http://schema.org/MedicalGuidelineContraindication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DataFeed(Dataset):
    term = RdfTerm(
        "DataFeed", "http://schema.org/DataFeed", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MusicRelease(MusicPlaylist):
    term = RdfTerm(
        "MusicRelease",
        "http://schema.org/MusicRelease",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MusicAlbum(MusicPlaylist):
    term = RdfTerm(
        "MusicAlbum", "http://schema.org/MusicAlbum", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Recipe(HowTo):
    term = RdfTerm(
        "Recipe", "http://schema.org/Recipe", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TechArticle(Article):
    term = RdfTerm(
        "TechArticle",
        "http://schema.org/TechArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ScholarlyArticle(Article):
    term = RdfTerm(
        "ScholarlyArticle",
        "http://schema.org/ScholarlyArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AdvertiserContentArticle(Article):
    term = RdfTerm(
        "AdvertiserContentArticle",
        "http://schema.org/AdvertiserContentArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SocialMediaPosting(Article):
    term = RdfTerm(
        "SocialMediaPosting",
        "http://schema.org/SocialMediaPosting",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class NewsArticle(Article):
    term = RdfTerm(
        "NewsArticle",
        "http://schema.org/NewsArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SatiricalArticle(Article):
    term = RdfTerm(
        "SatiricalArticle",
        "http://schema.org/SatiricalArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Report(Article):
    term = RdfTerm(
        "Report", "http://schema.org/Report", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class HealthTopicContent(WebContent):
    term = RdfTerm(
        "HealthTopicContent",
        "http://schema.org/HealthTopicContent",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class RadioClip(Clip):
    term = RdfTerm(
        "RadioClip", "http://schema.org/RadioClip", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TVClip(Clip):
    term = RdfTerm(
        "TVClip", "http://schema.org/TVClip", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class VideoGameClip(Clip):
    term = RdfTerm(
        "VideoGameClip",
        "http://schema.org/VideoGameClip",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MovieClip(Clip):
    term = RdfTerm(
        "MovieClip", "http://schema.org/MovieClip", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Table(WebPageElement):
    term = RdfTerm(
        "Table", "http://schema.org/Table", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class SiteNavigationElement(WebPageElement):
    term = RdfTerm(
        "SiteNavigationElement",
        "http://schema.org/SiteNavigationElement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class WPSideBar(WebPageElement):
    term = RdfTerm(
        "WPSideBar", "http://schema.org/WPSideBar", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WPAdBlock(WebPageElement):
    term = RdfTerm(
        "WPAdBlock", "http://schema.org/WPAdBlock", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WPHeader(WebPageElement):
    term = RdfTerm(
        "WPHeader", "http://schema.org/WPHeader", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WPFooter(WebPageElement):
    term = RdfTerm(
        "WPFooter", "http://schema.org/WPFooter", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class _3DModel(MediaObject):
    term = RdfTerm("3DModel", "http://schema.org/3DModel", ["1.0", "1.1", "1.2-DRAFT"])


class LegislationObject(Legislation, MediaObject):
    term = RdfTerm(
        "LegislationObject",
        "http://schema.org/LegislationObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MusicVideoObject(MediaObject):
    term = RdfTerm(
        "MusicVideoObject",
        "http://schema.org/MusicVideoObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class VideoObject(MediaObject):
    term = RdfTerm(
        "VideoObject",
        "http://schema.org/VideoObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DataDownload(MediaObject):
    term = RdfTerm(
        "DataDownload",
        "http://schema.org/DataDownload",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AudioObject(MediaObject):
    term = RdfTerm(
        "AudioObject",
        "http://schema.org/AudioObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ImageObject(MediaObject):
    term = RdfTerm(
        "ImageObject",
        "http://schema.org/ImageObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TextObject(MediaObject):
    term = RdfTerm("TextObject", "http://schema.org/TextObject", ["1.2-DRAFT"])


class AmpStory(MediaObject, CreativeWork):
    term = RdfTerm("AmpStory", "http://schema.org/AmpStory", ["1.2-DRAFT"])


class VideoGame(Game, SoftwareApplication):
    term = RdfTerm(
        "VideoGame", "http://schema.org/VideoGame", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WebApplication(SoftwareApplication):
    term = RdfTerm(
        "WebApplication",
        "http://schema.org/WebApplication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MobileApplication(SoftwareApplication):
    term = RdfTerm(
        "MobileApplication",
        "http://schema.org/MobileApplication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ComicIssue(PublicationIssue):
    term = RdfTerm(
        "ComicIssue", "http://schema.org/ComicIssue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CoverArt(VisualArtwork):
    term = RdfTerm(
        "CoverArt", "http://schema.org/CoverArt", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Course(CreativeWork, LearningResource):
    term = RdfTerm(
        "Course", "http://schema.org/Course", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Quiz(LearningResource):
    term = RdfTerm("Quiz", "http://schema.org/Quiz", ["1.1", "1.2-DRAFT"])


class Syllabus(LearningResource):
    term = RdfTerm("Syllabus", "http://schema.org/Syllabus", ["1.2-DRAFT"])


class SearchResultsPage(WebPage):
    term = RdfTerm(
        "SearchResultsPage",
        "http://schema.org/SearchResultsPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CollectionPage(WebPage):
    term = RdfTerm(
        "CollectionPage",
        "http://schema.org/CollectionPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AboutPage(WebPage):
    term = RdfTerm(
        "AboutPage", "http://schema.org/AboutPage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MedicalWebPage(WebPage):
    term = RdfTerm(
        "MedicalWebPage",
        "http://schema.org/MedicalWebPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RealEstateListing(WebPage):
    term = RdfTerm(
        "RealEstateListing",
        "http://schema.org/RealEstateListing",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class ItemPage(WebPage):
    term = RdfTerm(
        "ItemPage", "http://schema.org/ItemPage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CheckoutPage(WebPage):
    term = RdfTerm(
        "CheckoutPage",
        "http://schema.org/CheckoutPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class QAPage(WebPage):
    term = RdfTerm(
        "QAPage", "http://schema.org/QAPage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ContactPage(WebPage):
    term = RdfTerm(
        "ContactPage",
        "http://schema.org/ContactPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FAQPage(WebPage):
    term = RdfTerm("FAQPage", "http://schema.org/FAQPage", ["1.0", "1.1", "1.2-DRAFT"])


class ProfilePage(WebPage):
    term = RdfTerm(
        "ProfilePage",
        "http://schema.org/ProfilePage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MediaReview(Review):
    term = RdfTerm("MediaReview", "http://schema.org/MediaReview", ["1.1", "1.2-DRAFT"])


class Recommendation(Review):
    term = RdfTerm(
        "Recommendation", "http://schema.org/Recommendation", ["1.1", "1.2-DRAFT"]
    )


class UserReview(Review):
    term = RdfTerm(
        "UserReview", "http://schema.org/UserReview", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CriticReview(Review):
    term = RdfTerm(
        "CriticReview",
        "http://schema.org/CriticReview",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EmployerReview(Review):
    term = RdfTerm(
        "EmployerReview",
        "http://schema.org/EmployerReview",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ClaimReview(Review):
    term = RdfTerm(
        "ClaimReview",
        "http://schema.org/ClaimReview",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ProductCollection(Product, Collection):
    term = RdfTerm(
        "ProductCollection", "http://schema.org/ProductCollection", ["1.1", "1.2-DRAFT"]
    )


class NoteDigitalDocument(DigitalDocument):
    term = RdfTerm(
        "NoteDigitalDocument",
        "http://schema.org/NoteDigitalDocument",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TextDigitalDocument(DigitalDocument):
    term = RdfTerm(
        "TextDigitalDocument",
        "http://schema.org/TextDigitalDocument",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PresentationDigitalDocument(DigitalDocument):
    term = RdfTerm(
        "PresentationDigitalDocument",
        "http://schema.org/PresentationDigitalDocument",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SpreadsheetDigitalDocument(DigitalDocument):
    term = RdfTerm(
        "SpreadsheetDigitalDocument",
        "http://schema.org/SpreadsheetDigitalDocument",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EmailMessage(Message):
    term = RdfTerm(
        "EmailMessage",
        "http://schema.org/EmailMessage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CategoryCodeSet(DefinedTermSet):
    term = RdfTerm(
        "CategoryCodeSet",
        "http://schema.org/CategoryCodeSet",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PodcastEpisode(Episode):
    term = RdfTerm(
        "PodcastEpisode",
        "http://schema.org/PodcastEpisode",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class RadioEpisode(Episode):
    term = RdfTerm(
        "RadioEpisode",
        "http://schema.org/RadioEpisode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TVEpisode(Episode):
    term = RdfTerm(
        "TVEpisode", "http://schema.org/TVEpisode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Question(Comment):
    term = RdfTerm(
        "Question", "http://schema.org/Question", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CorrectionComment(Comment):
    term = RdfTerm(
        "CorrectionComment",
        "http://schema.org/CorrectionComment",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class Answer(Comment):
    term = RdfTerm(
        "Answer", "http://schema.org/Answer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TVSeason(CreativeWork, CreativeWorkSeason):
    term = RdfTerm(
        "TVSeason", "http://schema.org/TVSeason", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PodcastSeason(CreativeWorkSeason):
    term = RdfTerm(
        "PodcastSeason", "http://schema.org/PodcastSeason", ["1.0", "1.1", "1.2-DRAFT"]
    )


class RadioSeason(CreativeWorkSeason):
    term = RdfTerm(
        "RadioSeason",
        "http://schema.org/RadioSeason",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Car(Vehicle):
    term = RdfTerm("Car", "http://schema.org/Car", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Motorcycle(Vehicle):
    term = RdfTerm(
        "Motorcycle", "http://schema.org/Motorcycle", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MotorizedBicycle(Vehicle):
    term = RdfTerm(
        "MotorizedBicycle",
        "http://schema.org/MotorizedBicycle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BusOrCoach(Vehicle):
    term = RdfTerm(
        "BusOrCoach", "http://schema.org/BusOrCoach", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Duration(Quantity):
    term = RdfTerm(
        "Duration", "http://schema.org/Duration", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Mass(Quantity):
    term = RdfTerm("Mass", "http://schema.org/Mass", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Distance(Quantity):
    term = RdfTerm(
        "Distance", "http://schema.org/Distance", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Energy(Quantity):
    term = RdfTerm(
        "Energy", "http://schema.org/Energy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class EventAttendanceModeEnumeration(Enumeration):
    term = RdfTerm(
        "EventAttendanceModeEnumeration",
        "http://schema.org/EventAttendanceModeEnumeration",
        ["1.1", "1.2-DRAFT"],
    )


class ReturnFeesEnumeration(Enumeration):
    term = RdfTerm(
        "ReturnFeesEnumeration",
        "http://schema.org/ReturnFeesEnumeration",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class SizeGroupEnumeration(Enumeration):
    term = RdfTerm(
        "SizeGroupEnumeration", "http://schema.org/SizeGroupEnumeration", ["1.2-DRAFT"]
    )


class NonprofitType(Enumeration):
    term = RdfTerm(
        "NonprofitType", "http://schema.org/NonprofitType", ["1.1", "1.2-DRAFT"]
    )


class MeasurementTypeEnumeration(Enumeration):
    term = RdfTerm(
        "MeasurementTypeEnumeration",
        "http://schema.org/MeasurementTypeEnumeration",
        ["1.2-DRAFT"],
    )


class SizeSystemEnumeration(Enumeration):
    term = RdfTerm(
        "SizeSystemEnumeration",
        "http://schema.org/SizeSystemEnumeration",
        ["1.2-DRAFT"],
    )


class EnergyEfficiencyEnumeration(Enumeration):
    term = RdfTerm(
        "EnergyEfficiencyEnumeration",
        "http://schema.org/EnergyEfficiencyEnumeration",
        ["1.1", "1.2-DRAFT"],
    )


class MediaEnumeration(Enumeration):
    term = RdfTerm("MediaEnumeration", "http://schema.org/MediaEnumeration", [])


class MeasurementMethodEnum(Enumeration):
    term = RdfTerm(
        "MeasurementMethodEnum",
        "http://schema.org/MeasurementMethodEnum",
        ["1.2-DRAFT"],
    )


class IncentiveStatus(Enumeration):
    term = RdfTerm("IncentiveStatus", "http://schema.org/IncentiveStatus", [])


class MediaManipulationRatingEnumeration(Enumeration):
    term = RdfTerm(
        "MediaManipulationRatingEnumeration",
        "http://schema.org/MediaManipulationRatingEnumeration",
        ["1.1", "1.2-DRAFT"],
    )


class StatusEnumeration(Enumeration):
    term = RdfTerm(
        "StatusEnumeration", "http://schema.org/StatusEnumeration", ["1.1", "1.2-DRAFT"]
    )


class MapCategoryType(Enumeration):
    term = RdfTerm(
        "MapCategoryType",
        "http://schema.org/MapCategoryType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalEnumeration(Enumeration):
    term = RdfTerm(
        "MedicalEnumeration",
        "http://schema.org/MedicalEnumeration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FulfillmentTypeEnumeration(Enumeration):
    term = RdfTerm(
        "FulfillmentTypeEnumeration", "http://schema.org/FulfillmentTypeEnumeration", []
    )


class MusicReleaseFormatType(Enumeration):
    term = RdfTerm(
        "MusicReleaseFormatType",
        "http://schema.org/MusicReleaseFormatType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BoardingPolicyType(Enumeration):
    term = RdfTerm(
        "BoardingPolicyType",
        "http://schema.org/BoardingPolicyType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GovernmentBenefitsType(Enumeration):
    term = RdfTerm(
        "GovernmentBenefitsType",
        "http://schema.org/GovernmentBenefitsType",
        ["1.1", "1.2-DRAFT"],
    )


class GenderType(Enumeration):
    term = RdfTerm(
        "GenderType", "http://schema.org/GenderType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class LegalValueLevel(Enumeration):
    term = RdfTerm(
        "LegalValueLevel",
        "http://schema.org/LegalValueLevel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ItemListOrderType(Enumeration):
    term = RdfTerm(
        "ItemListOrderType",
        "http://schema.org/ItemListOrderType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class QualitativeValue(Enumeration):
    term = RdfTerm(
        "QualitativeValue",
        "http://schema.org/QualitativeValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PriceTypeEnumeration(Enumeration):
    term = RdfTerm(
        "PriceTypeEnumeration", "http://schema.org/PriceTypeEnumeration", ["1.2-DRAFT"]
    )


class GamePlayMode(Enumeration):
    term = RdfTerm(
        "GamePlayMode",
        "http://schema.org/GamePlayMode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PhysicalActivityCategory(Enumeration):
    term = RdfTerm(
        "PhysicalActivityCategory",
        "http://schema.org/PhysicalActivityCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Specialty(Enumeration):
    term = RdfTerm(
        "Specialty", "http://schema.org/Specialty", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MusicAlbumProductionType(Enumeration):
    term = RdfTerm(
        "MusicAlbumProductionType",
        "http://schema.org/MusicAlbumProductionType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class IncentiveQualifiedExpenseType(Enumeration):
    term = RdfTerm(
        "IncentiveQualifiedExpenseType",
        "http://schema.org/IncentiveQualifiedExpenseType",
        [],
    )


class OfferItemCondition(Enumeration):
    term = RdfTerm(
        "OfferItemCondition",
        "http://schema.org/OfferItemCondition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RsvpResponseType(Enumeration):
    term = RdfTerm(
        "RsvpResponseType",
        "http://schema.org/RsvpResponseType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ProductReturnEnumeration(Enumeration):
    term = RdfTerm(
        "ProductReturnEnumeration",
        "http://schema.org/ProductReturnEnumeration",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class MusicAlbumReleaseType(Enumeration):
    term = RdfTerm(
        "MusicAlbumReleaseType",
        "http://schema.org/MusicAlbumReleaseType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReturnLabelSourceEnumeration(Enumeration):
    term = RdfTerm(
        "ReturnLabelSourceEnumeration",
        "http://schema.org/ReturnLabelSourceEnumeration",
        ["1.2-DRAFT"],
    )


class RestrictedDiet(Enumeration):
    term = RdfTerm(
        "RestrictedDiet",
        "http://schema.org/RestrictedDiet",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class IncentiveType(Enumeration):
    term = RdfTerm("IncentiveType", "http://schema.org/IncentiveType", [])


class TierBenefitEnumeration(Enumeration):
    term = RdfTerm(
        "TierBenefitEnumeration", "http://schema.org/TierBenefitEnumeration", []
    )


class HealthAspectEnumeration(Enumeration):
    term = RdfTerm(
        "HealthAspectEnumeration",
        "http://schema.org/HealthAspectEnumeration",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class BusinessFunction(Enumeration):
    term = RdfTerm(
        "BusinessFunction",
        "http://schema.org/BusinessFunction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CertificationStatusEnumeration(Enumeration):
    term = RdfTerm(
        "CertificationStatusEnumeration",
        "http://schema.org/CertificationStatusEnumeration",
        [],
    )


class AdultOrientedEnumeration(Enumeration):
    term = RdfTerm(
        "AdultOrientedEnumeration",
        "http://schema.org/AdultOrientedEnumeration",
        ["1.2-DRAFT"],
    )


class CarUsageType(Enumeration):
    term = RdfTerm(
        "CarUsageType",
        "http://schema.org/CarUsageType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DeliveryMethod(Enumeration):
    term = RdfTerm(
        "DeliveryMethod",
        "http://schema.org/DeliveryMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DayOfWeek(Enumeration):
    term = RdfTerm(
        "DayOfWeek", "http://schema.org/DayOfWeek", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ReturnMethodEnumeration(Enumeration):
    term = RdfTerm(
        "ReturnMethodEnumeration",
        "http://schema.org/ReturnMethodEnumeration",
        ["1.2-DRAFT"],
    )


class MerchantReturnEnumeration(Enumeration):
    term = RdfTerm(
        "MerchantReturnEnumeration",
        "http://schema.org/MerchantReturnEnumeration",
        ["1.1", "1.2-DRAFT"],
    )


class WarrantyScope(Enumeration):
    term = RdfTerm(
        "WarrantyScope",
        "http://schema.org/WarrantyScope",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ItemAvailability(Enumeration):
    term = RdfTerm(
        "ItemAvailability",
        "http://schema.org/ItemAvailability",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RefundTypeEnumeration(Enumeration):
    term = RdfTerm(
        "RefundTypeEnumeration",
        "http://schema.org/RefundTypeEnumeration",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class DigitalDocumentPermissionType(Enumeration):
    term = RdfTerm(
        "DigitalDocumentPermissionType",
        "http://schema.org/DigitalDocumentPermissionType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BusinessEntityType(Enumeration):
    term = RdfTerm(
        "BusinessEntityType",
        "http://schema.org/BusinessEntityType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BookFormatType(Enumeration):
    term = RdfTerm(
        "BookFormatType",
        "http://schema.org/BookFormatType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GameAvailabilityEnumeration(Enumeration):
    term = RdfTerm(
        "GameAvailabilityEnumeration",
        "http://schema.org/GameAvailabilityEnumeration",
        ["1.2-DRAFT"],
    )


class DigitalPlatformEnumeration(Enumeration):
    term = RdfTerm(
        "DigitalPlatformEnumeration",
        "http://schema.org/DigitalPlatformEnumeration",
        ["1.2-DRAFT"],
    )


class PriceComponentTypeEnumeration(Enumeration):
    term = RdfTerm(
        "PriceComponentTypeEnumeration",
        "http://schema.org/PriceComponentTypeEnumeration",
        ["1.2-DRAFT"],
    )


class PaymentMethodType(Enumeration):
    term = RdfTerm("PaymentMethodType", "http://schema.org/PaymentMethodType", [])


class ContactPointOption(Enumeration):
    term = RdfTerm(
        "ContactPointOption",
        "http://schema.org/ContactPointOption",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PurchaseType(Enumeration):
    term = RdfTerm("PurchaseType", "http://schema.org/PurchaseType", [])


class LinkRole(Role):
    term = RdfTerm(
        "LinkRole", "http://schema.org/LinkRole", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OrganizationRole(Role):
    term = RdfTerm(
        "OrganizationRole",
        "http://schema.org/OrganizationRole",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PerformanceRole(Role):
    term = RdfTerm(
        "PerformanceRole",
        "http://schema.org/PerformanceRole",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GovernmentPermit(Permit):
    term = RdfTerm(
        "GovernmentPermit",
        "http://schema.org/GovernmentPermit",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EventReservation(Reservation):
    term = RdfTerm(
        "EventReservation",
        "http://schema.org/EventReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TaxiReservation(Reservation):
    term = RdfTerm(
        "TaxiReservation",
        "http://schema.org/TaxiReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReservationPackage(Reservation):
    term = RdfTerm(
        "ReservationPackage",
        "http://schema.org/ReservationPackage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RentalCarReservation(Reservation):
    term = RdfTerm(
        "RentalCarReservation",
        "http://schema.org/RentalCarReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LodgingReservation(Reservation):
    term = RdfTerm(
        "LodgingReservation",
        "http://schema.org/LodgingReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FlightReservation(Reservation):
    term = RdfTerm(
        "FlightReservation",
        "http://schema.org/FlightReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BusReservation(Reservation):
    term = RdfTerm(
        "BusReservation",
        "http://schema.org/BusReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FoodEstablishmentReservation(Reservation):
    term = RdfTerm(
        "FoodEstablishmentReservation",
        "http://schema.org/FoodEstablishmentReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BoatReservation(Reservation):
    term = RdfTerm(
        "BoatReservation", "http://schema.org/BoatReservation", ["1.1", "1.2-DRAFT"]
    )


class TrainReservation(Reservation):
    term = RdfTerm(
        "TrainReservation",
        "http://schema.org/TrainReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HowToItem(ListItem):
    term = RdfTerm(
        "HowToItem", "http://schema.org/HowToItem", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class HowToDirection(ListItem, CreativeWork):
    term = RdfTerm(
        "HowToDirection",
        "http://schema.org/HowToDirection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HowToTip(ListItem, CreativeWork):
    term = RdfTerm(
        "HowToTip", "http://schema.org/HowToTip", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BusinessAudience(Audience):
    term = RdfTerm(
        "BusinessAudience",
        "http://schema.org/BusinessAudience",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EducationalAudience(Audience):
    term = RdfTerm(
        "EducationalAudience",
        "http://schema.org/EducationalAudience",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Researcher(Audience):
    term = RdfTerm(
        "Researcher", "http://schema.org/Researcher", ["1.0", "1.1", "1.2-DRAFT"]
    )


class PeopleAudience(Audience):
    term = RdfTerm(
        "PeopleAudience",
        "http://schema.org/PeopleAudience",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class StatisticalVariable(ConstraintNode):
    term = RdfTerm(
        "StatisticalVariable", "http://schema.org/StatisticalVariable", ["1.2-DRAFT"]
    )


class AggregateOffer(Offer):
    term = RdfTerm(
        "AggregateOffer",
        "http://schema.org/AggregateOffer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OfferForLease(Offer):
    term = RdfTerm(
        "OfferForLease", "http://schema.org/OfferForLease", ["1.0", "1.1", "1.2-DRAFT"]
    )


class OfferForPurchase(Offer):
    term = RdfTerm(
        "OfferForPurchase",
        "http://schema.org/OfferForPurchase",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class EventSeries(Event, Series):
    term = RdfTerm(
        "EventSeries",
        "http://schema.org/EventSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CreativeWorkSeries(Series, CreativeWork):
    term = RdfTerm(
        "CreativeWorkSeries",
        "http://schema.org/CreativeWorkSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class WorkBasedProgram(EducationalOccupationalProgram):
    term = RdfTerm(
        "WorkBasedProgram",
        "http://schema.org/WorkBasedProgram",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class TelevisionChannel(BroadcastChannel):
    term = RdfTerm(
        "TelevisionChannel",
        "http://schema.org/TelevisionChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RadioChannel(BroadcastChannel):
    term = RdfTerm(
        "RadioChannel",
        "http://schema.org/RadioChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TrainTrip(Trip):
    term = RdfTerm(
        "TrainTrip", "http://schema.org/TrainTrip", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BoatTrip(Trip):
    term = RdfTerm("BoatTrip", "http://schema.org/BoatTrip", ["1.1", "1.2-DRAFT"])


class BusTrip(Trip):
    term = RdfTerm(
        "BusTrip", "http://schema.org/BusTrip", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Flight(Trip):
    term = RdfTerm(
        "Flight", "http://schema.org/Flight", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TouristTrip(Trip):
    term = RdfTerm(
        "TouristTrip", "http://schema.org/TouristTrip", ["1.0", "1.1", "1.2-DRAFT"]
    )


class MonetaryGrant(Grant):
    term = RdfTerm(
        "MonetaryGrant", "http://schema.org/MonetaryGrant", ["1.0", "1.1", "1.2-DRAFT"]
    )


class BroadcastService(Service):
    term = RdfTerm(
        "BroadcastService",
        "http://schema.org/BroadcastService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FoodService(Service):
    term = RdfTerm(
        "FoodService",
        "http://schema.org/FoodService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GovernmentService(Service):
    term = RdfTerm(
        "GovernmentService",
        "http://schema.org/GovernmentService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Taxi(Service):
    term = RdfTerm("Taxi", "http://schema.org/Taxi", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class FinancialProduct(Service):
    term = RdfTerm(
        "FinancialProduct",
        "http://schema.org/FinancialProduct",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class WebAPI(Service):
    term = RdfTerm(
        "WebAPI", "http://schema.org/WebAPI", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CableOrSatelliteService(Service):
    term = RdfTerm(
        "CableOrSatelliteService",
        "http://schema.org/CableOrSatelliteService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TaxiService(Service):
    term = RdfTerm(
        "TaxiService",
        "http://schema.org/TaxiService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HowToSection(ItemList, ListItem, CreativeWork):
    term = RdfTerm(
        "HowToSection",
        "http://schema.org/HowToSection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HowToStep(ItemList, ListItem, CreativeWork):
    term = RdfTerm(
        "HowToStep", "http://schema.org/HowToStep", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BreadcrumbList(ItemList):
    term = RdfTerm(
        "BreadcrumbList",
        "http://schema.org/BreadcrumbList",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OfferCatalog(ItemList):
    term = RdfTerm(
        "OfferCatalog",
        "http://schema.org/OfferCatalog",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DefinedRegion(StructuredValue):
    term = RdfTerm(
        "DefinedRegion", "http://schema.org/DefinedRegion", ["1.1", "1.2-DRAFT"]
    )


class ShippingDeliveryTime(StructuredValue):
    term = RdfTerm(
        "ShippingDeliveryTime",
        "http://schema.org/ShippingDeliveryTime",
        ["1.1", "1.2-DRAFT"],
    )


class RepaymentSpecification(StructuredValue):
    term = RdfTerm(
        "RepaymentSpecification",
        "http://schema.org/RepaymentSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PostalCodeRangeSpecification(StructuredValue):
    term = RdfTerm(
        "PostalCodeRangeSpecification",
        "http://schema.org/PostalCodeRangeSpecification",
        ["1.1", "1.2-DRAFT"],
    )


class ExchangeRateSpecification(StructuredValue):
    term = RdfTerm(
        "ExchangeRateSpecification",
        "http://schema.org/ExchangeRateSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GeoShape(StructuredValue):
    term = RdfTerm(
        "GeoShape", "http://schema.org/GeoShape", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OfferShippingDetails(StructuredValue):
    term = RdfTerm(
        "OfferShippingDetails",
        "http://schema.org/OfferShippingDetails",
        ["1.1", "1.2-DRAFT"],
    )


class QuantitativeValueDistribution(StructuredValue):
    term = RdfTerm(
        "QuantitativeValueDistribution",
        "http://schema.org/QuantitativeValueDistribution",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class CDCPMDRecord(StructuredValue):
    term = RdfTerm(
        "CDCPMDRecord", "http://schema.org/CDCPMDRecord", ["1.1", "1.2-DRAFT"]
    )


class EngineSpecification(StructuredValue):
    term = RdfTerm(
        "EngineSpecification",
        "http://schema.org/EngineSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PropertyValue(StructuredValue):
    term = RdfTerm(
        "PropertyValue",
        "http://schema.org/PropertyValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ShippingConditions(StructuredValue):
    term = RdfTerm("ShippingConditions", "http://schema.org/ShippingConditions", [])


class DatedMoneySpecification(StructuredValue):
    term = RdfTerm(
        "DatedMoneySpecification",
        "http://schema.org/DatedMoneySpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class QuantitativeValue(StructuredValue):
    term = RdfTerm(
        "QuantitativeValue",
        "http://schema.org/QuantitativeValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MonetaryAmount(StructuredValue):
    term = RdfTerm(
        "MonetaryAmount",
        "http://schema.org/MonetaryAmount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InteractionCounter(StructuredValue):
    term = RdfTerm(
        "InteractionCounter",
        "http://schema.org/InteractionCounter",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class WarrantyPromise(StructuredValue):
    term = RdfTerm(
        "WarrantyPromise",
        "http://schema.org/WarrantyPromise",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ContactPoint(StructuredValue):
    term = RdfTerm(
        "ContactPoint",
        "http://schema.org/ContactPoint",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GeoCoordinates(StructuredValue):
    term = RdfTerm(
        "GeoCoordinates",
        "http://schema.org/GeoCoordinates",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OwnershipInfo(StructuredValue):
    term = RdfTerm(
        "OwnershipInfo",
        "http://schema.org/OwnershipInfo",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PriceSpecification(StructuredValue):
    term = RdfTerm(
        "PriceSpecification",
        "http://schema.org/PriceSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ShippingRateSettings(StructuredValue):
    term = RdfTerm(
        "ShippingRateSettings",
        "http://schema.org/ShippingRateSettings",
        ["1.1", "1.2-DRAFT"],
    )


class ServicePeriod(StructuredValue):
    term = RdfTerm("ServicePeriod", "http://schema.org/ServicePeriod", [])


class NutritionInformation(StructuredValue):
    term = RdfTerm(
        "NutritionInformation",
        "http://schema.org/NutritionInformation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DeliveryTimeSettings(StructuredValue):
    term = RdfTerm(
        "DeliveryTimeSettings",
        "http://schema.org/DeliveryTimeSettings",
        ["1.1", "1.2-DRAFT"],
    )


class TypeAndQuantityNode(StructuredValue):
    term = RdfTerm(
        "TypeAndQuantityNode",
        "http://schema.org/TypeAndQuantityNode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ShippingService(StructuredValue):
    term = RdfTerm("ShippingService", "http://schema.org/ShippingService", [])


class OpeningHoursSpecification(StructuredValue):
    term = RdfTerm(
        "OpeningHoursSpecification",
        "http://schema.org/OpeningHoursSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CategoryCode(DefinedTerm):
    term = RdfTerm(
        "CategoryCode",
        "http://schema.org/CategoryCode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AggregateRating(Rating):
    term = RdfTerm(
        "AggregateRating",
        "http://schema.org/AggregateRating",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EndorsementRating(Rating):
    term = RdfTerm(
        "EndorsementRating",
        "http://schema.org/EndorsementRating",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ApartmentComplex(Residence):
    term = RdfTerm(
        "ApartmentComplex",
        "http://schema.org/ApartmentComplex",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GatedResidenceCommunity(Residence):
    term = RdfTerm(
        "GatedResidenceCommunity",
        "http://schema.org/GatedResidenceCommunity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CampingPitch(Accommodation):
    term = RdfTerm(
        "CampingPitch",
        "http://schema.org/CampingPitch",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Suite(Accommodation):
    term = RdfTerm(
        "Suite", "http://schema.org/Suite", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class House(Accommodation):
    term = RdfTerm(
        "House", "http://schema.org/House", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Apartment(Accommodation):
    term = RdfTerm(
        "Apartment", "http://schema.org/Apartment", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Room(Accommodation):
    term = RdfTerm("Room", "http://schema.org/Room", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class SchoolDistrict(AdministrativeArea):
    term = RdfTerm(
        "SchoolDistrict", "http://schema.org/SchoolDistrict", ["1.1", "1.2-DRAFT"]
    )


class Country(AdministrativeArea):
    term = RdfTerm(
        "Country", "http://schema.org/Country", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class City(AdministrativeArea):
    term = RdfTerm("City", "http://schema.org/City", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class State(AdministrativeArea):
    term = RdfTerm(
        "State", "http://schema.org/State", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Bridge(CivicStructure):
    term = RdfTerm(
        "Bridge", "http://schema.org/Bridge", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PublicToilet(CivicStructure):
    term = RdfTerm(
        "PublicToilet",
        "http://schema.org/PublicToilet",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Playground(CivicStructure):
    term = RdfTerm(
        "Playground", "http://schema.org/Playground", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PlaceOfWorship(CivicStructure):
    term = RdfTerm(
        "PlaceOfWorship",
        "http://schema.org/PlaceOfWorship",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Zoo(CivicStructure):
    term = RdfTerm("Zoo", "http://schema.org/Zoo", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Beach(CivicStructure):
    term = RdfTerm(
        "Beach", "http://schema.org/Beach", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class EducationalOrganization(CivicStructure, Organization):
    term = RdfTerm(
        "EducationalOrganization",
        "http://schema.org/EducationalOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RVPark(CivicStructure):
    term = RdfTerm(
        "RVPark", "http://schema.org/RVPark", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Airport(CivicStructure):
    term = RdfTerm(
        "Airport", "http://schema.org/Airport", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ParkingFacility(CivicStructure):
    term = RdfTerm(
        "ParkingFacility",
        "http://schema.org/ParkingFacility",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TrainStation(CivicStructure):
    term = RdfTerm(
        "TrainStation",
        "http://schema.org/TrainStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Park(CivicStructure):
    term = RdfTerm("Park", "http://schema.org/Park", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class MusicVenue(CivicStructure):
    term = RdfTerm(
        "MusicVenue", "http://schema.org/MusicVenue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class SubwayStation(CivicStructure):
    term = RdfTerm(
        "SubwayStation",
        "http://schema.org/SubwayStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Aquarium(CivicStructure):
    term = RdfTerm(
        "Aquarium", "http://schema.org/Aquarium", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Crematorium(CivicStructure):
    term = RdfTerm(
        "Crematorium",
        "http://schema.org/Crematorium",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Museum(CivicStructure):
    term = RdfTerm(
        "Museum", "http://schema.org/Museum", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class GovernmentBuilding(CivicStructure):
    term = RdfTerm(
        "GovernmentBuilding",
        "http://schema.org/GovernmentBuilding",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EventVenue(CivicStructure):
    term = RdfTerm(
        "EventVenue", "http://schema.org/EventVenue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BusStation(CivicStructure):
    term = RdfTerm(
        "BusStation", "http://schema.org/BusStation", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BusStop(CivicStructure):
    term = RdfTerm(
        "BusStop", "http://schema.org/BusStop", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Cemetery(CivicStructure):
    term = RdfTerm(
        "Cemetery", "http://schema.org/Cemetery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BoatTerminal(CivicStructure):
    term = RdfTerm(
        "BoatTerminal", "http://schema.org/BoatTerminal", ["1.1", "1.2-DRAFT"]
    )


class PerformingArtsTheater(CivicStructure):
    term = RdfTerm(
        "PerformingArtsTheater",
        "http://schema.org/PerformingArtsTheater",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TaxiStand(CivicStructure):
    term = RdfTerm(
        "TaxiStand", "http://schema.org/TaxiStand", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Continent(Landform):
    term = RdfTerm(
        "Continent", "http://schema.org/Continent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Mountain(Landform):
    term = RdfTerm(
        "Mountain", "http://schema.org/Mountain", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Volcano(Landform):
    term = RdfTerm(
        "Volcano", "http://schema.org/Volcano", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BodyOfWater(Landform):
    term = RdfTerm(
        "BodyOfWater",
        "http://schema.org/BodyOfWater",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FundingAgency(Project):
    term = RdfTerm(
        "FundingAgency", "http://schema.org/FundingAgency", ["1.0", "1.1", "1.2-DRAFT"]
    )


class ResearchProject(Project):
    term = RdfTerm(
        "ResearchProject",
        "http://schema.org/ResearchProject",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class VeterinaryCare(MedicalOrganization):
    term = RdfTerm(
        "VeterinaryCare",
        "http://schema.org/VeterinaryCare",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DiagnosticLab(MedicalOrganization):
    term = RdfTerm(
        "DiagnosticLab",
        "http://schema.org/DiagnosticLab",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LodgingBusiness(LocalBusiness):
    term = RdfTerm(
        "LodgingBusiness",
        "http://schema.org/LodgingBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EmergencyService(LocalBusiness):
    term = RdfTerm(
        "EmergencyService",
        "http://schema.org/EmergencyService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DryCleaningOrLaundry(LocalBusiness):
    term = RdfTerm(
        "DryCleaningOrLaundry",
        "http://schema.org/DryCleaningOrLaundry",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ArchiveOrganization(LocalBusiness):
    term = RdfTerm(
        "ArchiveOrganization",
        "http://schema.org/ArchiveOrganization",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalBusiness(LocalBusiness):
    term = RdfTerm(
        "MedicalBusiness",
        "http://schema.org/MedicalBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Library(LocalBusiness):
    term = RdfTerm(
        "Library", "http://schema.org/Library", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class EmploymentAgency(LocalBusiness):
    term = RdfTerm(
        "EmploymentAgency",
        "http://schema.org/EmploymentAgency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InternetCafe(LocalBusiness):
    term = RdfTerm(
        "InternetCafe",
        "http://schema.org/InternetCafe",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FoodEstablishment(LocalBusiness):
    term = RdfTerm(
        "FoodEstablishment",
        "http://schema.org/FoodEstablishment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TouristInformationCenter(LocalBusiness):
    term = RdfTerm(
        "TouristInformationCenter",
        "http://schema.org/TouristInformationCenter",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AutomotiveBusiness(LocalBusiness):
    term = RdfTerm(
        "AutomotiveBusiness",
        "http://schema.org/AutomotiveBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RealEstateAgent(LocalBusiness):
    term = RdfTerm(
        "RealEstateAgent",
        "http://schema.org/RealEstateAgent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SelfStorage(LocalBusiness):
    term = RdfTerm(
        "SelfStorage",
        "http://schema.org/SelfStorage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TravelAgency(LocalBusiness):
    term = RdfTerm(
        "TravelAgency",
        "http://schema.org/TravelAgency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ShoppingCenter(LocalBusiness):
    term = RdfTerm(
        "ShoppingCenter",
        "http://schema.org/ShoppingCenter",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HealthAndBeautyBusiness(LocalBusiness):
    term = RdfTerm(
        "HealthAndBeautyBusiness",
        "http://schema.org/HealthAndBeautyBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LegalService(LocalBusiness):
    term = RdfTerm(
        "LegalService",
        "http://schema.org/LegalService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Store(LocalBusiness):
    term = RdfTerm(
        "Store", "http://schema.org/Store", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class SportsActivityLocation(LocalBusiness):
    term = RdfTerm(
        "SportsActivityLocation",
        "http://schema.org/SportsActivityLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AnimalShelter(LocalBusiness):
    term = RdfTerm(
        "AnimalShelter",
        "http://schema.org/AnimalShelter",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TelevisionStation(LocalBusiness):
    term = RdfTerm(
        "TelevisionStation",
        "http://schema.org/TelevisionStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RadioStation(LocalBusiness):
    term = RdfTerm(
        "RadioStation",
        "http://schema.org/RadioStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ChildCare(LocalBusiness):
    term = RdfTerm(
        "ChildCare", "http://schema.org/ChildCare", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class RecyclingCenter(LocalBusiness):
    term = RdfTerm(
        "RecyclingCenter",
        "http://schema.org/RecyclingCenter",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GovernmentOffice(LocalBusiness):
    term = RdfTerm(
        "GovernmentOffice",
        "http://schema.org/GovernmentOffice",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ProfessionalService(LocalBusiness):
    term = RdfTerm(
        "ProfessionalService",
        "http://schema.org/ProfessionalService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FinancialService(LocalBusiness):
    term = RdfTerm(
        "FinancialService",
        "http://schema.org/FinancialService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HomeAndConstructionBusiness(LocalBusiness):
    term = RdfTerm(
        "HomeAndConstructionBusiness",
        "http://schema.org/HomeAndConstructionBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EntertainmentBusiness(LocalBusiness):
    term = RdfTerm(
        "EntertainmentBusiness",
        "http://schema.org/EntertainmentBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SportsTeam(SportsOrganization):
    term = RdfTerm(
        "SportsTeam", "http://schema.org/SportsTeam", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TheaterGroup(PerformingGroup):
    term = RdfTerm(
        "TheaterGroup",
        "http://schema.org/TheaterGroup",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DanceGroup(PerformingGroup):
    term = RdfTerm(
        "DanceGroup", "http://schema.org/DanceGroup", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MusicGroup(PerformingGroup):
    term = RdfTerm(
        "MusicGroup", "http://schema.org/MusicGroup", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OnlineStore(OnlineBusiness):
    term = RdfTerm("OnlineStore", "http://schema.org/OnlineStore", ["1.2-DRAFT"])


class AgreeAction(ReactAction):
    term = RdfTerm(
        "AgreeAction",
        "http://schema.org/AgreeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class WantAction(ReactAction):
    term = RdfTerm(
        "WantAction", "http://schema.org/WantAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class EndorseAction(ReactAction):
    term = RdfTerm(
        "EndorseAction",
        "http://schema.org/EndorseAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LikeAction(ReactAction):
    term = RdfTerm(
        "LikeAction", "http://schema.org/LikeAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DisagreeAction(ReactAction):
    term = RdfTerm(
        "DisagreeAction",
        "http://schema.org/DisagreeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DislikeAction(ReactAction):
    term = RdfTerm(
        "DislikeAction",
        "http://schema.org/DislikeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class VoteAction(ChooseAction):
    term = RdfTerm(
        "VoteAction", "http://schema.org/VoteAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WearAction(UseAction):
    term = RdfTerm(
        "WearAction", "http://schema.org/WearAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class AssignAction(AllocateAction):
    term = RdfTerm(
        "AssignAction",
        "http://schema.org/AssignAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AcceptAction(AllocateAction):
    term = RdfTerm(
        "AcceptAction",
        "http://schema.org/AcceptAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RejectAction(AllocateAction):
    term = RdfTerm(
        "RejectAction",
        "http://schema.org/RejectAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AuthorizeAction(AllocateAction):
    term = RdfTerm(
        "AuthorizeAction",
        "http://schema.org/AuthorizeAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ScheduleAction(PlanAction):
    term = RdfTerm(
        "ScheduleAction",
        "http://schema.org/ScheduleAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CancelAction(PlanAction):
    term = RdfTerm(
        "CancelAction",
        "http://schema.org/CancelAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReserveAction(PlanAction):
    term = RdfTerm(
        "ReserveAction",
        "http://schema.org/ReserveAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InsertAction(AddAction):
    term = RdfTerm(
        "InsertAction",
        "http://schema.org/InsertAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReplyAction(CommunicateAction):
    term = RdfTerm(
        "ReplyAction",
        "http://schema.org/ReplyAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AskAction(CommunicateAction):
    term = RdfTerm(
        "AskAction", "http://schema.org/AskAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ShareAction(CommunicateAction):
    term = RdfTerm(
        "ShareAction",
        "http://schema.org/ShareAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InviteAction(CommunicateAction):
    term = RdfTerm(
        "InviteAction",
        "http://schema.org/InviteAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CheckInAction(CommunicateAction):
    term = RdfTerm(
        "CheckInAction",
        "http://schema.org/CheckInAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InformAction(CommunicateAction):
    term = RdfTerm(
        "InformAction",
        "http://schema.org/InformAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CheckOutAction(CommunicateAction):
    term = RdfTerm(
        "CheckOutAction",
        "http://schema.org/CheckOutAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CommentAction(CommunicateAction):
    term = RdfTerm(
        "CommentAction",
        "http://schema.org/CommentAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PsychologicalTreatment(TherapeuticProcedure):
    term = RdfTerm(
        "PsychologicalTreatment",
        "http://schema.org/PsychologicalTreatment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalTherapy(TherapeuticProcedure):
    term = RdfTerm(
        "MedicalTherapy",
        "http://schema.org/MedicalTherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RecommendedDoseSchedule(DoseSchedule):
    term = RdfTerm(
        "RecommendedDoseSchedule",
        "http://schema.org/RecommendedDoseSchedule",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MaximumDoseSchedule(DoseSchedule):
    term = RdfTerm(
        "MaximumDoseSchedule",
        "http://schema.org/MaximumDoseSchedule",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReportedDoseSchedule(DoseSchedule):
    term = RdfTerm(
        "ReportedDoseSchedule",
        "http://schema.org/ReportedDoseSchedule",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalSymptom(MedicalSignOrSymptom):
    term = RdfTerm(
        "MedicalSymptom",
        "http://schema.org/MedicalSymptom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalSign(MedicalSignOrSymptom):
    term = RdfTerm(
        "MedicalSign",
        "http://schema.org/MedicalSign",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Vein(Vessel):
    term = RdfTerm("Vein", "http://schema.org/Vein", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Artery(Vessel):
    term = RdfTerm(
        "Artery", "http://schema.org/Artery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class LymphaticVessel(Vessel):
    term = RdfTerm(
        "LymphaticVessel",
        "http://schema.org/LymphaticVessel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ExercisePlan(CreativeWork, PhysicalActivity):
    term = RdfTerm(
        "ExercisePlan",
        "http://schema.org/ExercisePlan",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CompleteDataFeed(DataFeed):
    term = RdfTerm(
        "CompleteDataFeed",
        "http://schema.org/CompleteDataFeed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class APIReference(TechArticle):
    term = RdfTerm(
        "APIReference",
        "http://schema.org/APIReference",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalScholarlyArticle(ScholarlyArticle):
    term = RdfTerm(
        "MedicalScholarlyArticle",
        "http://schema.org/MedicalScholarlyArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BlogPosting(SocialMediaPosting):
    term = RdfTerm(
        "BlogPosting",
        "http://schema.org/BlogPosting",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DiscussionForumPosting(SocialMediaPosting):
    term = RdfTerm(
        "DiscussionForumPosting",
        "http://schema.org/DiscussionForumPosting",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BackgroundNewsArticle(NewsArticle):
    term = RdfTerm(
        "BackgroundNewsArticle",
        "http://schema.org/BackgroundNewsArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AnalysisNewsArticle(NewsArticle):
    term = RdfTerm(
        "AnalysisNewsArticle",
        "http://schema.org/AnalysisNewsArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReportageNewsArticle(NewsArticle):
    term = RdfTerm(
        "ReportageNewsArticle",
        "http://schema.org/ReportageNewsArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AskPublicNewsArticle(NewsArticle):
    term = RdfTerm(
        "AskPublicNewsArticle",
        "http://schema.org/AskPublicNewsArticle",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class OpinionNewsArticle(NewsArticle):
    term = RdfTerm(
        "OpinionNewsArticle",
        "http://schema.org/OpinionNewsArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class VideoObjectSnapshot(VideoObject):
    term = RdfTerm(
        "VideoObjectSnapshot", "http://schema.org/VideoObjectSnapshot", ["1.2-DRAFT"]
    )


class AudioObjectSnapshot(AudioObject):
    term = RdfTerm(
        "AudioObjectSnapshot", "http://schema.org/AudioObjectSnapshot", ["1.2-DRAFT"]
    )


class Audiobook(AudioObject, Book):
    term = RdfTerm(
        "Audiobook", "http://schema.org/Audiobook", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ImageObjectSnapshot(ImageObject):
    term = RdfTerm(
        "ImageObjectSnapshot", "http://schema.org/ImageObjectSnapshot", ["1.2-DRAFT"]
    )


class Barcode(ImageObject):
    term = RdfTerm(
        "Barcode", "http://schema.org/Barcode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ComicCoverArt(ComicStory, CoverArt):
    term = RdfTerm(
        "ComicCoverArt",
        "http://schema.org/ComicCoverArt",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MediaGallery(CollectionPage):
    term = RdfTerm(
        "MediaGallery", "http://schema.org/MediaGallery", ["1.1", "1.2-DRAFT"]
    )


class ReviewNewsArticle(CriticReview, NewsArticle):
    term = RdfTerm(
        "ReviewNewsArticle",
        "http://schema.org/ReviewNewsArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    term = RdfTerm(
        "WearableSizeGroupEnumeration",
        "http://schema.org/WearableSizeGroupEnumeration",
        ["1.2-DRAFT"],
    )


class USNonprofitType(NonprofitType):
    term = RdfTerm(
        "USNonprofitType", "http://schema.org/USNonprofitType", ["1.1", "1.2-DRAFT"]
    )


class UKNonprofitType(NonprofitType):
    term = RdfTerm(
        "UKNonprofitType", "http://schema.org/UKNonprofitType", ["1.1", "1.2-DRAFT"]
    )


class NLNonprofitType(NonprofitType):
    term = RdfTerm(
        "NLNonprofitType", "http://schema.org/NLNonprofitType", ["1.1", "1.2-DRAFT"]
    )


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm(
        "WearableMeasurementTypeEnumeration",
        "http://schema.org/WearableMeasurementTypeEnumeration",
        ["1.2-DRAFT"],
    )


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm(
        "BodyMeasurementTypeEnumeration",
        "http://schema.org/BodyMeasurementTypeEnumeration",
        ["1.2-DRAFT"],
    )


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    term = RdfTerm(
        "WearableSizeSystemEnumeration",
        "http://schema.org/WearableSizeSystemEnumeration",
        ["1.2-DRAFT"],
    )


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm(
        "EnergyStarEnergyEfficiencyEnumeration",
        "http://schema.org/EnergyStarEnergyEfficiencyEnumeration",
        ["1.1", "1.2-DRAFT"],
    )


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm(
        "EUEnergyEfficiencyEnumeration",
        "http://schema.org/EUEnergyEfficiencyEnumeration",
        ["1.1", "1.2-DRAFT"],
    )


class IPTCDigitalSourceEnumeration(MediaEnumeration):
    term = RdfTerm(
        "IPTCDigitalSourceEnumeration",
        "http://schema.org/IPTCDigitalSourceEnumeration",
        [],
    )


class PaymentStatusType(StatusEnumeration):
    term = RdfTerm(
        "PaymentStatusType",
        "http://schema.org/PaymentStatusType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OrderStatus(StatusEnumeration):
    term = RdfTerm(
        "OrderStatus",
        "http://schema.org/OrderStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EventStatusType(StatusEnumeration):
    term = RdfTerm(
        "EventStatusType",
        "http://schema.org/EventStatusType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ReservationStatusType(StatusEnumeration):
    term = RdfTerm(
        "ReservationStatusType",
        "http://schema.org/ReservationStatusType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LegalForceStatus(StatusEnumeration):
    term = RdfTerm(
        "LegalForceStatus",
        "http://schema.org/LegalForceStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ActionStatusType(StatusEnumeration):
    term = RdfTerm(
        "ActionStatusType",
        "http://schema.org/ActionStatusType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GameServerStatus(StatusEnumeration):
    term = RdfTerm(
        "GameServerStatus",
        "http://schema.org/GameServerStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalImagingTechnique(MedicalEnumeration):
    term = RdfTerm(
        "MedicalImagingTechnique",
        "http://schema.org/MedicalImagingTechnique",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrugCostCategory(MedicalEnumeration):
    term = RdfTerm(
        "DrugCostCategory",
        "http://schema.org/DrugCostCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicineSystem(MedicalEnumeration):
    term = RdfTerm(
        "MedicineSystem",
        "http://schema.org/MedicineSystem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrugPrescriptionStatus(MedicalEnumeration):
    term = RdfTerm(
        "DrugPrescriptionStatus",
        "http://schema.org/DrugPrescriptionStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalProcedureType(MedicalEnumeration):
    term = RdfTerm(
        "MedicalProcedureType",
        "http://schema.org/MedicalProcedureType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalTrialDesign(MedicalEnumeration):
    term = RdfTerm(
        "MedicalTrialDesign",
        "http://schema.org/MedicalTrialDesign",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalAudienceType(MedicalEnumeration):
    term = RdfTerm(
        "MedicalAudienceType",
        "http://schema.org/MedicalAudienceType",
        ["1.1", "1.2-DRAFT"],
    )


class MedicalObservationalStudyDesign(MedicalEnumeration):
    term = RdfTerm(
        "MedicalObservationalStudyDesign",
        "http://schema.org/MedicalObservationalStudyDesign",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalStudyStatus(MedicalEnumeration):
    term = RdfTerm(
        "MedicalStudyStatus",
        "http://schema.org/MedicalStudyStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InfectiousAgentClass(MedicalEnumeration):
    term = RdfTerm(
        "InfectiousAgentClass",
        "http://schema.org/InfectiousAgentClass",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PhysicalExam(MedicalProcedure, MedicalEnumeration):
    term = RdfTerm(
        "PhysicalExam",
        "http://schema.org/PhysicalExam",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalDevicePurpose(MedicalEnumeration):
    term = RdfTerm(
        "MedicalDevicePurpose",
        "http://schema.org/MedicalDevicePurpose",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalEvidenceLevel(MedicalEnumeration):
    term = RdfTerm(
        "MedicalEvidenceLevel",
        "http://schema.org/MedicalEvidenceLevel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DrugPregnancyCategory(MedicalEnumeration):
    term = RdfTerm(
        "DrugPregnancyCategory",
        "http://schema.org/DrugPregnancyCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SizeSpecification(QualitativeValue):
    term = RdfTerm(
        "SizeSpecification", "http://schema.org/SizeSpecification", ["1.2-DRAFT"]
    )


class SteeringPositionValue(QualitativeValue):
    term = RdfTerm(
        "SteeringPositionValue",
        "http://schema.org/SteeringPositionValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BedType(QualitativeValue):
    term = RdfTerm(
        "BedType", "http://schema.org/BedType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DriveWheelConfigurationValue(QualitativeValue):
    term = RdfTerm(
        "DriveWheelConfigurationValue",
        "http://schema.org/DriveWheelConfigurationValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalSpecialty(Specialty, MedicalEnumeration):
    term = RdfTerm(
        "MedicalSpecialty",
        "http://schema.org/MedicalSpecialty",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EmployeeRole(OrganizationRole):
    term = RdfTerm(
        "EmployeeRole",
        "http://schema.org/EmployeeRole",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HowToSupply(HowToItem):
    term = RdfTerm(
        "HowToSupply",
        "http://schema.org/HowToSupply",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HowToTool(HowToItem):
    term = RdfTerm(
        "HowToTool", "http://schema.org/HowToTool", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ParentAudience(PeopleAudience):
    term = RdfTerm(
        "ParentAudience",
        "http://schema.org/ParentAudience",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalAudience(Audience, PeopleAudience):
    term = RdfTerm(
        "MedicalAudience",
        "http://schema.org/MedicalAudience",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TVSeries(CreativeWorkSeries, CreativeWork):
    term = RdfTerm(
        "TVSeries", "http://schema.org/TVSeries", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BookSeries(CreativeWorkSeries):
    term = RdfTerm(
        "BookSeries", "http://schema.org/BookSeries", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Periodical(CreativeWorkSeries):
    term = RdfTerm(
        "Periodical", "http://schema.org/Periodical", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class VideoGameSeries(CreativeWorkSeries):
    term = RdfTerm(
        "VideoGameSeries",
        "http://schema.org/VideoGameSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MovieSeries(CreativeWorkSeries):
    term = RdfTerm(
        "MovieSeries",
        "http://schema.org/MovieSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PodcastSeries(CreativeWorkSeries):
    term = RdfTerm(
        "PodcastSeries", "http://schema.org/PodcastSeries", ["1.0", "1.1", "1.2-DRAFT"]
    )


class RadioSeries(CreativeWorkSeries):
    term = RdfTerm(
        "RadioSeries",
        "http://schema.org/RadioSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FMRadioChannel(RadioChannel):
    term = RdfTerm(
        "FMRadioChannel",
        "http://schema.org/FMRadioChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AMRadioChannel(RadioChannel):
    term = RdfTerm(
        "AMRadioChannel",
        "http://schema.org/AMRadioChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RadioBroadcastService(BroadcastService):
    term = RdfTerm(
        "RadioBroadcastService",
        "http://schema.org/RadioBroadcastService",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class CurrencyConversionService(FinancialProduct):
    term = RdfTerm(
        "CurrencyConversionService",
        "http://schema.org/CurrencyConversionService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PaymentService(PaymentMethod, FinancialProduct):
    term = RdfTerm(
        "PaymentService",
        "http://schema.org/PaymentService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PaymentCard(PaymentMethod, FinancialProduct):
    term = RdfTerm(
        "PaymentCard",
        "http://schema.org/PaymentCard",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BankAccount(FinancialProduct):
    term = RdfTerm(
        "BankAccount",
        "http://schema.org/BankAccount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LoanOrCredit(FinancialProduct):
    term = RdfTerm(
        "LoanOrCredit",
        "http://schema.org/LoanOrCredit",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InvestmentOrDeposit(FinancialProduct):
    term = RdfTerm(
        "InvestmentOrDeposit",
        "http://schema.org/InvestmentOrDeposit",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GeoCircle(GeoShape):
    term = RdfTerm(
        "GeoCircle", "http://schema.org/GeoCircle", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    term = RdfTerm(
        "MonetaryAmountDistribution",
        "http://schema.org/MonetaryAmountDistribution",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class LocationFeatureSpecification(PropertyValue):
    term = RdfTerm(
        "LocationFeatureSpecification",
        "http://schema.org/LocationFeatureSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Observation(QuantitativeValue, Intangible):
    term = RdfTerm(
        "Observation", "http://schema.org/Observation", ["1.0", "1.1", "1.2-DRAFT"]
    )


class PostalAddress(ContactPoint):
    term = RdfTerm(
        "PostalAddress",
        "http://schema.org/PostalAddress",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CompoundPriceSpecification(PriceSpecification):
    term = RdfTerm(
        "CompoundPriceSpecification",
        "http://schema.org/CompoundPriceSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PaymentChargeSpecification(PriceSpecification):
    term = RdfTerm(
        "PaymentChargeSpecification",
        "http://schema.org/PaymentChargeSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class UnitPriceSpecification(PriceSpecification):
    term = RdfTerm(
        "UnitPriceSpecification",
        "http://schema.org/UnitPriceSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DeliveryChargeSpecification(PriceSpecification):
    term = RdfTerm(
        "DeliveryChargeSpecification",
        "http://schema.org/DeliveryChargeSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MedicalCode(MedicalIntangible, CategoryCode):
    term = RdfTerm(
        "MedicalCode",
        "http://schema.org/MedicalCode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class EmployerAggregateRating(AggregateRating):
    term = RdfTerm(
        "EmployerAggregateRating",
        "http://schema.org/EmployerAggregateRating",
        ["1.0", "1.1", "1.2-DRAFT"],
    )


class SingleFamilyResidence(House):
    term = RdfTerm(
        "SingleFamilyResidence",
        "http://schema.org/SingleFamilyResidence",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MeetingRoom(Room):
    term = RdfTerm(
        "MeetingRoom",
        "http://schema.org/MeetingRoom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HotelRoom(Room):
    term = RdfTerm(
        "HotelRoom", "http://schema.org/HotelRoom", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Mosque(PlaceOfWorship):
    term = RdfTerm(
        "Mosque", "http://schema.org/Mosque", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Church(PlaceOfWorship):
    term = RdfTerm(
        "Church", "http://schema.org/Church", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BuddhistTemple(PlaceOfWorship):
    term = RdfTerm(
        "BuddhistTemple",
        "http://schema.org/BuddhistTemple",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Synagogue(PlaceOfWorship):
    term = RdfTerm(
        "Synagogue", "http://schema.org/Synagogue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class HinduTemple(PlaceOfWorship):
    term = RdfTerm(
        "HinduTemple",
        "http://schema.org/HinduTemple",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Preschool(EducationalOrganization):
    term = RdfTerm(
        "Preschool", "http://schema.org/Preschool", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ElementarySchool(EducationalOrganization):
    term = RdfTerm(
        "ElementarySchool",
        "http://schema.org/ElementarySchool",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class School(EducationalOrganization):
    term = RdfTerm(
        "School", "http://schema.org/School", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MiddleSchool(EducationalOrganization):
    term = RdfTerm(
        "MiddleSchool",
        "http://schema.org/MiddleSchool",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HighSchool(EducationalOrganization):
    term = RdfTerm(
        "HighSchool", "http://schema.org/HighSchool", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CollegeOrUniversity(EducationalOrganization):
    term = RdfTerm(
        "CollegeOrUniversity",
        "http://schema.org/CollegeOrUniversity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Embassy(GovernmentBuilding):
    term = RdfTerm(
        "Embassy", "http://schema.org/Embassy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DefenceEstablishment(GovernmentBuilding):
    term = RdfTerm(
        "DefenceEstablishment",
        "http://schema.org/DefenceEstablishment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class LegislativeBuilding(GovernmentBuilding):
    term = RdfTerm(
        "LegislativeBuilding",
        "http://schema.org/LegislativeBuilding",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Courthouse(GovernmentBuilding):
    term = RdfTerm(
        "Courthouse", "http://schema.org/Courthouse", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CityHall(GovernmentBuilding):
    term = RdfTerm(
        "CityHall", "http://schema.org/CityHall", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class LakeBodyOfWater(BodyOfWater):
    term = RdfTerm(
        "LakeBodyOfWater",
        "http://schema.org/LakeBodyOfWater",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OceanBodyOfWater(BodyOfWater):
    term = RdfTerm(
        "OceanBodyOfWater",
        "http://schema.org/OceanBodyOfWater",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Canal(BodyOfWater):
    term = RdfTerm(
        "Canal", "http://schema.org/Canal", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class RiverBodyOfWater(BodyOfWater):
    term = RdfTerm(
        "RiverBodyOfWater",
        "http://schema.org/RiverBodyOfWater",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SeaBodyOfWater(BodyOfWater):
    term = RdfTerm(
        "SeaBodyOfWater",
        "http://schema.org/SeaBodyOfWater",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Pond(BodyOfWater):
    term = RdfTerm("Pond", "http://schema.org/Pond", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Waterfall(BodyOfWater):
    term = RdfTerm(
        "Waterfall", "http://schema.org/Waterfall", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Reservoir(BodyOfWater):
    term = RdfTerm(
        "Reservoir", "http://schema.org/Reservoir", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Hostel(LodgingBusiness):
    term = RdfTerm(
        "Hostel", "http://schema.org/Hostel", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Motel(LodgingBusiness):
    term = RdfTerm(
        "Motel", "http://schema.org/Motel", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BedAndBreakfast(LodgingBusiness):
    term = RdfTerm(
        "BedAndBreakfast",
        "http://schema.org/BedAndBreakfast",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Resort(LodgingBusiness):
    term = RdfTerm(
        "Resort", "http://schema.org/Resort", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Campground(CivicStructure, LodgingBusiness):
    term = RdfTerm(
        "Campground", "http://schema.org/Campground", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class VacationRental(LodgingBusiness):
    term = RdfTerm("VacationRental", "http://schema.org/VacationRental", ["1.2-DRAFT"])


class Hotel(LodgingBusiness):
    term = RdfTerm(
        "Hotel", "http://schema.org/Hotel", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PoliceStation(CivicStructure, EmergencyService):
    term = RdfTerm(
        "PoliceStation",
        "http://schema.org/PoliceStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FireStation(CivicStructure, EmergencyService):
    term = RdfTerm(
        "FireStation",
        "http://schema.org/FireStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Hospital(EmergencyService, MedicalOrganization, CivicStructure):
    term = RdfTerm(
        "Hospital", "http://schema.org/Hospital", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Pharmacy(MedicalOrganization, MedicalBusiness):
    term = RdfTerm(
        "Pharmacy", "http://schema.org/Pharmacy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Dentist(LocalBusiness, MedicalBusiness, MedicalOrganization):
    term = RdfTerm(
        "Dentist", "http://schema.org/Dentist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Physician(MedicalOrganization, MedicalBusiness):
    term = RdfTerm(
        "Physician", "http://schema.org/Physician", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    term = RdfTerm(
        "MedicalClinic",
        "http://schema.org/MedicalClinic",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Psychiatric(MedicalBusiness):
    term = RdfTerm(
        "Psychiatric",
        "http://schema.org/Psychiatric",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Podiatric(MedicalBusiness):
    term = RdfTerm(
        "Podiatric", "http://schema.org/Podiatric", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PublicHealth(MedicalBusiness):
    term = RdfTerm(
        "PublicHealth",
        "http://schema.org/PublicHealth",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PlasticSurgery(MedicalBusiness):
    term = RdfTerm(
        "PlasticSurgery",
        "http://schema.org/PlasticSurgery",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DietNutrition(MedicalBusiness):
    term = RdfTerm(
        "DietNutrition",
        "http://schema.org/DietNutrition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Emergency(MedicalBusiness):
    term = RdfTerm(
        "Emergency", "http://schema.org/Emergency", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Oncologic(MedicalBusiness):
    term = RdfTerm(
        "Oncologic", "http://schema.org/Oncologic", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Gynecologic(MedicalBusiness):
    term = RdfTerm(
        "Gynecologic",
        "http://schema.org/Gynecologic",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Dermatology(MedicalBusiness):
    term = RdfTerm(
        "Dermatology",
        "http://schema.org/Dermatology",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Geriatric(MedicalBusiness):
    term = RdfTerm(
        "Geriatric", "http://schema.org/Geriatric", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Otolaryngologic(MedicalBusiness):
    term = RdfTerm(
        "Otolaryngologic",
        "http://schema.org/Otolaryngologic",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Physiotherapy(MedicalBusiness):
    term = RdfTerm(
        "Physiotherapy",
        "http://schema.org/Physiotherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PrimaryCare(MedicalBusiness):
    term = RdfTerm(
        "PrimaryCare",
        "http://schema.org/PrimaryCare",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Midwifery(MedicalBusiness):
    term = RdfTerm(
        "Midwifery", "http://schema.org/Midwifery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Obstetric(MedicalBusiness):
    term = RdfTerm(
        "Obstetric", "http://schema.org/Obstetric", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class CommunityHealth(MedicalBusiness):
    term = RdfTerm(
        "CommunityHealth",
        "http://schema.org/CommunityHealth",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Pediatric(MedicalBusiness):
    term = RdfTerm(
        "Pediatric", "http://schema.org/Pediatric", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Nursing(MedicalBusiness):
    term = RdfTerm(
        "Nursing", "http://schema.org/Nursing", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Optometric(MedicalBusiness):
    term = RdfTerm(
        "Optometric", "http://schema.org/Optometric", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Optician(MedicalBusiness):
    term = RdfTerm(
        "Optician", "http://schema.org/Optician", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Restaurant(FoodEstablishment):
    term = RdfTerm(
        "Restaurant", "http://schema.org/Restaurant", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BarOrPub(FoodEstablishment):
    term = RdfTerm(
        "BarOrPub", "http://schema.org/BarOrPub", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Distillery(FoodEstablishment):
    term = RdfTerm(
        "Distillery", "http://schema.org/Distillery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Brewery(FoodEstablishment):
    term = RdfTerm(
        "Brewery", "http://schema.org/Brewery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class FastFoodRestaurant(FoodEstablishment):
    term = RdfTerm(
        "FastFoodRestaurant",
        "http://schema.org/FastFoodRestaurant",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class IceCreamShop(FoodEstablishment):
    term = RdfTerm(
        "IceCreamShop",
        "http://schema.org/IceCreamShop",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CafeOrCoffeeShop(FoodEstablishment):
    term = RdfTerm(
        "CafeOrCoffeeShop",
        "http://schema.org/CafeOrCoffeeShop",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Bakery(FoodEstablishment):
    term = RdfTerm(
        "Bakery", "http://schema.org/Bakery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Winery(FoodEstablishment):
    term = RdfTerm(
        "Winery", "http://schema.org/Winery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class GasStation(AutomotiveBusiness):
    term = RdfTerm(
        "GasStation", "http://schema.org/GasStation", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class AutoBodyShop(AutomotiveBusiness):
    term = RdfTerm(
        "AutoBodyShop",
        "http://schema.org/AutoBodyShop",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AutoDealer(AutomotiveBusiness):
    term = RdfTerm(
        "AutoDealer", "http://schema.org/AutoDealer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class AutoRental(AutomotiveBusiness):
    term = RdfTerm(
        "AutoRental", "http://schema.org/AutoRental", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class AutoRepair(AutomotiveBusiness):
    term = RdfTerm(
        "AutoRepair", "http://schema.org/AutoRepair", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MotorcycleRepair(AutomotiveBusiness):
    term = RdfTerm(
        "MotorcycleRepair",
        "http://schema.org/MotorcycleRepair",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AutoWash(AutomotiveBusiness):
    term = RdfTerm(
        "AutoWash", "http://schema.org/AutoWash", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MotorcycleDealer(AutomotiveBusiness):
    term = RdfTerm(
        "MotorcycleDealer",
        "http://schema.org/MotorcycleDealer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HairSalon(HealthAndBeautyBusiness):
    term = RdfTerm(
        "HairSalon", "http://schema.org/HairSalon", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TattooParlor(HealthAndBeautyBusiness):
    term = RdfTerm(
        "TattooParlor",
        "http://schema.org/TattooParlor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class NailSalon(HealthAndBeautyBusiness):
    term = RdfTerm(
        "NailSalon", "http://schema.org/NailSalon", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BeautySalon(HealthAndBeautyBusiness):
    term = RdfTerm(
        "BeautySalon",
        "http://schema.org/BeautySalon",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DaySpa(HealthAndBeautyBusiness):
    term = RdfTerm(
        "DaySpa", "http://schema.org/DaySpa", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Notary(LegalService):
    term = RdfTerm(
        "Notary", "http://schema.org/Notary", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Attorney(LegalService):
    term = RdfTerm(
        "Attorney", "http://schema.org/Attorney", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OfficeEquipmentStore(Store):
    term = RdfTerm(
        "OfficeEquipmentStore",
        "http://schema.org/OfficeEquipmentStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MensClothingStore(Store):
    term = RdfTerm(
        "MensClothingStore",
        "http://schema.org/MensClothingStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ClothingStore(Store):
    term = RdfTerm(
        "ClothingStore",
        "http://schema.org/ClothingStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AutoPartsStore(Store, AutomotiveBusiness):
    term = RdfTerm(
        "AutoPartsStore",
        "http://schema.org/AutoPartsStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PawnShop(Store):
    term = RdfTerm(
        "PawnShop", "http://schema.org/PawnShop", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class GroceryStore(Store):
    term = RdfTerm(
        "GroceryStore",
        "http://schema.org/GroceryStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class OutletStore(Store):
    term = RdfTerm(
        "OutletStore",
        "http://schema.org/OutletStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class FurnitureStore(Store):
    term = RdfTerm(
        "FurnitureStore",
        "http://schema.org/FurnitureStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class JewelryStore(Store):
    term = RdfTerm(
        "JewelryStore",
        "http://schema.org/JewelryStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ToyStore(Store):
    term = RdfTerm(
        "ToyStore", "http://schema.org/ToyStore", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class LiquorStore(Store):
    term = RdfTerm(
        "LiquorStore",
        "http://schema.org/LiquorStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PetStore(Store):
    term = RdfTerm(
        "PetStore", "http://schema.org/PetStore", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ConvenienceStore(Store):
    term = RdfTerm(
        "ConvenienceStore",
        "http://schema.org/ConvenienceStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Florist(Store):
    term = RdfTerm(
        "Florist", "http://schema.org/Florist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class SportingGoodsStore(Store):
    term = RdfTerm(
        "SportingGoodsStore",
        "http://schema.org/SportingGoodsStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ElectronicsStore(Store):
    term = RdfTerm(
        "ElectronicsStore",
        "http://schema.org/ElectronicsStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BikeStore(Store):
    term = RdfTerm(
        "BikeStore", "http://schema.org/BikeStore", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BookStore(Store):
    term = RdfTerm(
        "BookStore", "http://schema.org/BookStore", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ComputerStore(Store):
    term = RdfTerm(
        "ComputerStore",
        "http://schema.org/ComputerStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MusicStore(Store):
    term = RdfTerm(
        "MusicStore", "http://schema.org/MusicStore", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class WholesaleStore(Store):
    term = RdfTerm(
        "WholesaleStore",
        "http://schema.org/WholesaleStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HomeGoodsStore(Store):
    term = RdfTerm(
        "HomeGoodsStore",
        "http://schema.org/HomeGoodsStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class TireShop(Store):
    term = RdfTerm(
        "TireShop", "http://schema.org/TireShop", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class GardenStore(Store):
    term = RdfTerm(
        "GardenStore",
        "http://schema.org/GardenStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DepartmentStore(Store):
    term = RdfTerm(
        "DepartmentStore",
        "http://schema.org/DepartmentStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HobbyShop(Store):
    term = RdfTerm(
        "HobbyShop", "http://schema.org/HobbyShop", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class HardwareStore(Store):
    term = RdfTerm(
        "HardwareStore",
        "http://schema.org/HardwareStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MobilePhoneStore(Store):
    term = RdfTerm(
        "MobilePhoneStore",
        "http://schema.org/MobilePhoneStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MovieRentalStore(Store):
    term = RdfTerm(
        "MovieRentalStore",
        "http://schema.org/MovieRentalStore",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ShoeStore(Store):
    term = RdfTerm(
        "ShoeStore", "http://schema.org/ShoeStore", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class StadiumOrArena(SportsActivityLocation, CivicStructure):
    term = RdfTerm(
        "StadiumOrArena",
        "http://schema.org/StadiumOrArena",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    term = RdfTerm(
        "HealthClub", "http://schema.org/HealthClub", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class SportsClub(SportsActivityLocation):
    term = RdfTerm(
        "SportsClub", "http://schema.org/SportsClub", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BowlingAlley(SportsActivityLocation):
    term = RdfTerm(
        "BowlingAlley",
        "http://schema.org/BowlingAlley",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PublicSwimmingPool(SportsActivityLocation):
    term = RdfTerm(
        "PublicSwimmingPool",
        "http://schema.org/PublicSwimmingPool",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ExerciseGym(SportsActivityLocation):
    term = RdfTerm(
        "ExerciseGym",
        "http://schema.org/ExerciseGym",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GolfCourse(SportsActivityLocation):
    term = RdfTerm(
        "GolfCourse", "http://schema.org/GolfCourse", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class TennisComplex(SportsActivityLocation):
    term = RdfTerm(
        "TennisComplex",
        "http://schema.org/TennisComplex",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PostOffice(GovernmentOffice):
    term = RdfTerm(
        "PostOffice", "http://schema.org/PostOffice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class BankOrCreditUnion(FinancialService):
    term = RdfTerm(
        "BankOrCreditUnion",
        "http://schema.org/BankOrCreditUnion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InsuranceAgency(FinancialService):
    term = RdfTerm(
        "InsuranceAgency",
        "http://schema.org/InsuranceAgency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AccountingService(FinancialService):
    term = RdfTerm(
        "AccountingService",
        "http://schema.org/AccountingService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AutomatedTeller(FinancialService):
    term = RdfTerm(
        "AutomatedTeller",
        "http://schema.org/AutomatedTeller",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HousePainter(HomeAndConstructionBusiness):
    term = RdfTerm(
        "HousePainter",
        "http://schema.org/HousePainter",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Locksmith(HomeAndConstructionBusiness):
    term = RdfTerm(
        "Locksmith", "http://schema.org/Locksmith", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class RoofingContractor(HomeAndConstructionBusiness):
    term = RdfTerm(
        "RoofingContractor",
        "http://schema.org/RoofingContractor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class GeneralContractor(HomeAndConstructionBusiness):
    term = RdfTerm(
        "GeneralContractor",
        "http://schema.org/GeneralContractor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class MovingCompany(HomeAndConstructionBusiness):
    term = RdfTerm(
        "MovingCompany",
        "http://schema.org/MovingCompany",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class HVACBusiness(HomeAndConstructionBusiness):
    term = RdfTerm(
        "HVACBusiness",
        "http://schema.org/HVACBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Electrician(HomeAndConstructionBusiness):
    term = RdfTerm(
        "Electrician",
        "http://schema.org/Electrician",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Plumber(HomeAndConstructionBusiness):
    term = RdfTerm(
        "Plumber", "http://schema.org/Plumber", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class NightClub(EntertainmentBusiness):
    term = RdfTerm(
        "NightClub", "http://schema.org/NightClub", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MovieTheater(EntertainmentBusiness, CivicStructure):
    term = RdfTerm(
        "MovieTheater",
        "http://schema.org/MovieTheater",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AdultEntertainment(EntertainmentBusiness):
    term = RdfTerm(
        "AdultEntertainment",
        "http://schema.org/AdultEntertainment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ArtGallery(EntertainmentBusiness):
    term = RdfTerm(
        "ArtGallery", "http://schema.org/ArtGallery", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class AmusementPark(EntertainmentBusiness):
    term = RdfTerm(
        "AmusementPark",
        "http://schema.org/AmusementPark",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Casino(EntertainmentBusiness):
    term = RdfTerm(
        "Casino", "http://schema.org/Casino", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ComedyClub(EntertainmentBusiness):
    term = RdfTerm(
        "ComedyClub", "http://schema.org/ComedyClub", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class PrependAction(InsertAction):
    term = RdfTerm(
        "PrependAction",
        "http://schema.org/PrependAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class AppendAction(InsertAction):
    term = RdfTerm(
        "AppendAction",
        "http://schema.org/AppendAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ConfirmAction(InformAction):
    term = RdfTerm(
        "ConfirmAction",
        "http://schema.org/ConfirmAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RsvpAction(InformAction):
    term = RdfTerm(
        "RsvpAction", "http://schema.org/RsvpAction", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class OccupationalTherapy(MedicalTherapy):
    term = RdfTerm(
        "OccupationalTherapy",
        "http://schema.org/OccupationalTherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PalliativeProcedure(MedicalTherapy, MedicalProcedure):
    term = RdfTerm(
        "PalliativeProcedure",
        "http://schema.org/PalliativeProcedure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PhysicalTherapy(MedicalTherapy):
    term = RdfTerm(
        "PhysicalTherapy",
        "http://schema.org/PhysicalTherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RadiationTherapy(MedicalTherapy):
    term = RdfTerm(
        "RadiationTherapy",
        "http://schema.org/RadiationTherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RespiratoryTherapy(MedicalTherapy):
    term = RdfTerm(
        "RespiratoryTherapy",
        "http://schema.org/RespiratoryTherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class VitalSign(MedicalSign):
    term = RdfTerm(
        "VitalSign", "http://schema.org/VitalSign", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class LiveBlogPosting(BlogPosting):
    term = RdfTerm(
        "LiveBlogPosting",
        "http://schema.org/LiveBlogPosting",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class ImageGallery(MediaGallery):
    term = RdfTerm(
        "ImageGallery",
        "http://schema.org/ImageGallery",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class VideoGallery(MediaGallery):
    term = RdfTerm(
        "VideoGallery",
        "http://schema.org/VideoGallery",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class Patient(MedicalAudience, Person):
    term = RdfTerm(
        "Patient", "http://schema.org/Patient", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Newspaper(Periodical):
    term = RdfTerm(
        "Newspaper", "http://schema.org/Newspaper", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class ComicSeries(Periodical):
    term = RdfTerm(
        "ComicSeries",
        "http://schema.org/ComicSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CreditCard(PaymentCard, LoanOrCredit):
    term = RdfTerm(
        "CreditCard", "http://schema.org/CreditCard", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class MortgageLoan(LoanOrCredit):
    term = RdfTerm(
        "MortgageLoan",
        "http://schema.org/MortgageLoan",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class DepositAccount(BankAccount, InvestmentOrDeposit):
    term = RdfTerm(
        "DepositAccount",
        "http://schema.org/DepositAccount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class InvestmentFund(InvestmentOrDeposit):
    term = RdfTerm(
        "InvestmentFund",
        "http://schema.org/InvestmentFund",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class BrokerageAccount(InvestmentOrDeposit):
    term = RdfTerm(
        "BrokerageAccount",
        "http://schema.org/BrokerageAccount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class CatholicChurch(Church):
    term = RdfTerm(
        "CatholicChurch",
        "http://schema.org/CatholicChurch",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class SkiResort(Resort, SportsActivityLocation):
    term = RdfTerm(
        "SkiResort", "http://schema.org/SkiResort", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class IndividualPhysician(Physician):
    term = RdfTerm("IndividualPhysician", "http://schema.org/IndividualPhysician", [])


class PhysiciansOffice(Physician):
    term = RdfTerm("PhysiciansOffice", "http://schema.org/PhysiciansOffice", [])


class CovidTestingFacility(MedicalClinic):
    term = RdfTerm(
        "CovidTestingFacility",
        "http://schema.org/CovidTestingFacility",
        ["1.1", "1.2-DRAFT"],
    )


@dataclass(frozen=True)
class paymentMethodType(RdfProperty):
    term = RdfTerm("paymentMethodType", "http://schema.org/paymentMethodType", [])
    object: schemaorg.PaymentMethodType


@dataclass(frozen=True)
class event(RdfProperty):
    term = RdfTerm(
        "event", "http://schema.org/event", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class maxValue(RdfProperty):
    term = RdfTerm(
        "maxValue", "http://schema.org/maxValue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class mileageFromOdometer(RdfProperty):
    term = RdfTerm(
        "mileageFromOdometer",
        "http://schema.org/mileageFromOdometer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class doorTime(RdfProperty):
    term = RdfTerm(
        "doorTime", "http://schema.org/doorTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Time | DateTime


@dataclass(frozen=True)
class contentUrl(RdfProperty):
    term = RdfTerm(
        "contentUrl", "http://schema.org/contentUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class sibling(RdfProperty):
    term = RdfTerm(
        "sibling", "http://schema.org/sibling", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class offersPrescriptionByMail(RdfProperty):
    term = RdfTerm(
        "offersPrescriptionByMail",
        "http://schema.org/offersPrescriptionByMail",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class reviewRating(RdfProperty):
    term = RdfTerm(
        "reviewRating",
        "http://schema.org/reviewRating",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Rating


@dataclass(frozen=True)
class reviewCount(RdfProperty):
    term = RdfTerm(
        "reviewCount",
        "http://schema.org/reviewCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class hasProductReturnPolicy(RdfProperty):
    term = RdfTerm(
        "hasProductReturnPolicy",
        "http://schema.org/hasProductReturnPolicy",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ProductReturnPolicy


@dataclass(frozen=True)
class fuelCapacity(RdfProperty):
    term = RdfTerm(
        "fuelCapacity",
        "http://schema.org/fuelCapacity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class howPerformed(RdfProperty):
    term = RdfTerm(
        "howPerformed",
        "http://schema.org/howPerformed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class productReturnLink(RdfProperty):
    term = RdfTerm(
        "productReturnLink",
        "http://schema.org/productReturnLink",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class childMinAge(RdfProperty):
    term = RdfTerm(
        "childMinAge",
        "http://schema.org/childMinAge",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class printSection(RdfProperty):
    term = RdfTerm(
        "printSection",
        "http://schema.org/printSection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class departureAirport(RdfProperty):
    term = RdfTerm(
        "departureAirport",
        "http://schema.org/departureAirport",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Airport


@dataclass(frozen=True)
class productID(RdfProperty):
    term = RdfTerm(
        "productID", "http://schema.org/productID", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class inverseOf(RdfProperty):
    term = RdfTerm(
        "inverseOf", "http://schema.org/inverseOf", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Property


@dataclass(frozen=True)
class name(RdfProperty):
    term = RdfTerm("name", "http://schema.org/name", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class unnamedSourcesPolicy(RdfProperty):
    term = RdfTerm(
        "unnamedSourcesPolicy",
        "http://schema.org/unnamedSourcesPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class playerType(RdfProperty):
    term = RdfTerm(
        "playerType", "http://schema.org/playerType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class knows(RdfProperty):
    term = RdfTerm(
        "knows", "http://schema.org/knows", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class isicV4(RdfProperty):
    term = RdfTerm(
        "isicV4", "http://schema.org/isicV4", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class fundedItem(RdfProperty):
    term = RdfTerm(
        "fundedItem", "http://schema.org/fundedItem", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: (
        schemaorg.Product
        | schemaorg.Person
        | schemaorg.MedicalEntity
        | schemaorg.BioChemEntity
        | schemaorg.Organization
        | schemaorg.Event
        | schemaorg.CreativeWork
    )


@dataclass(frozen=True)
class legislationIdentifier(RdfProperty):
    term = RdfTerm(
        "legislationIdentifier",
        "http://schema.org/legislationIdentifier",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class loanTerm(RdfProperty):
    term = RdfTerm(
        "loanTerm", "http://schema.org/loanTerm", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class provider(RdfProperty):
    term = RdfTerm(
        "provider", "http://schema.org/provider", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class physicalRequirement(RdfProperty):
    term = RdfTerm(
        "physicalRequirement",
        "http://schema.org/physicalRequirement",
        ["1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DefinedTerm | URL


@dataclass(frozen=True)
class applicationContact(RdfProperty):
    term = RdfTerm(
        "applicationContact",
        "http://schema.org/applicationContact",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPoint


@dataclass(frozen=True)
class drugClass(RdfProperty):
    term = RdfTerm(
        "drugClass", "http://schema.org/drugClass", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.DrugClass


@dataclass(frozen=True)
class endDate(RdfProperty):
    term = RdfTerm(
        "endDate", "http://schema.org/endDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime | Date


@dataclass(frozen=True)
class certificationIdentification(RdfProperty):
    term = RdfTerm(
        "certificationIdentification",
        "http://schema.org/certificationIdentification",
        [],
    )
    object: schemaorg.DefinedTerm | Text


@dataclass(frozen=True)
class resultReview(RdfProperty):
    term = RdfTerm(
        "resultReview",
        "http://schema.org/resultReview",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Review


@dataclass(frozen=True)
class vehicleTransmission(RdfProperty):
    term = RdfTerm(
        "vehicleTransmission",
        "http://schema.org/vehicleTransmission",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QualitativeValue | URL | Text


@dataclass(frozen=True)
class responsibilities(RdfProperty):
    term = RdfTerm(
        "responsibilities",
        "http://schema.org/responsibilities",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class nationality(RdfProperty):
    term = RdfTerm(
        "nationality",
        "http://schema.org/nationality",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Country


@dataclass(frozen=True)
class relatedDrug(RdfProperty):
    term = RdfTerm(
        "relatedDrug",
        "http://schema.org/relatedDrug",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Drug


@dataclass(frozen=True)
class diagram(RdfProperty):
    term = RdfTerm(
        "diagram", "http://schema.org/diagram", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ImageObject


@dataclass(frozen=True)
class photos(RdfProperty):
    term = RdfTerm(
        "photos", "http://schema.org/photos", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ImageObject | schemaorg.Photograph


@dataclass(frozen=True)
class downPayment(RdfProperty):
    term = RdfTerm(
        "downPayment",
        "http://schema.org/downPayment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.MonetaryAmount


@dataclass(frozen=True)
class usesDevice(RdfProperty):
    term = RdfTerm(
        "usesDevice", "http://schema.org/usesDevice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalDevice


@dataclass(frozen=True)
class warrantyScope(RdfProperty):
    term = RdfTerm(
        "warrantyScope",
        "http://schema.org/warrantyScope",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.WarrantyScope


@dataclass(frozen=True)
class parentService(RdfProperty):
    term = RdfTerm(
        "parentService",
        "http://schema.org/parentService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BroadcastService


@dataclass(frozen=True)
class bodyType(RdfProperty):
    term = RdfTerm(
        "bodyType", "http://schema.org/bodyType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QualitativeValue | URL | Text


@dataclass(frozen=True)
class actionProcess(RdfProperty):
    term = RdfTerm("actionProcess", "http://schema.org/actionProcess", [])
    object: schemaorg.HowTo


@dataclass(frozen=True)
class educationRequirements(RdfProperty):
    term = RdfTerm(
        "educationRequirements",
        "http://schema.org/educationRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.EducationalOccupationalCredential


@dataclass(frozen=True)
class commentTime(RdfProperty):
    term = RdfTerm(
        "commentTime",
        "http://schema.org/commentTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date | DateTime


@dataclass(frozen=True)
class coursePrerequisites(RdfProperty):
    term = RdfTerm(
        "coursePrerequisites",
        "http://schema.org/coursePrerequisites",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Course | Text | schemaorg.AlignmentObject


@dataclass(frozen=True)
class honorificPrefix(RdfProperty):
    term = RdfTerm(
        "honorificPrefix",
        "http://schema.org/honorificPrefix",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class priceValidUntil(RdfProperty):
    term = RdfTerm(
        "priceValidUntil",
        "http://schema.org/priceValidUntil",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class siblings(RdfProperty):
    term = RdfTerm(
        "siblings", "http://schema.org/siblings", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class recipe(RdfProperty):
    term = RdfTerm(
        "recipe", "http://schema.org/recipe", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Recipe


@dataclass(frozen=True)
class minPrice(RdfProperty):
    term = RdfTerm(
        "minPrice", "http://schema.org/minPrice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class yearsInOperation(RdfProperty):
    term = RdfTerm(
        "yearsInOperation",
        "http://schema.org/yearsInOperation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class petsAllowed(RdfProperty):
    term = RdfTerm(
        "petsAllowed",
        "http://schema.org/petsAllowed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean | Text


@dataclass(frozen=True)
class bioChemSimilarity(RdfProperty):
    term = RdfTerm(
        "bioChemSimilarity", "http://schema.org/bioChemSimilarity", ["1.2-DRAFT"]
    )
    object: schemaorg.BioChemEntity


@dataclass(frozen=True)
class aggregateRating(RdfProperty):
    term = RdfTerm(
        "aggregateRating",
        "http://schema.org/aggregateRating",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AggregateRating


@dataclass(frozen=True)
class hasEnergyEfficiencyCategory(RdfProperty):
    term = RdfTerm(
        "hasEnergyEfficiencyCategory",
        "http://schema.org/hasEnergyEfficiencyCategory",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EnergyEfficiencyEnumeration


@dataclass(frozen=True)
class alcoholWarning(RdfProperty):
    term = RdfTerm(
        "alcoholWarning",
        "http://schema.org/alcoholWarning",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class totalHistoricalEnrollment(RdfProperty):
    term = RdfTerm(
        "totalHistoricalEnrollment",
        "http://schema.org/totalHistoricalEnrollment",
        ["1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class colleague(RdfProperty):
    term = RdfTerm(
        "colleague", "http://schema.org/colleague", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.Person


@dataclass(frozen=True)
class permittedUsage(RdfProperty):
    term = RdfTerm(
        "permittedUsage",
        "http://schema.org/permittedUsage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class expectsAcceptanceOf(RdfProperty):
    term = RdfTerm(
        "expectsAcceptanceOf",
        "http://schema.org/expectsAcceptanceOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Offer


@dataclass(frozen=True)
class citation(RdfProperty):
    term = RdfTerm(
        "citation", "http://schema.org/citation", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.CreativeWork


@dataclass(frozen=True)
class locationCreated(RdfProperty):
    term = RdfTerm(
        "locationCreated",
        "http://schema.org/locationCreated",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class tourBookingPage(RdfProperty):
    term = RdfTerm(
        "tourBookingPage", "http://schema.org/tourBookingPage", ["1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class replyToUrl(RdfProperty):
    term = RdfTerm(
        "replyToUrl", "http://schema.org/replyToUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class sdPublisher(RdfProperty):
    term = RdfTerm(
        "sdPublisher", "http://schema.org/sdPublisher", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class programMembershipUsed(RdfProperty):
    term = RdfTerm(
        "programMembershipUsed",
        "http://schema.org/programMembershipUsed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ProgramMembership


@dataclass(frozen=True)
class totalPrice(RdfProperty):
    term = RdfTerm(
        "totalPrice", "http://schema.org/totalPrice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | Text | schemaorg.PriceSpecification


@dataclass(frozen=True)
class eligibleQuantity(RdfProperty):
    term = RdfTerm(
        "eligibleQuantity",
        "http://schema.org/eligibleQuantity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class antagonist(RdfProperty):
    term = RdfTerm(
        "antagonist", "http://schema.org/antagonist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Muscle


@dataclass(frozen=True)
class thumbnail(RdfProperty):
    term = RdfTerm(
        "thumbnail", "http://schema.org/thumbnail", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ImageObject


@dataclass(frozen=True)
class passengerSequenceNumber(RdfProperty):
    term = RdfTerm(
        "passengerSequenceNumber",
        "http://schema.org/passengerSequenceNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class vehicleInteriorColor(RdfProperty):
    term = RdfTerm(
        "vehicleInteriorColor",
        "http://schema.org/vehicleInteriorColor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class circle(RdfProperty):
    term = RdfTerm(
        "circle", "http://schema.org/circle", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class missionCoveragePrioritiesPolicy(RdfProperty):
    term = RdfTerm(
        "missionCoveragePrioritiesPolicy",
        "http://schema.org/missionCoveragePrioritiesPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class containedInPlace(RdfProperty):
    term = RdfTerm(
        "containedInPlace",
        "http://schema.org/containedInPlace",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class hasCertification(RdfProperty):
    term = RdfTerm("hasCertification", "http://schema.org/hasCertification", [])
    object: schemaorg.Certification


@dataclass(frozen=True)
class phoneticText(RdfProperty):
    term = RdfTerm(
        "phoneticText", "http://schema.org/phoneticText", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class isSimilarTo(RdfProperty):
    term = RdfTerm(
        "isSimilarTo",
        "http://schema.org/isSimilarTo",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Product | schemaorg.Service


@dataclass(frozen=True)
class videoFrameSize(RdfProperty):
    term = RdfTerm(
        "videoFrameSize",
        "http://schema.org/videoFrameSize",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class fuelConsumption(RdfProperty):
    term = RdfTerm(
        "fuelConsumption",
        "http://schema.org/fuelConsumption",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class yearlyRevenue(RdfProperty):
    term = RdfTerm(
        "yearlyRevenue",
        "http://schema.org/yearlyRevenue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class steps(RdfProperty):
    term = RdfTerm(
        "steps", "http://schema.org/steps", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.ItemList | schemaorg.CreativeWork


@dataclass(frozen=True)
class browserRequirements(RdfProperty):
    term = RdfTerm(
        "browserRequirements",
        "http://schema.org/browserRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class paymentMethod(RdfProperty):
    term = RdfTerm(
        "paymentMethod",
        "http://schema.org/paymentMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PaymentMethod | Text


@dataclass(frozen=True)
class hasRepresentation(RdfProperty):
    term = RdfTerm(
        "hasRepresentation", "http://schema.org/hasRepresentation", ["1.2-DRAFT"]
    )
    object: schemaorg.PropertyValue | URL | Text


@dataclass(frozen=True)
class carrierRequirements(RdfProperty):
    term = RdfTerm(
        "carrierRequirements",
        "http://schema.org/carrierRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class distribution(RdfProperty):
    term = RdfTerm(
        "distribution",
        "http://schema.org/distribution",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DataDownload


@dataclass(frozen=True)
class benefits(RdfProperty):
    term = RdfTerm(
        "benefits", "http://schema.org/benefits", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class variablesMeasured(RdfProperty):
    term = RdfTerm(
        "variablesMeasured",
        "http://schema.org/variablesMeasured",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.PropertyValue


@dataclass(frozen=True)
class educationalCredentialAwarded(RdfProperty):
    term = RdfTerm(
        "educationalCredentialAwarded",
        "http://schema.org/educationalCredentialAwarded",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EducationalOccupationalCredential | Text | URL


@dataclass(frozen=True)
class engineDisplacement(RdfProperty):
    term = RdfTerm(
        "engineDisplacement",
        "http://schema.org/engineDisplacement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class tripOrigin(RdfProperty):
    term = RdfTerm("tripOrigin", "http://schema.org/tripOrigin", ["1.2-DRAFT"])
    object: schemaorg.Place


@dataclass(frozen=True)
class programmingLanguage(RdfProperty):
    term = RdfTerm(
        "programmingLanguage",
        "http://schema.org/programmingLanguage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ComputerLanguage | Text


@dataclass(frozen=True)
class incentiveType(RdfProperty):
    term = RdfTerm("incentiveType", "http://schema.org/incentiveType", [])
    object: schemaorg.IncentiveType


@dataclass(frozen=True)
class holdingArchive(RdfProperty):
    term = RdfTerm(
        "holdingArchive",
        "http://schema.org/holdingArchive",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ArchiveOrganization


@dataclass(frozen=True)
class breastfeedingWarning(RdfProperty):
    term = RdfTerm(
        "breastfeedingWarning",
        "http://schema.org/breastfeedingWarning",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class exchangeRateSpread(RdfProperty):
    term = RdfTerm(
        "exchangeRateSpread",
        "http://schema.org/exchangeRateSpread",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.MonetaryAmount


@dataclass(frozen=True)
class colorSwatch(RdfProperty):
    term = RdfTerm("colorSwatch", "http://schema.org/colorSwatch", [])
    object: URL | schemaorg.ImageObject


@dataclass(frozen=True)
class geoMidpoint(RdfProperty):
    term = RdfTerm(
        "geoMidpoint",
        "http://schema.org/geoMidpoint",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.GeoCoordinates


@dataclass(frozen=True)
class numberOfBeds(RdfProperty):
    term = RdfTerm(
        "numberOfBeds",
        "http://schema.org/numberOfBeds",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class evidenceOrigin(RdfProperty):
    term = RdfTerm(
        "evidenceOrigin",
        "http://schema.org/evidenceOrigin",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class availableFrom(RdfProperty):
    term = RdfTerm(
        "availableFrom",
        "http://schema.org/availableFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class _yield(RdfProperty):
    term = RdfTerm(
        "yield", "http://schema.org/yield", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class pageEnd(RdfProperty):
    term = RdfTerm(
        "pageEnd", "http://schema.org/pageEnd", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer | Text


@dataclass(frozen=True)
class numberOfBathroomsTotal(RdfProperty):
    term = RdfTerm(
        "numberOfBathroomsTotal",
        "http://schema.org/numberOfBathroomsTotal",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class productionDate(RdfProperty):
    term = RdfTerm(
        "productionDate",
        "http://schema.org/productionDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class publicationType(RdfProperty):
    term = RdfTerm(
        "publicationType",
        "http://schema.org/publicationType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class parent(RdfProperty):
    term = RdfTerm(
        "parent", "http://schema.org/parent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class accessModeSufficient(RdfProperty):
    term = RdfTerm(
        "accessModeSufficient",
        "http://schema.org/accessModeSufficient",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ItemList


@dataclass(frozen=True)
class answerExplanation(RdfProperty):
    term = RdfTerm(
        "answerExplanation", "http://schema.org/answerExplanation", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Comment | schemaorg.WebContent


@dataclass(frozen=True)
class skills(RdfProperty):
    term = RdfTerm(
        "skills", "http://schema.org/skills", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class availableService(RdfProperty):
    term = RdfTerm(
        "availableService",
        "http://schema.org/availableService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: (
        schemaorg.MedicalTest | schemaorg.MedicalTherapy | schemaorg.MedicalProcedure
    )


@dataclass(frozen=True)
class requiredQuantity(RdfProperty):
    term = RdfTerm(
        "requiredQuantity",
        "http://schema.org/requiredQuantity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class publishingPrinciples(RdfProperty):
    term = RdfTerm(
        "publishingPrinciples",
        "http://schema.org/publishingPrinciples",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class contactlessPayment(RdfProperty):
    term = RdfTerm(
        "contactlessPayment",
        "http://schema.org/contactlessPayment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class album(RdfProperty):
    term = RdfTerm(
        "album", "http://schema.org/album", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicAlbum


@dataclass(frozen=True)
class applicationSubCategory(RdfProperty):
    term = RdfTerm(
        "applicationSubCategory",
        "http://schema.org/applicationSubCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class floorLimit(RdfProperty):
    term = RdfTerm(
        "floorLimit", "http://schema.org/floorLimit", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class birthPlace(RdfProperty):
    term = RdfTerm(
        "birthPlace", "http://schema.org/birthPlace", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class numConstraints(RdfProperty):
    term = RdfTerm(
        "numConstraints",
        "http://schema.org/numConstraints",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class floorSize(RdfProperty):
    term = RdfTerm(
        "floorSize", "http://schema.org/floorSize", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class polygon(RdfProperty):
    term = RdfTerm(
        "polygon", "http://schema.org/polygon", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class suggestedAge(RdfProperty):
    term = RdfTerm("suggestedAge", "http://schema.org/suggestedAge", ["1.2-DRAFT"])
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class audienceType(RdfProperty):
    term = RdfTerm(
        "audienceType",
        "http://schema.org/audienceType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class gameAvailabilityType(RdfProperty):
    term = RdfTerm(
        "gameAvailabilityType", "http://schema.org/gameAvailabilityType", ["1.2-DRAFT"]
    )
    object: Text | schemaorg.GameAvailabilityEnumeration


@dataclass(frozen=True)
class addressRegion(RdfProperty):
    term = RdfTerm(
        "addressRegion",
        "http://schema.org/addressRegion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class countryOfAssembly(RdfProperty):
    term = RdfTerm(
        "countryOfAssembly", "http://schema.org/countryOfAssembly", ["1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class vehicleSpecialUsage(RdfProperty):
    term = RdfTerm(
        "vehicleSpecialUsage",
        "http://schema.org/vehicleSpecialUsage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CarUsageType | Text


@dataclass(frozen=True)
class seasons(RdfProperty):
    term = RdfTerm(
        "seasons", "http://schema.org/seasons", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWorkSeason


@dataclass(frozen=True)
class cvdNumTotBeds(RdfProperty):
    term = RdfTerm(
        "cvdNumTotBeds", "http://schema.org/cvdNumTotBeds", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class releaseOf(RdfProperty):
    term = RdfTerm(
        "releaseOf", "http://schema.org/releaseOf", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicAlbum


@dataclass(frozen=True)
class itemDefectReturnLabelSource(RdfProperty):
    term = RdfTerm(
        "itemDefectReturnLabelSource",
        "http://schema.org/itemDefectReturnLabelSource",
        ["1.2-DRAFT"],
    )
    object: schemaorg.ReturnLabelSourceEnumeration


@dataclass(frozen=True)
class inLanguage(RdfProperty):
    term = RdfTerm(
        "inLanguage", "http://schema.org/inLanguage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.Language


@dataclass(frozen=True)
class abstract(RdfProperty):
    term = RdfTerm(
        "abstract", "http://schema.org/abstract", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class itemListElement(RdfProperty):
    term = RdfTerm(
        "itemListElement",
        "http://schema.org/itemListElement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing | Text | schemaorg.ListItem


@dataclass(frozen=True)
class startTime(RdfProperty):
    term = RdfTerm(
        "startTime", "http://schema.org/startTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Time | DateTime


@dataclass(frozen=True)
class associatedMediaReview(RdfProperty):
    term = RdfTerm(
        "associatedMediaReview",
        "http://schema.org/associatedMediaReview",
        ["1.2-DRAFT"],
    )
    object: schemaorg.Review


@dataclass(frozen=True)
class eligibleRegion(RdfProperty):
    term = RdfTerm(
        "eligibleRegion",
        "http://schema.org/eligibleRegion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.GeoShape | schemaorg.Place


@dataclass(frozen=True)
class molecularWeight(RdfProperty):
    term = RdfTerm(
        "molecularWeight", "http://schema.org/molecularWeight", ["1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | Text


@dataclass(frozen=True)
class valueMinLength(RdfProperty):
    term = RdfTerm(
        "valueMinLength",
        "http://schema.org/valueMinLength",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class affectedBy(RdfProperty):
    term = RdfTerm(
        "affectedBy", "http://schema.org/affectedBy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Drug


@dataclass(frozen=True)
class recordingOf(RdfProperty):
    term = RdfTerm(
        "recordingOf",
        "http://schema.org/recordingOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MusicComposition


@dataclass(frozen=True)
class availabilityStarts(RdfProperty):
    term = RdfTerm(
        "availabilityStarts",
        "http://schema.org/availabilityStarts",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Time | DateTime | Date


@dataclass(frozen=True)
class issueNumber(RdfProperty):
    term = RdfTerm(
        "issueNumber",
        "http://schema.org/issueNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer | Text


@dataclass(frozen=True)
class codeSampleType(RdfProperty):
    term = RdfTerm(
        "codeSampleType",
        "http://schema.org/codeSampleType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class inker(RdfProperty):
    term = RdfTerm(
        "inker", "http://schema.org/inker", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class geoIntersects(RdfProperty):
    term = RdfTerm(
        "geoIntersects", "http://schema.org/geoIntersects", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.GeospatialGeometry | schemaorg.Place


@dataclass(frozen=True)
class mainEntityOfPage(RdfProperty):
    term = RdfTerm(
        "mainEntityOfPage",
        "http://schema.org/mainEntityOfPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class associatedReview(RdfProperty):
    term = RdfTerm(
        "associatedReview", "http://schema.org/associatedReview", ["1.2-DRAFT"]
    )
    object: schemaorg.Review


@dataclass(frozen=True)
class flightDistance(RdfProperty):
    term = RdfTerm(
        "flightDistance",
        "http://schema.org/flightDistance",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Distance | Text


@dataclass(frozen=True)
class infectiousAgentClass(RdfProperty):
    term = RdfTerm(
        "infectiousAgentClass",
        "http://schema.org/infectiousAgentClass",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.InfectiousAgentClass


@dataclass(frozen=True)
class hasBioChemEntityPart(RdfProperty):
    term = RdfTerm(
        "hasBioChemEntityPart", "http://schema.org/hasBioChemEntityPart", ["1.2-DRAFT"]
    )
    object: schemaorg.BioChemEntity


@dataclass(frozen=True)
class returnPolicyCountry(RdfProperty):
    term = RdfTerm(
        "returnPolicyCountry", "http://schema.org/returnPolicyCountry", ["1.2-DRAFT"]
    )
    object: Text | schemaorg.Country


@dataclass(frozen=True)
class eventSchedule(RdfProperty):
    term = RdfTerm(
        "eventSchedule",
        "http://schema.org/eventSchedule",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Schedule


@dataclass(frozen=True)
class countryOfOrigin(RdfProperty):
    term = RdfTerm(
        "countryOfOrigin",
        "http://schema.org/countryOfOrigin",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Country


@dataclass(frozen=True)
class numAdults(RdfProperty):
    term = RdfTerm(
        "numAdults", "http://schema.org/numAdults", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class hasPOS(RdfProperty):
    term = RdfTerm(
        "hasPOS", "http://schema.org/hasPOS", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class suggestedMinAge(RdfProperty):
    term = RdfTerm(
        "suggestedMinAge",
        "http://schema.org/suggestedMinAge",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class shippingLabel(RdfProperty):
    term = RdfTerm(
        "shippingLabel", "http://schema.org/shippingLabel", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class ratingValue(RdfProperty):
    term = RdfTerm(
        "ratingValue",
        "http://schema.org/ratingValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | Text


@dataclass(frozen=True)
class numberOfBedrooms(RdfProperty):
    term = RdfTerm(
        "numberOfBedrooms", "http://schema.org/numberOfBedrooms", ["1.1", "1.2-DRAFT"]
    )
    object: Number | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class customerRemorseReturnLabelSource(RdfProperty):
    term = RdfTerm(
        "customerRemorseReturnLabelSource",
        "http://schema.org/customerRemorseReturnLabelSource",
        ["1.2-DRAFT"],
    )
    object: schemaorg.ReturnLabelSourceEnumeration


@dataclass(frozen=True)
class webFeed(RdfProperty):
    term = RdfTerm("webFeed", "http://schema.org/webFeed", ["1.0", "1.1", "1.2-DRAFT"])
    object: URL | schemaorg.DataFeed


@dataclass(frozen=True)
class functionalClass(RdfProperty):
    term = RdfTerm(
        "functionalClass",
        "http://schema.org/functionalClass",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEntity | Text


@dataclass(frozen=True)
class legislationJurisdiction(RdfProperty):
    term = RdfTerm(
        "legislationJurisdiction",
        "http://schema.org/legislationJurisdiction",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.AdministrativeArea


@dataclass(frozen=True)
class numItems(RdfProperty):
    term = RdfTerm("numItems", "http://schema.org/numItems", [])
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class employmentType(RdfProperty):
    term = RdfTerm(
        "employmentType",
        "http://schema.org/employmentType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class contentLocation(RdfProperty):
    term = RdfTerm(
        "contentLocation",
        "http://schema.org/contentLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class speakable(RdfProperty):
    term = RdfTerm(
        "speakable", "http://schema.org/speakable", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.SpeakableSpecification | URL


@dataclass(frozen=True)
class valueReference(RdfProperty):
    term = RdfTerm(
        "valueReference",
        "http://schema.org/valueReference",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: (
        Text
        | schemaorg.PropertyValue
        | schemaorg.MeasurementTypeEnumeration
        | schemaorg.DefinedTerm
        | schemaorg.QuantitativeValue
        | schemaorg.Enumeration
        | schemaorg.StructuredValue
        | schemaorg.QualitativeValue
    )


@dataclass(frozen=True)
class knowsAbout(RdfProperty):
    term = RdfTerm(
        "knowsAbout", "http://schema.org/knowsAbout", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing | Text | URL


@dataclass(frozen=True)
class urlTemplate(RdfProperty):
    term = RdfTerm(
        "urlTemplate",
        "http://schema.org/urlTemplate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class ownedFrom(RdfProperty):
    term = RdfTerm(
        "ownedFrom", "http://schema.org/ownedFrom", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime


@dataclass(frozen=True)
class endorsers(RdfProperty):
    term = RdfTerm(
        "endorsers", "http://schema.org/endorsers", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class actionStatus(RdfProperty):
    term = RdfTerm(
        "actionStatus",
        "http://schema.org/actionStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ActionStatusType


@dataclass(frozen=True)
class firstPerformance(RdfProperty):
    term = RdfTerm(
        "firstPerformance",
        "http://schema.org/firstPerformance",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class experienceInPlaceOfEducation(RdfProperty):
    term = RdfTerm(
        "experienceInPlaceOfEducation",
        "http://schema.org/experienceInPlaceOfEducation",
        ["1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class incomeLimit(RdfProperty):
    term = RdfTerm("incomeLimit", "http://schema.org/incomeLimit", [])
    object: schemaorg.MonetaryAmount | Text


@dataclass(frozen=True)
class liveBlogUpdate(RdfProperty):
    term = RdfTerm(
        "liveBlogUpdate",
        "http://schema.org/liveBlogUpdate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BlogPosting


@dataclass(frozen=True)
class gameEdition(RdfProperty):
    term = RdfTerm("gameEdition", "http://schema.org/gameEdition", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class dateModified(RdfProperty):
    term = RdfTerm(
        "dateModified",
        "http://schema.org/dateModified",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime | Date


@dataclass(frozen=True)
class billingIncrement(RdfProperty):
    term = RdfTerm(
        "billingIncrement",
        "http://schema.org/billingIncrement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class stepValue(RdfProperty):
    term = RdfTerm(
        "stepValue", "http://schema.org/stepValue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class monoisotopicMolecularWeight(RdfProperty):
    term = RdfTerm(
        "monoisotopicMolecularWeight",
        "http://schema.org/monoisotopicMolecularWeight",
        ["1.2-DRAFT"],
    )
    object: Text | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class hasTierBenefit(RdfProperty):
    term = RdfTerm("hasTierBenefit", "http://schema.org/hasTierBenefit", [])
    object: schemaorg.TierBenefitEnumeration


@dataclass(frozen=True)
class departureTime(RdfProperty):
    term = RdfTerm(
        "departureTime",
        "http://schema.org/departureTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Time | DateTime


@dataclass(frozen=True)
class sku(RdfProperty):
    term = RdfTerm("sku", "http://schema.org/sku", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class legislationEnsuresImplementationOf(RdfProperty):
    term = RdfTerm(
        "legislationEnsuresImplementationOf",
        "http://schema.org/legislationEnsuresImplementationOf",
        [],
    )
    object: schemaorg.Legislation


@dataclass(frozen=True)
class studySubject(RdfProperty):
    term = RdfTerm(
        "studySubject",
        "http://schema.org/studySubject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEntity


@dataclass(frozen=True)
class containsPlace(RdfProperty):
    term = RdfTerm(
        "containsPlace",
        "http://schema.org/containsPlace",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class telephone(RdfProperty):
    term = RdfTerm(
        "telephone", "http://schema.org/telephone", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class hasDigitalDocumentPermission(RdfProperty):
    term = RdfTerm(
        "hasDigitalDocumentPermission",
        "http://schema.org/hasDigitalDocumentPermission",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DigitalDocumentPermission


@dataclass(frozen=True)
class purchasePriceLimit(RdfProperty):
    term = RdfTerm("purchasePriceLimit", "http://schema.org/purchasePriceLimit", [])
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class usageInfo(RdfProperty):
    term = RdfTerm("usageInfo", "http://schema.org/usageInfo", ["1.1", "1.2-DRAFT"])
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class availableLanguage(RdfProperty):
    term = RdfTerm(
        "availableLanguage",
        "http://schema.org/availableLanguage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.Language


@dataclass(frozen=True)
class artist(RdfProperty):
    term = RdfTerm(
        "artist", "http://schema.org/artist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class geoOverlaps(RdfProperty):
    term = RdfTerm(
        "geoOverlaps", "http://schema.org/geoOverlaps", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place | schemaorg.GeospatialGeometry


@dataclass(frozen=True)
class hasCategoryCode(RdfProperty):
    term = RdfTerm(
        "hasCategoryCode",
        "http://schema.org/hasCategoryCode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CategoryCode


@dataclass(frozen=True)
class priceSpecification(RdfProperty):
    term = RdfTerm(
        "priceSpecification",
        "http://schema.org/priceSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PriceSpecification


@dataclass(frozen=True)
class mapType(RdfProperty):
    term = RdfTerm(
        "mapType", "http://schema.org/mapType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MapCategoryType


@dataclass(frozen=True)
class regionDrained(RdfProperty):
    term = RdfTerm(
        "regionDrained",
        "http://schema.org/regionDrained",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem


@dataclass(frozen=True)
class originatesFrom(RdfProperty):
    term = RdfTerm(
        "originatesFrom",
        "http://schema.org/originatesFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Vessel


@dataclass(frozen=True)
class workHours(RdfProperty):
    term = RdfTerm(
        "workHours", "http://schema.org/workHours", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class incentivizedItem(RdfProperty):
    term = RdfTerm("incentivizedItem", "http://schema.org/incentivizedItem", [])
    object: schemaorg.DefinedTerm | schemaorg.Product


@dataclass(frozen=True)
class checkoutTime(RdfProperty):
    term = RdfTerm(
        "checkoutTime",
        "http://schema.org/checkoutTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Time | DateTime


@dataclass(frozen=True)
class jurisdiction(RdfProperty):
    term = RdfTerm(
        "jurisdiction", "http://schema.org/jurisdiction", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.AdministrativeArea | Text


@dataclass(frozen=True)
class attendees(RdfProperty):
    term = RdfTerm(
        "attendees", "http://schema.org/attendees", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class eligibleCustomerType(RdfProperty):
    term = RdfTerm(
        "eligibleCustomerType",
        "http://schema.org/eligibleCustomerType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BusinessEntityType


@dataclass(frozen=True)
class departureStation(RdfProperty):
    term = RdfTerm(
        "departureStation",
        "http://schema.org/departureStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.TrainStation


@dataclass(frozen=True)
class datePosted(RdfProperty):
    term = RdfTerm(
        "datePosted", "http://schema.org/datePosted", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime | Date


@dataclass(frozen=True)
class vendor(RdfProperty):
    term = RdfTerm(
        "vendor", "http://schema.org/vendor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class warrantyPromise(RdfProperty):
    term = RdfTerm(
        "warrantyPromise",
        "http://schema.org/warrantyPromise",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.WarrantyPromise


@dataclass(frozen=True)
class numberOfForwardGears(RdfProperty):
    term = RdfTerm(
        "numberOfForwardGears",
        "http://schema.org/numberOfForwardGears",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class fuelEfficiency(RdfProperty):
    term = RdfTerm(
        "fuelEfficiency",
        "http://schema.org/fuelEfficiency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class letterer(RdfProperty):
    term = RdfTerm(
        "letterer", "http://schema.org/letterer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class issuedThrough(RdfProperty):
    term = RdfTerm(
        "issuedThrough",
        "http://schema.org/issuedThrough",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Service


@dataclass(frozen=True)
class dosageForm(RdfProperty):
    term = RdfTerm(
        "dosageForm", "http://schema.org/dosageForm", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class scheduledPaymentDate(RdfProperty):
    term = RdfTerm(
        "scheduledPaymentDate",
        "http://schema.org/scheduledPaymentDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class entertainmentBusiness(RdfProperty):
    term = RdfTerm(
        "entertainmentBusiness",
        "http://schema.org/entertainmentBusiness",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EntertainmentBusiness


@dataclass(frozen=True)
class season(RdfProperty):
    term = RdfTerm(
        "season", "http://schema.org/season", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.CreativeWorkSeason


@dataclass(frozen=True)
class durationOfWarranty(RdfProperty):
    term = RdfTerm(
        "durationOfWarranty",
        "http://schema.org/durationOfWarranty",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class includesAttraction(RdfProperty):
    term = RdfTerm(
        "includesAttraction",
        "http://schema.org/includesAttraction",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.TouristAttraction


@dataclass(frozen=True)
class vehicleModelDate(RdfProperty):
    term = RdfTerm(
        "vehicleModelDate",
        "http://schema.org/vehicleModelDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class structuralClass(RdfProperty):
    term = RdfTerm(
        "structuralClass",
        "http://schema.org/structuralClass",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class hasMerchantReturnPolicy(RdfProperty):
    term = RdfTerm(
        "hasMerchantReturnPolicy",
        "http://schema.org/hasMerchantReturnPolicy",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MerchantReturnPolicy


@dataclass(frozen=True)
class maxPrice(RdfProperty):
    term = RdfTerm(
        "maxPrice", "http://schema.org/maxPrice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class colorist(RdfProperty):
    term = RdfTerm(
        "colorist", "http://schema.org/colorist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class shippingRate(RdfProperty):
    term = RdfTerm(
        "shippingRate", "http://schema.org/shippingRate", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ShippingRateSettings | schemaorg.MonetaryAmount


@dataclass(frozen=True)
class procedure(RdfProperty):
    term = RdfTerm(
        "procedure", "http://schema.org/procedure", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class cvdFacilityCounty(RdfProperty):
    term = RdfTerm(
        "cvdFacilityCounty", "http://schema.org/cvdFacilityCounty", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class expectedPrognosis(RdfProperty):
    term = RdfTerm(
        "expectedPrognosis",
        "http://schema.org/expectedPrognosis",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class validForMemberTier(RdfProperty):
    term = RdfTerm("validForMemberTier", "http://schema.org/validForMemberTier", [])
    object: schemaorg.MemberProgramTier


@dataclass(frozen=True)
class borrower(RdfProperty):
    term = RdfTerm(
        "borrower", "http://schema.org/borrower", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class availability(RdfProperty):
    term = RdfTerm(
        "availability",
        "http://schema.org/availability",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ItemAvailability


@dataclass(frozen=True)
class servingSize(RdfProperty):
    term = RdfTerm(
        "servingSize",
        "http://schema.org/servingSize",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class sdDatePublished(RdfProperty):
    term = RdfTerm(
        "sdDatePublished",
        "http://schema.org/sdDatePublished",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class dateline(RdfProperty):
    term = RdfTerm(
        "dateline", "http://schema.org/dateline", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class arrivalPlatform(RdfProperty):
    term = RdfTerm(
        "arrivalPlatform",
        "http://schema.org/arrivalPlatform",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class courseMode(RdfProperty):
    term = RdfTerm(
        "courseMode", "http://schema.org/courseMode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | Text


@dataclass(frozen=True)
class object(RdfProperty):
    term = RdfTerm(
        "object", "http://schema.org/object", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class highPrice(RdfProperty):
    term = RdfTerm(
        "highPrice", "http://schema.org/highPrice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | Number


@dataclass(frozen=True)
class hospitalAffiliation(RdfProperty):
    term = RdfTerm(
        "hospitalAffiliation",
        "http://schema.org/hospitalAffiliation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Hospital


@dataclass(frozen=True)
class specialty(RdfProperty):
    term = RdfTerm(
        "specialty", "http://schema.org/specialty", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Specialty


@dataclass(frozen=True)
class measurementDenominator(RdfProperty):
    term = RdfTerm(
        "measurementDenominator",
        "http://schema.org/measurementDenominator",
        ["1.2-DRAFT"],
    )
    object: schemaorg.StatisticalVariable


@dataclass(frozen=True)
class imagingTechnique(RdfProperty):
    term = RdfTerm(
        "imagingTechnique",
        "http://schema.org/imagingTechnique",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalImagingTechnique


@dataclass(frozen=True)
class includedRiskFactor(RdfProperty):
    term = RdfTerm(
        "includedRiskFactor",
        "http://schema.org/includedRiskFactor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalRiskFactor


@dataclass(frozen=True)
class broadcastFrequency(RdfProperty):
    term = RdfTerm(
        "broadcastFrequency",
        "http://schema.org/broadcastFrequency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.BroadcastFrequencySpecification


@dataclass(frozen=True)
class isAvailableGenerically(RdfProperty):
    term = RdfTerm(
        "isAvailableGenerically",
        "http://schema.org/isAvailableGenerically",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class numberOfFullBathrooms(RdfProperty):
    term = RdfTerm(
        "numberOfFullBathrooms",
        "http://schema.org/numberOfFullBathrooms",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class percentile25(RdfProperty):
    term = RdfTerm(
        "percentile25", "http://schema.org/percentile25", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class subtitleLanguage(RdfProperty):
    term = RdfTerm(
        "subtitleLanguage",
        "http://schema.org/subtitleLanguage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.Language


@dataclass(frozen=True)
class availableChannel(RdfProperty):
    term = RdfTerm(
        "availableChannel",
        "http://schema.org/availableChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ServiceChannel


@dataclass(frozen=True)
class iswcCode(RdfProperty):
    term = RdfTerm(
        "iswcCode", "http://schema.org/iswcCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class encodesBioChemEntity(RdfProperty):
    term = RdfTerm(
        "encodesBioChemEntity", "http://schema.org/encodesBioChemEntity", ["1.2-DRAFT"]
    )
    object: schemaorg.BioChemEntity


@dataclass(frozen=True)
class inventoryLevel(RdfProperty):
    term = RdfTerm(
        "inventoryLevel",
        "http://schema.org/inventoryLevel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class accommodationFloorPlan(RdfProperty):
    term = RdfTerm(
        "accommodationFloorPlan",
        "http://schema.org/accommodationFloorPlan",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.FloorPlan


@dataclass(frozen=True)
class hasDeliveryMethod(RdfProperty):
    term = RdfTerm(
        "hasDeliveryMethod",
        "http://schema.org/hasDeliveryMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DeliveryMethod


@dataclass(frozen=True)
class servicePhone(RdfProperty):
    term = RdfTerm(
        "servicePhone",
        "http://schema.org/servicePhone",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPoint


@dataclass(frozen=True)
class trainNumber(RdfProperty):
    term = RdfTerm(
        "trainNumber",
        "http://schema.org/trainNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class numberOfEmployees(RdfProperty):
    term = RdfTerm(
        "numberOfEmployees",
        "http://schema.org/numberOfEmployees",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class healthcareReportingData(RdfProperty):
    term = RdfTerm(
        "healthcareReportingData",
        "http://schema.org/healthcareReportingData",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CDCPMDRecord | schemaorg.Dataset


@dataclass(frozen=True)
class acrissCode(RdfProperty):
    term = RdfTerm(
        "acrissCode", "http://schema.org/acrissCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class applicantLocationRequirements(RdfProperty):
    term = RdfTerm(
        "applicantLocationRequirements",
        "http://schema.org/applicantLocationRequirements",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AdministrativeArea


@dataclass(frozen=True)
class archiveHeld(RdfProperty):
    term = RdfTerm(
        "archiveHeld", "http://schema.org/archiveHeld", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ArchiveComponent


@dataclass(frozen=True)
class paymentStatus(RdfProperty):
    term = RdfTerm(
        "paymentStatus",
        "http://schema.org/paymentStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PaymentStatusType | Text


@dataclass(frozen=True)
class occupationLocation(RdfProperty):
    term = RdfTerm(
        "occupationLocation",
        "http://schema.org/occupationLocation",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AdministrativeArea


@dataclass(frozen=True)
class includesHealthPlanNetwork(RdfProperty):
    term = RdfTerm(
        "includesHealthPlanNetwork",
        "http://schema.org/includesHealthPlanNetwork",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.HealthPlanNetwork


@dataclass(frozen=True)
class itemLocation(RdfProperty):
    term = RdfTerm(
        "itemLocation", "http://schema.org/itemLocation", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place | schemaorg.PostalAddress | Text


@dataclass(frozen=True)
class clipNumber(RdfProperty):
    term = RdfTerm(
        "clipNumber", "http://schema.org/clipNumber", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer | Text


@dataclass(frozen=True)
class eligibleDuration(RdfProperty):
    term = RdfTerm(
        "eligibleDuration",
        "http://schema.org/eligibleDuration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class observationDate(RdfProperty):
    term = RdfTerm(
        "observationDate",
        "http://schema.org/observationDate",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class tocContinuation(RdfProperty):
    term = RdfTerm(
        "tocContinuation", "http://schema.org/tocContinuation", ["1.2-DRAFT"]
    )
    object: schemaorg.HyperTocEntry


@dataclass(frozen=True)
class archivedAt(RdfProperty):
    term = RdfTerm("archivedAt", "http://schema.org/archivedAt", ["1.2-DRAFT"])
    object: URL | schemaorg.WebPage


@dataclass(frozen=True)
class weight(RdfProperty):
    term = RdfTerm(
        "weight", "http://schema.org/weight", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | schemaorg.Mass


@dataclass(frozen=True)
class byMonthWeek(RdfProperty):
    term = RdfTerm("byMonthWeek", "http://schema.org/byMonthWeek", ["1.1", "1.2-DRAFT"])
    object: Integer


@dataclass(frozen=True)
class inDefinedTermSet(RdfProperty):
    term = RdfTerm(
        "inDefinedTermSet",
        "http://schema.org/inDefinedTermSet",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DefinedTermSet | URL


@dataclass(frozen=True)
class includedInHealthInsurancePlan(RdfProperty):
    term = RdfTerm(
        "includedInHealthInsurancePlan",
        "http://schema.org/includedInHealthInsurancePlan",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.HealthInsurancePlan


@dataclass(frozen=True)
class byDay(RdfProperty):
    term = RdfTerm(
        "byDay", "http://schema.org/byDay", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.DayOfWeek


@dataclass(frozen=True)
class line(RdfProperty):
    term = RdfTerm("line", "http://schema.org/line", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class vehicleEngine(RdfProperty):
    term = RdfTerm(
        "vehicleEngine",
        "http://schema.org/vehicleEngine",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EngineSpecification


@dataclass(frozen=True)
class branchOf(RdfProperty):
    term = RdfTerm(
        "branchOf", "http://schema.org/branchOf", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class expectedArrivalUntil(RdfProperty):
    term = RdfTerm(
        "expectedArrivalUntil",
        "http://schema.org/expectedArrivalUntil",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime | Date


@dataclass(frozen=True)
class originalMediaLink(RdfProperty):
    term = RdfTerm(
        "originalMediaLink", "http://schema.org/originalMediaLink", ["1.2-DRAFT"]
    )
    object: schemaorg.MediaObject | URL | schemaorg.WebPage


@dataclass(frozen=True)
class printColumn(RdfProperty):
    term = RdfTerm(
        "printColumn",
        "http://schema.org/printColumn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class trainingSalary(RdfProperty):
    term = RdfTerm(
        "trainingSalary",
        "http://schema.org/trainingSalary",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmountDistribution


@dataclass(frozen=True)
class typeOfBed(RdfProperty):
    term = RdfTerm(
        "typeOfBed", "http://schema.org/typeOfBed", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.BedType | Text


@dataclass(frozen=True)
class percentile75(RdfProperty):
    term = RdfTerm(
        "percentile75", "http://schema.org/percentile75", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class credentialCategory(RdfProperty):
    term = RdfTerm(
        "credentialCategory",
        "http://schema.org/credentialCategory",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DefinedTerm | URL | Text


@dataclass(frozen=True)
class eventStatus(RdfProperty):
    term = RdfTerm(
        "eventStatus",
        "http://schema.org/eventStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EventStatusType


@dataclass(frozen=True)
class medicalSpecialty(RdfProperty):
    term = RdfTerm(
        "medicalSpecialty",
        "http://schema.org/medicalSpecialty",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalSpecialty


@dataclass(frozen=True)
class returnShippingFeesAmount(RdfProperty):
    term = RdfTerm(
        "returnShippingFeesAmount",
        "http://schema.org/returnShippingFeesAmount",
        ["1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class healthPlanCostSharing(RdfProperty):
    term = RdfTerm(
        "healthPlanCostSharing",
        "http://schema.org/healthPlanCostSharing",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class customerRemorseReturnShippingFeesAmount(RdfProperty):
    term = RdfTerm(
        "customerRemorseReturnShippingFeesAmount",
        "http://schema.org/customerRemorseReturnShippingFeesAmount",
        ["1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class interactionCount(RdfProperty):
    term = RdfTerm(
        "interactionCount",
        "http://schema.org/interactionCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class billingAddress(RdfProperty):
    term = RdfTerm(
        "billingAddress",
        "http://schema.org/billingAddress",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PostalAddress


@dataclass(frozen=True)
class countriesNotSupported(RdfProperty):
    term = RdfTerm(
        "countriesNotSupported",
        "http://schema.org/countriesNotSupported",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class shippingDetails(RdfProperty):
    term = RdfTerm(
        "shippingDetails", "http://schema.org/shippingDetails", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.OfferShippingDetails


@dataclass(frozen=True)
class employees(RdfProperty):
    term = RdfTerm(
        "employees", "http://schema.org/employees", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class mpn(RdfProperty):
    term = RdfTerm("mpn", "http://schema.org/mpn", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class lesser(RdfProperty):
    term = RdfTerm(
        "lesser", "http://schema.org/lesser", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QualitativeValue


@dataclass(frozen=True)
class byMonth(RdfProperty):
    term = RdfTerm(
        "byMonth", "http://schema.org/byMonth", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer


@dataclass(frozen=True)
class loanRepaymentForm(RdfProperty):
    term = RdfTerm(
        "loanRepaymentForm",
        "http://schema.org/loanRepaymentForm",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.RepaymentSpecification


@dataclass(frozen=True)
class hasGS1DigitalLink(RdfProperty):
    term = RdfTerm("hasGS1DigitalLink", "http://schema.org/hasGS1DigitalLink", [])
    object: URL


@dataclass(frozen=True)
class ownershipFundingInfo(RdfProperty):
    term = RdfTerm(
        "ownershipFundingInfo",
        "http://schema.org/ownershipFundingInfo",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.AboutPage | schemaorg.CreativeWork | Text


@dataclass(frozen=True)
class mediaAuthenticityCategory(RdfProperty):
    term = RdfTerm(
        "mediaAuthenticityCategory",
        "http://schema.org/mediaAuthenticityCategory",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MediaManipulationRatingEnumeration


@dataclass(frozen=True)
class unsaturatedFatContent(RdfProperty):
    term = RdfTerm(
        "unsaturatedFatContent",
        "http://schema.org/unsaturatedFatContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class lastReviewed(RdfProperty):
    term = RdfTerm(
        "lastReviewed",
        "http://schema.org/lastReviewed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class workTranslation(RdfProperty):
    term = RdfTerm(
        "workTranslation",
        "http://schema.org/workTranslation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class partOfTrip(RdfProperty):
    term = RdfTerm(
        "partOfTrip", "http://schema.org/partOfTrip", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Trip


@dataclass(frozen=True)
class numberOfDoors(RdfProperty):
    term = RdfTerm(
        "numberOfDoors",
        "http://schema.org/numberOfDoors",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class preOp(RdfProperty):
    term = RdfTerm(
        "preOp", "http://schema.org/preOp", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class backstory(RdfProperty):
    term = RdfTerm(
        "backstory", "http://schema.org/backstory", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.CreativeWork


@dataclass(frozen=True)
class verificationFactCheckingPolicy(RdfProperty):
    term = RdfTerm(
        "verificationFactCheckingPolicy",
        "http://schema.org/verificationFactCheckingPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork | URL


@dataclass(frozen=True)
class url(RdfProperty):
    term = RdfTerm("url", "http://schema.org/url", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: URL


@dataclass(frozen=True)
class error(RdfProperty):
    term = RdfTerm(
        "error", "http://schema.org/error", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class sdLicense(RdfProperty):
    term = RdfTerm(
        "sdLicense", "http://schema.org/sdLicense", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class legislationRepeals(RdfProperty):
    term = RdfTerm("legislationRepeals", "http://schema.org/legislationRepeals", [])
    object: schemaorg.Legislation


@dataclass(frozen=True)
class catalog(RdfProperty):
    term = RdfTerm(
        "catalog", "http://schema.org/catalog", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.DataCatalog


@dataclass(frozen=True)
class embeddedTextCaption(RdfProperty):
    term = RdfTerm(
        "embeddedTextCaption", "http://schema.org/embeddedTextCaption", ["1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class educationalAlignment(RdfProperty):
    term = RdfTerm(
        "educationalAlignment",
        "http://schema.org/educationalAlignment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AlignmentObject


@dataclass(frozen=True)
class drainsTo(RdfProperty):
    term = RdfTerm(
        "drainsTo", "http://schema.org/drainsTo", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Vessel


@dataclass(frozen=True)
class editor(RdfProperty):
    term = RdfTerm(
        "editor", "http://schema.org/editor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class uploadDate(RdfProperty):
    term = RdfTerm(
        "uploadDate", "http://schema.org/uploadDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date | DateTime


@dataclass(frozen=True)
class gameItem(RdfProperty):
    term = RdfTerm(
        "gameItem", "http://schema.org/gameItem", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class legislationConsolidates(RdfProperty):
    term = RdfTerm(
        "legislationConsolidates",
        "http://schema.org/legislationConsolidates",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Legislation


@dataclass(frozen=True)
class interactionType(RdfProperty):
    term = RdfTerm(
        "interactionType",
        "http://schema.org/interactionType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Action


@dataclass(frozen=True)
class securityClearanceRequirement(RdfProperty):
    term = RdfTerm(
        "securityClearanceRequirement",
        "http://schema.org/securityClearanceRequirement",
        ["1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class salaryUponCompletion(RdfProperty):
    term = RdfTerm(
        "salaryUponCompletion",
        "http://schema.org/salaryUponCompletion",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmountDistribution


@dataclass(frozen=True)
class hoursAvailable(RdfProperty):
    term = RdfTerm(
        "hoursAvailable",
        "http://schema.org/hoursAvailable",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OpeningHoursSpecification


@dataclass(frozen=True)
class numberOfPreviousOwners(RdfProperty):
    term = RdfTerm(
        "numberOfPreviousOwners",
        "http://schema.org/numberOfPreviousOwners",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class legalStatus(RdfProperty):
    term = RdfTerm(
        "legalStatus",
        "http://schema.org/legalStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DrugLegalStatus | schemaorg.MedicalEnumeration


@dataclass(frozen=True)
class downloadUrl(RdfProperty):
    term = RdfTerm(
        "downloadUrl",
        "http://schema.org/downloadUrl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class valueName(RdfProperty):
    term = RdfTerm(
        "valueName", "http://schema.org/valueName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class partOfSystem(RdfProperty):
    term = RdfTerm(
        "partOfSystem",
        "http://schema.org/partOfSystem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalSystem


@dataclass(frozen=True)
class inCodeSet(RdfProperty):
    term = RdfTerm(
        "inCodeSet", "http://schema.org/inCodeSet", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CategoryCodeSet | URL


@dataclass(frozen=True)
class license(RdfProperty):
    term = RdfTerm(
        "license", "http://schema.org/license", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class businessDays(RdfProperty):
    term = RdfTerm(
        "businessDays", "http://schema.org/businessDays", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.OpeningHoursSpecification | schemaorg.DayOfWeek


@dataclass(frozen=True)
class ccRecipient(RdfProperty):
    term = RdfTerm(
        "ccRecipient",
        "http://schema.org/ccRecipient",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization | schemaorg.ContactPoint | schemaorg.Person


@dataclass(frozen=True)
class permissions(RdfProperty):
    term = RdfTerm(
        "permissions",
        "http://schema.org/permissions",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class broker(RdfProperty):
    term = RdfTerm(
        "broker", "http://schema.org/broker", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class contactType(RdfProperty):
    term = RdfTerm(
        "contactType",
        "http://schema.org/contactType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class recognizedBy(RdfProperty):
    term = RdfTerm(
        "recognizedBy", "http://schema.org/recognizedBy", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class greater(RdfProperty):
    term = RdfTerm(
        "greater", "http://schema.org/greater", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QualitativeValue


@dataclass(frozen=True)
class opponent(RdfProperty):
    term = RdfTerm(
        "opponent", "http://schema.org/opponent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class icaoCode(RdfProperty):
    term = RdfTerm(
        "icaoCode", "http://schema.org/icaoCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class associatedAnatomy(RdfProperty):
    term = RdfTerm(
        "associatedAnatomy",
        "http://schema.org/associatedAnatomy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: (
        schemaorg.SuperficialAnatomy
        | schemaorg.AnatomicalStructure
        | schemaorg.AnatomicalSystem
    )


@dataclass(frozen=True)
class playMode(RdfProperty):
    term = RdfTerm(
        "playMode", "http://schema.org/playMode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.GamePlayMode


@dataclass(frozen=True)
class tributary(RdfProperty):
    term = RdfTerm(
        "tributary", "http://schema.org/tributary", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class tool(RdfProperty):
    term = RdfTerm("tool", "http://schema.org/tool", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.HowToTool | Text


@dataclass(frozen=True)
class taxonomicRange(RdfProperty):
    term = RdfTerm("taxonomicRange", "http://schema.org/taxonomicRange", ["1.2-DRAFT"])
    object: Text | schemaorg.DefinedTerm | URL | schemaorg.Taxon


@dataclass(frozen=True)
class weightTotal(RdfProperty):
    term = RdfTerm(
        "weightTotal",
        "http://schema.org/weightTotal",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class actors(RdfProperty):
    term = RdfTerm(
        "actors", "http://schema.org/actors", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class maximumPhysicalAttendeeCapacity(RdfProperty):
    term = RdfTerm(
        "maximumPhysicalAttendeeCapacity",
        "http://schema.org/maximumPhysicalAttendeeCapacity",
        ["1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class grantee(RdfProperty):
    term = RdfTerm(
        "grantee", "http://schema.org/grantee", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: (
        schemaorg.Audience
        | schemaorg.ContactPoint
        | schemaorg.Person
        | schemaorg.Organization
    )


@dataclass(frozen=True)
class marginOfError(RdfProperty):
    term = RdfTerm(
        "marginOfError", "http://schema.org/marginOfError", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class followup(RdfProperty):
    term = RdfTerm(
        "followup", "http://schema.org/followup", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class connectedTo(RdfProperty):
    term = RdfTerm(
        "connectedTo",
        "http://schema.org/connectedTo",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class foundingLocation(RdfProperty):
    term = RdfTerm(
        "foundingLocation",
        "http://schema.org/foundingLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class acquiredFrom(RdfProperty):
    term = RdfTerm(
        "acquiredFrom",
        "http://schema.org/acquiredFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class estimatedFlightDuration(RdfProperty):
    term = RdfTerm(
        "estimatedFlightDuration",
        "http://schema.org/estimatedFlightDuration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration | Text


@dataclass(frozen=True)
class merchant(RdfProperty):
    term = RdfTerm(
        "merchant", "http://schema.org/merchant", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class game(RdfProperty):
    term = RdfTerm("game", "http://schema.org/game", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.VideoGame


@dataclass(frozen=True)
class partOfOrder(RdfProperty):
    term = RdfTerm(
        "partOfOrder",
        "http://schema.org/partOfOrder",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Order


@dataclass(frozen=True)
class maintainer(RdfProperty):
    term = RdfTerm("maintainer", "http://schema.org/maintainer", ["1.1", "1.2-DRAFT"])
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class serialNumber(RdfProperty):
    term = RdfTerm(
        "serialNumber",
        "http://schema.org/serialNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class numberOfAxles(RdfProperty):
    term = RdfTerm(
        "numberOfAxles",
        "http://schema.org/numberOfAxles",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class median(RdfProperty):
    term = RdfTerm("median", "http://schema.org/median", ["1.0", "1.1", "1.2-DRAFT"])
    object: Number


@dataclass(frozen=True)
class caption(RdfProperty):
    term = RdfTerm(
        "caption", "http://schema.org/caption", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MediaObject | Text


@dataclass(frozen=True)
class application(RdfProperty):
    term = RdfTerm(
        "application",
        "http://schema.org/application",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SoftwareApplication


@dataclass(frozen=True)
class serviceArea(RdfProperty):
    term = RdfTerm(
        "serviceArea",
        "http://schema.org/serviceArea",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.GeoShape | schemaorg.AdministrativeArea | schemaorg.Place


@dataclass(frozen=True)
class dateDeleted(RdfProperty):
    term = RdfTerm(
        "dateDeleted",
        "http://schema.org/dateDeleted",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date | DateTime


@dataclass(frozen=True)
class drugUnit(RdfProperty):
    term = RdfTerm(
        "drugUnit", "http://schema.org/drugUnit", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class programPrerequisites(RdfProperty):
    term = RdfTerm(
        "programPrerequisites",
        "http://schema.org/programPrerequisites",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: (
        schemaorg.EducationalOccupationalCredential
        | schemaorg.AlignmentObject
        | Text
        | schemaorg.Course
    )


@dataclass(frozen=True)
class childMaxAge(RdfProperty):
    term = RdfTerm(
        "childMaxAge",
        "http://schema.org/childMaxAge",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class featureList(RdfProperty):
    term = RdfTerm(
        "featureList",
        "http://schema.org/featureList",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class courseSchedule(RdfProperty):
    term = RdfTerm("courseSchedule", "http://schema.org/courseSchedule", ["1.2-DRAFT"])
    object: schemaorg.Schedule


@dataclass(frozen=True)
class suggestedGender(RdfProperty):
    term = RdfTerm(
        "suggestedGender",
        "http://schema.org/suggestedGender",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.GenderType


@dataclass(frozen=True)
class sourceOrganization(RdfProperty):
    term = RdfTerm(
        "sourceOrganization",
        "http://schema.org/sourceOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class hasTierRequirement(RdfProperty):
    term = RdfTerm("hasTierRequirement", "http://schema.org/hasTierRequirement", [])
    object: (
        Text
        | schemaorg.MonetaryAmount
        | schemaorg.CreditCard
        | schemaorg.UnitPriceSpecification
    )


@dataclass(frozen=True)
class paymentDueDate(RdfProperty):
    term = RdfTerm(
        "paymentDueDate",
        "http://schema.org/paymentDueDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime | Date


@dataclass(frozen=True)
class model(RdfProperty):
    term = RdfTerm(
        "model", "http://schema.org/model", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.ProductModel


@dataclass(frozen=True)
class contraindication(RdfProperty):
    term = RdfTerm(
        "contraindication",
        "http://schema.org/contraindication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalContraindication | Text


@dataclass(frozen=True)
class isRelatedTo(RdfProperty):
    term = RdfTerm(
        "isRelatedTo",
        "http://schema.org/isRelatedTo",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Product | schemaorg.Service


@dataclass(frozen=True)
class risks(RdfProperty):
    term = RdfTerm(
        "risks", "http://schema.org/risks", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class trailer(RdfProperty):
    term = RdfTerm(
        "trailer", "http://schema.org/trailer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.VideoObject


@dataclass(frozen=True)
class softwareVersion(RdfProperty):
    term = RdfTerm(
        "softwareVersion",
        "http://schema.org/softwareVersion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class recommendedIntake(RdfProperty):
    term = RdfTerm(
        "recommendedIntake",
        "http://schema.org/recommendedIntake",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.RecommendedDoseSchedule


@dataclass(frozen=True)
class sportsTeam(RdfProperty):
    term = RdfTerm(
        "sportsTeam", "http://schema.org/sportsTeam", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.SportsTeam


@dataclass(frozen=True)
class evidenceLevel(RdfProperty):
    term = RdfTerm(
        "evidenceLevel",
        "http://schema.org/evidenceLevel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEvidenceLevel


@dataclass(frozen=True)
class contentType(RdfProperty):
    term = RdfTerm(
        "contentType",
        "http://schema.org/contentType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class instructor(RdfProperty):
    term = RdfTerm(
        "instructor", "http://schema.org/instructor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class educationalFramework(RdfProperty):
    term = RdfTerm(
        "educationalFramework",
        "http://schema.org/educationalFramework",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class reviews(RdfProperty):
    term = RdfTerm(
        "reviews", "http://schema.org/reviews", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Review


@dataclass(frozen=True)
class accessibilityHazard(RdfProperty):
    term = RdfTerm(
        "accessibilityHazard",
        "http://schema.org/accessibilityHazard",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class partySize(RdfProperty):
    term = RdfTerm(
        "partySize", "http://schema.org/partySize", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | Integer


@dataclass(frozen=True)
class executableLibraryName(RdfProperty):
    term = RdfTerm(
        "executableLibraryName",
        "http://schema.org/executableLibraryName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class seeks(RdfProperty):
    term = RdfTerm(
        "seeks", "http://schema.org/seeks", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Demand


@dataclass(frozen=True)
class potentialUse(RdfProperty):
    term = RdfTerm("potentialUse", "http://schema.org/potentialUse", ["1.2-DRAFT"])
    object: schemaorg.DefinedTerm


@dataclass(frozen=True)
class nonprofitStatus(RdfProperty):
    term = RdfTerm(
        "nonprofitStatus", "http://schema.org/nonprofitStatus", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.NonprofitType


@dataclass(frozen=True)
class courseWorkload(RdfProperty):
    term = RdfTerm(
        "courseWorkload",
        "http://schema.org/courseWorkload",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class endOffset(RdfProperty):
    term = RdfTerm(
        "endOffset", "http://schema.org/endOffset", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | schemaorg.HyperTocEntry


@dataclass(frozen=True)
class requiresSubscription(RdfProperty):
    term = RdfTerm(
        "requiresSubscription",
        "http://schema.org/requiresSubscription",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean | schemaorg.MediaSubscription


@dataclass(frozen=True)
class parentOrganization(RdfProperty):
    term = RdfTerm(
        "parentOrganization",
        "http://schema.org/parentOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class leiCode(RdfProperty):
    term = RdfTerm(
        "leiCode", "http://schema.org/leiCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class returnFees(RdfProperty):
    term = RdfTerm(
        "returnFees", "http://schema.org/returnFees", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ReturnFeesEnumeration


@dataclass(frozen=True)
class artMedium(RdfProperty):
    term = RdfTerm(
        "artMedium", "http://schema.org/artMedium", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class numberOfAccommodationUnits(RdfProperty):
    term = RdfTerm(
        "numberOfAccommodationUnits",
        "http://schema.org/numberOfAccommodationUnits",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class associatedPathophysiology(RdfProperty):
    term = RdfTerm(
        "associatedPathophysiology",
        "http://schema.org/associatedPathophysiology",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class gtin12(RdfProperty):
    term = RdfTerm(
        "gtin12", "http://schema.org/gtin12", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class isAcceptingNewPatients(RdfProperty):
    term = RdfTerm(
        "isAcceptingNewPatients",
        "http://schema.org/isAcceptingNewPatients",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class tocEntry(RdfProperty):
    term = RdfTerm("tocEntry", "http://schema.org/tocEntry", ["1.2-DRAFT"])
    object: schemaorg.HyperTocEntry


@dataclass(frozen=True)
class step(RdfProperty):
    term = RdfTerm("step", "http://schema.org/step", ["1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.CreativeWork | Text | schemaorg.HowToSection | schemaorg.HowToStep


@dataclass(frozen=True)
class codeValue(RdfProperty):
    term = RdfTerm(
        "codeValue", "http://schema.org/codeValue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class orderValue(RdfProperty):
    term = RdfTerm("orderValue", "http://schema.org/orderValue", [])
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class payload(RdfProperty):
    term = RdfTerm(
        "payload", "http://schema.org/payload", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class additionalName(RdfProperty):
    term = RdfTerm(
        "additionalName",
        "http://schema.org/additionalName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class hasCredential(RdfProperty):
    term = RdfTerm(
        "hasCredential", "http://schema.org/hasCredential", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.EducationalOccupationalCredential


@dataclass(frozen=True)
class deathDate(RdfProperty):
    term = RdfTerm(
        "deathDate", "http://schema.org/deathDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date


@dataclass(frozen=True)
class populationType(RdfProperty):
    term = RdfTerm(
        "populationType",
        "http://schema.org/populationType",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Class


@dataclass(frozen=True)
class mealService(RdfProperty):
    term = RdfTerm(
        "mealService",
        "http://schema.org/mealService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class inStoreReturnsOffered(RdfProperty):
    term = RdfTerm(
        "inStoreReturnsOffered",
        "http://schema.org/inStoreReturnsOffered",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class workExample(RdfProperty):
    term = RdfTerm(
        "workExample",
        "http://schema.org/workExample",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class shippingConditions(RdfProperty):
    term = RdfTerm("shippingConditions", "http://schema.org/shippingConditions", [])
    object: schemaorg.ShippingConditions


@dataclass(frozen=True)
class composer(RdfProperty):
    term = RdfTerm(
        "composer", "http://schema.org/composer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class spokenByCharacter(RdfProperty):
    term = RdfTerm(
        "spokenByCharacter",
        "http://schema.org/spokenByCharacter",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class schoolClosuresInfo(RdfProperty):
    term = RdfTerm(
        "schoolClosuresInfo",
        "http://schema.org/schoolClosuresInfo",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.WebContent


@dataclass(frozen=True)
class disambiguatingDescription(RdfProperty):
    term = RdfTerm(
        "disambiguatingDescription",
        "http://schema.org/disambiguatingDescription",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class episodeNumber(RdfProperty):
    term = RdfTerm(
        "episodeNumber",
        "http://schema.org/episodeNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer | Text


@dataclass(frozen=True)
class supersededBy(RdfProperty):
    term = RdfTerm(
        "supersededBy",
        "http://schema.org/supersededBy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Class | schemaorg.Property | schemaorg.Enumeration


@dataclass(frozen=True)
class founders(RdfProperty):
    term = RdfTerm(
        "founders", "http://schema.org/founders", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class pattern(RdfProperty):
    term = RdfTerm("pattern", "http://schema.org/pattern", ["1.1", "1.2-DRAFT"])
    object: schemaorg.DefinedTerm | Text


@dataclass(frozen=True)
class commentText(RdfProperty):
    term = RdfTerm(
        "commentText",
        "http://schema.org/commentText",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class cvdNumICUBedsOcc(RdfProperty):
    term = RdfTerm(
        "cvdNumICUBedsOcc", "http://schema.org/cvdNumICUBedsOcc", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class sodiumContent(RdfProperty):
    term = RdfTerm(
        "sodiumContent",
        "http://schema.org/sodiumContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class videoQuality(RdfProperty):
    term = RdfTerm(
        "videoQuality",
        "http://schema.org/videoQuality",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class validFor(RdfProperty):
    term = RdfTerm(
        "validFor", "http://schema.org/validFor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class inBroadcastLineup(RdfProperty):
    term = RdfTerm(
        "inBroadcastLineup",
        "http://schema.org/inBroadcastLineup",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CableOrSatelliteService


@dataclass(frozen=True)
class broadcastTimezone(RdfProperty):
    term = RdfTerm(
        "broadcastTimezone",
        "http://schema.org/broadcastTimezone",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class characterName(RdfProperty):
    term = RdfTerm(
        "characterName",
        "http://schema.org/characterName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class hasMenuSection(RdfProperty):
    term = RdfTerm(
        "hasMenuSection",
        "http://schema.org/hasMenuSection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MenuSection


@dataclass(frozen=True)
class accessCode(RdfProperty):
    term = RdfTerm(
        "accessCode", "http://schema.org/accessCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class requiredMinAge(RdfProperty):
    term = RdfTerm(
        "requiredMinAge",
        "http://schema.org/requiredMinAge",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class offers(RdfProperty):
    term = RdfTerm(
        "offers", "http://schema.org/offers", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Offer | schemaorg.Demand


@dataclass(frozen=True)
class equal(RdfProperty):
    term = RdfTerm(
        "equal", "http://schema.org/equal", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QualitativeValue


@dataclass(frozen=True)
class geoCrosses(RdfProperty):
    term = RdfTerm(
        "geoCrosses", "http://schema.org/geoCrosses", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.GeospatialGeometry | schemaorg.Place


@dataclass(frozen=True)
class diseaseSpreadStatistics(RdfProperty):
    term = RdfTerm(
        "diseaseSpreadStatistics",
        "http://schema.org/diseaseSpreadStatistics",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Dataset | URL | schemaorg.Observation | schemaorg.WebContent


@dataclass(frozen=True)
class closes(RdfProperty):
    term = RdfTerm(
        "closes", "http://schema.org/closes", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Time


@dataclass(frozen=True)
class hasPart(RdfProperty):
    term = RdfTerm(
        "hasPart", "http://schema.org/hasPart", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class departureBusStop(RdfProperty):
    term = RdfTerm(
        "departureBusStop",
        "http://schema.org/departureBusStop",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BusStation | schemaorg.BusStop


@dataclass(frozen=True)
class recordedAs(RdfProperty):
    term = RdfTerm(
        "recordedAs", "http://schema.org/recordedAs", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicRecording


@dataclass(frozen=True)
class overdosage(RdfProperty):
    term = RdfTerm(
        "overdosage", "http://schema.org/overdosage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class cargoVolume(RdfProperty):
    term = RdfTerm(
        "cargoVolume",
        "http://schema.org/cargoVolume",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class keywords(RdfProperty):
    term = RdfTerm(
        "keywords", "http://schema.org/keywords", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.DefinedTerm | URL | Text


@dataclass(frozen=True)
class exampleOfWork(RdfProperty):
    term = RdfTerm(
        "exampleOfWork",
        "http://schema.org/exampleOfWork",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class contactOption(RdfProperty):
    term = RdfTerm(
        "contactOption",
        "http://schema.org/contactOption",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPointOption


@dataclass(frozen=True)
class copyrightNotice(RdfProperty):
    term = RdfTerm(
        "copyrightNotice", "http://schema.org/copyrightNotice", ["1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class musicBy(RdfProperty):
    term = RdfTerm(
        "musicBy", "http://schema.org/musicBy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.MusicGroup


@dataclass(frozen=True)
class arrivalBusStop(RdfProperty):
    term = RdfTerm(
        "arrivalBusStop",
        "http://schema.org/arrivalBusStop",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BusStation | schemaorg.BusStop


@dataclass(frozen=True)
class isLiveBroadcast(RdfProperty):
    term = RdfTerm(
        "isLiveBroadcast",
        "http://schema.org/isLiveBroadcast",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class fileSize(RdfProperty):
    term = RdfTerm(
        "fileSize", "http://schema.org/fileSize", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class encodingFormat(RdfProperty):
    term = RdfTerm(
        "encodingFormat",
        "http://schema.org/encodingFormat",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class hasDriveThroughService(RdfProperty):
    term = RdfTerm(
        "hasDriveThroughService",
        "http://schema.org/hasDriveThroughService",
        ["1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class arrivalGate(RdfProperty):
    term = RdfTerm(
        "arrivalGate",
        "http://schema.org/arrivalGate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class numberOfAvailableAccommodationUnits(RdfProperty):
    term = RdfTerm(
        "numberOfAvailableAccommodationUnits",
        "http://schema.org/numberOfAvailableAccommodationUnits",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class negativeNotes(RdfProperty):
    term = RdfTerm("negativeNotes", "http://schema.org/negativeNotes", ["1.2-DRAFT"])
    object: Text | schemaorg.ListItem | schemaorg.ItemList | schemaorg.WebContent


@dataclass(frozen=True)
class identifier(RdfProperty):
    term = RdfTerm(
        "identifier", "http://schema.org/identifier", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.PropertyValue | URL


@dataclass(frozen=True)
class suggestedMeasurement(RdfProperty):
    term = RdfTerm(
        "suggestedMeasurement", "http://schema.org/suggestedMeasurement", ["1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class recipeCuisine(RdfProperty):
    term = RdfTerm(
        "recipeCuisine",
        "http://schema.org/recipeCuisine",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class jobTitle(RdfProperty):
    term = RdfTerm(
        "jobTitle", "http://schema.org/jobTitle", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class broadcastSignalModulation(RdfProperty):
    term = RdfTerm(
        "broadcastSignalModulation",
        "http://schema.org/broadcastSignalModulation",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QualitativeValue


@dataclass(frozen=True)
class bed(RdfProperty):
    term = RdfTerm("bed", "http://schema.org/bed", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.BedType | Text | schemaorg.BedDetails


@dataclass(frozen=True)
class cutoffTime(RdfProperty):
    term = RdfTerm("cutoffTime", "http://schema.org/cutoffTime", ["1.1", "1.2-DRAFT"])
    object: Time


@dataclass(frozen=True)
class itemReviewed(RdfProperty):
    term = RdfTerm(
        "itemReviewed",
        "http://schema.org/itemReviewed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class vatID(RdfProperty):
    term = RdfTerm(
        "vatID", "http://schema.org/vatID", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class securityScreening(RdfProperty):
    term = RdfTerm(
        "securityScreening",
        "http://schema.org/securityScreening",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class leaseLength(RdfProperty):
    term = RdfTerm(
        "leaseLength", "http://schema.org/leaseLength", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | schemaorg.Duration


@dataclass(frozen=True)
class orderQuantity(RdfProperty):
    term = RdfTerm(
        "orderQuantity",
        "http://schema.org/orderQuantity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class targetName(RdfProperty):
    term = RdfTerm(
        "targetName", "http://schema.org/targetName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class engineType(RdfProperty):
    term = RdfTerm(
        "engineType", "http://schema.org/engineType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QualitativeValue | URL | Text


@dataclass(frozen=True)
class occupationalCategory(RdfProperty):
    term = RdfTerm(
        "occupationalCategory",
        "http://schema.org/occupationalCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CategoryCode | Text


@dataclass(frozen=True)
class branch(RdfProperty):
    term = RdfTerm(
        "branch", "http://schema.org/branch", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class mainEntity(RdfProperty):
    term = RdfTerm(
        "mainEntity", "http://schema.org/mainEntity", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class suitableForDiet(RdfProperty):
    term = RdfTerm(
        "suitableForDiet",
        "http://schema.org/suitableForDiet",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.RestrictedDiet


@dataclass(frozen=True)
class billingDuration(RdfProperty):
    term = RdfTerm(
        "billingDuration", "http://schema.org/billingDuration", ["1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | Number | schemaorg.Duration


@dataclass(frozen=True)
class coverageStartTime(RdfProperty):
    term = RdfTerm(
        "coverageStartTime",
        "http://schema.org/coverageStartTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class employmentUnit(RdfProperty):
    term = RdfTerm(
        "employmentUnit",
        "http://schema.org/employmentUnit",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class gtin13(RdfProperty):
    term = RdfTerm(
        "gtin13", "http://schema.org/gtin13", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class usesHealthPlanIdStandard(RdfProperty):
    term = RdfTerm(
        "usesHealthPlanIdStandard",
        "http://schema.org/usesHealthPlanIdStandard",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | Text


@dataclass(frozen=True)
class editEIDR(RdfProperty):
    term = RdfTerm("editEIDR", "http://schema.org/editEIDR", ["1.1", "1.2-DRAFT"])
    object: URL | Text


@dataclass(frozen=True)
class maximumAttendeeCapacity(RdfProperty):
    term = RdfTerm(
        "maximumAttendeeCapacity",
        "http://schema.org/maximumAttendeeCapacity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class relevantSpecialty(RdfProperty):
    term = RdfTerm(
        "relevantSpecialty",
        "http://schema.org/relevantSpecialty",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalSpecialty


@dataclass(frozen=True)
class billingPeriod(RdfProperty):
    term = RdfTerm(
        "billingPeriod",
        "http://schema.org/billingPeriod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class shippingSettingsLink(RdfProperty):
    term = RdfTerm(
        "shippingSettingsLink",
        "http://schema.org/shippingSettingsLink",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class referencesOrder(RdfProperty):
    term = RdfTerm(
        "referencesOrder",
        "http://schema.org/referencesOrder",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Order


@dataclass(frozen=True)
class processingTime(RdfProperty):
    term = RdfTerm(
        "processingTime",
        "http://schema.org/processingTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class copyrightYear(RdfProperty):
    term = RdfTerm(
        "copyrightYear",
        "http://schema.org/copyrightYear",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class broadcastSubChannel(RdfProperty):
    term = RdfTerm(
        "broadcastSubChannel",
        "http://schema.org/broadcastSubChannel",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class specialOpeningHoursSpecification(RdfProperty):
    term = RdfTerm(
        "specialOpeningHoursSpecification",
        "http://schema.org/specialOpeningHoursSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OpeningHoursSpecification


@dataclass(frozen=True)
class incentiveStatus(RdfProperty):
    term = RdfTerm("incentiveStatus", "http://schema.org/incentiveStatus", [])
    object: schemaorg.IncentiveStatus


@dataclass(frozen=True)
class servesCuisine(RdfProperty):
    term = RdfTerm(
        "servesCuisine",
        "http://schema.org/servesCuisine",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class collectionSize(RdfProperty):
    term = RdfTerm(
        "collectionSize",
        "http://schema.org/collectionSize",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class operatingSystem(RdfProperty):
    term = RdfTerm(
        "operatingSystem",
        "http://schema.org/operatingSystem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class orderPercentage(RdfProperty):
    term = RdfTerm("orderPercentage", "http://schema.org/orderPercentage", [])
    object: Number


@dataclass(frozen=True)
class encodingType(RdfProperty):
    term = RdfTerm(
        "encodingType",
        "http://schema.org/encodingType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class nerve(RdfProperty):
    term = RdfTerm(
        "nerve", "http://schema.org/nerve", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Nerve


@dataclass(frozen=True)
class webCheckinTime(RdfProperty):
    term = RdfTerm(
        "webCheckinTime",
        "http://schema.org/webCheckinTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class taxID(RdfProperty):
    term = RdfTerm(
        "taxID", "http://schema.org/taxID", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class hasMeasurement(RdfProperty):
    term = RdfTerm("hasMeasurement", "http://schema.org/hasMeasurement", ["1.2-DRAFT"])
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class about(RdfProperty):
    term = RdfTerm(
        "about", "http://schema.org/about", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class healthCondition(RdfProperty):
    term = RdfTerm(
        "healthCondition",
        "http://schema.org/healthCondition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalCondition


@dataclass(frozen=True)
class dataFeedElement(RdfProperty):
    term = RdfTerm(
        "dataFeedElement",
        "http://schema.org/dataFeedElement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DataFeedItem | schemaorg.Thing | Text


@dataclass(frozen=True)
class prescriptionStatus(RdfProperty):
    term = RdfTerm(
        "prescriptionStatus",
        "http://schema.org/prescriptionStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DrugPrescriptionStatus | Text


@dataclass(frozen=True)
class containedIn(RdfProperty):
    term = RdfTerm(
        "containedIn",
        "http://schema.org/containedIn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class diseasePreventionInfo(RdfProperty):
    term = RdfTerm(
        "diseasePreventionInfo",
        "http://schema.org/diseasePreventionInfo",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.WebContent


@dataclass(frozen=True)
class aspect(RdfProperty):
    term = RdfTerm(
        "aspect", "http://schema.org/aspect", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class deliveryLeadTime(RdfProperty):
    term = RdfTerm(
        "deliveryLeadTime",
        "http://schema.org/deliveryLeadTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class isrcCode(RdfProperty):
    term = RdfTerm(
        "isrcCode", "http://schema.org/isrcCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class nerveMotor(RdfProperty):
    term = RdfTerm(
        "nerveMotor", "http://schema.org/nerveMotor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Muscle


@dataclass(frozen=True)
class valuePattern(RdfProperty):
    term = RdfTerm(
        "valuePattern",
        "http://schema.org/valuePattern",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class programType(RdfProperty):
    term = RdfTerm("programType", "http://schema.org/programType", ["1.1", "1.2-DRAFT"])
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class datePublished(RdfProperty):
    term = RdfTerm(
        "datePublished",
        "http://schema.org/datePublished",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date | DateTime


@dataclass(frozen=True)
class location(RdfProperty):
    term = RdfTerm(
        "location", "http://schema.org/location", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.Place | schemaorg.VirtualLocation | schemaorg.PostalAddress


@dataclass(frozen=True)
class dropoffTime(RdfProperty):
    term = RdfTerm(
        "dropoffTime",
        "http://schema.org/dropoffTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class algorithm(RdfProperty):
    term = RdfTerm(
        "algorithm", "http://schema.org/algorithm", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class jobImmediateStart(RdfProperty):
    term = RdfTerm(
        "jobImmediateStart",
        "http://schema.org/jobImmediateStart",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class applicationCategory(RdfProperty):
    term = RdfTerm(
        "applicationCategory",
        "http://schema.org/applicationCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class directApply(RdfProperty):
    term = RdfTerm("directApply", "http://schema.org/directApply", ["1.2-DRAFT"])
    object: Boolean


@dataclass(frozen=True)
class estimatedCost(RdfProperty):
    term = RdfTerm(
        "estimatedCost",
        "http://schema.org/estimatedCost",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount | Text


@dataclass(frozen=True)
class lyricist(RdfProperty):
    term = RdfTerm(
        "lyricist", "http://schema.org/lyricist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class requiredGender(RdfProperty):
    term = RdfTerm(
        "requiredGender",
        "http://schema.org/requiredGender",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class reservationStatus(RdfProperty):
    term = RdfTerm(
        "reservationStatus",
        "http://schema.org/reservationStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ReservationStatusType


@dataclass(frozen=True)
class broadcastChannelId(RdfProperty):
    term = RdfTerm(
        "broadcastChannelId",
        "http://schema.org/broadcastChannelId",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class educationalLevel(RdfProperty):
    term = RdfTerm(
        "educationalLevel",
        "http://schema.org/educationalLevel",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DefinedTerm | URL


@dataclass(frozen=True)
class embedUrl(RdfProperty):
    term = RdfTerm(
        "embedUrl", "http://schema.org/embedUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class coverageEndTime(RdfProperty):
    term = RdfTerm(
        "coverageEndTime",
        "http://schema.org/coverageEndTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class timeToComplete(RdfProperty):
    term = RdfTerm(
        "timeToComplete",
        "http://schema.org/timeToComplete",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class isResizable(RdfProperty):
    term = RdfTerm("isResizable", "http://schema.org/isResizable", ["1.1", "1.2-DRAFT"])
    object: Boolean


@dataclass(frozen=True)
class seller(RdfProperty):
    term = RdfTerm(
        "seller", "http://schema.org/seller", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class passengerPriorityStatus(RdfProperty):
    term = RdfTerm(
        "passengerPriorityStatus",
        "http://schema.org/passengerPriorityStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QualitativeValue


@dataclass(frozen=True)
class possibleComplication(RdfProperty):
    term = RdfTerm(
        "possibleComplication",
        "http://schema.org/possibleComplication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class jobStartDate(RdfProperty):
    term = RdfTerm(
        "jobStartDate", "http://schema.org/jobStartDate", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | Date


@dataclass(frozen=True)
class adverseOutcome(RdfProperty):
    term = RdfTerm(
        "adverseOutcome",
        "http://schema.org/adverseOutcome",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEntity


@dataclass(frozen=True)
class membershipPointsEarned(RdfProperty):
    term = RdfTerm(
        "membershipPointsEarned",
        "http://schema.org/membershipPointsEarned",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class nextItem(RdfProperty):
    term = RdfTerm(
        "nextItem", "http://schema.org/nextItem", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ListItem


@dataclass(frozen=True)
class includedDataCatalog(RdfProperty):
    term = RdfTerm(
        "includedDataCatalog",
        "http://schema.org/includedDataCatalog",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DataCatalog


@dataclass(frozen=True)
class signDetected(RdfProperty):
    term = RdfTerm(
        "signDetected",
        "http://schema.org/signDetected",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalSign


@dataclass(frozen=True)
class cvdFacilityId(RdfProperty):
    term = RdfTerm(
        "cvdFacilityId", "http://schema.org/cvdFacilityId", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class programmingModel(RdfProperty):
    term = RdfTerm(
        "programmingModel",
        "http://schema.org/programmingModel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class chemicalComposition(RdfProperty):
    term = RdfTerm(
        "chemicalComposition", "http://schema.org/chemicalComposition", ["1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class accessibilityFeature(RdfProperty):
    term = RdfTerm(
        "accessibilityFeature",
        "http://schema.org/accessibilityFeature",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class relatedCondition(RdfProperty):
    term = RdfTerm(
        "relatedCondition",
        "http://schema.org/relatedCondition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalCondition


@dataclass(frozen=True)
class legislationChanges(RdfProperty):
    term = RdfTerm(
        "legislationChanges",
        "http://schema.org/legislationChanges",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Legislation


@dataclass(frozen=True)
class qualifications(RdfProperty):
    term = RdfTerm(
        "qualifications",
        "http://schema.org/qualifications",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EducationalOccupationalCredential | Text


@dataclass(frozen=True)
class colleagues(RdfProperty):
    term = RdfTerm(
        "colleagues", "http://schema.org/colleagues", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class returnLabelSource(RdfProperty):
    term = RdfTerm(
        "returnLabelSource", "http://schema.org/returnLabelSource", ["1.2-DRAFT"]
    )
    object: schemaorg.ReturnLabelSourceEnumeration


@dataclass(frozen=True)
class guidelineSubject(RdfProperty):
    term = RdfTerm(
        "guidelineSubject",
        "http://schema.org/guidelineSubject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEntity


@dataclass(frozen=True)
class duringMedia(RdfProperty):
    term = RdfTerm(
        "duringMedia",
        "http://schema.org/duringMedia",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MediaObject | URL


@dataclass(frozen=True)
class seatNumber(RdfProperty):
    term = RdfTerm(
        "seatNumber", "http://schema.org/seatNumber", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class musicReleaseFormat(RdfProperty):
    term = RdfTerm(
        "musicReleaseFormat",
        "http://schema.org/musicReleaseFormat",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MusicReleaseFormatType


@dataclass(frozen=True)
class articleSection(RdfProperty):
    term = RdfTerm(
        "articleSection",
        "http://schema.org/articleSection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class materialExtent(RdfProperty):
    term = RdfTerm(
        "materialExtent",
        "http://schema.org/materialExtent",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class signOrSymptom(RdfProperty):
    term = RdfTerm(
        "signOrSymptom",
        "http://schema.org/signOrSymptom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalSignOrSymptom


@dataclass(frozen=True)
class musicArrangement(RdfProperty):
    term = RdfTerm(
        "musicArrangement",
        "http://schema.org/musicArrangement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MusicComposition


@dataclass(frozen=True)
class video(RdfProperty):
    term = RdfTerm(
        "video", "http://schema.org/video", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Clip | schemaorg.VideoObject


@dataclass(frozen=True)
class remainingAttendeeCapacity(RdfProperty):
    term = RdfTerm(
        "remainingAttendeeCapacity",
        "http://schema.org/remainingAttendeeCapacity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class availableThrough(RdfProperty):
    term = RdfTerm(
        "availableThrough",
        "http://schema.org/availableThrough",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class geoCoveredBy(RdfProperty):
    term = RdfTerm(
        "geoCoveredBy", "http://schema.org/geoCoveredBy", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place | schemaorg.GeospatialGeometry


@dataclass(frozen=True)
class advanceBookingRequirement(RdfProperty):
    term = RdfTerm(
        "advanceBookingRequirement",
        "http://schema.org/advanceBookingRequirement",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class touristType(RdfProperty):
    term = RdfTerm(
        "touristType",
        "http://schema.org/touristType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Audience | Text


@dataclass(frozen=True)
class gtin(RdfProperty):
    term = RdfTerm("gtin", "http://schema.org/gtin", ["1.0", "1.1", "1.2-DRAFT"])
    object: Text | URL


@dataclass(frozen=True)
class seasonalOverride(RdfProperty):
    term = RdfTerm("seasonalOverride", "http://schema.org/seasonalOverride", [])
    object: schemaorg.OpeningHoursSpecification


@dataclass(frozen=True)
class loanType(RdfProperty):
    term = RdfTerm(
        "loanType", "http://schema.org/loanType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class meetsEmissionStandard(RdfProperty):
    term = RdfTerm(
        "meetsEmissionStandard",
        "http://schema.org/meetsEmissionStandard",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QualitativeValue | URL | Text


@dataclass(frozen=True)
class arrivalStation(RdfProperty):
    term = RdfTerm(
        "arrivalStation",
        "http://schema.org/arrivalStation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.TrainStation


@dataclass(frozen=True)
class description(RdfProperty):
    term = RdfTerm(
        "description",
        "http://schema.org/description",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.TextObject


@dataclass(frozen=True)
class applicationSuite(RdfProperty):
    term = RdfTerm(
        "applicationSuite",
        "http://schema.org/applicationSuite",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class handlingTime(RdfProperty):
    term = RdfTerm(
        "handlingTime", "http://schema.org/handlingTime", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | schemaorg.ServicePeriod


@dataclass(frozen=True)
class seriousAdverseOutcome(RdfProperty):
    term = RdfTerm(
        "seriousAdverseOutcome",
        "http://schema.org/seriousAdverseOutcome",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEntity


@dataclass(frozen=True)
class cookTime(RdfProperty):
    term = RdfTerm(
        "cookTime", "http://schema.org/cookTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class checkinTime(RdfProperty):
    term = RdfTerm(
        "checkinTime",
        "http://schema.org/checkinTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Time | DateTime


@dataclass(frozen=True)
class primaryPrevention(RdfProperty):
    term = RdfTerm(
        "primaryPrevention",
        "http://schema.org/primaryPrevention",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTherapy


@dataclass(frozen=True)
class isGift(RdfProperty):
    term = RdfTerm(
        "isGift", "http://schema.org/isGift", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Boolean


@dataclass(frozen=True)
class departureTerminal(RdfProperty):
    term = RdfTerm(
        "departureTerminal",
        "http://schema.org/departureTerminal",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class ticketToken(RdfProperty):
    term = RdfTerm(
        "ticketToken",
        "http://schema.org/ticketToken",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | Text


@dataclass(frozen=True)
class albumReleaseType(RdfProperty):
    term = RdfTerm(
        "albumReleaseType",
        "http://schema.org/albumReleaseType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MusicAlbumReleaseType


@dataclass(frozen=True)
class nonProprietaryName(RdfProperty):
    term = RdfTerm(
        "nonProprietaryName",
        "http://schema.org/nonProprietaryName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class seatRow(RdfProperty):
    term = RdfTerm(
        "seatRow", "http://schema.org/seatRow", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class countriesSupported(RdfProperty):
    term = RdfTerm(
        "countriesSupported",
        "http://schema.org/countriesSupported",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class winner(RdfProperty):
    term = RdfTerm(
        "winner", "http://schema.org/winner", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class geographicArea(RdfProperty):
    term = RdfTerm(
        "geographicArea",
        "http://schema.org/geographicArea",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AdministrativeArea


@dataclass(frozen=True)
class nutrition(RdfProperty):
    term = RdfTerm(
        "nutrition", "http://schema.org/nutrition", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.NutritionInformation


@dataclass(frozen=True)
class funding(RdfProperty):
    term = RdfTerm("funding", "http://schema.org/funding", ["1.1", "1.2-DRAFT"])
    object: schemaorg.Grant


@dataclass(frozen=True)
class legislationCommences(RdfProperty):
    term = RdfTerm("legislationCommences", "http://schema.org/legislationCommences", [])
    object: schemaorg.Legislation


@dataclass(frozen=True)
class healthPlanCoinsuranceOption(RdfProperty):
    term = RdfTerm(
        "healthPlanCoinsuranceOption",
        "http://schema.org/healthPlanCoinsuranceOption",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class termsOfService(RdfProperty):
    term = RdfTerm(
        "termsOfService",
        "http://schema.org/termsOfService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class artworkSurface(RdfProperty):
    term = RdfTerm(
        "artworkSurface",
        "http://schema.org/artworkSurface",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class diversityPolicy(RdfProperty):
    term = RdfTerm(
        "diversityPolicy",
        "http://schema.org/diversityPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class openingHours(RdfProperty):
    term = RdfTerm(
        "openingHours",
        "http://schema.org/openingHours",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class usNPI(RdfProperty):
    term = RdfTerm("usNPI", "http://schema.org/usNPI", [])
    object: Text


@dataclass(frozen=True)
class penciler(RdfProperty):
    term = RdfTerm(
        "penciler", "http://schema.org/penciler", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class publishedBy(RdfProperty):
    term = RdfTerm(
        "publishedBy",
        "http://schema.org/publishedBy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class numberOfPartialBathrooms(RdfProperty):
    term = RdfTerm(
        "numberOfPartialBathrooms",
        "http://schema.org/numberOfPartialBathrooms",
        ["1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class runsTo(RdfProperty):
    term = RdfTerm(
        "runsTo", "http://schema.org/runsTo", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Vessel


@dataclass(frozen=True)
class givenName(RdfProperty):
    term = RdfTerm(
        "givenName", "http://schema.org/givenName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class hasTiers(RdfProperty):
    term = RdfTerm("hasTiers", "http://schema.org/hasTiers", [])
    object: schemaorg.MemberProgramTier


@dataclass(frozen=True)
class reservationId(RdfProperty):
    term = RdfTerm(
        "reservationId",
        "http://schema.org/reservationId",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class specialCommitments(RdfProperty):
    term = RdfTerm(
        "specialCommitments",
        "http://schema.org/specialCommitments",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class surface(RdfProperty):
    term = RdfTerm(
        "surface", "http://schema.org/surface", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class isConsumableFor(RdfProperty):
    term = RdfTerm(
        "isConsumableFor",
        "http://schema.org/isConsumableFor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Product


@dataclass(frozen=True)
class bccRecipient(RdfProperty):
    term = RdfTerm(
        "bccRecipient",
        "http://schema.org/bccRecipient",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPoint | schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class pickupTime(RdfProperty):
    term = RdfTerm(
        "pickupTime", "http://schema.org/pickupTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime


@dataclass(frozen=True)
class inChI(RdfProperty):
    term = RdfTerm("inChI", "http://schema.org/inChI", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class sha256(RdfProperty):
    term = RdfTerm("sha256", "http://schema.org/sha256", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class attendee(RdfProperty):
    term = RdfTerm(
        "attendee", "http://schema.org/attendee", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class isProprietary(RdfProperty):
    term = RdfTerm(
        "isProprietary",
        "http://schema.org/isProprietary",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class ratingCount(RdfProperty):
    term = RdfTerm(
        "ratingCount",
        "http://schema.org/ratingCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class price(RdfProperty):
    term = RdfTerm(
        "price", "http://schema.org/price", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | Number


@dataclass(frozen=True)
class utterances(RdfProperty):
    term = RdfTerm("utterances", "http://schema.org/utterances", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class recognizingAuthority(RdfProperty):
    term = RdfTerm(
        "recognizingAuthority",
        "http://schema.org/recognizingAuthority",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class agent(RdfProperty):
    term = RdfTerm(
        "agent", "http://schema.org/agent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class validFrom(RdfProperty):
    term = RdfTerm(
        "validFrom", "http://schema.org/validFrom", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime | Date


@dataclass(frozen=True)
class broadcastServiceTier(RdfProperty):
    term = RdfTerm(
        "broadcastServiceTier",
        "http://schema.org/broadcastServiceTier",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class paymentAccepted(RdfProperty):
    term = RdfTerm(
        "paymentAccepted",
        "http://schema.org/paymentAccepted",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class legislationLegalValue(RdfProperty):
    term = RdfTerm(
        "legislationLegalValue",
        "http://schema.org/legislationLegalValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.LegalValueLevel


@dataclass(frozen=True)
class lodgingUnitDescription(RdfProperty):
    term = RdfTerm(
        "lodgingUnitDescription",
        "http://schema.org/lodgingUnitDescription",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class blogPosts(RdfProperty):
    term = RdfTerm(
        "blogPosts", "http://schema.org/blogPosts", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.BlogPosting


@dataclass(frozen=True)
class departurePlatform(RdfProperty):
    term = RdfTerm(
        "departurePlatform",
        "http://schema.org/departurePlatform",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class albumRelease(RdfProperty):
    term = RdfTerm(
        "albumRelease",
        "http://schema.org/albumRelease",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MusicRelease


@dataclass(frozen=True)
class mobileUrl(RdfProperty):
    term = RdfTerm("mobileUrl", "http://schema.org/mobileUrl", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class headline(RdfProperty):
    term = RdfTerm(
        "headline", "http://schema.org/headline", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class wheelbase(RdfProperty):
    term = RdfTerm(
        "wheelbase", "http://schema.org/wheelbase", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class appliesToPaymentMethod(RdfProperty):
    term = RdfTerm(
        "appliesToPaymentMethod",
        "http://schema.org/appliesToPaymentMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PaymentMethod


@dataclass(frozen=True)
class labelDetails(RdfProperty):
    term = RdfTerm(
        "labelDetails",
        "http://schema.org/labelDetails",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class originalMediaContextDescription(RdfProperty):
    term = RdfTerm(
        "originalMediaContextDescription",
        "http://schema.org/originalMediaContextDescription",
        ["1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class category(RdfProperty):
    term = RdfTerm(
        "category", "http://schema.org/category", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: (
        schemaorg.CategoryCode
        | URL
        | schemaorg.Thing
        | schemaorg.PhysicalActivityCategory
        | Text
    )


@dataclass(frozen=True)
class includedInDataCatalog(RdfProperty):
    term = RdfTerm(
        "includedInDataCatalog",
        "http://schema.org/includedInDataCatalog",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DataCatalog


@dataclass(frozen=True)
class distance(RdfProperty):
    term = RdfTerm(
        "distance", "http://schema.org/distance", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Distance


@dataclass(frozen=True)
class actionPlatform(RdfProperty):
    term = RdfTerm(
        "actionPlatform",
        "http://schema.org/actionPlatform",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DigitalPlatformEnumeration | URL


@dataclass(frozen=True)
class digitalSourceType(RdfProperty):
    term = RdfTerm("digitalSourceType", "http://schema.org/digitalSourceType", [])
    object: schemaorg.IPTCDigitalSourceEnumeration


@dataclass(frozen=True)
class workFeatured(RdfProperty):
    term = RdfTerm(
        "workFeatured",
        "http://schema.org/workFeatured",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class recordLabel(RdfProperty):
    term = RdfTerm(
        "recordLabel",
        "http://schema.org/recordLabel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class isEncodedByBioChemEntity(RdfProperty):
    term = RdfTerm(
        "isEncodedByBioChemEntity",
        "http://schema.org/isEncodedByBioChemEntity",
        ["1.2-DRAFT"],
    )
    object: schemaorg.Gene


@dataclass(frozen=True)
class costCategory(RdfProperty):
    term = RdfTerm(
        "costCategory",
        "http://schema.org/costCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DrugCostCategory


@dataclass(frozen=True)
class question(RdfProperty):
    term = RdfTerm(
        "question", "http://schema.org/question", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Question


@dataclass(frozen=True)
class measurementQualifier(RdfProperty):
    term = RdfTerm(
        "measurementQualifier", "http://schema.org/measurementQualifier", ["1.2-DRAFT"]
    )
    object: schemaorg.Enumeration


@dataclass(frozen=True)
class asin(RdfProperty):
    term = RdfTerm("asin", "http://schema.org/asin", ["1.2-DRAFT"])
    object: Text | URL


@dataclass(frozen=True)
class suggestedAnswer(RdfProperty):
    term = RdfTerm(
        "suggestedAnswer",
        "http://schema.org/suggestedAnswer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ItemList | schemaorg.Answer


@dataclass(frozen=True)
class postalCodeRange(RdfProperty):
    term = RdfTerm(
        "postalCodeRange", "http://schema.org/postalCodeRange", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.PostalCodeRangeSpecification


@dataclass(frozen=True)
class cvdNumC19HospPats(RdfProperty):
    term = RdfTerm(
        "cvdNumC19HospPats", "http://schema.org/cvdNumC19HospPats", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class assemblyVersion(RdfProperty):
    term = RdfTerm(
        "assemblyVersion",
        "http://schema.org/assemblyVersion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class runtime(RdfProperty):
    term = RdfTerm(
        "runtime", "http://schema.org/runtime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class isPlanForApartment(RdfProperty):
    term = RdfTerm(
        "isPlanForApartment",
        "http://schema.org/isPlanForApartment",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Accommodation


@dataclass(frozen=True)
class hasBroadcastChannel(RdfProperty):
    term = RdfTerm(
        "hasBroadcastChannel",
        "http://schema.org/hasBroadcastChannel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BroadcastChannel


@dataclass(frozen=True)
class learningResourceType(RdfProperty):
    term = RdfTerm(
        "learningResourceType",
        "http://schema.org/learningResourceType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DefinedTerm | Text


@dataclass(frozen=True)
class relatedTo(RdfProperty):
    term = RdfTerm(
        "relatedTo", "http://schema.org/relatedTo", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class gameServer(RdfProperty):
    term = RdfTerm(
        "gameServer", "http://schema.org/gameServer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.GameServer


@dataclass(frozen=True)
class foundingDate(RdfProperty):
    term = RdfTerm(
        "foundingDate",
        "http://schema.org/foundingDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class prepTime(RdfProperty):
    term = RdfTerm(
        "prepTime", "http://schema.org/prepTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class validIn(RdfProperty):
    term = RdfTerm(
        "validIn", "http://schema.org/validIn", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.AdministrativeArea


@dataclass(frozen=True)
class transmissionMethod(RdfProperty):
    term = RdfTerm(
        "transmissionMethod",
        "http://schema.org/transmissionMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class itinerary(RdfProperty):
    term = RdfTerm(
        "itinerary", "http://schema.org/itinerary", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ItemList | schemaorg.Place


@dataclass(frozen=True)
class alternativeHeadline(RdfProperty):
    term = RdfTerm(
        "alternativeHeadline",
        "http://schema.org/alternativeHeadline",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class numberOfPlayers(RdfProperty):
    term = RdfTerm(
        "numberOfPlayers",
        "http://schema.org/numberOfPlayers",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class numberOfCredits(RdfProperty):
    term = RdfTerm(
        "numberOfCredits", "http://schema.org/numberOfCredits", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.StructuredValue | Integer


@dataclass(frozen=True)
class aggregateElement(RdfProperty):
    term = RdfTerm("aggregateElement", "http://schema.org/aggregateElement", [])
    object: schemaorg.Thing


@dataclass(frozen=True)
class playersOnline(RdfProperty):
    term = RdfTerm(
        "playersOnline",
        "http://schema.org/playersOnline",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class maps(RdfProperty):
    term = RdfTerm("maps", "http://schema.org/maps", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: URL


@dataclass(frozen=True)
class birthDate(RdfProperty):
    term = RdfTerm(
        "birthDate", "http://schema.org/birthDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date


@dataclass(frozen=True)
class temporal(RdfProperty):
    term = RdfTerm(
        "temporal", "http://schema.org/temporal", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime | Text


@dataclass(frozen=True)
class deliveryTime(RdfProperty):
    term = RdfTerm(
        "deliveryTime", "http://schema.org/deliveryTime", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ShippingDeliveryTime


@dataclass(frozen=True)
class serviceLocation(RdfProperty):
    term = RdfTerm(
        "serviceLocation",
        "http://schema.org/serviceLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class performer(RdfProperty):
    term = RdfTerm(
        "performer", "http://schema.org/performer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class seatSection(RdfProperty):
    term = RdfTerm(
        "seatSection",
        "http://schema.org/seatSection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class result(RdfProperty):
    term = RdfTerm(
        "result", "http://schema.org/result", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class cookingMethod(RdfProperty):
    term = RdfTerm(
        "cookingMethod",
        "http://schema.org/cookingMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class subStageSuffix(RdfProperty):
    term = RdfTerm(
        "subStageSuffix",
        "http://schema.org/subStageSuffix",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class opens(RdfProperty):
    term = RdfTerm(
        "opens", "http://schema.org/opens", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Time


@dataclass(frozen=True)
class freeShippingThreshold(RdfProperty):
    term = RdfTerm(
        "freeShippingThreshold",
        "http://schema.org/freeShippingThreshold",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DeliveryChargeSpecification | schemaorg.MonetaryAmount


@dataclass(frozen=True)
class primaryImageOfPage(RdfProperty):
    term = RdfTerm(
        "primaryImageOfPage",
        "http://schema.org/primaryImageOfPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ImageObject


@dataclass(frozen=True)
class color(RdfProperty):
    term = RdfTerm(
        "color", "http://schema.org/color", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class acceptedAnswer(RdfProperty):
    term = RdfTerm(
        "acceptedAnswer",
        "http://schema.org/acceptedAnswer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Answer | schemaorg.ItemList


@dataclass(frozen=True)
class constraintProperty(RdfProperty):
    term = RdfTerm(
        "constraintProperty", "http://schema.org/constraintProperty", ["1.2-DRAFT"]
    )
    object: URL | schemaorg.Property


@dataclass(frozen=True)
class streetAddress(RdfProperty):
    term = RdfTerm(
        "streetAddress",
        "http://schema.org/streetAddress",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class isBasedOnUrl(RdfProperty):
    term = RdfTerm(
        "isBasedOnUrl",
        "http://schema.org/isBasedOnUrl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork | schemaorg.Product


@dataclass(frozen=True)
class recipient(RdfProperty):
    term = RdfTerm(
        "recipient", "http://schema.org/recipient", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: (
        schemaorg.Organization
        | schemaorg.Audience
        | schemaorg.ContactPoint
        | schemaorg.Person
    )


@dataclass(frozen=True)
class associatedMedia(RdfProperty):
    term = RdfTerm(
        "associatedMedia",
        "http://schema.org/associatedMedia",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MediaObject


@dataclass(frozen=True)
class dataset(RdfProperty):
    term = RdfTerm(
        "dataset", "http://schema.org/dataset", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Dataset


@dataclass(frozen=True)
class studyDesign(RdfProperty):
    term = RdfTerm(
        "studyDesign",
        "http://schema.org/studyDesign",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalObservationalStudyDesign


@dataclass(frozen=True)
class riskFactor(RdfProperty):
    term = RdfTerm(
        "riskFactor", "http://schema.org/riskFactor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalRiskFactor


@dataclass(frozen=True)
class servicePostalAddress(RdfProperty):
    term = RdfTerm(
        "servicePostalAddress",
        "http://schema.org/servicePostalAddress",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PostalAddress


@dataclass(frozen=True)
class commentCount(RdfProperty):
    term = RdfTerm(
        "commentCount",
        "http://schema.org/commentCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class hasVariant(RdfProperty):
    term = RdfTerm("hasVariant", "http://schema.org/hasVariant", ["1.1", "1.2-DRAFT"])
    object: schemaorg.Product


@dataclass(frozen=True)
class legislationTransposes(RdfProperty):
    term = RdfTerm(
        "legislationTransposes",
        "http://schema.org/legislationTransposes",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Legislation


@dataclass(frozen=True)
class speechToTextMarkup(RdfProperty):
    term = RdfTerm(
        "speechToTextMarkup",
        "http://schema.org/speechToTextMarkup",
        ["1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class cholesterolContent(RdfProperty):
    term = RdfTerm(
        "cholesterolContent",
        "http://schema.org/cholesterolContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class busNumber(RdfProperty):
    term = RdfTerm(
        "busNumber", "http://schema.org/busNumber", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class certificationRating(RdfProperty):
    term = RdfTerm("certificationRating", "http://schema.org/certificationRating", [])
    object: schemaorg.Rating


@dataclass(frozen=True)
class feesAndCommissionsSpecification(RdfProperty):
    term = RdfTerm(
        "feesAndCommissionsSpecification",
        "http://schema.org/feesAndCommissionsSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class infectiousAgent(RdfProperty):
    term = RdfTerm(
        "infectiousAgent",
        "http://schema.org/infectiousAgent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class incentiveCompensation(RdfProperty):
    term = RdfTerm(
        "incentiveCompensation",
        "http://schema.org/incentiveCompensation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class broadcastOfEvent(RdfProperty):
    term = RdfTerm(
        "broadcastOfEvent",
        "http://schema.org/broadcastOfEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class sportsEvent(RdfProperty):
    term = RdfTerm(
        "sportsEvent",
        "http://schema.org/sportsEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SportsEvent


@dataclass(frozen=True)
class dateCreated(RdfProperty):
    term = RdfTerm(
        "dateCreated",
        "http://schema.org/dateCreated",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date | DateTime


@dataclass(frozen=True)
class toRecipient(RdfProperty):
    term = RdfTerm(
        "toRecipient",
        "http://schema.org/toRecipient",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: (
        schemaorg.Organization
        | schemaorg.Audience
        | schemaorg.ContactPoint
        | schemaorg.Person
    )


@dataclass(frozen=True)
class medicineSystem(RdfProperty):
    term = RdfTerm(
        "medicineSystem",
        "http://schema.org/medicineSystem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicineSystem


@dataclass(frozen=True)
class unitText(RdfProperty):
    term = RdfTerm(
        "unitText", "http://schema.org/unitText", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class frequency(RdfProperty):
    term = RdfTerm(
        "frequency", "http://schema.org/frequency", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class orderStatus(RdfProperty):
    term = RdfTerm(
        "orderStatus",
        "http://schema.org/orderStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OrderStatus


@dataclass(frozen=True)
class addOn(RdfProperty):
    term = RdfTerm(
        "addOn", "http://schema.org/addOn", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Offer


@dataclass(frozen=True)
class acceptedOffer(RdfProperty):
    term = RdfTerm(
        "acceptedOffer",
        "http://schema.org/acceptedOffer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Offer


@dataclass(frozen=True)
class artEdition(RdfProperty):
    term = RdfTerm(
        "artEdition", "http://schema.org/artEdition", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer | Text


@dataclass(frozen=True)
class secondaryPrevention(RdfProperty):
    term = RdfTerm(
        "secondaryPrevention",
        "http://schema.org/secondaryPrevention",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTherapy


@dataclass(frozen=True)
class yearBuilt(RdfProperty):
    term = RdfTerm("yearBuilt", "http://schema.org/yearBuilt", ["1.1", "1.2-DRAFT"])
    object: Number


@dataclass(frozen=True)
class sharedContent(RdfProperty):
    term = RdfTerm(
        "sharedContent",
        "http://schema.org/sharedContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class certificationStatus(RdfProperty):
    term = RdfTerm("certificationStatus", "http://schema.org/certificationStatus", [])
    object: schemaorg.CertificationStatusEnumeration


@dataclass(frozen=True)
class subEvents(RdfProperty):
    term = RdfTerm(
        "subEvents", "http://schema.org/subEvents", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class fileFormat(RdfProperty):
    term = RdfTerm(
        "fileFormat", "http://schema.org/fileFormat", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class propertyID(RdfProperty):
    term = RdfTerm(
        "propertyID", "http://schema.org/propertyID", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class teaches(RdfProperty):
    term = RdfTerm("teaches", "http://schema.org/teaches", ["1.1", "1.2-DRAFT"])
    object: schemaorg.DefinedTerm | Text


@dataclass(frozen=True)
class regionsAllowed(RdfProperty):
    term = RdfTerm(
        "regionsAllowed",
        "http://schema.org/regionsAllowed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class addressCountry(RdfProperty):
    term = RdfTerm(
        "addressCountry",
        "http://schema.org/addressCountry",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.Country


@dataclass(frozen=True)
class validUntil(RdfProperty):
    term = RdfTerm(
        "validUntil", "http://schema.org/validUntil", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date


@dataclass(frozen=True)
class baseSalary(RdfProperty):
    term = RdfTerm(
        "baseSalary", "http://schema.org/baseSalary", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.PriceSpecification | Number | schemaorg.MonetaryAmount


@dataclass(frozen=True)
class productSupported(RdfProperty):
    term = RdfTerm(
        "productSupported",
        "http://schema.org/productSupported",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Product | Text


@dataclass(frozen=True)
class hasCourseInstance(RdfProperty):
    term = RdfTerm(
        "hasCourseInstance",
        "http://schema.org/hasCourseInstance",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CourseInstance


@dataclass(frozen=True)
class merchantReturnDays(RdfProperty):
    term = RdfTerm(
        "merchantReturnDays",
        "http://schema.org/merchantReturnDays",
        ["1.1", "1.2-DRAFT"],
    )
    object: Date | Integer | DateTime


@dataclass(frozen=True)
class sportsActivityLocation(RdfProperty):
    term = RdfTerm(
        "sportsActivityLocation",
        "http://schema.org/sportsActivityLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SportsActivityLocation


@dataclass(frozen=True)
class countryOfLastProcessing(RdfProperty):
    term = RdfTerm(
        "countryOfLastProcessing",
        "http://schema.org/countryOfLastProcessing",
        ["1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class availableDeliveryMethod(RdfProperty):
    term = RdfTerm(
        "availableDeliveryMethod",
        "http://schema.org/availableDeliveryMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DeliveryMethod


@dataclass(frozen=True)
class guideline(RdfProperty):
    term = RdfTerm(
        "guideline", "http://schema.org/guideline", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalGuideline


@dataclass(frozen=True)
class accessibilityControl(RdfProperty):
    term = RdfTerm(
        "accessibilityControl",
        "http://schema.org/accessibilityControl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class interestRate(RdfProperty):
    term = RdfTerm(
        "interestRate",
        "http://schema.org/interestRate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class isPartOf(RdfProperty):
    term = RdfTerm(
        "isPartOf", "http://schema.org/isPartOf", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class transcript(RdfProperty):
    term = RdfTerm(
        "transcript", "http://schema.org/transcript", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class containsSeason(RdfProperty):
    term = RdfTerm(
        "containsSeason",
        "http://schema.org/containsSeason",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWorkSeason


@dataclass(frozen=True)
class geoRadius(RdfProperty):
    term = RdfTerm(
        "geoRadius", "http://schema.org/geoRadius", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Distance | Text | Number


@dataclass(frozen=True)
class legislationResponsible(RdfProperty):
    term = RdfTerm(
        "legislationResponsible",
        "http://schema.org/legislationResponsible",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class homeLocation(RdfProperty):
    term = RdfTerm(
        "homeLocation",
        "http://schema.org/homeLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPoint | schemaorg.Place


@dataclass(frozen=True)
class legislationCorrects(RdfProperty):
    term = RdfTerm("legislationCorrects", "http://schema.org/legislationCorrects", [])
    object: schemaorg.Legislation


@dataclass(frozen=True)
class speed(RdfProperty):
    term = RdfTerm(
        "speed", "http://schema.org/speed", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class logo(RdfProperty):
    term = RdfTerm("logo", "http://schema.org/logo", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: URL | schemaorg.ImageObject


@dataclass(frozen=True)
class employee(RdfProperty):
    term = RdfTerm(
        "employee", "http://schema.org/employee", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class subjectOf(RdfProperty):
    term = RdfTerm(
        "subjectOf", "http://schema.org/subjectOf", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Event | schemaorg.CreativeWork


@dataclass(frozen=True)
class claimInterpreter(RdfProperty):
    term = RdfTerm(
        "claimInterpreter", "http://schema.org/claimInterpreter", ["1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class pagination(RdfProperty):
    term = RdfTerm(
        "pagination", "http://schema.org/pagination", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class afterMedia(RdfProperty):
    term = RdfTerm(
        "afterMedia", "http://schema.org/afterMedia", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MediaObject | URL


@dataclass(frozen=True)
class alumniOf(RdfProperty):
    term = RdfTerm(
        "alumniOf", "http://schema.org/alumniOf", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.EducationalOrganization


@dataclass(frozen=True)
class lender(RdfProperty):
    term = RdfTerm(
        "lender", "http://schema.org/lender", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class modelDate(RdfProperty):
    term = RdfTerm(
        "modelDate", "http://schema.org/modelDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date


@dataclass(frozen=True)
class parentTaxon(RdfProperty):
    term = RdfTerm("parentTaxon", "http://schema.org/parentTaxon", ["1.2-DRAFT"])
    object: schemaorg.Taxon | Text | URL


@dataclass(frozen=True)
class additionalNumberOfGuests(RdfProperty):
    term = RdfTerm(
        "additionalNumberOfGuests",
        "http://schema.org/additionalNumberOfGuests",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class iupacName(RdfProperty):
    term = RdfTerm("iupacName", "http://schema.org/iupacName", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class addressLocality(RdfProperty):
    term = RdfTerm(
        "addressLocality",
        "http://schema.org/addressLocality",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class contactPoints(RdfProperty):
    term = RdfTerm(
        "contactPoints",
        "http://schema.org/contactPoints",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPoint


@dataclass(frozen=True)
class roofLoad(RdfProperty):
    term = RdfTerm(
        "roofLoad", "http://schema.org/roofLoad", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class legalName(RdfProperty):
    term = RdfTerm(
        "legalName", "http://schema.org/legalName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class lodgingUnitType(RdfProperty):
    term = RdfTerm(
        "lodgingUnitType",
        "http://schema.org/lodgingUnitType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QualitativeValue


@dataclass(frozen=True)
class activityFrequency(RdfProperty):
    term = RdfTerm(
        "activityFrequency",
        "http://schema.org/activityFrequency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class isInvolvedInBiologicalProcess(RdfProperty):
    term = RdfTerm(
        "isInvolvedInBiologicalProcess",
        "http://schema.org/isInvolvedInBiologicalProcess",
        ["1.2-DRAFT"],
    )
    object: schemaorg.PropertyValue | schemaorg.DefinedTerm | URL


@dataclass(frozen=True)
class cheatCode(RdfProperty):
    term = RdfTerm(
        "cheatCode", "http://schema.org/cheatCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class jobBenefits(RdfProperty):
    term = RdfTerm(
        "jobBenefits",
        "http://schema.org/jobBenefits",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class subTest(RdfProperty):
    term = RdfTerm(
        "subTest", "http://schema.org/subTest", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalTest


@dataclass(frozen=True)
class competitor(RdfProperty):
    term = RdfTerm(
        "competitor", "http://schema.org/competitor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.SportsTeam


@dataclass(frozen=True)
class alumni(RdfProperty):
    term = RdfTerm(
        "alumni", "http://schema.org/alumni", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class numberOfSeasons(RdfProperty):
    term = RdfTerm(
        "numberOfSeasons",
        "http://schema.org/numberOfSeasons",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class numberOfRooms(RdfProperty):
    term = RdfTerm(
        "numberOfRooms",
        "http://schema.org/numberOfRooms",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class orderNumber(RdfProperty):
    term = RdfTerm(
        "orderNumber",
        "http://schema.org/orderNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class athlete(RdfProperty):
    term = RdfTerm(
        "athlete", "http://schema.org/athlete", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class associatedDisease(RdfProperty):
    term = RdfTerm(
        "associatedDisease", "http://schema.org/associatedDisease", ["1.2-DRAFT"]
    )
    object: schemaorg.MedicalCondition | URL | schemaorg.PropertyValue


@dataclass(frozen=True)
class accessibilityAPI(RdfProperty):
    term = RdfTerm(
        "accessibilityAPI",
        "http://schema.org/accessibilityAPI",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class relatedTherapy(RdfProperty):
    term = RdfTerm(
        "relatedTherapy",
        "http://schema.org/relatedTherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTherapy


@dataclass(frozen=True)
class returnMethod(RdfProperty):
    term = RdfTerm("returnMethod", "http://schema.org/returnMethod", ["1.2-DRAFT"])
    object: schemaorg.ReturnMethodEnumeration


@dataclass(frozen=True)
class issuedBy(RdfProperty):
    term = RdfTerm(
        "issuedBy", "http://schema.org/issuedBy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class contentReferenceTime(RdfProperty):
    term = RdfTerm(
        "contentReferenceTime",
        "http://schema.org/contentReferenceTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class amount(RdfProperty):
    term = RdfTerm(
        "amount", "http://schema.org/amount", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MonetaryAmount | Number


@dataclass(frozen=True)
class identifyingExam(RdfProperty):
    term = RdfTerm(
        "identifyingExam",
        "http://schema.org/identifyingExam",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PhysicalExam


@dataclass(frozen=True)
class syllabusSections(RdfProperty):
    term = RdfTerm(
        "syllabusSections", "http://schema.org/syllabusSections", ["1.2-DRAFT"]
    )
    object: schemaorg.Syllabus


@dataclass(frozen=True)
class targetPlatform(RdfProperty):
    term = RdfTerm(
        "targetPlatform",
        "http://schema.org/targetPlatform",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class shippingOrigin(RdfProperty):
    term = RdfTerm("shippingOrigin", "http://schema.org/shippingOrigin", ["1.2-DRAFT"])
    object: schemaorg.DefinedRegion


@dataclass(frozen=True)
class possibleTreatment(RdfProperty):
    term = RdfTerm(
        "possibleTreatment",
        "http://schema.org/possibleTreatment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTherapy


@dataclass(frozen=True)
class performTime(RdfProperty):
    term = RdfTerm(
        "performTime",
        "http://schema.org/performTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class partOfEpisode(RdfProperty):
    term = RdfTerm(
        "partOfEpisode",
        "http://schema.org/partOfEpisode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Episode


@dataclass(frozen=True)
class ratingExplanation(RdfProperty):
    term = RdfTerm(
        "ratingExplanation",
        "http://schema.org/ratingExplanation",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class newsUpdatesAndGuidelines(RdfProperty):
    term = RdfTerm(
        "newsUpdatesAndGuidelines",
        "http://schema.org/newsUpdatesAndGuidelines",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.WebContent


@dataclass(frozen=True)
class percentile90(RdfProperty):
    term = RdfTerm(
        "percentile90", "http://schema.org/percentile90", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class availableOnDevice(RdfProperty):
    term = RdfTerm(
        "availableOnDevice",
        "http://schema.org/availableOnDevice",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class albums(RdfProperty):
    term = RdfTerm(
        "albums", "http://schema.org/albums", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicAlbum


@dataclass(frozen=True)
class lyrics(RdfProperty):
    term = RdfTerm(
        "lyrics", "http://schema.org/lyrics", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class postOp(RdfProperty):
    term = RdfTerm(
        "postOp", "http://schema.org/postOp", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class orderDate(RdfProperty):
    term = RdfTerm(
        "orderDate", "http://schema.org/orderDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime | Date


@dataclass(frozen=True)
class orderItemNumber(RdfProperty):
    term = RdfTerm(
        "orderItemNumber",
        "http://schema.org/orderItemNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class stupidProperty(RdfProperty):
    term = RdfTerm(
        "stupidProperty",
        "http://schema.org/stupidProperty",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class providesBroadcastService(RdfProperty):
    term = RdfTerm(
        "providesBroadcastService",
        "http://schema.org/providesBroadcastService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BroadcastService


@dataclass(frozen=True)
class numberOfAirbags(RdfProperty):
    term = RdfTerm(
        "numberOfAirbags",
        "http://schema.org/numberOfAirbags",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | Text


@dataclass(frozen=True)
class naics(RdfProperty):
    term = RdfTerm(
        "naics", "http://schema.org/naics", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class readBy(RdfProperty):
    term = RdfTerm(
        "readBy", "http://schema.org/readBy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class healthPlanDrugOption(RdfProperty):
    term = RdfTerm(
        "healthPlanDrugOption",
        "http://schema.org/healthPlanDrugOption",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class gamePlatform(RdfProperty):
    term = RdfTerm(
        "gamePlatform",
        "http://schema.org/gamePlatform",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.Thing | Text


@dataclass(frozen=True)
class answerCount(RdfProperty):
    term = RdfTerm(
        "answerCount",
        "http://schema.org/answerCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class item(RdfProperty):
    term = RdfTerm("item", "http://schema.org/item", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.Thing


@dataclass(frozen=True)
class flightNumber(RdfProperty):
    term = RdfTerm(
        "flightNumber",
        "http://schema.org/flightNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class multipleValues(RdfProperty):
    term = RdfTerm(
        "multipleValues",
        "http://schema.org/multipleValues",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class legislationDate(RdfProperty):
    term = RdfTerm(
        "legislationDate",
        "http://schema.org/legislationDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class mechanismOfAction(RdfProperty):
    term = RdfTerm(
        "mechanismOfAction",
        "http://schema.org/mechanismOfAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class workPerformed(RdfProperty):
    term = RdfTerm(
        "workPerformed",
        "http://schema.org/workPerformed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class customerRemorseReturnFees(RdfProperty):
    term = RdfTerm(
        "customerRemorseReturnFees",
        "http://schema.org/customerRemorseReturnFees",
        ["1.2-DRAFT"],
    )
    object: schemaorg.ReturnFeesEnumeration


@dataclass(frozen=True)
class offeredBy(RdfProperty):
    term = RdfTerm(
        "offeredBy", "http://schema.org/offeredBy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class bankAccountType(RdfProperty):
    term = RdfTerm(
        "bankAccountType",
        "http://schema.org/bankAccountType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class duration(RdfProperty):
    term = RdfTerm(
        "duration", "http://schema.org/duration", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | schemaorg.Duration


@dataclass(frozen=True)
class fromLocation(RdfProperty):
    term = RdfTerm(
        "fromLocation",
        "http://schema.org/fromLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class accelerationTime(RdfProperty):
    term = RdfTerm(
        "accelerationTime",
        "http://schema.org/accelerationTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class hasDefinedTerm(RdfProperty):
    term = RdfTerm(
        "hasDefinedTerm",
        "http://schema.org/hasDefinedTerm",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DefinedTerm


@dataclass(frozen=True)
class childTaxon(RdfProperty):
    term = RdfTerm("childTaxon", "http://schema.org/childTaxon", ["1.2-DRAFT"])
    object: Text | URL | schemaorg.Taxon


@dataclass(frozen=True)
class study(RdfProperty):
    term = RdfTerm(
        "study", "http://schema.org/study", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalStudy


@dataclass(frozen=True)
class gettingTestedInfo(RdfProperty):
    term = RdfTerm(
        "gettingTestedInfo", "http://schema.org/gettingTestedInfo", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.WebContent | URL


@dataclass(frozen=True)
class artform(RdfProperty):
    term = RdfTerm(
        "artform", "http://schema.org/artform", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class isTierOf(RdfProperty):
    term = RdfTerm("isTierOf", "http://schema.org/isTierOf", [])
    object: schemaorg.MemberProgram


@dataclass(frozen=True)
class query(RdfProperty):
    term = RdfTerm(
        "query", "http://schema.org/query", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class healthPlanCopay(RdfProperty):
    term = RdfTerm(
        "healthPlanCopay",
        "http://schema.org/healthPlanCopay",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PriceSpecification


@dataclass(frozen=True)
class volumeNumber(RdfProperty):
    term = RdfTerm(
        "volumeNumber",
        "http://schema.org/volumeNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer | Text


@dataclass(frozen=True)
class stageAsNumber(RdfProperty):
    term = RdfTerm(
        "stageAsNumber",
        "http://schema.org/stageAsNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class geoContains(RdfProperty):
    term = RdfTerm(
        "geoContains", "http://schema.org/geoContains", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place | schemaorg.GeospatialGeometry


@dataclass(frozen=True)
class organizer(RdfProperty):
    term = RdfTerm(
        "organizer", "http://schema.org/organizer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class estimatesRiskOf(RdfProperty):
    term = RdfTerm(
        "estimatesRiskOf",
        "http://schema.org/estimatesRiskOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEntity


@dataclass(frozen=True)
class loser(RdfProperty):
    term = RdfTerm(
        "loser", "http://schema.org/loser", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class validThrough(RdfProperty):
    term = RdfTerm(
        "validThrough",
        "http://schema.org/validThrough",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date | DateTime


@dataclass(frozen=True)
class torque(RdfProperty):
    term = RdfTerm(
        "torque", "http://schema.org/torque", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class rxcui(RdfProperty):
    term = RdfTerm(
        "rxcui", "http://schema.org/rxcui", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class offerCount(RdfProperty):
    term = RdfTerm(
        "offerCount", "http://schema.org/offerCount", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer


@dataclass(frozen=True)
class broadcaster(RdfProperty):
    term = RdfTerm(
        "broadcaster",
        "http://schema.org/broadcaster",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class monthlyMinimumRepaymentAmount(RdfProperty):
    term = RdfTerm(
        "monthlyMinimumRepaymentAmount",
        "http://schema.org/monthlyMinimumRepaymentAmount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount | Number


@dataclass(frozen=True)
class isBasedOn(RdfProperty):
    term = RdfTerm(
        "isBasedOn", "http://schema.org/isBasedOn", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.CreativeWork | schemaorg.Product


@dataclass(frozen=True)
class itemListOrder(RdfProperty):
    term = RdfTerm(
        "itemListOrder",
        "http://schema.org/itemListOrder",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.ItemListOrderType


@dataclass(frozen=True)
class geo(RdfProperty):
    term = RdfTerm("geo", "http://schema.org/geo", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.GeoCoordinates | schemaorg.GeoShape


@dataclass(frozen=True)
class printPage(RdfProperty):
    term = RdfTerm(
        "printPage", "http://schema.org/printPage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class alternateName(RdfProperty):
    term = RdfTerm(
        "alternateName",
        "http://schema.org/alternateName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class timeOfDay(RdfProperty):
    term = RdfTerm("timeOfDay", "http://schema.org/timeOfDay", ["1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class publicAccess(RdfProperty):
    term = RdfTerm(
        "publicAccess",
        "http://schema.org/publicAccess",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class actor(RdfProperty):
    term = RdfTerm(
        "actor", "http://schema.org/actor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.PerformingGroup


@dataclass(frozen=True)
class performers(RdfProperty):
    term = RdfTerm(
        "performers", "http://schema.org/performers", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class owns(RdfProperty):
    term = RdfTerm("owns", "http://schema.org/owns", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.Product | schemaorg.OwnershipInfo


@dataclass(frozen=True)
class seasonNumber(RdfProperty):
    term = RdfTerm(
        "seasonNumber",
        "http://schema.org/seasonNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer | Text


@dataclass(frozen=True)
class valueAddedTaxIncluded(RdfProperty):
    term = RdfTerm(
        "valueAddedTaxIncluded",
        "http://schema.org/valueAddedTaxIncluded",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class requiredMaxAge(RdfProperty):
    term = RdfTerm(
        "requiredMaxAge",
        "http://schema.org/requiredMaxAge",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class worstRating(RdfProperty):
    term = RdfTerm(
        "worstRating",
        "http://schema.org/worstRating",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | Text


@dataclass(frozen=True)
class callSign(RdfProperty):
    term = RdfTerm(
        "callSign", "http://schema.org/callSign", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class cvdNumBedsOcc(RdfProperty):
    term = RdfTerm(
        "cvdNumBedsOcc", "http://schema.org/cvdNumBedsOcc", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class variesBy(RdfProperty):
    term = RdfTerm("variesBy", "http://schema.org/variesBy", ["1.1", "1.2-DRAFT"])
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class termCode(RdfProperty):
    term = RdfTerm(
        "termCode", "http://schema.org/termCode", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class creativeWorkStatus(RdfProperty):
    term = RdfTerm(
        "creativeWorkStatus",
        "http://schema.org/creativeWorkStatus",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DefinedTerm | Text


@dataclass(frozen=True)
class dateRead(RdfProperty):
    term = RdfTerm(
        "dateRead", "http://schema.org/dateRead", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date | DateTime


@dataclass(frozen=True)
class device(RdfProperty):
    term = RdfTerm(
        "device", "http://schema.org/device", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class departureGate(RdfProperty):
    term = RdfTerm(
        "departureGate",
        "http://schema.org/departureGate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class award(RdfProperty):
    term = RdfTerm(
        "award", "http://schema.org/award", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class estimatedSalary(RdfProperty):
    term = RdfTerm(
        "estimatedSalary",
        "http://schema.org/estimatedSalary",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmountDistribution | Number | schemaorg.MonetaryAmount


@dataclass(frozen=True)
class educationalUse(RdfProperty):
    term = RdfTerm(
        "educationalUse",
        "http://schema.org/educationalUse",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class drug(RdfProperty):
    term = RdfTerm("drug", "http://schema.org/drug", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.Drug


@dataclass(frozen=True)
class returnPolicyCategory(RdfProperty):
    term = RdfTerm(
        "returnPolicyCategory",
        "http://schema.org/returnPolicyCategory",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MerchantReturnEnumeration


@dataclass(frozen=True)
class sensoryUnit(RdfProperty):
    term = RdfTerm(
        "sensoryUnit",
        "http://schema.org/sensoryUnit",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalStructure | schemaorg.SuperficialAnatomy


@dataclass(frozen=True)
class isFamilyFriendly(RdfProperty):
    term = RdfTerm(
        "isFamilyFriendly",
        "http://schema.org/isFamilyFriendly",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class namedPosition(RdfProperty):
    term = RdfTerm(
        "namedPosition",
        "http://schema.org/namedPosition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | Text


@dataclass(frozen=True)
class activeIngredient(RdfProperty):
    term = RdfTerm(
        "activeIngredient",
        "http://schema.org/activeIngredient",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class costOrigin(RdfProperty):
    term = RdfTerm(
        "costOrigin", "http://schema.org/costOrigin", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class healthPlanNetworkId(RdfProperty):
    term = RdfTerm(
        "healthPlanNetworkId",
        "http://schema.org/healthPlanNetworkId",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class trackingNumber(RdfProperty):
    term = RdfTerm(
        "trackingNumber",
        "http://schema.org/trackingNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class tongueWeight(RdfProperty):
    term = RdfTerm(
        "tongueWeight",
        "http://schema.org/tongueWeight",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class screenshot(RdfProperty):
    term = RdfTerm(
        "screenshot", "http://schema.org/screenshot", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.ImageObject


@dataclass(frozen=True)
class interactivityType(RdfProperty):
    term = RdfTerm(
        "interactivityType",
        "http://schema.org/interactivityType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class releaseDate(RdfProperty):
    term = RdfTerm(
        "releaseDate",
        "http://schema.org/releaseDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class activityDuration(RdfProperty):
    term = RdfTerm(
        "activityDuration",
        "http://schema.org/activityDuration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class brand(RdfProperty):
    term = RdfTerm(
        "brand", "http://schema.org/brand", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Brand | schemaorg.Organization


@dataclass(frozen=True)
class hasHealthAspect(RdfProperty):
    term = RdfTerm(
        "hasHealthAspect",
        "http://schema.org/hasHealthAspect",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.HealthAspectEnumeration


@dataclass(frozen=True)
class value(RdfProperty):
    term = RdfTerm(
        "value", "http://schema.org/value", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.StructuredValue | Number | Boolean | Text


@dataclass(frozen=True)
class dateIssued(RdfProperty):
    term = RdfTerm(
        "dateIssued", "http://schema.org/dateIssued", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date | DateTime


@dataclass(frozen=True)
class transFatContent(RdfProperty):
    term = RdfTerm(
        "transFatContent",
        "http://schema.org/transFatContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class box(RdfProperty):
    term = RdfTerm("box", "http://schema.org/box", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class publication(RdfProperty):
    term = RdfTerm(
        "publication",
        "http://schema.org/publication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PublicationEvent


@dataclass(frozen=True)
class inProductGroupWithID(RdfProperty):
    term = RdfTerm(
        "inProductGroupWithID",
        "http://schema.org/inProductGroupWithID",
        ["1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class followee(RdfProperty):
    term = RdfTerm(
        "followee", "http://schema.org/followee", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class providerMobility(RdfProperty):
    term = RdfTerm(
        "providerMobility",
        "http://schema.org/providerMobility",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class children(RdfProperty):
    term = RdfTerm(
        "children", "http://schema.org/children", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class seatingCapacity(RdfProperty):
    term = RdfTerm(
        "seatingCapacity",
        "http://schema.org/seatingCapacity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class merchantReturnLink(RdfProperty):
    term = RdfTerm(
        "merchantReturnLink",
        "http://schema.org/merchantReturnLink",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class latitude(RdfProperty):
    term = RdfTerm(
        "latitude", "http://schema.org/latitude", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | Text


@dataclass(frozen=True)
class resultComment(RdfProperty):
    term = RdfTerm(
        "resultComment",
        "http://schema.org/resultComment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Comment


@dataclass(frozen=True)
class processorRequirements(RdfProperty):
    term = RdfTerm(
        "processorRequirements",
        "http://schema.org/processorRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class releaseNotes(RdfProperty):
    term = RdfTerm(
        "releaseNotes",
        "http://schema.org/releaseNotes",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | Text


@dataclass(frozen=True)
class lesserOrEqual(RdfProperty):
    term = RdfTerm(
        "lesserOrEqual",
        "http://schema.org/lesserOrEqual",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QualitativeValue


@dataclass(frozen=True)
class amountOfThisGood(RdfProperty):
    term = RdfTerm(
        "amountOfThisGood",
        "http://schema.org/amountOfThisGood",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class broadcastAffiliateOf(RdfProperty):
    term = RdfTerm(
        "broadcastAffiliateOf",
        "http://schema.org/broadcastAffiliateOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class legislationApplies(RdfProperty):
    term = RdfTerm(
        "legislationApplies",
        "http://schema.org/legislationApplies",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Legislation


@dataclass(frozen=True)
class accountablePerson(RdfProperty):
    term = RdfTerm(
        "accountablePerson",
        "http://schema.org/accountablePerson",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class linkRelationship(RdfProperty):
    term = RdfTerm(
        "linkRelationship",
        "http://schema.org/linkRelationship",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class mathExpression(RdfProperty):
    term = RdfTerm("mathExpression", "http://schema.org/mathExpression", ["1.2-DRAFT"])
    object: schemaorg.SolveMathAction | Text


@dataclass(frozen=True)
class bookingTime(RdfProperty):
    term = RdfTerm(
        "bookingTime",
        "http://schema.org/bookingTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class softwareAddOn(RdfProperty):
    term = RdfTerm(
        "softwareAddOn",
        "http://schema.org/softwareAddOn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SoftwareApplication


@dataclass(frozen=True)
class area(RdfProperty):
    term = RdfTerm("area", "http://schema.org/area", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.Place


@dataclass(frozen=True)
class knowsLanguage(RdfProperty):
    term = RdfTerm(
        "knowsLanguage", "http://schema.org/knowsLanguage", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.Language


@dataclass(frozen=True)
class totalJobOpenings(RdfProperty):
    term = RdfTerm(
        "totalJobOpenings",
        "http://schema.org/totalJobOpenings",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class hostingOrganization(RdfProperty):
    term = RdfTerm(
        "hostingOrganization",
        "http://schema.org/hostingOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class bioChemInteraction(RdfProperty):
    term = RdfTerm(
        "bioChemInteraction", "http://schema.org/bioChemInteraction", ["1.2-DRAFT"]
    )
    object: schemaorg.BioChemEntity


@dataclass(frozen=True)
class xpath(RdfProperty):
    term = RdfTerm(
        "xpath", "http://schema.org/xpath", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: XPathType


@dataclass(frozen=True)
class postOfficeBoxNumber(RdfProperty):
    term = RdfTerm(
        "postOfficeBoxNumber",
        "http://schema.org/postOfficeBoxNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class dropoffLocation(RdfProperty):
    term = RdfTerm(
        "dropoffLocation",
        "http://schema.org/dropoffLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class cssSelector(RdfProperty):
    term = RdfTerm(
        "cssSelector",
        "http://schema.org/cssSelector",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: CssSelectorType


@dataclass(frozen=True)
class isLocatedInSubcellularLocation(RdfProperty):
    term = RdfTerm(
        "isLocatedInSubcellularLocation",
        "http://schema.org/isLocatedInSubcellularLocation",
        ["1.2-DRAFT"],
    )
    object: schemaorg.PropertyValue | schemaorg.DefinedTerm | URL


@dataclass(frozen=True)
class totalPaymentDue(RdfProperty):
    term = RdfTerm(
        "totalPaymentDue",
        "http://schema.org/totalPaymentDue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount | schemaorg.PriceSpecification


@dataclass(frozen=True)
class gracePeriod(RdfProperty):
    term = RdfTerm(
        "gracePeriod",
        "http://schema.org/gracePeriod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class arterialBranch(RdfProperty):
    term = RdfTerm(
        "arterialBranch",
        "http://schema.org/arterialBranch",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class customer(RdfProperty):
    term = RdfTerm(
        "customer", "http://schema.org/customer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class requirements(RdfProperty):
    term = RdfTerm(
        "requirements",
        "http://schema.org/requirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | Text


@dataclass(frozen=True)
class language(RdfProperty):
    term = RdfTerm(
        "language", "http://schema.org/language", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Language


@dataclass(frozen=True)
class abridged(RdfProperty):
    term = RdfTerm(
        "abridged", "http://schema.org/abridged", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Boolean


@dataclass(frozen=True)
class driveWheelConfiguration(RdfProperty):
    term = RdfTerm(
        "driveWheelConfiguration",
        "http://schema.org/driveWheelConfiguration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DriveWheelConfigurationValue | Text


@dataclass(frozen=True)
class manufacturer(RdfProperty):
    term = RdfTerm(
        "manufacturer",
        "http://schema.org/manufacturer",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class map(RdfProperty):
    term = RdfTerm("map", "http://schema.org/map", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: URL


@dataclass(frozen=True)
class termsPerYear(RdfProperty):
    term = RdfTerm(
        "termsPerYear", "http://schema.org/termsPerYear", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class paymentMethodId(RdfProperty):
    term = RdfTerm(
        "paymentMethodId",
        "http://schema.org/paymentMethodId",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class sender(RdfProperty):
    term = RdfTerm(
        "sender", "http://schema.org/sender", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Audience | schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class targetUrl(RdfProperty):
    term = RdfTerm(
        "targetUrl", "http://schema.org/targetUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class arrivalTerminal(RdfProperty):
    term = RdfTerm(
        "arrivalTerminal",
        "http://schema.org/arrivalTerminal",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class version(RdfProperty):
    term = RdfTerm(
        "version", "http://schema.org/version", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | Text


@dataclass(frozen=True)
class accountId(RdfProperty):
    term = RdfTerm(
        "accountId", "http://schema.org/accountId", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class expires(RdfProperty):
    term = RdfTerm(
        "expires", "http://schema.org/expires", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime | Date


@dataclass(frozen=True)
class doseSchedule(RdfProperty):
    term = RdfTerm(
        "doseSchedule",
        "http://schema.org/doseSchedule",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DoseSchedule


@dataclass(frozen=True)
class currentExchangeRate(RdfProperty):
    term = RdfTerm(
        "currentExchangeRate",
        "http://schema.org/currentExchangeRate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.UnitPriceSpecification


@dataclass(frozen=True)
class menuAddOn(RdfProperty):
    term = RdfTerm(
        "menuAddOn", "http://schema.org/menuAddOn", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MenuSection | schemaorg.MenuItem


@dataclass(frozen=True)
class awards(RdfProperty):
    term = RdfTerm(
        "awards", "http://schema.org/awards", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class menu(RdfProperty):
    term = RdfTerm("menu", "http://schema.org/menu", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: URL | schemaorg.Menu | Text


@dataclass(frozen=True)
class codeRepository(RdfProperty):
    term = RdfTerm(
        "codeRepository",
        "http://schema.org/codeRepository",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class replacer(RdfProperty):
    term = RdfTerm(
        "replacer", "http://schema.org/replacer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class legislationDateOfApplicability(RdfProperty):
    term = RdfTerm(
        "legislationDateOfApplicability",
        "http://schema.org/legislationDateOfApplicability",
        [],
    )
    object: Date


@dataclass(frozen=True)
class representativeOfPage(RdfProperty):
    term = RdfTerm(
        "representativeOfPage",
        "http://schema.org/representativeOfPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class subStructure(RdfProperty):
    term = RdfTerm(
        "subStructure",
        "http://schema.org/subStructure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class firstAppearance(RdfProperty):
    term = RdfTerm(
        "firstAppearance",
        "http://schema.org/firstAppearance",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class pregnancyWarning(RdfProperty):
    term = RdfTerm(
        "pregnancyWarning",
        "http://schema.org/pregnancyWarning",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class affiliation(RdfProperty):
    term = RdfTerm(
        "affiliation",
        "http://schema.org/affiliation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class text(RdfProperty):
    term = RdfTerm("text", "http://schema.org/text", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class hasMap(RdfProperty):
    term = RdfTerm(
        "hasMap", "http://schema.org/hasMap", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | schemaorg.Map


@dataclass(frozen=True)
class trainName(RdfProperty):
    term = RdfTerm(
        "trainName", "http://schema.org/trainName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class width(RdfProperty):
    term = RdfTerm(
        "width", "http://schema.org/width", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Distance | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class financialAidEligible(RdfProperty):
    term = RdfTerm(
        "financialAidEligible",
        "http://schema.org/financialAidEligible",
        ["1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class producer(RdfProperty):
    term = RdfTerm(
        "producer", "http://schema.org/producer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class orderDelivery(RdfProperty):
    term = RdfTerm(
        "orderDelivery",
        "http://schema.org/orderDelivery",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ParcelDelivery


@dataclass(frozen=True)
class startDate(RdfProperty):
    term = RdfTerm(
        "startDate", "http://schema.org/startDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Date | DateTime


@dataclass(frozen=True)
class numChildren(RdfProperty):
    term = RdfTerm(
        "numChildren",
        "http://schema.org/numChildren",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class dietFeatures(RdfProperty):
    term = RdfTerm(
        "dietFeatures",
        "http://schema.org/dietFeatures",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class authenticator(RdfProperty):
    term = RdfTerm(
        "authenticator", "http://schema.org/authenticator", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class screenCount(RdfProperty):
    term = RdfTerm(
        "screenCount",
        "http://schema.org/screenCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class discountCode(RdfProperty):
    term = RdfTerm(
        "discountCode",
        "http://schema.org/discountCode",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class thumbnailUrl(RdfProperty):
    term = RdfTerm(
        "thumbnailUrl",
        "http://schema.org/thumbnailUrl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class dayOfWeek(RdfProperty):
    term = RdfTerm(
        "dayOfWeek", "http://schema.org/dayOfWeek", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.DayOfWeek


@dataclass(frozen=True)
class warranty(RdfProperty):
    term = RdfTerm(
        "warranty", "http://schema.org/warranty", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.WarrantyPromise


@dataclass(frozen=True)
class illustrator(RdfProperty):
    term = RdfTerm(
        "illustrator",
        "http://schema.org/illustrator",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class installUrl(RdfProperty):
    term = RdfTerm(
        "installUrl", "http://schema.org/installUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class parents(RdfProperty):
    term = RdfTerm(
        "parents", "http://schema.org/parents", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class availableIn(RdfProperty):
    term = RdfTerm(
        "availableIn",
        "http://schema.org/availableIn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AdministrativeArea


@dataclass(frozen=True)
class endorsee(RdfProperty):
    term = RdfTerm(
        "endorsee", "http://schema.org/endorsee", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class scheduledTime(RdfProperty):
    term = RdfTerm(
        "scheduledTime",
        "http://schema.org/scheduledTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date | DateTime


@dataclass(frozen=True)
class scheduleTimezone(RdfProperty):
    term = RdfTerm(
        "scheduleTimezone", "http://schema.org/scheduleTimezone", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class seatingType(RdfProperty):
    term = RdfTerm(
        "seatingType",
        "http://schema.org/seatingType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QualitativeValue | Text


@dataclass(frozen=True)
class supportingData(RdfProperty):
    term = RdfTerm(
        "supportingData",
        "http://schema.org/supportingData",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DataFeed


@dataclass(frozen=True)
class strengthUnit(RdfProperty):
    term = RdfTerm(
        "strengthUnit",
        "http://schema.org/strengthUnit",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class subEvent(RdfProperty):
    term = RdfTerm(
        "subEvent", "http://schema.org/subEvent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class discusses(RdfProperty):
    term = RdfTerm(
        "discusses", "http://schema.org/discusses", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class spouse(RdfProperty):
    term = RdfTerm(
        "spouse", "http://schema.org/spouse", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class energyEfficiencyScaleMin(RdfProperty):
    term = RdfTerm(
        "energyEfficiencyScaleMin",
        "http://schema.org/energyEfficiencyScaleMin",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EUEnergyEfficiencyEnumeration


@dataclass(frozen=True)
class exercisePlan(RdfProperty):
    term = RdfTerm(
        "exercisePlan",
        "http://schema.org/exercisePlan",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ExercisePlan


@dataclass(frozen=True)
class intensity(RdfProperty):
    term = RdfTerm(
        "intensity", "http://schema.org/intensity", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class warning(RdfProperty):
    term = RdfTerm(
        "warning", "http://schema.org/warning", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | Text


@dataclass(frozen=True)
class targetPopulation(RdfProperty):
    term = RdfTerm(
        "targetPopulation",
        "http://schema.org/targetPopulation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class collection(RdfProperty):
    term = RdfTerm(
        "collection", "http://schema.org/collection", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class agentInteractionStatistic(RdfProperty):
    term = RdfTerm(
        "agentInteractionStatistic", "http://schema.org/agentInteractionStatistic", []
    )
    object: schemaorg.InteractionCounter


@dataclass(frozen=True)
class hiringOrganization(RdfProperty):
    term = RdfTerm(
        "hiringOrganization",
        "http://schema.org/hiringOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class isbn(RdfProperty):
    term = RdfTerm("isbn", "http://schema.org/isbn", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class iso6523Code(RdfProperty):
    term = RdfTerm("iso6523Code", "http://schema.org/iso6523Code", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class relevantOccupation(RdfProperty):
    term = RdfTerm(
        "relevantOccupation",
        "http://schema.org/relevantOccupation",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Occupation


@dataclass(frozen=True)
class experienceRequirements(RdfProperty):
    term = RdfTerm(
        "experienceRequirements",
        "http://schema.org/experienceRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OccupationalExperienceRequirements | Text


@dataclass(frozen=True)
class mediaItemAppearance(RdfProperty):
    term = RdfTerm(
        "mediaItemAppearance", "http://schema.org/mediaItemAppearance", ["1.2-DRAFT"]
    )
    object: schemaorg.MediaObject


@dataclass(frozen=True)
class itemDefectReturnFees(RdfProperty):
    term = RdfTerm(
        "itemDefectReturnFees", "http://schema.org/itemDefectReturnFees", ["1.2-DRAFT"]
    )
    object: schemaorg.ReturnFeesEnumeration


@dataclass(frozen=True)
class repeatCount(RdfProperty):
    term = RdfTerm(
        "repeatCount",
        "http://schema.org/repeatCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class variantCover(RdfProperty):
    term = RdfTerm(
        "variantCover",
        "http://schema.org/variantCover",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class sampleType(RdfProperty):
    term = RdfTerm(
        "sampleType", "http://schema.org/sampleType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class recourseLoan(RdfProperty):
    term = RdfTerm(
        "recourseLoan",
        "http://schema.org/recourseLoan",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class includedComposition(RdfProperty):
    term = RdfTerm(
        "includedComposition",
        "http://schema.org/includedComposition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MusicComposition


@dataclass(frozen=True)
class sport(RdfProperty):
    term = RdfTerm(
        "sport", "http://schema.org/sport", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class copyrightHolder(RdfProperty):
    term = RdfTerm(
        "copyrightHolder",
        "http://schema.org/copyrightHolder",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class workPresented(RdfProperty):
    term = RdfTerm(
        "workPresented",
        "http://schema.org/workPresented",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Movie


@dataclass(frozen=True)
class quest(RdfProperty):
    term = RdfTerm(
        "quest", "http://schema.org/quest", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class monthsOfExperience(RdfProperty):
    term = RdfTerm(
        "monthsOfExperience", "http://schema.org/monthsOfExperience", ["1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class numberOfLoanPayments(RdfProperty):
    term = RdfTerm(
        "numberOfLoanPayments",
        "http://schema.org/numberOfLoanPayments",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class hasMenu(RdfProperty):
    term = RdfTerm(
        "hasMenu", "http://schema.org/hasMenu", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL | schemaorg.Menu


@dataclass(frozen=True)
class usedToDiagnose(RdfProperty):
    term = RdfTerm(
        "usedToDiagnose",
        "http://schema.org/usedToDiagnose",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalCondition


@dataclass(frozen=True)
class wordCount(RdfProperty):
    term = RdfTerm(
        "wordCount", "http://schema.org/wordCount", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer


@dataclass(frozen=True)
class occupationalCredentialAwarded(RdfProperty):
    term = RdfTerm(
        "occupationalCredentialAwarded",
        "http://schema.org/occupationalCredentialAwarded",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EducationalOccupationalCredential | Text | URL


@dataclass(frozen=True)
class sourcedFrom(RdfProperty):
    term = RdfTerm(
        "sourcedFrom",
        "http://schema.org/sourcedFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BrainStructure


@dataclass(frozen=True)
class jobLocationType(RdfProperty):
    term = RdfTerm(
        "jobLocationType",
        "http://schema.org/jobLocationType",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class doseValue(RdfProperty):
    term = RdfTerm(
        "doseValue", "http://schema.org/doseValue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QualitativeValue | Number


@dataclass(frozen=True)
class geoTouches(RdfProperty):
    term = RdfTerm(
        "geoTouches", "http://schema.org/geoTouches", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.GeospatialGeometry | schemaorg.Place


@dataclass(frozen=True)
class hasMolecularFunction(RdfProperty):
    term = RdfTerm(
        "hasMolecularFunction", "http://schema.org/hasMolecularFunction", ["1.2-DRAFT"]
    )
    object: schemaorg.PropertyValue | schemaorg.DefinedTerm | URL


@dataclass(frozen=True)
class elevation(RdfProperty):
    term = RdfTerm(
        "elevation", "http://schema.org/elevation", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | Text


@dataclass(frozen=True)
class homeTeam(RdfProperty):
    term = RdfTerm(
        "homeTeam", "http://schema.org/homeTeam", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.SportsTeam


@dataclass(frozen=True)
class bodyLocation(RdfProperty):
    term = RdfTerm(
        "bodyLocation",
        "http://schema.org/bodyLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class hasAdultConsideration(RdfProperty):
    term = RdfTerm(
        "hasAdultConsideration",
        "http://schema.org/hasAdultConsideration",
        ["1.2-DRAFT"],
    )
    object: schemaorg.AdultOrientedEnumeration


@dataclass(frozen=True)
class hasMenuItem(RdfProperty):
    term = RdfTerm(
        "hasMenuItem",
        "http://schema.org/hasMenuItem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MenuItem


@dataclass(frozen=True)
class free(RdfProperty):
    term = RdfTerm("free", "http://schema.org/free", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Boolean


@dataclass(frozen=True)
class directors(RdfProperty):
    term = RdfTerm(
        "directors", "http://schema.org/directors", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class actionAccessibilityRequirement(RdfProperty):
    term = RdfTerm(
        "actionAccessibilityRequirement",
        "http://schema.org/actionAccessibilityRequirement",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ActionAccessSpecification


@dataclass(frozen=True)
class target(RdfProperty):
    term = RdfTerm(
        "target", "http://schema.org/target", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.EntryPoint | URL


@dataclass(frozen=True)
class calories(RdfProperty):
    term = RdfTerm(
        "calories", "http://schema.org/calories", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Energy


@dataclass(frozen=True)
class articleBody(RdfProperty):
    term = RdfTerm(
        "articleBody",
        "http://schema.org/articleBody",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class recordedAt(RdfProperty):
    term = RdfTerm(
        "recordedAt", "http://schema.org/recordedAt", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class boardingGroup(RdfProperty):
    term = RdfTerm(
        "boardingGroup",
        "http://schema.org/boardingGroup",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class biomechnicalClass(RdfProperty):
    term = RdfTerm(
        "biomechnicalClass",
        "http://schema.org/biomechnicalClass",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class audience(RdfProperty):
    term = RdfTerm(
        "audience", "http://schema.org/audience", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Audience


@dataclass(frozen=True)
class distinguishingSign(RdfProperty):
    term = RdfTerm(
        "distinguishingSign",
        "http://schema.org/distinguishingSign",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalSignOrSymptom


@dataclass(frozen=True)
class businessFunction(RdfProperty):
    term = RdfTerm(
        "businessFunction",
        "http://schema.org/businessFunction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BusinessFunction


@dataclass(frozen=True)
class weightPercentage(RdfProperty):
    term = RdfTerm("weightPercentage", "http://schema.org/weightPercentage", [])
    object: Number


@dataclass(frozen=True)
class spatial(RdfProperty):
    term = RdfTerm(
        "spatial", "http://schema.org/spatial", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class serviceOperator(RdfProperty):
    term = RdfTerm(
        "serviceOperator",
        "http://schema.org/serviceOperator",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class biologicalRole(RdfProperty):
    term = RdfTerm("biologicalRole", "http://schema.org/biologicalRole", ["1.2-DRAFT"])
    object: schemaorg.DefinedTerm


@dataclass(frozen=True)
class loanPaymentFrequency(RdfProperty):
    term = RdfTerm(
        "loanPaymentFrequency",
        "http://schema.org/loanPaymentFrequency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class interpretedAsClaim(RdfProperty):
    term = RdfTerm(
        "interpretedAsClaim", "http://schema.org/interpretedAsClaim", ["1.2-DRAFT"]
    )
    object: schemaorg.Claim


@dataclass(frozen=True)
class discountCurrency(RdfProperty):
    term = RdfTerm(
        "discountCurrency",
        "http://schema.org/discountCurrency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class creditText(RdfProperty):
    term = RdfTerm("creditText", "http://schema.org/creditText", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class domiciledMortgage(RdfProperty):
    term = RdfTerm(
        "domiciledMortgage",
        "http://schema.org/domiciledMortgage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class encodesCreativeWork(RdfProperty):
    term = RdfTerm(
        "encodesCreativeWork",
        "http://schema.org/encodesCreativeWork",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class statType(RdfProperty):
    term = RdfTerm("statType", "http://schema.org/statType", ["1.2-DRAFT"])
    object: URL | schemaorg.Property | Text


@dataclass(frozen=True)
class course(RdfProperty):
    term = RdfTerm(
        "course", "http://schema.org/course", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class fuelType(RdfProperty):
    term = RdfTerm(
        "fuelType", "http://schema.org/fuelType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.QualitativeValue | URL


@dataclass(frozen=True)
class associatedArticle(RdfProperty):
    term = RdfTerm(
        "associatedArticle",
        "http://schema.org/associatedArticle",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.NewsArticle


@dataclass(frozen=True)
class vehicleInteriorType(RdfProperty):
    term = RdfTerm(
        "vehicleInteriorType",
        "http://schema.org/vehicleInteriorType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class cvdNumVentUse(RdfProperty):
    term = RdfTerm(
        "cvdNumVentUse", "http://schema.org/cvdNumVentUse", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class coach(RdfProperty):
    term = RdfTerm(
        "coach", "http://schema.org/coach", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class educationalRole(RdfProperty):
    term = RdfTerm(
        "educationalRole",
        "http://schema.org/educationalRole",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class reviewBody(RdfProperty):
    term = RdfTerm(
        "reviewBody", "http://schema.org/reviewBody", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class byMonthDay(RdfProperty):
    term = RdfTerm(
        "byMonthDay", "http://schema.org/byMonthDay", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer


@dataclass(frozen=True)
class endTime(RdfProperty):
    term = RdfTerm(
        "endTime", "http://schema.org/endTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Time | DateTime


@dataclass(frozen=True)
class material(RdfProperty):
    term = RdfTerm(
        "material", "http://schema.org/material", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Product | Text | URL


@dataclass(frozen=True)
class amenityFeature(RdfProperty):
    term = RdfTerm(
        "amenityFeature",
        "http://schema.org/amenityFeature",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.LocationFeatureSpecification


@dataclass(frozen=True)
class membershipNumber(RdfProperty):
    term = RdfTerm(
        "membershipNumber",
        "http://schema.org/membershipNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class dateReceived(RdfProperty):
    term = RdfTerm(
        "dateReceived",
        "http://schema.org/dateReceived",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class translator(RdfProperty):
    term = RdfTerm(
        "translator", "http://schema.org/translator", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class arrivalTime(RdfProperty):
    term = RdfTerm(
        "arrivalTime",
        "http://schema.org/arrivalTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Time | DateTime


@dataclass(frozen=True)
class numberOfItems(RdfProperty):
    term = RdfTerm(
        "numberOfItems",
        "http://schema.org/numberOfItems",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class greaterOrEqual(RdfProperty):
    term = RdfTerm(
        "greaterOrEqual",
        "http://schema.org/greaterOrEqual",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QualitativeValue


@dataclass(frozen=True)
class bloodSupply(RdfProperty):
    term = RdfTerm(
        "bloodSupply",
        "http://schema.org/bloodSupply",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Vessel


@dataclass(frozen=True)
class rsvpResponse(RdfProperty):
    term = RdfTerm(
        "rsvpResponse",
        "http://schema.org/rsvpResponse",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.RsvpResponseType


@dataclass(frozen=True)
class auditDate(RdfProperty):
    term = RdfTerm("auditDate", "http://schema.org/auditDate", [])
    object: DateTime | Date


@dataclass(frozen=True)
class suggestedMaxAge(RdfProperty):
    term = RdfTerm(
        "suggestedMaxAge",
        "http://schema.org/suggestedMaxAge",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class vehicleConfiguration(RdfProperty):
    term = RdfTerm(
        "vehicleConfiguration",
        "http://schema.org/vehicleConfiguration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class naturalProgression(RdfProperty):
    term = RdfTerm(
        "naturalProgression",
        "http://schema.org/naturalProgression",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class option(RdfProperty):
    term = RdfTerm(
        "option", "http://schema.org/option", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing | Text


@dataclass(frozen=True)
class buyer(RdfProperty):
    term = RdfTerm(
        "buyer", "http://schema.org/buyer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class identifyingTest(RdfProperty):
    term = RdfTerm(
        "identifyingTest",
        "http://schema.org/identifyingTest",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTest


@dataclass(frozen=True)
class blogPost(RdfProperty):
    term = RdfTerm(
        "blogPost", "http://schema.org/blogPost", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.BlogPosting


@dataclass(frozen=True)
class recordedIn(RdfProperty):
    term = RdfTerm(
        "recordedIn", "http://schema.org/recordedIn", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class runtimePlatform(RdfProperty):
    term = RdfTerm(
        "runtimePlatform",
        "http://schema.org/runtimePlatform",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class inAlbum(RdfProperty):
    term = RdfTerm(
        "inAlbum", "http://schema.org/inAlbum", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicAlbum


@dataclass(frozen=True)
class alignmentType(RdfProperty):
    term = RdfTerm(
        "alignmentType",
        "http://schema.org/alignmentType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class healthPlanCoinsuranceRate(RdfProperty):
    term = RdfTerm(
        "healthPlanCoinsuranceRate",
        "http://schema.org/healthPlanCoinsuranceRate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class tickerSymbol(RdfProperty):
    term = RdfTerm(
        "tickerSymbol",
        "http://schema.org/tickerSymbol",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class applicableLocation(RdfProperty):
    term = RdfTerm(
        "applicableLocation",
        "http://schema.org/applicableLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AdministrativeArea


@dataclass(frozen=True)
class preparation(RdfProperty):
    term = RdfTerm(
        "preparation",
        "http://schema.org/preparation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.MedicalEntity


@dataclass(frozen=True)
class numberOfEpisodes(RdfProperty):
    term = RdfTerm(
        "numberOfEpisodes",
        "http://schema.org/numberOfEpisodes",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class announcementLocation(RdfProperty):
    term = RdfTerm(
        "announcementLocation",
        "http://schema.org/announcementLocation",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.LocalBusiness | schemaorg.CivicStructure


@dataclass(frozen=True)
class actionApplication(RdfProperty):
    term = RdfTerm(
        "actionApplication",
        "http://schema.org/actionApplication",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SoftwareApplication


@dataclass(frozen=True)
class candidate(RdfProperty):
    term = RdfTerm(
        "candidate", "http://schema.org/candidate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class character(RdfProperty):
    term = RdfTerm(
        "character", "http://schema.org/character", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class parentItem(RdfProperty):
    term = RdfTerm(
        "parentItem", "http://schema.org/parentItem", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork | schemaorg.Comment


@dataclass(frozen=True)
class targetProduct(RdfProperty):
    term = RdfTerm(
        "targetProduct",
        "http://schema.org/targetProduct",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SoftwareApplication


@dataclass(frozen=True)
class sizeSystem(RdfProperty):
    term = RdfTerm("sizeSystem", "http://schema.org/sizeSystem", ["1.2-DRAFT"])
    object: Text | schemaorg.SizeSystemEnumeration


@dataclass(frozen=True)
class funder(RdfProperty):
    term = RdfTerm(
        "funder", "http://schema.org/funder", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class incentiveAmount(RdfProperty):
    term = RdfTerm("incentiveAmount", "http://schema.org/incentiveAmount", [])
    object: (
        schemaorg.QuantitativeValue
        | schemaorg.LoanOrCredit
        | schemaorg.UnitPriceSpecification
    )


@dataclass(frozen=True)
class address(RdfProperty):
    term = RdfTerm(
        "address", "http://schema.org/address", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.PostalAddress | Text


@dataclass(frozen=True)
class alternativeOf(RdfProperty):
    term = RdfTerm("alternativeOf", "http://schema.org/alternativeOf", ["1.2-DRAFT"])
    object: schemaorg.Gene


@dataclass(frozen=True)
class additionalProperty(RdfProperty):
    term = RdfTerm(
        "additionalProperty",
        "http://schema.org/additionalProperty",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PropertyValue


@dataclass(frozen=True)
class significance(RdfProperty):
    term = RdfTerm(
        "significance",
        "http://schema.org/significance",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class doesNotShip(RdfProperty):
    term = RdfTerm("doesNotShip", "http://schema.org/doesNotShip", ["1.1", "1.2-DRAFT"])
    object: Boolean


@dataclass(frozen=True)
class additionalType(RdfProperty):
    term = RdfTerm(
        "additionalType",
        "http://schema.org/additionalType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | Text


@dataclass(frozen=True)
class previousStartDate(RdfProperty):
    term = RdfTerm(
        "previousStartDate",
        "http://schema.org/previousStartDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class instrument(RdfProperty):
    term = RdfTerm(
        "instrument", "http://schema.org/instrument", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class inSupportOf(RdfProperty):
    term = RdfTerm(
        "inSupportOf",
        "http://schema.org/inSupportOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class status(RdfProperty):
    term = RdfTerm(
        "status", "http://schema.org/status", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.EventStatusType | Text | schemaorg.MedicalStudyStatus


@dataclass(frozen=True)
class healthPlanId(RdfProperty):
    term = RdfTerm(
        "healthPlanId",
        "http://schema.org/healthPlanId",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class programName(RdfProperty):
    term = RdfTerm(
        "programName",
        "http://schema.org/programName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class typeOfGood(RdfProperty):
    term = RdfTerm(
        "typeOfGood", "http://schema.org/typeOfGood", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Product | schemaorg.Service


@dataclass(frozen=True)
class slogan(RdfProperty):
    term = RdfTerm("slogan", "http://schema.org/slogan", ["1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class encodings(RdfProperty):
    term = RdfTerm(
        "encodings", "http://schema.org/encodings", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MediaObject


@dataclass(frozen=True)
class arrivalBoatTerminal(RdfProperty):
    term = RdfTerm(
        "arrivalBoatTerminal",
        "http://schema.org/arrivalBoatTerminal",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BoatTerminal


@dataclass(frozen=True)
class additionalVariable(RdfProperty):
    term = RdfTerm(
        "additionalVariable",
        "http://schema.org/additionalVariable",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class tissueSample(RdfProperty):
    term = RdfTerm(
        "tissueSample",
        "http://schema.org/tissueSample",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class hasMemberProgram(RdfProperty):
    term = RdfTerm("hasMemberProgram", "http://schema.org/hasMemberProgram", [])
    object: schemaorg.MemberProgram


@dataclass(frozen=True)
class duplicateTherapy(RdfProperty):
    term = RdfTerm(
        "duplicateTherapy",
        "http://schema.org/duplicateTherapy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTherapy


@dataclass(frozen=True)
class floorLevel(RdfProperty):
    term = RdfTerm(
        "floorLevel", "http://schema.org/floorLevel", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class educationalProgramMode(RdfProperty):
    term = RdfTerm(
        "educationalProgramMode",
        "http://schema.org/educationalProgramMode",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL | Text


@dataclass(frozen=True)
class depth(RdfProperty):
    term = RdfTerm(
        "depth", "http://schema.org/depth", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | schemaorg.Distance


@dataclass(frozen=True)
class netWorth(RdfProperty):
    term = RdfTerm(
        "netWorth", "http://schema.org/netWorth", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MonetaryAmount | schemaorg.PriceSpecification


@dataclass(frozen=True)
class hasCourse(RdfProperty):
    term = RdfTerm("hasCourse", "http://schema.org/hasCourse", ["1.1", "1.2-DRAFT"])
    object: schemaorg.Course


@dataclass(frozen=True)
class proprietaryName(RdfProperty):
    term = RdfTerm(
        "proprietaryName",
        "http://schema.org/proprietaryName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class orderItemStatus(RdfProperty):
    term = RdfTerm(
        "orderItemStatus",
        "http://schema.org/orderItemStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OrderStatus


@dataclass(frozen=True)
class memoryRequirements(RdfProperty):
    term = RdfTerm(
        "memoryRequirements",
        "http://schema.org/memoryRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class departureBoatTerminal(RdfProperty):
    term = RdfTerm(
        "departureBoatTerminal",
        "http://schema.org/departureBoatTerminal",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BoatTerminal


@dataclass(frozen=True)
class eligibleTransactionVolume(RdfProperty):
    term = RdfTerm(
        "eligibleTransactionVolume",
        "http://schema.org/eligibleTransactionVolume",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PriceSpecification


@dataclass(frozen=True)
class pageStart(RdfProperty):
    term = RdfTerm(
        "pageStart", "http://schema.org/pageStart", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer | Text


@dataclass(frozen=True)
class contributor(RdfProperty):
    term = RdfTerm(
        "contributor",
        "http://schema.org/contributor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class benefitsSummaryUrl(RdfProperty):
    term = RdfTerm(
        "benefitsSummaryUrl",
        "http://schema.org/benefitsSummaryUrl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class exerciseRelatedDiet(RdfProperty):
    term = RdfTerm(
        "exerciseRelatedDiet",
        "http://schema.org/exerciseRelatedDiet",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Diet


@dataclass(frozen=True)
class maximumVirtualAttendeeCapacity(RdfProperty):
    term = RdfTerm(
        "maximumVirtualAttendeeCapacity",
        "http://schema.org/maximumVirtualAttendeeCapacity",
        ["1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class maximumIntake(RdfProperty):
    term = RdfTerm(
        "maximumIntake",
        "http://schema.org/maximumIntake",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MaximumDoseSchedule


@dataclass(frozen=True)
class position(RdfProperty):
    term = RdfTerm(
        "position", "http://schema.org/position", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer | Text


@dataclass(frozen=True)
class correctionsPolicy(RdfProperty):
    term = RdfTerm(
        "correctionsPolicy",
        "http://schema.org/correctionsPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class replacee(RdfProperty):
    term = RdfTerm(
        "replacee", "http://schema.org/replacee", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class itemShipped(RdfProperty):
    term = RdfTerm(
        "itemShipped",
        "http://schema.org/itemShipped",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Product


@dataclass(frozen=True)
class cvdNumBeds(RdfProperty):
    term = RdfTerm("cvdNumBeds", "http://schema.org/cvdNumBeds", ["1.1", "1.2-DRAFT"])
    object: Number


@dataclass(frozen=True)
class priceRange(RdfProperty):
    term = RdfTerm(
        "priceRange", "http://schema.org/priceRange", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class partOfInvoice(RdfProperty):
    term = RdfTerm(
        "partOfInvoice",
        "http://schema.org/partOfInvoice",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Invoice


@dataclass(frozen=True)
class serviceUrl(RdfProperty):
    term = RdfTerm(
        "serviceUrl", "http://schema.org/serviceUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class subTrip(RdfProperty):
    term = RdfTerm("subTrip", "http://schema.org/subTrip", ["1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.Trip


@dataclass(frozen=True)
class beneficiaryBank(RdfProperty):
    term = RdfTerm(
        "beneficiaryBank",
        "http://schema.org/beneficiaryBank",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.BankOrCreditUnion


@dataclass(frozen=True)
class potentialAction(RdfProperty):
    term = RdfTerm(
        "potentialAction",
        "http://schema.org/potentialAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Action


@dataclass(frozen=True)
class conditionsOfAccess(RdfProperty):
    term = RdfTerm(
        "conditionsOfAccess",
        "http://schema.org/conditionsOfAccess",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class review(RdfProperty):
    term = RdfTerm(
        "review", "http://schema.org/review", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Review


@dataclass(frozen=True)
class temporalCoverage(RdfProperty):
    term = RdfTerm(
        "temporalCoverage",
        "http://schema.org/temporalCoverage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL | DateTime


@dataclass(frozen=True)
class productGroupID(RdfProperty):
    term = RdfTerm(
        "productGroupID", "http://schema.org/productGroupID", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class defaultValue(RdfProperty):
    term = RdfTerm(
        "defaultValue",
        "http://schema.org/defaultValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing | Text


@dataclass(frozen=True)
class molecularFormula(RdfProperty):
    term = RdfTerm(
        "molecularFormula", "http://schema.org/molecularFormula", ["1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class priceType(RdfProperty):
    term = RdfTerm(
        "priceType", "http://schema.org/priceType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.PriceTypeEnumeration | Text


@dataclass(frozen=True)
class permitAudience(RdfProperty):
    term = RdfTerm(
        "permitAudience",
        "http://schema.org/permitAudience",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Audience


@dataclass(frozen=True)
class mentions(RdfProperty):
    term = RdfTerm(
        "mentions", "http://schema.org/mentions", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class administrationRoute(RdfProperty):
    term = RdfTerm(
        "administrationRoute",
        "http://schema.org/administrationRoute",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class legislationType(RdfProperty):
    term = RdfTerm(
        "legislationType",
        "http://schema.org/legislationType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.CategoryCode


@dataclass(frozen=True)
class increasesRiskOf(RdfProperty):
    term = RdfTerm(
        "increasesRiskOf",
        "http://schema.org/increasesRiskOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalEntity


@dataclass(frozen=True)
class textValue(RdfProperty):
    term = RdfTerm("textValue", "http://schema.org/textValue", ["1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class reportNumber(RdfProperty):
    term = RdfTerm(
        "reportNumber",
        "http://schema.org/reportNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class dateSent(RdfProperty):
    term = RdfTerm(
        "dateSent", "http://schema.org/dateSent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime


@dataclass(frozen=True)
class itemCondition(RdfProperty):
    term = RdfTerm(
        "itemCondition",
        "http://schema.org/itemCondition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OfferItemCondition


@dataclass(frozen=True)
class hasBioPolymerSequence(RdfProperty):
    term = RdfTerm(
        "hasBioPolymerSequence",
        "http://schema.org/hasBioPolymerSequence",
        ["1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class relatedLink(RdfProperty):
    term = RdfTerm(
        "relatedLink",
        "http://schema.org/relatedLink",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class deliveryAddress(RdfProperty):
    term = RdfTerm(
        "deliveryAddress",
        "http://schema.org/deliveryAddress",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PostalAddress


@dataclass(frozen=True)
class interactionStatistic(RdfProperty):
    term = RdfTerm(
        "interactionStatistic",
        "http://schema.org/interactionStatistic",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.InteractionCounter


@dataclass(frozen=True)
class totalTime(RdfProperty):
    term = RdfTerm(
        "totalTime", "http://schema.org/totalTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class noBylinesPolicy(RdfProperty):
    term = RdfTerm(
        "noBylinesPolicy",
        "http://schema.org/noBylinesPolicy",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class globalLocationNumber(RdfProperty):
    term = RdfTerm(
        "globalLocationNumber",
        "http://schema.org/globalLocationNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class pregnancyCategory(RdfProperty):
    term = RdfTerm(
        "pregnancyCategory",
        "http://schema.org/pregnancyCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DrugPregnancyCategory


@dataclass(frozen=True)
class orderedItem(RdfProperty):
    term = RdfTerm(
        "orderedItem",
        "http://schema.org/orderedItem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Product | schemaorg.OrderItem | schemaorg.Service


@dataclass(frozen=True)
class paymentDue(RdfProperty):
    term = RdfTerm(
        "paymentDue", "http://schema.org/paymentDue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime


@dataclass(frozen=True)
class permissionType(RdfProperty):
    term = RdfTerm(
        "permissionType",
        "http://schema.org/permissionType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DigitalDocumentPermissionType


@dataclass(frozen=True)
class sameAs(RdfProperty):
    term = RdfTerm(
        "sameAs", "http://schema.org/sameAs", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class modifiedTime(RdfProperty):
    term = RdfTerm(
        "modifiedTime",
        "http://schema.org/modifiedTime",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class dependencies(RdfProperty):
    term = RdfTerm(
        "dependencies",
        "http://schema.org/dependencies",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class landlord(RdfProperty):
    term = RdfTerm(
        "landlord", "http://schema.org/landlord", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class diagnosis(RdfProperty):
    term = RdfTerm(
        "diagnosis", "http://schema.org/diagnosis", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalCondition


@dataclass(frozen=True)
class loanMortgageMandateAmount(RdfProperty):
    term = RdfTerm(
        "loanMortgageMandateAmount",
        "http://schema.org/loanMortgageMandateAmount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class serverStatus(RdfProperty):
    term = RdfTerm(
        "serverStatus",
        "http://schema.org/serverStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.GameServerStatus


@dataclass(frozen=True)
class typicalCreditsPerTerm(RdfProperty):
    term = RdfTerm(
        "typicalCreditsPerTerm",
        "http://schema.org/typicalCreditsPerTerm",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.StructuredValue | Integer


@dataclass(frozen=True)
class acceptsReservations(RdfProperty):
    term = RdfTerm(
        "acceptsReservations",
        "http://schema.org/acceptsReservations",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean | Text | URL


@dataclass(frozen=True)
class eventAttendanceMode(RdfProperty):
    term = RdfTerm(
        "eventAttendanceMode",
        "http://schema.org/eventAttendanceMode",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EventAttendanceModeEnumeration


@dataclass(frozen=True)
class schemaVersion(RdfProperty):
    term = RdfTerm(
        "schemaVersion",
        "http://schema.org/schemaVersion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class physiologicalBenefits(RdfProperty):
    term = RdfTerm(
        "physiologicalBenefits",
        "http://schema.org/physiologicalBenefits",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class hasOccupation(RdfProperty):
    term = RdfTerm(
        "hasOccupation", "http://schema.org/hasOccupation", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Occupation


@dataclass(frozen=True)
class acquireLicensePage(RdfProperty):
    term = RdfTerm(
        "acquireLicensePage",
        "http://schema.org/acquireLicensePage",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class priceComponent(RdfProperty):
    term = RdfTerm(
        "priceComponent",
        "http://schema.org/priceComponent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.UnitPriceSpecification


@dataclass(frozen=True)
class cvdNumC19Died(RdfProperty):
    term = RdfTerm(
        "cvdNumC19Died", "http://schema.org/cvdNumC19Died", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class catalogNumber(RdfProperty):
    term = RdfTerm(
        "catalogNumber",
        "http://schema.org/catalogNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class ticketedSeat(RdfProperty):
    term = RdfTerm(
        "ticketedSeat",
        "http://schema.org/ticketedSeat",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Seat


@dataclass(frozen=True)
class recipeIngredient(RdfProperty):
    term = RdfTerm(
        "recipeIngredient",
        "http://schema.org/recipeIngredient",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class starRating(RdfProperty):
    term = RdfTerm(
        "starRating", "http://schema.org/starRating", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Rating


@dataclass(frozen=True)
class recipeInstructions(RdfProperty):
    term = RdfTerm(
        "recipeInstructions",
        "http://schema.org/recipeInstructions",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ItemList | schemaorg.CreativeWork | Text


@dataclass(frozen=True)
class partOfSeason(RdfProperty):
    term = RdfTerm(
        "partOfSeason",
        "http://schema.org/partOfSeason",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWorkSeason


@dataclass(frozen=True)
class creditedTo(RdfProperty):
    term = RdfTerm(
        "creditedTo", "http://schema.org/creditedTo", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class restPeriods(RdfProperty):
    term = RdfTerm(
        "restPeriods",
        "http://schema.org/restPeriods",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class geoWithin(RdfProperty):
    term = RdfTerm(
        "geoWithin", "http://schema.org/geoWithin", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.GeospatialGeometry | schemaorg.Place


@dataclass(frozen=True)
class differentialDiagnosis(RdfProperty):
    term = RdfTerm(
        "differentialDiagnosis",
        "http://schema.org/differentialDiagnosis",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DDxElement


@dataclass(frozen=True)
class numTracks(RdfProperty):
    term = RdfTerm(
        "numTracks", "http://schema.org/numTracks", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Integer


@dataclass(frozen=True)
class eduQuestionType(RdfProperty):
    term = RdfTerm(
        "eduQuestionType", "http://schema.org/eduQuestionType", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class referenceQuantity(RdfProperty):
    term = RdfTerm(
        "referenceQuantity",
        "http://schema.org/referenceQuantity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class deathPlace(RdfProperty):
    term = RdfTerm(
        "deathPlace", "http://schema.org/deathPlace", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class makesOffer(RdfProperty):
    term = RdfTerm(
        "makesOffer", "http://schema.org/makesOffer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Offer


@dataclass(frozen=True)
class eligibilityToWorkRequirement(RdfProperty):
    term = RdfTerm(
        "eligibilityToWorkRequirement",
        "http://schema.org/eligibilityToWorkRequirement",
        ["1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class dateVehicleFirstRegistered(RdfProperty):
    term = RdfTerm(
        "dateVehicleFirstRegistered",
        "http://schema.org/dateVehicleFirstRegistered",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class cvdNumICUBeds(RdfProperty):
    term = RdfTerm(
        "cvdNumICUBeds", "http://schema.org/cvdNumICUBeds", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class deliveryStatus(RdfProperty):
    term = RdfTerm(
        "deliveryStatus",
        "http://schema.org/deliveryStatus",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DeliveryEvent


@dataclass(frozen=True)
class vehicleIdentificationNumber(RdfProperty):
    term = RdfTerm(
        "vehicleIdentificationNumber",
        "http://schema.org/vehicleIdentificationNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class successorOf(RdfProperty):
    term = RdfTerm(
        "successorOf",
        "http://schema.org/successorOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ProductModel


@dataclass(frozen=True)
class reviewedBy(RdfProperty):
    term = RdfTerm(
        "reviewedBy", "http://schema.org/reviewedBy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class measuredProperty(RdfProperty):
    term = RdfTerm(
        "measuredProperty",
        "http://schema.org/measuredProperty",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Property


@dataclass(frozen=True)
class causeOf(RdfProperty):
    term = RdfTerm(
        "causeOf", "http://schema.org/causeOf", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalEntity


@dataclass(frozen=True)
class printEdition(RdfProperty):
    term = RdfTerm(
        "printEdition",
        "http://schema.org/printEdition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class purchaseType(RdfProperty):
    term = RdfTerm("purchaseType", "http://schema.org/purchaseType", [])
    object: schemaorg.PurchaseType


@dataclass(frozen=True)
class sugarContent(RdfProperty):
    term = RdfTerm(
        "sugarContent",
        "http://schema.org/sugarContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class diet(RdfProperty):
    term = RdfTerm("diet", "http://schema.org/diet", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.Diet


@dataclass(frozen=True)
class department(RdfProperty):
    term = RdfTerm(
        "department", "http://schema.org/department", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class publicTransportClosuresInfo(RdfProperty):
    term = RdfTerm(
        "publicTransportClosuresInfo",
        "http://schema.org/publicTransportClosuresInfo",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.WebContent | URL


@dataclass(frozen=True)
class availableStrength(RdfProperty):
    term = RdfTerm(
        "availableStrength",
        "http://schema.org/availableStrength",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DrugStrength


@dataclass(frozen=True)
class appearance(RdfProperty):
    term = RdfTerm(
        "appearance", "http://schema.org/appearance", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class observationAbout(RdfProperty):
    term = RdfTerm(
        "observationAbout", "http://schema.org/observationAbout", ["1.2-DRAFT"]
    )
    object: schemaorg.Place | schemaorg.Thing


@dataclass(frozen=True)
class bookEdition(RdfProperty):
    term = RdfTerm(
        "bookEdition",
        "http://schema.org/bookEdition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class clincalPharmacology(RdfProperty):
    term = RdfTerm(
        "clincalPharmacology",
        "http://schema.org/clincalPharmacology",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class bookFormat(RdfProperty):
    term = RdfTerm(
        "bookFormat", "http://schema.org/bookFormat", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.BookFormatType


@dataclass(frozen=True)
class codingSystem(RdfProperty):
    term = RdfTerm(
        "codingSystem",
        "http://schema.org/codingSystem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class quarantineGuidelines(RdfProperty):
    term = RdfTerm(
        "quarantineGuidelines",
        "http://schema.org/quarantineGuidelines",
        ["1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.WebContent


@dataclass(frozen=True)
class epidemiology(RdfProperty):
    term = RdfTerm(
        "epidemiology",
        "http://schema.org/epidemiology",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class currenciesAccepted(RdfProperty):
    term = RdfTerm(
        "currenciesAccepted",
        "http://schema.org/currenciesAccepted",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class legislationAmends(RdfProperty):
    term = RdfTerm("legislationAmends", "http://schema.org/legislationAmends", [])
    object: schemaorg.Legislation


@dataclass(frozen=True)
class emissionsCO2(RdfProperty):
    term = RdfTerm(
        "emissionsCO2",
        "http://schema.org/emissionsCO2",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class healthPlanMarketingUrl(RdfProperty):
    term = RdfTerm(
        "healthPlanMarketingUrl",
        "http://schema.org/healthPlanMarketingUrl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class serviceSmsNumber(RdfProperty):
    term = RdfTerm(
        "serviceSmsNumber",
        "http://schema.org/serviceSmsNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPoint


@dataclass(frozen=True)
class comprisedOf(RdfProperty):
    term = RdfTerm(
        "comprisedOf",
        "http://schema.org/comprisedOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem


@dataclass(frozen=True)
class sponsor(RdfProperty):
    term = RdfTerm(
        "sponsor", "http://schema.org/sponsor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class recommendationStrength(RdfProperty):
    term = RdfTerm(
        "recommendationStrength",
        "http://schema.org/recommendationStrength",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class valueMaxLength(RdfProperty):
    term = RdfTerm(
        "valueMaxLength",
        "http://schema.org/valueMaxLength",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class itemDefectReturnShippingFeesAmount(RdfProperty):
    term = RdfTerm(
        "itemDefectReturnShippingFeesAmount",
        "http://schema.org/itemDefectReturnShippingFeesAmount",
        ["1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class doseUnit(RdfProperty):
    term = RdfTerm(
        "doseUnit", "http://schema.org/doseUnit", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class measurementTechnique(RdfProperty):
    term = RdfTerm(
        "measurementTechnique",
        "http://schema.org/measurementTechnique",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DefinedTerm | URL | schemaorg.MeasurementMethodEnum


@dataclass(frozen=True)
class ticketNumber(RdfProperty):
    term = RdfTerm(
        "ticketNumber",
        "http://schema.org/ticketNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class accountOverdraftLimit(RdfProperty):
    term = RdfTerm(
        "accountOverdraftLimit",
        "http://schema.org/accountOverdraftLimit",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class measurementMethod(RdfProperty):
    term = RdfTerm(
        "measurementMethod", "http://schema.org/measurementMethod", ["1.2-DRAFT"]
    )
    object: schemaorg.DefinedTerm | URL | schemaorg.MeasurementMethodEnum | Text


@dataclass(frozen=True)
class relatedStructure(RdfProperty):
    term = RdfTerm(
        "relatedStructure",
        "http://schema.org/relatedStructure",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class publisher(RdfProperty):
    term = RdfTerm(
        "publisher", "http://schema.org/publisher", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class applicationStartDate(RdfProperty):
    term = RdfTerm(
        "applicationStartDate",
        "http://schema.org/applicationStartDate",
        ["1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class inChIKey(RdfProperty):
    term = RdfTerm("inChIKey", "http://schema.org/inChIKey", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class fiberContent(RdfProperty):
    term = RdfTerm(
        "fiberContent",
        "http://schema.org/fiberContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class knownVehicleDamages(RdfProperty):
    term = RdfTerm(
        "knownVehicleDamages",
        "http://schema.org/knownVehicleDamages",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class accommodationCategory(RdfProperty):
    term = RdfTerm(
        "accommodationCategory",
        "http://schema.org/accommodationCategory",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class originAddress(RdfProperty):
    term = RdfTerm(
        "originAddress",
        "http://schema.org/originAddress",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PostalAddress


@dataclass(frozen=True)
class costCurrency(RdfProperty):
    term = RdfTerm(
        "costCurrency",
        "http://schema.org/costCurrency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class episodes(RdfProperty):
    term = RdfTerm(
        "episodes", "http://schema.org/episodes", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Episode


@dataclass(frozen=True)
class rangeIncludes(RdfProperty):
    term = RdfTerm(
        "rangeIncludes",
        "http://schema.org/rangeIncludes",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Class


@dataclass(frozen=True)
class relatedAnatomy(RdfProperty):
    term = RdfTerm(
        "relatedAnatomy",
        "http://schema.org/relatedAnatomy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AnatomicalSystem | schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class guidelineDate(RdfProperty):
    term = RdfTerm(
        "guidelineDate",
        "http://schema.org/guidelineDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class httpMethod(RdfProperty):
    term = RdfTerm(
        "httpMethod", "http://schema.org/httpMethod", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class repetitions(RdfProperty):
    term = RdfTerm(
        "repetitions",
        "http://schema.org/repetitions",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class nsn(RdfProperty):
    term = RdfTerm("nsn", "http://schema.org/nsn", ["1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class foodEstablishment(RdfProperty):
    term = RdfTerm(
        "foodEstablishment",
        "http://schema.org/foodEstablishment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.FoodEstablishment | schemaorg.Place


@dataclass(frozen=True)
class positiveNotes(RdfProperty):
    term = RdfTerm("positiveNotes", "http://schema.org/positiveNotes", ["1.2-DRAFT"])
    object: schemaorg.WebContent | Text | schemaorg.ItemList | schemaorg.ListItem


@dataclass(frozen=True)
class softwareHelp(RdfProperty):
    term = RdfTerm(
        "softwareHelp",
        "http://schema.org/softwareHelp",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class publishedOn(RdfProperty):
    term = RdfTerm(
        "publishedOn",
        "http://schema.org/publishedOn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BroadcastService


@dataclass(frozen=True)
class assesses(RdfProperty):
    term = RdfTerm("assesses", "http://schema.org/assesses", ["1.1", "1.2-DRAFT"])
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class ingredients(RdfProperty):
    term = RdfTerm(
        "ingredients",
        "http://schema.org/ingredients",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class appliesToDeliveryMethod(RdfProperty):
    term = RdfTerm(
        "appliesToDeliveryMethod",
        "http://schema.org/appliesToDeliveryMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DeliveryMethod


@dataclass(frozen=True)
class repeatFrequency(RdfProperty):
    term = RdfTerm(
        "repeatFrequency",
        "http://schema.org/repeatFrequency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration | Text


@dataclass(frozen=True)
class numberedPosition(RdfProperty):
    term = RdfTerm(
        "numberedPosition",
        "http://schema.org/numberedPosition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class energyEfficiencyScaleMax(RdfProperty):
    term = RdfTerm(
        "energyEfficiencyScaleMax",
        "http://schema.org/energyEfficiencyScaleMax",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EUEnergyEfficiencyEnumeration


@dataclass(frozen=True)
class postalCode(RdfProperty):
    term = RdfTerm(
        "postalCode", "http://schema.org/postalCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class gameLocation(RdfProperty):
    term = RdfTerm(
        "gameLocation",
        "http://schema.org/gameLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.Place | schemaorg.PostalAddress


@dataclass(frozen=True)
class foodWarning(RdfProperty):
    term = RdfTerm(
        "foodWarning",
        "http://schema.org/foodWarning",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class exifData(RdfProperty):
    term = RdfTerm(
        "exifData", "http://schema.org/exifData", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.PropertyValue


@dataclass(frozen=True)
class spatialCoverage(RdfProperty):
    term = RdfTerm(
        "spatialCoverage",
        "http://schema.org/spatialCoverage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class size(RdfProperty):
    term = RdfTerm("size", "http://schema.org/size", ["1.1", "1.2-DRAFT"])
    object: (
        schemaorg.QuantitativeValue
        | schemaorg.DefinedTerm
        | schemaorg.SizeSpecification
        | Text
    )


@dataclass(frozen=True)
class includesObject(RdfProperty):
    term = RdfTerm(
        "includesObject",
        "http://schema.org/includesObject",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.TypeAndQuantityNode


@dataclass(frozen=True)
class loanPaymentAmount(RdfProperty):
    term = RdfTerm(
        "loanPaymentAmount",
        "http://schema.org/loanPaymentAmount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class recipeYield(RdfProperty):
    term = RdfTerm(
        "recipeYield",
        "http://schema.org/recipeYield",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class healthPlanDrugTier(RdfProperty):
    term = RdfTerm(
        "healthPlanDrugTier",
        "http://schema.org/healthPlanDrugTier",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class postalCodeEnd(RdfProperty):
    term = RdfTerm(
        "postalCodeEnd", "http://schema.org/postalCodeEnd", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class track(RdfProperty):
    term = RdfTerm(
        "track", "http://schema.org/track", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicRecording | schemaorg.ItemList


@dataclass(frozen=True)
class image(RdfProperty):
    term = RdfTerm(
        "image", "http://schema.org/image", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ImageObject | URL


@dataclass(frozen=True)
class messageAttachment(RdfProperty):
    term = RdfTerm(
        "messageAttachment",
        "http://schema.org/messageAttachment",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class priceCurrency(RdfProperty):
    term = RdfTerm(
        "priceCurrency",
        "http://schema.org/priceCurrency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class maximumEnrollment(RdfProperty):
    term = RdfTerm(
        "maximumEnrollment", "http://schema.org/maximumEnrollment", ["1.1", "1.2-DRAFT"]
    )
    object: Integer


@dataclass(frozen=True)
class participant(RdfProperty):
    term = RdfTerm(
        "participant",
        "http://schema.org/participant",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class sizeGroup(RdfProperty):
    term = RdfTerm("sizeGroup", "http://schema.org/sizeGroup", ["1.2-DRAFT"])
    object: schemaorg.SizeGroupEnumeration | Text


@dataclass(frozen=True)
class memberOf(RdfProperty):
    term = RdfTerm(
        "memberOf", "http://schema.org/memberOf", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: (
        schemaorg.Organization
        | schemaorg.ProgramMembership
        | schemaorg.MemberProgramTier
    )


@dataclass(frozen=True)
class contentRating(RdfProperty):
    term = RdfTerm(
        "contentRating",
        "http://schema.org/contentRating",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.Rating


@dataclass(frozen=True)
class expressedIn(RdfProperty):
    term = RdfTerm("expressedIn", "http://schema.org/expressedIn", ["1.2-DRAFT"])
    object: (
        schemaorg.AnatomicalStructure
        | schemaorg.BioChemEntity
        | schemaorg.DefinedTerm
        | schemaorg.AnatomicalSystem
    )


@dataclass(frozen=True)
class hasOfferCatalog(RdfProperty):
    term = RdfTerm(
        "hasOfferCatalog",
        "http://schema.org/hasOfferCatalog",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OfferCatalog


@dataclass(frozen=True)
class accessMode(RdfProperty):
    term = RdfTerm(
        "accessMode", "http://schema.org/accessMode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class valueRequired(RdfProperty):
    term = RdfTerm(
        "valueRequired",
        "http://schema.org/valueRequired",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class partOfSeries(RdfProperty):
    term = RdfTerm(
        "partOfSeries",
        "http://schema.org/partOfSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWorkSeries


@dataclass(frozen=True)
class tracks(RdfProperty):
    term = RdfTerm(
        "tracks", "http://schema.org/tracks", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicRecording


@dataclass(frozen=True)
class documentation(RdfProperty):
    term = RdfTerm(
        "documentation",
        "http://schema.org/documentation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class creator(RdfProperty):
    term = RdfTerm(
        "creator", "http://schema.org/creator", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class targetCollection(RdfProperty):
    term = RdfTerm(
        "targetCollection",
        "http://schema.org/targetCollection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class jobLocation(RdfProperty):
    term = RdfTerm(
        "jobLocation",
        "http://schema.org/jobLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class deliveryMethod(RdfProperty):
    term = RdfTerm(
        "deliveryMethod",
        "http://schema.org/deliveryMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DeliveryMethod


@dataclass(frozen=True)
class numberOfPages(RdfProperty):
    term = RdfTerm(
        "numberOfPages",
        "http://schema.org/numberOfPages",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class arrivalAirport(RdfProperty):
    term = RdfTerm(
        "arrivalAirport",
        "http://schema.org/arrivalAirport",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Airport


@dataclass(frozen=True)
class nonEqual(RdfProperty):
    term = RdfTerm(
        "nonEqual", "http://schema.org/nonEqual", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QualitativeValue


@dataclass(frozen=True)
class produces(RdfProperty):
    term = RdfTerm(
        "produces", "http://schema.org/produces", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class expectedArrivalFrom(RdfProperty):
    term = RdfTerm(
        "expectedArrivalFrom",
        "http://schema.org/expectedArrivalFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime | Date


@dataclass(frozen=True)
class healthPlanCopayOption(RdfProperty):
    term = RdfTerm(
        "healthPlanCopayOption",
        "http://schema.org/healthPlanCopayOption",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class vehicleSeatingCapacity(RdfProperty):
    term = RdfTerm(
        "vehicleSeatingCapacity",
        "http://schema.org/vehicleSeatingCapacity",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue | Number


@dataclass(frozen=True)
class carrier(RdfProperty):
    term = RdfTerm(
        "carrier", "http://schema.org/carrier", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class smokingAllowed(RdfProperty):
    term = RdfTerm(
        "smokingAllowed",
        "http://schema.org/smokingAllowed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class breadcrumb(RdfProperty):
    term = RdfTerm(
        "breadcrumb", "http://schema.org/breadcrumb", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.BreadcrumbList


@dataclass(frozen=True)
class normalRange(RdfProperty):
    term = RdfTerm(
        "normalRange",
        "http://schema.org/normalRange",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.MedicalEnumeration


@dataclass(frozen=True)
class ineligibleRegion(RdfProperty):
    term = RdfTerm(
        "ineligibleRegion",
        "http://schema.org/ineligibleRegion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.GeoShape | schemaorg.Place


@dataclass(frozen=True)
class ownedThrough(RdfProperty):
    term = RdfTerm(
        "ownedThrough",
        "http://schema.org/ownedThrough",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class aircraft(RdfProperty):
    term = RdfTerm(
        "aircraft", "http://schema.org/aircraft", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.Vehicle


@dataclass(frozen=True)
class accountMinimumInflow(RdfProperty):
    term = RdfTerm(
        "accountMinimumInflow",
        "http://schema.org/accountMinimumInflow",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class cvdNumC19HOPats(RdfProperty):
    term = RdfTerm(
        "cvdNumC19HOPats", "http://schema.org/cvdNumC19HOPats", ["1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class hasEnergyConsumptionDetails(RdfProperty):
    term = RdfTerm(
        "hasEnergyConsumptionDetails",
        "http://schema.org/hasEnergyConsumptionDetails",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.EnergyConsumptionDetails


@dataclass(frozen=True)
class trackingUrl(RdfProperty):
    term = RdfTerm(
        "trackingUrl",
        "http://schema.org/trackingUrl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class unitCode(RdfProperty):
    term = RdfTerm(
        "unitCode", "http://schema.org/unitCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL | Text


@dataclass(frozen=True)
class returnPolicySeasonalOverride(RdfProperty):
    term = RdfTerm(
        "returnPolicySeasonalOverride",
        "http://schema.org/returnPolicySeasonalOverride",
        ["1.2-DRAFT"],
    )
    object: schemaorg.MerchantReturnPolicySeasonalOverride


@dataclass(frozen=True)
class healthPlanPharmacyCategory(RdfProperty):
    term = RdfTerm(
        "healthPlanPharmacyCategory",
        "http://schema.org/healthPlanPharmacyCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class previousItem(RdfProperty):
    term = RdfTerm(
        "previousItem",
        "http://schema.org/previousItem",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ListItem


@dataclass(frozen=True)
class requiredCollateral(RdfProperty):
    term = RdfTerm(
        "requiredCollateral",
        "http://schema.org/requiredCollateral",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing | Text


@dataclass(frozen=True)
class cashBack(RdfProperty):
    term = RdfTerm(
        "cashBack", "http://schema.org/cashBack", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Boolean | Number


@dataclass(frozen=True)
class diversityStaffingReport(RdfProperty):
    term = RdfTerm(
        "diversityStaffingReport",
        "http://schema.org/diversityStaffingReport",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.Article


@dataclass(frozen=True)
class datasetTimeInterval(RdfProperty):
    term = RdfTerm(
        "datasetTimeInterval",
        "http://schema.org/datasetTimeInterval",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: DateTime


@dataclass(frozen=True)
class awayTeam(RdfProperty):
    term = RdfTerm(
        "awayTeam", "http://schema.org/awayTeam", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.SportsTeam


@dataclass(frozen=True)
class discount(RdfProperty):
    term = RdfTerm(
        "discount", "http://schema.org/discount", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | Text


@dataclass(frozen=True)
class priceComponentType(RdfProperty):
    term = RdfTerm(
        "priceComponentType", "http://schema.org/priceComponentType", ["1.2-DRAFT"]
    )
    object: schemaorg.PriceComponentTypeEnumeration


@dataclass(frozen=True)
class productionCompany(RdfProperty):
    term = RdfTerm(
        "productionCompany",
        "http://schema.org/productionCompany",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class claimReviewed(RdfProperty):
    term = RdfTerm(
        "claimReviewed",
        "http://schema.org/claimReviewed",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class supplyTo(RdfProperty):
    term = RdfTerm(
        "supplyTo", "http://schema.org/supplyTo", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.AnatomicalStructure


@dataclass(frozen=True)
class workload(RdfProperty):
    term = RdfTerm(
        "workload", "http://schema.org/workload", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue | schemaorg.Energy


@dataclass(frozen=True)
class gtin14(RdfProperty):
    term = RdfTerm(
        "gtin14", "http://schema.org/gtin14", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class height(RdfProperty):
    term = RdfTerm(
        "height", "http://schema.org/height", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Distance | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class trailerWeight(RdfProperty):
    term = RdfTerm(
        "trailerWeight",
        "http://schema.org/trailerWeight",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class exerciseType(RdfProperty):
    term = RdfTerm(
        "exerciseType",
        "http://schema.org/exerciseType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class issn(RdfProperty):
    term = RdfTerm("issn", "http://schema.org/issn", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class readonlyValue(RdfProperty):
    term = RdfTerm(
        "readonlyValue",
        "http://schema.org/readonlyValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class duns(RdfProperty):
    term = RdfTerm("duns", "http://schema.org/duns", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class ethicsPolicy(RdfProperty):
    term = RdfTerm(
        "ethicsPolicy",
        "http://schema.org/ethicsPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class stage(RdfProperty):
    term = RdfTerm(
        "stage", "http://schema.org/stage", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalConditionStage


@dataclass(frozen=True)
class downvoteCount(RdfProperty):
    term = RdfTerm(
        "downvoteCount",
        "http://schema.org/downvoteCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class releasedEvent(RdfProperty):
    term = RdfTerm(
        "releasedEvent",
        "http://schema.org/releasedEvent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PublicationEvent


@dataclass(frozen=True)
class longitude(RdfProperty):
    term = RdfTerm(
        "longitude", "http://schema.org/longitude", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | Text


@dataclass(frozen=True)
class prescribingInfo(RdfProperty):
    term = RdfTerm(
        "prescribingInfo",
        "http://schema.org/prescribingInfo",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class applicationDeadline(RdfProperty):
    term = RdfTerm(
        "applicationDeadline",
        "http://schema.org/applicationDeadline",
        ["1.1", "1.2-DRAFT"],
    )
    object: Text | Date


@dataclass(frozen=True)
class taxonRank(RdfProperty):
    term = RdfTerm("taxonRank", "http://schema.org/taxonRank", ["1.2-DRAFT"])
    object: URL | Text | schemaorg.PropertyValue


@dataclass(frozen=True)
class subReservation(RdfProperty):
    term = RdfTerm(
        "subReservation",
        "http://schema.org/subReservation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Reservation


@dataclass(frozen=True)
class gameTip(RdfProperty):
    term = RdfTerm(
        "gameTip", "http://schema.org/gameTip", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class shippingDestination(RdfProperty):
    term = RdfTerm(
        "shippingDestination",
        "http://schema.org/shippingDestination",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DefinedRegion


@dataclass(frozen=True)
class mainContentOfPage(RdfProperty):
    term = RdfTerm(
        "mainContentOfPage",
        "http://schema.org/mainContentOfPage",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.WebPageElement


@dataclass(frozen=True)
class familyName(RdfProperty):
    term = RdfTerm(
        "familyName", "http://schema.org/familyName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class titleEIDR(RdfProperty):
    term = RdfTerm("titleEIDR", "http://schema.org/titleEIDR", ["1.1", "1.2-DRAFT"])
    object: URL | Text


@dataclass(frozen=True)
class musicGroupMember(RdfProperty):
    term = RdfTerm(
        "musicGroupMember",
        "http://schema.org/musicGroupMember",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class sensoryRequirement(RdfProperty):
    term = RdfTerm(
        "sensoryRequirement",
        "http://schema.org/sensoryRequirement",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.DefinedTerm | URL | Text


@dataclass(frozen=True)
class actionableFeedbackPolicy(RdfProperty):
    term = RdfTerm(
        "actionableFeedbackPolicy",
        "http://schema.org/actionableFeedbackPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL | schemaorg.CreativeWork


@dataclass(frozen=True)
class supply(RdfProperty):
    term = RdfTerm(
        "supply", "http://schema.org/supply", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.HowToSupply | Text


@dataclass(frozen=True)
class accessibilitySummary(RdfProperty):
    term = RdfTerm(
        "accessibilitySummary",
        "http://schema.org/accessibilitySummary",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class translationOfWork(RdfProperty):
    term = RdfTerm(
        "translationOfWork",
        "http://schema.org/translationOfWork",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.CreativeWork


@dataclass(frozen=True)
class roleName(RdfProperty):
    term = RdfTerm(
        "roleName", "http://schema.org/roleName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class significantLinks(RdfProperty):
    term = RdfTerm(
        "significantLinks",
        "http://schema.org/significantLinks",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class purchaseDate(RdfProperty):
    term = RdfTerm(
        "purchaseDate",
        "http://schema.org/purchaseDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class interactionService(RdfProperty):
    term = RdfTerm(
        "interactionService",
        "http://schema.org/interactionService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SoftwareApplication | schemaorg.WebSite


@dataclass(frozen=True)
class fulfillmentType(RdfProperty):
    term = RdfTerm("fulfillmentType", "http://schema.org/fulfillmentType", [])
    object: schemaorg.FulfillmentTypeEnumeration


@dataclass(frozen=True)
class typicalTest(RdfProperty):
    term = RdfTerm(
        "typicalTest",
        "http://schema.org/typicalTest",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTest


@dataclass(frozen=True)
class areaServed(RdfProperty):
    term = RdfTerm(
        "areaServed", "http://schema.org/areaServed", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.AdministrativeArea | schemaorg.GeoShape | schemaorg.Place


@dataclass(frozen=True)
class serviceAudience(RdfProperty):
    term = RdfTerm(
        "serviceAudience",
        "http://schema.org/serviceAudience",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Audience


@dataclass(frozen=True)
class recipeCategory(RdfProperty):
    term = RdfTerm(
        "recipeCategory",
        "http://schema.org/recipeCategory",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class employerOverview(RdfProperty):
    term = RdfTerm(
        "employerOverview", "http://schema.org/employerOverview", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class cvdNumC19OverflowPats(RdfProperty):
    term = RdfTerm(
        "cvdNumC19OverflowPats",
        "http://schema.org/cvdNumC19OverflowPats",
        ["1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class incentives(RdfProperty):
    term = RdfTerm(
        "incentives", "http://schema.org/incentives", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class smiles(RdfProperty):
    term = RdfTerm("smiles", "http://schema.org/smiles", ["1.2-DRAFT"])
    object: Text


@dataclass(frozen=True)
class proficiencyLevel(RdfProperty):
    term = RdfTerm(
        "proficiencyLevel",
        "http://schema.org/proficiencyLevel",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class pathophysiology(RdfProperty):
    term = RdfTerm(
        "pathophysiology",
        "http://schema.org/pathophysiology",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class geoDisjoint(RdfProperty):
    term = RdfTerm(
        "geoDisjoint", "http://schema.org/geoDisjoint", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place | schemaorg.GeospatialGeometry


@dataclass(frozen=True)
class legislationCountersignedBy(RdfProperty):
    term = RdfTerm(
        "legislationCountersignedBy", "http://schema.org/legislationCountersignedBy", []
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class medicalAudience(RdfProperty):
    term = RdfTerm(
        "medicalAudience", "http://schema.org/medicalAudience", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MedicalAudienceType | schemaorg.MedicalAudience


@dataclass(frozen=True)
class worksFor(RdfProperty):
    term = RdfTerm(
        "worksFor", "http://schema.org/worksFor", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class reviewAspect(RdfProperty):
    term = RdfTerm(
        "reviewAspect", "http://schema.org/reviewAspect", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class minimumPaymentDue(RdfProperty):
    term = RdfTerm(
        "minimumPaymentDue",
        "http://schema.org/minimumPaymentDue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PriceSpecification | schemaorg.MonetaryAmount


@dataclass(frozen=True)
class members(RdfProperty):
    term = RdfTerm(
        "members", "http://schema.org/members", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class postalCodePrefix(RdfProperty):
    term = RdfTerm(
        "postalCodePrefix", "http://schema.org/postalCodePrefix", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class strengthValue(RdfProperty):
    term = RdfTerm(
        "strengthValue",
        "http://schema.org/strengthValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class legislationLegalForce(RdfProperty):
    term = RdfTerm(
        "legislationLegalForce",
        "http://schema.org/legislationLegalForce",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.LegalForceStatus


@dataclass(frozen=True)
class publisherImprint(RdfProperty):
    term = RdfTerm(
        "publisherImprint",
        "http://schema.org/publisherImprint",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class typicalAgeRange(RdfProperty):
    term = RdfTerm(
        "typicalAgeRange",
        "http://schema.org/typicalAgeRange",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class legislationPassedBy(RdfProperty):
    term = RdfTerm(
        "legislationPassedBy",
        "http://schema.org/legislationPassedBy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization | schemaorg.Person


@dataclass(frozen=True)
class refundType(RdfProperty):
    term = RdfTerm(
        "refundType", "http://schema.org/refundType", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.RefundTypeEnumeration


@dataclass(frozen=True)
class isPartOfBioChemEntity(RdfProperty):
    term = RdfTerm(
        "isPartOfBioChemEntity",
        "http://schema.org/isPartOfBioChemEntity",
        ["1.2-DRAFT"],
    )
    object: schemaorg.BioChemEntity


@dataclass(frozen=True)
class comment(RdfProperty):
    term = RdfTerm(
        "comment", "http://schema.org/comment", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Comment


@dataclass(frozen=True)
class governmentBenefitsInfo(RdfProperty):
    term = RdfTerm(
        "governmentBenefitsInfo",
        "http://schema.org/governmentBenefitsInfo",
        ["1.1", "1.2-DRAFT"],
    )
    object: schemaorg.GovernmentService


@dataclass(frozen=True)
class practicesAt(RdfProperty):
    term = RdfTerm("practicesAt", "http://schema.org/practicesAt", [])
    object: schemaorg.MedicalOrganization


@dataclass(frozen=True)
class bitrate(RdfProperty):
    term = RdfTerm(
        "bitrate", "http://schema.org/bitrate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class musicalKey(RdfProperty):
    term = RdfTerm(
        "musicalKey", "http://schema.org/musicalKey", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class boardingPolicy(RdfProperty):
    term = RdfTerm(
        "boardingPolicy",
        "http://schema.org/boardingPolicy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.BoardingPolicyType


@dataclass(frozen=True)
class encoding(RdfProperty):
    term = RdfTerm(
        "encoding", "http://schema.org/encoding", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MediaObject


@dataclass(frozen=True)
class userInteractionCount(RdfProperty):
    term = RdfTerm(
        "userInteractionCount",
        "http://schema.org/userInteractionCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class bookingAgent(RdfProperty):
    term = RdfTerm(
        "bookingAgent",
        "http://schema.org/bookingAgent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class minValue(RdfProperty):
    term = RdfTerm(
        "minValue", "http://schema.org/minValue", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class enginePower(RdfProperty):
    term = RdfTerm(
        "enginePower",
        "http://schema.org/enginePower",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class discussionUrl(RdfProperty):
    term = RdfTerm(
        "discussionUrl",
        "http://schema.org/discussionUrl",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class lowPrice(RdfProperty):
    term = RdfTerm(
        "lowPrice", "http://schema.org/lowPrice", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | Number


@dataclass(frozen=True)
class competencyRequired(RdfProperty):
    term = RdfTerm(
        "competencyRequired",
        "http://schema.org/competencyRequired",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.DefinedTerm | URL


@dataclass(frozen=True)
class title(RdfProperty):
    term = RdfTerm(
        "title", "http://schema.org/title", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class layoutImage(RdfProperty):
    term = RdfTerm("layoutImage", "http://schema.org/layoutImage", ["1.1", "1.2-DRAFT"])
    object: schemaorg.ImageObject | URL


@dataclass(frozen=True)
class proteinContent(RdfProperty):
    term = RdfTerm(
        "proteinContent",
        "http://schema.org/proteinContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class checkoutPageURLTemplate(RdfProperty):
    term = RdfTerm(
        "checkoutPageURLTemplate",
        "http://schema.org/checkoutPageURLTemplate",
        ["1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class member(RdfProperty):
    term = RdfTerm(
        "member", "http://schema.org/member", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class healthPlanNetworkTier(RdfProperty):
    term = RdfTerm(
        "healthPlanNetworkTier",
        "http://schema.org/healthPlanNetworkTier",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class transitTime(RdfProperty):
    term = RdfTerm("transitTime", "http://schema.org/transitTime", ["1.1", "1.2-DRAFT"])
    object: schemaorg.ServicePeriod | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class predecessorOf(RdfProperty):
    term = RdfTerm(
        "predecessorOf",
        "http://schema.org/predecessorOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ProductModel


@dataclass(frozen=True)
class legislationDateVersion(RdfProperty):
    term = RdfTerm(
        "legislationDateVersion",
        "http://schema.org/legislationDateVersion",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class geoCovers(RdfProperty):
    term = RdfTerm(
        "geoCovers", "http://schema.org/geoCovers", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place | schemaorg.GeospatialGeometry


@dataclass(frozen=True)
class studyLocation(RdfProperty):
    term = RdfTerm(
        "studyLocation",
        "http://schema.org/studyLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.AdministrativeArea


@dataclass(frozen=True)
class albumProductionType(RdfProperty):
    term = RdfTerm(
        "albumProductionType",
        "http://schema.org/albumProductionType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MusicAlbumProductionType


@dataclass(frozen=True)
class inPlaylist(RdfProperty):
    term = RdfTerm(
        "inPlaylist", "http://schema.org/inPlaylist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicPlaylist


@dataclass(frozen=True)
class billingStart(RdfProperty):
    term = RdfTerm("billingStart", "http://schema.org/billingStart", ["1.2-DRAFT"])
    object: Number


@dataclass(frozen=True)
class cvdCollectionDate(RdfProperty):
    term = RdfTerm(
        "cvdCollectionDate", "http://schema.org/cvdCollectionDate", ["1.1", "1.2-DRAFT"]
    )
    object: DateTime | Text


@dataclass(frozen=True)
class confirmationNumber(RdfProperty):
    term = RdfTerm(
        "confirmationNumber",
        "http://schema.org/confirmationNumber",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class targetDescription(RdfProperty):
    term = RdfTerm(
        "targetDescription",
        "http://schema.org/targetDescription",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class superEvent(RdfProperty):
    term = RdfTerm(
        "superEvent", "http://schema.org/superEvent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class transitTimeLabel(RdfProperty):
    term = RdfTerm(
        "transitTimeLabel", "http://schema.org/transitTimeLabel", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class timeRequired(RdfProperty):
    term = RdfTerm(
        "timeRequired",
        "http://schema.org/timeRequired",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class dissolutionDate(RdfProperty):
    term = RdfTerm(
        "dissolutionDate",
        "http://schema.org/dissolutionDate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date


@dataclass(frozen=True)
class acceptedPaymentMethod(RdfProperty):
    term = RdfTerm(
        "acceptedPaymentMethod",
        "http://schema.org/acceptedPaymentMethod",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.PaymentMethod | Text | schemaorg.LoanOrCredit


@dataclass(frozen=True)
class realEstateAgent(RdfProperty):
    term = RdfTerm(
        "realEstateAgent",
        "http://schema.org/realEstateAgent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.RealEstateAgent


@dataclass(frozen=True)
class beforeMedia(RdfProperty):
    term = RdfTerm(
        "beforeMedia",
        "http://schema.org/beforeMedia",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MediaObject | URL


@dataclass(frozen=True)
class follows(RdfProperty):
    term = RdfTerm(
        "follows", "http://schema.org/follows", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class isVariantOf(RdfProperty):
    term = RdfTerm(
        "isVariantOf",
        "http://schema.org/isVariantOf",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ProductModel | schemaorg.ProductGroup


@dataclass(frozen=True)
class busName(RdfProperty):
    term = RdfTerm(
        "busName", "http://schema.org/busName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class reservationFor(RdfProperty):
    term = RdfTerm(
        "reservationFor",
        "http://schema.org/reservationFor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class qualifiedExpense(RdfProperty):
    term = RdfTerm("qualifiedExpense", "http://schema.org/qualifiedExpense", [])
    object: schemaorg.IncentiveQualifiedExpenseType


@dataclass(frozen=True)
class founder(RdfProperty):
    term = RdfTerm(
        "founder", "http://schema.org/founder", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class providesService(RdfProperty):
    term = RdfTerm(
        "providesService",
        "http://schema.org/providesService",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Service


@dataclass(frozen=True)
class isAccessibleForFree(RdfProperty):
    term = RdfTerm(
        "isAccessibleForFree",
        "http://schema.org/isAccessibleForFree",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class cvdNumVent(RdfProperty):
    term = RdfTerm("cvdNumVent", "http://schema.org/cvdNumVent", ["1.1", "1.2-DRAFT"])
    object: Number


@dataclass(frozen=True)
class storageRequirements(RdfProperty):
    term = RdfTerm(
        "storageRequirements",
        "http://schema.org/storageRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class occupancy(RdfProperty):
    term = RdfTerm(
        "occupancy", "http://schema.org/occupancy", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.QuantitativeValue


@dataclass(frozen=True)
class procedureType(RdfProperty):
    term = RdfTerm(
        "procedureType",
        "http://schema.org/procedureType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalProcedureType


@dataclass(frozen=True)
class earlyPrepaymentPenalty(RdfProperty):
    term = RdfTerm(
        "earlyPrepaymentPenalty",
        "http://schema.org/earlyPrepaymentPenalty",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MonetaryAmount


@dataclass(frozen=True)
class softwareRequirements(RdfProperty):
    term = RdfTerm(
        "softwareRequirements",
        "http://schema.org/softwareRequirements",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | URL


@dataclass(frozen=True)
class photo(RdfProperty):
    term = RdfTerm(
        "photo", "http://schema.org/photo", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.ImageObject | schemaorg.Photograph


@dataclass(frozen=True)
class gtin8(RdfProperty):
    term = RdfTerm(
        "gtin8", "http://schema.org/gtin8", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class industry(RdfProperty):
    term = RdfTerm(
        "industry", "http://schema.org/industry", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.DefinedTerm


@dataclass(frozen=True)
class audio(RdfProperty):
    term = RdfTerm(
        "audio", "http://schema.org/audio", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.AudioObject | schemaorg.MusicRecording | schemaorg.Clip


@dataclass(frozen=True)
class program(RdfProperty):
    term = RdfTerm("program", "http://schema.org/program", [])
    object: schemaorg.MemberProgram


@dataclass(frozen=True)
class courseCode(RdfProperty):
    term = RdfTerm(
        "courseCode", "http://schema.org/courseCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class startOffset(RdfProperty):
    term = RdfTerm(
        "startOffset", "http://schema.org/startOffset", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.HyperTocEntry | Number


@dataclass(frozen=True)
class characterAttribute(RdfProperty):
    term = RdfTerm(
        "characterAttribute",
        "http://schema.org/characterAttribute",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class availableAtOrFrom(RdfProperty):
    term = RdfTerm(
        "availableAtOrFrom",
        "http://schema.org/availableAtOrFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class correction(RdfProperty):
    term = RdfTerm(
        "correction", "http://schema.org/correction", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CorrectionComment | Text | URL


@dataclass(frozen=True)
class includesHealthPlanFormulary(RdfProperty):
    term = RdfTerm(
        "includesHealthPlanFormulary",
        "http://schema.org/includesHealthPlanFormulary",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.HealthPlanFormulary


@dataclass(frozen=True)
class faxNumber(RdfProperty):
    term = RdfTerm(
        "faxNumber", "http://schema.org/faxNumber", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class foodEvent(RdfProperty):
    term = RdfTerm(
        "foodEvent", "http://schema.org/foodEvent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.FoodEvent


@dataclass(frozen=True)
class contactPoint(RdfProperty):
    term = RdfTerm(
        "contactPoint",
        "http://schema.org/contactPoint",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.ContactPoint


@dataclass(frozen=True)
class muscleAction(RdfProperty):
    term = RdfTerm(
        "muscleAction",
        "http://schema.org/muscleAction",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class salaryCurrency(RdfProperty):
    term = RdfTerm(
        "salaryCurrency",
        "http://schema.org/salaryCurrency",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class cvdNumC19OFMechVentPats(RdfProperty):
    term = RdfTerm(
        "cvdNumC19OFMechVentPats",
        "http://schema.org/cvdNumC19OFMechVentPats",
        ["1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class bestRating(RdfProperty):
    term = RdfTerm(
        "bestRating", "http://schema.org/bestRating", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number | Text


@dataclass(frozen=True)
class broadcastFrequencyValue(RdfProperty):
    term = RdfTerm(
        "broadcastFrequencyValue",
        "http://schema.org/broadcastFrequencyValue",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class applicableCountry(RdfProperty):
    term = RdfTerm(
        "applicableCountry", "http://schema.org/applicableCountry", ["1.2-DRAFT"]
    )
    object: schemaorg.Country | Text


@dataclass(frozen=True)
class chemicalRole(RdfProperty):
    term = RdfTerm("chemicalRole", "http://schema.org/chemicalRole", ["1.2-DRAFT"])
    object: schemaorg.DefinedTerm


@dataclass(frozen=True)
class author(RdfProperty):
    term = RdfTerm(
        "author", "http://schema.org/author", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class iataCode(RdfProperty):
    term = RdfTerm(
        "iataCode", "http://schema.org/iataCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class fatContent(RdfProperty):
    term = RdfTerm(
        "fatContent", "http://schema.org/fatContent", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class branchCode(RdfProperty):
    term = RdfTerm(
        "branchCode", "http://schema.org/branchCode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class clinicalPharmacology(RdfProperty):
    term = RdfTerm(
        "clinicalPharmacology",
        "http://schema.org/clinicalPharmacology",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class travelBans(RdfProperty):
    term = RdfTerm("travelBans", "http://schema.org/travelBans", ["1.1", "1.2-DRAFT"])
    object: URL | schemaorg.WebContent


@dataclass(frozen=True)
class safetyConsideration(RdfProperty):
    term = RdfTerm(
        "safetyConsideration",
        "http://schema.org/safetyConsideration",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class carbohydrateContent(RdfProperty):
    term = RdfTerm(
        "carbohydrateContent",
        "http://schema.org/carbohydrateContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class eligibleWithSupplier(RdfProperty):
    term = RdfTerm("eligibleWithSupplier", "http://schema.org/eligibleWithSupplier", [])
    object: schemaorg.Organization


@dataclass(frozen=True)
class itemOffered(RdfProperty):
    term = RdfTerm(
        "itemOffered",
        "http://schema.org/itemOffered",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: (
        schemaorg.Trip
        | schemaorg.Product
        | schemaorg.AggregateOffer
        | schemaorg.MenuItem
        | schemaorg.Service
        | schemaorg.Event
        | schemaorg.CreativeWork
    )


@dataclass(frozen=True)
class serviceType(RdfProperty):
    term = RdfTerm(
        "serviceType",
        "http://schema.org/serviceType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text | schemaorg.GovernmentBenefitsType


@dataclass(frozen=True)
class availableTest(RdfProperty):
    term = RdfTerm(
        "availableTest",
        "http://schema.org/availableTest",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTest


@dataclass(frozen=True)
class pickupLocation(RdfProperty):
    term = RdfTerm(
        "pickupLocation",
        "http://schema.org/pickupLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class restockingFee(RdfProperty):
    term = RdfTerm("restockingFee", "http://schema.org/restockingFee", ["1.2-DRAFT"])
    object: schemaorg.MonetaryAmount | Number


@dataclass(frozen=True)
class masthead(RdfProperty):
    term = RdfTerm(
        "masthead", "http://schema.org/masthead", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.CreativeWork | URL


@dataclass(frozen=True)
class code(RdfProperty):
    term = RdfTerm("code", "http://schema.org/code", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
    object: schemaorg.MedicalCode


@dataclass(frozen=True)
class saturatedFatContent(RdfProperty):
    term = RdfTerm(
        "saturatedFatContent",
        "http://schema.org/saturatedFatContent",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Mass


@dataclass(frozen=True)
class productReturnDays(RdfProperty):
    term = RdfTerm(
        "productReturnDays",
        "http://schema.org/productReturnDays",
        ["1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class byArtist(RdfProperty):
    term = RdfTerm(
        "byArtist", "http://schema.org/byArtist", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.MusicGroup | schemaorg.Person


@dataclass(frozen=True)
class musicCompositionForm(RdfProperty):
    term = RdfTerm(
        "musicCompositionForm",
        "http://schema.org/musicCompositionForm",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class assembly(RdfProperty):
    term = RdfTerm(
        "assembly", "http://schema.org/assembly", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class isUnlabelledFallback(RdfProperty):
    term = RdfTerm(
        "isUnlabelledFallback",
        "http://schema.org/isUnlabelledFallback",
        ["1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class cvdNumC19MechVentPats(RdfProperty):
    term = RdfTerm(
        "cvdNumC19MechVentPats",
        "http://schema.org/cvdNumC19MechVentPats",
        ["1.1", "1.2-DRAFT"],
    )
    object: Number


@dataclass(frozen=True)
class significantLink(RdfProperty):
    term = RdfTerm(
        "significantLink",
        "http://schema.org/significantLink",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: URL


@dataclass(frozen=True)
class steeringPosition(RdfProperty):
    term = RdfTerm(
        "steeringPosition",
        "http://schema.org/steeringPosition",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.SteeringPositionValue


@dataclass(frozen=True)
class observationPeriod(RdfProperty):
    term = RdfTerm(
        "observationPeriod", "http://schema.org/observationPeriod", ["1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class honorificSuffix(RdfProperty):
    term = RdfTerm(
        "honorificSuffix",
        "http://schema.org/honorificSuffix",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class underName(RdfProperty):
    term = RdfTerm(
        "underName", "http://schema.org/underName", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person | schemaorg.Organization


@dataclass(frozen=True)
class availabilityEnds(RdfProperty):
    term = RdfTerm(
        "availabilityEnds",
        "http://schema.org/availabilityEnds",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Date | Time | DateTime


@dataclass(frozen=True)
class paymentUrl(RdfProperty):
    term = RdfTerm(
        "paymentUrl", "http://schema.org/paymentUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: URL


@dataclass(frozen=True)
class annualPercentageRate(RdfProperty):
    term = RdfTerm(
        "annualPercentageRate",
        "http://schema.org/annualPercentageRate",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Number | schemaorg.QuantitativeValue


@dataclass(frozen=True)
class actionOption(RdfProperty):
    term = RdfTerm(
        "actionOption",
        "http://schema.org/actionOption",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing | Text


@dataclass(frozen=True)
class subOrganization(RdfProperty):
    term = RdfTerm(
        "subOrganization",
        "http://schema.org/subOrganization",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Organization


@dataclass(frozen=True)
class director(RdfProperty):
    term = RdfTerm(
        "director", "http://schema.org/director", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Person


@dataclass(frozen=True)
class currency(RdfProperty):
    term = RdfTerm(
        "currency", "http://schema.org/currency", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class postalCodeBegin(RdfProperty):
    term = RdfTerm(
        "postalCodeBegin", "http://schema.org/postalCodeBegin", ["1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class isAccessoryOrSparePartFor(RdfProperty):
    term = RdfTerm(
        "isAccessoryOrSparePartFor",
        "http://schema.org/isAccessoryOrSparePartFor",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Product


@dataclass(frozen=True)
class openingHoursSpecification(RdfProperty):
    term = RdfTerm(
        "openingHoursSpecification",
        "http://schema.org/openingHoursSpecification",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.OpeningHoursSpecification


@dataclass(frozen=True)
class events(RdfProperty):
    term = RdfTerm(
        "events", "http://schema.org/events", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class upvoteCount(RdfProperty):
    term = RdfTerm(
        "upvoteCount",
        "http://schema.org/upvoteCount",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Integer


@dataclass(frozen=True)
class costPerUnit(RdfProperty):
    term = RdfTerm(
        "costPerUnit",
        "http://schema.org/costPerUnit",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.QualitativeValue | Number | Text


@dataclass(frozen=True)
class geoEquals(RdfProperty):
    term = RdfTerm(
        "geoEquals", "http://schema.org/geoEquals", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.GeospatialGeometry | schemaorg.Place


@dataclass(frozen=True)
class performerIn(RdfProperty):
    term = RdfTerm(
        "performerIn",
        "http://schema.org/performerIn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Event


@dataclass(frozen=True)
class interactingDrug(RdfProperty):
    term = RdfTerm(
        "interactingDrug",
        "http://schema.org/interactingDrug",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Drug


@dataclass(frozen=True)
class expertConsiderations(RdfProperty):
    term = RdfTerm(
        "expertConsiderations",
        "http://schema.org/expertConsiderations",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class renegotiableLoan(RdfProperty):
    term = RdfTerm(
        "renegotiableLoan",
        "http://schema.org/renegotiableLoan",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Boolean


@dataclass(frozen=True)
class domainIncludes(RdfProperty):
    term = RdfTerm(
        "domainIncludes",
        "http://schema.org/domainIncludes",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Class


@dataclass(frozen=True)
class partOfTVSeries(RdfProperty):
    term = RdfTerm(
        "partOfTVSeries",
        "http://schema.org/partOfTVSeries",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.TVSeries


@dataclass(frozen=True)
class reservedTicket(RdfProperty):
    term = RdfTerm(
        "reservedTicket",
        "http://schema.org/reservedTicket",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Ticket


@dataclass(frozen=True)
class hasShippingService(RdfProperty):
    term = RdfTerm("hasShippingService", "http://schema.org/hasShippingService", [])
    object: schemaorg.ShippingService


@dataclass(frozen=True)
class genre(RdfProperty):
    term = RdfTerm(
        "genre", "http://schema.org/genre", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | URL


@dataclass(frozen=True)
class exceptDate(RdfProperty):
    term = RdfTerm(
        "exceptDate", "http://schema.org/exceptDate", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: DateTime | Date


@dataclass(frozen=True)
class exerciseCourse(RdfProperty):
    term = RdfTerm(
        "exerciseCourse",
        "http://schema.org/exerciseCourse",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class termDuration(RdfProperty):
    term = RdfTerm(
        "termDuration", "http://schema.org/termDuration", ["1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Duration


@dataclass(frozen=True)
class email(RdfProperty):
    term = RdfTerm(
        "email", "http://schema.org/email", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text


@dataclass(frozen=True)
class workLocation(RdfProperty):
    term = RdfTerm(
        "workLocation",
        "http://schema.org/workLocation",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Place | schemaorg.ContactPoint


@dataclass(frozen=True)
class contentSize(RdfProperty):
    term = RdfTerm(
        "contentSize",
        "http://schema.org/contentSize",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class videoFormat(RdfProperty):
    term = RdfTerm(
        "videoFormat",
        "http://schema.org/videoFormat",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class associatedClaimReview(RdfProperty):
    term = RdfTerm(
        "associatedClaimReview",
        "http://schema.org/associatedClaimReview",
        ["1.2-DRAFT"],
    )
    object: schemaorg.Review


@dataclass(frozen=True)
class trialDesign(RdfProperty):
    term = RdfTerm(
        "trialDesign",
        "http://schema.org/trialDesign",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.MedicalTrialDesign


@dataclass(frozen=True)
class broadcastDisplayName(RdfProperty):
    term = RdfTerm(
        "broadcastDisplayName",
        "http://schema.org/broadcastDisplayName",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Text


@dataclass(frozen=True)
class gender(RdfProperty):
    term = RdfTerm(
        "gender", "http://schema.org/gender", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: Text | schemaorg.GenderType


@dataclass(frozen=True)
class variableMeasured(RdfProperty):
    term = RdfTerm(
        "variableMeasured",
        "http://schema.org/variableMeasured",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: (
        schemaorg.Property
        | schemaorg.StatisticalVariable
        | schemaorg.PropertyValue
        | Text
    )


@dataclass(frozen=True)
class percentile10(RdfProperty):
    term = RdfTerm(
        "percentile10", "http://schema.org/percentile10", ["1.0", "1.1", "1.2-DRAFT"]
    )
    object: Number


@dataclass(frozen=True)
class serviceOutput(RdfProperty):
    term = RdfTerm(
        "serviceOutput",
        "http://schema.org/serviceOutput",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: schemaorg.Thing


@dataclass(frozen=True)
class toLocation(RdfProperty):
    term = RdfTerm(
        "toLocation", "http://schema.org/toLocation", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Place


@dataclass(frozen=True)
class episode(RdfProperty):
    term = RdfTerm(
        "episode", "http://schema.org/episode", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.Episode


@dataclass(frozen=True)
class insertion(RdfProperty):
    term = RdfTerm(
        "insertion", "http://schema.org/insertion", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.AnatomicalStructure


class Date(RdfDataType):
    term = RdfTerm("Date", "http://schema.org/Date", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class Text(RdfDataType):
    term = RdfTerm("Text", "http://schema.org/Text", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class URL(RdfDataType):
    term = RdfTerm("URL", "http://schema.org/URL", ["0.2", "1.0", "1.1", "1.2-DRAFT"])


class CssSelectorType(RdfDataType):
    term = RdfTerm(
        "CssSelectorType",
        "http://schema.org/CssSelectorType",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class PronounceableText(RdfDataType):
    term = RdfTerm(
        "PronounceableText", "http://schema.org/PronounceableText", ["1.1", "1.2-DRAFT"]
    )


class XPathType(RdfDataType):
    term = RdfTerm(
        "XPathType", "http://schema.org/XPathType", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class DateTime(RdfDataType):
    term = RdfTerm(
        "DateTime", "http://schema.org/DateTime", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Number(RdfDataType):
    term = RdfTerm(
        "Number", "http://schema.org/Number", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Float(RdfDataType):
    term = RdfTerm(
        "Float", "http://schema.org/Float", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Integer(RdfDataType):
    term = RdfTerm(
        "Integer", "http://schema.org/Integer", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Boolean(RdfDataType):
    term = RdfTerm(
        "Boolean", "http://schema.org/Boolean", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Time(RdfDataType):
    term = RdfTerm("Time", "http://schema.org/Time", ["0.2", "1.0", "1.1", "1.2-DRAFT"])
