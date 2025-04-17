from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import schemaorg

class Date(RdfDataType):
    term = RdfTerm('Date', 'http://schema.org/Date', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Text(RdfDataType):
    term = RdfTerm('Text', 'http://schema.org/Text', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class URL(RdfDataType):
    term = RdfTerm('URL', 'http://schema.org/URL', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CssSelectorType(RdfDataType):
    term = RdfTerm('CssSelectorType', 'http://schema.org/CssSelectorType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PronounceableText(RdfDataType):
    term = RdfTerm('PronounceableText', 'http://schema.org/PronounceableText', ['1.1', '1.2-DRAFT'])

class XPathType(RdfDataType):
    term = RdfTerm('XPathType', 'http://schema.org/XPathType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DateTime(RdfDataType):
    term = RdfTerm('DateTime', 'http://schema.org/DateTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Number(RdfDataType):
    term = RdfTerm('Number', 'http://schema.org/Number', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Float(RdfDataType):
    term = RdfTerm('Float', 'http://schema.org/Float', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Integer(RdfDataType):
    term = RdfTerm('Integer', 'http://schema.org/Integer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Boolean(RdfDataType):
    term = RdfTerm('Boolean', 'http://schema.org/Boolean', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Time(RdfDataType):
    term = RdfTerm('Time', 'http://schema.org/Time', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DataType(rdfs.Class):
    term = RdfTerm('DataType', 'http://schema.org/DataType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Thing(RdfClass):
    term = RdfTerm('Thing', 'http://schema.org/Thing', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Event(Thing):
    term = RdfTerm('Event', 'http://schema.org/Event', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Action(Thing):
    term = RdfTerm('Action', 'http://schema.org/Action', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BioChemEntity(Thing):
    term = RdfTerm('BioChemEntity', 'http://schema.org/BioChemEntity', ['1.2-DRAFT'])

class MedicalEntity(Thing):
    term = RdfTerm('MedicalEntity', 'http://schema.org/MedicalEntity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CreativeWork(Thing):
    term = RdfTerm('CreativeWork', 'http://schema.org/CreativeWork', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Product(Thing):
    term = RdfTerm('Product', 'http://schema.org/Product', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class StupidType(Thing):
    term = RdfTerm('StupidType', 'http://schema.org/StupidType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Intangible(Thing):
    term = RdfTerm('Intangible', 'http://schema.org/Intangible', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Taxon(Thing):
    term = RdfTerm('Taxon', 'http://schema.org/Taxon', ['1.2-DRAFT'])

class Place(Thing):
    term = RdfTerm('Place', 'http://schema.org/Place', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Person(Thing):
    term = RdfTerm('Person', 'http://schema.org/Person', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Organization(Thing):
    term = RdfTerm('Organization', 'http://schema.org/Organization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CourseInstance(Event):
    term = RdfTerm('CourseInstance', 'http://schema.org/CourseInstance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Hackathon(Event):
    term = RdfTerm('Hackathon', 'http://schema.org/Hackathon', ['1.1', '1.2-DRAFT'])

class LiteraryEvent(Event):
    term = RdfTerm('LiteraryEvent', 'http://schema.org/LiteraryEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EducationEvent(Event):
    term = RdfTerm('EducationEvent', 'http://schema.org/EducationEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserInteraction(Event):
    term = RdfTerm('UserInteraction', 'http://schema.org/UserInteraction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DeliveryEvent(Event):
    term = RdfTerm('DeliveryEvent', 'http://schema.org/DeliveryEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComedyEvent(Event):
    term = RdfTerm('ComedyEvent', 'http://schema.org/ComedyEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Festival(Event):
    term = RdfTerm('Festival', 'http://schema.org/Festival', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PublicationEvent(Event):
    term = RdfTerm('PublicationEvent', 'http://schema.org/PublicationEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SportsEvent(Event):
    term = RdfTerm('SportsEvent', 'http://schema.org/SportsEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TheaterEvent(Event):
    term = RdfTerm('TheaterEvent', 'http://schema.org/TheaterEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DanceEvent(Event):
    term = RdfTerm('DanceEvent', 'http://schema.org/DanceEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ExhibitionEvent(Event):
    term = RdfTerm('ExhibitionEvent', 'http://schema.org/ExhibitionEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FoodEvent(Event):
    term = RdfTerm('FoodEvent', 'http://schema.org/FoodEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicEvent(Event):
    term = RdfTerm('MusicEvent', 'http://schema.org/MusicEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SaleEvent(Event):
    term = RdfTerm('SaleEvent', 'http://schema.org/SaleEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ScreeningEvent(Event):
    term = RdfTerm('ScreeningEvent', 'http://schema.org/ScreeningEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SocialEvent(Event):
    term = RdfTerm('SocialEvent', 'http://schema.org/SocialEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ChildrensEvent(Event):
    term = RdfTerm('ChildrensEvent', 'http://schema.org/ChildrensEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BusinessEvent(Event):
    term = RdfTerm('BusinessEvent', 'http://schema.org/BusinessEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VisualArtsEvent(Event):
    term = RdfTerm('VisualArtsEvent', 'http://schema.org/VisualArtsEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TransferAction(Action):
    term = RdfTerm('TransferAction', 'http://schema.org/TransferAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SolveMathAction(Action):
    term = RdfTerm('SolveMathAction', 'http://schema.org/SolveMathAction', ['1.2-DRAFT'])

class AssessAction(Action):
    term = RdfTerm('AssessAction', 'http://schema.org/AssessAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SeekToAction(Action):
    term = RdfTerm('SeekToAction', 'http://schema.org/SeekToAction', ['1.2-DRAFT'])

class SearchAction(Action):
    term = RdfTerm('SearchAction', 'http://schema.org/SearchAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ConsumeAction(Action):
    term = RdfTerm('ConsumeAction', 'http://schema.org/ConsumeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PlayAction(Action):
    term = RdfTerm('PlayAction', 'http://schema.org/PlayAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OrganizeAction(Action):
    term = RdfTerm('OrganizeAction', 'http://schema.org/OrganizeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MoveAction(Action):
    term = RdfTerm('MoveAction', 'http://schema.org/MoveAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CreateAction(Action):
    term = RdfTerm('CreateAction', 'http://schema.org/CreateAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AchieveAction(Action):
    term = RdfTerm('AchieveAction', 'http://schema.org/AchieveAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FindAction(Action):
    term = RdfTerm('FindAction', 'http://schema.org/FindAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TradeAction(Action):
    term = RdfTerm('TradeAction', 'http://schema.org/TradeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ControlAction(Action):
    term = RdfTerm('ControlAction', 'http://schema.org/ControlAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UpdateAction(Action):
    term = RdfTerm('UpdateAction', 'http://schema.org/UpdateAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InteractAction(Action):
    term = RdfTerm('InteractAction', 'http://schema.org/InteractAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ChemicalSubstance(BioChemEntity):
    term = RdfTerm('ChemicalSubstance', 'http://schema.org/ChemicalSubstance', ['1.2-DRAFT'])

class Gene(BioChemEntity):
    term = RdfTerm('Gene', 'http://schema.org/Gene', ['1.2-DRAFT'])

class Protein(BioChemEntity):
    term = RdfTerm('Protein', 'http://schema.org/Protein', ['1.2-DRAFT'])

class MolecularEntity(BioChemEntity):
    term = RdfTerm('MolecularEntity', 'http://schema.org/MolecularEntity', ['1.2-DRAFT'])

class MedicalIndication(MedicalEntity):
    term = RdfTerm('MedicalIndication', 'http://schema.org/MedicalIndication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalRiskEstimator(MedicalEntity):
    term = RdfTerm('MedicalRiskEstimator', 'http://schema.org/MedicalRiskEstimator', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalDevice(MedicalEntity):
    term = RdfTerm('MedicalDevice', 'http://schema.org/MedicalDevice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalRiskFactor(MedicalEntity):
    term = RdfTerm('MedicalRiskFactor', 'http://schema.org/MedicalRiskFactor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrugCost(MedicalEntity):
    term = RdfTerm('DrugCost', 'http://schema.org/DrugCost', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalStudy(MedicalEntity):
    term = RdfTerm('MedicalStudy', 'http://schema.org/MedicalStudy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AnatomicalSystem(MedicalEntity):
    term = RdfTerm('AnatomicalSystem', 'http://schema.org/AnatomicalSystem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrugClass(MedicalEntity):
    term = RdfTerm('DrugClass', 'http://schema.org/DrugClass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Substance(MedicalEntity):
    term = RdfTerm('Substance', 'http://schema.org/Substance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalCause(MedicalEntity):
    term = RdfTerm('MedicalCause', 'http://schema.org/MedicalCause', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalProcedure(MedicalEntity):
    term = RdfTerm('MedicalProcedure', 'http://schema.org/MedicalProcedure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalIntangible(MedicalEntity):
    term = RdfTerm('MedicalIntangible', 'http://schema.org/MedicalIntangible', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalCondition(MedicalEntity):
    term = RdfTerm('MedicalCondition', 'http://schema.org/MedicalCondition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AnatomicalStructure(MedicalEntity):
    term = RdfTerm('AnatomicalStructure', 'http://schema.org/AnatomicalStructure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalTest(MedicalEntity):
    term = RdfTerm('MedicalTest', 'http://schema.org/MedicalTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LifestyleModification(MedicalEntity):
    term = RdfTerm('LifestyleModification', 'http://schema.org/LifestyleModification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalGuideline(MedicalEntity):
    term = RdfTerm('MedicalGuideline', 'http://schema.org/MedicalGuideline', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalContraindication(MedicalEntity):
    term = RdfTerm('MedicalContraindication', 'http://schema.org/MedicalContraindication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SuperficialAnatomy(MedicalEntity):
    term = RdfTerm('SuperficialAnatomy', 'http://schema.org/SuperficialAnatomy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Sculpture(CreativeWork):
    term = RdfTerm('Sculpture', 'http://schema.org/Sculpture', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Quotation(CreativeWork):
    term = RdfTerm('Quotation', 'http://schema.org/Quotation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Legislation(CreativeWork):
    term = RdfTerm('Legislation', 'http://schema.org/Legislation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Dataset(CreativeWork):
    term = RdfTerm('Dataset', 'http://schema.org/Dataset', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Blog(CreativeWork):
    term = RdfTerm('Blog', 'http://schema.org/Blog', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicPlaylist(CreativeWork):
    term = RdfTerm('MusicPlaylist', 'http://schema.org/MusicPlaylist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowTo(CreativeWork):
    term = RdfTerm('HowTo', 'http://schema.org/HowTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Manuscript(CreativeWork):
    term = RdfTerm('Manuscript', 'http://schema.org/Manuscript', ['1.0', '1.1', '1.2-DRAFT'])

class Conversation(CreativeWork):
    term = RdfTerm('Conversation', 'http://schema.org/Conversation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ShortStory(CreativeWork):
    term = RdfTerm('ShortStory', 'http://schema.org/ShortStory', ['1.0', '1.1', '1.2-DRAFT'])

class Thesis(CreativeWork):
    term = RdfTerm('Thesis', 'http://schema.org/Thesis', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Article(CreativeWork):
    term = RdfTerm('Article', 'http://schema.org/Article', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Drawing(CreativeWork):
    term = RdfTerm('Drawing', 'http://schema.org/Drawing', ['1.0', '1.1', '1.2-DRAFT'])

class WebContent(CreativeWork):
    term = RdfTerm('WebContent', 'http://schema.org/WebContent', ['1.0', '1.1', '1.2-DRAFT'])

class Game(CreativeWork):
    term = RdfTerm('Game', 'http://schema.org/Game', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComicStory(CreativeWork):
    term = RdfTerm('ComicStory', 'http://schema.org/ComicStory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Season(CreativeWork):
    term = RdfTerm('Season', 'http://schema.org/Season', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Atlas(CreativeWork):
    term = RdfTerm('Atlas', 'http://schema.org/Atlas', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Clip(CreativeWork):
    term = RdfTerm('Clip', 'http://schema.org/Clip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WebSite(CreativeWork):
    term = RdfTerm('WebSite', 'http://schema.org/WebSite', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WebPageElement(CreativeWork):
    term = RdfTerm('WebPageElement', 'http://schema.org/WebPageElement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MediaObject(CreativeWork):
    term = RdfTerm('MediaObject', 'http://schema.org/MediaObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Painting(CreativeWork):
    term = RdfTerm('Painting', 'http://schema.org/Painting', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SoftwareApplication(CreativeWork):
    term = RdfTerm('SoftwareApplication', 'http://schema.org/SoftwareApplication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Claim(CreativeWork):
    term = RdfTerm('Claim', 'http://schema.org/Claim', ['1.0', '1.1', '1.2-DRAFT'])

class PublicationIssue(CreativeWork):
    term = RdfTerm('PublicationIssue', 'http://schema.org/PublicationIssue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ArchiveComponent(CreativeWork):
    term = RdfTerm('ArchiveComponent', 'http://schema.org/ArchiveComponent', ['1.0', '1.1', '1.2-DRAFT'])

class DataCatalog(CreativeWork):
    term = RdfTerm('DataCatalog', 'http://schema.org/DataCatalog', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Play(CreativeWork):
    term = RdfTerm('Play', 'http://schema.org/Play', ['1.0', '1.1', '1.2-DRAFT'])

class MenuSection(CreativeWork):
    term = RdfTerm('MenuSection', 'http://schema.org/MenuSection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VisualArtwork(CreativeWork):
    term = RdfTerm('VisualArtwork', 'http://schema.org/VisualArtwork', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LearningResource(CreativeWork):
    term = RdfTerm('LearningResource', 'http://schema.org/LearningResource', ['1.1', '1.2-DRAFT'])

class MusicRecording(CreativeWork):
    term = RdfTerm('MusicRecording', 'http://schema.org/MusicRecording', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WebPage(CreativeWork):
    term = RdfTerm('WebPage', 'http://schema.org/WebPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HyperTocEntry(CreativeWork):
    term = RdfTerm('HyperTocEntry', 'http://schema.org/HyperTocEntry', ['1.2-DRAFT'])

class Statement(CreativeWork):
    term = RdfTerm('Statement', 'http://schema.org/Statement', ['1.2-DRAFT'])

class Book(CreativeWork):
    term = RdfTerm('Book', 'http://schema.org/Book', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Review(CreativeWork):
    term = RdfTerm('Review', 'http://schema.org/Review', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Chapter(CreativeWork):
    term = RdfTerm('Chapter', 'http://schema.org/Chapter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Menu(CreativeWork):
    term = RdfTerm('Menu', 'http://schema.org/Menu', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SpecialAnnouncement(CreativeWork):
    term = RdfTerm('SpecialAnnouncement', 'http://schema.org/SpecialAnnouncement', ['1.1', '1.2-DRAFT'])

class Collection(CreativeWork):
    term = RdfTerm('Collection', 'http://schema.org/Collection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Certification(CreativeWork):
    term = RdfTerm('Certification', 'http://schema.org/Certification', [])

class DigitalDocument(CreativeWork):
    term = RdfTerm('DigitalDocument', 'http://schema.org/DigitalDocument', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Message(CreativeWork):
    term = RdfTerm('Message', 'http://schema.org/Message', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DefinedTermSet(CreativeWork):
    term = RdfTerm('DefinedTermSet', 'http://schema.org/DefinedTermSet', ['1.0', '1.1', '1.2-DRAFT'])

class Guide(CreativeWork):
    term = RdfTerm('Guide', 'http://schema.org/Guide', ['1.1', '1.2-DRAFT'])

class EducationalOccupationalCredential(CreativeWork):
    term = RdfTerm('EducationalOccupationalCredential', 'http://schema.org/EducationalOccupationalCredential', ['1.0', '1.1', '1.2-DRAFT'])

class Map(CreativeWork):
    term = RdfTerm('Map', 'http://schema.org/Map', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Episode(CreativeWork):
    term = RdfTerm('Episode', 'http://schema.org/Episode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Photograph(CreativeWork):
    term = RdfTerm('Photograph', 'http://schema.org/Photograph', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicComposition(CreativeWork):
    term = RdfTerm('MusicComposition', 'http://schema.org/MusicComposition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Code(CreativeWork):
    term = RdfTerm('Code', 'http://schema.org/Code', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SoftwareSourceCode(CreativeWork):
    term = RdfTerm('SoftwareSourceCode', 'http://schema.org/SoftwareSourceCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MathSolver(CreativeWork):
    term = RdfTerm('MathSolver', 'http://schema.org/MathSolver', ['1.2-DRAFT'])

class SheetMusic(CreativeWork):
    term = RdfTerm('SheetMusic', 'http://schema.org/SheetMusic', ['1.0', '1.1', '1.2-DRAFT'])

class MediaReviewItem(CreativeWork):
    term = RdfTerm('MediaReviewItem', 'http://schema.org/MediaReviewItem', ['1.2-DRAFT'])

class Comment(CreativeWork):
    term = RdfTerm('Comment', 'http://schema.org/Comment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Poster(CreativeWork):
    term = RdfTerm('Poster', 'http://schema.org/Poster', ['1.0', '1.1', '1.2-DRAFT'])

class Movie(CreativeWork):
    term = RdfTerm('Movie', 'http://schema.org/Movie', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HyperToc(CreativeWork):
    term = RdfTerm('HyperToc', 'http://schema.org/HyperToc', ['1.2-DRAFT'])

class CreativeWorkSeason(CreativeWork):
    term = RdfTerm('CreativeWorkSeason', 'http://schema.org/CreativeWorkSeason', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PublicationVolume(CreativeWork):
    term = RdfTerm('PublicationVolume', 'http://schema.org/PublicationVolume', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ProductGroup(Product):
    term = RdfTerm('ProductGroup', 'http://schema.org/ProductGroup', ['1.1', '1.2-DRAFT'])

class ProductModel(Product):
    term = RdfTerm('ProductModel', 'http://schema.org/ProductModel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class IndividualProduct(Product):
    term = RdfTerm('IndividualProduct', 'http://schema.org/IndividualProduct', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SomeProducts(Product):
    term = RdfTerm('SomeProducts', 'http://schema.org/SomeProducts', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Vehicle(Product):
    term = RdfTerm('Vehicle', 'http://schema.org/Vehicle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Invoice(Intangible):
    term = RdfTerm('Invoice', 'http://schema.org/Invoice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MediaSubscription(Intangible):
    term = RdfTerm('MediaSubscription', 'http://schema.org/MediaSubscription', ['1.0', '1.1', '1.2-DRAFT'])

class MerchantReturnPolicy(Intangible):
    term = RdfTerm('MerchantReturnPolicy', 'http://schema.org/MerchantReturnPolicy', ['1.1', '1.2-DRAFT'])

class Class(Intangible):
    term = RdfTerm('Class', 'http://schema.org/Class', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Quantity(Intangible):
    term = RdfTerm('Quantity', 'http://schema.org/Quantity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FinancialIncentive(Intangible):
    term = RdfTerm('FinancialIncentive', 'http://schema.org/FinancialIncentive', [])

class MemberProgram(Intangible):
    term = RdfTerm('MemberProgram', 'http://schema.org/MemberProgram', [])

class Enumeration(Intangible):
    term = RdfTerm('Enumeration', 'http://schema.org/Enumeration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Occupation(Intangible):
    term = RdfTerm('Occupation', 'http://schema.org/Occupation', ['1.0', '1.1', '1.2-DRAFT'])

class StatisticalPopulation(Intangible):
    term = RdfTerm('StatisticalPopulation', 'http://schema.org/StatisticalPopulation', ['1.0', '1.1', '1.2-DRAFT'])

class Demand(Intangible):
    term = RdfTerm('Demand', 'http://schema.org/Demand', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Role(Intangible):
    term = RdfTerm('Role', 'http://schema.org/Role', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BroadcastFrequencySpecification(Intangible):
    term = RdfTerm('BroadcastFrequencySpecification', 'http://schema.org/BroadcastFrequencySpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HealthInsurancePlan(Intangible):
    term = RdfTerm('HealthInsurancePlan', 'http://schema.org/HealthInsurancePlan', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Permit(Intangible):
    term = RdfTerm('Permit', 'http://schema.org/Permit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GameServer(Intangible):
    term = RdfTerm('GameServer', 'http://schema.org/GameServer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PaymentMethod(Intangible):
    term = RdfTerm('PaymentMethod', 'http://schema.org/PaymentMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MemberProgramTier(Intangible):
    term = RdfTerm('MemberProgramTier', 'http://schema.org/MemberProgramTier', [])

class HealthPlanFormulary(Intangible):
    term = RdfTerm('HealthPlanFormulary', 'http://schema.org/HealthPlanFormulary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GeospatialGeometry(Intangible):
    term = RdfTerm('GeospatialGeometry', 'http://schema.org/GeospatialGeometry', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Property(Intangible):
    term = RdfTerm('Property', 'http://schema.org/Property', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Reservation(Intangible):
    term = RdfTerm('Reservation', 'http://schema.org/Reservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DigitalDocumentPermission(Intangible):
    term = RdfTerm('DigitalDocumentPermission', 'http://schema.org/DigitalDocumentPermission', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HealthPlanNetwork(Intangible):
    term = RdfTerm('HealthPlanNetwork', 'http://schema.org/HealthPlanNetwork', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AlignmentObject(Intangible):
    term = RdfTerm('AlignmentObject', 'http://schema.org/AlignmentObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MenuItem(Intangible):
    term = RdfTerm('MenuItem', 'http://schema.org/MenuItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DataFeedItem(Intangible):
    term = RdfTerm('DataFeedItem', 'http://schema.org/DataFeedItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ParcelDelivery(Intangible):
    term = RdfTerm('ParcelDelivery', 'http://schema.org/ParcelDelivery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EntryPoint(Intangible):
    term = RdfTerm('EntryPoint', 'http://schema.org/EntryPoint', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PropertyValueSpecification(Intangible):
    term = RdfTerm('PropertyValueSpecification', 'http://schema.org/PropertyValueSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ListItem(Intangible):
    term = RdfTerm('ListItem', 'http://schema.org/ListItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Seat(Intangible):
    term = RdfTerm('Seat', 'http://schema.org/Seat', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Audience(Intangible):
    term = RdfTerm('Audience', 'http://schema.org/Audience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ProgramMembership(Intangible):
    term = RdfTerm('ProgramMembership', 'http://schema.org/ProgramMembership', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Schedule(Intangible):
    term = RdfTerm('Schedule', 'http://schema.org/Schedule', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ConstraintNode(Intangible):
    term = RdfTerm('ConstraintNode', 'http://schema.org/ConstraintNode', ['1.2-DRAFT'])

class Offer(Intangible):
    term = RdfTerm('Offer', 'http://schema.org/Offer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Language(Intangible):
    term = RdfTerm('Language', 'http://schema.org/Language', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OrderItem(Intangible):
    term = RdfTerm('OrderItem', 'http://schema.org/OrderItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Series(Intangible):
    term = RdfTerm('Series', 'http://schema.org/Series', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComputerLanguage(Intangible):
    term = RdfTerm('ComputerLanguage', 'http://schema.org/ComputerLanguage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MerchantReturnPolicySeasonalOverride(Intangible):
    term = RdfTerm('MerchantReturnPolicySeasonalOverride', 'http://schema.org/MerchantReturnPolicySeasonalOverride', ['1.2-DRAFT'])

class SpeakableSpecification(Intangible):
    term = RdfTerm('SpeakableSpecification', 'http://schema.org/SpeakableSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FloorPlan(Intangible):
    term = RdfTerm('FloorPlan', 'http://schema.org/FloorPlan', ['1.1', '1.2-DRAFT'])

class Brand(Intangible):
    term = RdfTerm('Brand', 'http://schema.org/Brand', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EducationalOccupationalProgram(Intangible):
    term = RdfTerm('EducationalOccupationalProgram', 'http://schema.org/EducationalOccupationalProgram', ['1.0', '1.1', '1.2-DRAFT'])

class HealthPlanCostSharingSpecification(Intangible):
    term = RdfTerm('HealthPlanCostSharingSpecification', 'http://schema.org/HealthPlanCostSharingSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class JobPosting(Intangible):
    term = RdfTerm('JobPosting', 'http://schema.org/JobPosting', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Ticket(Intangible):
    term = RdfTerm('Ticket', 'http://schema.org/Ticket', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BedDetails(Intangible):
    term = RdfTerm('BedDetails', 'http://schema.org/BedDetails', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ProductReturnPolicy(Intangible):
    term = RdfTerm('ProductReturnPolicy', 'http://schema.org/ProductReturnPolicy', ['1.0', '1.1', '1.2-DRAFT'])

class BroadcastChannel(Intangible):
    term = RdfTerm('BroadcastChannel', 'http://schema.org/BroadcastChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Trip(Intangible):
    term = RdfTerm('Trip', 'http://schema.org/Trip', ['1.0', '1.1', '1.2-DRAFT'])

class VirtualLocation(Intangible):
    term = RdfTerm('VirtualLocation', 'http://schema.org/VirtualLocation', ['1.1', '1.2-DRAFT'])

class Grant(Intangible):
    term = RdfTerm('Grant', 'http://schema.org/Grant', ['1.0', '1.1', '1.2-DRAFT'])

class ServiceChannel(Intangible):
    term = RdfTerm('ServiceChannel', 'http://schema.org/ServiceChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Service(Intangible):
    term = RdfTerm('Service', 'http://schema.org/Service', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ItemList(Intangible):
    term = RdfTerm('ItemList', 'http://schema.org/ItemList', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OccupationalExperienceRequirements(Intangible):
    term = RdfTerm('OccupationalExperienceRequirements', 'http://schema.org/OccupationalExperienceRequirements', ['1.2-DRAFT'])

class StructuredValue(Intangible):
    term = RdfTerm('StructuredValue', 'http://schema.org/StructuredValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Order(Intangible):
    term = RdfTerm('Order', 'http://schema.org/Order', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DefinedTerm(Intangible):
    term = RdfTerm('DefinedTerm', 'http://schema.org/DefinedTerm', ['1.0', '1.1', '1.2-DRAFT'])

class ActionAccessSpecification(Intangible):
    term = RdfTerm('ActionAccessSpecification', 'http://schema.org/ActionAccessSpecification', ['1.0', '1.1', '1.2-DRAFT'])

class EnergyConsumptionDetails(Intangible):
    term = RdfTerm('EnergyConsumptionDetails', 'http://schema.org/EnergyConsumptionDetails', ['1.1', '1.2-DRAFT'])

class Rating(Intangible):
    term = RdfTerm('Rating', 'http://schema.org/Rating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Residence(Place):
    term = RdfTerm('Residence', 'http://schema.org/Residence', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TouristDestination(Place):
    term = RdfTerm('TouristDestination', 'http://schema.org/TouristDestination', ['1.0', '1.1', '1.2-DRAFT'])

class TouristAttraction(Place):
    term = RdfTerm('TouristAttraction', 'http://schema.org/TouristAttraction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LandmarksOrHistoricalBuildings(Place):
    term = RdfTerm('LandmarksOrHistoricalBuildings', 'http://schema.org/LandmarksOrHistoricalBuildings', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Accommodation(Place):
    term = RdfTerm('Accommodation', 'http://schema.org/Accommodation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AdministrativeArea(Place):
    term = RdfTerm('AdministrativeArea', 'http://schema.org/AdministrativeArea', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CivicStructure(Place):
    term = RdfTerm('CivicStructure', 'http://schema.org/CivicStructure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Landform(Place):
    term = RdfTerm('Landform', 'http://schema.org/Landform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Project(Organization):
    term = RdfTerm('Project', 'http://schema.org/Project', ['1.0', '1.1', '1.2-DRAFT'])

class MedicalOrganization(Organization):
    term = RdfTerm('MedicalOrganization', 'http://schema.org/MedicalOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SearchRescueOrganization(Organization):
    term = RdfTerm('SearchRescueOrganization', 'http://schema.org/SearchRescueOrganization', ['1.2-DRAFT'])

class PoliticalParty(Organization):
    term = RdfTerm('PoliticalParty', 'http://schema.org/PoliticalParty', ['1.2-DRAFT'])

class LocalBusiness(Place, Organization):
    term = RdfTerm('LocalBusiness', 'http://schema.org/LocalBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ResearchOrganization(Organization):
    term = RdfTerm('ResearchOrganization', 'http://schema.org/ResearchOrganization', ['1.2-DRAFT'])

class SportsOrganization(Organization):
    term = RdfTerm('SportsOrganization', 'http://schema.org/SportsOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LibrarySystem(Organization):
    term = RdfTerm('LibrarySystem', 'http://schema.org/LibrarySystem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PerformingGroup(Organization):
    term = RdfTerm('PerformingGroup', 'http://schema.org/PerformingGroup', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Corporation(Organization):
    term = RdfTerm('Corporation', 'http://schema.org/Corporation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Consortium(Organization):
    term = RdfTerm('Consortium', 'http://schema.org/Consortium', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WorkersUnion(Organization):
    term = RdfTerm('WorkersUnion', 'http://schema.org/WorkersUnion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class NewsMediaOrganization(Organization):
    term = RdfTerm('NewsMediaOrganization', 'http://schema.org/NewsMediaOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class NGO(Organization):
    term = RdfTerm('NGO', 'http://schema.org/NGO', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OnlineBusiness(Organization):
    term = RdfTerm('OnlineBusiness', 'http://schema.org/OnlineBusiness', ['1.2-DRAFT'])

class GovernmentOrganization(Organization):
    term = RdfTerm('GovernmentOrganization', 'http://schema.org/GovernmentOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FundingScheme(Organization):
    term = RdfTerm('FundingScheme', 'http://schema.org/FundingScheme', ['1.0', '1.1', '1.2-DRAFT'])

class Airline(Organization):
    term = RdfTerm('Airline', 'http://schema.org/Airline', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserBlocks(UserInteraction):
    term = RdfTerm('UserBlocks', 'http://schema.org/UserBlocks', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserDownloads(UserInteraction):
    term = RdfTerm('UserDownloads', 'http://schema.org/UserDownloads', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserTweets(UserInteraction):
    term = RdfTerm('UserTweets', 'http://schema.org/UserTweets', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserCheckins(UserInteraction):
    term = RdfTerm('UserCheckins', 'http://schema.org/UserCheckins', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserPlays(UserInteraction):
    term = RdfTerm('UserPlays', 'http://schema.org/UserPlays', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserPageVisits(UserInteraction):
    term = RdfTerm('UserPageVisits', 'http://schema.org/UserPageVisits', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserLikes(UserInteraction):
    term = RdfTerm('UserLikes', 'http://schema.org/UserLikes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserComments(UserInteraction):
    term = RdfTerm('UserComments', 'http://schema.org/UserComments', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UserPlusOnes(UserInteraction):
    term = RdfTerm('UserPlusOnes', 'http://schema.org/UserPlusOnes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OnDemandEvent(PublicationEvent):
    term = RdfTerm('OnDemandEvent', 'http://schema.org/OnDemandEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BroadcastEvent(PublicationEvent):
    term = RdfTerm('BroadcastEvent', 'http://schema.org/BroadcastEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DownloadAction(TransferAction):
    term = RdfTerm('DownloadAction', 'http://schema.org/DownloadAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReturnAction(TransferAction):
    term = RdfTerm('ReturnAction', 'http://schema.org/ReturnAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DonateAction(TransferAction):
    term = RdfTerm('DonateAction', 'http://schema.org/DonateAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GiveAction(TransferAction):
    term = RdfTerm('GiveAction', 'http://schema.org/GiveAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LendAction(TransferAction):
    term = RdfTerm('LendAction', 'http://schema.org/LendAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TakeAction(TransferAction):
    term = RdfTerm('TakeAction', 'http://schema.org/TakeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MoneyTransfer(TransferAction):
    term = RdfTerm('MoneyTransfer', 'http://schema.org/MoneyTransfer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BorrowAction(TransferAction):
    term = RdfTerm('BorrowAction', 'http://schema.org/BorrowAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReceiveAction(TransferAction):
    term = RdfTerm('ReceiveAction', 'http://schema.org/ReceiveAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SendAction(TransferAction):
    term = RdfTerm('SendAction', 'http://schema.org/SendAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class IgnoreAction(AssessAction):
    term = RdfTerm('IgnoreAction', 'http://schema.org/IgnoreAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReactAction(AssessAction):
    term = RdfTerm('ReactAction', 'http://schema.org/ReactAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ChooseAction(AssessAction):
    term = RdfTerm('ChooseAction', 'http://schema.org/ChooseAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReviewAction(AssessAction):
    term = RdfTerm('ReviewAction', 'http://schema.org/ReviewAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UseAction(ConsumeAction):
    term = RdfTerm('UseAction', 'http://schema.org/UseAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ViewAction(ConsumeAction):
    term = RdfTerm('ViewAction', 'http://schema.org/ViewAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InstallAction(ConsumeAction):
    term = RdfTerm('InstallAction', 'http://schema.org/InstallAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ListenAction(ConsumeAction):
    term = RdfTerm('ListenAction', 'http://schema.org/ListenAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReadAction(ConsumeAction):
    term = RdfTerm('ReadAction', 'http://schema.org/ReadAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrinkAction(ConsumeAction):
    term = RdfTerm('DrinkAction', 'http://schema.org/DrinkAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PlayGameAction(ConsumeAction):
    term = RdfTerm('PlayGameAction', 'http://schema.org/PlayGameAction', ['1.2-DRAFT'])

class WatchAction(ConsumeAction):
    term = RdfTerm('WatchAction', 'http://schema.org/WatchAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EatAction(ConsumeAction):
    term = RdfTerm('EatAction', 'http://schema.org/EatAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PerformAction(PlayAction):
    term = RdfTerm('PerformAction', 'http://schema.org/PerformAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ExerciseAction(PlayAction):
    term = RdfTerm('ExerciseAction', 'http://schema.org/ExerciseAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AllocateAction(OrganizeAction):
    term = RdfTerm('AllocateAction', 'http://schema.org/AllocateAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BookmarkAction(OrganizeAction):
    term = RdfTerm('BookmarkAction', 'http://schema.org/BookmarkAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PlanAction(OrganizeAction):
    term = RdfTerm('PlanAction', 'http://schema.org/PlanAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ApplyAction(OrganizeAction):
    term = RdfTerm('ApplyAction', 'http://schema.org/ApplyAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TravelAction(MoveAction):
    term = RdfTerm('TravelAction', 'http://schema.org/TravelAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ArriveAction(MoveAction):
    term = RdfTerm('ArriveAction', 'http://schema.org/ArriveAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DepartAction(MoveAction):
    term = RdfTerm('DepartAction', 'http://schema.org/DepartAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CookAction(CreateAction):
    term = RdfTerm('CookAction', 'http://schema.org/CookAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WriteAction(CreateAction):
    term = RdfTerm('WriteAction', 'http://schema.org/WriteAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FilmAction(CreateAction):
    term = RdfTerm('FilmAction', 'http://schema.org/FilmAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PhotographAction(CreateAction):
    term = RdfTerm('PhotographAction', 'http://schema.org/PhotographAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrawAction(CreateAction):
    term = RdfTerm('DrawAction', 'http://schema.org/DrawAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PaintAction(CreateAction):
    term = RdfTerm('PaintAction', 'http://schema.org/PaintAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LoseAction(AchieveAction):
    term = RdfTerm('LoseAction', 'http://schema.org/LoseAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WinAction(AchieveAction):
    term = RdfTerm('WinAction', 'http://schema.org/WinAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TieAction(AchieveAction):
    term = RdfTerm('TieAction', 'http://schema.org/TieAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TrackAction(FindAction):
    term = RdfTerm('TrackAction', 'http://schema.org/TrackAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CheckAction(FindAction):
    term = RdfTerm('CheckAction', 'http://schema.org/CheckAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DiscoverAction(FindAction):
    term = RdfTerm('DiscoverAction', 'http://schema.org/DiscoverAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OrderAction(TradeAction):
    term = RdfTerm('OrderAction', 'http://schema.org/OrderAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class QuoteAction(TradeAction):
    term = RdfTerm('QuoteAction', 'http://schema.org/QuoteAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SellAction(TradeAction):
    term = RdfTerm('SellAction', 'http://schema.org/SellAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RentAction(TradeAction):
    term = RdfTerm('RentAction', 'http://schema.org/RentAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PreOrderAction(TradeAction):
    term = RdfTerm('PreOrderAction', 'http://schema.org/PreOrderAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PayAction(TradeAction):
    term = RdfTerm('PayAction', 'http://schema.org/PayAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BuyAction(TradeAction):
    term = RdfTerm('BuyAction', 'http://schema.org/BuyAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TipAction(TradeAction):
    term = RdfTerm('TipAction', 'http://schema.org/TipAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ActivateAction(ControlAction):
    term = RdfTerm('ActivateAction', 'http://schema.org/ActivateAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DeactivateAction(ControlAction):
    term = RdfTerm('DeactivateAction', 'http://schema.org/DeactivateAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ResumeAction(ControlAction):
    term = RdfTerm('ResumeAction', 'http://schema.org/ResumeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SuspendAction(ControlAction):
    term = RdfTerm('SuspendAction', 'http://schema.org/SuspendAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReplaceAction(UpdateAction):
    term = RdfTerm('ReplaceAction', 'http://schema.org/ReplaceAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AddAction(UpdateAction):
    term = RdfTerm('AddAction', 'http://schema.org/AddAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DeleteAction(UpdateAction):
    term = RdfTerm('DeleteAction', 'http://schema.org/DeleteAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SubscribeAction(InteractAction):
    term = RdfTerm('SubscribeAction', 'http://schema.org/SubscribeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BefriendAction(InteractAction):
    term = RdfTerm('BefriendAction', 'http://schema.org/BefriendAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RegisterAction(InteractAction):
    term = RdfTerm('RegisterAction', 'http://schema.org/RegisterAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FollowAction(InteractAction):
    term = RdfTerm('FollowAction', 'http://schema.org/FollowAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MarryAction(InteractAction):
    term = RdfTerm('MarryAction', 'http://schema.org/MarryAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LeaveAction(InteractAction):
    term = RdfTerm('LeaveAction', 'http://schema.org/LeaveAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class JoinAction(InteractAction):
    term = RdfTerm('JoinAction', 'http://schema.org/JoinAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UnRegisterAction(InteractAction):
    term = RdfTerm('UnRegisterAction', 'http://schema.org/UnRegisterAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CommunicateAction(InteractAction):
    term = RdfTerm('CommunicateAction', 'http://schema.org/CommunicateAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TreatmentIndication(MedicalIndication):
    term = RdfTerm('TreatmentIndication', 'http://schema.org/TreatmentIndication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ApprovedIndication(MedicalIndication):
    term = RdfTerm('ApprovedIndication', 'http://schema.org/ApprovedIndication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PreventionIndication(MedicalIndication):
    term = RdfTerm('PreventionIndication', 'http://schema.org/PreventionIndication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalRiskScore(MedicalRiskEstimator):
    term = RdfTerm('MedicalRiskScore', 'http://schema.org/MedicalRiskScore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalRiskCalculator(MedicalRiskEstimator):
    term = RdfTerm('MedicalRiskCalculator', 'http://schema.org/MedicalRiskCalculator', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalTrial(MedicalStudy):
    term = RdfTerm('MedicalTrial', 'http://schema.org/MedicalTrial', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalObservationalStudy(MedicalStudy):
    term = RdfTerm('MedicalObservationalStudy', 'http://schema.org/MedicalObservationalStudy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DietarySupplement(Product, Substance):
    term = RdfTerm('DietarySupplement', 'http://schema.org/DietarySupplement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Drug(Substance, Product):
    term = RdfTerm('Drug', 'http://schema.org/Drug', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SurgicalProcedure(MedicalProcedure):
    term = RdfTerm('SurgicalProcedure', 'http://schema.org/SurgicalProcedure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DiagnosticProcedure(MedicalProcedure):
    term = RdfTerm('DiagnosticProcedure', 'http://schema.org/DiagnosticProcedure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TherapeuticProcedure(MedicalProcedure):
    term = RdfTerm('TherapeuticProcedure', 'http://schema.org/TherapeuticProcedure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrugLegalStatus(MedicalIntangible):
    term = RdfTerm('DrugLegalStatus', 'http://schema.org/DrugLegalStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrugStrength(MedicalIntangible):
    term = RdfTerm('DrugStrength', 'http://schema.org/DrugStrength', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DDxElement(MedicalIntangible):
    term = RdfTerm('DDxElement', 'http://schema.org/DDxElement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DoseSchedule(MedicalIntangible):
    term = RdfTerm('DoseSchedule', 'http://schema.org/DoseSchedule', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalConditionStage(MedicalIntangible):
    term = RdfTerm('MedicalConditionStage', 'http://schema.org/MedicalConditionStage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalSignOrSymptom(MedicalCondition):
    term = RdfTerm('MedicalSignOrSymptom', 'http://schema.org/MedicalSignOrSymptom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InfectiousDisease(MedicalCondition):
    term = RdfTerm('InfectiousDisease', 'http://schema.org/InfectiousDisease', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Nerve(AnatomicalStructure):
    term = RdfTerm('Nerve', 'http://schema.org/Nerve', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BrainStructure(AnatomicalStructure):
    term = RdfTerm('BrainStructure', 'http://schema.org/BrainStructure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Ligament(AnatomicalStructure):
    term = RdfTerm('Ligament', 'http://schema.org/Ligament', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Vessel(AnatomicalStructure):
    term = RdfTerm('Vessel', 'http://schema.org/Vessel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Joint(AnatomicalStructure):
    term = RdfTerm('Joint', 'http://schema.org/Joint', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Muscle(AnatomicalStructure):
    term = RdfTerm('Muscle', 'http://schema.org/Muscle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Bone(AnatomicalStructure):
    term = RdfTerm('Bone', 'http://schema.org/Bone', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PathologyTest(MedicalTest):
    term = RdfTerm('PathologyTest', 'http://schema.org/PathologyTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BloodTest(MedicalTest):
    term = RdfTerm('BloodTest', 'http://schema.org/BloodTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ImagingTest(MedicalTest):
    term = RdfTerm('ImagingTest', 'http://schema.org/ImagingTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalTestPanel(MedicalTest):
    term = RdfTerm('MedicalTestPanel', 'http://schema.org/MedicalTestPanel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PhysicalActivity(LifestyleModification):
    term = RdfTerm('PhysicalActivity', 'http://schema.org/PhysicalActivity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Diet(LifestyleModification, CreativeWork):
    term = RdfTerm('Diet', 'http://schema.org/Diet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalGuidelineRecommendation(MedicalGuideline):
    term = RdfTerm('MedicalGuidelineRecommendation', 'http://schema.org/MedicalGuidelineRecommendation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalGuidelineContraindication(MedicalGuideline):
    term = RdfTerm('MedicalGuidelineContraindication', 'http://schema.org/MedicalGuidelineContraindication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DataFeed(Dataset):
    term = RdfTerm('DataFeed', 'http://schema.org/DataFeed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicRelease(MusicPlaylist):
    term = RdfTerm('MusicRelease', 'http://schema.org/MusicRelease', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicAlbum(MusicPlaylist):
    term = RdfTerm('MusicAlbum', 'http://schema.org/MusicAlbum', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Recipe(HowTo):
    term = RdfTerm('Recipe', 'http://schema.org/Recipe', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TechArticle(Article):
    term = RdfTerm('TechArticle', 'http://schema.org/TechArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ScholarlyArticle(Article):
    term = RdfTerm('ScholarlyArticle', 'http://schema.org/ScholarlyArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AdvertiserContentArticle(Article):
    term = RdfTerm('AdvertiserContentArticle', 'http://schema.org/AdvertiserContentArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SocialMediaPosting(Article):
    term = RdfTerm('SocialMediaPosting', 'http://schema.org/SocialMediaPosting', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class NewsArticle(Article):
    term = RdfTerm('NewsArticle', 'http://schema.org/NewsArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SatiricalArticle(Article):
    term = RdfTerm('SatiricalArticle', 'http://schema.org/SatiricalArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Report(Article):
    term = RdfTerm('Report', 'http://schema.org/Report', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HealthTopicContent(WebContent):
    term = RdfTerm('HealthTopicContent', 'http://schema.org/HealthTopicContent', ['1.0', '1.1', '1.2-DRAFT'])

class RadioClip(Clip):
    term = RdfTerm('RadioClip', 'http://schema.org/RadioClip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TVClip(Clip):
    term = RdfTerm('TVClip', 'http://schema.org/TVClip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VideoGameClip(Clip):
    term = RdfTerm('VideoGameClip', 'http://schema.org/VideoGameClip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MovieClip(Clip):
    term = RdfTerm('MovieClip', 'http://schema.org/MovieClip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Table(WebPageElement):
    term = RdfTerm('Table', 'http://schema.org/Table', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SiteNavigationElement(WebPageElement):
    term = RdfTerm('SiteNavigationElement', 'http://schema.org/SiteNavigationElement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WPSideBar(WebPageElement):
    term = RdfTerm('WPSideBar', 'http://schema.org/WPSideBar', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WPAdBlock(WebPageElement):
    term = RdfTerm('WPAdBlock', 'http://schema.org/WPAdBlock', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WPHeader(WebPageElement):
    term = RdfTerm('WPHeader', 'http://schema.org/WPHeader', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WPFooter(WebPageElement):
    term = RdfTerm('WPFooter', 'http://schema.org/WPFooter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class _3DModel(MediaObject):
    term = RdfTerm('3DModel', 'http://schema.org/3DModel', ['1.0', '1.1', '1.2-DRAFT'])

class LegislationObject(Legislation, MediaObject):
    term = RdfTerm('LegislationObject', 'http://schema.org/LegislationObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicVideoObject(MediaObject):
    term = RdfTerm('MusicVideoObject', 'http://schema.org/MusicVideoObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VideoObject(MediaObject):
    term = RdfTerm('VideoObject', 'http://schema.org/VideoObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DataDownload(MediaObject):
    term = RdfTerm('DataDownload', 'http://schema.org/DataDownload', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AudioObject(MediaObject):
    term = RdfTerm('AudioObject', 'http://schema.org/AudioObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ImageObject(MediaObject):
    term = RdfTerm('ImageObject', 'http://schema.org/ImageObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TextObject(MediaObject):
    term = RdfTerm('TextObject', 'http://schema.org/TextObject', ['1.2-DRAFT'])

class AmpStory(MediaObject, CreativeWork):
    term = RdfTerm('AmpStory', 'http://schema.org/AmpStory', ['1.2-DRAFT'])

class VideoGame(Game, SoftwareApplication):
    term = RdfTerm('VideoGame', 'http://schema.org/VideoGame', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WebApplication(SoftwareApplication):
    term = RdfTerm('WebApplication', 'http://schema.org/WebApplication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MobileApplication(SoftwareApplication):
    term = RdfTerm('MobileApplication', 'http://schema.org/MobileApplication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComicIssue(PublicationIssue):
    term = RdfTerm('ComicIssue', 'http://schema.org/ComicIssue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CoverArt(VisualArtwork):
    term = RdfTerm('CoverArt', 'http://schema.org/CoverArt', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Course(CreativeWork, LearningResource):
    term = RdfTerm('Course', 'http://schema.org/Course', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Quiz(LearningResource):
    term = RdfTerm('Quiz', 'http://schema.org/Quiz', ['1.1', '1.2-DRAFT'])

class Syllabus(LearningResource):
    term = RdfTerm('Syllabus', 'http://schema.org/Syllabus', ['1.2-DRAFT'])

class SearchResultsPage(WebPage):
    term = RdfTerm('SearchResultsPage', 'http://schema.org/SearchResultsPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CollectionPage(WebPage):
    term = RdfTerm('CollectionPage', 'http://schema.org/CollectionPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AboutPage(WebPage):
    term = RdfTerm('AboutPage', 'http://schema.org/AboutPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalWebPage(WebPage):
    term = RdfTerm('MedicalWebPage', 'http://schema.org/MedicalWebPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RealEstateListing(WebPage):
    term = RdfTerm('RealEstateListing', 'http://schema.org/RealEstateListing', ['1.0', '1.1', '1.2-DRAFT'])

class ItemPage(WebPage):
    term = RdfTerm('ItemPage', 'http://schema.org/ItemPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CheckoutPage(WebPage):
    term = RdfTerm('CheckoutPage', 'http://schema.org/CheckoutPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class QAPage(WebPage):
    term = RdfTerm('QAPage', 'http://schema.org/QAPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ContactPage(WebPage):
    term = RdfTerm('ContactPage', 'http://schema.org/ContactPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FAQPage(WebPage):
    term = RdfTerm('FAQPage', 'http://schema.org/FAQPage', ['1.0', '1.1', '1.2-DRAFT'])

class ProfilePage(WebPage):
    term = RdfTerm('ProfilePage', 'http://schema.org/ProfilePage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MediaReview(Review):
    term = RdfTerm('MediaReview', 'http://schema.org/MediaReview', ['1.1', '1.2-DRAFT'])

class Recommendation(Review):
    term = RdfTerm('Recommendation', 'http://schema.org/Recommendation', ['1.1', '1.2-DRAFT'])

class UserReview(Review):
    term = RdfTerm('UserReview', 'http://schema.org/UserReview', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CriticReview(Review):
    term = RdfTerm('CriticReview', 'http://schema.org/CriticReview', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EmployerReview(Review):
    term = RdfTerm('EmployerReview', 'http://schema.org/EmployerReview', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ClaimReview(Review):
    term = RdfTerm('ClaimReview', 'http://schema.org/ClaimReview', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ProductCollection(Product, Collection):
    term = RdfTerm('ProductCollection', 'http://schema.org/ProductCollection', ['1.1', '1.2-DRAFT'])

class NoteDigitalDocument(DigitalDocument):
    term = RdfTerm('NoteDigitalDocument', 'http://schema.org/NoteDigitalDocument', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TextDigitalDocument(DigitalDocument):
    term = RdfTerm('TextDigitalDocument', 'http://schema.org/TextDigitalDocument', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PresentationDigitalDocument(DigitalDocument):
    term = RdfTerm('PresentationDigitalDocument', 'http://schema.org/PresentationDigitalDocument', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SpreadsheetDigitalDocument(DigitalDocument):
    term = RdfTerm('SpreadsheetDigitalDocument', 'http://schema.org/SpreadsheetDigitalDocument', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EmailMessage(Message):
    term = RdfTerm('EmailMessage', 'http://schema.org/EmailMessage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CategoryCodeSet(DefinedTermSet):
    term = RdfTerm('CategoryCodeSet', 'http://schema.org/CategoryCodeSet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PodcastEpisode(Episode):
    term = RdfTerm('PodcastEpisode', 'http://schema.org/PodcastEpisode', ['1.0', '1.1', '1.2-DRAFT'])

class RadioEpisode(Episode):
    term = RdfTerm('RadioEpisode', 'http://schema.org/RadioEpisode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TVEpisode(Episode):
    term = RdfTerm('TVEpisode', 'http://schema.org/TVEpisode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Question(Comment):
    term = RdfTerm('Question', 'http://schema.org/Question', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CorrectionComment(Comment):
    term = RdfTerm('CorrectionComment', 'http://schema.org/CorrectionComment', ['1.0', '1.1', '1.2-DRAFT'])

class Answer(Comment):
    term = RdfTerm('Answer', 'http://schema.org/Answer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TVSeason(CreativeWork, CreativeWorkSeason):
    term = RdfTerm('TVSeason', 'http://schema.org/TVSeason', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PodcastSeason(CreativeWorkSeason):
    term = RdfTerm('PodcastSeason', 'http://schema.org/PodcastSeason', ['1.0', '1.1', '1.2-DRAFT'])

class RadioSeason(CreativeWorkSeason):
    term = RdfTerm('RadioSeason', 'http://schema.org/RadioSeason', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Car(Vehicle):
    term = RdfTerm('Car', 'http://schema.org/Car', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Motorcycle(Vehicle):
    term = RdfTerm('Motorcycle', 'http://schema.org/Motorcycle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MotorizedBicycle(Vehicle):
    term = RdfTerm('MotorizedBicycle', 'http://schema.org/MotorizedBicycle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BusOrCoach(Vehicle):
    term = RdfTerm('BusOrCoach', 'http://schema.org/BusOrCoach', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Duration(Quantity):
    term = RdfTerm('Duration', 'http://schema.org/Duration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Mass(Quantity):
    term = RdfTerm('Mass', 'http://schema.org/Mass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Distance(Quantity):
    term = RdfTerm('Distance', 'http://schema.org/Distance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Energy(Quantity):
    term = RdfTerm('Energy', 'http://schema.org/Energy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EventAttendanceModeEnumeration(Enumeration):
    term = RdfTerm('EventAttendanceModeEnumeration', 'http://schema.org/EventAttendanceModeEnumeration', ['1.1', '1.2-DRAFT'])

class ReturnFeesEnumeration(Enumeration):
    term = RdfTerm('ReturnFeesEnumeration', 'http://schema.org/ReturnFeesEnumeration', ['1.0', '1.1', '1.2-DRAFT'])

class SizeGroupEnumeration(Enumeration):
    term = RdfTerm('SizeGroupEnumeration', 'http://schema.org/SizeGroupEnumeration', ['1.2-DRAFT'])

class NonprofitType(Enumeration):
    term = RdfTerm('NonprofitType', 'http://schema.org/NonprofitType', ['1.1', '1.2-DRAFT'])

class MeasurementTypeEnumeration(Enumeration):
    term = RdfTerm('MeasurementTypeEnumeration', 'http://schema.org/MeasurementTypeEnumeration', ['1.2-DRAFT'])

class SizeSystemEnumeration(Enumeration):
    term = RdfTerm('SizeSystemEnumeration', 'http://schema.org/SizeSystemEnumeration', ['1.2-DRAFT'])

class EnergyEfficiencyEnumeration(Enumeration):
    term = RdfTerm('EnergyEfficiencyEnumeration', 'http://schema.org/EnergyEfficiencyEnumeration', ['1.1', '1.2-DRAFT'])

class MediaEnumeration(Enumeration):
    term = RdfTerm('MediaEnumeration', 'http://schema.org/MediaEnumeration', [])

class MeasurementMethodEnum(Enumeration):
    term = RdfTerm('MeasurementMethodEnum', 'http://schema.org/MeasurementMethodEnum', ['1.2-DRAFT'])

class IncentiveStatus(Enumeration):
    term = RdfTerm('IncentiveStatus', 'http://schema.org/IncentiveStatus', [])

class MediaManipulationRatingEnumeration(Enumeration):
    term = RdfTerm('MediaManipulationRatingEnumeration', 'http://schema.org/MediaManipulationRatingEnumeration', ['1.1', '1.2-DRAFT'])

class StatusEnumeration(Enumeration):
    term = RdfTerm('StatusEnumeration', 'http://schema.org/StatusEnumeration', ['1.1', '1.2-DRAFT'])

class MapCategoryType(Enumeration):
    term = RdfTerm('MapCategoryType', 'http://schema.org/MapCategoryType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalEnumeration(Enumeration):
    term = RdfTerm('MedicalEnumeration', 'http://schema.org/MedicalEnumeration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FulfillmentTypeEnumeration(Enumeration):
    term = RdfTerm('FulfillmentTypeEnumeration', 'http://schema.org/FulfillmentTypeEnumeration', [])

class MusicReleaseFormatType(Enumeration):
    term = RdfTerm('MusicReleaseFormatType', 'http://schema.org/MusicReleaseFormatType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BoardingPolicyType(Enumeration):
    term = RdfTerm('BoardingPolicyType', 'http://schema.org/BoardingPolicyType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GovernmentBenefitsType(Enumeration):
    term = RdfTerm('GovernmentBenefitsType', 'http://schema.org/GovernmentBenefitsType', ['1.1', '1.2-DRAFT'])

class GenderType(Enumeration):
    term = RdfTerm('GenderType', 'http://schema.org/GenderType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LegalValueLevel(Enumeration):
    term = RdfTerm('LegalValueLevel', 'http://schema.org/LegalValueLevel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ItemListOrderType(Enumeration):
    term = RdfTerm('ItemListOrderType', 'http://schema.org/ItemListOrderType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class QualitativeValue(Enumeration):
    term = RdfTerm('QualitativeValue', 'http://schema.org/QualitativeValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PriceTypeEnumeration(Enumeration):
    term = RdfTerm('PriceTypeEnumeration', 'http://schema.org/PriceTypeEnumeration', ['1.2-DRAFT'])

class GamePlayMode(Enumeration):
    term = RdfTerm('GamePlayMode', 'http://schema.org/GamePlayMode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PhysicalActivityCategory(Enumeration):
    term = RdfTerm('PhysicalActivityCategory', 'http://schema.org/PhysicalActivityCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Specialty(Enumeration):
    term = RdfTerm('Specialty', 'http://schema.org/Specialty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicAlbumProductionType(Enumeration):
    term = RdfTerm('MusicAlbumProductionType', 'http://schema.org/MusicAlbumProductionType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class IncentiveQualifiedExpenseType(Enumeration):
    term = RdfTerm('IncentiveQualifiedExpenseType', 'http://schema.org/IncentiveQualifiedExpenseType', [])

class OfferItemCondition(Enumeration):
    term = RdfTerm('OfferItemCondition', 'http://schema.org/OfferItemCondition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RsvpResponseType(Enumeration):
    term = RdfTerm('RsvpResponseType', 'http://schema.org/RsvpResponseType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ProductReturnEnumeration(Enumeration):
    term = RdfTerm('ProductReturnEnumeration', 'http://schema.org/ProductReturnEnumeration', ['1.0', '1.1', '1.2-DRAFT'])

class MusicAlbumReleaseType(Enumeration):
    term = RdfTerm('MusicAlbumReleaseType', 'http://schema.org/MusicAlbumReleaseType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReturnLabelSourceEnumeration(Enumeration):
    term = RdfTerm('ReturnLabelSourceEnumeration', 'http://schema.org/ReturnLabelSourceEnumeration', ['1.2-DRAFT'])

class RestrictedDiet(Enumeration):
    term = RdfTerm('RestrictedDiet', 'http://schema.org/RestrictedDiet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class IncentiveType(Enumeration):
    term = RdfTerm('IncentiveType', 'http://schema.org/IncentiveType', [])

class TierBenefitEnumeration(Enumeration):
    term = RdfTerm('TierBenefitEnumeration', 'http://schema.org/TierBenefitEnumeration', [])

class HealthAspectEnumeration(Enumeration):
    term = RdfTerm('HealthAspectEnumeration', 'http://schema.org/HealthAspectEnumeration', ['1.0', '1.1', '1.2-DRAFT'])

class BusinessFunction(Enumeration):
    term = RdfTerm('BusinessFunction', 'http://schema.org/BusinessFunction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CertificationStatusEnumeration(Enumeration):
    term = RdfTerm('CertificationStatusEnumeration', 'http://schema.org/CertificationStatusEnumeration', [])

class AdultOrientedEnumeration(Enumeration):
    term = RdfTerm('AdultOrientedEnumeration', 'http://schema.org/AdultOrientedEnumeration', ['1.2-DRAFT'])

class CarUsageType(Enumeration):
    term = RdfTerm('CarUsageType', 'http://schema.org/CarUsageType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DeliveryMethod(Enumeration):
    term = RdfTerm('DeliveryMethod', 'http://schema.org/DeliveryMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DayOfWeek(Enumeration):
    term = RdfTerm('DayOfWeek', 'http://schema.org/DayOfWeek', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReturnMethodEnumeration(Enumeration):
    term = RdfTerm('ReturnMethodEnumeration', 'http://schema.org/ReturnMethodEnumeration', ['1.2-DRAFT'])

class MerchantReturnEnumeration(Enumeration):
    term = RdfTerm('MerchantReturnEnumeration', 'http://schema.org/MerchantReturnEnumeration', ['1.1', '1.2-DRAFT'])

class WarrantyScope(Enumeration):
    term = RdfTerm('WarrantyScope', 'http://schema.org/WarrantyScope', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ItemAvailability(Enumeration):
    term = RdfTerm('ItemAvailability', 'http://schema.org/ItemAvailability', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RefundTypeEnumeration(Enumeration):
    term = RdfTerm('RefundTypeEnumeration', 'http://schema.org/RefundTypeEnumeration', ['1.0', '1.1', '1.2-DRAFT'])

class DigitalDocumentPermissionType(Enumeration):
    term = RdfTerm('DigitalDocumentPermissionType', 'http://schema.org/DigitalDocumentPermissionType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BusinessEntityType(Enumeration):
    term = RdfTerm('BusinessEntityType', 'http://schema.org/BusinessEntityType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BookFormatType(Enumeration):
    term = RdfTerm('BookFormatType', 'http://schema.org/BookFormatType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GameAvailabilityEnumeration(Enumeration):
    term = RdfTerm('GameAvailabilityEnumeration', 'http://schema.org/GameAvailabilityEnumeration', ['1.2-DRAFT'])

class DigitalPlatformEnumeration(Enumeration):
    term = RdfTerm('DigitalPlatformEnumeration', 'http://schema.org/DigitalPlatformEnumeration', ['1.2-DRAFT'])

class PriceComponentTypeEnumeration(Enumeration):
    term = RdfTerm('PriceComponentTypeEnumeration', 'http://schema.org/PriceComponentTypeEnumeration', ['1.2-DRAFT'])

class PaymentMethodType(Enumeration):
    term = RdfTerm('PaymentMethodType', 'http://schema.org/PaymentMethodType', [])

class ContactPointOption(Enumeration):
    term = RdfTerm('ContactPointOption', 'http://schema.org/ContactPointOption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PurchaseType(Enumeration):
    term = RdfTerm('PurchaseType', 'http://schema.org/PurchaseType', [])

class LinkRole(Role):
    term = RdfTerm('LinkRole', 'http://schema.org/LinkRole', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OrganizationRole(Role):
    term = RdfTerm('OrganizationRole', 'http://schema.org/OrganizationRole', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PerformanceRole(Role):
    term = RdfTerm('PerformanceRole', 'http://schema.org/PerformanceRole', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GovernmentPermit(Permit):
    term = RdfTerm('GovernmentPermit', 'http://schema.org/GovernmentPermit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EventReservation(Reservation):
    term = RdfTerm('EventReservation', 'http://schema.org/EventReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TaxiReservation(Reservation):
    term = RdfTerm('TaxiReservation', 'http://schema.org/TaxiReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReservationPackage(Reservation):
    term = RdfTerm('ReservationPackage', 'http://schema.org/ReservationPackage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RentalCarReservation(Reservation):
    term = RdfTerm('RentalCarReservation', 'http://schema.org/RentalCarReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LodgingReservation(Reservation):
    term = RdfTerm('LodgingReservation', 'http://schema.org/LodgingReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FlightReservation(Reservation):
    term = RdfTerm('FlightReservation', 'http://schema.org/FlightReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BusReservation(Reservation):
    term = RdfTerm('BusReservation', 'http://schema.org/BusReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FoodEstablishmentReservation(Reservation):
    term = RdfTerm('FoodEstablishmentReservation', 'http://schema.org/FoodEstablishmentReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BoatReservation(Reservation):
    term = RdfTerm('BoatReservation', 'http://schema.org/BoatReservation', ['1.1', '1.2-DRAFT'])

class TrainReservation(Reservation):
    term = RdfTerm('TrainReservation', 'http://schema.org/TrainReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowToItem(ListItem):
    term = RdfTerm('HowToItem', 'http://schema.org/HowToItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowToDirection(ListItem, CreativeWork):
    term = RdfTerm('HowToDirection', 'http://schema.org/HowToDirection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowToTip(ListItem, CreativeWork):
    term = RdfTerm('HowToTip', 'http://schema.org/HowToTip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BusinessAudience(Audience):
    term = RdfTerm('BusinessAudience', 'http://schema.org/BusinessAudience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EducationalAudience(Audience):
    term = RdfTerm('EducationalAudience', 'http://schema.org/EducationalAudience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Researcher(Audience):
    term = RdfTerm('Researcher', 'http://schema.org/Researcher', ['1.0', '1.1', '1.2-DRAFT'])

class PeopleAudience(Audience):
    term = RdfTerm('PeopleAudience', 'http://schema.org/PeopleAudience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class StatisticalVariable(ConstraintNode):
    term = RdfTerm('StatisticalVariable', 'http://schema.org/StatisticalVariable', ['1.2-DRAFT'])

class AggregateOffer(Offer):
    term = RdfTerm('AggregateOffer', 'http://schema.org/AggregateOffer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OfferForLease(Offer):
    term = RdfTerm('OfferForLease', 'http://schema.org/OfferForLease', ['1.0', '1.1', '1.2-DRAFT'])

class OfferForPurchase(Offer):
    term = RdfTerm('OfferForPurchase', 'http://schema.org/OfferForPurchase', ['1.0', '1.1', '1.2-DRAFT'])

class EventSeries(Event, Series):
    term = RdfTerm('EventSeries', 'http://schema.org/EventSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CreativeWorkSeries(Series, CreativeWork):
    term = RdfTerm('CreativeWorkSeries', 'http://schema.org/CreativeWorkSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WorkBasedProgram(EducationalOccupationalProgram):
    term = RdfTerm('WorkBasedProgram', 'http://schema.org/WorkBasedProgram', ['1.0', '1.1', '1.2-DRAFT'])

class TelevisionChannel(BroadcastChannel):
    term = RdfTerm('TelevisionChannel', 'http://schema.org/TelevisionChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RadioChannel(BroadcastChannel):
    term = RdfTerm('RadioChannel', 'http://schema.org/RadioChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TrainTrip(Trip):
    term = RdfTerm('TrainTrip', 'http://schema.org/TrainTrip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BoatTrip(Trip):
    term = RdfTerm('BoatTrip', 'http://schema.org/BoatTrip', ['1.1', '1.2-DRAFT'])

class BusTrip(Trip):
    term = RdfTerm('BusTrip', 'http://schema.org/BusTrip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Flight(Trip):
    term = RdfTerm('Flight', 'http://schema.org/Flight', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TouristTrip(Trip):
    term = RdfTerm('TouristTrip', 'http://schema.org/TouristTrip', ['1.0', '1.1', '1.2-DRAFT'])

class MonetaryGrant(Grant):
    term = RdfTerm('MonetaryGrant', 'http://schema.org/MonetaryGrant', ['1.0', '1.1', '1.2-DRAFT'])

class BroadcastService(Service):
    term = RdfTerm('BroadcastService', 'http://schema.org/BroadcastService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FoodService(Service):
    term = RdfTerm('FoodService', 'http://schema.org/FoodService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GovernmentService(Service):
    term = RdfTerm('GovernmentService', 'http://schema.org/GovernmentService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Taxi(Service):
    term = RdfTerm('Taxi', 'http://schema.org/Taxi', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FinancialProduct(Service):
    term = RdfTerm('FinancialProduct', 'http://schema.org/FinancialProduct', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WebAPI(Service):
    term = RdfTerm('WebAPI', 'http://schema.org/WebAPI', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CableOrSatelliteService(Service):
    term = RdfTerm('CableOrSatelliteService', 'http://schema.org/CableOrSatelliteService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TaxiService(Service):
    term = RdfTerm('TaxiService', 'http://schema.org/TaxiService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowToSection(ItemList, ListItem, CreativeWork):
    term = RdfTerm('HowToSection', 'http://schema.org/HowToSection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowToStep(ItemList, ListItem, CreativeWork):
    term = RdfTerm('HowToStep', 'http://schema.org/HowToStep', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BreadcrumbList(ItemList):
    term = RdfTerm('BreadcrumbList', 'http://schema.org/BreadcrumbList', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OfferCatalog(ItemList):
    term = RdfTerm('OfferCatalog', 'http://schema.org/OfferCatalog', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DefinedRegion(StructuredValue):
    term = RdfTerm('DefinedRegion', 'http://schema.org/DefinedRegion', ['1.1', '1.2-DRAFT'])

class ShippingDeliveryTime(StructuredValue):
    term = RdfTerm('ShippingDeliveryTime', 'http://schema.org/ShippingDeliveryTime', ['1.1', '1.2-DRAFT'])

class RepaymentSpecification(StructuredValue):
    term = RdfTerm('RepaymentSpecification', 'http://schema.org/RepaymentSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PostalCodeRangeSpecification(StructuredValue):
    term = RdfTerm('PostalCodeRangeSpecification', 'http://schema.org/PostalCodeRangeSpecification', ['1.1', '1.2-DRAFT'])

class ExchangeRateSpecification(StructuredValue):
    term = RdfTerm('ExchangeRateSpecification', 'http://schema.org/ExchangeRateSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GeoShape(StructuredValue):
    term = RdfTerm('GeoShape', 'http://schema.org/GeoShape', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OfferShippingDetails(StructuredValue):
    term = RdfTerm('OfferShippingDetails', 'http://schema.org/OfferShippingDetails', ['1.1', '1.2-DRAFT'])

class QuantitativeValueDistribution(StructuredValue):
    term = RdfTerm('QuantitativeValueDistribution', 'http://schema.org/QuantitativeValueDistribution', ['1.0', '1.1', '1.2-DRAFT'])

class CDCPMDRecord(StructuredValue):
    term = RdfTerm('CDCPMDRecord', 'http://schema.org/CDCPMDRecord', ['1.1', '1.2-DRAFT'])

class EngineSpecification(StructuredValue):
    term = RdfTerm('EngineSpecification', 'http://schema.org/EngineSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PropertyValue(StructuredValue):
    term = RdfTerm('PropertyValue', 'http://schema.org/PropertyValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ShippingConditions(StructuredValue):
    term = RdfTerm('ShippingConditions', 'http://schema.org/ShippingConditions', [])

class DatedMoneySpecification(StructuredValue):
    term = RdfTerm('DatedMoneySpecification', 'http://schema.org/DatedMoneySpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class QuantitativeValue(StructuredValue):
    term = RdfTerm('QuantitativeValue', 'http://schema.org/QuantitativeValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MonetaryAmount(StructuredValue):
    term = RdfTerm('MonetaryAmount', 'http://schema.org/MonetaryAmount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InteractionCounter(StructuredValue):
    term = RdfTerm('InteractionCounter', 'http://schema.org/InteractionCounter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WarrantyPromise(StructuredValue):
    term = RdfTerm('WarrantyPromise', 'http://schema.org/WarrantyPromise', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ContactPoint(StructuredValue):
    term = RdfTerm('ContactPoint', 'http://schema.org/ContactPoint', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GeoCoordinates(StructuredValue):
    term = RdfTerm('GeoCoordinates', 'http://schema.org/GeoCoordinates', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OwnershipInfo(StructuredValue):
    term = RdfTerm('OwnershipInfo', 'http://schema.org/OwnershipInfo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PriceSpecification(StructuredValue):
    term = RdfTerm('PriceSpecification', 'http://schema.org/PriceSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ShippingRateSettings(StructuredValue):
    term = RdfTerm('ShippingRateSettings', 'http://schema.org/ShippingRateSettings', ['1.1', '1.2-DRAFT'])

class ServicePeriod(StructuredValue):
    term = RdfTerm('ServicePeriod', 'http://schema.org/ServicePeriod', [])

class NutritionInformation(StructuredValue):
    term = RdfTerm('NutritionInformation', 'http://schema.org/NutritionInformation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DeliveryTimeSettings(StructuredValue):
    term = RdfTerm('DeliveryTimeSettings', 'http://schema.org/DeliveryTimeSettings', ['1.1', '1.2-DRAFT'])

class TypeAndQuantityNode(StructuredValue):
    term = RdfTerm('TypeAndQuantityNode', 'http://schema.org/TypeAndQuantityNode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ShippingService(StructuredValue):
    term = RdfTerm('ShippingService', 'http://schema.org/ShippingService', [])

class OpeningHoursSpecification(StructuredValue):
    term = RdfTerm('OpeningHoursSpecification', 'http://schema.org/OpeningHoursSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CategoryCode(DefinedTerm):
    term = RdfTerm('CategoryCode', 'http://schema.org/CategoryCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AggregateRating(Rating):
    term = RdfTerm('AggregateRating', 'http://schema.org/AggregateRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EndorsementRating(Rating):
    term = RdfTerm('EndorsementRating', 'http://schema.org/EndorsementRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ApartmentComplex(Residence):
    term = RdfTerm('ApartmentComplex', 'http://schema.org/ApartmentComplex', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GatedResidenceCommunity(Residence):
    term = RdfTerm('GatedResidenceCommunity', 'http://schema.org/GatedResidenceCommunity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CampingPitch(Accommodation):
    term = RdfTerm('CampingPitch', 'http://schema.org/CampingPitch', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Suite(Accommodation):
    term = RdfTerm('Suite', 'http://schema.org/Suite', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class House(Accommodation):
    term = RdfTerm('House', 'http://schema.org/House', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Apartment(Accommodation):
    term = RdfTerm('Apartment', 'http://schema.org/Apartment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Room(Accommodation):
    term = RdfTerm('Room', 'http://schema.org/Room', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SchoolDistrict(AdministrativeArea):
    term = RdfTerm('SchoolDistrict', 'http://schema.org/SchoolDistrict', ['1.1', '1.2-DRAFT'])

class Country(AdministrativeArea):
    term = RdfTerm('Country', 'http://schema.org/Country', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class City(AdministrativeArea):
    term = RdfTerm('City', 'http://schema.org/City', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class State(AdministrativeArea):
    term = RdfTerm('State', 'http://schema.org/State', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Bridge(CivicStructure):
    term = RdfTerm('Bridge', 'http://schema.org/Bridge', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PublicToilet(CivicStructure):
    term = RdfTerm('PublicToilet', 'http://schema.org/PublicToilet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Playground(CivicStructure):
    term = RdfTerm('Playground', 'http://schema.org/Playground', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PlaceOfWorship(CivicStructure):
    term = RdfTerm('PlaceOfWorship', 'http://schema.org/PlaceOfWorship', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Zoo(CivicStructure):
    term = RdfTerm('Zoo', 'http://schema.org/Zoo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Beach(CivicStructure):
    term = RdfTerm('Beach', 'http://schema.org/Beach', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EducationalOrganization(CivicStructure, Organization):
    term = RdfTerm('EducationalOrganization', 'http://schema.org/EducationalOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RVPark(CivicStructure):
    term = RdfTerm('RVPark', 'http://schema.org/RVPark', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Airport(CivicStructure):
    term = RdfTerm('Airport', 'http://schema.org/Airport', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ParkingFacility(CivicStructure):
    term = RdfTerm('ParkingFacility', 'http://schema.org/ParkingFacility', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TrainStation(CivicStructure):
    term = RdfTerm('TrainStation', 'http://schema.org/TrainStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Park(CivicStructure):
    term = RdfTerm('Park', 'http://schema.org/Park', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicVenue(CivicStructure):
    term = RdfTerm('MusicVenue', 'http://schema.org/MusicVenue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SubwayStation(CivicStructure):
    term = RdfTerm('SubwayStation', 'http://schema.org/SubwayStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Aquarium(CivicStructure):
    term = RdfTerm('Aquarium', 'http://schema.org/Aquarium', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Crematorium(CivicStructure):
    term = RdfTerm('Crematorium', 'http://schema.org/Crematorium', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Museum(CivicStructure):
    term = RdfTerm('Museum', 'http://schema.org/Museum', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GovernmentBuilding(CivicStructure):
    term = RdfTerm('GovernmentBuilding', 'http://schema.org/GovernmentBuilding', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EventVenue(CivicStructure):
    term = RdfTerm('EventVenue', 'http://schema.org/EventVenue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BusStation(CivicStructure):
    term = RdfTerm('BusStation', 'http://schema.org/BusStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BusStop(CivicStructure):
    term = RdfTerm('BusStop', 'http://schema.org/BusStop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Cemetery(CivicStructure):
    term = RdfTerm('Cemetery', 'http://schema.org/Cemetery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BoatTerminal(CivicStructure):
    term = RdfTerm('BoatTerminal', 'http://schema.org/BoatTerminal', ['1.1', '1.2-DRAFT'])

class PerformingArtsTheater(CivicStructure):
    term = RdfTerm('PerformingArtsTheater', 'http://schema.org/PerformingArtsTheater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TaxiStand(CivicStructure):
    term = RdfTerm('TaxiStand', 'http://schema.org/TaxiStand', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Continent(Landform):
    term = RdfTerm('Continent', 'http://schema.org/Continent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Mountain(Landform):
    term = RdfTerm('Mountain', 'http://schema.org/Mountain', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Volcano(Landform):
    term = RdfTerm('Volcano', 'http://schema.org/Volcano', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BodyOfWater(Landform):
    term = RdfTerm('BodyOfWater', 'http://schema.org/BodyOfWater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FundingAgency(Project):
    term = RdfTerm('FundingAgency', 'http://schema.org/FundingAgency', ['1.0', '1.1', '1.2-DRAFT'])

class ResearchProject(Project):
    term = RdfTerm('ResearchProject', 'http://schema.org/ResearchProject', ['1.0', '1.1', '1.2-DRAFT'])

class VeterinaryCare(MedicalOrganization):
    term = RdfTerm('VeterinaryCare', 'http://schema.org/VeterinaryCare', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DiagnosticLab(MedicalOrganization):
    term = RdfTerm('DiagnosticLab', 'http://schema.org/DiagnosticLab', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LodgingBusiness(LocalBusiness):
    term = RdfTerm('LodgingBusiness', 'http://schema.org/LodgingBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EmergencyService(LocalBusiness):
    term = RdfTerm('EmergencyService', 'http://schema.org/EmergencyService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DryCleaningOrLaundry(LocalBusiness):
    term = RdfTerm('DryCleaningOrLaundry', 'http://schema.org/DryCleaningOrLaundry', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ArchiveOrganization(LocalBusiness):
    term = RdfTerm('ArchiveOrganization', 'http://schema.org/ArchiveOrganization', ['1.0', '1.1', '1.2-DRAFT'])

class MedicalBusiness(LocalBusiness):
    term = RdfTerm('MedicalBusiness', 'http://schema.org/MedicalBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Library(LocalBusiness):
    term = RdfTerm('Library', 'http://schema.org/Library', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EmploymentAgency(LocalBusiness):
    term = RdfTerm('EmploymentAgency', 'http://schema.org/EmploymentAgency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InternetCafe(LocalBusiness):
    term = RdfTerm('InternetCafe', 'http://schema.org/InternetCafe', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FoodEstablishment(LocalBusiness):
    term = RdfTerm('FoodEstablishment', 'http://schema.org/FoodEstablishment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TouristInformationCenter(LocalBusiness):
    term = RdfTerm('TouristInformationCenter', 'http://schema.org/TouristInformationCenter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutomotiveBusiness(LocalBusiness):
    term = RdfTerm('AutomotiveBusiness', 'http://schema.org/AutomotiveBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RealEstateAgent(LocalBusiness):
    term = RdfTerm('RealEstateAgent', 'http://schema.org/RealEstateAgent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SelfStorage(LocalBusiness):
    term = RdfTerm('SelfStorage', 'http://schema.org/SelfStorage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TravelAgency(LocalBusiness):
    term = RdfTerm('TravelAgency', 'http://schema.org/TravelAgency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ShoppingCenter(LocalBusiness):
    term = RdfTerm('ShoppingCenter', 'http://schema.org/ShoppingCenter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HealthAndBeautyBusiness(LocalBusiness):
    term = RdfTerm('HealthAndBeautyBusiness', 'http://schema.org/HealthAndBeautyBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LegalService(LocalBusiness):
    term = RdfTerm('LegalService', 'http://schema.org/LegalService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Store(LocalBusiness):
    term = RdfTerm('Store', 'http://schema.org/Store', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SportsActivityLocation(LocalBusiness):
    term = RdfTerm('SportsActivityLocation', 'http://schema.org/SportsActivityLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AnimalShelter(LocalBusiness):
    term = RdfTerm('AnimalShelter', 'http://schema.org/AnimalShelter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TelevisionStation(LocalBusiness):
    term = RdfTerm('TelevisionStation', 'http://schema.org/TelevisionStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RadioStation(LocalBusiness):
    term = RdfTerm('RadioStation', 'http://schema.org/RadioStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ChildCare(LocalBusiness):
    term = RdfTerm('ChildCare', 'http://schema.org/ChildCare', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RecyclingCenter(LocalBusiness):
    term = RdfTerm('RecyclingCenter', 'http://schema.org/RecyclingCenter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GovernmentOffice(LocalBusiness):
    term = RdfTerm('GovernmentOffice', 'http://schema.org/GovernmentOffice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ProfessionalService(LocalBusiness):
    term = RdfTerm('ProfessionalService', 'http://schema.org/ProfessionalService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FinancialService(LocalBusiness):
    term = RdfTerm('FinancialService', 'http://schema.org/FinancialService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HomeAndConstructionBusiness(LocalBusiness):
    term = RdfTerm('HomeAndConstructionBusiness', 'http://schema.org/HomeAndConstructionBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EntertainmentBusiness(LocalBusiness):
    term = RdfTerm('EntertainmentBusiness', 'http://schema.org/EntertainmentBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SportsTeam(SportsOrganization):
    term = RdfTerm('SportsTeam', 'http://schema.org/SportsTeam', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TheaterGroup(PerformingGroup):
    term = RdfTerm('TheaterGroup', 'http://schema.org/TheaterGroup', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DanceGroup(PerformingGroup):
    term = RdfTerm('DanceGroup', 'http://schema.org/DanceGroup', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicGroup(PerformingGroup):
    term = RdfTerm('MusicGroup', 'http://schema.org/MusicGroup', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OnlineStore(OnlineBusiness):
    term = RdfTerm('OnlineStore', 'http://schema.org/OnlineStore', ['1.2-DRAFT'])

class AgreeAction(ReactAction):
    term = RdfTerm('AgreeAction', 'http://schema.org/AgreeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WantAction(ReactAction):
    term = RdfTerm('WantAction', 'http://schema.org/WantAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EndorseAction(ReactAction):
    term = RdfTerm('EndorseAction', 'http://schema.org/EndorseAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LikeAction(ReactAction):
    term = RdfTerm('LikeAction', 'http://schema.org/LikeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DisagreeAction(ReactAction):
    term = RdfTerm('DisagreeAction', 'http://schema.org/DisagreeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DislikeAction(ReactAction):
    term = RdfTerm('DislikeAction', 'http://schema.org/DislikeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VoteAction(ChooseAction):
    term = RdfTerm('VoteAction', 'http://schema.org/VoteAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WearAction(UseAction):
    term = RdfTerm('WearAction', 'http://schema.org/WearAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AssignAction(AllocateAction):
    term = RdfTerm('AssignAction', 'http://schema.org/AssignAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AcceptAction(AllocateAction):
    term = RdfTerm('AcceptAction', 'http://schema.org/AcceptAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RejectAction(AllocateAction):
    term = RdfTerm('RejectAction', 'http://schema.org/RejectAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AuthorizeAction(AllocateAction):
    term = RdfTerm('AuthorizeAction', 'http://schema.org/AuthorizeAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ScheduleAction(PlanAction):
    term = RdfTerm('ScheduleAction', 'http://schema.org/ScheduleAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CancelAction(PlanAction):
    term = RdfTerm('CancelAction', 'http://schema.org/CancelAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReserveAction(PlanAction):
    term = RdfTerm('ReserveAction', 'http://schema.org/ReserveAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InsertAction(AddAction):
    term = RdfTerm('InsertAction', 'http://schema.org/InsertAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReplyAction(CommunicateAction):
    term = RdfTerm('ReplyAction', 'http://schema.org/ReplyAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AskAction(CommunicateAction):
    term = RdfTerm('AskAction', 'http://schema.org/AskAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ShareAction(CommunicateAction):
    term = RdfTerm('ShareAction', 'http://schema.org/ShareAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InviteAction(CommunicateAction):
    term = RdfTerm('InviteAction', 'http://schema.org/InviteAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CheckInAction(CommunicateAction):
    term = RdfTerm('CheckInAction', 'http://schema.org/CheckInAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InformAction(CommunicateAction):
    term = RdfTerm('InformAction', 'http://schema.org/InformAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CheckOutAction(CommunicateAction):
    term = RdfTerm('CheckOutAction', 'http://schema.org/CheckOutAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CommentAction(CommunicateAction):
    term = RdfTerm('CommentAction', 'http://schema.org/CommentAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PsychologicalTreatment(TherapeuticProcedure):
    term = RdfTerm('PsychologicalTreatment', 'http://schema.org/PsychologicalTreatment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalTherapy(TherapeuticProcedure):
    term = RdfTerm('MedicalTherapy', 'http://schema.org/MedicalTherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RecommendedDoseSchedule(DoseSchedule):
    term = RdfTerm('RecommendedDoseSchedule', 'http://schema.org/RecommendedDoseSchedule', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MaximumDoseSchedule(DoseSchedule):
    term = RdfTerm('MaximumDoseSchedule', 'http://schema.org/MaximumDoseSchedule', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReportedDoseSchedule(DoseSchedule):
    term = RdfTerm('ReportedDoseSchedule', 'http://schema.org/ReportedDoseSchedule', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalSymptom(MedicalSignOrSymptom):
    term = RdfTerm('MedicalSymptom', 'http://schema.org/MedicalSymptom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalSign(MedicalSignOrSymptom):
    term = RdfTerm('MedicalSign', 'http://schema.org/MedicalSign', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Vein(Vessel):
    term = RdfTerm('Vein', 'http://schema.org/Vein', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Artery(Vessel):
    term = RdfTerm('Artery', 'http://schema.org/Artery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LymphaticVessel(Vessel):
    term = RdfTerm('LymphaticVessel', 'http://schema.org/LymphaticVessel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ExercisePlan(CreativeWork, PhysicalActivity):
    term = RdfTerm('ExercisePlan', 'http://schema.org/ExercisePlan', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CompleteDataFeed(DataFeed):
    term = RdfTerm('CompleteDataFeed', 'http://schema.org/CompleteDataFeed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class APIReference(TechArticle):
    term = RdfTerm('APIReference', 'http://schema.org/APIReference', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalScholarlyArticle(ScholarlyArticle):
    term = RdfTerm('MedicalScholarlyArticle', 'http://schema.org/MedicalScholarlyArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BlogPosting(SocialMediaPosting):
    term = RdfTerm('BlogPosting', 'http://schema.org/BlogPosting', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DiscussionForumPosting(SocialMediaPosting):
    term = RdfTerm('DiscussionForumPosting', 'http://schema.org/DiscussionForumPosting', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BackgroundNewsArticle(NewsArticle):
    term = RdfTerm('BackgroundNewsArticle', 'http://schema.org/BackgroundNewsArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AnalysisNewsArticle(NewsArticle):
    term = RdfTerm('AnalysisNewsArticle', 'http://schema.org/AnalysisNewsArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReportageNewsArticle(NewsArticle):
    term = RdfTerm('ReportageNewsArticle', 'http://schema.org/ReportageNewsArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AskPublicNewsArticle(NewsArticle):
    term = RdfTerm('AskPublicNewsArticle', 'http://schema.org/AskPublicNewsArticle', ['1.0', '1.1', '1.2-DRAFT'])

class OpinionNewsArticle(NewsArticle):
    term = RdfTerm('OpinionNewsArticle', 'http://schema.org/OpinionNewsArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VideoObjectSnapshot(VideoObject):
    term = RdfTerm('VideoObjectSnapshot', 'http://schema.org/VideoObjectSnapshot', ['1.2-DRAFT'])

class AudioObjectSnapshot(AudioObject):
    term = RdfTerm('AudioObjectSnapshot', 'http://schema.org/AudioObjectSnapshot', ['1.2-DRAFT'])

class Audiobook(AudioObject, Book):
    term = RdfTerm('Audiobook', 'http://schema.org/Audiobook', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ImageObjectSnapshot(ImageObject):
    term = RdfTerm('ImageObjectSnapshot', 'http://schema.org/ImageObjectSnapshot', ['1.2-DRAFT'])

class Barcode(ImageObject):
    term = RdfTerm('Barcode', 'http://schema.org/Barcode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComicCoverArt(ComicStory, CoverArt):
    term = RdfTerm('ComicCoverArt', 'http://schema.org/ComicCoverArt', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MediaGallery(CollectionPage):
    term = RdfTerm('MediaGallery', 'http://schema.org/MediaGallery', ['1.1', '1.2-DRAFT'])

class ReviewNewsArticle(CriticReview, NewsArticle):
    term = RdfTerm('ReviewNewsArticle', 'http://schema.org/ReviewNewsArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    term = RdfTerm('WearableSizeGroupEnumeration', 'http://schema.org/WearableSizeGroupEnumeration', ['1.2-DRAFT'])

class USNonprofitType(NonprofitType):
    term = RdfTerm('USNonprofitType', 'http://schema.org/USNonprofitType', ['1.1', '1.2-DRAFT'])

class UKNonprofitType(NonprofitType):
    term = RdfTerm('UKNonprofitType', 'http://schema.org/UKNonprofitType', ['1.1', '1.2-DRAFT'])

class NLNonprofitType(NonprofitType):
    term = RdfTerm('NLNonprofitType', 'http://schema.org/NLNonprofitType', ['1.1', '1.2-DRAFT'])

class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm('WearableMeasurementTypeEnumeration', 'http://schema.org/WearableMeasurementTypeEnumeration', ['1.2-DRAFT'])

class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm('BodyMeasurementTypeEnumeration', 'http://schema.org/BodyMeasurementTypeEnumeration', ['1.2-DRAFT'])

class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    term = RdfTerm('WearableSizeSystemEnumeration', 'http://schema.org/WearableSizeSystemEnumeration', ['1.2-DRAFT'])

class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm('EnergyStarEnergyEfficiencyEnumeration', 'http://schema.org/EnergyStarEnergyEfficiencyEnumeration', ['1.1', '1.2-DRAFT'])

class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm('EUEnergyEfficiencyEnumeration', 'http://schema.org/EUEnergyEfficiencyEnumeration', ['1.1', '1.2-DRAFT'])

class IPTCDigitalSourceEnumeration(MediaEnumeration):
    term = RdfTerm('IPTCDigitalSourceEnumeration', 'http://schema.org/IPTCDigitalSourceEnumeration', [])

class PaymentStatusType(StatusEnumeration):
    term = RdfTerm('PaymentStatusType', 'http://schema.org/PaymentStatusType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OrderStatus(StatusEnumeration):
    term = RdfTerm('OrderStatus', 'http://schema.org/OrderStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EventStatusType(StatusEnumeration):
    term = RdfTerm('EventStatusType', 'http://schema.org/EventStatusType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ReservationStatusType(StatusEnumeration):
    term = RdfTerm('ReservationStatusType', 'http://schema.org/ReservationStatusType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LegalForceStatus(StatusEnumeration):
    term = RdfTerm('LegalForceStatus', 'http://schema.org/LegalForceStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ActionStatusType(StatusEnumeration):
    term = RdfTerm('ActionStatusType', 'http://schema.org/ActionStatusType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GameServerStatus(StatusEnumeration):
    term = RdfTerm('GameServerStatus', 'http://schema.org/GameServerStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalImagingTechnique(MedicalEnumeration):
    term = RdfTerm('MedicalImagingTechnique', 'http://schema.org/MedicalImagingTechnique', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrugCostCategory(MedicalEnumeration):
    term = RdfTerm('DrugCostCategory', 'http://schema.org/DrugCostCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicineSystem(MedicalEnumeration):
    term = RdfTerm('MedicineSystem', 'http://schema.org/MedicineSystem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrugPrescriptionStatus(MedicalEnumeration):
    term = RdfTerm('DrugPrescriptionStatus', 'http://schema.org/DrugPrescriptionStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalProcedureType(MedicalEnumeration):
    term = RdfTerm('MedicalProcedureType', 'http://schema.org/MedicalProcedureType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalTrialDesign(MedicalEnumeration):
    term = RdfTerm('MedicalTrialDesign', 'http://schema.org/MedicalTrialDesign', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalAudienceType(MedicalEnumeration):
    term = RdfTerm('MedicalAudienceType', 'http://schema.org/MedicalAudienceType', ['1.1', '1.2-DRAFT'])

class MedicalObservationalStudyDesign(MedicalEnumeration):
    term = RdfTerm('MedicalObservationalStudyDesign', 'http://schema.org/MedicalObservationalStudyDesign', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalStudyStatus(MedicalEnumeration):
    term = RdfTerm('MedicalStudyStatus', 'http://schema.org/MedicalStudyStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InfectiousAgentClass(MedicalEnumeration):
    term = RdfTerm('InfectiousAgentClass', 'http://schema.org/InfectiousAgentClass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PhysicalExam(MedicalProcedure, MedicalEnumeration):
    term = RdfTerm('PhysicalExam', 'http://schema.org/PhysicalExam', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalDevicePurpose(MedicalEnumeration):
    term = RdfTerm('MedicalDevicePurpose', 'http://schema.org/MedicalDevicePurpose', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalEvidenceLevel(MedicalEnumeration):
    term = RdfTerm('MedicalEvidenceLevel', 'http://schema.org/MedicalEvidenceLevel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DrugPregnancyCategory(MedicalEnumeration):
    term = RdfTerm('DrugPregnancyCategory', 'http://schema.org/DrugPregnancyCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SizeSpecification(QualitativeValue):
    term = RdfTerm('SizeSpecification', 'http://schema.org/SizeSpecification', ['1.2-DRAFT'])

class SteeringPositionValue(QualitativeValue):
    term = RdfTerm('SteeringPositionValue', 'http://schema.org/SteeringPositionValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BedType(QualitativeValue):
    term = RdfTerm('BedType', 'http://schema.org/BedType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DriveWheelConfigurationValue(QualitativeValue):
    term = RdfTerm('DriveWheelConfigurationValue', 'http://schema.org/DriveWheelConfigurationValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalSpecialty(Specialty, MedicalEnumeration):
    term = RdfTerm('MedicalSpecialty', 'http://schema.org/MedicalSpecialty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EmployeeRole(OrganizationRole):
    term = RdfTerm('EmployeeRole', 'http://schema.org/EmployeeRole', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowToSupply(HowToItem):
    term = RdfTerm('HowToSupply', 'http://schema.org/HowToSupply', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HowToTool(HowToItem):
    term = RdfTerm('HowToTool', 'http://schema.org/HowToTool', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ParentAudience(PeopleAudience):
    term = RdfTerm('ParentAudience', 'http://schema.org/ParentAudience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalAudience(Audience, PeopleAudience):
    term = RdfTerm('MedicalAudience', 'http://schema.org/MedicalAudience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TVSeries(CreativeWorkSeries, CreativeWork):
    term = RdfTerm('TVSeries', 'http://schema.org/TVSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BookSeries(CreativeWorkSeries):
    term = RdfTerm('BookSeries', 'http://schema.org/BookSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Periodical(CreativeWorkSeries):
    term = RdfTerm('Periodical', 'http://schema.org/Periodical', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VideoGameSeries(CreativeWorkSeries):
    term = RdfTerm('VideoGameSeries', 'http://schema.org/VideoGameSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MovieSeries(CreativeWorkSeries):
    term = RdfTerm('MovieSeries', 'http://schema.org/MovieSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PodcastSeries(CreativeWorkSeries):
    term = RdfTerm('PodcastSeries', 'http://schema.org/PodcastSeries', ['1.0', '1.1', '1.2-DRAFT'])

class RadioSeries(CreativeWorkSeries):
    term = RdfTerm('RadioSeries', 'http://schema.org/RadioSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FMRadioChannel(RadioChannel):
    term = RdfTerm('FMRadioChannel', 'http://schema.org/FMRadioChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AMRadioChannel(RadioChannel):
    term = RdfTerm('AMRadioChannel', 'http://schema.org/AMRadioChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RadioBroadcastService(BroadcastService):
    term = RdfTerm('RadioBroadcastService', 'http://schema.org/RadioBroadcastService', ['1.0', '1.1', '1.2-DRAFT'])

class CurrencyConversionService(FinancialProduct):
    term = RdfTerm('CurrencyConversionService', 'http://schema.org/CurrencyConversionService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PaymentService(PaymentMethod, FinancialProduct):
    term = RdfTerm('PaymentService', 'http://schema.org/PaymentService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PaymentCard(PaymentMethod, FinancialProduct):
    term = RdfTerm('PaymentCard', 'http://schema.org/PaymentCard', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BankAccount(FinancialProduct):
    term = RdfTerm('BankAccount', 'http://schema.org/BankAccount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LoanOrCredit(FinancialProduct):
    term = RdfTerm('LoanOrCredit', 'http://schema.org/LoanOrCredit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InvestmentOrDeposit(FinancialProduct):
    term = RdfTerm('InvestmentOrDeposit', 'http://schema.org/InvestmentOrDeposit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GeoCircle(GeoShape):
    term = RdfTerm('GeoCircle', 'http://schema.org/GeoCircle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MonetaryAmountDistribution(QuantitativeValueDistribution):
    term = RdfTerm('MonetaryAmountDistribution', 'http://schema.org/MonetaryAmountDistribution', ['1.0', '1.1', '1.2-DRAFT'])

class LocationFeatureSpecification(PropertyValue):
    term = RdfTerm('LocationFeatureSpecification', 'http://schema.org/LocationFeatureSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Observation(QuantitativeValue, Intangible):
    term = RdfTerm('Observation', 'http://schema.org/Observation', ['1.0', '1.1', '1.2-DRAFT'])

class PostalAddress(ContactPoint):
    term = RdfTerm('PostalAddress', 'http://schema.org/PostalAddress', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CompoundPriceSpecification(PriceSpecification):
    term = RdfTerm('CompoundPriceSpecification', 'http://schema.org/CompoundPriceSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PaymentChargeSpecification(PriceSpecification):
    term = RdfTerm('PaymentChargeSpecification', 'http://schema.org/PaymentChargeSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class UnitPriceSpecification(PriceSpecification):
    term = RdfTerm('UnitPriceSpecification', 'http://schema.org/UnitPriceSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DeliveryChargeSpecification(PriceSpecification):
    term = RdfTerm('DeliveryChargeSpecification', 'http://schema.org/DeliveryChargeSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalCode(MedicalIntangible, CategoryCode):
    term = RdfTerm('MedicalCode', 'http://schema.org/MedicalCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class EmployerAggregateRating(AggregateRating):
    term = RdfTerm('EmployerAggregateRating', 'http://schema.org/EmployerAggregateRating', ['1.0', '1.1', '1.2-DRAFT'])

class SingleFamilyResidence(House):
    term = RdfTerm('SingleFamilyResidence', 'http://schema.org/SingleFamilyResidence', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MeetingRoom(Room):
    term = RdfTerm('MeetingRoom', 'http://schema.org/MeetingRoom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HotelRoom(Room):
    term = RdfTerm('HotelRoom', 'http://schema.org/HotelRoom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Mosque(PlaceOfWorship):
    term = RdfTerm('Mosque', 'http://schema.org/Mosque', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Church(PlaceOfWorship):
    term = RdfTerm('Church', 'http://schema.org/Church', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BuddhistTemple(PlaceOfWorship):
    term = RdfTerm('BuddhistTemple', 'http://schema.org/BuddhistTemple', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Synagogue(PlaceOfWorship):
    term = RdfTerm('Synagogue', 'http://schema.org/Synagogue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HinduTemple(PlaceOfWorship):
    term = RdfTerm('HinduTemple', 'http://schema.org/HinduTemple', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Preschool(EducationalOrganization):
    term = RdfTerm('Preschool', 'http://schema.org/Preschool', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ElementarySchool(EducationalOrganization):
    term = RdfTerm('ElementarySchool', 'http://schema.org/ElementarySchool', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class School(EducationalOrganization):
    term = RdfTerm('School', 'http://schema.org/School', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MiddleSchool(EducationalOrganization):
    term = RdfTerm('MiddleSchool', 'http://schema.org/MiddleSchool', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HighSchool(EducationalOrganization):
    term = RdfTerm('HighSchool', 'http://schema.org/HighSchool', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CollegeOrUniversity(EducationalOrganization):
    term = RdfTerm('CollegeOrUniversity', 'http://schema.org/CollegeOrUniversity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Embassy(GovernmentBuilding):
    term = RdfTerm('Embassy', 'http://schema.org/Embassy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DefenceEstablishment(GovernmentBuilding):
    term = RdfTerm('DefenceEstablishment', 'http://schema.org/DefenceEstablishment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LegislativeBuilding(GovernmentBuilding):
    term = RdfTerm('LegislativeBuilding', 'http://schema.org/LegislativeBuilding', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Courthouse(GovernmentBuilding):
    term = RdfTerm('Courthouse', 'http://schema.org/Courthouse', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CityHall(GovernmentBuilding):
    term = RdfTerm('CityHall', 'http://schema.org/CityHall', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LakeBodyOfWater(BodyOfWater):
    term = RdfTerm('LakeBodyOfWater', 'http://schema.org/LakeBodyOfWater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OceanBodyOfWater(BodyOfWater):
    term = RdfTerm('OceanBodyOfWater', 'http://schema.org/OceanBodyOfWater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Canal(BodyOfWater):
    term = RdfTerm('Canal', 'http://schema.org/Canal', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RiverBodyOfWater(BodyOfWater):
    term = RdfTerm('RiverBodyOfWater', 'http://schema.org/RiverBodyOfWater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SeaBodyOfWater(BodyOfWater):
    term = RdfTerm('SeaBodyOfWater', 'http://schema.org/SeaBodyOfWater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Pond(BodyOfWater):
    term = RdfTerm('Pond', 'http://schema.org/Pond', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Waterfall(BodyOfWater):
    term = RdfTerm('Waterfall', 'http://schema.org/Waterfall', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Reservoir(BodyOfWater):
    term = RdfTerm('Reservoir', 'http://schema.org/Reservoir', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Hostel(LodgingBusiness):
    term = RdfTerm('Hostel', 'http://schema.org/Hostel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Motel(LodgingBusiness):
    term = RdfTerm('Motel', 'http://schema.org/Motel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BedAndBreakfast(LodgingBusiness):
    term = RdfTerm('BedAndBreakfast', 'http://schema.org/BedAndBreakfast', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Resort(LodgingBusiness):
    term = RdfTerm('Resort', 'http://schema.org/Resort', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Campground(CivicStructure, LodgingBusiness):
    term = RdfTerm('Campground', 'http://schema.org/Campground', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VacationRental(LodgingBusiness):
    term = RdfTerm('VacationRental', 'http://schema.org/VacationRental', ['1.2-DRAFT'])

class Hotel(LodgingBusiness):
    term = RdfTerm('Hotel', 'http://schema.org/Hotel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PoliceStation(CivicStructure, EmergencyService):
    term = RdfTerm('PoliceStation', 'http://schema.org/PoliceStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FireStation(CivicStructure, EmergencyService):
    term = RdfTerm('FireStation', 'http://schema.org/FireStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Hospital(EmergencyService, MedicalOrganization, CivicStructure):
    term = RdfTerm('Hospital', 'http://schema.org/Hospital', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Pharmacy(MedicalOrganization, MedicalBusiness):
    term = RdfTerm('Pharmacy', 'http://schema.org/Pharmacy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Dentist(LocalBusiness, MedicalBusiness, MedicalOrganization):
    term = RdfTerm('Dentist', 'http://schema.org/Dentist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Physician(MedicalOrganization, MedicalBusiness):
    term = RdfTerm('Physician', 'http://schema.org/Physician', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MedicalClinic(MedicalBusiness, MedicalOrganization):
    term = RdfTerm('MedicalClinic', 'http://schema.org/MedicalClinic', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Psychiatric(MedicalBusiness):
    term = RdfTerm('Psychiatric', 'http://schema.org/Psychiatric', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Podiatric(MedicalBusiness):
    term = RdfTerm('Podiatric', 'http://schema.org/Podiatric', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PublicHealth(MedicalBusiness):
    term = RdfTerm('PublicHealth', 'http://schema.org/PublicHealth', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PlasticSurgery(MedicalBusiness):
    term = RdfTerm('PlasticSurgery', 'http://schema.org/PlasticSurgery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DietNutrition(MedicalBusiness):
    term = RdfTerm('DietNutrition', 'http://schema.org/DietNutrition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Emergency(MedicalBusiness):
    term = RdfTerm('Emergency', 'http://schema.org/Emergency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Oncologic(MedicalBusiness):
    term = RdfTerm('Oncologic', 'http://schema.org/Oncologic', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Gynecologic(MedicalBusiness):
    term = RdfTerm('Gynecologic', 'http://schema.org/Gynecologic', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Dermatology(MedicalBusiness):
    term = RdfTerm('Dermatology', 'http://schema.org/Dermatology', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Geriatric(MedicalBusiness):
    term = RdfTerm('Geriatric', 'http://schema.org/Geriatric', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Otolaryngologic(MedicalBusiness):
    term = RdfTerm('Otolaryngologic', 'http://schema.org/Otolaryngologic', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Physiotherapy(MedicalBusiness):
    term = RdfTerm('Physiotherapy', 'http://schema.org/Physiotherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PrimaryCare(MedicalBusiness):
    term = RdfTerm('PrimaryCare', 'http://schema.org/PrimaryCare', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Midwifery(MedicalBusiness):
    term = RdfTerm('Midwifery', 'http://schema.org/Midwifery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Obstetric(MedicalBusiness):
    term = RdfTerm('Obstetric', 'http://schema.org/Obstetric', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CommunityHealth(MedicalBusiness):
    term = RdfTerm('CommunityHealth', 'http://schema.org/CommunityHealth', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Pediatric(MedicalBusiness):
    term = RdfTerm('Pediatric', 'http://schema.org/Pediatric', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Nursing(MedicalBusiness):
    term = RdfTerm('Nursing', 'http://schema.org/Nursing', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Optometric(MedicalBusiness):
    term = RdfTerm('Optometric', 'http://schema.org/Optometric', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Optician(MedicalBusiness):
    term = RdfTerm('Optician', 'http://schema.org/Optician', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Restaurant(FoodEstablishment):
    term = RdfTerm('Restaurant', 'http://schema.org/Restaurant', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BarOrPub(FoodEstablishment):
    term = RdfTerm('BarOrPub', 'http://schema.org/BarOrPub', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Distillery(FoodEstablishment):
    term = RdfTerm('Distillery', 'http://schema.org/Distillery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Brewery(FoodEstablishment):
    term = RdfTerm('Brewery', 'http://schema.org/Brewery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FastFoodRestaurant(FoodEstablishment):
    term = RdfTerm('FastFoodRestaurant', 'http://schema.org/FastFoodRestaurant', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class IceCreamShop(FoodEstablishment):
    term = RdfTerm('IceCreamShop', 'http://schema.org/IceCreamShop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CafeOrCoffeeShop(FoodEstablishment):
    term = RdfTerm('CafeOrCoffeeShop', 'http://schema.org/CafeOrCoffeeShop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Bakery(FoodEstablishment):
    term = RdfTerm('Bakery', 'http://schema.org/Bakery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Winery(FoodEstablishment):
    term = RdfTerm('Winery', 'http://schema.org/Winery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GasStation(AutomotiveBusiness):
    term = RdfTerm('GasStation', 'http://schema.org/GasStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutoBodyShop(AutomotiveBusiness):
    term = RdfTerm('AutoBodyShop', 'http://schema.org/AutoBodyShop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutoDealer(AutomotiveBusiness):
    term = RdfTerm('AutoDealer', 'http://schema.org/AutoDealer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutoRental(AutomotiveBusiness):
    term = RdfTerm('AutoRental', 'http://schema.org/AutoRental', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutoRepair(AutomotiveBusiness):
    term = RdfTerm('AutoRepair', 'http://schema.org/AutoRepair', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MotorcycleRepair(AutomotiveBusiness):
    term = RdfTerm('MotorcycleRepair', 'http://schema.org/MotorcycleRepair', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutoWash(AutomotiveBusiness):
    term = RdfTerm('AutoWash', 'http://schema.org/AutoWash', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MotorcycleDealer(AutomotiveBusiness):
    term = RdfTerm('MotorcycleDealer', 'http://schema.org/MotorcycleDealer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HairSalon(HealthAndBeautyBusiness):
    term = RdfTerm('HairSalon', 'http://schema.org/HairSalon', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TattooParlor(HealthAndBeautyBusiness):
    term = RdfTerm('TattooParlor', 'http://schema.org/TattooParlor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class NailSalon(HealthAndBeautyBusiness):
    term = RdfTerm('NailSalon', 'http://schema.org/NailSalon', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BeautySalon(HealthAndBeautyBusiness):
    term = RdfTerm('BeautySalon', 'http://schema.org/BeautySalon', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DaySpa(HealthAndBeautyBusiness):
    term = RdfTerm('DaySpa', 'http://schema.org/DaySpa', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Notary(LegalService):
    term = RdfTerm('Notary', 'http://schema.org/Notary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Attorney(LegalService):
    term = RdfTerm('Attorney', 'http://schema.org/Attorney', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OfficeEquipmentStore(Store):
    term = RdfTerm('OfficeEquipmentStore', 'http://schema.org/OfficeEquipmentStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MensClothingStore(Store):
    term = RdfTerm('MensClothingStore', 'http://schema.org/MensClothingStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ClothingStore(Store):
    term = RdfTerm('ClothingStore', 'http://schema.org/ClothingStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutoPartsStore(Store, AutomotiveBusiness):
    term = RdfTerm('AutoPartsStore', 'http://schema.org/AutoPartsStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PawnShop(Store):
    term = RdfTerm('PawnShop', 'http://schema.org/PawnShop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GroceryStore(Store):
    term = RdfTerm('GroceryStore', 'http://schema.org/GroceryStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OutletStore(Store):
    term = RdfTerm('OutletStore', 'http://schema.org/OutletStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class FurnitureStore(Store):
    term = RdfTerm('FurnitureStore', 'http://schema.org/FurnitureStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class JewelryStore(Store):
    term = RdfTerm('JewelryStore', 'http://schema.org/JewelryStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ToyStore(Store):
    term = RdfTerm('ToyStore', 'http://schema.org/ToyStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LiquorStore(Store):
    term = RdfTerm('LiquorStore', 'http://schema.org/LiquorStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PetStore(Store):
    term = RdfTerm('PetStore', 'http://schema.org/PetStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ConvenienceStore(Store):
    term = RdfTerm('ConvenienceStore', 'http://schema.org/ConvenienceStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Florist(Store):
    term = RdfTerm('Florist', 'http://schema.org/Florist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SportingGoodsStore(Store):
    term = RdfTerm('SportingGoodsStore', 'http://schema.org/SportingGoodsStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ElectronicsStore(Store):
    term = RdfTerm('ElectronicsStore', 'http://schema.org/ElectronicsStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BikeStore(Store):
    term = RdfTerm('BikeStore', 'http://schema.org/BikeStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BookStore(Store):
    term = RdfTerm('BookStore', 'http://schema.org/BookStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComputerStore(Store):
    term = RdfTerm('ComputerStore', 'http://schema.org/ComputerStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MusicStore(Store):
    term = RdfTerm('MusicStore', 'http://schema.org/MusicStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class WholesaleStore(Store):
    term = RdfTerm('WholesaleStore', 'http://schema.org/WholesaleStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HomeGoodsStore(Store):
    term = RdfTerm('HomeGoodsStore', 'http://schema.org/HomeGoodsStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TireShop(Store):
    term = RdfTerm('TireShop', 'http://schema.org/TireShop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GardenStore(Store):
    term = RdfTerm('GardenStore', 'http://schema.org/GardenStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DepartmentStore(Store):
    term = RdfTerm('DepartmentStore', 'http://schema.org/DepartmentStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HobbyShop(Store):
    term = RdfTerm('HobbyShop', 'http://schema.org/HobbyShop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HardwareStore(Store):
    term = RdfTerm('HardwareStore', 'http://schema.org/HardwareStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MobilePhoneStore(Store):
    term = RdfTerm('MobilePhoneStore', 'http://schema.org/MobilePhoneStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MovieRentalStore(Store):
    term = RdfTerm('MovieRentalStore', 'http://schema.org/MovieRentalStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ShoeStore(Store):
    term = RdfTerm('ShoeStore', 'http://schema.org/ShoeStore', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class StadiumOrArena(SportsActivityLocation, CivicStructure):
    term = RdfTerm('StadiumOrArena', 'http://schema.org/StadiumOrArena', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    term = RdfTerm('HealthClub', 'http://schema.org/HealthClub', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SportsClub(SportsActivityLocation):
    term = RdfTerm('SportsClub', 'http://schema.org/SportsClub', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BowlingAlley(SportsActivityLocation):
    term = RdfTerm('BowlingAlley', 'http://schema.org/BowlingAlley', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PublicSwimmingPool(SportsActivityLocation):
    term = RdfTerm('PublicSwimmingPool', 'http://schema.org/PublicSwimmingPool', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ExerciseGym(SportsActivityLocation):
    term = RdfTerm('ExerciseGym', 'http://schema.org/ExerciseGym', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GolfCourse(SportsActivityLocation):
    term = RdfTerm('GolfCourse', 'http://schema.org/GolfCourse', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class TennisComplex(SportsActivityLocation):
    term = RdfTerm('TennisComplex', 'http://schema.org/TennisComplex', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PostOffice(GovernmentOffice):
    term = RdfTerm('PostOffice', 'http://schema.org/PostOffice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BankOrCreditUnion(FinancialService):
    term = RdfTerm('BankOrCreditUnion', 'http://schema.org/BankOrCreditUnion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InsuranceAgency(FinancialService):
    term = RdfTerm('InsuranceAgency', 'http://schema.org/InsuranceAgency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AccountingService(FinancialService):
    term = RdfTerm('AccountingService', 'http://schema.org/AccountingService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AutomatedTeller(FinancialService):
    term = RdfTerm('AutomatedTeller', 'http://schema.org/AutomatedTeller', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HousePainter(HomeAndConstructionBusiness):
    term = RdfTerm('HousePainter', 'http://schema.org/HousePainter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Locksmith(HomeAndConstructionBusiness):
    term = RdfTerm('Locksmith', 'http://schema.org/Locksmith', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RoofingContractor(HomeAndConstructionBusiness):
    term = RdfTerm('RoofingContractor', 'http://schema.org/RoofingContractor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class GeneralContractor(HomeAndConstructionBusiness):
    term = RdfTerm('GeneralContractor', 'http://schema.org/GeneralContractor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MovingCompany(HomeAndConstructionBusiness):
    term = RdfTerm('MovingCompany', 'http://schema.org/MovingCompany', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class HVACBusiness(HomeAndConstructionBusiness):
    term = RdfTerm('HVACBusiness', 'http://schema.org/HVACBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Electrician(HomeAndConstructionBusiness):
    term = RdfTerm('Electrician', 'http://schema.org/Electrician', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Plumber(HomeAndConstructionBusiness):
    term = RdfTerm('Plumber', 'http://schema.org/Plumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class NightClub(EntertainmentBusiness):
    term = RdfTerm('NightClub', 'http://schema.org/NightClub', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MovieTheater(EntertainmentBusiness, CivicStructure):
    term = RdfTerm('MovieTheater', 'http://schema.org/MovieTheater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AdultEntertainment(EntertainmentBusiness):
    term = RdfTerm('AdultEntertainment', 'http://schema.org/AdultEntertainment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ArtGallery(EntertainmentBusiness):
    term = RdfTerm('ArtGallery', 'http://schema.org/ArtGallery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AmusementPark(EntertainmentBusiness):
    term = RdfTerm('AmusementPark', 'http://schema.org/AmusementPark', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Casino(EntertainmentBusiness):
    term = RdfTerm('Casino', 'http://schema.org/Casino', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComedyClub(EntertainmentBusiness):
    term = RdfTerm('ComedyClub', 'http://schema.org/ComedyClub', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PrependAction(InsertAction):
    term = RdfTerm('PrependAction', 'http://schema.org/PrependAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class AppendAction(InsertAction):
    term = RdfTerm('AppendAction', 'http://schema.org/AppendAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ConfirmAction(InformAction):
    term = RdfTerm('ConfirmAction', 'http://schema.org/ConfirmAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RsvpAction(InformAction):
    term = RdfTerm('RsvpAction', 'http://schema.org/RsvpAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class OccupationalTherapy(MedicalTherapy):
    term = RdfTerm('OccupationalTherapy', 'http://schema.org/OccupationalTherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PalliativeProcedure(MedicalTherapy, MedicalProcedure):
    term = RdfTerm('PalliativeProcedure', 'http://schema.org/PalliativeProcedure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class PhysicalTherapy(MedicalTherapy):
    term = RdfTerm('PhysicalTherapy', 'http://schema.org/PhysicalTherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RadiationTherapy(MedicalTherapy):
    term = RdfTerm('RadiationTherapy', 'http://schema.org/RadiationTherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class RespiratoryTherapy(MedicalTherapy):
    term = RdfTerm('RespiratoryTherapy', 'http://schema.org/RespiratoryTherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VitalSign(MedicalSign):
    term = RdfTerm('VitalSign', 'http://schema.org/VitalSign', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class LiveBlogPosting(BlogPosting):
    term = RdfTerm('LiveBlogPosting', 'http://schema.org/LiveBlogPosting', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ImageGallery(MediaGallery):
    term = RdfTerm('ImageGallery', 'http://schema.org/ImageGallery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class VideoGallery(MediaGallery):
    term = RdfTerm('VideoGallery', 'http://schema.org/VideoGallery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Patient(MedicalAudience, Person):
    term = RdfTerm('Patient', 'http://schema.org/Patient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class Newspaper(Periodical):
    term = RdfTerm('Newspaper', 'http://schema.org/Newspaper', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ComicSeries(Periodical):
    term = RdfTerm('ComicSeries', 'http://schema.org/ComicSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CreditCard(PaymentCard, LoanOrCredit):
    term = RdfTerm('CreditCard', 'http://schema.org/CreditCard', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class MortgageLoan(LoanOrCredit):
    term = RdfTerm('MortgageLoan', 'http://schema.org/MortgageLoan', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class DepositAccount(BankAccount, InvestmentOrDeposit):
    term = RdfTerm('DepositAccount', 'http://schema.org/DepositAccount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class InvestmentFund(InvestmentOrDeposit):
    term = RdfTerm('InvestmentFund', 'http://schema.org/InvestmentFund', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class BrokerageAccount(InvestmentOrDeposit):
    term = RdfTerm('BrokerageAccount', 'http://schema.org/BrokerageAccount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class CatholicChurch(Church):
    term = RdfTerm('CatholicChurch', 'http://schema.org/CatholicChurch', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class SkiResort(Resort, SportsActivityLocation):
    term = RdfTerm('SkiResort', 'http://schema.org/SkiResort', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class IndividualPhysician(Physician):
    term = RdfTerm('IndividualPhysician', 'http://schema.org/IndividualPhysician', [])

class PhysiciansOffice(Physician):
    term = RdfTerm('PhysiciansOffice', 'http://schema.org/PhysiciansOffice', [])

class CovidTestingFacility(MedicalClinic):
    term = RdfTerm('CovidTestingFacility', 'http://schema.org/CovidTestingFacility', ['1.1', '1.2-DRAFT'])

class paymentMethodType(RdfProperty[schemaorg.PaymentMethodType]):
    term = RdfTerm('paymentMethodType', 'http://schema.org/paymentMethodType', [])

class event(RdfProperty[schemaorg.Event]):
    term = RdfTerm('event', 'http://schema.org/event', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class maxValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm('maxValue', 'http://schema.org/maxValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mileageFromOdometer(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('mileageFromOdometer', 'http://schema.org/mileageFromOdometer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class doorTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('doorTime', 'http://schema.org/doorTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contentUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('contentUrl', 'http://schema.org/contentUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sibling(RdfProperty[schemaorg.Person]):
    term = RdfTerm('sibling', 'http://schema.org/sibling', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class offersPrescriptionByMail(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('offersPrescriptionByMail', 'http://schema.org/offersPrescriptionByMail', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reviewRating(RdfProperty[schemaorg.Rating]):
    term = RdfTerm('reviewRating', 'http://schema.org/reviewRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reviewCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('reviewCount', 'http://schema.org/reviewCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasProductReturnPolicy(RdfProperty[schemaorg.ProductReturnPolicy]):
    term = RdfTerm('hasProductReturnPolicy', 'http://schema.org/hasProductReturnPolicy', ['1.0', '1.1', '1.2-DRAFT'])

class fuelCapacity(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('fuelCapacity', 'http://schema.org/fuelCapacity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class howPerformed(RdfProperty[schemaorg.Text]):
    term = RdfTerm('howPerformed', 'http://schema.org/howPerformed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class productReturnLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm('productReturnLink', 'http://schema.org/productReturnLink', ['1.0', '1.1', '1.2-DRAFT'])

class childMinAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm('childMinAge', 'http://schema.org/childMinAge', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class printSection(RdfProperty[schemaorg.Text]):
    term = RdfTerm('printSection', 'http://schema.org/printSection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class departureAirport(RdfProperty[schemaorg.Airport]):
    term = RdfTerm('departureAirport', 'http://schema.org/departureAirport', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class productID(RdfProperty[schemaorg.Text]):
    term = RdfTerm('productID', 'http://schema.org/productID', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inverseOf(RdfProperty[schemaorg.Property]):
    term = RdfTerm('inverseOf', 'http://schema.org/inverseOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class name(RdfProperty[schemaorg.Text]):
    term = RdfTerm('name', 'http://schema.org/name', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class unnamedSourcesPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('unnamedSourcesPolicy', 'http://schema.org/unnamedSourcesPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class playerType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('playerType', 'http://schema.org/playerType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class knows(RdfProperty[schemaorg.Person]):
    term = RdfTerm('knows', 'http://schema.org/knows', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isicV4(RdfProperty[schemaorg.Text]):
    term = RdfTerm('isicV4', 'http://schema.org/isicV4', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fundedItem(RdfProperty[schemaorg.Product | schemaorg.Person | schemaorg.MedicalEntity | schemaorg.BioChemEntity | schemaorg.Organization | schemaorg.Event | schemaorg.CreativeWork]):
    term = RdfTerm('fundedItem', 'http://schema.org/fundedItem', ['1.0', '1.1', '1.2-DRAFT'])

class legislationIdentifier(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('legislationIdentifier', 'http://schema.org/legislationIdentifier', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class loanTerm(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('loanTerm', 'http://schema.org/loanTerm', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class provider(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('provider', 'http://schema.org/provider', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class physicalRequirement(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('physicalRequirement', 'http://schema.org/physicalRequirement', ['1.1', '1.2-DRAFT'])

class applicationContact(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm('applicationContact', 'http://schema.org/applicationContact', ['1.1', '1.2-DRAFT'])

class drugClass(RdfProperty[schemaorg.DrugClass]):
    term = RdfTerm('drugClass', 'http://schema.org/drugClass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class endDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('endDate', 'http://schema.org/endDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class certificationIdentification(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('certificationIdentification', 'http://schema.org/certificationIdentification', [])

class resultReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm('resultReview', 'http://schema.org/resultReview', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vehicleTransmission(RdfProperty[schemaorg.QualitativeValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('vehicleTransmission', 'http://schema.org/vehicleTransmission', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class responsibilities(RdfProperty[schemaorg.Text]):
    term = RdfTerm('responsibilities', 'http://schema.org/responsibilities', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class nationality(RdfProperty[schemaorg.Country]):
    term = RdfTerm('nationality', 'http://schema.org/nationality', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class relatedDrug(RdfProperty[schemaorg.Drug]):
    term = RdfTerm('relatedDrug', 'http://schema.org/relatedDrug', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class diagram(RdfProperty[schemaorg.ImageObject]):
    term = RdfTerm('diagram', 'http://schema.org/diagram', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class photos(RdfProperty[schemaorg.ImageObject | schemaorg.Photograph]):
    term = RdfTerm('photos', 'http://schema.org/photos', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class downPayment(RdfProperty[schemaorg.Number | schemaorg.MonetaryAmount]):
    term = RdfTerm('downPayment', 'http://schema.org/downPayment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class usesDevice(RdfProperty[schemaorg.MedicalDevice]):
    term = RdfTerm('usesDevice', 'http://schema.org/usesDevice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class warrantyScope(RdfProperty[schemaorg.WarrantyScope]):
    term = RdfTerm('warrantyScope', 'http://schema.org/warrantyScope', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class parentService(RdfProperty[schemaorg.BroadcastService]):
    term = RdfTerm('parentService', 'http://schema.org/parentService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bodyType(RdfProperty[schemaorg.QualitativeValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('bodyType', 'http://schema.org/bodyType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class actionProcess(RdfProperty[schemaorg.HowTo]):
    term = RdfTerm('actionProcess', 'http://schema.org/actionProcess', [])

class educationRequirements(RdfProperty[schemaorg.Text | schemaorg.EducationalOccupationalCredential]):
    term = RdfTerm('educationRequirements', 'http://schema.org/educationRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class commentTime(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('commentTime', 'http://schema.org/commentTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class coursePrerequisites(RdfProperty[schemaorg.Course | schemaorg.Text | schemaorg.AlignmentObject]):
    term = RdfTerm('coursePrerequisites', 'http://schema.org/coursePrerequisites', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class honorificPrefix(RdfProperty[schemaorg.Text]):
    term = RdfTerm('honorificPrefix', 'http://schema.org/honorificPrefix', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class priceValidUntil(RdfProperty[schemaorg.Date]):
    term = RdfTerm('priceValidUntil', 'http://schema.org/priceValidUntil', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class siblings(RdfProperty[schemaorg.Person]):
    term = RdfTerm('siblings', 'http://schema.org/siblings', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recipe(RdfProperty[schemaorg.Recipe]):
    term = RdfTerm('recipe', 'http://schema.org/recipe', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class minPrice(RdfProperty[schemaorg.Number]):
    term = RdfTerm('minPrice', 'http://schema.org/minPrice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class yearsInOperation(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('yearsInOperation', 'http://schema.org/yearsInOperation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class petsAllowed(RdfProperty[schemaorg.Boolean | schemaorg.Text]):
    term = RdfTerm('petsAllowed', 'http://schema.org/petsAllowed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bioChemSimilarity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('bioChemSimilarity', 'http://schema.org/bioChemSimilarity', ['1.2-DRAFT'])

class aggregateRating(RdfProperty[schemaorg.AggregateRating]):
    term = RdfTerm('aggregateRating', 'http://schema.org/aggregateRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasEnergyEfficiencyCategory(RdfProperty[schemaorg.EnergyEfficiencyEnumeration]):
    term = RdfTerm('hasEnergyEfficiencyCategory', 'http://schema.org/hasEnergyEfficiencyCategory', ['1.1', '1.2-DRAFT'])

class alcoholWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm('alcoholWarning', 'http://schema.org/alcoholWarning', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class totalHistoricalEnrollment(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('totalHistoricalEnrollment', 'http://schema.org/totalHistoricalEnrollment', ['1.2-DRAFT'])

class colleague(RdfProperty[schemaorg.URL | schemaorg.Person]):
    term = RdfTerm('colleague', 'http://schema.org/colleague', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class permittedUsage(RdfProperty[schemaorg.Text]):
    term = RdfTerm('permittedUsage', 'http://schema.org/permittedUsage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class expectsAcceptanceOf(RdfProperty[schemaorg.Offer]):
    term = RdfTerm('expectsAcceptanceOf', 'http://schema.org/expectsAcceptanceOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class citation(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('citation', 'http://schema.org/citation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class locationCreated(RdfProperty[schemaorg.Place]):
    term = RdfTerm('locationCreated', 'http://schema.org/locationCreated', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tourBookingPage(RdfProperty[schemaorg.URL]):
    term = RdfTerm('tourBookingPage', 'http://schema.org/tourBookingPage', ['1.1', '1.2-DRAFT'])

class replyToUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('replyToUrl', 'http://schema.org/replyToUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sdPublisher(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('sdPublisher', 'http://schema.org/sdPublisher', ['1.0', '1.1', '1.2-DRAFT'])

class programMembershipUsed(RdfProperty[schemaorg.ProgramMembership]):
    term = RdfTerm('programMembershipUsed', 'http://schema.org/programMembershipUsed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class totalPrice(RdfProperty[schemaorg.Number | schemaorg.Text | schemaorg.PriceSpecification]):
    term = RdfTerm('totalPrice', 'http://schema.org/totalPrice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class eligibleQuantity(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('eligibleQuantity', 'http://schema.org/eligibleQuantity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class antagonist(RdfProperty[schemaorg.Muscle]):
    term = RdfTerm('antagonist', 'http://schema.org/antagonist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class thumbnail(RdfProperty[schemaorg.ImageObject]):
    term = RdfTerm('thumbnail', 'http://schema.org/thumbnail', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class passengerSequenceNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('passengerSequenceNumber', 'http://schema.org/passengerSequenceNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vehicleInteriorColor(RdfProperty[schemaorg.Text]):
    term = RdfTerm('vehicleInteriorColor', 'http://schema.org/vehicleInteriorColor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class circle(RdfProperty[schemaorg.Text]):
    term = RdfTerm('circle', 'http://schema.org/circle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class missionCoveragePrioritiesPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('missionCoveragePrioritiesPolicy', 'http://schema.org/missionCoveragePrioritiesPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class containedInPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm('containedInPlace', 'http://schema.org/containedInPlace', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasCertification(RdfProperty[schemaorg.Certification]):
    term = RdfTerm('hasCertification', 'http://schema.org/hasCertification', [])

class phoneticText(RdfProperty[schemaorg.Text]):
    term = RdfTerm('phoneticText', 'http://schema.org/phoneticText', ['1.1', '1.2-DRAFT'])

class isSimilarTo(RdfProperty[schemaorg.Product | schemaorg.Service]):
    term = RdfTerm('isSimilarTo', 'http://schema.org/isSimilarTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class videoFrameSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm('videoFrameSize', 'http://schema.org/videoFrameSize', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fuelConsumption(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('fuelConsumption', 'http://schema.org/fuelConsumption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class yearlyRevenue(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('yearlyRevenue', 'http://schema.org/yearlyRevenue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class steps(RdfProperty[schemaorg.Text | schemaorg.ItemList | schemaorg.CreativeWork]):
    term = RdfTerm('steps', 'http://schema.org/steps', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class browserRequirements(RdfProperty[schemaorg.Text]):
    term = RdfTerm('browserRequirements', 'http://schema.org/browserRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class paymentMethod(RdfProperty[schemaorg.PaymentMethod | schemaorg.Text]):
    term = RdfTerm('paymentMethod', 'http://schema.org/paymentMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasRepresentation(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('hasRepresentation', 'http://schema.org/hasRepresentation', ['1.2-DRAFT'])

class carrierRequirements(RdfProperty[schemaorg.Text]):
    term = RdfTerm('carrierRequirements', 'http://schema.org/carrierRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class distribution(RdfProperty[schemaorg.DataDownload]):
    term = RdfTerm('distribution', 'http://schema.org/distribution', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class benefits(RdfProperty[schemaorg.Text]):
    term = RdfTerm('benefits', 'http://schema.org/benefits', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class variablesMeasured(RdfProperty[schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm('variablesMeasured', 'http://schema.org/variablesMeasured', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class educationalCredentialAwarded(RdfProperty[schemaorg.EducationalOccupationalCredential | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('educationalCredentialAwarded', 'http://schema.org/educationalCredentialAwarded', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class engineDisplacement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('engineDisplacement', 'http://schema.org/engineDisplacement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tripOrigin(RdfProperty[schemaorg.Place]):
    term = RdfTerm('tripOrigin', 'http://schema.org/tripOrigin', ['1.2-DRAFT'])

class programmingLanguage(RdfProperty[schemaorg.ComputerLanguage | schemaorg.Text]):
    term = RdfTerm('programmingLanguage', 'http://schema.org/programmingLanguage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class incentiveType(RdfProperty[schemaorg.IncentiveType]):
    term = RdfTerm('incentiveType', 'http://schema.org/incentiveType', [])

class holdingArchive(RdfProperty[schemaorg.ArchiveOrganization]):
    term = RdfTerm('holdingArchive', 'http://schema.org/holdingArchive', ['1.0', '1.1', '1.2-DRAFT'])

class breastfeedingWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm('breastfeedingWarning', 'http://schema.org/breastfeedingWarning', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class exchangeRateSpread(RdfProperty[schemaorg.Number | schemaorg.MonetaryAmount]):
    term = RdfTerm('exchangeRateSpread', 'http://schema.org/exchangeRateSpread', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class colorSwatch(RdfProperty[schemaorg.URL | schemaorg.ImageObject]):
    term = RdfTerm('colorSwatch', 'http://schema.org/colorSwatch', [])

class geoMidpoint(RdfProperty[schemaorg.GeoCoordinates]):
    term = RdfTerm('geoMidpoint', 'http://schema.org/geoMidpoint', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm('numberOfBeds', 'http://schema.org/numberOfBeds', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class evidenceOrigin(RdfProperty[schemaorg.Text]):
    term = RdfTerm('evidenceOrigin', 'http://schema.org/evidenceOrigin', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availableFrom(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('availableFrom', 'http://schema.org/availableFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class _yield(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm('yield', 'http://schema.org/yield', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class pageEnd(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('pageEnd', 'http://schema.org/pageEnd', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfBathroomsTotal(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('numberOfBathroomsTotal', 'http://schema.org/numberOfBathroomsTotal', ['1.0', '1.1', '1.2-DRAFT'])

class productionDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('productionDate', 'http://schema.org/productionDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publicationType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('publicationType', 'http://schema.org/publicationType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class parent(RdfProperty[schemaorg.Person]):
    term = RdfTerm('parent', 'http://schema.org/parent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accessModeSufficient(RdfProperty[schemaorg.ItemList]):
    term = RdfTerm('accessModeSufficient', 'http://schema.org/accessModeSufficient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class answerExplanation(RdfProperty[schemaorg.Comment | schemaorg.WebContent]):
    term = RdfTerm('answerExplanation', 'http://schema.org/answerExplanation', ['1.1', '1.2-DRAFT'])

class skills(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('skills', 'http://schema.org/skills', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availableService(RdfProperty[schemaorg.MedicalTest | schemaorg.MedicalTherapy | schemaorg.MedicalProcedure]):
    term = RdfTerm('availableService', 'http://schema.org/availableService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class requiredQuantity(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('requiredQuantity', 'http://schema.org/requiredQuantity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publishingPrinciples(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('publishingPrinciples', 'http://schema.org/publishingPrinciples', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contactlessPayment(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('contactlessPayment', 'http://schema.org/contactlessPayment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class album(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm('album', 'http://schema.org/album', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class applicationSubCategory(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('applicationSubCategory', 'http://schema.org/applicationSubCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class floorLimit(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('floorLimit', 'http://schema.org/floorLimit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class birthPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm('birthPlace', 'http://schema.org/birthPlace', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numConstraints(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('numConstraints', 'http://schema.org/numConstraints', ['1.0', '1.1', '1.2-DRAFT'])

class floorSize(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('floorSize', 'http://schema.org/floorSize', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class polygon(RdfProperty[schemaorg.Text]):
    term = RdfTerm('polygon', 'http://schema.org/polygon', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class suggestedAge(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('suggestedAge', 'http://schema.org/suggestedAge', ['1.2-DRAFT'])

class audienceType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('audienceType', 'http://schema.org/audienceType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gameAvailabilityType(RdfProperty[schemaorg.Text | schemaorg.GameAvailabilityEnumeration]):
    term = RdfTerm('gameAvailabilityType', 'http://schema.org/gameAvailabilityType', ['1.2-DRAFT'])

class addressRegion(RdfProperty[schemaorg.Text]):
    term = RdfTerm('addressRegion', 'http://schema.org/addressRegion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class countryOfAssembly(RdfProperty[schemaorg.Text]):
    term = RdfTerm('countryOfAssembly', 'http://schema.org/countryOfAssembly', ['1.2-DRAFT'])

class vehicleSpecialUsage(RdfProperty[schemaorg.CarUsageType | schemaorg.Text]):
    term = RdfTerm('vehicleSpecialUsage', 'http://schema.org/vehicleSpecialUsage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class seasons(RdfProperty[schemaorg.CreativeWorkSeason]):
    term = RdfTerm('seasons', 'http://schema.org/seasons', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumTotBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumTotBeds', 'http://schema.org/cvdNumTotBeds', ['1.1', '1.2-DRAFT'])

class releaseOf(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm('releaseOf', 'http://schema.org/releaseOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class itemDefectReturnLabelSource(RdfProperty[schemaorg.ReturnLabelSourceEnumeration]):
    term = RdfTerm('itemDefectReturnLabelSource', 'http://schema.org/itemDefectReturnLabelSource', ['1.2-DRAFT'])

class inLanguage(RdfProperty[schemaorg.Text | schemaorg.Language]):
    term = RdfTerm('inLanguage', 'http://schema.org/inLanguage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class abstract(RdfProperty[schemaorg.Text]):
    term = RdfTerm('abstract', 'http://schema.org/abstract', ['1.0', '1.1', '1.2-DRAFT'])

class itemListElement(RdfProperty[schemaorg.Thing | schemaorg.Text | schemaorg.ListItem]):
    term = RdfTerm('itemListElement', 'http://schema.org/itemListElement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class startTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('startTime', 'http://schema.org/startTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class associatedMediaReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm('associatedMediaReview', 'http://schema.org/associatedMediaReview', ['1.2-DRAFT'])

class eligibleRegion(RdfProperty[schemaorg.Text | schemaorg.GeoShape | schemaorg.Place]):
    term = RdfTerm('eligibleRegion', 'http://schema.org/eligibleRegion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class molecularWeight(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm('molecularWeight', 'http://schema.org/molecularWeight', ['1.2-DRAFT'])

class valueMinLength(RdfProperty[schemaorg.Number]):
    term = RdfTerm('valueMinLength', 'http://schema.org/valueMinLength', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class affectedBy(RdfProperty[schemaorg.Drug]):
    term = RdfTerm('affectedBy', 'http://schema.org/affectedBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recordingOf(RdfProperty[schemaorg.MusicComposition]):
    term = RdfTerm('recordingOf', 'http://schema.org/recordingOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availabilityStarts(RdfProperty[schemaorg.Time | schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('availabilityStarts', 'http://schema.org/availabilityStarts', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class issueNumber(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('issueNumber', 'http://schema.org/issueNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class codeSampleType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('codeSampleType', 'http://schema.org/codeSampleType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inker(RdfProperty[schemaorg.Person]):
    term = RdfTerm('inker', 'http://schema.org/inker', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoIntersects(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm('geoIntersects', 'http://schema.org/geoIntersects', ['1.0', '1.1', '1.2-DRAFT'])

class mainEntityOfPage(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('mainEntityOfPage', 'http://schema.org/mainEntityOfPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class associatedReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm('associatedReview', 'http://schema.org/associatedReview', ['1.2-DRAFT'])

class flightDistance(RdfProperty[schemaorg.Distance | schemaorg.Text]):
    term = RdfTerm('flightDistance', 'http://schema.org/flightDistance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class infectiousAgentClass(RdfProperty[schemaorg.InfectiousAgentClass]):
    term = RdfTerm('infectiousAgentClass', 'http://schema.org/infectiousAgentClass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasBioChemEntityPart(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('hasBioChemEntityPart', 'http://schema.org/hasBioChemEntityPart', ['1.2-DRAFT'])

class returnPolicyCountry(RdfProperty[schemaorg.Text | schemaorg.Country]):
    term = RdfTerm('returnPolicyCountry', 'http://schema.org/returnPolicyCountry', ['1.2-DRAFT'])

class eventSchedule(RdfProperty[schemaorg.Schedule]):
    term = RdfTerm('eventSchedule', 'http://schema.org/eventSchedule', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class countryOfOrigin(RdfProperty[schemaorg.Country]):
    term = RdfTerm('countryOfOrigin', 'http://schema.org/countryOfOrigin', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numAdults(RdfProperty[schemaorg.Integer | schemaorg.QuantitativeValue]):
    term = RdfTerm('numAdults', 'http://schema.org/numAdults', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasPOS(RdfProperty[schemaorg.Place]):
    term = RdfTerm('hasPOS', 'http://schema.org/hasPOS', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class suggestedMinAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm('suggestedMinAge', 'http://schema.org/suggestedMinAge', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class shippingLabel(RdfProperty[schemaorg.Text]):
    term = RdfTerm('shippingLabel', 'http://schema.org/shippingLabel', ['1.1', '1.2-DRAFT'])

class ratingValue(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('ratingValue', 'http://schema.org/ratingValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfBedrooms(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm('numberOfBedrooms', 'http://schema.org/numberOfBedrooms', ['1.1', '1.2-DRAFT'])

class customerRemorseReturnLabelSource(RdfProperty[schemaorg.ReturnLabelSourceEnumeration]):
    term = RdfTerm('customerRemorseReturnLabelSource', 'http://schema.org/customerRemorseReturnLabelSource', ['1.2-DRAFT'])

class webFeed(RdfProperty[schemaorg.URL | schemaorg.DataFeed]):
    term = RdfTerm('webFeed', 'http://schema.org/webFeed', ['1.0', '1.1', '1.2-DRAFT'])

class functionalClass(RdfProperty[schemaorg.MedicalEntity | schemaorg.Text]):
    term = RdfTerm('functionalClass', 'http://schema.org/functionalClass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationJurisdiction(RdfProperty[schemaorg.Text | schemaorg.AdministrativeArea]):
    term = RdfTerm('legislationJurisdiction', 'http://schema.org/legislationJurisdiction', ['1.0', '1.1', '1.2-DRAFT'])

class numItems(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('numItems', 'http://schema.org/numItems', [])

class employmentType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('employmentType', 'http://schema.org/employmentType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contentLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('contentLocation', 'http://schema.org/contentLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class speakable(RdfProperty[schemaorg.SpeakableSpecification | schemaorg.URL]):
    term = RdfTerm('speakable', 'http://schema.org/speakable', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class valueReference(RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.MeasurementTypeEnumeration | schemaorg.DefinedTerm | schemaorg.QuantitativeValue | schemaorg.Enumeration | schemaorg.StructuredValue | schemaorg.QualitativeValue]):
    term = RdfTerm('valueReference', 'http://schema.org/valueReference', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class knowsAbout(RdfProperty[schemaorg.Thing | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('knowsAbout', 'http://schema.org/knowsAbout', ['1.0', '1.1', '1.2-DRAFT'])

class urlTemplate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('urlTemplate', 'http://schema.org/urlTemplate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ownedFrom(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('ownedFrom', 'http://schema.org/ownedFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class endorsers(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('endorsers', 'http://schema.org/endorsers', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class actionStatus(RdfProperty[schemaorg.ActionStatusType]):
    term = RdfTerm('actionStatus', 'http://schema.org/actionStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class firstPerformance(RdfProperty[schemaorg.Event]):
    term = RdfTerm('firstPerformance', 'http://schema.org/firstPerformance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class experienceInPlaceOfEducation(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('experienceInPlaceOfEducation', 'http://schema.org/experienceInPlaceOfEducation', ['1.2-DRAFT'])

class incomeLimit(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Text]):
    term = RdfTerm('incomeLimit', 'http://schema.org/incomeLimit', [])

class liveBlogUpdate(RdfProperty[schemaorg.BlogPosting]):
    term = RdfTerm('liveBlogUpdate', 'http://schema.org/liveBlogUpdate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gameEdition(RdfProperty[schemaorg.Text]):
    term = RdfTerm('gameEdition', 'http://schema.org/gameEdition', ['1.2-DRAFT'])

class dateModified(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('dateModified', 'http://schema.org/dateModified', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class billingIncrement(RdfProperty[schemaorg.Number]):
    term = RdfTerm('billingIncrement', 'http://schema.org/billingIncrement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class stepValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm('stepValue', 'http://schema.org/stepValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class monoisotopicMolecularWeight(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm('monoisotopicMolecularWeight', 'http://schema.org/monoisotopicMolecularWeight', ['1.2-DRAFT'])

class hasTierBenefit(RdfProperty[schemaorg.TierBenefitEnumeration]):
    term = RdfTerm('hasTierBenefit', 'http://schema.org/hasTierBenefit', [])

class departureTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('departureTime', 'http://schema.org/departureTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sku(RdfProperty[schemaorg.Text]):
    term = RdfTerm('sku', 'http://schema.org/sku', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationEnsuresImplementationOf(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationEnsuresImplementationOf', 'http://schema.org/legislationEnsuresImplementationOf', [])

class studySubject(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm('studySubject', 'http://schema.org/studySubject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class containsPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm('containsPlace', 'http://schema.org/containsPlace', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class telephone(RdfProperty[schemaorg.Text]):
    term = RdfTerm('telephone', 'http://schema.org/telephone', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasDigitalDocumentPermission(RdfProperty[schemaorg.DigitalDocumentPermission]):
    term = RdfTerm('hasDigitalDocumentPermission', 'http://schema.org/hasDigitalDocumentPermission', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class purchasePriceLimit(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('purchasePriceLimit', 'http://schema.org/purchasePriceLimit', [])

class usageInfo(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('usageInfo', 'http://schema.org/usageInfo', ['1.1', '1.2-DRAFT'])

class availableLanguage(RdfProperty[schemaorg.Text | schemaorg.Language]):
    term = RdfTerm('availableLanguage', 'http://schema.org/availableLanguage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class artist(RdfProperty[schemaorg.Person]):
    term = RdfTerm('artist', 'http://schema.org/artist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoOverlaps(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm('geoOverlaps', 'http://schema.org/geoOverlaps', ['1.0', '1.1', '1.2-DRAFT'])

class hasCategoryCode(RdfProperty[schemaorg.CategoryCode]):
    term = RdfTerm('hasCategoryCode', 'http://schema.org/hasCategoryCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class priceSpecification(RdfProperty[schemaorg.PriceSpecification]):
    term = RdfTerm('priceSpecification', 'http://schema.org/priceSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mapType(RdfProperty[schemaorg.MapCategoryType]):
    term = RdfTerm('mapType', 'http://schema.org/mapType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class regionDrained(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem]):
    term = RdfTerm('regionDrained', 'http://schema.org/regionDrained', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class originatesFrom(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm('originatesFrom', 'http://schema.org/originatesFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class workHours(RdfProperty[schemaorg.Text]):
    term = RdfTerm('workHours', 'http://schema.org/workHours', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class incentivizedItem(RdfProperty[schemaorg.DefinedTerm | schemaorg.Product]):
    term = RdfTerm('incentivizedItem', 'http://schema.org/incentivizedItem', [])

class checkoutTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('checkoutTime', 'http://schema.org/checkoutTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class jurisdiction(RdfProperty[schemaorg.AdministrativeArea | schemaorg.Text]):
    term = RdfTerm('jurisdiction', 'http://schema.org/jurisdiction', ['1.1', '1.2-DRAFT'])

class attendees(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('attendees', 'http://schema.org/attendees', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class eligibleCustomerType(RdfProperty[schemaorg.BusinessEntityType]):
    term = RdfTerm('eligibleCustomerType', 'http://schema.org/eligibleCustomerType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class departureStation(RdfProperty[schemaorg.TrainStation]):
    term = RdfTerm('departureStation', 'http://schema.org/departureStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class datePosted(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('datePosted', 'http://schema.org/datePosted', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vendor(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('vendor', 'http://schema.org/vendor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class warrantyPromise(RdfProperty[schemaorg.WarrantyPromise]):
    term = RdfTerm('warrantyPromise', 'http://schema.org/warrantyPromise', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfForwardGears(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm('numberOfForwardGears', 'http://schema.org/numberOfForwardGears', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fuelEfficiency(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('fuelEfficiency', 'http://schema.org/fuelEfficiency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class letterer(RdfProperty[schemaorg.Person]):
    term = RdfTerm('letterer', 'http://schema.org/letterer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class issuedThrough(RdfProperty[schemaorg.Service]):
    term = RdfTerm('issuedThrough', 'http://schema.org/issuedThrough', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dosageForm(RdfProperty[schemaorg.Text]):
    term = RdfTerm('dosageForm', 'http://schema.org/dosageForm', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class scheduledPaymentDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('scheduledPaymentDate', 'http://schema.org/scheduledPaymentDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class entertainmentBusiness(RdfProperty[schemaorg.EntertainmentBusiness]):
    term = RdfTerm('entertainmentBusiness', 'http://schema.org/entertainmentBusiness', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class season(RdfProperty[schemaorg.URL | schemaorg.CreativeWorkSeason]):
    term = RdfTerm('season', 'http://schema.org/season', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class durationOfWarranty(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('durationOfWarranty', 'http://schema.org/durationOfWarranty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class includesAttraction(RdfProperty[schemaorg.TouristAttraction]):
    term = RdfTerm('includesAttraction', 'http://schema.org/includesAttraction', ['1.0', '1.1', '1.2-DRAFT'])

class vehicleModelDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('vehicleModelDate', 'http://schema.org/vehicleModelDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class structuralClass(RdfProperty[schemaorg.Text]):
    term = RdfTerm('structuralClass', 'http://schema.org/structuralClass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasMerchantReturnPolicy(RdfProperty[schemaorg.MerchantReturnPolicy]):
    term = RdfTerm('hasMerchantReturnPolicy', 'http://schema.org/hasMerchantReturnPolicy', ['1.1', '1.2-DRAFT'])

class maxPrice(RdfProperty[schemaorg.Number]):
    term = RdfTerm('maxPrice', 'http://schema.org/maxPrice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class colorist(RdfProperty[schemaorg.Person]):
    term = RdfTerm('colorist', 'http://schema.org/colorist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class shippingRate(RdfProperty[schemaorg.ShippingRateSettings | schemaorg.MonetaryAmount]):
    term = RdfTerm('shippingRate', 'http://schema.org/shippingRate', ['1.1', '1.2-DRAFT'])

class procedure(RdfProperty[schemaorg.Text]):
    term = RdfTerm('procedure', 'http://schema.org/procedure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdFacilityCounty(RdfProperty[schemaorg.Text]):
    term = RdfTerm('cvdFacilityCounty', 'http://schema.org/cvdFacilityCounty', ['1.1', '1.2-DRAFT'])

class expectedPrognosis(RdfProperty[schemaorg.Text]):
    term = RdfTerm('expectedPrognosis', 'http://schema.org/expectedPrognosis', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class validForMemberTier(RdfProperty[schemaorg.MemberProgramTier]):
    term = RdfTerm('validForMemberTier', 'http://schema.org/validForMemberTier', [])

class borrower(RdfProperty[schemaorg.Person]):
    term = RdfTerm('borrower', 'http://schema.org/borrower', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availability(RdfProperty[schemaorg.ItemAvailability]):
    term = RdfTerm('availability', 'http://schema.org/availability', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class servingSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm('servingSize', 'http://schema.org/servingSize', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sdDatePublished(RdfProperty[schemaorg.Date]):
    term = RdfTerm('sdDatePublished', 'http://schema.org/sdDatePublished', ['1.0', '1.1', '1.2-DRAFT'])

class dateline(RdfProperty[schemaorg.Text]):
    term = RdfTerm('dateline', 'http://schema.org/dateline', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arrivalPlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm('arrivalPlatform', 'http://schema.org/arrivalPlatform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class courseMode(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('courseMode', 'http://schema.org/courseMode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class object(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('object', 'http://schema.org/object', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class highPrice(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm('highPrice', 'http://schema.org/highPrice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hospitalAffiliation(RdfProperty[schemaorg.Hospital]):
    term = RdfTerm('hospitalAffiliation', 'http://schema.org/hospitalAffiliation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class specialty(RdfProperty[schemaorg.Specialty]):
    term = RdfTerm('specialty', 'http://schema.org/specialty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class measurementDenominator(RdfProperty[schemaorg.StatisticalVariable]):
    term = RdfTerm('measurementDenominator', 'http://schema.org/measurementDenominator', ['1.2-DRAFT'])

class imagingTechnique(RdfProperty[schemaorg.MedicalImagingTechnique]):
    term = RdfTerm('imagingTechnique', 'http://schema.org/imagingTechnique', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class includedRiskFactor(RdfProperty[schemaorg.MedicalRiskFactor]):
    term = RdfTerm('includedRiskFactor', 'http://schema.org/includedRiskFactor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastFrequency(RdfProperty[schemaorg.Text | schemaorg.BroadcastFrequencySpecification]):
    term = RdfTerm('broadcastFrequency', 'http://schema.org/broadcastFrequency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isAvailableGenerically(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isAvailableGenerically', 'http://schema.org/isAvailableGenerically', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfFullBathrooms(RdfProperty[schemaorg.Number]):
    term = RdfTerm('numberOfFullBathrooms', 'http://schema.org/numberOfFullBathrooms', ['1.0', '1.1', '1.2-DRAFT'])

class percentile25(RdfProperty[schemaorg.Number]):
    term = RdfTerm('percentile25', 'http://schema.org/percentile25', ['1.0', '1.1', '1.2-DRAFT'])

class subtitleLanguage(RdfProperty[schemaorg.Text | schemaorg.Language]):
    term = RdfTerm('subtitleLanguage', 'http://schema.org/subtitleLanguage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availableChannel(RdfProperty[schemaorg.ServiceChannel]):
    term = RdfTerm('availableChannel', 'http://schema.org/availableChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class iswcCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('iswcCode', 'http://schema.org/iswcCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class encodesBioChemEntity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('encodesBioChemEntity', 'http://schema.org/encodesBioChemEntity', ['1.2-DRAFT'])

class inventoryLevel(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('inventoryLevel', 'http://schema.org/inventoryLevel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accommodationFloorPlan(RdfProperty[schemaorg.FloorPlan]):
    term = RdfTerm('accommodationFloorPlan', 'http://schema.org/accommodationFloorPlan', ['1.1', '1.2-DRAFT'])

class hasDeliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm('hasDeliveryMethod', 'http://schema.org/hasDeliveryMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class servicePhone(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm('servicePhone', 'http://schema.org/servicePhone', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class trainNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('trainNumber', 'http://schema.org/trainNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfEmployees(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('numberOfEmployees', 'http://schema.org/numberOfEmployees', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthcareReportingData(RdfProperty[schemaorg.CDCPMDRecord | schemaorg.Dataset]):
    term = RdfTerm('healthcareReportingData', 'http://schema.org/healthcareReportingData', ['1.1', '1.2-DRAFT'])

class acrissCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('acrissCode', 'http://schema.org/acrissCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class applicantLocationRequirements(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm('applicantLocationRequirements', 'http://schema.org/applicantLocationRequirements', ['1.0', '1.1', '1.2-DRAFT'])

class archiveHeld(RdfProperty[schemaorg.ArchiveComponent]):
    term = RdfTerm('archiveHeld', 'http://schema.org/archiveHeld', ['1.0', '1.1', '1.2-DRAFT'])

class paymentStatus(RdfProperty[schemaorg.PaymentStatusType | schemaorg.Text]):
    term = RdfTerm('paymentStatus', 'http://schema.org/paymentStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class occupationLocation(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm('occupationLocation', 'http://schema.org/occupationLocation', ['1.0', '1.1', '1.2-DRAFT'])

class includesHealthPlanNetwork(RdfProperty[schemaorg.HealthPlanNetwork]):
    term = RdfTerm('includesHealthPlanNetwork', 'http://schema.org/includesHealthPlanNetwork', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class itemLocation(RdfProperty[schemaorg.Place | schemaorg.PostalAddress | schemaorg.Text]):
    term = RdfTerm('itemLocation', 'http://schema.org/itemLocation', ['1.0', '1.1', '1.2-DRAFT'])

class clipNumber(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('clipNumber', 'http://schema.org/clipNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class eligibleDuration(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('eligibleDuration', 'http://schema.org/eligibleDuration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class observationDate(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('observationDate', 'http://schema.org/observationDate', ['1.0', '1.1', '1.2-DRAFT'])

class tocContinuation(RdfProperty[schemaorg.HyperTocEntry]):
    term = RdfTerm('tocContinuation', 'http://schema.org/tocContinuation', ['1.2-DRAFT'])

class archivedAt(RdfProperty[schemaorg.URL | schemaorg.WebPage]):
    term = RdfTerm('archivedAt', 'http://schema.org/archivedAt', ['1.2-DRAFT'])

class weight(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Mass]):
    term = RdfTerm('weight', 'http://schema.org/weight', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class byMonthWeek(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('byMonthWeek', 'http://schema.org/byMonthWeek', ['1.1', '1.2-DRAFT'])

class inDefinedTermSet(RdfProperty[schemaorg.DefinedTermSet | schemaorg.URL]):
    term = RdfTerm('inDefinedTermSet', 'http://schema.org/inDefinedTermSet', ['1.0', '1.1', '1.2-DRAFT'])

class includedInHealthInsurancePlan(RdfProperty[schemaorg.HealthInsurancePlan]):
    term = RdfTerm('includedInHealthInsurancePlan', 'http://schema.org/includedInHealthInsurancePlan', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class byDay(RdfProperty[schemaorg.Text | schemaorg.DayOfWeek]):
    term = RdfTerm('byDay', 'http://schema.org/byDay', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class line(RdfProperty[schemaorg.Text]):
    term = RdfTerm('line', 'http://schema.org/line', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vehicleEngine(RdfProperty[schemaorg.EngineSpecification]):
    term = RdfTerm('vehicleEngine', 'http://schema.org/vehicleEngine', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class branchOf(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('branchOf', 'http://schema.org/branchOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class expectedArrivalUntil(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('expectedArrivalUntil', 'http://schema.org/expectedArrivalUntil', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class originalMediaLink(RdfProperty[schemaorg.MediaObject | schemaorg.URL | schemaorg.WebPage]):
    term = RdfTerm('originalMediaLink', 'http://schema.org/originalMediaLink', ['1.2-DRAFT'])

class printColumn(RdfProperty[schemaorg.Text]):
    term = RdfTerm('printColumn', 'http://schema.org/printColumn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class trainingSalary(RdfProperty[schemaorg.MonetaryAmountDistribution]):
    term = RdfTerm('trainingSalary', 'http://schema.org/trainingSalary', ['1.0', '1.1', '1.2-DRAFT'])

class typeOfBed(RdfProperty[schemaorg.BedType | schemaorg.Text]):
    term = RdfTerm('typeOfBed', 'http://schema.org/typeOfBed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class percentile75(RdfProperty[schemaorg.Number]):
    term = RdfTerm('percentile75', 'http://schema.org/percentile75', ['1.0', '1.1', '1.2-DRAFT'])

class credentialCategory(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('credentialCategory', 'http://schema.org/credentialCategory', ['1.0', '1.1', '1.2-DRAFT'])

class eventStatus(RdfProperty[schemaorg.EventStatusType]):
    term = RdfTerm('eventStatus', 'http://schema.org/eventStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class medicalSpecialty(RdfProperty[schemaorg.MedicalSpecialty]):
    term = RdfTerm('medicalSpecialty', 'http://schema.org/medicalSpecialty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class returnShippingFeesAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('returnShippingFeesAmount', 'http://schema.org/returnShippingFeesAmount', ['1.2-DRAFT'])

class healthPlanCostSharing(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('healthPlanCostSharing', 'http://schema.org/healthPlanCostSharing', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class customerRemorseReturnShippingFeesAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('customerRemorseReturnShippingFeesAmount', 'http://schema.org/customerRemorseReturnShippingFeesAmount', ['1.2-DRAFT'])

class interactionCount(RdfProperty[Identifier]):
    term = RdfTerm('interactionCount', 'http://schema.org/interactionCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class billingAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm('billingAddress', 'http://schema.org/billingAddress', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class countriesNotSupported(RdfProperty[schemaorg.Text]):
    term = RdfTerm('countriesNotSupported', 'http://schema.org/countriesNotSupported', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class shippingDetails(RdfProperty[schemaorg.OfferShippingDetails]):
    term = RdfTerm('shippingDetails', 'http://schema.org/shippingDetails', ['1.1', '1.2-DRAFT'])

class employees(RdfProperty[schemaorg.Person]):
    term = RdfTerm('employees', 'http://schema.org/employees', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mpn(RdfProperty[schemaorg.Text]):
    term = RdfTerm('mpn', 'http://schema.org/mpn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lesser(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm('lesser', 'http://schema.org/lesser', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class byMonth(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('byMonth', 'http://schema.org/byMonth', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class loanRepaymentForm(RdfProperty[schemaorg.RepaymentSpecification]):
    term = RdfTerm('loanRepaymentForm', 'http://schema.org/loanRepaymentForm', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasGS1DigitalLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm('hasGS1DigitalLink', 'http://schema.org/hasGS1DigitalLink', [])

class ownershipFundingInfo(RdfProperty[schemaorg.URL | schemaorg.AboutPage | schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('ownershipFundingInfo', 'http://schema.org/ownershipFundingInfo', ['1.0', '1.1', '1.2-DRAFT'])

class mediaAuthenticityCategory(RdfProperty[schemaorg.MediaManipulationRatingEnumeration]):
    term = RdfTerm('mediaAuthenticityCategory', 'http://schema.org/mediaAuthenticityCategory', ['1.1', '1.2-DRAFT'])

class unsaturatedFatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('unsaturatedFatContent', 'http://schema.org/unsaturatedFatContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lastReviewed(RdfProperty[schemaorg.Date]):
    term = RdfTerm('lastReviewed', 'http://schema.org/lastReviewed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class workTranslation(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('workTranslation', 'http://schema.org/workTranslation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfTrip(RdfProperty[schemaorg.Trip]):
    term = RdfTerm('partOfTrip', 'http://schema.org/partOfTrip', ['1.0', '1.1', '1.2-DRAFT'])

class numberOfDoors(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('numberOfDoors', 'http://schema.org/numberOfDoors', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class preOp(RdfProperty[schemaorg.Text]):
    term = RdfTerm('preOp', 'http://schema.org/preOp', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class backstory(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm('backstory', 'http://schema.org/backstory', ['1.0', '1.1', '1.2-DRAFT'])

class verificationFactCheckingPolicy(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm('verificationFactCheckingPolicy', 'http://schema.org/verificationFactCheckingPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class url(RdfProperty[schemaorg.URL]):
    term = RdfTerm('url', 'http://schema.org/url', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class error(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('error', 'http://schema.org/error', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sdLicense(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('sdLicense', 'http://schema.org/sdLicense', ['1.0', '1.1', '1.2-DRAFT'])

class legislationRepeals(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationRepeals', 'http://schema.org/legislationRepeals', [])

class catalog(RdfProperty[schemaorg.DataCatalog]):
    term = RdfTerm('catalog', 'http://schema.org/catalog', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class embeddedTextCaption(RdfProperty[schemaorg.Text]):
    term = RdfTerm('embeddedTextCaption', 'http://schema.org/embeddedTextCaption', ['1.2-DRAFT'])

class educationalAlignment(RdfProperty[schemaorg.AlignmentObject]):
    term = RdfTerm('educationalAlignment', 'http://schema.org/educationalAlignment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class drainsTo(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm('drainsTo', 'http://schema.org/drainsTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class editor(RdfProperty[schemaorg.Person]):
    term = RdfTerm('editor', 'http://schema.org/editor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class uploadDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('uploadDate', 'http://schema.org/uploadDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gameItem(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('gameItem', 'http://schema.org/gameItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationConsolidates(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationConsolidates', 'http://schema.org/legislationConsolidates', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class interactionType(RdfProperty[schemaorg.Action]):
    term = RdfTerm('interactionType', 'http://schema.org/interactionType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class securityClearanceRequirement(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('securityClearanceRequirement', 'http://schema.org/securityClearanceRequirement', ['1.1', '1.2-DRAFT'])

class salaryUponCompletion(RdfProperty[schemaorg.MonetaryAmountDistribution]):
    term = RdfTerm('salaryUponCompletion', 'http://schema.org/salaryUponCompletion', ['1.0', '1.1', '1.2-DRAFT'])

class hoursAvailable(RdfProperty[schemaorg.OpeningHoursSpecification]):
    term = RdfTerm('hoursAvailable', 'http://schema.org/hoursAvailable', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfPreviousOwners(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('numberOfPreviousOwners', 'http://schema.org/numberOfPreviousOwners', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legalStatus(RdfProperty[schemaorg.Text | schemaorg.DrugLegalStatus | schemaorg.MedicalEnumeration]):
    term = RdfTerm('legalStatus', 'http://schema.org/legalStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class downloadUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('downloadUrl', 'http://schema.org/downloadUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class valueName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('valueName', 'http://schema.org/valueName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfSystem(RdfProperty[schemaorg.AnatomicalSystem]):
    term = RdfTerm('partOfSystem', 'http://schema.org/partOfSystem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inCodeSet(RdfProperty[schemaorg.CategoryCodeSet | schemaorg.URL]):
    term = RdfTerm('inCodeSet', 'http://schema.org/inCodeSet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class license(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('license', 'http://schema.org/license', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class businessDays(RdfProperty[schemaorg.OpeningHoursSpecification | schemaorg.DayOfWeek]):
    term = RdfTerm('businessDays', 'http://schema.org/businessDays', ['1.1', '1.2-DRAFT'])

class ccRecipient(RdfProperty[schemaorg.Organization | schemaorg.ContactPoint | schemaorg.Person]):
    term = RdfTerm('ccRecipient', 'http://schema.org/ccRecipient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class permissions(RdfProperty[schemaorg.Text]):
    term = RdfTerm('permissions', 'http://schema.org/permissions', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broker(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('broker', 'http://schema.org/broker', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contactType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('contactType', 'http://schema.org/contactType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recognizedBy(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('recognizedBy', 'http://schema.org/recognizedBy', ['1.0', '1.1', '1.2-DRAFT'])

class greater(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm('greater', 'http://schema.org/greater', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class opponent(RdfProperty[schemaorg.Person]):
    term = RdfTerm('opponent', 'http://schema.org/opponent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class icaoCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('icaoCode', 'http://schema.org/icaoCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class associatedAnatomy(RdfProperty[schemaorg.SuperficialAnatomy | schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem]):
    term = RdfTerm('associatedAnatomy', 'http://schema.org/associatedAnatomy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class playMode(RdfProperty[schemaorg.GamePlayMode]):
    term = RdfTerm('playMode', 'http://schema.org/playMode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tributary(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('tributary', 'http://schema.org/tributary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tool(RdfProperty[schemaorg.HowToTool | schemaorg.Text]):
    term = RdfTerm('tool', 'http://schema.org/tool', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class taxonomicRange(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Taxon]):
    term = RdfTerm('taxonomicRange', 'http://schema.org/taxonomicRange', ['1.2-DRAFT'])

class weightTotal(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('weightTotal', 'http://schema.org/weightTotal', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class actors(RdfProperty[schemaorg.Person]):
    term = RdfTerm('actors', 'http://schema.org/actors', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class maximumPhysicalAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('maximumPhysicalAttendeeCapacity', 'http://schema.org/maximumPhysicalAttendeeCapacity', ['1.1', '1.2-DRAFT'])

class grantee(RdfProperty[schemaorg.Audience | schemaorg.ContactPoint | schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('grantee', 'http://schema.org/grantee', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class marginOfError(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('marginOfError', 'http://schema.org/marginOfError', ['1.0', '1.1', '1.2-DRAFT'])

class followup(RdfProperty[schemaorg.Text]):
    term = RdfTerm('followup', 'http://schema.org/followup', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class connectedTo(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('connectedTo', 'http://schema.org/connectedTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class foundingLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('foundingLocation', 'http://schema.org/foundingLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class acquiredFrom(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('acquiredFrom', 'http://schema.org/acquiredFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class estimatedFlightDuration(RdfProperty[schemaorg.Duration | schemaorg.Text]):
    term = RdfTerm('estimatedFlightDuration', 'http://schema.org/estimatedFlightDuration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class merchant(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('merchant', 'http://schema.org/merchant', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class game(RdfProperty[schemaorg.VideoGame]):
    term = RdfTerm('game', 'http://schema.org/game', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfOrder(RdfProperty[schemaorg.Order]):
    term = RdfTerm('partOfOrder', 'http://schema.org/partOfOrder', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class maintainer(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('maintainer', 'http://schema.org/maintainer', ['1.1', '1.2-DRAFT'])

class serialNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('serialNumber', 'http://schema.org/serialNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfAxles(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm('numberOfAxles', 'http://schema.org/numberOfAxles', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class median(RdfProperty[schemaorg.Number]):
    term = RdfTerm('median', 'http://schema.org/median', ['1.0', '1.1', '1.2-DRAFT'])

class caption(RdfProperty[schemaorg.MediaObject | schemaorg.Text]):
    term = RdfTerm('caption', 'http://schema.org/caption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class application(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm('application', 'http://schema.org/application', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class serviceArea(RdfProperty[schemaorg.GeoShape | schemaorg.AdministrativeArea | schemaorg.Place]):
    term = RdfTerm('serviceArea', 'http://schema.org/serviceArea', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dateDeleted(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('dateDeleted', 'http://schema.org/dateDeleted', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class drugUnit(RdfProperty[schemaorg.Text]):
    term = RdfTerm('drugUnit', 'http://schema.org/drugUnit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class programPrerequisites(RdfProperty[schemaorg.EducationalOccupationalCredential | schemaorg.AlignmentObject | schemaorg.Text | schemaorg.Course]):
    term = RdfTerm('programPrerequisites', 'http://schema.org/programPrerequisites', ['1.0', '1.1', '1.2-DRAFT'])

class childMaxAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm('childMaxAge', 'http://schema.org/childMaxAge', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class featureList(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('featureList', 'http://schema.org/featureList', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class courseSchedule(RdfProperty[schemaorg.Schedule]):
    term = RdfTerm('courseSchedule', 'http://schema.org/courseSchedule', ['1.2-DRAFT'])

class suggestedGender(RdfProperty[schemaorg.Text | schemaorg.GenderType]):
    term = RdfTerm('suggestedGender', 'http://schema.org/suggestedGender', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sourceOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('sourceOrganization', 'http://schema.org/sourceOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasTierRequirement(RdfProperty[schemaorg.Text | schemaorg.MonetaryAmount | schemaorg.CreditCard | schemaorg.UnitPriceSpecification]):
    term = RdfTerm('hasTierRequirement', 'http://schema.org/hasTierRequirement', [])

class paymentDueDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('paymentDueDate', 'http://schema.org/paymentDueDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class model(RdfProperty[schemaorg.Text | schemaorg.ProductModel]):
    term = RdfTerm('model', 'http://schema.org/model', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contraindication(RdfProperty[schemaorg.MedicalContraindication | schemaorg.Text]):
    term = RdfTerm('contraindication', 'http://schema.org/contraindication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isRelatedTo(RdfProperty[schemaorg.Product | schemaorg.Service]):
    term = RdfTerm('isRelatedTo', 'http://schema.org/isRelatedTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class risks(RdfProperty[schemaorg.Text]):
    term = RdfTerm('risks', 'http://schema.org/risks', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class trailer(RdfProperty[schemaorg.VideoObject]):
    term = RdfTerm('trailer', 'http://schema.org/trailer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class softwareVersion(RdfProperty[schemaorg.Text]):
    term = RdfTerm('softwareVersion', 'http://schema.org/softwareVersion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recommendedIntake(RdfProperty[schemaorg.RecommendedDoseSchedule]):
    term = RdfTerm('recommendedIntake', 'http://schema.org/recommendedIntake', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sportsTeam(RdfProperty[schemaorg.SportsTeam]):
    term = RdfTerm('sportsTeam', 'http://schema.org/sportsTeam', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class evidenceLevel(RdfProperty[schemaorg.MedicalEvidenceLevel]):
    term = RdfTerm('evidenceLevel', 'http://schema.org/evidenceLevel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contentType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('contentType', 'http://schema.org/contentType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class instructor(RdfProperty[schemaorg.Person]):
    term = RdfTerm('instructor', 'http://schema.org/instructor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class educationalFramework(RdfProperty[schemaorg.Text]):
    term = RdfTerm('educationalFramework', 'http://schema.org/educationalFramework', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reviews(RdfProperty[schemaorg.Review]):
    term = RdfTerm('reviews', 'http://schema.org/reviews', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accessibilityHazard(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accessibilityHazard', 'http://schema.org/accessibilityHazard', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partySize(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Integer]):
    term = RdfTerm('partySize', 'http://schema.org/partySize', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class executableLibraryName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('executableLibraryName', 'http://schema.org/executableLibraryName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class seeks(RdfProperty[schemaorg.Demand]):
    term = RdfTerm('seeks', 'http://schema.org/seeks', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class potentialUse(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm('potentialUse', 'http://schema.org/potentialUse', ['1.2-DRAFT'])

class nonprofitStatus(RdfProperty[schemaorg.NonprofitType]):
    term = RdfTerm('nonprofitStatus', 'http://schema.org/nonprofitStatus', ['1.1', '1.2-DRAFT'])

class courseWorkload(RdfProperty[schemaorg.Text]):
    term = RdfTerm('courseWorkload', 'http://schema.org/courseWorkload', ['1.0', '1.1', '1.2-DRAFT'])

class endOffset(RdfProperty[schemaorg.Number | schemaorg.HyperTocEntry]):
    term = RdfTerm('endOffset', 'http://schema.org/endOffset', ['1.0', '1.1', '1.2-DRAFT'])

class requiresSubscription(RdfProperty[schemaorg.Boolean | schemaorg.MediaSubscription]):
    term = RdfTerm('requiresSubscription', 'http://schema.org/requiresSubscription', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class parentOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('parentOrganization', 'http://schema.org/parentOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class leiCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('leiCode', 'http://schema.org/leiCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class returnFees(RdfProperty[schemaorg.ReturnFeesEnumeration]):
    term = RdfTerm('returnFees', 'http://schema.org/returnFees', ['1.0', '1.1', '1.2-DRAFT'])

class artMedium(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('artMedium', 'http://schema.org/artMedium', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfAccommodationUnits(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('numberOfAccommodationUnits', 'http://schema.org/numberOfAccommodationUnits', ['1.1', '1.2-DRAFT'])

class associatedPathophysiology(RdfProperty[schemaorg.Text]):
    term = RdfTerm('associatedPathophysiology', 'http://schema.org/associatedPathophysiology', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gtin12(RdfProperty[schemaorg.Text]):
    term = RdfTerm('gtin12', 'http://schema.org/gtin12', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isAcceptingNewPatients(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isAcceptingNewPatients', 'http://schema.org/isAcceptingNewPatients', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tocEntry(RdfProperty[schemaorg.HyperTocEntry]):
    term = RdfTerm('tocEntry', 'http://schema.org/tocEntry', ['1.2-DRAFT'])

class step(RdfProperty[schemaorg.CreativeWork | schemaorg.Text | schemaorg.HowToSection | schemaorg.HowToStep]):
    term = RdfTerm('step', 'http://schema.org/step', ['1.0', '1.1', '1.2-DRAFT'])

class codeValue(RdfProperty[schemaorg.Text]):
    term = RdfTerm('codeValue', 'http://schema.org/codeValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderValue(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('orderValue', 'http://schema.org/orderValue', [])

class payload(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('payload', 'http://schema.org/payload', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class additionalName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('additionalName', 'http://schema.org/additionalName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasCredential(RdfProperty[schemaorg.EducationalOccupationalCredential]):
    term = RdfTerm('hasCredential', 'http://schema.org/hasCredential', ['1.0', '1.1', '1.2-DRAFT'])

class deathDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('deathDate', 'http://schema.org/deathDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class populationType(RdfProperty[schemaorg.Class]):
    term = RdfTerm('populationType', 'http://schema.org/populationType', ['1.0', '1.1', '1.2-DRAFT'])

class mealService(RdfProperty[schemaorg.Text]):
    term = RdfTerm('mealService', 'http://schema.org/mealService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inStoreReturnsOffered(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('inStoreReturnsOffered', 'http://schema.org/inStoreReturnsOffered', ['1.0', '1.1', '1.2-DRAFT'])

class workExample(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('workExample', 'http://schema.org/workExample', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class shippingConditions(RdfProperty[schemaorg.ShippingConditions]):
    term = RdfTerm('shippingConditions', 'http://schema.org/shippingConditions', [])

class composer(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('composer', 'http://schema.org/composer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class spokenByCharacter(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('spokenByCharacter', 'http://schema.org/spokenByCharacter', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class schoolClosuresInfo(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm('schoolClosuresInfo', 'http://schema.org/schoolClosuresInfo', ['1.1', '1.2-DRAFT'])

class disambiguatingDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm('disambiguatingDescription', 'http://schema.org/disambiguatingDescription', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class episodeNumber(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('episodeNumber', 'http://schema.org/episodeNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class supersededBy(RdfProperty[schemaorg.Class | schemaorg.Property | schemaorg.Enumeration]):
    term = RdfTerm('supersededBy', 'http://schema.org/supersededBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class founders(RdfProperty[schemaorg.Person]):
    term = RdfTerm('founders', 'http://schema.org/founders', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class pattern(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('pattern', 'http://schema.org/pattern', ['1.1', '1.2-DRAFT'])

class commentText(RdfProperty[schemaorg.Text]):
    term = RdfTerm('commentText', 'http://schema.org/commentText', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumICUBedsOcc(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumICUBedsOcc', 'http://schema.org/cvdNumICUBedsOcc', ['1.1', '1.2-DRAFT'])

class sodiumContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('sodiumContent', 'http://schema.org/sodiumContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class videoQuality(RdfProperty[schemaorg.Text]):
    term = RdfTerm('videoQuality', 'http://schema.org/videoQuality', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class validFor(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('validFor', 'http://schema.org/validFor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inBroadcastLineup(RdfProperty[schemaorg.CableOrSatelliteService]):
    term = RdfTerm('inBroadcastLineup', 'http://schema.org/inBroadcastLineup', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastTimezone(RdfProperty[schemaorg.Text]):
    term = RdfTerm('broadcastTimezone', 'http://schema.org/broadcastTimezone', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class characterName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('characterName', 'http://schema.org/characterName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasMenuSection(RdfProperty[schemaorg.MenuSection]):
    term = RdfTerm('hasMenuSection', 'http://schema.org/hasMenuSection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accessCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accessCode', 'http://schema.org/accessCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class requiredMinAge(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('requiredMinAge', 'http://schema.org/requiredMinAge', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class offers(RdfProperty[schemaorg.Offer | schemaorg.Demand]):
    term = RdfTerm('offers', 'http://schema.org/offers', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class equal(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm('equal', 'http://schema.org/equal', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoCrosses(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm('geoCrosses', 'http://schema.org/geoCrosses', ['1.0', '1.1', '1.2-DRAFT'])

class diseaseSpreadStatistics(RdfProperty[schemaorg.Dataset | schemaorg.URL | schemaorg.Observation | schemaorg.WebContent]):
    term = RdfTerm('diseaseSpreadStatistics', 'http://schema.org/diseaseSpreadStatistics', ['1.1', '1.2-DRAFT'])

class closes(RdfProperty[schemaorg.Time]):
    term = RdfTerm('closes', 'http://schema.org/closes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasPart(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('hasPart', 'http://schema.org/hasPart', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class departureBusStop(RdfProperty[schemaorg.BusStation | schemaorg.BusStop]):
    term = RdfTerm('departureBusStop', 'http://schema.org/departureBusStop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recordedAs(RdfProperty[schemaorg.MusicRecording]):
    term = RdfTerm('recordedAs', 'http://schema.org/recordedAs', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class overdosage(RdfProperty[schemaorg.Text]):
    term = RdfTerm('overdosage', 'http://schema.org/overdosage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cargoVolume(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('cargoVolume', 'http://schema.org/cargoVolume', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class keywords(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('keywords', 'http://schema.org/keywords', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class exampleOfWork(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('exampleOfWork', 'http://schema.org/exampleOfWork', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contactOption(RdfProperty[schemaorg.ContactPointOption]):
    term = RdfTerm('contactOption', 'http://schema.org/contactOption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class copyrightNotice(RdfProperty[schemaorg.Text]):
    term = RdfTerm('copyrightNotice', 'http://schema.org/copyrightNotice', ['1.2-DRAFT'])

class musicBy(RdfProperty[schemaorg.Person | schemaorg.MusicGroup]):
    term = RdfTerm('musicBy', 'http://schema.org/musicBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arrivalBusStop(RdfProperty[schemaorg.BusStation | schemaorg.BusStop]):
    term = RdfTerm('arrivalBusStop', 'http://schema.org/arrivalBusStop', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isLiveBroadcast(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isLiveBroadcast', 'http://schema.org/isLiveBroadcast', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fileSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm('fileSize', 'http://schema.org/fileSize', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class encodingFormat(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('encodingFormat', 'http://schema.org/encodingFormat', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasDriveThroughService(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('hasDriveThroughService', 'http://schema.org/hasDriveThroughService', ['1.1', '1.2-DRAFT'])

class arrivalGate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('arrivalGate', 'http://schema.org/arrivalGate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfAvailableAccommodationUnits(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('numberOfAvailableAccommodationUnits', 'http://schema.org/numberOfAvailableAccommodationUnits', ['1.1', '1.2-DRAFT'])

class negativeNotes(RdfProperty[schemaorg.Text | schemaorg.ListItem | schemaorg.ItemList | schemaorg.WebContent]):
    term = RdfTerm('negativeNotes', 'http://schema.org/negativeNotes', ['1.2-DRAFT'])

class identifier(RdfProperty[schemaorg.Text | schemaorg.PropertyValue | schemaorg.URL]):
    term = RdfTerm('identifier', 'http://schema.org/identifier', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class suggestedMeasurement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('suggestedMeasurement', 'http://schema.org/suggestedMeasurement', ['1.2-DRAFT'])

class recipeCuisine(RdfProperty[schemaorg.Text]):
    term = RdfTerm('recipeCuisine', 'http://schema.org/recipeCuisine', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class jobTitle(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('jobTitle', 'http://schema.org/jobTitle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastSignalModulation(RdfProperty[schemaorg.Text | schemaorg.QualitativeValue]):
    term = RdfTerm('broadcastSignalModulation', 'http://schema.org/broadcastSignalModulation', ['1.0', '1.1', '1.2-DRAFT'])

class bed(RdfProperty[schemaorg.BedType | schemaorg.Text | schemaorg.BedDetails]):
    term = RdfTerm('bed', 'http://schema.org/bed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cutoffTime(RdfProperty[schemaorg.Time]):
    term = RdfTerm('cutoffTime', 'http://schema.org/cutoffTime', ['1.1', '1.2-DRAFT'])

class itemReviewed(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('itemReviewed', 'http://schema.org/itemReviewed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vatID(RdfProperty[schemaorg.Text]):
    term = RdfTerm('vatID', 'http://schema.org/vatID', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class securityScreening(RdfProperty[schemaorg.Text]):
    term = RdfTerm('securityScreening', 'http://schema.org/securityScreening', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class leaseLength(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Duration]):
    term = RdfTerm('leaseLength', 'http://schema.org/leaseLength', ['1.0', '1.1', '1.2-DRAFT'])

class orderQuantity(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm('orderQuantity', 'http://schema.org/orderQuantity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class targetName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('targetName', 'http://schema.org/targetName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class engineType(RdfProperty[schemaorg.QualitativeValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('engineType', 'http://schema.org/engineType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class occupationalCategory(RdfProperty[schemaorg.CategoryCode | schemaorg.Text]):
    term = RdfTerm('occupationalCategory', 'http://schema.org/occupationalCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class branch(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('branch', 'http://schema.org/branch', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mainEntity(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('mainEntity', 'http://schema.org/mainEntity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class suitableForDiet(RdfProperty[schemaorg.RestrictedDiet]):
    term = RdfTerm('suitableForDiet', 'http://schema.org/suitableForDiet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class billingDuration(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number | schemaorg.Duration]):
    term = RdfTerm('billingDuration', 'http://schema.org/billingDuration', ['1.2-DRAFT'])

class coverageStartTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('coverageStartTime', 'http://schema.org/coverageStartTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class employmentUnit(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('employmentUnit', 'http://schema.org/employmentUnit', ['1.0', '1.1', '1.2-DRAFT'])

class gtin13(RdfProperty[schemaorg.Text]):
    term = RdfTerm('gtin13', 'http://schema.org/gtin13', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class usesHealthPlanIdStandard(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('usesHealthPlanIdStandard', 'http://schema.org/usesHealthPlanIdStandard', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class editEIDR(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('editEIDR', 'http://schema.org/editEIDR', ['1.1', '1.2-DRAFT'])

class maximumAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('maximumAttendeeCapacity', 'http://schema.org/maximumAttendeeCapacity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class relevantSpecialty(RdfProperty[schemaorg.MedicalSpecialty]):
    term = RdfTerm('relevantSpecialty', 'http://schema.org/relevantSpecialty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class billingPeriod(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('billingPeriod', 'http://schema.org/billingPeriod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class shippingSettingsLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm('shippingSettingsLink', 'http://schema.org/shippingSettingsLink', ['1.1', '1.2-DRAFT'])

class referencesOrder(RdfProperty[schemaorg.Order]):
    term = RdfTerm('referencesOrder', 'http://schema.org/referencesOrder', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class processingTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('processingTime', 'http://schema.org/processingTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class copyrightYear(RdfProperty[schemaorg.Number]):
    term = RdfTerm('copyrightYear', 'http://schema.org/copyrightYear', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastSubChannel(RdfProperty[schemaorg.Text]):
    term = RdfTerm('broadcastSubChannel', 'http://schema.org/broadcastSubChannel', ['1.0', '1.1', '1.2-DRAFT'])

class specialOpeningHoursSpecification(RdfProperty[schemaorg.OpeningHoursSpecification]):
    term = RdfTerm('specialOpeningHoursSpecification', 'http://schema.org/specialOpeningHoursSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class incentiveStatus(RdfProperty[schemaorg.IncentiveStatus]):
    term = RdfTerm('incentiveStatus', 'http://schema.org/incentiveStatus', [])

class servesCuisine(RdfProperty[schemaorg.Text]):
    term = RdfTerm('servesCuisine', 'http://schema.org/servesCuisine', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class collectionSize(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('collectionSize', 'http://schema.org/collectionSize', ['1.0', '1.1', '1.2-DRAFT'])

class operatingSystem(RdfProperty[schemaorg.Text]):
    term = RdfTerm('operatingSystem', 'http://schema.org/operatingSystem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderPercentage(RdfProperty[schemaorg.Number]):
    term = RdfTerm('orderPercentage', 'http://schema.org/orderPercentage', [])

class encodingType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('encodingType', 'http://schema.org/encodingType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class nerve(RdfProperty[schemaorg.Nerve]):
    term = RdfTerm('nerve', 'http://schema.org/nerve', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class webCheckinTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('webCheckinTime', 'http://schema.org/webCheckinTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class taxID(RdfProperty[schemaorg.Text]):
    term = RdfTerm('taxID', 'http://schema.org/taxID', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasMeasurement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('hasMeasurement', 'http://schema.org/hasMeasurement', ['1.2-DRAFT'])

class about(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('about', 'http://schema.org/about', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthCondition(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm('healthCondition', 'http://schema.org/healthCondition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dataFeedElement(RdfProperty[schemaorg.DataFeedItem | schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm('dataFeedElement', 'http://schema.org/dataFeedElement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class prescriptionStatus(RdfProperty[schemaorg.DrugPrescriptionStatus | schemaorg.Text]):
    term = RdfTerm('prescriptionStatus', 'http://schema.org/prescriptionStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class containedIn(RdfProperty[schemaorg.Place]):
    term = RdfTerm('containedIn', 'http://schema.org/containedIn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class diseasePreventionInfo(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm('diseasePreventionInfo', 'http://schema.org/diseasePreventionInfo', ['1.1', '1.2-DRAFT'])

class aspect(RdfProperty[schemaorg.Text]):
    term = RdfTerm('aspect', 'http://schema.org/aspect', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class deliveryLeadTime(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('deliveryLeadTime', 'http://schema.org/deliveryLeadTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isrcCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('isrcCode', 'http://schema.org/isrcCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class nerveMotor(RdfProperty[schemaorg.Muscle]):
    term = RdfTerm('nerveMotor', 'http://schema.org/nerveMotor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class valuePattern(RdfProperty[schemaorg.Text]):
    term = RdfTerm('valuePattern', 'http://schema.org/valuePattern', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class programType(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('programType', 'http://schema.org/programType', ['1.1', '1.2-DRAFT'])

class datePublished(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('datePublished', 'http://schema.org/datePublished', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class location(RdfProperty[schemaorg.Text | schemaorg.Place | schemaorg.VirtualLocation | schemaorg.PostalAddress]):
    term = RdfTerm('location', 'http://schema.org/location', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dropoffTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('dropoffTime', 'http://schema.org/dropoffTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class algorithm(RdfProperty[schemaorg.Text]):
    term = RdfTerm('algorithm', 'http://schema.org/algorithm', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class jobImmediateStart(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('jobImmediateStart', 'http://schema.org/jobImmediateStart', ['1.0', '1.1', '1.2-DRAFT'])

class applicationCategory(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('applicationCategory', 'http://schema.org/applicationCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class directApply(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('directApply', 'http://schema.org/directApply', ['1.2-DRAFT'])

class estimatedCost(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Text]):
    term = RdfTerm('estimatedCost', 'http://schema.org/estimatedCost', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lyricist(RdfProperty[schemaorg.Person]):
    term = RdfTerm('lyricist', 'http://schema.org/lyricist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class requiredGender(RdfProperty[schemaorg.Text]):
    term = RdfTerm('requiredGender', 'http://schema.org/requiredGender', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reservationStatus(RdfProperty[schemaorg.ReservationStatusType]):
    term = RdfTerm('reservationStatus', 'http://schema.org/reservationStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastChannelId(RdfProperty[schemaorg.Text]):
    term = RdfTerm('broadcastChannelId', 'http://schema.org/broadcastChannelId', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class educationalLevel(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('educationalLevel', 'http://schema.org/educationalLevel', ['1.0', '1.1', '1.2-DRAFT'])

class embedUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('embedUrl', 'http://schema.org/embedUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class coverageEndTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('coverageEndTime', 'http://schema.org/coverageEndTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class timeToComplete(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('timeToComplete', 'http://schema.org/timeToComplete', ['1.0', '1.1', '1.2-DRAFT'])

class isResizable(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isResizable', 'http://schema.org/isResizable', ['1.1', '1.2-DRAFT'])

class seller(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('seller', 'http://schema.org/seller', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class passengerPriorityStatus(RdfProperty[schemaorg.Text | schemaorg.QualitativeValue]):
    term = RdfTerm('passengerPriorityStatus', 'http://schema.org/passengerPriorityStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class possibleComplication(RdfProperty[schemaorg.Text]):
    term = RdfTerm('possibleComplication', 'http://schema.org/possibleComplication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class jobStartDate(RdfProperty[schemaorg.Text | schemaorg.Date]):
    term = RdfTerm('jobStartDate', 'http://schema.org/jobStartDate', ['1.0', '1.1', '1.2-DRAFT'])

class adverseOutcome(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm('adverseOutcome', 'http://schema.org/adverseOutcome', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class membershipPointsEarned(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('membershipPointsEarned', 'http://schema.org/membershipPointsEarned', ['1.0', '1.1', '1.2-DRAFT'])

class nextItem(RdfProperty[schemaorg.ListItem]):
    term = RdfTerm('nextItem', 'http://schema.org/nextItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class includedDataCatalog(RdfProperty[schemaorg.DataCatalog]):
    term = RdfTerm('includedDataCatalog', 'http://schema.org/includedDataCatalog', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class signDetected(RdfProperty[schemaorg.MedicalSign]):
    term = RdfTerm('signDetected', 'http://schema.org/signDetected', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdFacilityId(RdfProperty[schemaorg.Text]):
    term = RdfTerm('cvdFacilityId', 'http://schema.org/cvdFacilityId', ['1.1', '1.2-DRAFT'])

class programmingModel(RdfProperty[schemaorg.Text]):
    term = RdfTerm('programmingModel', 'http://schema.org/programmingModel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class chemicalComposition(RdfProperty[schemaorg.Text]):
    term = RdfTerm('chemicalComposition', 'http://schema.org/chemicalComposition', ['1.2-DRAFT'])

class accessibilityFeature(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accessibilityFeature', 'http://schema.org/accessibilityFeature', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class relatedCondition(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm('relatedCondition', 'http://schema.org/relatedCondition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationChanges(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationChanges', 'http://schema.org/legislationChanges', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class qualifications(RdfProperty[schemaorg.EducationalOccupationalCredential | schemaorg.Text]):
    term = RdfTerm('qualifications', 'http://schema.org/qualifications', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class colleagues(RdfProperty[schemaorg.Person]):
    term = RdfTerm('colleagues', 'http://schema.org/colleagues', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class returnLabelSource(RdfProperty[schemaorg.ReturnLabelSourceEnumeration]):
    term = RdfTerm('returnLabelSource', 'http://schema.org/returnLabelSource', ['1.2-DRAFT'])

class guidelineSubject(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm('guidelineSubject', 'http://schema.org/guidelineSubject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class duringMedia(RdfProperty[schemaorg.MediaObject | schemaorg.URL]):
    term = RdfTerm('duringMedia', 'http://schema.org/duringMedia', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class seatNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('seatNumber', 'http://schema.org/seatNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class musicReleaseFormat(RdfProperty[schemaorg.MusicReleaseFormatType]):
    term = RdfTerm('musicReleaseFormat', 'http://schema.org/musicReleaseFormat', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class articleSection(RdfProperty[schemaorg.Text]):
    term = RdfTerm('articleSection', 'http://schema.org/articleSection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class materialExtent(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm('materialExtent', 'http://schema.org/materialExtent', ['1.0', '1.1', '1.2-DRAFT'])

class signOrSymptom(RdfProperty[schemaorg.MedicalSignOrSymptom]):
    term = RdfTerm('signOrSymptom', 'http://schema.org/signOrSymptom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class musicArrangement(RdfProperty[schemaorg.MusicComposition]):
    term = RdfTerm('musicArrangement', 'http://schema.org/musicArrangement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class video(RdfProperty[schemaorg.Clip | schemaorg.VideoObject]):
    term = RdfTerm('video', 'http://schema.org/video', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class remainingAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('remainingAttendeeCapacity', 'http://schema.org/remainingAttendeeCapacity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availableThrough(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('availableThrough', 'http://schema.org/availableThrough', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoCoveredBy(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm('geoCoveredBy', 'http://schema.org/geoCoveredBy', ['1.0', '1.1', '1.2-DRAFT'])

class advanceBookingRequirement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('advanceBookingRequirement', 'http://schema.org/advanceBookingRequirement', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class touristType(RdfProperty[schemaorg.Audience | schemaorg.Text]):
    term = RdfTerm('touristType', 'http://schema.org/touristType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gtin(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('gtin', 'http://schema.org/gtin', ['1.0', '1.1', '1.2-DRAFT'])

class seasonalOverride(RdfProperty[schemaorg.OpeningHoursSpecification]):
    term = RdfTerm('seasonalOverride', 'http://schema.org/seasonalOverride', [])

class loanType(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('loanType', 'http://schema.org/loanType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class meetsEmissionStandard(RdfProperty[schemaorg.QualitativeValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('meetsEmissionStandard', 'http://schema.org/meetsEmissionStandard', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arrivalStation(RdfProperty[schemaorg.TrainStation]):
    term = RdfTerm('arrivalStation', 'http://schema.org/arrivalStation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class description(RdfProperty[schemaorg.Text | schemaorg.TextObject]):
    term = RdfTerm('description', 'http://schema.org/description', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class applicationSuite(RdfProperty[schemaorg.Text]):
    term = RdfTerm('applicationSuite', 'http://schema.org/applicationSuite', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class handlingTime(RdfProperty[schemaorg.QuantitativeValue | schemaorg.ServicePeriod]):
    term = RdfTerm('handlingTime', 'http://schema.org/handlingTime', ['1.1', '1.2-DRAFT'])

class seriousAdverseOutcome(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm('seriousAdverseOutcome', 'http://schema.org/seriousAdverseOutcome', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cookTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('cookTime', 'http://schema.org/cookTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class checkinTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('checkinTime', 'http://schema.org/checkinTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class primaryPrevention(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm('primaryPrevention', 'http://schema.org/primaryPrevention', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isGift(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isGift', 'http://schema.org/isGift', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class departureTerminal(RdfProperty[schemaorg.Text]):
    term = RdfTerm('departureTerminal', 'http://schema.org/departureTerminal', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ticketToken(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('ticketToken', 'http://schema.org/ticketToken', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class albumReleaseType(RdfProperty[schemaorg.MusicAlbumReleaseType]):
    term = RdfTerm('albumReleaseType', 'http://schema.org/albumReleaseType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class nonProprietaryName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('nonProprietaryName', 'http://schema.org/nonProprietaryName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class seatRow(RdfProperty[schemaorg.Text]):
    term = RdfTerm('seatRow', 'http://schema.org/seatRow', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class countriesSupported(RdfProperty[schemaorg.Text]):
    term = RdfTerm('countriesSupported', 'http://schema.org/countriesSupported', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class winner(RdfProperty[schemaorg.Person]):
    term = RdfTerm('winner', 'http://schema.org/winner', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geographicArea(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm('geographicArea', 'http://schema.org/geographicArea', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class nutrition(RdfProperty[schemaorg.NutritionInformation]):
    term = RdfTerm('nutrition', 'http://schema.org/nutrition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class funding(RdfProperty[schemaorg.Grant]):
    term = RdfTerm('funding', 'http://schema.org/funding', ['1.1', '1.2-DRAFT'])

class legislationCommences(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationCommences', 'http://schema.org/legislationCommences', [])

class healthPlanCoinsuranceOption(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanCoinsuranceOption', 'http://schema.org/healthPlanCoinsuranceOption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class termsOfService(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('termsOfService', 'http://schema.org/termsOfService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class artworkSurface(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('artworkSurface', 'http://schema.org/artworkSurface', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class diversityPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('diversityPolicy', 'http://schema.org/diversityPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class openingHours(RdfProperty[schemaorg.Text]):
    term = RdfTerm('openingHours', 'http://schema.org/openingHours', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class usNPI(RdfProperty[schemaorg.Text]):
    term = RdfTerm('usNPI', 'http://schema.org/usNPI', [])

class penciler(RdfProperty[schemaorg.Person]):
    term = RdfTerm('penciler', 'http://schema.org/penciler', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publishedBy(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('publishedBy', 'http://schema.org/publishedBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfPartialBathrooms(RdfProperty[schemaorg.Number]):
    term = RdfTerm('numberOfPartialBathrooms', 'http://schema.org/numberOfPartialBathrooms', ['1.1', '1.2-DRAFT'])

class runsTo(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm('runsTo', 'http://schema.org/runsTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class givenName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('givenName', 'http://schema.org/givenName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasTiers(RdfProperty[schemaorg.MemberProgramTier]):
    term = RdfTerm('hasTiers', 'http://schema.org/hasTiers', [])

class reservationId(RdfProperty[schemaorg.Text]):
    term = RdfTerm('reservationId', 'http://schema.org/reservationId', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class specialCommitments(RdfProperty[schemaorg.Text]):
    term = RdfTerm('specialCommitments', 'http://schema.org/specialCommitments', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class surface(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('surface', 'http://schema.org/surface', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isConsumableFor(RdfProperty[schemaorg.Product]):
    term = RdfTerm('isConsumableFor', 'http://schema.org/isConsumableFor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bccRecipient(RdfProperty[schemaorg.ContactPoint | schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('bccRecipient', 'http://schema.org/bccRecipient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class pickupTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('pickupTime', 'http://schema.org/pickupTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inChI(RdfProperty[schemaorg.Text]):
    term = RdfTerm('inChI', 'http://schema.org/inChI', ['1.2-DRAFT'])

class sha256(RdfProperty[schemaorg.Text]):
    term = RdfTerm('sha256', 'http://schema.org/sha256', ['1.2-DRAFT'])

class attendee(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('attendee', 'http://schema.org/attendee', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isProprietary(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isProprietary', 'http://schema.org/isProprietary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ratingCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('ratingCount', 'http://schema.org/ratingCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class price(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm('price', 'http://schema.org/price', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class utterances(RdfProperty[schemaorg.Text]):
    term = RdfTerm('utterances', 'http://schema.org/utterances', ['1.2-DRAFT'])

class recognizingAuthority(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('recognizingAuthority', 'http://schema.org/recognizingAuthority', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class agent(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('agent', 'http://schema.org/agent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class validFrom(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('validFrom', 'http://schema.org/validFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastServiceTier(RdfProperty[schemaorg.Text]):
    term = RdfTerm('broadcastServiceTier', 'http://schema.org/broadcastServiceTier', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class paymentAccepted(RdfProperty[schemaorg.Text]):
    term = RdfTerm('paymentAccepted', 'http://schema.org/paymentAccepted', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationLegalValue(RdfProperty[schemaorg.LegalValueLevel]):
    term = RdfTerm('legislationLegalValue', 'http://schema.org/legislationLegalValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lodgingUnitDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm('lodgingUnitDescription', 'http://schema.org/lodgingUnitDescription', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class blogPosts(RdfProperty[schemaorg.BlogPosting]):
    term = RdfTerm('blogPosts', 'http://schema.org/blogPosts', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class departurePlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm('departurePlatform', 'http://schema.org/departurePlatform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class albumRelease(RdfProperty[schemaorg.MusicRelease]):
    term = RdfTerm('albumRelease', 'http://schema.org/albumRelease', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mobileUrl(RdfProperty[schemaorg.Text]):
    term = RdfTerm('mobileUrl', 'http://schema.org/mobileUrl', ['1.2-DRAFT'])

class headline(RdfProperty[schemaorg.Text]):
    term = RdfTerm('headline', 'http://schema.org/headline', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class wheelbase(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('wheelbase', 'http://schema.org/wheelbase', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class appliesToPaymentMethod(RdfProperty[schemaorg.PaymentMethod]):
    term = RdfTerm('appliesToPaymentMethod', 'http://schema.org/appliesToPaymentMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class labelDetails(RdfProperty[schemaorg.URL]):
    term = RdfTerm('labelDetails', 'http://schema.org/labelDetails', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class originalMediaContextDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm('originalMediaContextDescription', 'http://schema.org/originalMediaContextDescription', ['1.2-DRAFT'])

class category(RdfProperty[schemaorg.CategoryCode | schemaorg.URL | schemaorg.Thing | schemaorg.PhysicalActivityCategory | schemaorg.Text]):
    term = RdfTerm('category', 'http://schema.org/category', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class includedInDataCatalog(RdfProperty[schemaorg.DataCatalog]):
    term = RdfTerm('includedInDataCatalog', 'http://schema.org/includedInDataCatalog', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class distance(RdfProperty[schemaorg.Distance]):
    term = RdfTerm('distance', 'http://schema.org/distance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class actionPlatform(RdfProperty[schemaorg.Text | schemaorg.DigitalPlatformEnumeration | schemaorg.URL]):
    term = RdfTerm('actionPlatform', 'http://schema.org/actionPlatform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class digitalSourceType(RdfProperty[schemaorg.IPTCDigitalSourceEnumeration]):
    term = RdfTerm('digitalSourceType', 'http://schema.org/digitalSourceType', [])

class workFeatured(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('workFeatured', 'http://schema.org/workFeatured', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recordLabel(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('recordLabel', 'http://schema.org/recordLabel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isEncodedByBioChemEntity(RdfProperty[schemaorg.Gene]):
    term = RdfTerm('isEncodedByBioChemEntity', 'http://schema.org/isEncodedByBioChemEntity', ['1.2-DRAFT'])

class costCategory(RdfProperty[schemaorg.DrugCostCategory]):
    term = RdfTerm('costCategory', 'http://schema.org/costCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class question(RdfProperty[schemaorg.Question]):
    term = RdfTerm('question', 'http://schema.org/question', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class measurementQualifier(RdfProperty[schemaorg.Enumeration]):
    term = RdfTerm('measurementQualifier', 'http://schema.org/measurementQualifier', ['1.2-DRAFT'])

class asin(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('asin', 'http://schema.org/asin', ['1.2-DRAFT'])

class suggestedAnswer(RdfProperty[schemaorg.ItemList | schemaorg.Answer]):
    term = RdfTerm('suggestedAnswer', 'http://schema.org/suggestedAnswer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class postalCodeRange(RdfProperty[schemaorg.PostalCodeRangeSpecification]):
    term = RdfTerm('postalCodeRange', 'http://schema.org/postalCodeRange', ['1.1', '1.2-DRAFT'])

class cvdNumC19HospPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumC19HospPats', 'http://schema.org/cvdNumC19HospPats', ['1.1', '1.2-DRAFT'])

class assemblyVersion(RdfProperty[schemaorg.Text]):
    term = RdfTerm('assemblyVersion', 'http://schema.org/assemblyVersion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class runtime(RdfProperty[schemaorg.Text]):
    term = RdfTerm('runtime', 'http://schema.org/runtime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isPlanForApartment(RdfProperty[schemaorg.Accommodation]):
    term = RdfTerm('isPlanForApartment', 'http://schema.org/isPlanForApartment', ['1.1', '1.2-DRAFT'])

class hasBroadcastChannel(RdfProperty[schemaorg.BroadcastChannel]):
    term = RdfTerm('hasBroadcastChannel', 'http://schema.org/hasBroadcastChannel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class learningResourceType(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('learningResourceType', 'http://schema.org/learningResourceType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class relatedTo(RdfProperty[schemaorg.Person]):
    term = RdfTerm('relatedTo', 'http://schema.org/relatedTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gameServer(RdfProperty[schemaorg.GameServer]):
    term = RdfTerm('gameServer', 'http://schema.org/gameServer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class foundingDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('foundingDate', 'http://schema.org/foundingDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class prepTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('prepTime', 'http://schema.org/prepTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class validIn(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm('validIn', 'http://schema.org/validIn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class transmissionMethod(RdfProperty[schemaorg.Text]):
    term = RdfTerm('transmissionMethod', 'http://schema.org/transmissionMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class itinerary(RdfProperty[schemaorg.ItemList | schemaorg.Place]):
    term = RdfTerm('itinerary', 'http://schema.org/itinerary', ['1.0', '1.1', '1.2-DRAFT'])

class alternativeHeadline(RdfProperty[schemaorg.Text]):
    term = RdfTerm('alternativeHeadline', 'http://schema.org/alternativeHeadline', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfPlayers(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('numberOfPlayers', 'http://schema.org/numberOfPlayers', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfCredits(RdfProperty[schemaorg.StructuredValue | schemaorg.Integer]):
    term = RdfTerm('numberOfCredits', 'http://schema.org/numberOfCredits', ['1.1', '1.2-DRAFT'])

class aggregateElement(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('aggregateElement', 'http://schema.org/aggregateElement', [])

class playersOnline(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('playersOnline', 'http://schema.org/playersOnline', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class maps(RdfProperty[schemaorg.URL]):
    term = RdfTerm('maps', 'http://schema.org/maps', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class birthDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('birthDate', 'http://schema.org/birthDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class temporal(RdfProperty[schemaorg.DateTime | schemaorg.Text]):
    term = RdfTerm('temporal', 'http://schema.org/temporal', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class deliveryTime(RdfProperty[schemaorg.ShippingDeliveryTime]):
    term = RdfTerm('deliveryTime', 'http://schema.org/deliveryTime', ['1.1', '1.2-DRAFT'])

class serviceLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('serviceLocation', 'http://schema.org/serviceLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class performer(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('performer', 'http://schema.org/performer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class seatSection(RdfProperty[schemaorg.Text]):
    term = RdfTerm('seatSection', 'http://schema.org/seatSection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class result(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('result', 'http://schema.org/result', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cookingMethod(RdfProperty[schemaorg.Text]):
    term = RdfTerm('cookingMethod', 'http://schema.org/cookingMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class subStageSuffix(RdfProperty[schemaorg.Text]):
    term = RdfTerm('subStageSuffix', 'http://schema.org/subStageSuffix', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class opens(RdfProperty[schemaorg.Time]):
    term = RdfTerm('opens', 'http://schema.org/opens', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class freeShippingThreshold(RdfProperty[schemaorg.DeliveryChargeSpecification | schemaorg.MonetaryAmount]):
    term = RdfTerm('freeShippingThreshold', 'http://schema.org/freeShippingThreshold', ['1.1', '1.2-DRAFT'])

class primaryImageOfPage(RdfProperty[schemaorg.ImageObject]):
    term = RdfTerm('primaryImageOfPage', 'http://schema.org/primaryImageOfPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class color(RdfProperty[schemaorg.Text]):
    term = RdfTerm('color', 'http://schema.org/color', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class acceptedAnswer(RdfProperty[schemaorg.Answer | schemaorg.ItemList]):
    term = RdfTerm('acceptedAnswer', 'http://schema.org/acceptedAnswer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class constraintProperty(RdfProperty[schemaorg.URL | schemaorg.Property]):
    term = RdfTerm('constraintProperty', 'http://schema.org/constraintProperty', ['1.2-DRAFT'])

class streetAddress(RdfProperty[schemaorg.Text]):
    term = RdfTerm('streetAddress', 'http://schema.org/streetAddress', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isBasedOnUrl(RdfProperty[schemaorg.URL | schemaorg.CreativeWork | schemaorg.Product]):
    term = RdfTerm('isBasedOnUrl', 'http://schema.org/isBasedOnUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recipient(RdfProperty[schemaorg.Organization | schemaorg.Audience | schemaorg.ContactPoint | schemaorg.Person]):
    term = RdfTerm('recipient', 'http://schema.org/recipient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class associatedMedia(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm('associatedMedia', 'http://schema.org/associatedMedia', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dataset(RdfProperty[schemaorg.Dataset]):
    term = RdfTerm('dataset', 'http://schema.org/dataset', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class studyDesign(RdfProperty[schemaorg.MedicalObservationalStudyDesign]):
    term = RdfTerm('studyDesign', 'http://schema.org/studyDesign', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class riskFactor(RdfProperty[schemaorg.MedicalRiskFactor]):
    term = RdfTerm('riskFactor', 'http://schema.org/riskFactor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class servicePostalAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm('servicePostalAddress', 'http://schema.org/servicePostalAddress', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class commentCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('commentCount', 'http://schema.org/commentCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasVariant(RdfProperty[schemaorg.Product]):
    term = RdfTerm('hasVariant', 'http://schema.org/hasVariant', ['1.1', '1.2-DRAFT'])

class legislationTransposes(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationTransposes', 'http://schema.org/legislationTransposes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class speechToTextMarkup(RdfProperty[schemaorg.Text]):
    term = RdfTerm('speechToTextMarkup', 'http://schema.org/speechToTextMarkup', ['1.1', '1.2-DRAFT'])

class cholesterolContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('cholesterolContent', 'http://schema.org/cholesterolContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class busNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('busNumber', 'http://schema.org/busNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class certificationRating(RdfProperty[schemaorg.Rating]):
    term = RdfTerm('certificationRating', 'http://schema.org/certificationRating', [])

class feesAndCommissionsSpecification(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('feesAndCommissionsSpecification', 'http://schema.org/feesAndCommissionsSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class infectiousAgent(RdfProperty[schemaorg.Text]):
    term = RdfTerm('infectiousAgent', 'http://schema.org/infectiousAgent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class incentiveCompensation(RdfProperty[schemaorg.Text]):
    term = RdfTerm('incentiveCompensation', 'http://schema.org/incentiveCompensation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastOfEvent(RdfProperty[schemaorg.Event]):
    term = RdfTerm('broadcastOfEvent', 'http://schema.org/broadcastOfEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sportsEvent(RdfProperty[schemaorg.SportsEvent]):
    term = RdfTerm('sportsEvent', 'http://schema.org/sportsEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dateCreated(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('dateCreated', 'http://schema.org/dateCreated', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class toRecipient(RdfProperty[schemaorg.Organization | schemaorg.Audience | schemaorg.ContactPoint | schemaorg.Person]):
    term = RdfTerm('toRecipient', 'http://schema.org/toRecipient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class medicineSystem(RdfProperty[schemaorg.MedicineSystem]):
    term = RdfTerm('medicineSystem', 'http://schema.org/medicineSystem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class unitText(RdfProperty[schemaorg.Text]):
    term = RdfTerm('unitText', 'http://schema.org/unitText', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class frequency(RdfProperty[schemaorg.Text]):
    term = RdfTerm('frequency', 'http://schema.org/frequency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderStatus(RdfProperty[schemaorg.OrderStatus]):
    term = RdfTerm('orderStatus', 'http://schema.org/orderStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class addOn(RdfProperty[schemaorg.Offer]):
    term = RdfTerm('addOn', 'http://schema.org/addOn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class acceptedOffer(RdfProperty[schemaorg.Offer]):
    term = RdfTerm('acceptedOffer', 'http://schema.org/acceptedOffer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class artEdition(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('artEdition', 'http://schema.org/artEdition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class secondaryPrevention(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm('secondaryPrevention', 'http://schema.org/secondaryPrevention', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class yearBuilt(RdfProperty[schemaorg.Number]):
    term = RdfTerm('yearBuilt', 'http://schema.org/yearBuilt', ['1.1', '1.2-DRAFT'])

class sharedContent(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('sharedContent', 'http://schema.org/sharedContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class certificationStatus(RdfProperty[schemaorg.CertificationStatusEnumeration]):
    term = RdfTerm('certificationStatus', 'http://schema.org/certificationStatus', [])

class subEvents(RdfProperty[schemaorg.Event]):
    term = RdfTerm('subEvents', 'http://schema.org/subEvents', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fileFormat(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('fileFormat', 'http://schema.org/fileFormat', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class propertyID(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('propertyID', 'http://schema.org/propertyID', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class teaches(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('teaches', 'http://schema.org/teaches', ['1.1', '1.2-DRAFT'])

class regionsAllowed(RdfProperty[schemaorg.Place]):
    term = RdfTerm('regionsAllowed', 'http://schema.org/regionsAllowed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class addressCountry(RdfProperty[schemaorg.Text | schemaorg.Country]):
    term = RdfTerm('addressCountry', 'http://schema.org/addressCountry', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class validUntil(RdfProperty[schemaorg.Date]):
    term = RdfTerm('validUntil', 'http://schema.org/validUntil', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class baseSalary(RdfProperty[schemaorg.PriceSpecification | schemaorg.Number | schemaorg.MonetaryAmount]):
    term = RdfTerm('baseSalary', 'http://schema.org/baseSalary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class productSupported(RdfProperty[schemaorg.Product | schemaorg.Text]):
    term = RdfTerm('productSupported', 'http://schema.org/productSupported', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasCourseInstance(RdfProperty[schemaorg.CourseInstance]):
    term = RdfTerm('hasCourseInstance', 'http://schema.org/hasCourseInstance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class merchantReturnDays(RdfProperty[schemaorg.Date | schemaorg.Integer | schemaorg.DateTime]):
    term = RdfTerm('merchantReturnDays', 'http://schema.org/merchantReturnDays', ['1.1', '1.2-DRAFT'])

class sportsActivityLocation(RdfProperty[schemaorg.SportsActivityLocation]):
    term = RdfTerm('sportsActivityLocation', 'http://schema.org/sportsActivityLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class countryOfLastProcessing(RdfProperty[schemaorg.Text]):
    term = RdfTerm('countryOfLastProcessing', 'http://schema.org/countryOfLastProcessing', ['1.2-DRAFT'])

class availableDeliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm('availableDeliveryMethod', 'http://schema.org/availableDeliveryMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class guideline(RdfProperty[schemaorg.MedicalGuideline]):
    term = RdfTerm('guideline', 'http://schema.org/guideline', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accessibilityControl(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accessibilityControl', 'http://schema.org/accessibilityControl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class interestRate(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('interestRate', 'http://schema.org/interestRate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isPartOf(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('isPartOf', 'http://schema.org/isPartOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class transcript(RdfProperty[schemaorg.Text]):
    term = RdfTerm('transcript', 'http://schema.org/transcript', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class containsSeason(RdfProperty[schemaorg.CreativeWorkSeason]):
    term = RdfTerm('containsSeason', 'http://schema.org/containsSeason', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoRadius(RdfProperty[schemaorg.Distance | schemaorg.Text | schemaorg.Number]):
    term = RdfTerm('geoRadius', 'http://schema.org/geoRadius', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationResponsible(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('legislationResponsible', 'http://schema.org/legislationResponsible', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class homeLocation(RdfProperty[schemaorg.ContactPoint | schemaorg.Place]):
    term = RdfTerm('homeLocation', 'http://schema.org/homeLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationCorrects(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationCorrects', 'http://schema.org/legislationCorrects', [])

class speed(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('speed', 'http://schema.org/speed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class logo(RdfProperty[schemaorg.URL | schemaorg.ImageObject]):
    term = RdfTerm('logo', 'http://schema.org/logo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class employee(RdfProperty[schemaorg.Person]):
    term = RdfTerm('employee', 'http://schema.org/employee', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class subjectOf(RdfProperty[schemaorg.Event | schemaorg.CreativeWork]):
    term = RdfTerm('subjectOf', 'http://schema.org/subjectOf', ['1.0', '1.1', '1.2-DRAFT'])

class claimInterpreter(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('claimInterpreter', 'http://schema.org/claimInterpreter', ['1.2-DRAFT'])

class pagination(RdfProperty[schemaorg.Text]):
    term = RdfTerm('pagination', 'http://schema.org/pagination', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class afterMedia(RdfProperty[schemaorg.MediaObject | schemaorg.URL]):
    term = RdfTerm('afterMedia', 'http://schema.org/afterMedia', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class alumniOf(RdfProperty[schemaorg.Organization | schemaorg.EducationalOrganization]):
    term = RdfTerm('alumniOf', 'http://schema.org/alumniOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lender(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('lender', 'http://schema.org/lender', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class modelDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('modelDate', 'http://schema.org/modelDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class parentTaxon(RdfProperty[schemaorg.Taxon | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('parentTaxon', 'http://schema.org/parentTaxon', ['1.2-DRAFT'])

class additionalNumberOfGuests(RdfProperty[schemaorg.Number]):
    term = RdfTerm('additionalNumberOfGuests', 'http://schema.org/additionalNumberOfGuests', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class iupacName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('iupacName', 'http://schema.org/iupacName', ['1.2-DRAFT'])

class addressLocality(RdfProperty[schemaorg.Text]):
    term = RdfTerm('addressLocality', 'http://schema.org/addressLocality', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contactPoints(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm('contactPoints', 'http://schema.org/contactPoints', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class roofLoad(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('roofLoad', 'http://schema.org/roofLoad', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legalName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('legalName', 'http://schema.org/legalName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lodgingUnitType(RdfProperty[schemaorg.Text | schemaorg.QualitativeValue]):
    term = RdfTerm('lodgingUnitType', 'http://schema.org/lodgingUnitType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class activityFrequency(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm('activityFrequency', 'http://schema.org/activityFrequency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isInvolvedInBiologicalProcess(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('isInvolvedInBiologicalProcess', 'http://schema.org/isInvolvedInBiologicalProcess', ['1.2-DRAFT'])

class cheatCode(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('cheatCode', 'http://schema.org/cheatCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class jobBenefits(RdfProperty[schemaorg.Text]):
    term = RdfTerm('jobBenefits', 'http://schema.org/jobBenefits', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class subTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm('subTest', 'http://schema.org/subTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class competitor(RdfProperty[schemaorg.Person | schemaorg.SportsTeam]):
    term = RdfTerm('competitor', 'http://schema.org/competitor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class alumni(RdfProperty[schemaorg.Person]):
    term = RdfTerm('alumni', 'http://schema.org/alumni', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfSeasons(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('numberOfSeasons', 'http://schema.org/numberOfSeasons', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfRooms(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('numberOfRooms', 'http://schema.org/numberOfRooms', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('orderNumber', 'http://schema.org/orderNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class athlete(RdfProperty[schemaorg.Person]):
    term = RdfTerm('athlete', 'http://schema.org/athlete', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class associatedDisease(RdfProperty[schemaorg.MedicalCondition | schemaorg.URL | schemaorg.PropertyValue]):
    term = RdfTerm('associatedDisease', 'http://schema.org/associatedDisease', ['1.2-DRAFT'])

class accessibilityAPI(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accessibilityAPI', 'http://schema.org/accessibilityAPI', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class relatedTherapy(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm('relatedTherapy', 'http://schema.org/relatedTherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class returnMethod(RdfProperty[schemaorg.ReturnMethodEnumeration]):
    term = RdfTerm('returnMethod', 'http://schema.org/returnMethod', ['1.2-DRAFT'])

class issuedBy(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('issuedBy', 'http://schema.org/issuedBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contentReferenceTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('contentReferenceTime', 'http://schema.org/contentReferenceTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class amount(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Number]):
    term = RdfTerm('amount', 'http://schema.org/amount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class identifyingExam(RdfProperty[schemaorg.PhysicalExam]):
    term = RdfTerm('identifyingExam', 'http://schema.org/identifyingExam', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class syllabusSections(RdfProperty[schemaorg.Syllabus]):
    term = RdfTerm('syllabusSections', 'http://schema.org/syllabusSections', ['1.2-DRAFT'])

class targetPlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm('targetPlatform', 'http://schema.org/targetPlatform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class shippingOrigin(RdfProperty[schemaorg.DefinedRegion]):
    term = RdfTerm('shippingOrigin', 'http://schema.org/shippingOrigin', ['1.2-DRAFT'])

class possibleTreatment(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm('possibleTreatment', 'http://schema.org/possibleTreatment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class performTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('performTime', 'http://schema.org/performTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfEpisode(RdfProperty[schemaorg.Episode]):
    term = RdfTerm('partOfEpisode', 'http://schema.org/partOfEpisode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ratingExplanation(RdfProperty[schemaorg.Text]):
    term = RdfTerm('ratingExplanation', 'http://schema.org/ratingExplanation', ['1.0', '1.1', '1.2-DRAFT'])

class newsUpdatesAndGuidelines(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm('newsUpdatesAndGuidelines', 'http://schema.org/newsUpdatesAndGuidelines', ['1.1', '1.2-DRAFT'])

class percentile90(RdfProperty[schemaorg.Number]):
    term = RdfTerm('percentile90', 'http://schema.org/percentile90', ['1.0', '1.1', '1.2-DRAFT'])

class availableOnDevice(RdfProperty[schemaorg.Text]):
    term = RdfTerm('availableOnDevice', 'http://schema.org/availableOnDevice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class albums(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm('albums', 'http://schema.org/albums', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lyrics(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('lyrics', 'http://schema.org/lyrics', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class postOp(RdfProperty[schemaorg.Text]):
    term = RdfTerm('postOp', 'http://schema.org/postOp', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('orderDate', 'http://schema.org/orderDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderItemNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('orderItemNumber', 'http://schema.org/orderItemNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class stupidProperty(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('stupidProperty', 'http://schema.org/stupidProperty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class providesBroadcastService(RdfProperty[schemaorg.BroadcastService]):
    term = RdfTerm('providesBroadcastService', 'http://schema.org/providesBroadcastService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfAirbags(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('numberOfAirbags', 'http://schema.org/numberOfAirbags', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class naics(RdfProperty[schemaorg.Text]):
    term = RdfTerm('naics', 'http://schema.org/naics', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class readBy(RdfProperty[schemaorg.Person]):
    term = RdfTerm('readBy', 'http://schema.org/readBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanDrugOption(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanDrugOption', 'http://schema.org/healthPlanDrugOption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gamePlatform(RdfProperty[schemaorg.URL | schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm('gamePlatform', 'http://schema.org/gamePlatform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class answerCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('answerCount', 'http://schema.org/answerCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class item(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('item', 'http://schema.org/item', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class flightNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('flightNumber', 'http://schema.org/flightNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class multipleValues(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('multipleValues', 'http://schema.org/multipleValues', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('legislationDate', 'http://schema.org/legislationDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mechanismOfAction(RdfProperty[schemaorg.Text]):
    term = RdfTerm('mechanismOfAction', 'http://schema.org/mechanismOfAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class workPerformed(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('workPerformed', 'http://schema.org/workPerformed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class customerRemorseReturnFees(RdfProperty[schemaorg.ReturnFeesEnumeration]):
    term = RdfTerm('customerRemorseReturnFees', 'http://schema.org/customerRemorseReturnFees', ['1.2-DRAFT'])

class offeredBy(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('offeredBy', 'http://schema.org/offeredBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bankAccountType(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('bankAccountType', 'http://schema.org/bankAccountType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class duration(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Duration]):
    term = RdfTerm('duration', 'http://schema.org/duration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fromLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('fromLocation', 'http://schema.org/fromLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accelerationTime(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('accelerationTime', 'http://schema.org/accelerationTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasDefinedTerm(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm('hasDefinedTerm', 'http://schema.org/hasDefinedTerm', ['1.0', '1.1', '1.2-DRAFT'])

class childTaxon(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.Taxon]):
    term = RdfTerm('childTaxon', 'http://schema.org/childTaxon', ['1.2-DRAFT'])

class study(RdfProperty[schemaorg.MedicalStudy]):
    term = RdfTerm('study', 'http://schema.org/study', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gettingTestedInfo(RdfProperty[schemaorg.WebContent | schemaorg.URL]):
    term = RdfTerm('gettingTestedInfo', 'http://schema.org/gettingTestedInfo', ['1.1', '1.2-DRAFT'])

class artform(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('artform', 'http://schema.org/artform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isTierOf(RdfProperty[schemaorg.MemberProgram]):
    term = RdfTerm('isTierOf', 'http://schema.org/isTierOf', [])

class query(RdfProperty[schemaorg.Text]):
    term = RdfTerm('query', 'http://schema.org/query', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanCopay(RdfProperty[schemaorg.PriceSpecification]):
    term = RdfTerm('healthPlanCopay', 'http://schema.org/healthPlanCopay', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class volumeNumber(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('volumeNumber', 'http://schema.org/volumeNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class stageAsNumber(RdfProperty[schemaorg.Number]):
    term = RdfTerm('stageAsNumber', 'http://schema.org/stageAsNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoContains(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm('geoContains', 'http://schema.org/geoContains', ['1.0', '1.1', '1.2-DRAFT'])

class organizer(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('organizer', 'http://schema.org/organizer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class estimatesRiskOf(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm('estimatesRiskOf', 'http://schema.org/estimatesRiskOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class loser(RdfProperty[schemaorg.Person]):
    term = RdfTerm('loser', 'http://schema.org/loser', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class validThrough(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('validThrough', 'http://schema.org/validThrough', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class torque(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('torque', 'http://schema.org/torque', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class rxcui(RdfProperty[schemaorg.Text]):
    term = RdfTerm('rxcui', 'http://schema.org/rxcui', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class offerCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('offerCount', 'http://schema.org/offerCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcaster(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('broadcaster', 'http://schema.org/broadcaster', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class monthlyMinimumRepaymentAmount(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Number]):
    term = RdfTerm('monthlyMinimumRepaymentAmount', 'http://schema.org/monthlyMinimumRepaymentAmount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isBasedOn(RdfProperty[schemaorg.URL | schemaorg.CreativeWork | schemaorg.Product]):
    term = RdfTerm('isBasedOn', 'http://schema.org/isBasedOn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class itemListOrder(RdfProperty[schemaorg.Text | schemaorg.ItemListOrderType]):
    term = RdfTerm('itemListOrder', 'http://schema.org/itemListOrder', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geo(RdfProperty[schemaorg.GeoCoordinates | schemaorg.GeoShape]):
    term = RdfTerm('geo', 'http://schema.org/geo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class printPage(RdfProperty[schemaorg.Text]):
    term = RdfTerm('printPage', 'http://schema.org/printPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class alternateName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('alternateName', 'http://schema.org/alternateName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class timeOfDay(RdfProperty[schemaorg.Text]):
    term = RdfTerm('timeOfDay', 'http://schema.org/timeOfDay', ['1.1', '1.2-DRAFT'])

class publicAccess(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('publicAccess', 'http://schema.org/publicAccess', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class actor(RdfProperty[schemaorg.Person | schemaorg.PerformingGroup]):
    term = RdfTerm('actor', 'http://schema.org/actor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class performers(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('performers', 'http://schema.org/performers', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class owns(RdfProperty[schemaorg.Product | schemaorg.OwnershipInfo]):
    term = RdfTerm('owns', 'http://schema.org/owns', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class seasonNumber(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('seasonNumber', 'http://schema.org/seasonNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class valueAddedTaxIncluded(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('valueAddedTaxIncluded', 'http://schema.org/valueAddedTaxIncluded', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class requiredMaxAge(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('requiredMaxAge', 'http://schema.org/requiredMaxAge', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class worstRating(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('worstRating', 'http://schema.org/worstRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class callSign(RdfProperty[schemaorg.Text]):
    term = RdfTerm('callSign', 'http://schema.org/callSign', ['1.0', '1.1', '1.2-DRAFT'])

class cvdNumBedsOcc(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumBedsOcc', 'http://schema.org/cvdNumBedsOcc', ['1.1', '1.2-DRAFT'])

class variesBy(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('variesBy', 'http://schema.org/variesBy', ['1.1', '1.2-DRAFT'])

class termCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('termCode', 'http://schema.org/termCode', ['1.0', '1.1', '1.2-DRAFT'])

class creativeWorkStatus(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm('creativeWorkStatus', 'http://schema.org/creativeWorkStatus', ['1.0', '1.1', '1.2-DRAFT'])

class dateRead(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('dateRead', 'http://schema.org/dateRead', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class device(RdfProperty[schemaorg.Text]):
    term = RdfTerm('device', 'http://schema.org/device', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class departureGate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('departureGate', 'http://schema.org/departureGate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class award(RdfProperty[schemaorg.Text]):
    term = RdfTerm('award', 'http://schema.org/award', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class estimatedSalary(RdfProperty[schemaorg.MonetaryAmountDistribution | schemaorg.Number | schemaorg.MonetaryAmount]):
    term = RdfTerm('estimatedSalary', 'http://schema.org/estimatedSalary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class educationalUse(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('educationalUse', 'http://schema.org/educationalUse', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class drug(RdfProperty[schemaorg.Drug]):
    term = RdfTerm('drug', 'http://schema.org/drug', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class returnPolicyCategory(RdfProperty[schemaorg.MerchantReturnEnumeration]):
    term = RdfTerm('returnPolicyCategory', 'http://schema.org/returnPolicyCategory', ['1.0', '1.1', '1.2-DRAFT'])

class sensoryUnit(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.SuperficialAnatomy]):
    term = RdfTerm('sensoryUnit', 'http://schema.org/sensoryUnit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isFamilyFriendly(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isFamilyFriendly', 'http://schema.org/isFamilyFriendly', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class namedPosition(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('namedPosition', 'http://schema.org/namedPosition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class activeIngredient(RdfProperty[schemaorg.Text]):
    term = RdfTerm('activeIngredient', 'http://schema.org/activeIngredient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class costOrigin(RdfProperty[schemaorg.Text]):
    term = RdfTerm('costOrigin', 'http://schema.org/costOrigin', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanNetworkId(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanNetworkId', 'http://schema.org/healthPlanNetworkId', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class trackingNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('trackingNumber', 'http://schema.org/trackingNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tongueWeight(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('tongueWeight', 'http://schema.org/tongueWeight', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class screenshot(RdfProperty[schemaorg.URL | schemaorg.ImageObject]):
    term = RdfTerm('screenshot', 'http://schema.org/screenshot', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class interactivityType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('interactivityType', 'http://schema.org/interactivityType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class releaseDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('releaseDate', 'http://schema.org/releaseDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class activityDuration(RdfProperty[schemaorg.Duration | schemaorg.QuantitativeValue]):
    term = RdfTerm('activityDuration', 'http://schema.org/activityDuration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class brand(RdfProperty[schemaorg.Brand | schemaorg.Organization]):
    term = RdfTerm('brand', 'http://schema.org/brand', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasHealthAspect(RdfProperty[schemaorg.HealthAspectEnumeration]):
    term = RdfTerm('hasHealthAspect', 'http://schema.org/hasHealthAspect', ['1.0', '1.1', '1.2-DRAFT'])

class value(RdfProperty[schemaorg.StructuredValue | schemaorg.Number | schemaorg.Boolean | schemaorg.Text]):
    term = RdfTerm('value', 'http://schema.org/value', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dateIssued(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('dateIssued', 'http://schema.org/dateIssued', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class transFatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('transFatContent', 'http://schema.org/transFatContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class box(RdfProperty[schemaorg.Text]):
    term = RdfTerm('box', 'http://schema.org/box', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publication(RdfProperty[schemaorg.PublicationEvent]):
    term = RdfTerm('publication', 'http://schema.org/publication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inProductGroupWithID(RdfProperty[schemaorg.Text]):
    term = RdfTerm('inProductGroupWithID', 'http://schema.org/inProductGroupWithID', ['1.1', '1.2-DRAFT'])

class followee(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('followee', 'http://schema.org/followee', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class providerMobility(RdfProperty[schemaorg.Text]):
    term = RdfTerm('providerMobility', 'http://schema.org/providerMobility', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class children(RdfProperty[schemaorg.Person]):
    term = RdfTerm('children', 'http://schema.org/children', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class seatingCapacity(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm('seatingCapacity', 'http://schema.org/seatingCapacity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class merchantReturnLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm('merchantReturnLink', 'http://schema.org/merchantReturnLink', ['1.1', '1.2-DRAFT'])

class latitude(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('latitude', 'http://schema.org/latitude', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class resultComment(RdfProperty[schemaorg.Comment]):
    term = RdfTerm('resultComment', 'http://schema.org/resultComment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class processorRequirements(RdfProperty[schemaorg.Text]):
    term = RdfTerm('processorRequirements', 'http://schema.org/processorRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class releaseNotes(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('releaseNotes', 'http://schema.org/releaseNotes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lesserOrEqual(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm('lesserOrEqual', 'http://schema.org/lesserOrEqual', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class amountOfThisGood(RdfProperty[schemaorg.Number]):
    term = RdfTerm('amountOfThisGood', 'http://schema.org/amountOfThisGood', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastAffiliateOf(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('broadcastAffiliateOf', 'http://schema.org/broadcastAffiliateOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationApplies(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationApplies', 'http://schema.org/legislationApplies', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accountablePerson(RdfProperty[schemaorg.Person]):
    term = RdfTerm('accountablePerson', 'http://schema.org/accountablePerson', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class linkRelationship(RdfProperty[schemaorg.Text]):
    term = RdfTerm('linkRelationship', 'http://schema.org/linkRelationship', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mathExpression(RdfProperty[schemaorg.SolveMathAction | schemaorg.Text]):
    term = RdfTerm('mathExpression', 'http://schema.org/mathExpression', ['1.2-DRAFT'])

class bookingTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('bookingTime', 'http://schema.org/bookingTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class softwareAddOn(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm('softwareAddOn', 'http://schema.org/softwareAddOn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class area(RdfProperty[schemaorg.Place]):
    term = RdfTerm('area', 'http://schema.org/area', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class knowsLanguage(RdfProperty[schemaorg.Text | schemaorg.Language]):
    term = RdfTerm('knowsLanguage', 'http://schema.org/knowsLanguage', ['1.0', '1.1', '1.2-DRAFT'])

class totalJobOpenings(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('totalJobOpenings', 'http://schema.org/totalJobOpenings', ['1.0', '1.1', '1.2-DRAFT'])

class hostingOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('hostingOrganization', 'http://schema.org/hostingOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bioChemInteraction(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('bioChemInteraction', 'http://schema.org/bioChemInteraction', ['1.2-DRAFT'])

class xpath(RdfProperty[schemaorg.XPathType]):
    term = RdfTerm('xpath', 'http://schema.org/xpath', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class postOfficeBoxNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('postOfficeBoxNumber', 'http://schema.org/postOfficeBoxNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dropoffLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('dropoffLocation', 'http://schema.org/dropoffLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cssSelector(RdfProperty[schemaorg.CssSelectorType]):
    term = RdfTerm('cssSelector', 'http://schema.org/cssSelector', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isLocatedInSubcellularLocation(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('isLocatedInSubcellularLocation', 'http://schema.org/isLocatedInSubcellularLocation', ['1.2-DRAFT'])

class totalPaymentDue(RdfProperty[schemaorg.MonetaryAmount | schemaorg.PriceSpecification]):
    term = RdfTerm('totalPaymentDue', 'http://schema.org/totalPaymentDue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gracePeriod(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('gracePeriod', 'http://schema.org/gracePeriod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arterialBranch(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('arterialBranch', 'http://schema.org/arterialBranch', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class customer(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('customer', 'http://schema.org/customer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class requirements(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('requirements', 'http://schema.org/requirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class language(RdfProperty[schemaorg.Language]):
    term = RdfTerm('language', 'http://schema.org/language', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class abridged(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('abridged', 'http://schema.org/abridged', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class driveWheelConfiguration(RdfProperty[schemaorg.DriveWheelConfigurationValue | schemaorg.Text]):
    term = RdfTerm('driveWheelConfiguration', 'http://schema.org/driveWheelConfiguration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class manufacturer(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('manufacturer', 'http://schema.org/manufacturer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class map(RdfProperty[schemaorg.URL]):
    term = RdfTerm('map', 'http://schema.org/map', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class termsPerYear(RdfProperty[schemaorg.Number]):
    term = RdfTerm('termsPerYear', 'http://schema.org/termsPerYear', ['1.1', '1.2-DRAFT'])

class paymentMethodId(RdfProperty[schemaorg.Text]):
    term = RdfTerm('paymentMethodId', 'http://schema.org/paymentMethodId', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sender(RdfProperty[schemaorg.Audience | schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('sender', 'http://schema.org/sender', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class targetUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('targetUrl', 'http://schema.org/targetUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arrivalTerminal(RdfProperty[schemaorg.Text]):
    term = RdfTerm('arrivalTerminal', 'http://schema.org/arrivalTerminal', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class version(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('version', 'http://schema.org/version', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accountId(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accountId', 'http://schema.org/accountId', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class expires(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('expires', 'http://schema.org/expires', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class doseSchedule(RdfProperty[schemaorg.DoseSchedule]):
    term = RdfTerm('doseSchedule', 'http://schema.org/doseSchedule', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class currentExchangeRate(RdfProperty[schemaorg.UnitPriceSpecification]):
    term = RdfTerm('currentExchangeRate', 'http://schema.org/currentExchangeRate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class menuAddOn(RdfProperty[schemaorg.MenuSection | schemaorg.MenuItem]):
    term = RdfTerm('menuAddOn', 'http://schema.org/menuAddOn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class awards(RdfProperty[schemaorg.Text]):
    term = RdfTerm('awards', 'http://schema.org/awards', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class menu(RdfProperty[schemaorg.URL | schemaorg.Menu | schemaorg.Text]):
    term = RdfTerm('menu', 'http://schema.org/menu', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class codeRepository(RdfProperty[schemaorg.URL]):
    term = RdfTerm('codeRepository', 'http://schema.org/codeRepository', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class replacer(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('replacer', 'http://schema.org/replacer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationDateOfApplicability(RdfProperty[schemaorg.Date]):
    term = RdfTerm('legislationDateOfApplicability', 'http://schema.org/legislationDateOfApplicability', [])

class representativeOfPage(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('representativeOfPage', 'http://schema.org/representativeOfPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class subStructure(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('subStructure', 'http://schema.org/subStructure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class firstAppearance(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('firstAppearance', 'http://schema.org/firstAppearance', ['1.0', '1.1', '1.2-DRAFT'])

class pregnancyWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm('pregnancyWarning', 'http://schema.org/pregnancyWarning', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class affiliation(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('affiliation', 'http://schema.org/affiliation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class text(RdfProperty[schemaorg.Text]):
    term = RdfTerm('text', 'http://schema.org/text', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasMap(RdfProperty[schemaorg.URL | schemaorg.Map]):
    term = RdfTerm('hasMap', 'http://schema.org/hasMap', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class trainName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('trainName', 'http://schema.org/trainName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class width(RdfProperty[schemaorg.Distance | schemaorg.QuantitativeValue]):
    term = RdfTerm('width', 'http://schema.org/width', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class financialAidEligible(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('financialAidEligible', 'http://schema.org/financialAidEligible', ['1.1', '1.2-DRAFT'])

class producer(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('producer', 'http://schema.org/producer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderDelivery(RdfProperty[schemaorg.ParcelDelivery]):
    term = RdfTerm('orderDelivery', 'http://schema.org/orderDelivery', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class startDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('startDate', 'http://schema.org/startDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numChildren(RdfProperty[schemaorg.Integer | schemaorg.QuantitativeValue]):
    term = RdfTerm('numChildren', 'http://schema.org/numChildren', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dietFeatures(RdfProperty[schemaorg.Text]):
    term = RdfTerm('dietFeatures', 'http://schema.org/dietFeatures', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class authenticator(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('authenticator', 'http://schema.org/authenticator', ['1.0', '1.1', '1.2-DRAFT'])

class screenCount(RdfProperty[schemaorg.Number]):
    term = RdfTerm('screenCount', 'http://schema.org/screenCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class discountCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('discountCode', 'http://schema.org/discountCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class thumbnailUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('thumbnailUrl', 'http://schema.org/thumbnailUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dayOfWeek(RdfProperty[schemaorg.DayOfWeek]):
    term = RdfTerm('dayOfWeek', 'http://schema.org/dayOfWeek', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class warranty(RdfProperty[schemaorg.WarrantyPromise]):
    term = RdfTerm('warranty', 'http://schema.org/warranty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class illustrator(RdfProperty[schemaorg.Person]):
    term = RdfTerm('illustrator', 'http://schema.org/illustrator', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class installUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('installUrl', 'http://schema.org/installUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class parents(RdfProperty[schemaorg.Person]):
    term = RdfTerm('parents', 'http://schema.org/parents', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availableIn(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm('availableIn', 'http://schema.org/availableIn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class endorsee(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('endorsee', 'http://schema.org/endorsee', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class scheduledTime(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm('scheduledTime', 'http://schema.org/scheduledTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class scheduleTimezone(RdfProperty[schemaorg.Text]):
    term = RdfTerm('scheduleTimezone', 'http://schema.org/scheduleTimezone', ['1.1', '1.2-DRAFT'])

class seatingType(RdfProperty[schemaorg.QualitativeValue | schemaorg.Text]):
    term = RdfTerm('seatingType', 'http://schema.org/seatingType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class supportingData(RdfProperty[schemaorg.DataFeed]):
    term = RdfTerm('supportingData', 'http://schema.org/supportingData', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class strengthUnit(RdfProperty[schemaorg.Text]):
    term = RdfTerm('strengthUnit', 'http://schema.org/strengthUnit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class subEvent(RdfProperty[schemaorg.Event]):
    term = RdfTerm('subEvent', 'http://schema.org/subEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class discusses(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('discusses', 'http://schema.org/discusses', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class spouse(RdfProperty[schemaorg.Person]):
    term = RdfTerm('spouse', 'http://schema.org/spouse', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class energyEfficiencyScaleMin(RdfProperty[schemaorg.EUEnergyEfficiencyEnumeration]):
    term = RdfTerm('energyEfficiencyScaleMin', 'http://schema.org/energyEfficiencyScaleMin', ['1.1', '1.2-DRAFT'])

class exercisePlan(RdfProperty[schemaorg.ExercisePlan]):
    term = RdfTerm('exercisePlan', 'http://schema.org/exercisePlan', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class intensity(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm('intensity', 'http://schema.org/intensity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class warning(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('warning', 'http://schema.org/warning', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class targetPopulation(RdfProperty[schemaorg.Text]):
    term = RdfTerm('targetPopulation', 'http://schema.org/targetPopulation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class collection(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('collection', 'http://schema.org/collection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class agentInteractionStatistic(RdfProperty[schemaorg.InteractionCounter]):
    term = RdfTerm('agentInteractionStatistic', 'http://schema.org/agentInteractionStatistic', [])

class hiringOrganization(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('hiringOrganization', 'http://schema.org/hiringOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isbn(RdfProperty[schemaorg.Text]):
    term = RdfTerm('isbn', 'http://schema.org/isbn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class iso6523Code(RdfProperty[schemaorg.Text]):
    term = RdfTerm('iso6523Code', 'http://schema.org/iso6523Code', ['1.2-DRAFT'])

class relevantOccupation(RdfProperty[schemaorg.Occupation]):
    term = RdfTerm('relevantOccupation', 'http://schema.org/relevantOccupation', ['1.0', '1.1', '1.2-DRAFT'])

class experienceRequirements(RdfProperty[schemaorg.OccupationalExperienceRequirements | schemaorg.Text]):
    term = RdfTerm('experienceRequirements', 'http://schema.org/experienceRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mediaItemAppearance(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm('mediaItemAppearance', 'http://schema.org/mediaItemAppearance', ['1.2-DRAFT'])

class itemDefectReturnFees(RdfProperty[schemaorg.ReturnFeesEnumeration]):
    term = RdfTerm('itemDefectReturnFees', 'http://schema.org/itemDefectReturnFees', ['1.2-DRAFT'])

class repeatCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('repeatCount', 'http://schema.org/repeatCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class variantCover(RdfProperty[schemaorg.Text]):
    term = RdfTerm('variantCover', 'http://schema.org/variantCover', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sampleType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('sampleType', 'http://schema.org/sampleType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recourseLoan(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('recourseLoan', 'http://schema.org/recourseLoan', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class includedComposition(RdfProperty[schemaorg.MusicComposition]):
    term = RdfTerm('includedComposition', 'http://schema.org/includedComposition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sport(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('sport', 'http://schema.org/sport', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class copyrightHolder(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('copyrightHolder', 'http://schema.org/copyrightHolder', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class workPresented(RdfProperty[schemaorg.Movie]):
    term = RdfTerm('workPresented', 'http://schema.org/workPresented', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class quest(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('quest', 'http://schema.org/quest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class monthsOfExperience(RdfProperty[schemaorg.Number]):
    term = RdfTerm('monthsOfExperience', 'http://schema.org/monthsOfExperience', ['1.2-DRAFT'])

class numberOfLoanPayments(RdfProperty[schemaorg.Number]):
    term = RdfTerm('numberOfLoanPayments', 'http://schema.org/numberOfLoanPayments', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasMenu(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.Menu]):
    term = RdfTerm('hasMenu', 'http://schema.org/hasMenu', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class usedToDiagnose(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm('usedToDiagnose', 'http://schema.org/usedToDiagnose', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class wordCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('wordCount', 'http://schema.org/wordCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class occupationalCredentialAwarded(RdfProperty[schemaorg.EducationalOccupationalCredential | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('occupationalCredentialAwarded', 'http://schema.org/occupationalCredentialAwarded', ['1.0', '1.1', '1.2-DRAFT'])

class sourcedFrom(RdfProperty[schemaorg.BrainStructure]):
    term = RdfTerm('sourcedFrom', 'http://schema.org/sourcedFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class jobLocationType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('jobLocationType', 'http://schema.org/jobLocationType', ['1.0', '1.1', '1.2-DRAFT'])

class doseValue(RdfProperty[schemaorg.QualitativeValue | schemaorg.Number]):
    term = RdfTerm('doseValue', 'http://schema.org/doseValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoTouches(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm('geoTouches', 'http://schema.org/geoTouches', ['1.0', '1.1', '1.2-DRAFT'])

class hasMolecularFunction(RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('hasMolecularFunction', 'http://schema.org/hasMolecularFunction', ['1.2-DRAFT'])

class elevation(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('elevation', 'http://schema.org/elevation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class homeTeam(RdfProperty[schemaorg.Person | schemaorg.SportsTeam]):
    term = RdfTerm('homeTeam', 'http://schema.org/homeTeam', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bodyLocation(RdfProperty[schemaorg.Text]):
    term = RdfTerm('bodyLocation', 'http://schema.org/bodyLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasAdultConsideration(RdfProperty[schemaorg.AdultOrientedEnumeration]):
    term = RdfTerm('hasAdultConsideration', 'http://schema.org/hasAdultConsideration', ['1.2-DRAFT'])

class hasMenuItem(RdfProperty[schemaorg.MenuItem]):
    term = RdfTerm('hasMenuItem', 'http://schema.org/hasMenuItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class free(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('free', 'http://schema.org/free', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class directors(RdfProperty[schemaorg.Person]):
    term = RdfTerm('directors', 'http://schema.org/directors', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class actionAccessibilityRequirement(RdfProperty[schemaorg.ActionAccessSpecification]):
    term = RdfTerm('actionAccessibilityRequirement', 'http://schema.org/actionAccessibilityRequirement', ['1.0', '1.1', '1.2-DRAFT'])

class target(RdfProperty[schemaorg.EntryPoint | schemaorg.URL]):
    term = RdfTerm('target', 'http://schema.org/target', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class calories(RdfProperty[schemaorg.Energy]):
    term = RdfTerm('calories', 'http://schema.org/calories', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class articleBody(RdfProperty[schemaorg.Text]):
    term = RdfTerm('articleBody', 'http://schema.org/articleBody', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recordedAt(RdfProperty[schemaorg.Event]):
    term = RdfTerm('recordedAt', 'http://schema.org/recordedAt', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class boardingGroup(RdfProperty[schemaorg.Text]):
    term = RdfTerm('boardingGroup', 'http://schema.org/boardingGroup', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class biomechnicalClass(RdfProperty[schemaorg.Text]):
    term = RdfTerm('biomechnicalClass', 'http://schema.org/biomechnicalClass', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class audience(RdfProperty[schemaorg.Audience]):
    term = RdfTerm('audience', 'http://schema.org/audience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class distinguishingSign(RdfProperty[schemaorg.MedicalSignOrSymptom]):
    term = RdfTerm('distinguishingSign', 'http://schema.org/distinguishingSign', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class businessFunction(RdfProperty[schemaorg.BusinessFunction]):
    term = RdfTerm('businessFunction', 'http://schema.org/businessFunction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class weightPercentage(RdfProperty[schemaorg.Number]):
    term = RdfTerm('weightPercentage', 'http://schema.org/weightPercentage', [])

class spatial(RdfProperty[schemaorg.Place]):
    term = RdfTerm('spatial', 'http://schema.org/spatial', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class serviceOperator(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('serviceOperator', 'http://schema.org/serviceOperator', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class biologicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm('biologicalRole', 'http://schema.org/biologicalRole', ['1.2-DRAFT'])

class loanPaymentFrequency(RdfProperty[schemaorg.Number]):
    term = RdfTerm('loanPaymentFrequency', 'http://schema.org/loanPaymentFrequency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class interpretedAsClaim(RdfProperty[schemaorg.Claim]):
    term = RdfTerm('interpretedAsClaim', 'http://schema.org/interpretedAsClaim', ['1.2-DRAFT'])

class discountCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm('discountCurrency', 'http://schema.org/discountCurrency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class creditText(RdfProperty[schemaorg.Text]):
    term = RdfTerm('creditText', 'http://schema.org/creditText', ['1.2-DRAFT'])

class domiciledMortgage(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('domiciledMortgage', 'http://schema.org/domiciledMortgage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class encodesCreativeWork(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('encodesCreativeWork', 'http://schema.org/encodesCreativeWork', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class statType(RdfProperty[schemaorg.URL | schemaorg.Property | schemaorg.Text]):
    term = RdfTerm('statType', 'http://schema.org/statType', ['1.2-DRAFT'])

class course(RdfProperty[schemaorg.Place]):
    term = RdfTerm('course', 'http://schema.org/course', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fuelType(RdfProperty[schemaorg.Text | schemaorg.QualitativeValue | schemaorg.URL]):
    term = RdfTerm('fuelType', 'http://schema.org/fuelType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class associatedArticle(RdfProperty[schemaorg.NewsArticle]):
    term = RdfTerm('associatedArticle', 'http://schema.org/associatedArticle', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vehicleInteriorType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('vehicleInteriorType', 'http://schema.org/vehicleInteriorType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumVentUse(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumVentUse', 'http://schema.org/cvdNumVentUse', ['1.1', '1.2-DRAFT'])

class coach(RdfProperty[schemaorg.Person]):
    term = RdfTerm('coach', 'http://schema.org/coach', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class educationalRole(RdfProperty[schemaorg.Text]):
    term = RdfTerm('educationalRole', 'http://schema.org/educationalRole', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reviewBody(RdfProperty[schemaorg.Text]):
    term = RdfTerm('reviewBody', 'http://schema.org/reviewBody', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class byMonthDay(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('byMonthDay', 'http://schema.org/byMonthDay', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class endTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('endTime', 'http://schema.org/endTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class material(RdfProperty[schemaorg.Product | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('material', 'http://schema.org/material', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class amenityFeature(RdfProperty[schemaorg.LocationFeatureSpecification]):
    term = RdfTerm('amenityFeature', 'http://schema.org/amenityFeature', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class membershipNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('membershipNumber', 'http://schema.org/membershipNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dateReceived(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('dateReceived', 'http://schema.org/dateReceived', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class translator(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('translator', 'http://schema.org/translator', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arrivalTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('arrivalTime', 'http://schema.org/arrivalTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfItems(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('numberOfItems', 'http://schema.org/numberOfItems', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class greaterOrEqual(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm('greaterOrEqual', 'http://schema.org/greaterOrEqual', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bloodSupply(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm('bloodSupply', 'http://schema.org/bloodSupply', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class rsvpResponse(RdfProperty[schemaorg.RsvpResponseType]):
    term = RdfTerm('rsvpResponse', 'http://schema.org/rsvpResponse', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class auditDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('auditDate', 'http://schema.org/auditDate', [])

class suggestedMaxAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm('suggestedMaxAge', 'http://schema.org/suggestedMaxAge', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vehicleConfiguration(RdfProperty[schemaorg.Text]):
    term = RdfTerm('vehicleConfiguration', 'http://schema.org/vehicleConfiguration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class naturalProgression(RdfProperty[schemaorg.Text]):
    term = RdfTerm('naturalProgression', 'http://schema.org/naturalProgression', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class option(RdfProperty[schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm('option', 'http://schema.org/option', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class buyer(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('buyer', 'http://schema.org/buyer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class identifyingTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm('identifyingTest', 'http://schema.org/identifyingTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class blogPost(RdfProperty[schemaorg.BlogPosting]):
    term = RdfTerm('blogPost', 'http://schema.org/blogPost', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recordedIn(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('recordedIn', 'http://schema.org/recordedIn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class runtimePlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm('runtimePlatform', 'http://schema.org/runtimePlatform', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inAlbum(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm('inAlbum', 'http://schema.org/inAlbum', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class alignmentType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('alignmentType', 'http://schema.org/alignmentType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanCoinsuranceRate(RdfProperty[schemaorg.Number]):
    term = RdfTerm('healthPlanCoinsuranceRate', 'http://schema.org/healthPlanCoinsuranceRate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tickerSymbol(RdfProperty[schemaorg.Text]):
    term = RdfTerm('tickerSymbol', 'http://schema.org/tickerSymbol', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class applicableLocation(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm('applicableLocation', 'http://schema.org/applicableLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class preparation(RdfProperty[schemaorg.Text | schemaorg.MedicalEntity]):
    term = RdfTerm('preparation', 'http://schema.org/preparation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfEpisodes(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('numberOfEpisodes', 'http://schema.org/numberOfEpisodes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class announcementLocation(RdfProperty[schemaorg.LocalBusiness | schemaorg.CivicStructure]):
    term = RdfTerm('announcementLocation', 'http://schema.org/announcementLocation', ['1.1', '1.2-DRAFT'])

class actionApplication(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm('actionApplication', 'http://schema.org/actionApplication', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class candidate(RdfProperty[schemaorg.Person]):
    term = RdfTerm('candidate', 'http://schema.org/candidate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class character(RdfProperty[schemaorg.Person]):
    term = RdfTerm('character', 'http://schema.org/character', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class parentItem(RdfProperty[schemaorg.CreativeWork | schemaorg.Comment]):
    term = RdfTerm('parentItem', 'http://schema.org/parentItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class targetProduct(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm('targetProduct', 'http://schema.org/targetProduct', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sizeSystem(RdfProperty[schemaorg.Text | schemaorg.SizeSystemEnumeration]):
    term = RdfTerm('sizeSystem', 'http://schema.org/sizeSystem', ['1.2-DRAFT'])

class funder(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('funder', 'http://schema.org/funder', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class incentiveAmount(RdfProperty[schemaorg.QuantitativeValue | schemaorg.LoanOrCredit | schemaorg.UnitPriceSpecification]):
    term = RdfTerm('incentiveAmount', 'http://schema.org/incentiveAmount', [])

class address(RdfProperty[schemaorg.PostalAddress | schemaorg.Text]):
    term = RdfTerm('address', 'http://schema.org/address', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm('alternativeOf', 'http://schema.org/alternativeOf', ['1.2-DRAFT'])

class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm('additionalProperty', 'http://schema.org/additionalProperty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class significance(RdfProperty[schemaorg.Text]):
    term = RdfTerm('significance', 'http://schema.org/significance', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class doesNotShip(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('doesNotShip', 'http://schema.org/doesNotShip', ['1.1', '1.2-DRAFT'])

class additionalType(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('additionalType', 'http://schema.org/additionalType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class previousStartDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('previousStartDate', 'http://schema.org/previousStartDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class instrument(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('instrument', 'http://schema.org/instrument', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inSupportOf(RdfProperty[schemaorg.Text]):
    term = RdfTerm('inSupportOf', 'http://schema.org/inSupportOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class status(RdfProperty[schemaorg.EventStatusType | schemaorg.Text | schemaorg.MedicalStudyStatus]):
    term = RdfTerm('status', 'http://schema.org/status', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanId(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanId', 'http://schema.org/healthPlanId', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class programName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('programName', 'http://schema.org/programName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class typeOfGood(RdfProperty[schemaorg.Product | schemaorg.Service]):
    term = RdfTerm('typeOfGood', 'http://schema.org/typeOfGood', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class slogan(RdfProperty[schemaorg.Text]):
    term = RdfTerm('slogan', 'http://schema.org/slogan', ['1.0', '1.1', '1.2-DRAFT'])

class encodings(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm('encodings', 'http://schema.org/encodings', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arrivalBoatTerminal(RdfProperty[schemaorg.BoatTerminal]):
    term = RdfTerm('arrivalBoatTerminal', 'http://schema.org/arrivalBoatTerminal', ['1.1', '1.2-DRAFT'])

class additionalVariable(RdfProperty[schemaorg.Text]):
    term = RdfTerm('additionalVariable', 'http://schema.org/additionalVariable', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tissueSample(RdfProperty[schemaorg.Text]):
    term = RdfTerm('tissueSample', 'http://schema.org/tissueSample', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasMemberProgram(RdfProperty[schemaorg.MemberProgram]):
    term = RdfTerm('hasMemberProgram', 'http://schema.org/hasMemberProgram', [])

class duplicateTherapy(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm('duplicateTherapy', 'http://schema.org/duplicateTherapy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class floorLevel(RdfProperty[schemaorg.Text]):
    term = RdfTerm('floorLevel', 'http://schema.org/floorLevel', ['1.0', '1.1', '1.2-DRAFT'])

class educationalProgramMode(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('educationalProgramMode', 'http://schema.org/educationalProgramMode', ['1.1', '1.2-DRAFT'])

class depth(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Distance]):
    term = RdfTerm('depth', 'http://schema.org/depth', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class netWorth(RdfProperty[schemaorg.MonetaryAmount | schemaorg.PriceSpecification]):
    term = RdfTerm('netWorth', 'http://schema.org/netWorth', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasCourse(RdfProperty[schemaorg.Course]):
    term = RdfTerm('hasCourse', 'http://schema.org/hasCourse', ['1.1', '1.2-DRAFT'])

class proprietaryName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('proprietaryName', 'http://schema.org/proprietaryName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderItemStatus(RdfProperty[schemaorg.OrderStatus]):
    term = RdfTerm('orderItemStatus', 'http://schema.org/orderItemStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class memoryRequirements(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('memoryRequirements', 'http://schema.org/memoryRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class departureBoatTerminal(RdfProperty[schemaorg.BoatTerminal]):
    term = RdfTerm('departureBoatTerminal', 'http://schema.org/departureBoatTerminal', ['1.1', '1.2-DRAFT'])

class eligibleTransactionVolume(RdfProperty[schemaorg.PriceSpecification]):
    term = RdfTerm('eligibleTransactionVolume', 'http://schema.org/eligibleTransactionVolume', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class pageStart(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('pageStart', 'http://schema.org/pageStart', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contributor(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('contributor', 'http://schema.org/contributor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class benefitsSummaryUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('benefitsSummaryUrl', 'http://schema.org/benefitsSummaryUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class exerciseRelatedDiet(RdfProperty[schemaorg.Diet]):
    term = RdfTerm('exerciseRelatedDiet', 'http://schema.org/exerciseRelatedDiet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class maximumVirtualAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('maximumVirtualAttendeeCapacity', 'http://schema.org/maximumVirtualAttendeeCapacity', ['1.1', '1.2-DRAFT'])

class maximumIntake(RdfProperty[schemaorg.MaximumDoseSchedule]):
    term = RdfTerm('maximumIntake', 'http://schema.org/maximumIntake', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class position(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm('position', 'http://schema.org/position', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class correctionsPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('correctionsPolicy', 'http://schema.org/correctionsPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class replacee(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('replacee', 'http://schema.org/replacee', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class itemShipped(RdfProperty[schemaorg.Product]):
    term = RdfTerm('itemShipped', 'http://schema.org/itemShipped', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumBeds', 'http://schema.org/cvdNumBeds', ['1.1', '1.2-DRAFT'])

class priceRange(RdfProperty[schemaorg.Text]):
    term = RdfTerm('priceRange', 'http://schema.org/priceRange', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfInvoice(RdfProperty[schemaorg.Invoice]):
    term = RdfTerm('partOfInvoice', 'http://schema.org/partOfInvoice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class serviceUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('serviceUrl', 'http://schema.org/serviceUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class subTrip(RdfProperty[schemaorg.Trip]):
    term = RdfTerm('subTrip', 'http://schema.org/subTrip', ['1.0', '1.1', '1.2-DRAFT'])

class beneficiaryBank(RdfProperty[schemaorg.Text | schemaorg.BankOrCreditUnion]):
    term = RdfTerm('beneficiaryBank', 'http://schema.org/beneficiaryBank', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class potentialAction(RdfProperty[schemaorg.Action]):
    term = RdfTerm('potentialAction', 'http://schema.org/potentialAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class conditionsOfAccess(RdfProperty[schemaorg.Text]):
    term = RdfTerm('conditionsOfAccess', 'http://schema.org/conditionsOfAccess', ['1.0', '1.1', '1.2-DRAFT'])

class review(RdfProperty[schemaorg.Review]):
    term = RdfTerm('review', 'http://schema.org/review', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class temporalCoverage(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.DateTime]):
    term = RdfTerm('temporalCoverage', 'http://schema.org/temporalCoverage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class productGroupID(RdfProperty[schemaorg.Text]):
    term = RdfTerm('productGroupID', 'http://schema.org/productGroupID', ['1.1', '1.2-DRAFT'])

class defaultValue(RdfProperty[schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm('defaultValue', 'http://schema.org/defaultValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class molecularFormula(RdfProperty[schemaorg.Text]):
    term = RdfTerm('molecularFormula', 'http://schema.org/molecularFormula', ['1.2-DRAFT'])

class priceType(RdfProperty[schemaorg.PriceTypeEnumeration | schemaorg.Text]):
    term = RdfTerm('priceType', 'http://schema.org/priceType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class permitAudience(RdfProperty[schemaorg.Audience]):
    term = RdfTerm('permitAudience', 'http://schema.org/permitAudience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class mentions(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('mentions', 'http://schema.org/mentions', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class administrationRoute(RdfProperty[schemaorg.Text]):
    term = RdfTerm('administrationRoute', 'http://schema.org/administrationRoute', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationType(RdfProperty[schemaorg.Text | schemaorg.CategoryCode]):
    term = RdfTerm('legislationType', 'http://schema.org/legislationType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class increasesRiskOf(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm('increasesRiskOf', 'http://schema.org/increasesRiskOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class textValue(RdfProperty[schemaorg.Text]):
    term = RdfTerm('textValue', 'http://schema.org/textValue', ['1.1', '1.2-DRAFT'])

class reportNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('reportNumber', 'http://schema.org/reportNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dateSent(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('dateSent', 'http://schema.org/dateSent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class itemCondition(RdfProperty[schemaorg.OfferItemCondition]):
    term = RdfTerm('itemCondition', 'http://schema.org/itemCondition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm('hasBioPolymerSequence', 'http://schema.org/hasBioPolymerSequence', ['1.2-DRAFT'])

class relatedLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm('relatedLink', 'http://schema.org/relatedLink', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class deliveryAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm('deliveryAddress', 'http://schema.org/deliveryAddress', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class interactionStatistic(RdfProperty[schemaorg.InteractionCounter]):
    term = RdfTerm('interactionStatistic', 'http://schema.org/interactionStatistic', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class totalTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('totalTime', 'http://schema.org/totalTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class noBylinesPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('noBylinesPolicy', 'http://schema.org/noBylinesPolicy', ['1.0', '1.1', '1.2-DRAFT'])

class globalLocationNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('globalLocationNumber', 'http://schema.org/globalLocationNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class pregnancyCategory(RdfProperty[schemaorg.DrugPregnancyCategory]):
    term = RdfTerm('pregnancyCategory', 'http://schema.org/pregnancyCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class orderedItem(RdfProperty[schemaorg.Product | schemaorg.OrderItem | schemaorg.Service]):
    term = RdfTerm('orderedItem', 'http://schema.org/orderedItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class paymentDue(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('paymentDue', 'http://schema.org/paymentDue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class permissionType(RdfProperty[schemaorg.DigitalDocumentPermissionType]):
    term = RdfTerm('permissionType', 'http://schema.org/permissionType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sameAs(RdfProperty[schemaorg.URL]):
    term = RdfTerm('sameAs', 'http://schema.org/sameAs', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class modifiedTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('modifiedTime', 'http://schema.org/modifiedTime', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dependencies(RdfProperty[schemaorg.Text]):
    term = RdfTerm('dependencies', 'http://schema.org/dependencies', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class landlord(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('landlord', 'http://schema.org/landlord', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class diagnosis(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm('diagnosis', 'http://schema.org/diagnosis', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class loanMortgageMandateAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('loanMortgageMandateAmount', 'http://schema.org/loanMortgageMandateAmount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class serverStatus(RdfProperty[schemaorg.GameServerStatus]):
    term = RdfTerm('serverStatus', 'http://schema.org/serverStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class typicalCreditsPerTerm(RdfProperty[schemaorg.StructuredValue | schemaorg.Integer]):
    term = RdfTerm('typicalCreditsPerTerm', 'http://schema.org/typicalCreditsPerTerm', ['1.1', '1.2-DRAFT'])

class acceptsReservations(RdfProperty[schemaorg.Boolean | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('acceptsReservations', 'http://schema.org/acceptsReservations', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class eventAttendanceMode(RdfProperty[schemaorg.EventAttendanceModeEnumeration]):
    term = RdfTerm('eventAttendanceMode', 'http://schema.org/eventAttendanceMode', ['1.1', '1.2-DRAFT'])

class schemaVersion(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('schemaVersion', 'http://schema.org/schemaVersion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class physiologicalBenefits(RdfProperty[schemaorg.Text]):
    term = RdfTerm('physiologicalBenefits', 'http://schema.org/physiologicalBenefits', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasOccupation(RdfProperty[schemaorg.Occupation]):
    term = RdfTerm('hasOccupation', 'http://schema.org/hasOccupation', ['1.0', '1.1', '1.2-DRAFT'])

class acquireLicensePage(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('acquireLicensePage', 'http://schema.org/acquireLicensePage', ['1.1', '1.2-DRAFT'])

class priceComponent(RdfProperty[schemaorg.UnitPriceSpecification]):
    term = RdfTerm('priceComponent', 'http://schema.org/priceComponent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumC19Died(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumC19Died', 'http://schema.org/cvdNumC19Died', ['1.1', '1.2-DRAFT'])

class catalogNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('catalogNumber', 'http://schema.org/catalogNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ticketedSeat(RdfProperty[schemaorg.Seat]):
    term = RdfTerm('ticketedSeat', 'http://schema.org/ticketedSeat', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recipeIngredient(RdfProperty[schemaorg.Text]):
    term = RdfTerm('recipeIngredient', 'http://schema.org/recipeIngredient', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class starRating(RdfProperty[schemaorg.Rating]):
    term = RdfTerm('starRating', 'http://schema.org/starRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recipeInstructions(RdfProperty[schemaorg.ItemList | schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm('recipeInstructions', 'http://schema.org/recipeInstructions', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfSeason(RdfProperty[schemaorg.CreativeWorkSeason]):
    term = RdfTerm('partOfSeason', 'http://schema.org/partOfSeason', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class creditedTo(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('creditedTo', 'http://schema.org/creditedTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class restPeriods(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm('restPeriods', 'http://schema.org/restPeriods', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoWithin(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm('geoWithin', 'http://schema.org/geoWithin', ['1.0', '1.1', '1.2-DRAFT'])

class differentialDiagnosis(RdfProperty[schemaorg.DDxElement]):
    term = RdfTerm('differentialDiagnosis', 'http://schema.org/differentialDiagnosis', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numTracks(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('numTracks', 'http://schema.org/numTracks', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class eduQuestionType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('eduQuestionType', 'http://schema.org/eduQuestionType', ['1.1', '1.2-DRAFT'])

class referenceQuantity(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('referenceQuantity', 'http://schema.org/referenceQuantity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class deathPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm('deathPlace', 'http://schema.org/deathPlace', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class makesOffer(RdfProperty[schemaorg.Offer]):
    term = RdfTerm('makesOffer', 'http://schema.org/makesOffer', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class eligibilityToWorkRequirement(RdfProperty[schemaorg.Text]):
    term = RdfTerm('eligibilityToWorkRequirement', 'http://schema.org/eligibilityToWorkRequirement', ['1.1', '1.2-DRAFT'])

class dateVehicleFirstRegistered(RdfProperty[schemaorg.Date]):
    term = RdfTerm('dateVehicleFirstRegistered', 'http://schema.org/dateVehicleFirstRegistered', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumICUBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumICUBeds', 'http://schema.org/cvdNumICUBeds', ['1.1', '1.2-DRAFT'])

class deliveryStatus(RdfProperty[schemaorg.DeliveryEvent]):
    term = RdfTerm('deliveryStatus', 'http://schema.org/deliveryStatus', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vehicleIdentificationNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('vehicleIdentificationNumber', 'http://schema.org/vehicleIdentificationNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class successorOf(RdfProperty[schemaorg.ProductModel]):
    term = RdfTerm('successorOf', 'http://schema.org/successorOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reviewedBy(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('reviewedBy', 'http://schema.org/reviewedBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class measuredProperty(RdfProperty[schemaorg.Property]):
    term = RdfTerm('measuredProperty', 'http://schema.org/measuredProperty', ['1.0', '1.1', '1.2-DRAFT'])

class causeOf(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm('causeOf', 'http://schema.org/causeOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class printEdition(RdfProperty[schemaorg.Text]):
    term = RdfTerm('printEdition', 'http://schema.org/printEdition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class purchaseType(RdfProperty[schemaorg.PurchaseType]):
    term = RdfTerm('purchaseType', 'http://schema.org/purchaseType', [])

class sugarContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('sugarContent', 'http://schema.org/sugarContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class diet(RdfProperty[schemaorg.Diet]):
    term = RdfTerm('diet', 'http://schema.org/diet', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class department(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('department', 'http://schema.org/department', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publicTransportClosuresInfo(RdfProperty[schemaorg.WebContent | schemaorg.URL]):
    term = RdfTerm('publicTransportClosuresInfo', 'http://schema.org/publicTransportClosuresInfo', ['1.1', '1.2-DRAFT'])

class availableStrength(RdfProperty[schemaorg.DrugStrength]):
    term = RdfTerm('availableStrength', 'http://schema.org/availableStrength', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class appearance(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('appearance', 'http://schema.org/appearance', ['1.0', '1.1', '1.2-DRAFT'])

class observationAbout(RdfProperty[schemaorg.Place | schemaorg.Thing]):
    term = RdfTerm('observationAbout', 'http://schema.org/observationAbout', ['1.2-DRAFT'])

class bookEdition(RdfProperty[schemaorg.Text]):
    term = RdfTerm('bookEdition', 'http://schema.org/bookEdition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class clincalPharmacology(RdfProperty[schemaorg.Text]):
    term = RdfTerm('clincalPharmacology', 'http://schema.org/clincalPharmacology', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bookFormat(RdfProperty[schemaorg.BookFormatType]):
    term = RdfTerm('bookFormat', 'http://schema.org/bookFormat', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class codingSystem(RdfProperty[schemaorg.Text]):
    term = RdfTerm('codingSystem', 'http://schema.org/codingSystem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class quarantineGuidelines(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm('quarantineGuidelines', 'http://schema.org/quarantineGuidelines', ['1.1', '1.2-DRAFT'])

class epidemiology(RdfProperty[schemaorg.Text]):
    term = RdfTerm('epidemiology', 'http://schema.org/epidemiology', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class currenciesAccepted(RdfProperty[schemaorg.Text]):
    term = RdfTerm('currenciesAccepted', 'http://schema.org/currenciesAccepted', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationAmends(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm('legislationAmends', 'http://schema.org/legislationAmends', [])

class emissionsCO2(RdfProperty[schemaorg.Number]):
    term = RdfTerm('emissionsCO2', 'http://schema.org/emissionsCO2', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanMarketingUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('healthPlanMarketingUrl', 'http://schema.org/healthPlanMarketingUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class serviceSmsNumber(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm('serviceSmsNumber', 'http://schema.org/serviceSmsNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class comprisedOf(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem]):
    term = RdfTerm('comprisedOf', 'http://schema.org/comprisedOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sponsor(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('sponsor', 'http://schema.org/sponsor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recommendationStrength(RdfProperty[schemaorg.Text]):
    term = RdfTerm('recommendationStrength', 'http://schema.org/recommendationStrength', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class valueMaxLength(RdfProperty[schemaorg.Number]):
    term = RdfTerm('valueMaxLength', 'http://schema.org/valueMaxLength', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class itemDefectReturnShippingFeesAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('itemDefectReturnShippingFeesAmount', 'http://schema.org/itemDefectReturnShippingFeesAmount', ['1.2-DRAFT'])

class doseUnit(RdfProperty[schemaorg.Text]):
    term = RdfTerm('doseUnit', 'http://schema.org/doseUnit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class measurementTechnique(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL | schemaorg.MeasurementMethodEnum]):
    term = RdfTerm('measurementTechnique', 'http://schema.org/measurementTechnique', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ticketNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('ticketNumber', 'http://schema.org/ticketNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accountOverdraftLimit(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('accountOverdraftLimit', 'http://schema.org/accountOverdraftLimit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class measurementMethod(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.MeasurementMethodEnum | schemaorg.Text]):
    term = RdfTerm('measurementMethod', 'http://schema.org/measurementMethod', ['1.2-DRAFT'])

class relatedStructure(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('relatedStructure', 'http://schema.org/relatedStructure', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publisher(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('publisher', 'http://schema.org/publisher', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class applicationStartDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('applicationStartDate', 'http://schema.org/applicationStartDate', ['1.1', '1.2-DRAFT'])

class inChIKey(RdfProperty[schemaorg.Text]):
    term = RdfTerm('inChIKey', 'http://schema.org/inChIKey', ['1.2-DRAFT'])

class fiberContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('fiberContent', 'http://schema.org/fiberContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class knownVehicleDamages(RdfProperty[schemaorg.Text]):
    term = RdfTerm('knownVehicleDamages', 'http://schema.org/knownVehicleDamages', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accommodationCategory(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accommodationCategory', 'http://schema.org/accommodationCategory', ['1.0', '1.1', '1.2-DRAFT'])

class originAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm('originAddress', 'http://schema.org/originAddress', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class costCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm('costCurrency', 'http://schema.org/costCurrency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class episodes(RdfProperty[schemaorg.Episode]):
    term = RdfTerm('episodes', 'http://schema.org/episodes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class rangeIncludes(RdfProperty[schemaorg.Class]):
    term = RdfTerm('rangeIncludes', 'http://schema.org/rangeIncludes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class relatedAnatomy(RdfProperty[schemaorg.AnatomicalSystem | schemaorg.AnatomicalStructure]):
    term = RdfTerm('relatedAnatomy', 'http://schema.org/relatedAnatomy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class guidelineDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('guidelineDate', 'http://schema.org/guidelineDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class httpMethod(RdfProperty[schemaorg.Text]):
    term = RdfTerm('httpMethod', 'http://schema.org/httpMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class repetitions(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('repetitions', 'http://schema.org/repetitions', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class nsn(RdfProperty[schemaorg.Text]):
    term = RdfTerm('nsn', 'http://schema.org/nsn', ['1.0', '1.1', '1.2-DRAFT'])

class foodEstablishment(RdfProperty[schemaorg.FoodEstablishment | schemaorg.Place]):
    term = RdfTerm('foodEstablishment', 'http://schema.org/foodEstablishment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class positiveNotes(RdfProperty[schemaorg.WebContent | schemaorg.Text | schemaorg.ItemList | schemaorg.ListItem]):
    term = RdfTerm('positiveNotes', 'http://schema.org/positiveNotes', ['1.2-DRAFT'])

class softwareHelp(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('softwareHelp', 'http://schema.org/softwareHelp', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publishedOn(RdfProperty[schemaorg.BroadcastService]):
    term = RdfTerm('publishedOn', 'http://schema.org/publishedOn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class assesses(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('assesses', 'http://schema.org/assesses', ['1.1', '1.2-DRAFT'])

class ingredients(RdfProperty[schemaorg.Text]):
    term = RdfTerm('ingredients', 'http://schema.org/ingredients', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class appliesToDeliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm('appliesToDeliveryMethod', 'http://schema.org/appliesToDeliveryMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class repeatFrequency(RdfProperty[schemaorg.Duration | schemaorg.Text]):
    term = RdfTerm('repeatFrequency', 'http://schema.org/repeatFrequency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberedPosition(RdfProperty[schemaorg.Number]):
    term = RdfTerm('numberedPosition', 'http://schema.org/numberedPosition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class energyEfficiencyScaleMax(RdfProperty[schemaorg.EUEnergyEfficiencyEnumeration]):
    term = RdfTerm('energyEfficiencyScaleMax', 'http://schema.org/energyEfficiencyScaleMax', ['1.1', '1.2-DRAFT'])

class postalCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('postalCode', 'http://schema.org/postalCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gameLocation(RdfProperty[schemaorg.URL | schemaorg.Place | schemaorg.PostalAddress]):
    term = RdfTerm('gameLocation', 'http://schema.org/gameLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class foodWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm('foodWarning', 'http://schema.org/foodWarning', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class exifData(RdfProperty[schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm('exifData', 'http://schema.org/exifData', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class spatialCoverage(RdfProperty[schemaorg.Place]):
    term = RdfTerm('spatialCoverage', 'http://schema.org/spatialCoverage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class size(RdfProperty[schemaorg.QuantitativeValue | schemaorg.DefinedTerm | schemaorg.SizeSpecification | schemaorg.Text]):
    term = RdfTerm('size', 'http://schema.org/size', ['1.1', '1.2-DRAFT'])

class includesObject(RdfProperty[schemaorg.TypeAndQuantityNode]):
    term = RdfTerm('includesObject', 'http://schema.org/includesObject', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class loanPaymentAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('loanPaymentAmount', 'http://schema.org/loanPaymentAmount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recipeYield(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm('recipeYield', 'http://schema.org/recipeYield', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanDrugTier(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanDrugTier', 'http://schema.org/healthPlanDrugTier', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class postalCodeEnd(RdfProperty[schemaorg.Text]):
    term = RdfTerm('postalCodeEnd', 'http://schema.org/postalCodeEnd', ['1.1', '1.2-DRAFT'])

class track(RdfProperty[schemaorg.MusicRecording | schemaorg.ItemList]):
    term = RdfTerm('track', 'http://schema.org/track', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class image(RdfProperty[schemaorg.ImageObject | schemaorg.URL]):
    term = RdfTerm('image', 'http://schema.org/image', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class messageAttachment(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('messageAttachment', 'http://schema.org/messageAttachment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class priceCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm('priceCurrency', 'http://schema.org/priceCurrency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class maximumEnrollment(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('maximumEnrollment', 'http://schema.org/maximumEnrollment', ['1.1', '1.2-DRAFT'])

class participant(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('participant', 'http://schema.org/participant', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sizeGroup(RdfProperty[schemaorg.SizeGroupEnumeration | schemaorg.Text]):
    term = RdfTerm('sizeGroup', 'http://schema.org/sizeGroup', ['1.2-DRAFT'])

class memberOf(RdfProperty[schemaorg.Organization | schemaorg.ProgramMembership | schemaorg.MemberProgramTier]):
    term = RdfTerm('memberOf', 'http://schema.org/memberOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contentRating(RdfProperty[schemaorg.Text | schemaorg.Rating]):
    term = RdfTerm('contentRating', 'http://schema.org/contentRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class expressedIn(RdfProperty[schemaorg.AnatomicalStructure | schemaorg.BioChemEntity | schemaorg.DefinedTerm | schemaorg.AnatomicalSystem]):
    term = RdfTerm('expressedIn', 'http://schema.org/expressedIn', ['1.2-DRAFT'])

class hasOfferCatalog(RdfProperty[schemaorg.OfferCatalog]):
    term = RdfTerm('hasOfferCatalog', 'http://schema.org/hasOfferCatalog', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accessMode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accessMode', 'http://schema.org/accessMode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class valueRequired(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('valueRequired', 'http://schema.org/valueRequired', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfSeries(RdfProperty[schemaorg.CreativeWorkSeries]):
    term = RdfTerm('partOfSeries', 'http://schema.org/partOfSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class tracks(RdfProperty[schemaorg.MusicRecording]):
    term = RdfTerm('tracks', 'http://schema.org/tracks', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class documentation(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('documentation', 'http://schema.org/documentation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class creator(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('creator', 'http://schema.org/creator', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class targetCollection(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('targetCollection', 'http://schema.org/targetCollection', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class jobLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('jobLocation', 'http://schema.org/jobLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class deliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm('deliveryMethod', 'http://schema.org/deliveryMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class numberOfPages(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('numberOfPages', 'http://schema.org/numberOfPages', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class arrivalAirport(RdfProperty[schemaorg.Airport]):
    term = RdfTerm('arrivalAirport', 'http://schema.org/arrivalAirport', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class nonEqual(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm('nonEqual', 'http://schema.org/nonEqual', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class produces(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('produces', 'http://schema.org/produces', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class expectedArrivalFrom(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('expectedArrivalFrom', 'http://schema.org/expectedArrivalFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanCopayOption(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanCopayOption', 'http://schema.org/healthPlanCopayOption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class vehicleSeatingCapacity(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm('vehicleSeatingCapacity', 'http://schema.org/vehicleSeatingCapacity', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class carrier(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('carrier', 'http://schema.org/carrier', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class smokingAllowed(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('smokingAllowed', 'http://schema.org/smokingAllowed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class breadcrumb(RdfProperty[schemaorg.Text | schemaorg.BreadcrumbList]):
    term = RdfTerm('breadcrumb', 'http://schema.org/breadcrumb', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class normalRange(RdfProperty[schemaorg.Text | schemaorg.MedicalEnumeration]):
    term = RdfTerm('normalRange', 'http://schema.org/normalRange', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ineligibleRegion(RdfProperty[schemaorg.Text | schemaorg.GeoShape | schemaorg.Place]):
    term = RdfTerm('ineligibleRegion', 'http://schema.org/ineligibleRegion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ownedThrough(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('ownedThrough', 'http://schema.org/ownedThrough', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class aircraft(RdfProperty[schemaorg.Text | schemaorg.Vehicle]):
    term = RdfTerm('aircraft', 'http://schema.org/aircraft', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accountMinimumInflow(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('accountMinimumInflow', 'http://schema.org/accountMinimumInflow', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumC19HOPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumC19HOPats', 'http://schema.org/cvdNumC19HOPats', ['1.1', '1.2-DRAFT'])

class hasEnergyConsumptionDetails(RdfProperty[schemaorg.EnergyConsumptionDetails]):
    term = RdfTerm('hasEnergyConsumptionDetails', 'http://schema.org/hasEnergyConsumptionDetails', ['1.1', '1.2-DRAFT'])

class trackingUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('trackingUrl', 'http://schema.org/trackingUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class unitCode(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('unitCode', 'http://schema.org/unitCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class returnPolicySeasonalOverride(RdfProperty[schemaorg.MerchantReturnPolicySeasonalOverride]):
    term = RdfTerm('returnPolicySeasonalOverride', 'http://schema.org/returnPolicySeasonalOverride', ['1.2-DRAFT'])

class healthPlanPharmacyCategory(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanPharmacyCategory', 'http://schema.org/healthPlanPharmacyCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class previousItem(RdfProperty[schemaorg.ListItem]):
    term = RdfTerm('previousItem', 'http://schema.org/previousItem', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class requiredCollateral(RdfProperty[schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm('requiredCollateral', 'http://schema.org/requiredCollateral', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cashBack(RdfProperty[schemaorg.Boolean | schemaorg.Number]):
    term = RdfTerm('cashBack', 'http://schema.org/cashBack', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class diversityStaffingReport(RdfProperty[schemaorg.URL | schemaorg.Article]):
    term = RdfTerm('diversityStaffingReport', 'http://schema.org/diversityStaffingReport', ['1.0', '1.1', '1.2-DRAFT'])

class datasetTimeInterval(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm('datasetTimeInterval', 'http://schema.org/datasetTimeInterval', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class awayTeam(RdfProperty[schemaorg.Person | schemaorg.SportsTeam]):
    term = RdfTerm('awayTeam', 'http://schema.org/awayTeam', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class discount(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('discount', 'http://schema.org/discount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class priceComponentType(RdfProperty[schemaorg.PriceComponentTypeEnumeration]):
    term = RdfTerm('priceComponentType', 'http://schema.org/priceComponentType', ['1.2-DRAFT'])

class productionCompany(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('productionCompany', 'http://schema.org/productionCompany', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class claimReviewed(RdfProperty[schemaorg.Text]):
    term = RdfTerm('claimReviewed', 'http://schema.org/claimReviewed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class supplyTo(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('supplyTo', 'http://schema.org/supplyTo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class workload(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Energy]):
    term = RdfTerm('workload', 'http://schema.org/workload', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gtin14(RdfProperty[schemaorg.Text]):
    term = RdfTerm('gtin14', 'http://schema.org/gtin14', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class height(RdfProperty[schemaorg.Distance | schemaorg.QuantitativeValue]):
    term = RdfTerm('height', 'http://schema.org/height', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class trailerWeight(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('trailerWeight', 'http://schema.org/trailerWeight', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class exerciseType(RdfProperty[schemaorg.Text]):
    term = RdfTerm('exerciseType', 'http://schema.org/exerciseType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class issn(RdfProperty[schemaorg.Text]):
    term = RdfTerm('issn', 'http://schema.org/issn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class readonlyValue(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('readonlyValue', 'http://schema.org/readonlyValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class duns(RdfProperty[schemaorg.Text]):
    term = RdfTerm('duns', 'http://schema.org/duns', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class ethicsPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('ethicsPolicy', 'http://schema.org/ethicsPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class stage(RdfProperty[schemaorg.MedicalConditionStage]):
    term = RdfTerm('stage', 'http://schema.org/stage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class downvoteCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('downvoteCount', 'http://schema.org/downvoteCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class releasedEvent(RdfProperty[schemaorg.PublicationEvent]):
    term = RdfTerm('releasedEvent', 'http://schema.org/releasedEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class longitude(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('longitude', 'http://schema.org/longitude', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class prescribingInfo(RdfProperty[schemaorg.URL]):
    term = RdfTerm('prescribingInfo', 'http://schema.org/prescribingInfo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class applicationDeadline(RdfProperty[schemaorg.Text | schemaorg.Date]):
    term = RdfTerm('applicationDeadline', 'http://schema.org/applicationDeadline', ['1.1', '1.2-DRAFT'])

class taxonRank(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.PropertyValue]):
    term = RdfTerm('taxonRank', 'http://schema.org/taxonRank', ['1.2-DRAFT'])

class subReservation(RdfProperty[schemaorg.Reservation]):
    term = RdfTerm('subReservation', 'http://schema.org/subReservation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gameTip(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('gameTip', 'http://schema.org/gameTip', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class shippingDestination(RdfProperty[schemaorg.DefinedRegion]):
    term = RdfTerm('shippingDestination', 'http://schema.org/shippingDestination', ['1.1', '1.2-DRAFT'])

class mainContentOfPage(RdfProperty[schemaorg.WebPageElement]):
    term = RdfTerm('mainContentOfPage', 'http://schema.org/mainContentOfPage', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class familyName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('familyName', 'http://schema.org/familyName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class titleEIDR(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('titleEIDR', 'http://schema.org/titleEIDR', ['1.1', '1.2-DRAFT'])

class musicGroupMember(RdfProperty[schemaorg.Person]):
    term = RdfTerm('musicGroupMember', 'http://schema.org/musicGroupMember', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class sensoryRequirement(RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm('sensoryRequirement', 'http://schema.org/sensoryRequirement', ['1.1', '1.2-DRAFT'])

class actionableFeedbackPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm('actionableFeedbackPolicy', 'http://schema.org/actionableFeedbackPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class supply(RdfProperty[schemaorg.HowToSupply | schemaorg.Text]):
    term = RdfTerm('supply', 'http://schema.org/supply', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class accessibilitySummary(RdfProperty[schemaorg.Text]):
    term = RdfTerm('accessibilitySummary', 'http://schema.org/accessibilitySummary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class translationOfWork(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm('translationOfWork', 'http://schema.org/translationOfWork', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class roleName(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('roleName', 'http://schema.org/roleName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class significantLinks(RdfProperty[schemaorg.URL]):
    term = RdfTerm('significantLinks', 'http://schema.org/significantLinks', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class purchaseDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('purchaseDate', 'http://schema.org/purchaseDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class interactionService(RdfProperty[schemaorg.SoftwareApplication | schemaorg.WebSite]):
    term = RdfTerm('interactionService', 'http://schema.org/interactionService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fulfillmentType(RdfProperty[schemaorg.FulfillmentTypeEnumeration]):
    term = RdfTerm('fulfillmentType', 'http://schema.org/fulfillmentType', [])

class typicalTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm('typicalTest', 'http://schema.org/typicalTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class areaServed(RdfProperty[schemaorg.Text | schemaorg.AdministrativeArea | schemaorg.GeoShape | schemaorg.Place]):
    term = RdfTerm('areaServed', 'http://schema.org/areaServed', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class serviceAudience(RdfProperty[schemaorg.Audience]):
    term = RdfTerm('serviceAudience', 'http://schema.org/serviceAudience', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class recipeCategory(RdfProperty[schemaorg.Text]):
    term = RdfTerm('recipeCategory', 'http://schema.org/recipeCategory', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class employerOverview(RdfProperty[schemaorg.Text]):
    term = RdfTerm('employerOverview', 'http://schema.org/employerOverview', ['1.1', '1.2-DRAFT'])

class cvdNumC19OverflowPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumC19OverflowPats', 'http://schema.org/cvdNumC19OverflowPats', ['1.1', '1.2-DRAFT'])

class incentives(RdfProperty[schemaorg.Text]):
    term = RdfTerm('incentives', 'http://schema.org/incentives', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class smiles(RdfProperty[schemaorg.Text]):
    term = RdfTerm('smiles', 'http://schema.org/smiles', ['1.2-DRAFT'])

class proficiencyLevel(RdfProperty[schemaorg.Text]):
    term = RdfTerm('proficiencyLevel', 'http://schema.org/proficiencyLevel', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class pathophysiology(RdfProperty[schemaorg.Text]):
    term = RdfTerm('pathophysiology', 'http://schema.org/pathophysiology', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoDisjoint(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm('geoDisjoint', 'http://schema.org/geoDisjoint', ['1.0', '1.1', '1.2-DRAFT'])

class legislationCountersignedBy(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('legislationCountersignedBy', 'http://schema.org/legislationCountersignedBy', [])

class medicalAudience(RdfProperty[schemaorg.MedicalAudienceType | schemaorg.MedicalAudience]):
    term = RdfTerm('medicalAudience', 'http://schema.org/medicalAudience', ['1.1', '1.2-DRAFT'])

class worksFor(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('worksFor', 'http://schema.org/worksFor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reviewAspect(RdfProperty[schemaorg.Text]):
    term = RdfTerm('reviewAspect', 'http://schema.org/reviewAspect', ['1.0', '1.1', '1.2-DRAFT'])

class minimumPaymentDue(RdfProperty[schemaorg.PriceSpecification | schemaorg.MonetaryAmount]):
    term = RdfTerm('minimumPaymentDue', 'http://schema.org/minimumPaymentDue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class members(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('members', 'http://schema.org/members', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class postalCodePrefix(RdfProperty[schemaorg.Text]):
    term = RdfTerm('postalCodePrefix', 'http://schema.org/postalCodePrefix', ['1.1', '1.2-DRAFT'])

class strengthValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm('strengthValue', 'http://schema.org/strengthValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationLegalForce(RdfProperty[schemaorg.LegalForceStatus]):
    term = RdfTerm('legislationLegalForce', 'http://schema.org/legislationLegalForce', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class publisherImprint(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('publisherImprint', 'http://schema.org/publisherImprint', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class typicalAgeRange(RdfProperty[schemaorg.Text]):
    term = RdfTerm('typicalAgeRange', 'http://schema.org/typicalAgeRange', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationPassedBy(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm('legislationPassedBy', 'http://schema.org/legislationPassedBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class refundType(RdfProperty[schemaorg.RefundTypeEnumeration]):
    term = RdfTerm('refundType', 'http://schema.org/refundType', ['1.0', '1.1', '1.2-DRAFT'])

class isPartOfBioChemEntity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm('isPartOfBioChemEntity', 'http://schema.org/isPartOfBioChemEntity', ['1.2-DRAFT'])

class comment(RdfProperty[schemaorg.Comment]):
    term = RdfTerm('comment', 'http://schema.org/comment', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class governmentBenefitsInfo(RdfProperty[schemaorg.GovernmentService]):
    term = RdfTerm('governmentBenefitsInfo', 'http://schema.org/governmentBenefitsInfo', ['1.1', '1.2-DRAFT'])

class practicesAt(RdfProperty[schemaorg.MedicalOrganization]):
    term = RdfTerm('practicesAt', 'http://schema.org/practicesAt', [])

class bitrate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('bitrate', 'http://schema.org/bitrate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class musicalKey(RdfProperty[schemaorg.Text]):
    term = RdfTerm('musicalKey', 'http://schema.org/musicalKey', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class boardingPolicy(RdfProperty[schemaorg.BoardingPolicyType]):
    term = RdfTerm('boardingPolicy', 'http://schema.org/boardingPolicy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class encoding(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm('encoding', 'http://schema.org/encoding', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class userInteractionCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('userInteractionCount', 'http://schema.org/userInteractionCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class bookingAgent(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('bookingAgent', 'http://schema.org/bookingAgent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class minValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm('minValue', 'http://schema.org/minValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class enginePower(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('enginePower', 'http://schema.org/enginePower', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class discussionUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('discussionUrl', 'http://schema.org/discussionUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class lowPrice(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm('lowPrice', 'http://schema.org/lowPrice', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class competencyRequired(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm | schemaorg.URL]):
    term = RdfTerm('competencyRequired', 'http://schema.org/competencyRequired', ['1.0', '1.1', '1.2-DRAFT'])

class title(RdfProperty[schemaorg.Text]):
    term = RdfTerm('title', 'http://schema.org/title', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class layoutImage(RdfProperty[schemaorg.ImageObject | schemaorg.URL]):
    term = RdfTerm('layoutImage', 'http://schema.org/layoutImage', ['1.1', '1.2-DRAFT'])

class proteinContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('proteinContent', 'http://schema.org/proteinContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class checkoutPageURLTemplate(RdfProperty[schemaorg.Text]):
    term = RdfTerm('checkoutPageURLTemplate', 'http://schema.org/checkoutPageURLTemplate', ['1.2-DRAFT'])

class member(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('member', 'http://schema.org/member', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class healthPlanNetworkTier(RdfProperty[schemaorg.Text]):
    term = RdfTerm('healthPlanNetworkTier', 'http://schema.org/healthPlanNetworkTier', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class transitTime(RdfProperty[schemaorg.ServicePeriod | schemaorg.QuantitativeValue]):
    term = RdfTerm('transitTime', 'http://schema.org/transitTime', ['1.1', '1.2-DRAFT'])

class predecessorOf(RdfProperty[schemaorg.ProductModel]):
    term = RdfTerm('predecessorOf', 'http://schema.org/predecessorOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class legislationDateVersion(RdfProperty[schemaorg.Date]):
    term = RdfTerm('legislationDateVersion', 'http://schema.org/legislationDateVersion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoCovers(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm('geoCovers', 'http://schema.org/geoCovers', ['1.0', '1.1', '1.2-DRAFT'])

class studyLocation(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm('studyLocation', 'http://schema.org/studyLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class albumProductionType(RdfProperty[schemaorg.MusicAlbumProductionType]):
    term = RdfTerm('albumProductionType', 'http://schema.org/albumProductionType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class inPlaylist(RdfProperty[schemaorg.MusicPlaylist]):
    term = RdfTerm('inPlaylist', 'http://schema.org/inPlaylist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class billingStart(RdfProperty[schemaorg.Number]):
    term = RdfTerm('billingStart', 'http://schema.org/billingStart', ['1.2-DRAFT'])

class cvdCollectionDate(RdfProperty[schemaorg.DateTime | schemaorg.Text]):
    term = RdfTerm('cvdCollectionDate', 'http://schema.org/cvdCollectionDate', ['1.1', '1.2-DRAFT'])

class confirmationNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('confirmationNumber', 'http://schema.org/confirmationNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class targetDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm('targetDescription', 'http://schema.org/targetDescription', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class superEvent(RdfProperty[schemaorg.Event]):
    term = RdfTerm('superEvent', 'http://schema.org/superEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class transitTimeLabel(RdfProperty[schemaorg.Text]):
    term = RdfTerm('transitTimeLabel', 'http://schema.org/transitTimeLabel', ['1.1', '1.2-DRAFT'])

class timeRequired(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('timeRequired', 'http://schema.org/timeRequired', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class dissolutionDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm('dissolutionDate', 'http://schema.org/dissolutionDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class acceptedPaymentMethod(RdfProperty[schemaorg.PaymentMethod | schemaorg.Text | schemaorg.LoanOrCredit]):
    term = RdfTerm('acceptedPaymentMethod', 'http://schema.org/acceptedPaymentMethod', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class realEstateAgent(RdfProperty[schemaorg.RealEstateAgent]):
    term = RdfTerm('realEstateAgent', 'http://schema.org/realEstateAgent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class beforeMedia(RdfProperty[schemaorg.MediaObject | schemaorg.URL]):
    term = RdfTerm('beforeMedia', 'http://schema.org/beforeMedia', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class follows(RdfProperty[schemaorg.Person]):
    term = RdfTerm('follows', 'http://schema.org/follows', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isVariantOf(RdfProperty[schemaorg.ProductModel | schemaorg.ProductGroup]):
    term = RdfTerm('isVariantOf', 'http://schema.org/isVariantOf', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class busName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('busName', 'http://schema.org/busName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reservationFor(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('reservationFor', 'http://schema.org/reservationFor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class qualifiedExpense(RdfProperty[schemaorg.IncentiveQualifiedExpenseType]):
    term = RdfTerm('qualifiedExpense', 'http://schema.org/qualifiedExpense', [])

class founder(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('founder', 'http://schema.org/founder', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class providesService(RdfProperty[schemaorg.Service]):
    term = RdfTerm('providesService', 'http://schema.org/providesService', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isAccessibleForFree(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isAccessibleForFree', 'http://schema.org/isAccessibleForFree', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumVent(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumVent', 'http://schema.org/cvdNumVent', ['1.1', '1.2-DRAFT'])

class storageRequirements(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('storageRequirements', 'http://schema.org/storageRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class occupancy(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm('occupancy', 'http://schema.org/occupancy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class procedureType(RdfProperty[schemaorg.MedicalProcedureType]):
    term = RdfTerm('procedureType', 'http://schema.org/procedureType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class earlyPrepaymentPenalty(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm('earlyPrepaymentPenalty', 'http://schema.org/earlyPrepaymentPenalty', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class softwareRequirements(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('softwareRequirements', 'http://schema.org/softwareRequirements', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class photo(RdfProperty[schemaorg.ImageObject | schemaorg.Photograph]):
    term = RdfTerm('photo', 'http://schema.org/photo', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gtin8(RdfProperty[schemaorg.Text]):
    term = RdfTerm('gtin8', 'http://schema.org/gtin8', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class industry(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm('industry', 'http://schema.org/industry', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class audio(RdfProperty[schemaorg.AudioObject | schemaorg.MusicRecording | schemaorg.Clip]):
    term = RdfTerm('audio', 'http://schema.org/audio', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class program(RdfProperty[schemaorg.MemberProgram]):
    term = RdfTerm('program', 'http://schema.org/program', [])

class courseCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('courseCode', 'http://schema.org/courseCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class startOffset(RdfProperty[schemaorg.HyperTocEntry | schemaorg.Number]):
    term = RdfTerm('startOffset', 'http://schema.org/startOffset', ['1.0', '1.1', '1.2-DRAFT'])

class characterAttribute(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('characterAttribute', 'http://schema.org/characterAttribute', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availableAtOrFrom(RdfProperty[schemaorg.Place]):
    term = RdfTerm('availableAtOrFrom', 'http://schema.org/availableAtOrFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class correction(RdfProperty[schemaorg.CorrectionComment | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('correction', 'http://schema.org/correction', ['1.0', '1.1', '1.2-DRAFT'])

class includesHealthPlanFormulary(RdfProperty[schemaorg.HealthPlanFormulary]):
    term = RdfTerm('includesHealthPlanFormulary', 'http://schema.org/includesHealthPlanFormulary', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class faxNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm('faxNumber', 'http://schema.org/faxNumber', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class foodEvent(RdfProperty[schemaorg.FoodEvent]):
    term = RdfTerm('foodEvent', 'http://schema.org/foodEvent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contactPoint(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm('contactPoint', 'http://schema.org/contactPoint', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class muscleAction(RdfProperty[schemaorg.Text]):
    term = RdfTerm('muscleAction', 'http://schema.org/muscleAction', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class salaryCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm('salaryCurrency', 'http://schema.org/salaryCurrency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class cvdNumC19OFMechVentPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumC19OFMechVentPats', 'http://schema.org/cvdNumC19OFMechVentPats', ['1.1', '1.2-DRAFT'])

class bestRating(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('bestRating', 'http://schema.org/bestRating', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastFrequencyValue(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm('broadcastFrequencyValue', 'http://schema.org/broadcastFrequencyValue', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class applicableCountry(RdfProperty[schemaorg.Country | schemaorg.Text]):
    term = RdfTerm('applicableCountry', 'http://schema.org/applicableCountry', ['1.2-DRAFT'])

class chemicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm('chemicalRole', 'http://schema.org/chemicalRole', ['1.2-DRAFT'])

class author(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('author', 'http://schema.org/author', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class iataCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('iataCode', 'http://schema.org/iataCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class fatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('fatContent', 'http://schema.org/fatContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class branchCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm('branchCode', 'http://schema.org/branchCode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class clinicalPharmacology(RdfProperty[schemaorg.Text]):
    term = RdfTerm('clinicalPharmacology', 'http://schema.org/clinicalPharmacology', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class travelBans(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm('travelBans', 'http://schema.org/travelBans', ['1.1', '1.2-DRAFT'])

class safetyConsideration(RdfProperty[schemaorg.Text]):
    term = RdfTerm('safetyConsideration', 'http://schema.org/safetyConsideration', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class carbohydrateContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('carbohydrateContent', 'http://schema.org/carbohydrateContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class eligibleWithSupplier(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('eligibleWithSupplier', 'http://schema.org/eligibleWithSupplier', [])

class itemOffered(RdfProperty[schemaorg.Trip | schemaorg.Product | schemaorg.AggregateOffer | schemaorg.MenuItem | schemaorg.Service | schemaorg.Event | schemaorg.CreativeWork]):
    term = RdfTerm('itemOffered', 'http://schema.org/itemOffered', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class serviceType(RdfProperty[schemaorg.Text | schemaorg.GovernmentBenefitsType]):
    term = RdfTerm('serviceType', 'http://schema.org/serviceType', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availableTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm('availableTest', 'http://schema.org/availableTest', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class pickupLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('pickupLocation', 'http://schema.org/pickupLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class restockingFee(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Number]):
    term = RdfTerm('restockingFee', 'http://schema.org/restockingFee', ['1.2-DRAFT'])

class masthead(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm('masthead', 'http://schema.org/masthead', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class code(RdfProperty[schemaorg.MedicalCode]):
    term = RdfTerm('code', 'http://schema.org/code', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class saturatedFatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm('saturatedFatContent', 'http://schema.org/saturatedFatContent', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class productReturnDays(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('productReturnDays', 'http://schema.org/productReturnDays', ['1.0', '1.1', '1.2-DRAFT'])

class byArtist(RdfProperty[schemaorg.MusicGroup | schemaorg.Person]):
    term = RdfTerm('byArtist', 'http://schema.org/byArtist', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class musicCompositionForm(RdfProperty[schemaorg.Text]):
    term = RdfTerm('musicCompositionForm', 'http://schema.org/musicCompositionForm', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class assembly(RdfProperty[schemaorg.Text]):
    term = RdfTerm('assembly', 'http://schema.org/assembly', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class isUnlabelledFallback(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('isUnlabelledFallback', 'http://schema.org/isUnlabelledFallback', ['1.1', '1.2-DRAFT'])

class cvdNumC19MechVentPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm('cvdNumC19MechVentPats', 'http://schema.org/cvdNumC19MechVentPats', ['1.1', '1.2-DRAFT'])

class significantLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm('significantLink', 'http://schema.org/significantLink', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class steeringPosition(RdfProperty[schemaorg.SteeringPositionValue]):
    term = RdfTerm('steeringPosition', 'http://schema.org/steeringPosition', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class observationPeriod(RdfProperty[schemaorg.Text]):
    term = RdfTerm('observationPeriod', 'http://schema.org/observationPeriod', ['1.2-DRAFT'])

class honorificSuffix(RdfProperty[schemaorg.Text]):
    term = RdfTerm('honorificSuffix', 'http://schema.org/honorificSuffix', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class underName(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm('underName', 'http://schema.org/underName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class availabilityEnds(RdfProperty[schemaorg.Date | schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm('availabilityEnds', 'http://schema.org/availabilityEnds', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class paymentUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm('paymentUrl', 'http://schema.org/paymentUrl', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class annualPercentageRate(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm('annualPercentageRate', 'http://schema.org/annualPercentageRate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class actionOption(RdfProperty[schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm('actionOption', 'http://schema.org/actionOption', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class subOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm('subOrganization', 'http://schema.org/subOrganization', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class director(RdfProperty[schemaorg.Person]):
    term = RdfTerm('director', 'http://schema.org/director', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class currency(RdfProperty[schemaorg.Text]):
    term = RdfTerm('currency', 'http://schema.org/currency', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class postalCodeBegin(RdfProperty[schemaorg.Text]):
    term = RdfTerm('postalCodeBegin', 'http://schema.org/postalCodeBegin', ['1.1', '1.2-DRAFT'])

class isAccessoryOrSparePartFor(RdfProperty[schemaorg.Product]):
    term = RdfTerm('isAccessoryOrSparePartFor', 'http://schema.org/isAccessoryOrSparePartFor', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class openingHoursSpecification(RdfProperty[schemaorg.OpeningHoursSpecification]):
    term = RdfTerm('openingHoursSpecification', 'http://schema.org/openingHoursSpecification', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class events(RdfProperty[schemaorg.Event]):
    term = RdfTerm('events', 'http://schema.org/events', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class upvoteCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm('upvoteCount', 'http://schema.org/upvoteCount', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class costPerUnit(RdfProperty[schemaorg.QualitativeValue | schemaorg.Number | schemaorg.Text]):
    term = RdfTerm('costPerUnit', 'http://schema.org/costPerUnit', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class geoEquals(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm('geoEquals', 'http://schema.org/geoEquals', ['1.0', '1.1', '1.2-DRAFT'])

class performerIn(RdfProperty[schemaorg.Event]):
    term = RdfTerm('performerIn', 'http://schema.org/performerIn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class interactingDrug(RdfProperty[schemaorg.Drug]):
    term = RdfTerm('interactingDrug', 'http://schema.org/interactingDrug', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class expertConsiderations(RdfProperty[schemaorg.Text]):
    term = RdfTerm('expertConsiderations', 'http://schema.org/expertConsiderations', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class renegotiableLoan(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm('renegotiableLoan', 'http://schema.org/renegotiableLoan', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class domainIncludes(RdfProperty[schemaorg.Class]):
    term = RdfTerm('domainIncludes', 'http://schema.org/domainIncludes', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class partOfTVSeries(RdfProperty[schemaorg.TVSeries]):
    term = RdfTerm('partOfTVSeries', 'http://schema.org/partOfTVSeries', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class reservedTicket(RdfProperty[schemaorg.Ticket]):
    term = RdfTerm('reservedTicket', 'http://schema.org/reservedTicket', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class hasShippingService(RdfProperty[schemaorg.ShippingService]):
    term = RdfTerm('hasShippingService', 'http://schema.org/hasShippingService', [])

class genre(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm('genre', 'http://schema.org/genre', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class exceptDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm('exceptDate', 'http://schema.org/exceptDate', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class exerciseCourse(RdfProperty[schemaorg.Place]):
    term = RdfTerm('exerciseCourse', 'http://schema.org/exerciseCourse', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class termDuration(RdfProperty[schemaorg.Duration]):
    term = RdfTerm('termDuration', 'http://schema.org/termDuration', ['1.1', '1.2-DRAFT'])

class email(RdfProperty[schemaorg.Text]):
    term = RdfTerm('email', 'http://schema.org/email', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class workLocation(RdfProperty[schemaorg.Place | schemaorg.ContactPoint]):
    term = RdfTerm('workLocation', 'http://schema.org/workLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class contentSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm('contentSize', 'http://schema.org/contentSize', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class videoFormat(RdfProperty[schemaorg.Text]):
    term = RdfTerm('videoFormat', 'http://schema.org/videoFormat', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class associatedClaimReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm('associatedClaimReview', 'http://schema.org/associatedClaimReview', ['1.2-DRAFT'])

class trialDesign(RdfProperty[schemaorg.MedicalTrialDesign]):
    term = RdfTerm('trialDesign', 'http://schema.org/trialDesign', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class broadcastDisplayName(RdfProperty[schemaorg.Text]):
    term = RdfTerm('broadcastDisplayName', 'http://schema.org/broadcastDisplayName', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class gender(RdfProperty[schemaorg.Text | schemaorg.GenderType]):
    term = RdfTerm('gender', 'http://schema.org/gender', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class variableMeasured(RdfProperty[schemaorg.Property | schemaorg.StatisticalVariable | schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm('variableMeasured', 'http://schema.org/variableMeasured', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class percentile10(RdfProperty[schemaorg.Number]):
    term = RdfTerm('percentile10', 'http://schema.org/percentile10', ['1.0', '1.1', '1.2-DRAFT'])

class serviceOutput(RdfProperty[schemaorg.Thing]):
    term = RdfTerm('serviceOutput', 'http://schema.org/serviceOutput', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class toLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm('toLocation', 'http://schema.org/toLocation', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class episode(RdfProperty[schemaorg.Episode]):
    term = RdfTerm('episode', 'http://schema.org/episode', ['0.2', '1.0', '1.1', '1.2-DRAFT'])

class insertion(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm('insertion', 'http://schema.org/insertion', ['0.2', '1.0', '1.1', '1.2-DRAFT'])