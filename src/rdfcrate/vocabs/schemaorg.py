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
    term = RdfTerm('DataType', 'https://schema.org/DataType', [])

class Thing(RdfClass):
    term = RdfTerm('Thing', 'https://schema.org/Thing', [])

class Taxon(Thing):
    term = RdfTerm('Taxon', 'https://schema.org/Taxon', [])

class Product(Thing):
    term = RdfTerm('Product', 'https://schema.org/Product', [])

class Event(Thing):
    term = RdfTerm('Event', 'https://schema.org/Event', [])

class Place(Thing):
    term = RdfTerm('Place', 'https://schema.org/Place', [])

class CreativeWork(Thing):
    term = RdfTerm('CreativeWork', 'https://schema.org/CreativeWork', [])

class BioChemEntity(Thing):
    term = RdfTerm('BioChemEntity', 'https://schema.org/BioChemEntity', [])

class StupidType(Thing):
    term = RdfTerm('StupidType', 'https://schema.org/StupidType', [])

class Person(Thing):
    term = RdfTerm('Person', 'https://schema.org/Person', [])

class Intangible(Thing):
    term = RdfTerm('Intangible', 'https://schema.org/Intangible', [])

class Action(Thing):
    term = RdfTerm('Action', 'https://schema.org/Action', [])

class MedicalEntity(Thing):
    term = RdfTerm('MedicalEntity', 'https://schema.org/MedicalEntity', [])

class Organization(Thing):
    term = RdfTerm('Organization', 'https://schema.org/Organization', [])

class ProductGroup(Product):
    term = RdfTerm('ProductGroup', 'https://schema.org/ProductGroup', [])

class SomeProducts(Product):
    term = RdfTerm('SomeProducts', 'https://schema.org/SomeProducts', [])

class ProductModel(Product):
    term = RdfTerm('ProductModel', 'https://schema.org/ProductModel', [])

class Vehicle(Product):
    term = RdfTerm('Vehicle', 'https://schema.org/Vehicle', [])

class IndividualProduct(Product):
    term = RdfTerm('IndividualProduct', 'https://schema.org/IndividualProduct', [])

class ChildrensEvent(Event):
    term = RdfTerm('ChildrensEvent', 'https://schema.org/ChildrensEvent', [])

class SocialEvent(Event):
    term = RdfTerm('SocialEvent', 'https://schema.org/SocialEvent', [])

class DanceEvent(Event):
    term = RdfTerm('DanceEvent', 'https://schema.org/DanceEvent', [])

class Festival(Event):
    term = RdfTerm('Festival', 'https://schema.org/Festival', [])

class FoodEvent(Event):
    term = RdfTerm('FoodEvent', 'https://schema.org/FoodEvent', [])

class PublicationEvent(Event):
    term = RdfTerm('PublicationEvent', 'https://schema.org/PublicationEvent', [])

class DeliveryEvent(Event):
    term = RdfTerm('DeliveryEvent', 'https://schema.org/DeliveryEvent', [])

class Hackathon(Event):
    term = RdfTerm('Hackathon', 'https://schema.org/Hackathon', [])

class ScreeningEvent(Event):
    term = RdfTerm('ScreeningEvent', 'https://schema.org/ScreeningEvent', [])

class EducationEvent(Event):
    term = RdfTerm('EducationEvent', 'https://schema.org/EducationEvent', [])

class SaleEvent(Event):
    term = RdfTerm('SaleEvent', 'https://schema.org/SaleEvent', [])

class VisualArtsEvent(Event):
    term = RdfTerm('VisualArtsEvent', 'https://schema.org/VisualArtsEvent', [])

class CourseInstance(Event):
    term = RdfTerm('CourseInstance', 'https://schema.org/CourseInstance', [])

class ExhibitionEvent(Event):
    term = RdfTerm('ExhibitionEvent', 'https://schema.org/ExhibitionEvent', [])

class SportsEvent(Event):
    term = RdfTerm('SportsEvent', 'https://schema.org/SportsEvent', [])

class LiteraryEvent(Event):
    term = RdfTerm('LiteraryEvent', 'https://schema.org/LiteraryEvent', [])

class ComedyEvent(Event):
    term = RdfTerm('ComedyEvent', 'https://schema.org/ComedyEvent', [])

class TheaterEvent(Event):
    term = RdfTerm('TheaterEvent', 'https://schema.org/TheaterEvent', [])

class MusicEvent(Event):
    term = RdfTerm('MusicEvent', 'https://schema.org/MusicEvent', [])

class BusinessEvent(Event):
    term = RdfTerm('BusinessEvent', 'https://schema.org/BusinessEvent', [])

class UserInteraction(Event):
    term = RdfTerm('UserInteraction', 'https://schema.org/UserInteraction', [])

class Landform(Place):
    term = RdfTerm('Landform', 'https://schema.org/Landform', [])

class Residence(Place):
    term = RdfTerm('Residence', 'https://schema.org/Residence', [])

class CivicStructure(Place):
    term = RdfTerm('CivicStructure', 'https://schema.org/CivicStructure', [])

class AdministrativeArea(Place):
    term = RdfTerm('AdministrativeArea', 'https://schema.org/AdministrativeArea', [])

class LandmarksOrHistoricalBuildings(Place):
    term = RdfTerm('LandmarksOrHistoricalBuildings', 'https://schema.org/LandmarksOrHistoricalBuildings', [])

class Accommodation(Place):
    term = RdfTerm('Accommodation', 'https://schema.org/Accommodation', [])

class TouristAttraction(Place):
    term = RdfTerm('TouristAttraction', 'https://schema.org/TouristAttraction', [])

class TouristDestination(Place):
    term = RdfTerm('TouristDestination', 'https://schema.org/TouristDestination', [])

class Claim(CreativeWork):
    term = RdfTerm('Claim', 'https://schema.org/Claim', [])

class Certification(CreativeWork):
    term = RdfTerm('Certification', 'https://schema.org/Certification', [])

class Play(CreativeWork):
    term = RdfTerm('Play', 'https://schema.org/Play', [])

class Atlas(CreativeWork):
    term = RdfTerm('Atlas', 'https://schema.org/Atlas', [])

class Dataset(CreativeWork):
    term = RdfTerm('Dataset', 'https://schema.org/Dataset', [])

class Legislation(CreativeWork):
    term = RdfTerm('Legislation', 'https://schema.org/Legislation', [])

class LearningResource(CreativeWork):
    term = RdfTerm('LearningResource', 'https://schema.org/LearningResource', [])

class MathSolver(CreativeWork):
    term = RdfTerm('MathSolver', 'https://schema.org/MathSolver', [])

class Collection(CreativeWork):
    term = RdfTerm('Collection', 'https://schema.org/Collection', [])

class Movie(CreativeWork):
    term = RdfTerm('Movie', 'https://schema.org/Movie', [])

class ShortStory(CreativeWork):
    term = RdfTerm('ShortStory', 'https://schema.org/ShortStory', [])

class Article(CreativeWork):
    term = RdfTerm('Article', 'https://schema.org/Article', [])

class Clip(CreativeWork):
    term = RdfTerm('Clip', 'https://schema.org/Clip', [])

class ComicStory(CreativeWork):
    term = RdfTerm('ComicStory', 'https://schema.org/ComicStory', [])

class Photograph(CreativeWork):
    term = RdfTerm('Photograph', 'https://schema.org/Photograph', [])

class MediaReviewItem(CreativeWork):
    term = RdfTerm('MediaReviewItem', 'https://schema.org/MediaReviewItem', [])

class Statement(CreativeWork):
    term = RdfTerm('Statement', 'https://schema.org/Statement', [])

class Chapter(CreativeWork):
    term = RdfTerm('Chapter', 'https://schema.org/Chapter', [])

class Game(CreativeWork):
    term = RdfTerm('Game', 'https://schema.org/Game', [])

class WebPageElement(CreativeWork):
    term = RdfTerm('WebPageElement', 'https://schema.org/WebPageElement', [])

class WebContent(CreativeWork):
    term = RdfTerm('WebContent', 'https://schema.org/WebContent', [])

class PublicationIssue(CreativeWork):
    term = RdfTerm('PublicationIssue', 'https://schema.org/PublicationIssue', [])

class DefinedTermSet(CreativeWork):
    term = RdfTerm('DefinedTermSet', 'https://schema.org/DefinedTermSet', [])

class CreativeWorkSeason(CreativeWork):
    term = RdfTerm('CreativeWorkSeason', 'https://schema.org/CreativeWorkSeason', [])

class Code(CreativeWork):
    term = RdfTerm('Code', 'https://schema.org/Code', [])

class Sculpture(CreativeWork):
    term = RdfTerm('Sculpture', 'https://schema.org/Sculpture', [])

class SoftwareSourceCode(CreativeWork):
    term = RdfTerm('SoftwareSourceCode', 'https://schema.org/SoftwareSourceCode', [])

class HowTo(CreativeWork):
    term = RdfTerm('HowTo', 'https://schema.org/HowTo', [])

class HyperTocEntry(CreativeWork):
    term = RdfTerm('HyperTocEntry', 'https://schema.org/HyperTocEntry', [])

class Message(CreativeWork):
    term = RdfTerm('Message', 'https://schema.org/Message', [])

class MenuSection(CreativeWork):
    term = RdfTerm('MenuSection', 'https://schema.org/MenuSection', [])

class Blog(CreativeWork):
    term = RdfTerm('Blog', 'https://schema.org/Blog', [])

class Quotation(CreativeWork):
    term = RdfTerm('Quotation', 'https://schema.org/Quotation', [])

class Episode(CreativeWork):
    term = RdfTerm('Episode', 'https://schema.org/Episode', [])

class Map(CreativeWork):
    term = RdfTerm('Map', 'https://schema.org/Map', [])

class Thesis(CreativeWork):
    term = RdfTerm('Thesis', 'https://schema.org/Thesis', [])

class VisualArtwork(CreativeWork):
    term = RdfTerm('VisualArtwork', 'https://schema.org/VisualArtwork', [])

class MusicPlaylist(CreativeWork):
    term = RdfTerm('MusicPlaylist', 'https://schema.org/MusicPlaylist', [])

class MediaObject(CreativeWork):
    term = RdfTerm('MediaObject', 'https://schema.org/MediaObject', [])

class Season(CreativeWork):
    term = RdfTerm('Season', 'https://schema.org/Season', [])

class SheetMusic(CreativeWork):
    term = RdfTerm('SheetMusic', 'https://schema.org/SheetMusic', [])

class Menu(CreativeWork):
    term = RdfTerm('Menu', 'https://schema.org/Menu', [])

class Drawing(CreativeWork):
    term = RdfTerm('Drawing', 'https://schema.org/Drawing', [])

class Comment(CreativeWork):
    term = RdfTerm('Comment', 'https://schema.org/Comment', [])

class DigitalDocument(CreativeWork):
    term = RdfTerm('DigitalDocument', 'https://schema.org/DigitalDocument', [])

class ArchiveComponent(CreativeWork):
    term = RdfTerm('ArchiveComponent', 'https://schema.org/ArchiveComponent', [])

class Review(CreativeWork):
    term = RdfTerm('Review', 'https://schema.org/Review', [])

class WebSite(CreativeWork):
    term = RdfTerm('WebSite', 'https://schema.org/WebSite', [])

class WebPage(CreativeWork):
    term = RdfTerm('WebPage', 'https://schema.org/WebPage', [])

class Poster(CreativeWork):
    term = RdfTerm('Poster', 'https://schema.org/Poster', [])

class Book(CreativeWork):
    term = RdfTerm('Book', 'https://schema.org/Book', [])

class SoftwareApplication(CreativeWork):
    term = RdfTerm('SoftwareApplication', 'https://schema.org/SoftwareApplication', [])

class Guide(CreativeWork):
    term = RdfTerm('Guide', 'https://schema.org/Guide', [])

class SpecialAnnouncement(CreativeWork):
    term = RdfTerm('SpecialAnnouncement', 'https://schema.org/SpecialAnnouncement', [])

class Painting(CreativeWork):
    term = RdfTerm('Painting', 'https://schema.org/Painting', [])

class Manuscript(CreativeWork):
    term = RdfTerm('Manuscript', 'https://schema.org/Manuscript', [])

class PublicationVolume(CreativeWork):
    term = RdfTerm('PublicationVolume', 'https://schema.org/PublicationVolume', [])

class MusicComposition(CreativeWork):
    term = RdfTerm('MusicComposition', 'https://schema.org/MusicComposition', [])

class DataCatalog(CreativeWork):
    term = RdfTerm('DataCatalog', 'https://schema.org/DataCatalog', [])

class MusicRecording(CreativeWork):
    term = RdfTerm('MusicRecording', 'https://schema.org/MusicRecording', [])

class Conversation(CreativeWork):
    term = RdfTerm('Conversation', 'https://schema.org/Conversation', [])

class HyperToc(CreativeWork):
    term = RdfTerm('HyperToc', 'https://schema.org/HyperToc', [])

class EducationalOccupationalCredential(CreativeWork):
    term = RdfTerm('EducationalOccupationalCredential', 'https://schema.org/EducationalOccupationalCredential', [])

class MolecularEntity(BioChemEntity):
    term = RdfTerm('MolecularEntity', 'https://schema.org/MolecularEntity', [])

class Protein(BioChemEntity):
    term = RdfTerm('Protein', 'https://schema.org/Protein', [])

class ChemicalSubstance(BioChemEntity):
    term = RdfTerm('ChemicalSubstance', 'https://schema.org/ChemicalSubstance', [])

class Gene(BioChemEntity):
    term = RdfTerm('Gene', 'https://schema.org/Gene', [])

class PropertyValueSpecification(Intangible):
    term = RdfTerm('PropertyValueSpecification', 'https://schema.org/PropertyValueSpecification', [])

class HealthPlanNetwork(Intangible):
    term = RdfTerm('HealthPlanNetwork', 'https://schema.org/HealthPlanNetwork', [])

class Invoice(Intangible):
    term = RdfTerm('Invoice', 'https://schema.org/Invoice', [])

class DataFeedItem(Intangible):
    term = RdfTerm('DataFeedItem', 'https://schema.org/DataFeedItem', [])

class StatisticalPopulation(Intangible):
    term = RdfTerm('StatisticalPopulation', 'https://schema.org/StatisticalPopulation', [])

class MerchantReturnPolicy(Intangible):
    term = RdfTerm('MerchantReturnPolicy', 'https://schema.org/MerchantReturnPolicy', [])

class ComputerLanguage(Intangible):
    term = RdfTerm('ComputerLanguage', 'https://schema.org/ComputerLanguage', [])

class StructuredValue(Intangible):
    term = RdfTerm('StructuredValue', 'https://schema.org/StructuredValue', [])

class MemberProgramTier(Intangible):
    term = RdfTerm('MemberProgramTier', 'https://schema.org/MemberProgramTier', [])

class GameServer(Intangible):
    term = RdfTerm('GameServer', 'https://schema.org/GameServer', [])

class SpeakableSpecification(Intangible):
    term = RdfTerm('SpeakableSpecification', 'https://schema.org/SpeakableSpecification', [])

class Series(Intangible):
    term = RdfTerm('Series', 'https://schema.org/Series', [])

class Class(Intangible):
    term = RdfTerm('Class', 'https://schema.org/Class', [])

class MediaSubscription(Intangible):
    term = RdfTerm('MediaSubscription', 'https://schema.org/MediaSubscription', [])

class VirtualLocation(Intangible):
    term = RdfTerm('VirtualLocation', 'https://schema.org/VirtualLocation', [])

class ServiceChannel(Intangible):
    term = RdfTerm('ServiceChannel', 'https://schema.org/ServiceChannel', [])

class BroadcastFrequencySpecification(Intangible):
    term = RdfTerm('BroadcastFrequencySpecification', 'https://schema.org/BroadcastFrequencySpecification', [])

class Demand(Intangible):
    term = RdfTerm('Demand', 'https://schema.org/Demand', [])

class BroadcastChannel(Intangible):
    term = RdfTerm('BroadcastChannel', 'https://schema.org/BroadcastChannel', [])

class ProgramMembership(Intangible):
    term = RdfTerm('ProgramMembership', 'https://schema.org/ProgramMembership', [])

class Order(Intangible):
    term = RdfTerm('Order', 'https://schema.org/Order', [])

class Ticket(Intangible):
    term = RdfTerm('Ticket', 'https://schema.org/Ticket', [])

class Grant(Intangible):
    term = RdfTerm('Grant', 'https://schema.org/Grant', [])

class OrderItem(Intangible):
    term = RdfTerm('OrderItem', 'https://schema.org/OrderItem', [])

class Enumeration(Intangible):
    term = RdfTerm('Enumeration', 'https://schema.org/Enumeration', [])

class FinancialIncentive(Intangible):
    term = RdfTerm('FinancialIncentive', 'https://schema.org/FinancialIncentive', [])

class ItemList(Intangible):
    term = RdfTerm('ItemList', 'https://schema.org/ItemList', [])

class EntryPoint(Intangible):
    term = RdfTerm('EntryPoint', 'https://schema.org/EntryPoint', [])

class ConstraintNode(Intangible):
    term = RdfTerm('ConstraintNode', 'https://schema.org/ConstraintNode', [])

class Occupation(Intangible):
    term = RdfTerm('Occupation', 'https://schema.org/Occupation', [])

class Role(Intangible):
    term = RdfTerm('Role', 'https://schema.org/Role', [])

class Audience(Intangible):
    term = RdfTerm('Audience', 'https://schema.org/Audience', [])

class PaymentMethod(Intangible):
    term = RdfTerm('PaymentMethod', 'https://schema.org/PaymentMethod', [])

class Permit(Intangible):
    term = RdfTerm('Permit', 'https://schema.org/Permit', [])

class GeospatialGeometry(Intangible):
    term = RdfTerm('GeospatialGeometry', 'https://schema.org/GeospatialGeometry', [])

class BedDetails(Intangible):
    term = RdfTerm('BedDetails', 'https://schema.org/BedDetails', [])

class AlignmentObject(Intangible):
    term = RdfTerm('AlignmentObject', 'https://schema.org/AlignmentObject', [])

class MenuItem(Intangible):
    term = RdfTerm('MenuItem', 'https://schema.org/MenuItem', [])

class HealthPlanCostSharingSpecification(Intangible):
    term = RdfTerm('HealthPlanCostSharingSpecification', 'https://schema.org/HealthPlanCostSharingSpecification', [])

class MerchantReturnPolicySeasonalOverride(Intangible):
    term = RdfTerm('MerchantReturnPolicySeasonalOverride', 'https://schema.org/MerchantReturnPolicySeasonalOverride', [])

class MemberProgram(Intangible):
    term = RdfTerm('MemberProgram', 'https://schema.org/MemberProgram', [])

class Language(Intangible):
    term = RdfTerm('Language', 'https://schema.org/Language', [])

class FloorPlan(Intangible):
    term = RdfTerm('FloorPlan', 'https://schema.org/FloorPlan', [])

class Reservation(Intangible):
    term = RdfTerm('Reservation', 'https://schema.org/Reservation', [])

class HealthInsurancePlan(Intangible):
    term = RdfTerm('HealthInsurancePlan', 'https://schema.org/HealthInsurancePlan', [])

class DigitalDocumentPermission(Intangible):
    term = RdfTerm('DigitalDocumentPermission', 'https://schema.org/DigitalDocumentPermission', [])

class DefinedTerm(Intangible):
    term = RdfTerm('DefinedTerm', 'https://schema.org/DefinedTerm', [])

class ProductReturnPolicy(Intangible):
    term = RdfTerm('ProductReturnPolicy', 'https://schema.org/ProductReturnPolicy', [])

class Schedule(Intangible):
    term = RdfTerm('Schedule', 'https://schema.org/Schedule', [])

class EnergyConsumptionDetails(Intangible):
    term = RdfTerm('EnergyConsumptionDetails', 'https://schema.org/EnergyConsumptionDetails', [])

class Property(Intangible):
    term = RdfTerm('Property', 'https://schema.org/Property', [])

class Seat(Intangible):
    term = RdfTerm('Seat', 'https://schema.org/Seat', [])

class ActionAccessSpecification(Intangible):
    term = RdfTerm('ActionAccessSpecification', 'https://schema.org/ActionAccessSpecification', [])

class OccupationalExperienceRequirements(Intangible):
    term = RdfTerm('OccupationalExperienceRequirements', 'https://schema.org/OccupationalExperienceRequirements', [])

class HealthPlanFormulary(Intangible):
    term = RdfTerm('HealthPlanFormulary', 'https://schema.org/HealthPlanFormulary', [])

class JobPosting(Intangible):
    term = RdfTerm('JobPosting', 'https://schema.org/JobPosting', [])

class Quantity(Intangible):
    term = RdfTerm('Quantity', 'https://schema.org/Quantity', [])

class EducationalOccupationalProgram(Intangible):
    term = RdfTerm('EducationalOccupationalProgram', 'https://schema.org/EducationalOccupationalProgram', [])

class Trip(Intangible):
    term = RdfTerm('Trip', 'https://schema.org/Trip', [])

class Service(Intangible):
    term = RdfTerm('Service', 'https://schema.org/Service', [])

class ListItem(Intangible):
    term = RdfTerm('ListItem', 'https://schema.org/ListItem', [])

class Rating(Intangible):
    term = RdfTerm('Rating', 'https://schema.org/Rating', [])

class Offer(Intangible):
    term = RdfTerm('Offer', 'https://schema.org/Offer', [])

class Brand(Intangible):
    term = RdfTerm('Brand', 'https://schema.org/Brand', [])

class ParcelDelivery(Intangible):
    term = RdfTerm('ParcelDelivery', 'https://schema.org/ParcelDelivery', [])

class AssessAction(Action):
    term = RdfTerm('AssessAction', 'https://schema.org/AssessAction', [])

class ControlAction(Action):
    term = RdfTerm('ControlAction', 'https://schema.org/ControlAction', [])

class MoveAction(Action):
    term = RdfTerm('MoveAction', 'https://schema.org/MoveAction', [])

class AchieveAction(Action):
    term = RdfTerm('AchieveAction', 'https://schema.org/AchieveAction', [])

class TransferAction(Action):
    term = RdfTerm('TransferAction', 'https://schema.org/TransferAction', [])

class TradeAction(Action):
    term = RdfTerm('TradeAction', 'https://schema.org/TradeAction', [])

class CreateAction(Action):
    term = RdfTerm('CreateAction', 'https://schema.org/CreateAction', [])

class UpdateAction(Action):
    term = RdfTerm('UpdateAction', 'https://schema.org/UpdateAction', [])

class SearchAction(Action):
    term = RdfTerm('SearchAction', 'https://schema.org/SearchAction', [])

class SolveMathAction(Action):
    term = RdfTerm('SolveMathAction', 'https://schema.org/SolveMathAction', [])

class ConsumeAction(Action):
    term = RdfTerm('ConsumeAction', 'https://schema.org/ConsumeAction', [])

class InteractAction(Action):
    term = RdfTerm('InteractAction', 'https://schema.org/InteractAction', [])

class SeekToAction(Action):
    term = RdfTerm('SeekToAction', 'https://schema.org/SeekToAction', [])

class PlayAction(Action):
    term = RdfTerm('PlayAction', 'https://schema.org/PlayAction', [])

class OrganizeAction(Action):
    term = RdfTerm('OrganizeAction', 'https://schema.org/OrganizeAction', [])

class FindAction(Action):
    term = RdfTerm('FindAction', 'https://schema.org/FindAction', [])

class MedicalCause(MedicalEntity):
    term = RdfTerm('MedicalCause', 'https://schema.org/MedicalCause', [])

class MedicalRiskFactor(MedicalEntity):
    term = RdfTerm('MedicalRiskFactor', 'https://schema.org/MedicalRiskFactor', [])

class MedicalTest(MedicalEntity):
    term = RdfTerm('MedicalTest', 'https://schema.org/MedicalTest', [])

class MedicalStudy(MedicalEntity):
    term = RdfTerm('MedicalStudy', 'https://schema.org/MedicalStudy', [])

class MedicalProcedure(MedicalEntity):
    term = RdfTerm('MedicalProcedure', 'https://schema.org/MedicalProcedure', [])

class DrugCost(MedicalEntity):
    term = RdfTerm('DrugCost', 'https://schema.org/DrugCost', [])

class AnatomicalSystem(MedicalEntity):
    term = RdfTerm('AnatomicalSystem', 'https://schema.org/AnatomicalSystem', [])

class MedicalRiskEstimator(MedicalEntity):
    term = RdfTerm('MedicalRiskEstimator', 'https://schema.org/MedicalRiskEstimator', [])

class MedicalContraindication(MedicalEntity):
    term = RdfTerm('MedicalContraindication', 'https://schema.org/MedicalContraindication', [])

class MedicalCondition(MedicalEntity):
    term = RdfTerm('MedicalCondition', 'https://schema.org/MedicalCondition', [])

class MedicalDevice(MedicalEntity):
    term = RdfTerm('MedicalDevice', 'https://schema.org/MedicalDevice', [])

class SuperficialAnatomy(MedicalEntity):
    term = RdfTerm('SuperficialAnatomy', 'https://schema.org/SuperficialAnatomy', [])

class DrugClass(MedicalEntity):
    term = RdfTerm('DrugClass', 'https://schema.org/DrugClass', [])

class AnatomicalStructure(MedicalEntity):
    term = RdfTerm('AnatomicalStructure', 'https://schema.org/AnatomicalStructure', [])

class MedicalGuideline(MedicalEntity):
    term = RdfTerm('MedicalGuideline', 'https://schema.org/MedicalGuideline', [])

class Substance(MedicalEntity):
    term = RdfTerm('Substance', 'https://schema.org/Substance', [])

class LifestyleModification(MedicalEntity):
    term = RdfTerm('LifestyleModification', 'https://schema.org/LifestyleModification', [])

class MedicalIndication(MedicalEntity):
    term = RdfTerm('MedicalIndication', 'https://schema.org/MedicalIndication', [])

class MedicalIntangible(MedicalEntity):
    term = RdfTerm('MedicalIntangible', 'https://schema.org/MedicalIntangible', [])

class MedicalOrganization(Organization):
    term = RdfTerm('MedicalOrganization', 'https://schema.org/MedicalOrganization', [])

class Project(Organization):
    term = RdfTerm('Project', 'https://schema.org/Project', [])

class FundingScheme(Organization):
    term = RdfTerm('FundingScheme', 'https://schema.org/FundingScheme', [])

class NGO(Organization):
    term = RdfTerm('NGO', 'https://schema.org/NGO', [])

class LocalBusiness(Place, Organization):
    term = RdfTerm('LocalBusiness', 'https://schema.org/LocalBusiness', [])

class Airline(Organization):
    term = RdfTerm('Airline', 'https://schema.org/Airline', [])

class OnlineBusiness(Organization):
    term = RdfTerm('OnlineBusiness', 'https://schema.org/OnlineBusiness', [])

class PoliticalParty(Organization):
    term = RdfTerm('PoliticalParty', 'https://schema.org/PoliticalParty', [])

class GovernmentOrganization(Organization):
    term = RdfTerm('GovernmentOrganization', 'https://schema.org/GovernmentOrganization', [])

class PerformingGroup(Organization):
    term = RdfTerm('PerformingGroup', 'https://schema.org/PerformingGroup', [])

class LibrarySystem(Organization):
    term = RdfTerm('LibrarySystem', 'https://schema.org/LibrarySystem', [])

class SearchRescueOrganization(Organization):
    term = RdfTerm('SearchRescueOrganization', 'https://schema.org/SearchRescueOrganization', [])

class ResearchOrganization(Organization):
    term = RdfTerm('ResearchOrganization', 'https://schema.org/ResearchOrganization', [])

class NewsMediaOrganization(Organization):
    term = RdfTerm('NewsMediaOrganization', 'https://schema.org/NewsMediaOrganization', [])

class Corporation(Organization):
    term = RdfTerm('Corporation', 'https://schema.org/Corporation', [])

class WorkersUnion(Organization):
    term = RdfTerm('WorkersUnion', 'https://schema.org/WorkersUnion', [])

class SportsOrganization(Organization):
    term = RdfTerm('SportsOrganization', 'https://schema.org/SportsOrganization', [])

class Consortium(Organization):
    term = RdfTerm('Consortium', 'https://schema.org/Consortium', [])

class BusOrCoach(Vehicle):
    term = RdfTerm('BusOrCoach', 'https://schema.org/BusOrCoach', [])

class Car(Vehicle):
    term = RdfTerm('Car', 'https://schema.org/Car', [])

class MotorizedBicycle(Vehicle):
    term = RdfTerm('MotorizedBicycle', 'https://schema.org/MotorizedBicycle', [])

class Motorcycle(Vehicle):
    term = RdfTerm('Motorcycle', 'https://schema.org/Motorcycle', [])

class BroadcastEvent(PublicationEvent):
    term = RdfTerm('BroadcastEvent', 'https://schema.org/BroadcastEvent', [])

class OnDemandEvent(PublicationEvent):
    term = RdfTerm('OnDemandEvent', 'https://schema.org/OnDemandEvent', [])

class UserPlusOnes(UserInteraction):
    term = RdfTerm('UserPlusOnes', 'https://schema.org/UserPlusOnes', [])

class UserTweets(UserInteraction):
    term = RdfTerm('UserTweets', 'https://schema.org/UserTweets', [])

class UserLikes(UserInteraction):
    term = RdfTerm('UserLikes', 'https://schema.org/UserLikes', [])

class UserCheckins(UserInteraction):
    term = RdfTerm('UserCheckins', 'https://schema.org/UserCheckins', [])

class UserComments(UserInteraction):
    term = RdfTerm('UserComments', 'https://schema.org/UserComments', [])

class UserPlays(UserInteraction):
    term = RdfTerm('UserPlays', 'https://schema.org/UserPlays', [])

class UserPageVisits(UserInteraction):
    term = RdfTerm('UserPageVisits', 'https://schema.org/UserPageVisits', [])

class UserBlocks(UserInteraction):
    term = RdfTerm('UserBlocks', 'https://schema.org/UserBlocks', [])

class UserDownloads(UserInteraction):
    term = RdfTerm('UserDownloads', 'https://schema.org/UserDownloads', [])

class Continent(Landform):
    term = RdfTerm('Continent', 'https://schema.org/Continent', [])

class Mountain(Landform):
    term = RdfTerm('Mountain', 'https://schema.org/Mountain', [])

class BodyOfWater(Landform):
    term = RdfTerm('BodyOfWater', 'https://schema.org/BodyOfWater', [])

class Volcano(Landform):
    term = RdfTerm('Volcano', 'https://schema.org/Volcano', [])

class GatedResidenceCommunity(Residence):
    term = RdfTerm('GatedResidenceCommunity', 'https://schema.org/GatedResidenceCommunity', [])

class ApartmentComplex(Residence):
    term = RdfTerm('ApartmentComplex', 'https://schema.org/ApartmentComplex', [])

class SubwayStation(CivicStructure):
    term = RdfTerm('SubwayStation', 'https://schema.org/SubwayStation', [])

class Bridge(CivicStructure):
    term = RdfTerm('Bridge', 'https://schema.org/Bridge', [])

class MusicVenue(CivicStructure):
    term = RdfTerm('MusicVenue', 'https://schema.org/MusicVenue', [])

class Airport(CivicStructure):
    term = RdfTerm('Airport', 'https://schema.org/Airport', [])

class Beach(CivicStructure):
    term = RdfTerm('Beach', 'https://schema.org/Beach', [])

class RVPark(CivicStructure):
    term = RdfTerm('RVPark', 'https://schema.org/RVPark', [])

class Museum(CivicStructure):
    term = RdfTerm('Museum', 'https://schema.org/Museum', [])

class BoatTerminal(CivicStructure):
    term = RdfTerm('BoatTerminal', 'https://schema.org/BoatTerminal', [])

class ParkingFacility(CivicStructure):
    term = RdfTerm('ParkingFacility', 'https://schema.org/ParkingFacility', [])

class TrainStation(CivicStructure):
    term = RdfTerm('TrainStation', 'https://schema.org/TrainStation', [])

class PublicToilet(CivicStructure):
    term = RdfTerm('PublicToilet', 'https://schema.org/PublicToilet', [])

class Zoo(CivicStructure):
    term = RdfTerm('Zoo', 'https://schema.org/Zoo', [])

class Playground(CivicStructure):
    term = RdfTerm('Playground', 'https://schema.org/Playground', [])

class GovernmentBuilding(CivicStructure):
    term = RdfTerm('GovernmentBuilding', 'https://schema.org/GovernmentBuilding', [])

class PerformingArtsTheater(CivicStructure):
    term = RdfTerm('PerformingArtsTheater', 'https://schema.org/PerformingArtsTheater', [])

class PlaceOfWorship(CivicStructure):
    term = RdfTerm('PlaceOfWorship', 'https://schema.org/PlaceOfWorship', [])

class Crematorium(CivicStructure):
    term = RdfTerm('Crematorium', 'https://schema.org/Crematorium', [])

class EducationalOrganization(CivicStructure, Organization):
    term = RdfTerm('EducationalOrganization', 'https://schema.org/EducationalOrganization', [])

class Aquarium(CivicStructure):
    term = RdfTerm('Aquarium', 'https://schema.org/Aquarium', [])

class Park(CivicStructure):
    term = RdfTerm('Park', 'https://schema.org/Park', [])

class Cemetery(CivicStructure):
    term = RdfTerm('Cemetery', 'https://schema.org/Cemetery', [])

class TaxiStand(CivicStructure):
    term = RdfTerm('TaxiStand', 'https://schema.org/TaxiStand', [])

class EventVenue(CivicStructure):
    term = RdfTerm('EventVenue', 'https://schema.org/EventVenue', [])

class BusStop(CivicStructure):
    term = RdfTerm('BusStop', 'https://schema.org/BusStop', [])

class BusStation(CivicStructure):
    term = RdfTerm('BusStation', 'https://schema.org/BusStation', [])

class Country(AdministrativeArea):
    term = RdfTerm('Country', 'https://schema.org/Country', [])

class State(AdministrativeArea):
    term = RdfTerm('State', 'https://schema.org/State', [])

class SchoolDistrict(AdministrativeArea):
    term = RdfTerm('SchoolDistrict', 'https://schema.org/SchoolDistrict', [])

class City(AdministrativeArea):
    term = RdfTerm('City', 'https://schema.org/City', [])

class Apartment(Accommodation):
    term = RdfTerm('Apartment', 'https://schema.org/Apartment', [])

class CampingPitch(Accommodation):
    term = RdfTerm('CampingPitch', 'https://schema.org/CampingPitch', [])

class Suite(Accommodation):
    term = RdfTerm('Suite', 'https://schema.org/Suite', [])

class Room(Accommodation):
    term = RdfTerm('Room', 'https://schema.org/Room', [])

class House(Accommodation):
    term = RdfTerm('House', 'https://schema.org/House', [])

class DataFeed(Dataset):
    term = RdfTerm('DataFeed', 'https://schema.org/DataFeed', [])

class Syllabus(LearningResource):
    term = RdfTerm('Syllabus', 'https://schema.org/Syllabus', [])

class Course(LearningResource, CreativeWork):
    term = RdfTerm('Course', 'https://schema.org/Course', [])

class Quiz(LearningResource):
    term = RdfTerm('Quiz', 'https://schema.org/Quiz', [])

class ProductCollection(Collection, Product):
    term = RdfTerm('ProductCollection', 'https://schema.org/ProductCollection', [])

class Report(Article):
    term = RdfTerm('Report', 'https://schema.org/Report', [])

class SocialMediaPosting(Article):
    term = RdfTerm('SocialMediaPosting', 'https://schema.org/SocialMediaPosting', [])

class NewsArticle(Article):
    term = RdfTerm('NewsArticle', 'https://schema.org/NewsArticle', [])

class SatiricalArticle(Article):
    term = RdfTerm('SatiricalArticle', 'https://schema.org/SatiricalArticle', [])

class AdvertiserContentArticle(Article):
    term = RdfTerm('AdvertiserContentArticle', 'https://schema.org/AdvertiserContentArticle', [])

class ScholarlyArticle(Article):
    term = RdfTerm('ScholarlyArticle', 'https://schema.org/ScholarlyArticle', [])

class TechArticle(Article):
    term = RdfTerm('TechArticle', 'https://schema.org/TechArticle', [])

class TVClip(Clip):
    term = RdfTerm('TVClip', 'https://schema.org/TVClip', [])

class VideoGameClip(Clip):
    term = RdfTerm('VideoGameClip', 'https://schema.org/VideoGameClip', [])

class RadioClip(Clip):
    term = RdfTerm('RadioClip', 'https://schema.org/RadioClip', [])

class MovieClip(Clip):
    term = RdfTerm('MovieClip', 'https://schema.org/MovieClip', [])

class WPAdBlock(WebPageElement):
    term = RdfTerm('WPAdBlock', 'https://schema.org/WPAdBlock', [])

class Table(WebPageElement):
    term = RdfTerm('Table', 'https://schema.org/Table', [])

class WPSideBar(WebPageElement):
    term = RdfTerm('WPSideBar', 'https://schema.org/WPSideBar', [])

class WPHeader(WebPageElement):
    term = RdfTerm('WPHeader', 'https://schema.org/WPHeader', [])

class WPFooter(WebPageElement):
    term = RdfTerm('WPFooter', 'https://schema.org/WPFooter', [])

class SiteNavigationElement(WebPageElement):
    term = RdfTerm('SiteNavigationElement', 'https://schema.org/SiteNavigationElement', [])

class HealthTopicContent(WebContent):
    term = RdfTerm('HealthTopicContent', 'https://schema.org/HealthTopicContent', [])

class ComicIssue(PublicationIssue):
    term = RdfTerm('ComicIssue', 'https://schema.org/ComicIssue', [])

class CategoryCodeSet(DefinedTermSet):
    term = RdfTerm('CategoryCodeSet', 'https://schema.org/CategoryCodeSet', [])

class PodcastSeason(CreativeWorkSeason):
    term = RdfTerm('PodcastSeason', 'https://schema.org/PodcastSeason', [])

class TVSeason(CreativeWork, CreativeWorkSeason):
    term = RdfTerm('TVSeason', 'https://schema.org/TVSeason', [])

class RadioSeason(CreativeWorkSeason):
    term = RdfTerm('RadioSeason', 'https://schema.org/RadioSeason', [])

class Recipe(HowTo):
    term = RdfTerm('Recipe', 'https://schema.org/Recipe', [])

class EmailMessage(Message):
    term = RdfTerm('EmailMessage', 'https://schema.org/EmailMessage', [])

class TVEpisode(Episode):
    term = RdfTerm('TVEpisode', 'https://schema.org/TVEpisode', [])

class PodcastEpisode(Episode):
    term = RdfTerm('PodcastEpisode', 'https://schema.org/PodcastEpisode', [])

class RadioEpisode(Episode):
    term = RdfTerm('RadioEpisode', 'https://schema.org/RadioEpisode', [])

class CoverArt(VisualArtwork):
    term = RdfTerm('CoverArt', 'https://schema.org/CoverArt', [])

class MusicAlbum(MusicPlaylist):
    term = RdfTerm('MusicAlbum', 'https://schema.org/MusicAlbum', [])

class MusicRelease(MusicPlaylist):
    term = RdfTerm('MusicRelease', 'https://schema.org/MusicRelease', [])

class TextObject(MediaObject):
    term = RdfTerm('TextObject', 'https://schema.org/TextObject', [])

class AudioObject(MediaObject):
    term = RdfTerm('AudioObject', 'https://schema.org/AudioObject', [])

class LegislationObject(Legislation, MediaObject):
    term = RdfTerm('LegislationObject', 'https://schema.org/LegislationObject', [])

class _3DModel(MediaObject):
    term = RdfTerm('3DModel', 'https://schema.org/3DModel', [])

class AmpStory(MediaObject, CreativeWork):
    term = RdfTerm('AmpStory', 'https://schema.org/AmpStory', [])

class MusicVideoObject(MediaObject):
    term = RdfTerm('MusicVideoObject', 'https://schema.org/MusicVideoObject', [])

class DataDownload(MediaObject):
    term = RdfTerm('DataDownload', 'https://schema.org/DataDownload', [])

class VideoObject(MediaObject):
    term = RdfTerm('VideoObject', 'https://schema.org/VideoObject', [])

class ImageObject(MediaObject):
    term = RdfTerm('ImageObject', 'https://schema.org/ImageObject', [])

class Answer(Comment):
    term = RdfTerm('Answer', 'https://schema.org/Answer', [])

class Question(Comment):
    term = RdfTerm('Question', 'https://schema.org/Question', [])

class CorrectionComment(Comment):
    term = RdfTerm('CorrectionComment', 'https://schema.org/CorrectionComment', [])

class TextDigitalDocument(DigitalDocument):
    term = RdfTerm('TextDigitalDocument', 'https://schema.org/TextDigitalDocument', [])

class SpreadsheetDigitalDocument(DigitalDocument):
    term = RdfTerm('SpreadsheetDigitalDocument', 'https://schema.org/SpreadsheetDigitalDocument', [])

class NoteDigitalDocument(DigitalDocument):
    term = RdfTerm('NoteDigitalDocument', 'https://schema.org/NoteDigitalDocument', [])

class PresentationDigitalDocument(DigitalDocument):
    term = RdfTerm('PresentationDigitalDocument', 'https://schema.org/PresentationDigitalDocument', [])

class Recommendation(Review):
    term = RdfTerm('Recommendation', 'https://schema.org/Recommendation', [])

class UserReview(Review):
    term = RdfTerm('UserReview', 'https://schema.org/UserReview', [])

class EmployerReview(Review):
    term = RdfTerm('EmployerReview', 'https://schema.org/EmployerReview', [])

class MediaReview(Review):
    term = RdfTerm('MediaReview', 'https://schema.org/MediaReview', [])

class CriticReview(Review):
    term = RdfTerm('CriticReview', 'https://schema.org/CriticReview', [])

class ClaimReview(Review):
    term = RdfTerm('ClaimReview', 'https://schema.org/ClaimReview', [])

class CheckoutPage(WebPage):
    term = RdfTerm('CheckoutPage', 'https://schema.org/CheckoutPage', [])

class FAQPage(WebPage):
    term = RdfTerm('FAQPage', 'https://schema.org/FAQPage', [])

class ProfilePage(WebPage):
    term = RdfTerm('ProfilePage', 'https://schema.org/ProfilePage', [])

class QAPage(WebPage):
    term = RdfTerm('QAPage', 'https://schema.org/QAPage', [])

class SearchResultsPage(WebPage):
    term = RdfTerm('SearchResultsPage', 'https://schema.org/SearchResultsPage', [])

class RealEstateListing(WebPage):
    term = RdfTerm('RealEstateListing', 'https://schema.org/RealEstateListing', [])

class ItemPage(WebPage):
    term = RdfTerm('ItemPage', 'https://schema.org/ItemPage', [])

class ContactPage(WebPage):
    term = RdfTerm('ContactPage', 'https://schema.org/ContactPage', [])

class MedicalWebPage(WebPage):
    term = RdfTerm('MedicalWebPage', 'https://schema.org/MedicalWebPage', [])

class CollectionPage(WebPage):
    term = RdfTerm('CollectionPage', 'https://schema.org/CollectionPage', [])

class AboutPage(WebPage):
    term = RdfTerm('AboutPage', 'https://schema.org/AboutPage', [])

class VideoGame(SoftwareApplication, Game):
    term = RdfTerm('VideoGame', 'https://schema.org/VideoGame', [])

class WebApplication(SoftwareApplication):
    term = RdfTerm('WebApplication', 'https://schema.org/WebApplication', [])

class MobileApplication(SoftwareApplication):
    term = RdfTerm('MobileApplication', 'https://schema.org/MobileApplication', [])

class GeoCoordinates(StructuredValue):
    term = RdfTerm('GeoCoordinates', 'https://schema.org/GeoCoordinates', [])

class DeliveryTimeSettings(StructuredValue):
    term = RdfTerm('DeliveryTimeSettings', 'https://schema.org/DeliveryTimeSettings', [])

class InteractionCounter(StructuredValue):
    term = RdfTerm('InteractionCounter', 'https://schema.org/InteractionCounter', [])

class DatedMoneySpecification(StructuredValue):
    term = RdfTerm('DatedMoneySpecification', 'https://schema.org/DatedMoneySpecification', [])

class PriceSpecification(StructuredValue):
    term = RdfTerm('PriceSpecification', 'https://schema.org/PriceSpecification', [])

class PostalCodeRangeSpecification(StructuredValue):
    term = RdfTerm('PostalCodeRangeSpecification', 'https://schema.org/PostalCodeRangeSpecification', [])

class ShippingDeliveryTime(StructuredValue):
    term = RdfTerm('ShippingDeliveryTime', 'https://schema.org/ShippingDeliveryTime', [])

class CDCPMDRecord(StructuredValue):
    term = RdfTerm('CDCPMDRecord', 'https://schema.org/CDCPMDRecord', [])

class ShippingConditions(StructuredValue):
    term = RdfTerm('ShippingConditions', 'https://schema.org/ShippingConditions', [])

class MonetaryAmount(StructuredValue):
    term = RdfTerm('MonetaryAmount', 'https://schema.org/MonetaryAmount', [])

class GeoShape(StructuredValue):
    term = RdfTerm('GeoShape', 'https://schema.org/GeoShape', [])

class PropertyValue(StructuredValue):
    term = RdfTerm('PropertyValue', 'https://schema.org/PropertyValue', [])

class WarrantyPromise(StructuredValue):
    term = RdfTerm('WarrantyPromise', 'https://schema.org/WarrantyPromise', [])

class TypeAndQuantityNode(StructuredValue):
    term = RdfTerm('TypeAndQuantityNode', 'https://schema.org/TypeAndQuantityNode', [])

class OwnershipInfo(StructuredValue):
    term = RdfTerm('OwnershipInfo', 'https://schema.org/OwnershipInfo', [])

class NutritionInformation(StructuredValue):
    term = RdfTerm('NutritionInformation', 'https://schema.org/NutritionInformation', [])

class ContactPoint(StructuredValue):
    term = RdfTerm('ContactPoint', 'https://schema.org/ContactPoint', [])

class QuantitativeValue(StructuredValue):
    term = RdfTerm('QuantitativeValue', 'https://schema.org/QuantitativeValue', [])

class ShippingService(StructuredValue):
    term = RdfTerm('ShippingService', 'https://schema.org/ShippingService', [])

class DefinedRegion(StructuredValue):
    term = RdfTerm('DefinedRegion', 'https://schema.org/DefinedRegion', [])

class ExchangeRateSpecification(StructuredValue):
    term = RdfTerm('ExchangeRateSpecification', 'https://schema.org/ExchangeRateSpecification', [])

class QuantitativeValueDistribution(StructuredValue):
    term = RdfTerm('QuantitativeValueDistribution', 'https://schema.org/QuantitativeValueDistribution', [])

class ShippingRateSettings(StructuredValue):
    term = RdfTerm('ShippingRateSettings', 'https://schema.org/ShippingRateSettings', [])

class EngineSpecification(StructuredValue):
    term = RdfTerm('EngineSpecification', 'https://schema.org/EngineSpecification', [])

class OpeningHoursSpecification(StructuredValue):
    term = RdfTerm('OpeningHoursSpecification', 'https://schema.org/OpeningHoursSpecification', [])

class ServicePeriod(StructuredValue):
    term = RdfTerm('ServicePeriod', 'https://schema.org/ServicePeriod', [])

class OfferShippingDetails(StructuredValue):
    term = RdfTerm('OfferShippingDetails', 'https://schema.org/OfferShippingDetails', [])

class RepaymentSpecification(StructuredValue):
    term = RdfTerm('RepaymentSpecification', 'https://schema.org/RepaymentSpecification', [])

class EventSeries(Series, Event):
    term = RdfTerm('EventSeries', 'https://schema.org/EventSeries', [])

class CreativeWorkSeries(Series, CreativeWork):
    term = RdfTerm('CreativeWorkSeries', 'https://schema.org/CreativeWorkSeries', [])

class RadioChannel(BroadcastChannel):
    term = RdfTerm('RadioChannel', 'https://schema.org/RadioChannel', [])

class TelevisionChannel(BroadcastChannel):
    term = RdfTerm('TelevisionChannel', 'https://schema.org/TelevisionChannel', [])

class MonetaryGrant(Grant):
    term = RdfTerm('MonetaryGrant', 'https://schema.org/MonetaryGrant', [])

class MediaManipulationRatingEnumeration(Enumeration):
    term = RdfTerm('MediaManipulationRatingEnumeration', 'https://schema.org/MediaManipulationRatingEnumeration', [])

class OfferItemCondition(Enumeration):
    term = RdfTerm('OfferItemCondition', 'https://schema.org/OfferItemCondition', [])

class IncentiveType(Enumeration):
    term = RdfTerm('IncentiveType', 'https://schema.org/IncentiveType', [])

class FulfillmentTypeEnumeration(Enumeration):
    term = RdfTerm('FulfillmentTypeEnumeration', 'https://schema.org/FulfillmentTypeEnumeration', [])

class TierBenefitEnumeration(Enumeration):
    term = RdfTerm('TierBenefitEnumeration', 'https://schema.org/TierBenefitEnumeration', [])

class Specialty(Enumeration):
    term = RdfTerm('Specialty', 'https://schema.org/Specialty', [])

class CertificationStatusEnumeration(Enumeration):
    term = RdfTerm('CertificationStatusEnumeration', 'https://schema.org/CertificationStatusEnumeration', [])

class MedicalEnumeration(Enumeration):
    term = RdfTerm('MedicalEnumeration', 'https://schema.org/MedicalEnumeration', [])

class GamePlayMode(Enumeration):
    term = RdfTerm('GamePlayMode', 'https://schema.org/GamePlayMode', [])

class MeasurementMethodEnum(Enumeration):
    term = RdfTerm('MeasurementMethodEnum', 'https://schema.org/MeasurementMethodEnum', [])

class PriceComponentTypeEnumeration(Enumeration):
    term = RdfTerm('PriceComponentTypeEnumeration', 'https://schema.org/PriceComponentTypeEnumeration', [])

class IncentiveStatus(Enumeration):
    term = RdfTerm('IncentiveStatus', 'https://schema.org/IncentiveStatus', [])

class NonprofitType(Enumeration):
    term = RdfTerm('NonprofitType', 'https://schema.org/NonprofitType', [])

class DayOfWeek(Enumeration):
    term = RdfTerm('DayOfWeek', 'https://schema.org/DayOfWeek', [])

class BookFormatType(Enumeration):
    term = RdfTerm('BookFormatType', 'https://schema.org/BookFormatType', [])

class ItemListOrderType(Enumeration):
    term = RdfTerm('ItemListOrderType', 'https://schema.org/ItemListOrderType', [])

class CarUsageType(Enumeration):
    term = RdfTerm('CarUsageType', 'https://schema.org/CarUsageType', [])

class AdultOrientedEnumeration(Enumeration):
    term = RdfTerm('AdultOrientedEnumeration', 'https://schema.org/AdultOrientedEnumeration', [])

class ReturnLabelSourceEnumeration(Enumeration):
    term = RdfTerm('ReturnLabelSourceEnumeration', 'https://schema.org/ReturnLabelSourceEnumeration', [])

class RefundTypeEnumeration(Enumeration):
    term = RdfTerm('RefundTypeEnumeration', 'https://schema.org/RefundTypeEnumeration', [])

class DeliveryMethod(Enumeration):
    term = RdfTerm('DeliveryMethod', 'https://schema.org/DeliveryMethod', [])

class MerchantReturnEnumeration(Enumeration):
    term = RdfTerm('MerchantReturnEnumeration', 'https://schema.org/MerchantReturnEnumeration', [])

class MusicAlbumReleaseType(Enumeration):
    term = RdfTerm('MusicAlbumReleaseType', 'https://schema.org/MusicAlbumReleaseType', [])

class PhysicalActivityCategory(Enumeration):
    term = RdfTerm('PhysicalActivityCategory', 'https://schema.org/PhysicalActivityCategory', [])

class WarrantyScope(Enumeration):
    term = RdfTerm('WarrantyScope', 'https://schema.org/WarrantyScope', [])

class SizeGroupEnumeration(Enumeration):
    term = RdfTerm('SizeGroupEnumeration', 'https://schema.org/SizeGroupEnumeration', [])

class MediaEnumeration(Enumeration):
    term = RdfTerm('MediaEnumeration', 'https://schema.org/MediaEnumeration', [])

class MusicAlbumProductionType(Enumeration):
    term = RdfTerm('MusicAlbumProductionType', 'https://schema.org/MusicAlbumProductionType', [])

class HealthAspectEnumeration(Enumeration):
    term = RdfTerm('HealthAspectEnumeration', 'https://schema.org/HealthAspectEnumeration', [])

class DigitalPlatformEnumeration(Enumeration):
    term = RdfTerm('DigitalPlatformEnumeration', 'https://schema.org/DigitalPlatformEnumeration', [])

class QualitativeValue(Enumeration):
    term = RdfTerm('QualitativeValue', 'https://schema.org/QualitativeValue', [])

class RestrictedDiet(Enumeration):
    term = RdfTerm('RestrictedDiet', 'https://schema.org/RestrictedDiet', [])

class PaymentMethodType(Enumeration):
    term = RdfTerm('PaymentMethodType', 'https://schema.org/PaymentMethodType', [])

class SizeSystemEnumeration(Enumeration):
    term = RdfTerm('SizeSystemEnumeration', 'https://schema.org/SizeSystemEnumeration', [])

class MeasurementTypeEnumeration(Enumeration):
    term = RdfTerm('MeasurementTypeEnumeration', 'https://schema.org/MeasurementTypeEnumeration', [])

class BoardingPolicyType(Enumeration):
    term = RdfTerm('BoardingPolicyType', 'https://schema.org/BoardingPolicyType', [])

class PurchaseType(Enumeration):
    term = RdfTerm('PurchaseType', 'https://schema.org/PurchaseType', [])

class MapCategoryType(Enumeration):
    term = RdfTerm('MapCategoryType', 'https://schema.org/MapCategoryType', [])

class BusinessFunction(Enumeration):
    term = RdfTerm('BusinessFunction', 'https://schema.org/BusinessFunction', [])

class IncentiveQualifiedExpenseType(Enumeration):
    term = RdfTerm('IncentiveQualifiedExpenseType', 'https://schema.org/IncentiveQualifiedExpenseType', [])

class GovernmentBenefitsType(Enumeration):
    term = RdfTerm('GovernmentBenefitsType', 'https://schema.org/GovernmentBenefitsType', [])

class ProductReturnEnumeration(Enumeration):
    term = RdfTerm('ProductReturnEnumeration', 'https://schema.org/ProductReturnEnumeration', [])

class LegalValueLevel(Enumeration):
    term = RdfTerm('LegalValueLevel', 'https://schema.org/LegalValueLevel', [])

class BusinessEntityType(Enumeration):
    term = RdfTerm('BusinessEntityType', 'https://schema.org/BusinessEntityType', [])

class StatusEnumeration(Enumeration):
    term = RdfTerm('StatusEnumeration', 'https://schema.org/StatusEnumeration', [])

class ReturnFeesEnumeration(Enumeration):
    term = RdfTerm('ReturnFeesEnumeration', 'https://schema.org/ReturnFeesEnumeration', [])

class GenderType(Enumeration):
    term = RdfTerm('GenderType', 'https://schema.org/GenderType', [])

class PriceTypeEnumeration(Enumeration):
    term = RdfTerm('PriceTypeEnumeration', 'https://schema.org/PriceTypeEnumeration', [])

class DigitalDocumentPermissionType(Enumeration):
    term = RdfTerm('DigitalDocumentPermissionType', 'https://schema.org/DigitalDocumentPermissionType', [])

class GameAvailabilityEnumeration(Enumeration):
    term = RdfTerm('GameAvailabilityEnumeration', 'https://schema.org/GameAvailabilityEnumeration', [])

class EventAttendanceModeEnumeration(Enumeration):
    term = RdfTerm('EventAttendanceModeEnumeration', 'https://schema.org/EventAttendanceModeEnumeration', [])

class RsvpResponseType(Enumeration):
    term = RdfTerm('RsvpResponseType', 'https://schema.org/RsvpResponseType', [])

class EnergyEfficiencyEnumeration(Enumeration):
    term = RdfTerm('EnergyEfficiencyEnumeration', 'https://schema.org/EnergyEfficiencyEnumeration', [])

class ItemAvailability(Enumeration):
    term = RdfTerm('ItemAvailability', 'https://schema.org/ItemAvailability', [])

class ReturnMethodEnumeration(Enumeration):
    term = RdfTerm('ReturnMethodEnumeration', 'https://schema.org/ReturnMethodEnumeration', [])

class ContactPointOption(Enumeration):
    term = RdfTerm('ContactPointOption', 'https://schema.org/ContactPointOption', [])

class MusicReleaseFormatType(Enumeration):
    term = RdfTerm('MusicReleaseFormatType', 'https://schema.org/MusicReleaseFormatType', [])

class OfferCatalog(ItemList):
    term = RdfTerm('OfferCatalog', 'https://schema.org/OfferCatalog', [])

class BreadcrumbList(ItemList):
    term = RdfTerm('BreadcrumbList', 'https://schema.org/BreadcrumbList', [])

class StatisticalVariable(ConstraintNode):
    term = RdfTerm('StatisticalVariable', 'https://schema.org/StatisticalVariable', [])

class LinkRole(Role):
    term = RdfTerm('LinkRole', 'https://schema.org/LinkRole', [])

class PerformanceRole(Role):
    term = RdfTerm('PerformanceRole', 'https://schema.org/PerformanceRole', [])

class OrganizationRole(Role):
    term = RdfTerm('OrganizationRole', 'https://schema.org/OrganizationRole', [])

class BusinessAudience(Audience):
    term = RdfTerm('BusinessAudience', 'https://schema.org/BusinessAudience', [])

class EducationalAudience(Audience):
    term = RdfTerm('EducationalAudience', 'https://schema.org/EducationalAudience', [])

class PeopleAudience(Audience):
    term = RdfTerm('PeopleAudience', 'https://schema.org/PeopleAudience', [])

class Researcher(Audience):
    term = RdfTerm('Researcher', 'https://schema.org/Researcher', [])

class GovernmentPermit(Permit):
    term = RdfTerm('GovernmentPermit', 'https://schema.org/GovernmentPermit', [])

class LodgingReservation(Reservation):
    term = RdfTerm('LodgingReservation', 'https://schema.org/LodgingReservation', [])

class RentalCarReservation(Reservation):
    term = RdfTerm('RentalCarReservation', 'https://schema.org/RentalCarReservation', [])

class FlightReservation(Reservation):
    term = RdfTerm('FlightReservation', 'https://schema.org/FlightReservation', [])

class BoatReservation(Reservation):
    term = RdfTerm('BoatReservation', 'https://schema.org/BoatReservation', [])

class TrainReservation(Reservation):
    term = RdfTerm('TrainReservation', 'https://schema.org/TrainReservation', [])

class EventReservation(Reservation):
    term = RdfTerm('EventReservation', 'https://schema.org/EventReservation', [])

class FoodEstablishmentReservation(Reservation):
    term = RdfTerm('FoodEstablishmentReservation', 'https://schema.org/FoodEstablishmentReservation', [])

class BusReservation(Reservation):
    term = RdfTerm('BusReservation', 'https://schema.org/BusReservation', [])

class TaxiReservation(Reservation):
    term = RdfTerm('TaxiReservation', 'https://schema.org/TaxiReservation', [])

class ReservationPackage(Reservation):
    term = RdfTerm('ReservationPackage', 'https://schema.org/ReservationPackage', [])

class CategoryCode(DefinedTerm):
    term = RdfTerm('CategoryCode', 'https://schema.org/CategoryCode', [])

class Mass(Quantity):
    term = RdfTerm('Mass', 'https://schema.org/Mass', [])

class Distance(Quantity):
    term = RdfTerm('Distance', 'https://schema.org/Distance', [])

class Duration(Quantity):
    term = RdfTerm('Duration', 'https://schema.org/Duration', [])

class Energy(Quantity):
    term = RdfTerm('Energy', 'https://schema.org/Energy', [])

class WorkBasedProgram(EducationalOccupationalProgram):
    term = RdfTerm('WorkBasedProgram', 'https://schema.org/WorkBasedProgram', [])

class TrainTrip(Trip):
    term = RdfTerm('TrainTrip', 'https://schema.org/TrainTrip', [])

class Flight(Trip):
    term = RdfTerm('Flight', 'https://schema.org/Flight', [])

class BoatTrip(Trip):
    term = RdfTerm('BoatTrip', 'https://schema.org/BoatTrip', [])

class TouristTrip(Trip):
    term = RdfTerm('TouristTrip', 'https://schema.org/TouristTrip', [])

class BusTrip(Trip):
    term = RdfTerm('BusTrip', 'https://schema.org/BusTrip', [])

class CableOrSatelliteService(Service):
    term = RdfTerm('CableOrSatelliteService', 'https://schema.org/CableOrSatelliteService', [])

class Taxi(Service):
    term = RdfTerm('Taxi', 'https://schema.org/Taxi', [])

class FinancialProduct(Service):
    term = RdfTerm('FinancialProduct', 'https://schema.org/FinancialProduct', [])

class BroadcastService(Service):
    term = RdfTerm('BroadcastService', 'https://schema.org/BroadcastService', [])

class FoodService(Service):
    term = RdfTerm('FoodService', 'https://schema.org/FoodService', [])

class TaxiService(Service):
    term = RdfTerm('TaxiService', 'https://schema.org/TaxiService', [])

class WebAPI(Service):
    term = RdfTerm('WebAPI', 'https://schema.org/WebAPI', [])

class GovernmentService(Service):
    term = RdfTerm('GovernmentService', 'https://schema.org/GovernmentService', [])

class HowToStep(ItemList, CreativeWork, ListItem):
    term = RdfTerm('HowToStep', 'https://schema.org/HowToStep', [])

class HowToDirection(CreativeWork, ListItem):
    term = RdfTerm('HowToDirection', 'https://schema.org/HowToDirection', [])

class HowToSection(ListItem, ItemList, CreativeWork):
    term = RdfTerm('HowToSection', 'https://schema.org/HowToSection', [])

class HowToTip(ListItem, CreativeWork):
    term = RdfTerm('HowToTip', 'https://schema.org/HowToTip', [])

class HowToItem(ListItem):
    term = RdfTerm('HowToItem', 'https://schema.org/HowToItem', [])

class EndorsementRating(Rating):
    term = RdfTerm('EndorsementRating', 'https://schema.org/EndorsementRating', [])

class AggregateRating(Rating):
    term = RdfTerm('AggregateRating', 'https://schema.org/AggregateRating', [])

class OfferForPurchase(Offer):
    term = RdfTerm('OfferForPurchase', 'https://schema.org/OfferForPurchase', [])

class OfferForLease(Offer):
    term = RdfTerm('OfferForLease', 'https://schema.org/OfferForLease', [])

class AggregateOffer(Offer):
    term = RdfTerm('AggregateOffer', 'https://schema.org/AggregateOffer', [])

class ChooseAction(AssessAction):
    term = RdfTerm('ChooseAction', 'https://schema.org/ChooseAction', [])

class ReactAction(AssessAction):
    term = RdfTerm('ReactAction', 'https://schema.org/ReactAction', [])

class IgnoreAction(AssessAction):
    term = RdfTerm('IgnoreAction', 'https://schema.org/IgnoreAction', [])

class ReviewAction(AssessAction):
    term = RdfTerm('ReviewAction', 'https://schema.org/ReviewAction', [])

class ResumeAction(ControlAction):
    term = RdfTerm('ResumeAction', 'https://schema.org/ResumeAction', [])

class ActivateAction(ControlAction):
    term = RdfTerm('ActivateAction', 'https://schema.org/ActivateAction', [])

class DeactivateAction(ControlAction):
    term = RdfTerm('DeactivateAction', 'https://schema.org/DeactivateAction', [])

class SuspendAction(ControlAction):
    term = RdfTerm('SuspendAction', 'https://schema.org/SuspendAction', [])

class ArriveAction(MoveAction):
    term = RdfTerm('ArriveAction', 'https://schema.org/ArriveAction', [])

class TravelAction(MoveAction):
    term = RdfTerm('TravelAction', 'https://schema.org/TravelAction', [])

class DepartAction(MoveAction):
    term = RdfTerm('DepartAction', 'https://schema.org/DepartAction', [])

class LoseAction(AchieveAction):
    term = RdfTerm('LoseAction', 'https://schema.org/LoseAction', [])

class WinAction(AchieveAction):
    term = RdfTerm('WinAction', 'https://schema.org/WinAction', [])

class TieAction(AchieveAction):
    term = RdfTerm('TieAction', 'https://schema.org/TieAction', [])

class DonateAction(TransferAction):
    term = RdfTerm('DonateAction', 'https://schema.org/DonateAction', [])

class SendAction(TransferAction):
    term = RdfTerm('SendAction', 'https://schema.org/SendAction', [])

class ReceiveAction(TransferAction):
    term = RdfTerm('ReceiveAction', 'https://schema.org/ReceiveAction', [])

class GiveAction(TransferAction):
    term = RdfTerm('GiveAction', 'https://schema.org/GiveAction', [])

class DownloadAction(TransferAction):
    term = RdfTerm('DownloadAction', 'https://schema.org/DownloadAction', [])

class ReturnAction(TransferAction):
    term = RdfTerm('ReturnAction', 'https://schema.org/ReturnAction', [])

class LendAction(TransferAction):
    term = RdfTerm('LendAction', 'https://schema.org/LendAction', [])

class BorrowAction(TransferAction):
    term = RdfTerm('BorrowAction', 'https://schema.org/BorrowAction', [])

class TakeAction(TransferAction):
    term = RdfTerm('TakeAction', 'https://schema.org/TakeAction', [])

class MoneyTransfer(TransferAction):
    term = RdfTerm('MoneyTransfer', 'https://schema.org/MoneyTransfer', [])

class QuoteAction(TradeAction):
    term = RdfTerm('QuoteAction', 'https://schema.org/QuoteAction', [])

class SellAction(TradeAction):
    term = RdfTerm('SellAction', 'https://schema.org/SellAction', [])

class OrderAction(TradeAction):
    term = RdfTerm('OrderAction', 'https://schema.org/OrderAction', [])

class PreOrderAction(TradeAction):
    term = RdfTerm('PreOrderAction', 'https://schema.org/PreOrderAction', [])

class BuyAction(TradeAction):
    term = RdfTerm('BuyAction', 'https://schema.org/BuyAction', [])

class RentAction(TradeAction):
    term = RdfTerm('RentAction', 'https://schema.org/RentAction', [])

class PayAction(TradeAction):
    term = RdfTerm('PayAction', 'https://schema.org/PayAction', [])

class TipAction(TradeAction):
    term = RdfTerm('TipAction', 'https://schema.org/TipAction', [])

class PhotographAction(CreateAction):
    term = RdfTerm('PhotographAction', 'https://schema.org/PhotographAction', [])

class PaintAction(CreateAction):
    term = RdfTerm('PaintAction', 'https://schema.org/PaintAction', [])

class DrawAction(CreateAction):
    term = RdfTerm('DrawAction', 'https://schema.org/DrawAction', [])

class CookAction(CreateAction):
    term = RdfTerm('CookAction', 'https://schema.org/CookAction', [])

class WriteAction(CreateAction):
    term = RdfTerm('WriteAction', 'https://schema.org/WriteAction', [])

class FilmAction(CreateAction):
    term = RdfTerm('FilmAction', 'https://schema.org/FilmAction', [])

class DeleteAction(UpdateAction):
    term = RdfTerm('DeleteAction', 'https://schema.org/DeleteAction', [])

class AddAction(UpdateAction):
    term = RdfTerm('AddAction', 'https://schema.org/AddAction', [])

class ReplaceAction(UpdateAction):
    term = RdfTerm('ReplaceAction', 'https://schema.org/ReplaceAction', [])

class DrinkAction(ConsumeAction):
    term = RdfTerm('DrinkAction', 'https://schema.org/DrinkAction', [])

class WatchAction(ConsumeAction):
    term = RdfTerm('WatchAction', 'https://schema.org/WatchAction', [])

class UseAction(ConsumeAction):
    term = RdfTerm('UseAction', 'https://schema.org/UseAction', [])

class ReadAction(ConsumeAction):
    term = RdfTerm('ReadAction', 'https://schema.org/ReadAction', [])

class ListenAction(ConsumeAction):
    term = RdfTerm('ListenAction', 'https://schema.org/ListenAction', [])

class InstallAction(ConsumeAction):
    term = RdfTerm('InstallAction', 'https://schema.org/InstallAction', [])

class ViewAction(ConsumeAction):
    term = RdfTerm('ViewAction', 'https://schema.org/ViewAction', [])

class EatAction(ConsumeAction):
    term = RdfTerm('EatAction', 'https://schema.org/EatAction', [])

class PlayGameAction(ConsumeAction):
    term = RdfTerm('PlayGameAction', 'https://schema.org/PlayGameAction', [])

class UnRegisterAction(InteractAction):
    term = RdfTerm('UnRegisterAction', 'https://schema.org/UnRegisterAction', [])

class JoinAction(InteractAction):
    term = RdfTerm('JoinAction', 'https://schema.org/JoinAction', [])

class MarryAction(InteractAction):
    term = RdfTerm('MarryAction', 'https://schema.org/MarryAction', [])

class LeaveAction(InteractAction):
    term = RdfTerm('LeaveAction', 'https://schema.org/LeaveAction', [])

class CommunicateAction(InteractAction):
    term = RdfTerm('CommunicateAction', 'https://schema.org/CommunicateAction', [])

class RegisterAction(InteractAction):
    term = RdfTerm('RegisterAction', 'https://schema.org/RegisterAction', [])

class SubscribeAction(InteractAction):
    term = RdfTerm('SubscribeAction', 'https://schema.org/SubscribeAction', [])

class FollowAction(InteractAction):
    term = RdfTerm('FollowAction', 'https://schema.org/FollowAction', [])

class BefriendAction(InteractAction):
    term = RdfTerm('BefriendAction', 'https://schema.org/BefriendAction', [])

class ExerciseAction(PlayAction):
    term = RdfTerm('ExerciseAction', 'https://schema.org/ExerciseAction', [])

class PerformAction(PlayAction):
    term = RdfTerm('PerformAction', 'https://schema.org/PerformAction', [])

class BookmarkAction(OrganizeAction):
    term = RdfTerm('BookmarkAction', 'https://schema.org/BookmarkAction', [])

class ApplyAction(OrganizeAction):
    term = RdfTerm('ApplyAction', 'https://schema.org/ApplyAction', [])

class PlanAction(OrganizeAction):
    term = RdfTerm('PlanAction', 'https://schema.org/PlanAction', [])

class AllocateAction(OrganizeAction):
    term = RdfTerm('AllocateAction', 'https://schema.org/AllocateAction', [])

class CheckAction(FindAction):
    term = RdfTerm('CheckAction', 'https://schema.org/CheckAction', [])

class DiscoverAction(FindAction):
    term = RdfTerm('DiscoverAction', 'https://schema.org/DiscoverAction', [])

class TrackAction(FindAction):
    term = RdfTerm('TrackAction', 'https://schema.org/TrackAction', [])

class MedicalTestPanel(MedicalTest):
    term = RdfTerm('MedicalTestPanel', 'https://schema.org/MedicalTestPanel', [])

class PathologyTest(MedicalTest):
    term = RdfTerm('PathologyTest', 'https://schema.org/PathologyTest', [])

class ImagingTest(MedicalTest):
    term = RdfTerm('ImagingTest', 'https://schema.org/ImagingTest', [])

class BloodTest(MedicalTest):
    term = RdfTerm('BloodTest', 'https://schema.org/BloodTest', [])

class MedicalObservationalStudy(MedicalStudy):
    term = RdfTerm('MedicalObservationalStudy', 'https://schema.org/MedicalObservationalStudy', [])

class MedicalTrial(MedicalStudy):
    term = RdfTerm('MedicalTrial', 'https://schema.org/MedicalTrial', [])

class TherapeuticProcedure(MedicalProcedure):
    term = RdfTerm('TherapeuticProcedure', 'https://schema.org/TherapeuticProcedure', [])

class SurgicalProcedure(MedicalProcedure):
    term = RdfTerm('SurgicalProcedure', 'https://schema.org/SurgicalProcedure', [])

class DiagnosticProcedure(MedicalProcedure):
    term = RdfTerm('DiagnosticProcedure', 'https://schema.org/DiagnosticProcedure', [])

class MedicalRiskScore(MedicalRiskEstimator):
    term = RdfTerm('MedicalRiskScore', 'https://schema.org/MedicalRiskScore', [])

class MedicalRiskCalculator(MedicalRiskEstimator):
    term = RdfTerm('MedicalRiskCalculator', 'https://schema.org/MedicalRiskCalculator', [])

class MedicalSignOrSymptom(MedicalCondition):
    term = RdfTerm('MedicalSignOrSymptom', 'https://schema.org/MedicalSignOrSymptom', [])

class InfectiousDisease(MedicalCondition):
    term = RdfTerm('InfectiousDisease', 'https://schema.org/InfectiousDisease', [])

class Muscle(AnatomicalStructure):
    term = RdfTerm('Muscle', 'https://schema.org/Muscle', [])

class BrainStructure(AnatomicalStructure):
    term = RdfTerm('BrainStructure', 'https://schema.org/BrainStructure', [])

class Nerve(AnatomicalStructure):
    term = RdfTerm('Nerve', 'https://schema.org/Nerve', [])

class Joint(AnatomicalStructure):
    term = RdfTerm('Joint', 'https://schema.org/Joint', [])

class Vessel(AnatomicalStructure):
    term = RdfTerm('Vessel', 'https://schema.org/Vessel', [])

class Ligament(AnatomicalStructure):
    term = RdfTerm('Ligament', 'https://schema.org/Ligament', [])

class Bone(AnatomicalStructure):
    term = RdfTerm('Bone', 'https://schema.org/Bone', [])

class MedicalGuidelineContraindication(MedicalGuideline):
    term = RdfTerm('MedicalGuidelineContraindication', 'https://schema.org/MedicalGuidelineContraindication', [])

class MedicalGuidelineRecommendation(MedicalGuideline):
    term = RdfTerm('MedicalGuidelineRecommendation', 'https://schema.org/MedicalGuidelineRecommendation', [])

class Drug(Product, Substance):
    term = RdfTerm('Drug', 'https://schema.org/Drug', [])

class DietarySupplement(Product, Substance):
    term = RdfTerm('DietarySupplement', 'https://schema.org/DietarySupplement', [])

class Diet(CreativeWork, LifestyleModification):
    term = RdfTerm('Diet', 'https://schema.org/Diet', [])

class PhysicalActivity(LifestyleModification):
    term = RdfTerm('PhysicalActivity', 'https://schema.org/PhysicalActivity', [])

class ApprovedIndication(MedicalIndication):
    term = RdfTerm('ApprovedIndication', 'https://schema.org/ApprovedIndication', [])

class PreventionIndication(MedicalIndication):
    term = RdfTerm('PreventionIndication', 'https://schema.org/PreventionIndication', [])

class TreatmentIndication(MedicalIndication):
    term = RdfTerm('TreatmentIndication', 'https://schema.org/TreatmentIndication', [])

class MedicalConditionStage(MedicalIntangible):
    term = RdfTerm('MedicalConditionStage', 'https://schema.org/MedicalConditionStage', [])

class DrugLegalStatus(MedicalIntangible):
    term = RdfTerm('DrugLegalStatus', 'https://schema.org/DrugLegalStatus', [])

class DDxElement(MedicalIntangible):
    term = RdfTerm('DDxElement', 'https://schema.org/DDxElement', [])

class DrugStrength(MedicalIntangible):
    term = RdfTerm('DrugStrength', 'https://schema.org/DrugStrength', [])

class DoseSchedule(MedicalIntangible):
    term = RdfTerm('DoseSchedule', 'https://schema.org/DoseSchedule', [])

class DiagnosticLab(MedicalOrganization):
    term = RdfTerm('DiagnosticLab', 'https://schema.org/DiagnosticLab', [])

class VeterinaryCare(MedicalOrganization):
    term = RdfTerm('VeterinaryCare', 'https://schema.org/VeterinaryCare', [])

class FundingAgency(Project):
    term = RdfTerm('FundingAgency', 'https://schema.org/FundingAgency', [])

class ResearchProject(Project):
    term = RdfTerm('ResearchProject', 'https://schema.org/ResearchProject', [])

class SelfStorage(LocalBusiness):
    term = RdfTerm('SelfStorage', 'https://schema.org/SelfStorage', [])

class ShoppingCenter(LocalBusiness):
    term = RdfTerm('ShoppingCenter', 'https://schema.org/ShoppingCenter', [])

class MedicalBusiness(LocalBusiness):
    term = RdfTerm('MedicalBusiness', 'https://schema.org/MedicalBusiness', [])

class GovernmentOffice(LocalBusiness):
    term = RdfTerm('GovernmentOffice', 'https://schema.org/GovernmentOffice', [])

class LodgingBusiness(LocalBusiness):
    term = RdfTerm('LodgingBusiness', 'https://schema.org/LodgingBusiness', [])

class DryCleaningOrLaundry(LocalBusiness):
    term = RdfTerm('DryCleaningOrLaundry', 'https://schema.org/DryCleaningOrLaundry', [])

class EmergencyService(LocalBusiness):
    term = RdfTerm('EmergencyService', 'https://schema.org/EmergencyService', [])

class Library(LocalBusiness):
    term = RdfTerm('Library', 'https://schema.org/Library', [])

class InternetCafe(LocalBusiness):
    term = RdfTerm('InternetCafe', 'https://schema.org/InternetCafe', [])

class ProfessionalService(LocalBusiness):
    term = RdfTerm('ProfessionalService', 'https://schema.org/ProfessionalService', [])

class HealthAndBeautyBusiness(LocalBusiness):
    term = RdfTerm('HealthAndBeautyBusiness', 'https://schema.org/HealthAndBeautyBusiness', [])

class HomeAndConstructionBusiness(LocalBusiness):
    term = RdfTerm('HomeAndConstructionBusiness', 'https://schema.org/HomeAndConstructionBusiness', [])

class FoodEstablishment(LocalBusiness):
    term = RdfTerm('FoodEstablishment', 'https://schema.org/FoodEstablishment', [])

class EmploymentAgency(LocalBusiness):
    term = RdfTerm('EmploymentAgency', 'https://schema.org/EmploymentAgency', [])

class LegalService(LocalBusiness):
    term = RdfTerm('LegalService', 'https://schema.org/LegalService', [])

class FinancialService(LocalBusiness):
    term = RdfTerm('FinancialService', 'https://schema.org/FinancialService', [])

class ArchiveOrganization(LocalBusiness):
    term = RdfTerm('ArchiveOrganization', 'https://schema.org/ArchiveOrganization', [])

class RecyclingCenter(LocalBusiness):
    term = RdfTerm('RecyclingCenter', 'https://schema.org/RecyclingCenter', [])

class SportsActivityLocation(LocalBusiness):
    term = RdfTerm('SportsActivityLocation', 'https://schema.org/SportsActivityLocation', [])

class AnimalShelter(LocalBusiness):
    term = RdfTerm('AnimalShelter', 'https://schema.org/AnimalShelter', [])

class Store(LocalBusiness):
    term = RdfTerm('Store', 'https://schema.org/Store', [])

class TouristInformationCenter(LocalBusiness):
    term = RdfTerm('TouristInformationCenter', 'https://schema.org/TouristInformationCenter', [])

class TravelAgency(LocalBusiness):
    term = RdfTerm('TravelAgency', 'https://schema.org/TravelAgency', [])

class RealEstateAgent(LocalBusiness):
    term = RdfTerm('RealEstateAgent', 'https://schema.org/RealEstateAgent', [])

class TelevisionStation(LocalBusiness):
    term = RdfTerm('TelevisionStation', 'https://schema.org/TelevisionStation', [])

class RadioStation(LocalBusiness):
    term = RdfTerm('RadioStation', 'https://schema.org/RadioStation', [])

class ChildCare(LocalBusiness):
    term = RdfTerm('ChildCare', 'https://schema.org/ChildCare', [])

class AutomotiveBusiness(LocalBusiness):
    term = RdfTerm('AutomotiveBusiness', 'https://schema.org/AutomotiveBusiness', [])

class EntertainmentBusiness(LocalBusiness):
    term = RdfTerm('EntertainmentBusiness', 'https://schema.org/EntertainmentBusiness', [])

class OnlineStore(OnlineBusiness):
    term = RdfTerm('OnlineStore', 'https://schema.org/OnlineStore', [])

class DanceGroup(PerformingGroup):
    term = RdfTerm('DanceGroup', 'https://schema.org/DanceGroup', [])

class MusicGroup(PerformingGroup):
    term = RdfTerm('MusicGroup', 'https://schema.org/MusicGroup', [])

class TheaterGroup(PerformingGroup):
    term = RdfTerm('TheaterGroup', 'https://schema.org/TheaterGroup', [])

class SportsTeam(SportsOrganization):
    term = RdfTerm('SportsTeam', 'https://schema.org/SportsTeam', [])

class Reservoir(BodyOfWater):
    term = RdfTerm('Reservoir', 'https://schema.org/Reservoir', [])

class Pond(BodyOfWater):
    term = RdfTerm('Pond', 'https://schema.org/Pond', [])

class LakeBodyOfWater(BodyOfWater):
    term = RdfTerm('LakeBodyOfWater', 'https://schema.org/LakeBodyOfWater', [])

class Canal(BodyOfWater):
    term = RdfTerm('Canal', 'https://schema.org/Canal', [])

class OceanBodyOfWater(BodyOfWater):
    term = RdfTerm('OceanBodyOfWater', 'https://schema.org/OceanBodyOfWater', [])

class SeaBodyOfWater(BodyOfWater):
    term = RdfTerm('SeaBodyOfWater', 'https://schema.org/SeaBodyOfWater', [])

class RiverBodyOfWater(BodyOfWater):
    term = RdfTerm('RiverBodyOfWater', 'https://schema.org/RiverBodyOfWater', [])

class Waterfall(BodyOfWater):
    term = RdfTerm('Waterfall', 'https://schema.org/Waterfall', [])

class CityHall(GovernmentBuilding):
    term = RdfTerm('CityHall', 'https://schema.org/CityHall', [])

class Embassy(GovernmentBuilding):
    term = RdfTerm('Embassy', 'https://schema.org/Embassy', [])

class DefenceEstablishment(GovernmentBuilding):
    term = RdfTerm('DefenceEstablishment', 'https://schema.org/DefenceEstablishment', [])

class Courthouse(GovernmentBuilding):
    term = RdfTerm('Courthouse', 'https://schema.org/Courthouse', [])

class LegislativeBuilding(GovernmentBuilding):
    term = RdfTerm('LegislativeBuilding', 'https://schema.org/LegislativeBuilding', [])

class HinduTemple(PlaceOfWorship):
    term = RdfTerm('HinduTemple', 'https://schema.org/HinduTemple', [])

class BuddhistTemple(PlaceOfWorship):
    term = RdfTerm('BuddhistTemple', 'https://schema.org/BuddhistTemple', [])

class Synagogue(PlaceOfWorship):
    term = RdfTerm('Synagogue', 'https://schema.org/Synagogue', [])

class Church(PlaceOfWorship):
    term = RdfTerm('Church', 'https://schema.org/Church', [])

class Mosque(PlaceOfWorship):
    term = RdfTerm('Mosque', 'https://schema.org/Mosque', [])

class MiddleSchool(EducationalOrganization):
    term = RdfTerm('MiddleSchool', 'https://schema.org/MiddleSchool', [])

class ElementarySchool(EducationalOrganization):
    term = RdfTerm('ElementarySchool', 'https://schema.org/ElementarySchool', [])

class School(EducationalOrganization):
    term = RdfTerm('School', 'https://schema.org/School', [])

class CollegeOrUniversity(EducationalOrganization):
    term = RdfTerm('CollegeOrUniversity', 'https://schema.org/CollegeOrUniversity', [])

class Preschool(EducationalOrganization):
    term = RdfTerm('Preschool', 'https://schema.org/Preschool', [])

class HighSchool(EducationalOrganization):
    term = RdfTerm('HighSchool', 'https://schema.org/HighSchool', [])

class MeetingRoom(Room):
    term = RdfTerm('MeetingRoom', 'https://schema.org/MeetingRoom', [])

class HotelRoom(Room):
    term = RdfTerm('HotelRoom', 'https://schema.org/HotelRoom', [])

class SingleFamilyResidence(House):
    term = RdfTerm('SingleFamilyResidence', 'https://schema.org/SingleFamilyResidence', [])

class CompleteDataFeed(DataFeed):
    term = RdfTerm('CompleteDataFeed', 'https://schema.org/CompleteDataFeed', [])

class BlogPosting(SocialMediaPosting):
    term = RdfTerm('BlogPosting', 'https://schema.org/BlogPosting', [])

class DiscussionForumPosting(SocialMediaPosting):
    term = RdfTerm('DiscussionForumPosting', 'https://schema.org/DiscussionForumPosting', [])

class ReportageNewsArticle(NewsArticle):
    term = RdfTerm('ReportageNewsArticle', 'https://schema.org/ReportageNewsArticle', [])

class AskPublicNewsArticle(NewsArticle):
    term = RdfTerm('AskPublicNewsArticle', 'https://schema.org/AskPublicNewsArticle', [])

class BackgroundNewsArticle(NewsArticle):
    term = RdfTerm('BackgroundNewsArticle', 'https://schema.org/BackgroundNewsArticle', [])

class AnalysisNewsArticle(NewsArticle):
    term = RdfTerm('AnalysisNewsArticle', 'https://schema.org/AnalysisNewsArticle', [])

class OpinionNewsArticle(NewsArticle):
    term = RdfTerm('OpinionNewsArticle', 'https://schema.org/OpinionNewsArticle', [])

class MedicalScholarlyArticle(ScholarlyArticle):
    term = RdfTerm('MedicalScholarlyArticle', 'https://schema.org/MedicalScholarlyArticle', [])

class APIReference(TechArticle):
    term = RdfTerm('APIReference', 'https://schema.org/APIReference', [])

class ComicCoverArt(ComicStory, CoverArt):
    term = RdfTerm('ComicCoverArt', 'https://schema.org/ComicCoverArt', [])

class Audiobook(Book, AudioObject):
    term = RdfTerm('Audiobook', 'https://schema.org/Audiobook', [])

class AudioObjectSnapshot(AudioObject):
    term = RdfTerm('AudioObjectSnapshot', 'https://schema.org/AudioObjectSnapshot', [])

class VideoObjectSnapshot(VideoObject):
    term = RdfTerm('VideoObjectSnapshot', 'https://schema.org/VideoObjectSnapshot', [])

class ImageObjectSnapshot(ImageObject):
    term = RdfTerm('ImageObjectSnapshot', 'https://schema.org/ImageObjectSnapshot', [])

class Barcode(ImageObject):
    term = RdfTerm('Barcode', 'https://schema.org/Barcode', [])

class ReviewNewsArticle(NewsArticle, CriticReview):
    term = RdfTerm('ReviewNewsArticle', 'https://schema.org/ReviewNewsArticle', [])

class MediaGallery(CollectionPage):
    term = RdfTerm('MediaGallery', 'https://schema.org/MediaGallery', [])

class DeliveryChargeSpecification(PriceSpecification):
    term = RdfTerm('DeliveryChargeSpecification', 'https://schema.org/DeliveryChargeSpecification', [])

class CompoundPriceSpecification(PriceSpecification):
    term = RdfTerm('CompoundPriceSpecification', 'https://schema.org/CompoundPriceSpecification', [])

class PaymentChargeSpecification(PriceSpecification):
    term = RdfTerm('PaymentChargeSpecification', 'https://schema.org/PaymentChargeSpecification', [])

class UnitPriceSpecification(PriceSpecification):
    term = RdfTerm('UnitPriceSpecification', 'https://schema.org/UnitPriceSpecification', [])

class GeoCircle(GeoShape):
    term = RdfTerm('GeoCircle', 'https://schema.org/GeoCircle', [])

class LocationFeatureSpecification(PropertyValue):
    term = RdfTerm('LocationFeatureSpecification', 'https://schema.org/LocationFeatureSpecification', [])

class PostalAddress(ContactPoint):
    term = RdfTerm('PostalAddress', 'https://schema.org/PostalAddress', [])

class Observation(QuantitativeValue, Intangible):
    term = RdfTerm('Observation', 'https://schema.org/Observation', [])

class MonetaryAmountDistribution(QuantitativeValueDistribution):
    term = RdfTerm('MonetaryAmountDistribution', 'https://schema.org/MonetaryAmountDistribution', [])

class Periodical(CreativeWorkSeries):
    term = RdfTerm('Periodical', 'https://schema.org/Periodical', [])

class VideoGameSeries(CreativeWorkSeries):
    term = RdfTerm('VideoGameSeries', 'https://schema.org/VideoGameSeries', [])

class MovieSeries(CreativeWorkSeries):
    term = RdfTerm('MovieSeries', 'https://schema.org/MovieSeries', [])

class PodcastSeries(CreativeWorkSeries):
    term = RdfTerm('PodcastSeries', 'https://schema.org/PodcastSeries', [])

class TVSeries(CreativeWorkSeries, CreativeWork):
    term = RdfTerm('TVSeries', 'https://schema.org/TVSeries', [])

class RadioSeries(CreativeWorkSeries):
    term = RdfTerm('RadioSeries', 'https://schema.org/RadioSeries', [])

class BookSeries(CreativeWorkSeries):
    term = RdfTerm('BookSeries', 'https://schema.org/BookSeries', [])

class AMRadioChannel(RadioChannel):
    term = RdfTerm('AMRadioChannel', 'https://schema.org/AMRadioChannel', [])

class FMRadioChannel(RadioChannel):
    term = RdfTerm('FMRadioChannel', 'https://schema.org/FMRadioChannel', [])

class MedicineSystem(MedicalEnumeration):
    term = RdfTerm('MedicineSystem', 'https://schema.org/MedicineSystem', [])

class DrugCostCategory(MedicalEnumeration):
    term = RdfTerm('DrugCostCategory', 'https://schema.org/DrugCostCategory', [])

class MedicalSpecialty(Specialty, MedicalEnumeration):
    term = RdfTerm('MedicalSpecialty', 'https://schema.org/MedicalSpecialty', [])

class MedicalImagingTechnique(MedicalEnumeration):
    term = RdfTerm('MedicalImagingTechnique', 'https://schema.org/MedicalImagingTechnique', [])

class PhysicalExam(MedicalEnumeration, MedicalProcedure):
    term = RdfTerm('PhysicalExam', 'https://schema.org/PhysicalExam', [])

class MedicalDevicePurpose(MedicalEnumeration):
    term = RdfTerm('MedicalDevicePurpose', 'https://schema.org/MedicalDevicePurpose', [])

class InfectiousAgentClass(MedicalEnumeration):
    term = RdfTerm('InfectiousAgentClass', 'https://schema.org/InfectiousAgentClass', [])

class MedicalObservationalStudyDesign(MedicalEnumeration):
    term = RdfTerm('MedicalObservationalStudyDesign', 'https://schema.org/MedicalObservationalStudyDesign', [])

class MedicalAudienceType(MedicalEnumeration):
    term = RdfTerm('MedicalAudienceType', 'https://schema.org/MedicalAudienceType', [])

class DrugPregnancyCategory(MedicalEnumeration):
    term = RdfTerm('DrugPregnancyCategory', 'https://schema.org/DrugPregnancyCategory', [])

class DrugPrescriptionStatus(MedicalEnumeration):
    term = RdfTerm('DrugPrescriptionStatus', 'https://schema.org/DrugPrescriptionStatus', [])

class MedicalEvidenceLevel(MedicalEnumeration):
    term = RdfTerm('MedicalEvidenceLevel', 'https://schema.org/MedicalEvidenceLevel', [])

class MedicalTrialDesign(MedicalEnumeration):
    term = RdfTerm('MedicalTrialDesign', 'https://schema.org/MedicalTrialDesign', [])

class MedicalStudyStatus(MedicalEnumeration):
    term = RdfTerm('MedicalStudyStatus', 'https://schema.org/MedicalStudyStatus', [])

class MedicalProcedureType(MedicalEnumeration):
    term = RdfTerm('MedicalProcedureType', 'https://schema.org/MedicalProcedureType', [])

class NLNonprofitType(NonprofitType):
    term = RdfTerm('NLNonprofitType', 'https://schema.org/NLNonprofitType', [])

class USNonprofitType(NonprofitType):
    term = RdfTerm('USNonprofitType', 'https://schema.org/USNonprofitType', [])

class UKNonprofitType(NonprofitType):
    term = RdfTerm('UKNonprofitType', 'https://schema.org/UKNonprofitType', [])

class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    term = RdfTerm('WearableSizeGroupEnumeration', 'https://schema.org/WearableSizeGroupEnumeration', [])

class IPTCDigitalSourceEnumeration(MediaEnumeration):
    term = RdfTerm('IPTCDigitalSourceEnumeration', 'https://schema.org/IPTCDigitalSourceEnumeration', [])

class SizeSpecification(QualitativeValue):
    term = RdfTerm('SizeSpecification', 'https://schema.org/SizeSpecification', [])

class SteeringPositionValue(QualitativeValue):
    term = RdfTerm('SteeringPositionValue', 'https://schema.org/SteeringPositionValue', [])

class DriveWheelConfigurationValue(QualitativeValue):
    term = RdfTerm('DriveWheelConfigurationValue', 'https://schema.org/DriveWheelConfigurationValue', [])

class BedType(QualitativeValue):
    term = RdfTerm('BedType', 'https://schema.org/BedType', [])

class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    term = RdfTerm('WearableSizeSystemEnumeration', 'https://schema.org/WearableSizeSystemEnumeration', [])

class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm('BodyMeasurementTypeEnumeration', 'https://schema.org/BodyMeasurementTypeEnumeration', [])

class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm('WearableMeasurementTypeEnumeration', 'https://schema.org/WearableMeasurementTypeEnumeration', [])

class PaymentStatusType(StatusEnumeration):
    term = RdfTerm('PaymentStatusType', 'https://schema.org/PaymentStatusType', [])

class EventStatusType(StatusEnumeration):
    term = RdfTerm('EventStatusType', 'https://schema.org/EventStatusType', [])

class LegalForceStatus(StatusEnumeration):
    term = RdfTerm('LegalForceStatus', 'https://schema.org/LegalForceStatus', [])

class OrderStatus(StatusEnumeration):
    term = RdfTerm('OrderStatus', 'https://schema.org/OrderStatus', [])

class ActionStatusType(StatusEnumeration):
    term = RdfTerm('ActionStatusType', 'https://schema.org/ActionStatusType', [])

class ReservationStatusType(StatusEnumeration):
    term = RdfTerm('ReservationStatusType', 'https://schema.org/ReservationStatusType', [])

class GameServerStatus(StatusEnumeration):
    term = RdfTerm('GameServerStatus', 'https://schema.org/GameServerStatus', [])

class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm('EUEnergyEfficiencyEnumeration', 'https://schema.org/EUEnergyEfficiencyEnumeration', [])

class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm('EnergyStarEnergyEfficiencyEnumeration', 'https://schema.org/EnergyStarEnergyEfficiencyEnumeration', [])

class EmployeeRole(OrganizationRole):
    term = RdfTerm('EmployeeRole', 'https://schema.org/EmployeeRole', [])

class MedicalAudience(PeopleAudience, Audience):
    term = RdfTerm('MedicalAudience', 'https://schema.org/MedicalAudience', [])

class ParentAudience(PeopleAudience):
    term = RdfTerm('ParentAudience', 'https://schema.org/ParentAudience', [])

class MedicalCode(MedicalIntangible, CategoryCode):
    term = RdfTerm('MedicalCode', 'https://schema.org/MedicalCode', [])

class LoanOrCredit(FinancialProduct):
    term = RdfTerm('LoanOrCredit', 'https://schema.org/LoanOrCredit', [])

class PaymentService(PaymentMethod, FinancialProduct):
    term = RdfTerm('PaymentService', 'https://schema.org/PaymentService', [])

class PaymentCard(FinancialProduct, PaymentMethod):
    term = RdfTerm('PaymentCard', 'https://schema.org/PaymentCard', [])

class BankAccount(FinancialProduct):
    term = RdfTerm('BankAccount', 'https://schema.org/BankAccount', [])

class InvestmentOrDeposit(FinancialProduct):
    term = RdfTerm('InvestmentOrDeposit', 'https://schema.org/InvestmentOrDeposit', [])

class CurrencyConversionService(FinancialProduct):
    term = RdfTerm('CurrencyConversionService', 'https://schema.org/CurrencyConversionService', [])

class RadioBroadcastService(BroadcastService):
    term = RdfTerm('RadioBroadcastService', 'https://schema.org/RadioBroadcastService', [])

class HowToSupply(HowToItem):
    term = RdfTerm('HowToSupply', 'https://schema.org/HowToSupply', [])

class HowToTool(HowToItem):
    term = RdfTerm('HowToTool', 'https://schema.org/HowToTool', [])

class EmployerAggregateRating(AggregateRating):
    term = RdfTerm('EmployerAggregateRating', 'https://schema.org/EmployerAggregateRating', [])

class VoteAction(ChooseAction):
    term = RdfTerm('VoteAction', 'https://schema.org/VoteAction', [])

class DisagreeAction(ReactAction):
    term = RdfTerm('DisagreeAction', 'https://schema.org/DisagreeAction', [])

class LikeAction(ReactAction):
    term = RdfTerm('LikeAction', 'https://schema.org/LikeAction', [])

class EndorseAction(ReactAction):
    term = RdfTerm('EndorseAction', 'https://schema.org/EndorseAction', [])

class DislikeAction(ReactAction):
    term = RdfTerm('DislikeAction', 'https://schema.org/DislikeAction', [])

class WantAction(ReactAction):
    term = RdfTerm('WantAction', 'https://schema.org/WantAction', [])

class AgreeAction(ReactAction):
    term = RdfTerm('AgreeAction', 'https://schema.org/AgreeAction', [])

class InsertAction(AddAction):
    term = RdfTerm('InsertAction', 'https://schema.org/InsertAction', [])

class WearAction(UseAction):
    term = RdfTerm('WearAction', 'https://schema.org/WearAction', [])

class ShareAction(CommunicateAction):
    term = RdfTerm('ShareAction', 'https://schema.org/ShareAction', [])

class InformAction(CommunicateAction):
    term = RdfTerm('InformAction', 'https://schema.org/InformAction', [])

class InviteAction(CommunicateAction):
    term = RdfTerm('InviteAction', 'https://schema.org/InviteAction', [])

class AskAction(CommunicateAction):
    term = RdfTerm('AskAction', 'https://schema.org/AskAction', [])

class ReplyAction(CommunicateAction):
    term = RdfTerm('ReplyAction', 'https://schema.org/ReplyAction', [])

class CommentAction(CommunicateAction):
    term = RdfTerm('CommentAction', 'https://schema.org/CommentAction', [])

class CheckInAction(CommunicateAction):
    term = RdfTerm('CheckInAction', 'https://schema.org/CheckInAction', [])

class CheckOutAction(CommunicateAction):
    term = RdfTerm('CheckOutAction', 'https://schema.org/CheckOutAction', [])

class ReserveAction(PlanAction):
    term = RdfTerm('ReserveAction', 'https://schema.org/ReserveAction', [])

class ScheduleAction(PlanAction):
    term = RdfTerm('ScheduleAction', 'https://schema.org/ScheduleAction', [])

class CancelAction(PlanAction):
    term = RdfTerm('CancelAction', 'https://schema.org/CancelAction', [])

class RejectAction(AllocateAction):
    term = RdfTerm('RejectAction', 'https://schema.org/RejectAction', [])

class AcceptAction(AllocateAction):
    term = RdfTerm('AcceptAction', 'https://schema.org/AcceptAction', [])

class AuthorizeAction(AllocateAction):
    term = RdfTerm('AuthorizeAction', 'https://schema.org/AuthorizeAction', [])

class AssignAction(AllocateAction):
    term = RdfTerm('AssignAction', 'https://schema.org/AssignAction', [])

class MedicalTherapy(TherapeuticProcedure):
    term = RdfTerm('MedicalTherapy', 'https://schema.org/MedicalTherapy', [])

class PsychologicalTreatment(TherapeuticProcedure):
    term = RdfTerm('PsychologicalTreatment', 'https://schema.org/PsychologicalTreatment', [])

class MedicalSign(MedicalSignOrSymptom):
    term = RdfTerm('MedicalSign', 'https://schema.org/MedicalSign', [])

class MedicalSymptom(MedicalSignOrSymptom):
    term = RdfTerm('MedicalSymptom', 'https://schema.org/MedicalSymptom', [])

class LymphaticVessel(Vessel):
    term = RdfTerm('LymphaticVessel', 'https://schema.org/LymphaticVessel', [])

class Vein(Vessel):
    term = RdfTerm('Vein', 'https://schema.org/Vein', [])

class Artery(Vessel):
    term = RdfTerm('Artery', 'https://schema.org/Artery', [])

class ExercisePlan(CreativeWork, PhysicalActivity):
    term = RdfTerm('ExercisePlan', 'https://schema.org/ExercisePlan', [])

class ReportedDoseSchedule(DoseSchedule):
    term = RdfTerm('ReportedDoseSchedule', 'https://schema.org/ReportedDoseSchedule', [])

class MaximumDoseSchedule(DoseSchedule):
    term = RdfTerm('MaximumDoseSchedule', 'https://schema.org/MaximumDoseSchedule', [])

class RecommendedDoseSchedule(DoseSchedule):
    term = RdfTerm('RecommendedDoseSchedule', 'https://schema.org/RecommendedDoseSchedule', [])

class MedicalClinic(MedicalOrganization, MedicalBusiness):
    term = RdfTerm('MedicalClinic', 'https://schema.org/MedicalClinic', [])

class Pharmacy(MedicalOrganization, MedicalBusiness):
    term = RdfTerm('Pharmacy', 'https://schema.org/Pharmacy', [])

class Dentist(LocalBusiness, MedicalOrganization, MedicalBusiness):
    term = RdfTerm('Dentist', 'https://schema.org/Dentist', [])

class Physician(MedicalBusiness, MedicalOrganization):
    term = RdfTerm('Physician', 'https://schema.org/Physician', [])

class Physiotherapy(MedicalBusiness):
    term = RdfTerm('Physiotherapy', 'https://schema.org/Physiotherapy', [])

class PrimaryCare(MedicalBusiness):
    term = RdfTerm('PrimaryCare', 'https://schema.org/PrimaryCare', [])

class Oncologic(MedicalBusiness):
    term = RdfTerm('Oncologic', 'https://schema.org/Oncologic', [])

class Pediatric(MedicalBusiness):
    term = RdfTerm('Pediatric', 'https://schema.org/Pediatric', [])

class Optometric(MedicalBusiness):
    term = RdfTerm('Optometric', 'https://schema.org/Optometric', [])

class Gynecologic(MedicalBusiness):
    term = RdfTerm('Gynecologic', 'https://schema.org/Gynecologic', [])

class Geriatric(MedicalBusiness):
    term = RdfTerm('Geriatric', 'https://schema.org/Geriatric', [])

class Dermatology(MedicalBusiness):
    term = RdfTerm('Dermatology', 'https://schema.org/Dermatology', [])

class Otolaryngologic(MedicalBusiness):
    term = RdfTerm('Otolaryngologic', 'https://schema.org/Otolaryngologic', [])

class Emergency(MedicalBusiness):
    term = RdfTerm('Emergency', 'https://schema.org/Emergency', [])

class PublicHealth(MedicalBusiness):
    term = RdfTerm('PublicHealth', 'https://schema.org/PublicHealth', [])

class CommunityHealth(MedicalBusiness):
    term = RdfTerm('CommunityHealth', 'https://schema.org/CommunityHealth', [])

class Nursing(MedicalBusiness):
    term = RdfTerm('Nursing', 'https://schema.org/Nursing', [])

class Podiatric(MedicalBusiness):
    term = RdfTerm('Podiatric', 'https://schema.org/Podiatric', [])

class PlasticSurgery(MedicalBusiness):
    term = RdfTerm('PlasticSurgery', 'https://schema.org/PlasticSurgery', [])

class DietNutrition(MedicalBusiness):
    term = RdfTerm('DietNutrition', 'https://schema.org/DietNutrition', [])

class Obstetric(MedicalBusiness):
    term = RdfTerm('Obstetric', 'https://schema.org/Obstetric', [])

class Psychiatric(MedicalBusiness):
    term = RdfTerm('Psychiatric', 'https://schema.org/Psychiatric', [])

class Midwifery(MedicalBusiness):
    term = RdfTerm('Midwifery', 'https://schema.org/Midwifery', [])

class Optician(MedicalBusiness):
    term = RdfTerm('Optician', 'https://schema.org/Optician', [])

class PostOffice(GovernmentOffice):
    term = RdfTerm('PostOffice', 'https://schema.org/PostOffice', [])

class Hostel(LodgingBusiness):
    term = RdfTerm('Hostel', 'https://schema.org/Hostel', [])

class Resort(LodgingBusiness):
    term = RdfTerm('Resort', 'https://schema.org/Resort', [])

class VacationRental(LodgingBusiness):
    term = RdfTerm('VacationRental', 'https://schema.org/VacationRental', [])

class Campground(CivicStructure, LodgingBusiness):
    term = RdfTerm('Campground', 'https://schema.org/Campground', [])

class Motel(LodgingBusiness):
    term = RdfTerm('Motel', 'https://schema.org/Motel', [])

class BedAndBreakfast(LodgingBusiness):
    term = RdfTerm('BedAndBreakfast', 'https://schema.org/BedAndBreakfast', [])

class Hotel(LodgingBusiness):
    term = RdfTerm('Hotel', 'https://schema.org/Hotel', [])

class Hospital(CivicStructure, MedicalOrganization, EmergencyService):
    term = RdfTerm('Hospital', 'https://schema.org/Hospital', [])

class FireStation(CivicStructure, EmergencyService):
    term = RdfTerm('FireStation', 'https://schema.org/FireStation', [])

class PoliceStation(CivicStructure, EmergencyService):
    term = RdfTerm('PoliceStation', 'https://schema.org/PoliceStation', [])

class TattooParlor(HealthAndBeautyBusiness):
    term = RdfTerm('TattooParlor', 'https://schema.org/TattooParlor', [])

class BeautySalon(HealthAndBeautyBusiness):
    term = RdfTerm('BeautySalon', 'https://schema.org/BeautySalon', [])

class DaySpa(HealthAndBeautyBusiness):
    term = RdfTerm('DaySpa', 'https://schema.org/DaySpa', [])

class NailSalon(HealthAndBeautyBusiness):
    term = RdfTerm('NailSalon', 'https://schema.org/NailSalon', [])

class HairSalon(HealthAndBeautyBusiness):
    term = RdfTerm('HairSalon', 'https://schema.org/HairSalon', [])

class HousePainter(HomeAndConstructionBusiness):
    term = RdfTerm('HousePainter', 'https://schema.org/HousePainter', [])

class HVACBusiness(HomeAndConstructionBusiness):
    term = RdfTerm('HVACBusiness', 'https://schema.org/HVACBusiness', [])

class GeneralContractor(HomeAndConstructionBusiness):
    term = RdfTerm('GeneralContractor', 'https://schema.org/GeneralContractor', [])

class Electrician(HomeAndConstructionBusiness):
    term = RdfTerm('Electrician', 'https://schema.org/Electrician', [])

class Plumber(HomeAndConstructionBusiness):
    term = RdfTerm('Plumber', 'https://schema.org/Plumber', [])

class RoofingContractor(HomeAndConstructionBusiness):
    term = RdfTerm('RoofingContractor', 'https://schema.org/RoofingContractor', [])

class MovingCompany(HomeAndConstructionBusiness):
    term = RdfTerm('MovingCompany', 'https://schema.org/MovingCompany', [])

class Locksmith(HomeAndConstructionBusiness):
    term = RdfTerm('Locksmith', 'https://schema.org/Locksmith', [])

class Brewery(FoodEstablishment):
    term = RdfTerm('Brewery', 'https://schema.org/Brewery', [])

class Distillery(FoodEstablishment):
    term = RdfTerm('Distillery', 'https://schema.org/Distillery', [])

class FastFoodRestaurant(FoodEstablishment):
    term = RdfTerm('FastFoodRestaurant', 'https://schema.org/FastFoodRestaurant', [])

class Restaurant(FoodEstablishment):
    term = RdfTerm('Restaurant', 'https://schema.org/Restaurant', [])

class Bakery(FoodEstablishment):
    term = RdfTerm('Bakery', 'https://schema.org/Bakery', [])

class BarOrPub(FoodEstablishment):
    term = RdfTerm('BarOrPub', 'https://schema.org/BarOrPub', [])

class Winery(FoodEstablishment):
    term = RdfTerm('Winery', 'https://schema.org/Winery', [])

class IceCreamShop(FoodEstablishment):
    term = RdfTerm('IceCreamShop', 'https://schema.org/IceCreamShop', [])

class CafeOrCoffeeShop(FoodEstablishment):
    term = RdfTerm('CafeOrCoffeeShop', 'https://schema.org/CafeOrCoffeeShop', [])

class Notary(LegalService):
    term = RdfTerm('Notary', 'https://schema.org/Notary', [])

class Attorney(LegalService):
    term = RdfTerm('Attorney', 'https://schema.org/Attorney', [])

class InsuranceAgency(FinancialService):
    term = RdfTerm('InsuranceAgency', 'https://schema.org/InsuranceAgency', [])

class BankOrCreditUnion(FinancialService):
    term = RdfTerm('BankOrCreditUnion', 'https://schema.org/BankOrCreditUnion', [])

class AutomatedTeller(FinancialService):
    term = RdfTerm('AutomatedTeller', 'https://schema.org/AutomatedTeller', [])

class AccountingService(FinancialService):
    term = RdfTerm('AccountingService', 'https://schema.org/AccountingService', [])

class HealthClub(SportsActivityLocation, HealthAndBeautyBusiness):
    term = RdfTerm('HealthClub', 'https://schema.org/HealthClub', [])

class StadiumOrArena(SportsActivityLocation, CivicStructure):
    term = RdfTerm('StadiumOrArena', 'https://schema.org/StadiumOrArena', [])

class ExerciseGym(SportsActivityLocation):
    term = RdfTerm('ExerciseGym', 'https://schema.org/ExerciseGym', [])

class SportsClub(SportsActivityLocation):
    term = RdfTerm('SportsClub', 'https://schema.org/SportsClub', [])

class GolfCourse(SportsActivityLocation):
    term = RdfTerm('GolfCourse', 'https://schema.org/GolfCourse', [])

class BowlingAlley(SportsActivityLocation):
    term = RdfTerm('BowlingAlley', 'https://schema.org/BowlingAlley', [])

class TennisComplex(SportsActivityLocation):
    term = RdfTerm('TennisComplex', 'https://schema.org/TennisComplex', [])

class PublicSwimmingPool(SportsActivityLocation):
    term = RdfTerm('PublicSwimmingPool', 'https://schema.org/PublicSwimmingPool', [])

class FurnitureStore(Store):
    term = RdfTerm('FurnitureStore', 'https://schema.org/FurnitureStore', [])

class MensClothingStore(Store):
    term = RdfTerm('MensClothingStore', 'https://schema.org/MensClothingStore', [])

class LiquorStore(Store):
    term = RdfTerm('LiquorStore', 'https://schema.org/LiquorStore', [])

class BikeStore(Store):
    term = RdfTerm('BikeStore', 'https://schema.org/BikeStore', [])

class ToyStore(Store):
    term = RdfTerm('ToyStore', 'https://schema.org/ToyStore', [])

class ClothingStore(Store):
    term = RdfTerm('ClothingStore', 'https://schema.org/ClothingStore', [])

class MusicStore(Store):
    term = RdfTerm('MusicStore', 'https://schema.org/MusicStore', [])

class JewelryStore(Store):
    term = RdfTerm('JewelryStore', 'https://schema.org/JewelryStore', [])

class MovieRentalStore(Store):
    term = RdfTerm('MovieRentalStore', 'https://schema.org/MovieRentalStore', [])

class HardwareStore(Store):
    term = RdfTerm('HardwareStore', 'https://schema.org/HardwareStore', [])

class ElectronicsStore(Store):
    term = RdfTerm('ElectronicsStore', 'https://schema.org/ElectronicsStore', [])

class PetStore(Store):
    term = RdfTerm('PetStore', 'https://schema.org/PetStore', [])

class ConvenienceStore(Store):
    term = RdfTerm('ConvenienceStore', 'https://schema.org/ConvenienceStore', [])

class SportingGoodsStore(Store):
    term = RdfTerm('SportingGoodsStore', 'https://schema.org/SportingGoodsStore', [])

class PawnShop(Store):
    term = RdfTerm('PawnShop', 'https://schema.org/PawnShop', [])

class TireShop(Store):
    term = RdfTerm('TireShop', 'https://schema.org/TireShop', [])

class Florist(Store):
    term = RdfTerm('Florist', 'https://schema.org/Florist', [])

class ComputerStore(Store):
    term = RdfTerm('ComputerStore', 'https://schema.org/ComputerStore', [])

class OfficeEquipmentStore(Store):
    term = RdfTerm('OfficeEquipmentStore', 'https://schema.org/OfficeEquipmentStore', [])

class OutletStore(Store):
    term = RdfTerm('OutletStore', 'https://schema.org/OutletStore', [])

class HobbyShop(Store):
    term = RdfTerm('HobbyShop', 'https://schema.org/HobbyShop', [])

class HomeGoodsStore(Store):
    term = RdfTerm('HomeGoodsStore', 'https://schema.org/HomeGoodsStore', [])

class ShoeStore(Store):
    term = RdfTerm('ShoeStore', 'https://schema.org/ShoeStore', [])

class GardenStore(Store):
    term = RdfTerm('GardenStore', 'https://schema.org/GardenStore', [])

class BookStore(Store):
    term = RdfTerm('BookStore', 'https://schema.org/BookStore', [])

class MobilePhoneStore(Store):
    term = RdfTerm('MobilePhoneStore', 'https://schema.org/MobilePhoneStore', [])

class GroceryStore(Store):
    term = RdfTerm('GroceryStore', 'https://schema.org/GroceryStore', [])

class WholesaleStore(Store):
    term = RdfTerm('WholesaleStore', 'https://schema.org/WholesaleStore', [])

class DepartmentStore(Store):
    term = RdfTerm('DepartmentStore', 'https://schema.org/DepartmentStore', [])

class AutoBodyShop(AutomotiveBusiness):
    term = RdfTerm('AutoBodyShop', 'https://schema.org/AutoBodyShop', [])

class AutoDealer(AutomotiveBusiness):
    term = RdfTerm('AutoDealer', 'https://schema.org/AutoDealer', [])

class AutoPartsStore(AutomotiveBusiness, Store):
    term = RdfTerm('AutoPartsStore', 'https://schema.org/AutoPartsStore', [])

class GasStation(AutomotiveBusiness):
    term = RdfTerm('GasStation', 'https://schema.org/GasStation', [])

class AutoRental(AutomotiveBusiness):
    term = RdfTerm('AutoRental', 'https://schema.org/AutoRental', [])

class AutoRepair(AutomotiveBusiness):
    term = RdfTerm('AutoRepair', 'https://schema.org/AutoRepair', [])

class AutoWash(AutomotiveBusiness):
    term = RdfTerm('AutoWash', 'https://schema.org/AutoWash', [])

class MotorcycleRepair(AutomotiveBusiness):
    term = RdfTerm('MotorcycleRepair', 'https://schema.org/MotorcycleRepair', [])

class MotorcycleDealer(AutomotiveBusiness):
    term = RdfTerm('MotorcycleDealer', 'https://schema.org/MotorcycleDealer', [])

class ArtGallery(EntertainmentBusiness):
    term = RdfTerm('ArtGallery', 'https://schema.org/ArtGallery', [])

class Casino(EntertainmentBusiness):
    term = RdfTerm('Casino', 'https://schema.org/Casino', [])

class NightClub(EntertainmentBusiness):
    term = RdfTerm('NightClub', 'https://schema.org/NightClub', [])

class AdultEntertainment(EntertainmentBusiness):
    term = RdfTerm('AdultEntertainment', 'https://schema.org/AdultEntertainment', [])

class AmusementPark(EntertainmentBusiness):
    term = RdfTerm('AmusementPark', 'https://schema.org/AmusementPark', [])

class ComedyClub(EntertainmentBusiness):
    term = RdfTerm('ComedyClub', 'https://schema.org/ComedyClub', [])

class MovieTheater(CivicStructure, EntertainmentBusiness):
    term = RdfTerm('MovieTheater', 'https://schema.org/MovieTheater', [])

class CatholicChurch(Church):
    term = RdfTerm('CatholicChurch', 'https://schema.org/CatholicChurch', [])

class LiveBlogPosting(BlogPosting):
    term = RdfTerm('LiveBlogPosting', 'https://schema.org/LiveBlogPosting', [])

class VideoGallery(MediaGallery):
    term = RdfTerm('VideoGallery', 'https://schema.org/VideoGallery', [])

class ImageGallery(MediaGallery):
    term = RdfTerm('ImageGallery', 'https://schema.org/ImageGallery', [])

class ComicSeries(Periodical):
    term = RdfTerm('ComicSeries', 'https://schema.org/ComicSeries', [])

class Newspaper(Periodical):
    term = RdfTerm('Newspaper', 'https://schema.org/Newspaper', [])

class Patient(MedicalAudience, Person):
    term = RdfTerm('Patient', 'https://schema.org/Patient', [])

class MortgageLoan(LoanOrCredit):
    term = RdfTerm('MortgageLoan', 'https://schema.org/MortgageLoan', [])

class CreditCard(PaymentCard, LoanOrCredit):
    term = RdfTerm('CreditCard', 'https://schema.org/CreditCard', [])

class DepositAccount(BankAccount, InvestmentOrDeposit):
    term = RdfTerm('DepositAccount', 'https://schema.org/DepositAccount', [])

class InvestmentFund(InvestmentOrDeposit):
    term = RdfTerm('InvestmentFund', 'https://schema.org/InvestmentFund', [])

class BrokerageAccount(InvestmentOrDeposit):
    term = RdfTerm('BrokerageAccount', 'https://schema.org/BrokerageAccount', [])

class AppendAction(InsertAction):
    term = RdfTerm('AppendAction', 'https://schema.org/AppendAction', [])

class PrependAction(InsertAction):
    term = RdfTerm('PrependAction', 'https://schema.org/PrependAction', [])

class ConfirmAction(InformAction):
    term = RdfTerm('ConfirmAction', 'https://schema.org/ConfirmAction', [])

class RsvpAction(InformAction):
    term = RdfTerm('RsvpAction', 'https://schema.org/RsvpAction', [])

class PalliativeProcedure(MedicalProcedure, MedicalTherapy):
    term = RdfTerm('PalliativeProcedure', 'https://schema.org/PalliativeProcedure', [])

class PhysicalTherapy(MedicalTherapy):
    term = RdfTerm('PhysicalTherapy', 'https://schema.org/PhysicalTherapy', [])

class OccupationalTherapy(MedicalTherapy):
    term = RdfTerm('OccupationalTherapy', 'https://schema.org/OccupationalTherapy', [])

class RespiratoryTherapy(MedicalTherapy):
    term = RdfTerm('RespiratoryTherapy', 'https://schema.org/RespiratoryTherapy', [])

class RadiationTherapy(MedicalTherapy):
    term = RdfTerm('RadiationTherapy', 'https://schema.org/RadiationTherapy', [])

class VitalSign(MedicalSign):
    term = RdfTerm('VitalSign', 'https://schema.org/VitalSign', [])

class CovidTestingFacility(MedicalClinic):
    term = RdfTerm('CovidTestingFacility', 'https://schema.org/CovidTestingFacility', [])

class PhysiciansOffice(Physician):
    term = RdfTerm('PhysiciansOffice', 'https://schema.org/PhysiciansOffice', [])

class IndividualPhysician(Physician):
    term = RdfTerm('IndividualPhysician', 'https://schema.org/IndividualPhysician', [])

class SkiResort(SportsActivityLocation, Resort):
    term = RdfTerm('SkiResort', 'https://schema.org/SkiResort', [])

@dataclass(frozen=True)
class hasPart(RdfProperty):
    term = RdfTerm('hasPart', 'https://schema.org/hasPart', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class backstory(RdfProperty):
    term = RdfTerm('backstory', 'https://schema.org/backstory', [])
    object: schemaorg.CreativeWork | Text

@dataclass(frozen=True)
class numberOfLoanPayments(RdfProperty):
    term = RdfTerm('numberOfLoanPayments', 'https://schema.org/numberOfLoanPayments', [])
    object: Number

@dataclass(frozen=True)
class priceValidUntil(RdfProperty):
    term = RdfTerm('priceValidUntil', 'https://schema.org/priceValidUntil', [])
    object: Date

@dataclass(frozen=True)
class title(RdfProperty):
    term = RdfTerm('title', 'https://schema.org/title', [])
    object: Text

@dataclass(frozen=True)
class numberOfEmployees(RdfProperty):
    term = RdfTerm('numberOfEmployees', 'https://schema.org/numberOfEmployees', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class securityScreening(RdfProperty):
    term = RdfTerm('securityScreening', 'https://schema.org/securityScreening', [])
    object: Text

@dataclass(frozen=True)
class carrier(RdfProperty):
    term = RdfTerm('carrier', 'https://schema.org/carrier', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class healthCondition(RdfProperty):
    term = RdfTerm('healthCondition', 'https://schema.org/healthCondition', [])
    object: schemaorg.MedicalCondition

@dataclass(frozen=True)
class underName(RdfProperty):
    term = RdfTerm('underName', 'https://schema.org/underName', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class actionableFeedbackPolicy(RdfProperty):
    term = RdfTerm('actionableFeedbackPolicy', 'https://schema.org/actionableFeedbackPolicy', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class mapType(RdfProperty):
    term = RdfTerm('mapType', 'https://schema.org/mapType', [])
    object: schemaorg.MapCategoryType

@dataclass(frozen=True)
class educationalProgramMode(RdfProperty):
    term = RdfTerm('educationalProgramMode', 'https://schema.org/educationalProgramMode', [])
    object: Text | URL

@dataclass(frozen=True)
class benefits(RdfProperty):
    term = RdfTerm('benefits', 'https://schema.org/benefits', [])
    object: Text

@dataclass(frozen=True)
class legislationDate(RdfProperty):
    term = RdfTerm('legislationDate', 'https://schema.org/legislationDate', [])
    object: Date

@dataclass(frozen=True)
class geo(RdfProperty):
    term = RdfTerm('geo', 'https://schema.org/geo', [])
    object: schemaorg.GeoCoordinates | schemaorg.GeoShape

@dataclass(frozen=True)
class alternateName(RdfProperty):
    term = RdfTerm('alternateName', 'https://schema.org/alternateName', [])
    object: Text

@dataclass(frozen=True)
class risks(RdfProperty):
    term = RdfTerm('risks', 'https://schema.org/risks', [])
    object: Text

@dataclass(frozen=True)
class legislationChanges(RdfProperty):
    term = RdfTerm('legislationChanges', 'https://schema.org/legislationChanges', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class bed(RdfProperty):
    term = RdfTerm('bed', 'https://schema.org/bed', [])
    object: schemaorg.BedDetails | schemaorg.BedType | Text

@dataclass(frozen=True)
class diversityPolicy(RdfProperty):
    term = RdfTerm('diversityPolicy', 'https://schema.org/diversityPolicy', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class totalHistoricalEnrollment(RdfProperty):
    term = RdfTerm('totalHistoricalEnrollment', 'https://schema.org/totalHistoricalEnrollment', [])
    object: Integer

@dataclass(frozen=True)
class dataFeedElement(RdfProperty):
    term = RdfTerm('dataFeedElement', 'https://schema.org/dataFeedElement', [])
    object: schemaorg.DataFeedItem | schemaorg.Thing | Text

@dataclass(frozen=True)
class eventAttendanceMode(RdfProperty):
    term = RdfTerm('eventAttendanceMode', 'https://schema.org/eventAttendanceMode', [])
    object: schemaorg.EventAttendanceModeEnumeration

@dataclass(frozen=True)
class exifData(RdfProperty):
    term = RdfTerm('exifData', 'https://schema.org/exifData', [])
    object: schemaorg.PropertyValue | Text

@dataclass(frozen=True)
class broadcastSignalModulation(RdfProperty):
    term = RdfTerm('broadcastSignalModulation', 'https://schema.org/broadcastSignalModulation', [])
    object: schemaorg.QualitativeValue | Text

@dataclass(frozen=True)
class broadcastChannelId(RdfProperty):
    term = RdfTerm('broadcastChannelId', 'https://schema.org/broadcastChannelId', [])
    object: Text

@dataclass(frozen=True)
class videoFrameSize(RdfProperty):
    term = RdfTerm('videoFrameSize', 'https://schema.org/videoFrameSize', [])
    object: Text

@dataclass(frozen=True)
class paymentAccepted(RdfProperty):
    term = RdfTerm('paymentAccepted', 'https://schema.org/paymentAccepted', [])
    object: Text

@dataclass(frozen=True)
class saturatedFatContent(RdfProperty):
    term = RdfTerm('saturatedFatContent', 'https://schema.org/saturatedFatContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class procedure(RdfProperty):
    term = RdfTerm('procedure', 'https://schema.org/procedure', [])
    object: Text

@dataclass(frozen=True)
class fuelEfficiency(RdfProperty):
    term = RdfTerm('fuelEfficiency', 'https://schema.org/fuelEfficiency', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class endTime(RdfProperty):
    term = RdfTerm('endTime', 'https://schema.org/endTime', [])
    object: Time | DateTime

@dataclass(frozen=True)
class _yield(RdfProperty):
    term = RdfTerm('yield', 'https://schema.org/yield', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class addressRegion(RdfProperty):
    term = RdfTerm('addressRegion', 'https://schema.org/addressRegion', [])
    object: Text

@dataclass(frozen=True)
class billingIncrement(RdfProperty):
    term = RdfTerm('billingIncrement', 'https://schema.org/billingIncrement', [])
    object: Number

@dataclass(frozen=True)
class opens(RdfProperty):
    term = RdfTerm('opens', 'https://schema.org/opens', [])
    object: Time

@dataclass(frozen=True)
class trialDesign(RdfProperty):
    term = RdfTerm('trialDesign', 'https://schema.org/trialDesign', [])
    object: schemaorg.MedicalTrialDesign

@dataclass(frozen=True)
class verificationFactCheckingPolicy(RdfProperty):
    term = RdfTerm('verificationFactCheckingPolicy', 'https://schema.org/verificationFactCheckingPolicy', [])
    object: URL | schemaorg.CreativeWork

@dataclass(frozen=True)
class significantLinks(RdfProperty):
    term = RdfTerm('significantLinks', 'https://schema.org/significantLinks', [])
    object: URL

@dataclass(frozen=True)
class reservedTicket(RdfProperty):
    term = RdfTerm('reservedTicket', 'https://schema.org/reservedTicket', [])
    object: schemaorg.Ticket

@dataclass(frozen=True)
class potentialAction(RdfProperty):
    term = RdfTerm('potentialAction', 'https://schema.org/potentialAction', [])
    object: schemaorg.Action

@dataclass(frozen=True)
class episodes(RdfProperty):
    term = RdfTerm('episodes', 'https://schema.org/episodes', [])
    object: schemaorg.Episode

@dataclass(frozen=True)
class legislationConsolidates(RdfProperty):
    term = RdfTerm('legislationConsolidates', 'https://schema.org/legislationConsolidates', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class scheduleTimezone(RdfProperty):
    term = RdfTerm('scheduleTimezone', 'https://schema.org/scheduleTimezone', [])
    object: Text

@dataclass(frozen=True)
class mainContentOfPage(RdfProperty):
    term = RdfTerm('mainContentOfPage', 'https://schema.org/mainContentOfPage', [])
    object: schemaorg.WebPageElement

@dataclass(frozen=True)
class produces(RdfProperty):
    term = RdfTerm('produces', 'https://schema.org/produces', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class appearance(RdfProperty):
    term = RdfTerm('appearance', 'https://schema.org/appearance', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class branch(RdfProperty):
    term = RdfTerm('branch', 'https://schema.org/branch', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class gameItem(RdfProperty):
    term = RdfTerm('gameItem', 'https://schema.org/gameItem', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class menuAddOn(RdfProperty):
    term = RdfTerm('menuAddOn', 'https://schema.org/menuAddOn', [])
    object: schemaorg.MenuItem | schemaorg.MenuSection

@dataclass(frozen=True)
class servesCuisine(RdfProperty):
    term = RdfTerm('servesCuisine', 'https://schema.org/servesCuisine', [])
    object: Text

@dataclass(frozen=True)
class alumniOf(RdfProperty):
    term = RdfTerm('alumniOf', 'https://schema.org/alumniOf', [])
    object: schemaorg.EducationalOrganization | schemaorg.Organization

@dataclass(frozen=True)
class dropoffTime(RdfProperty):
    term = RdfTerm('dropoffTime', 'https://schema.org/dropoffTime', [])
    object: DateTime

@dataclass(frozen=True)
class bestRating(RdfProperty):
    term = RdfTerm('bestRating', 'https://schema.org/bestRating', [])
    object: Number | Text

@dataclass(frozen=True)
class instrument(RdfProperty):
    term = RdfTerm('instrument', 'https://schema.org/instrument', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class creativeWorkStatus(RdfProperty):
    term = RdfTerm('creativeWorkStatus', 'https://schema.org/creativeWorkStatus', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class missionCoveragePrioritiesPolicy(RdfProperty):
    term = RdfTerm('missionCoveragePrioritiesPolicy', 'https://schema.org/missionCoveragePrioritiesPolicy', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class biologicalRole(RdfProperty):
    term = RdfTerm('biologicalRole', 'https://schema.org/biologicalRole', [])
    object: schemaorg.DefinedTerm

@dataclass(frozen=True)
class isAccessoryOrSparePartFor(RdfProperty):
    term = RdfTerm('isAccessoryOrSparePartFor', 'https://schema.org/isAccessoryOrSparePartFor', [])
    object: schemaorg.Product

@dataclass(frozen=True)
class iswcCode(RdfProperty):
    term = RdfTerm('iswcCode', 'https://schema.org/iswcCode', [])
    object: Text

@dataclass(frozen=True)
class childMinAge(RdfProperty):
    term = RdfTerm('childMinAge', 'https://schema.org/childMinAge', [])
    object: Number

@dataclass(frozen=True)
class aggregateRating(RdfProperty):
    term = RdfTerm('aggregateRating', 'https://schema.org/aggregateRating', [])
    object: schemaorg.AggregateRating

@dataclass(frozen=True)
class engineType(RdfProperty):
    term = RdfTerm('engineType', 'https://schema.org/engineType', [])
    object: schemaorg.QualitativeValue | Text | URL

@dataclass(frozen=True)
class performerIn(RdfProperty):
    term = RdfTerm('performerIn', 'https://schema.org/performerIn', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class eventSchedule(RdfProperty):
    term = RdfTerm('eventSchedule', 'https://schema.org/eventSchedule', [])
    object: schemaorg.Schedule

@dataclass(frozen=True)
class recipeInstructions(RdfProperty):
    term = RdfTerm('recipeInstructions', 'https://schema.org/recipeInstructions', [])
    object: schemaorg.ItemList | schemaorg.CreativeWork | Text

@dataclass(frozen=True)
class gamePlatform(RdfProperty):
    term = RdfTerm('gamePlatform', 'https://schema.org/gamePlatform', [])
    object: schemaorg.Thing | Text | URL

@dataclass(frozen=True)
class ratingCount(RdfProperty):
    term = RdfTerm('ratingCount', 'https://schema.org/ratingCount', [])
    object: Integer

@dataclass(frozen=True)
class isProprietary(RdfProperty):
    term = RdfTerm('isProprietary', 'https://schema.org/isProprietary', [])
    object: Boolean

@dataclass(frozen=True)
class free(RdfProperty):
    term = RdfTerm('free', 'https://schema.org/free', [])
    object: Boolean

@dataclass(frozen=True)
class dateIssued(RdfProperty):
    term = RdfTerm('dateIssued', 'https://schema.org/dateIssued', [])
    object: Date | DateTime

@dataclass(frozen=True)
class productReturnDays(RdfProperty):
    term = RdfTerm('productReturnDays', 'https://schema.org/productReturnDays', [])
    object: Integer

@dataclass(frozen=True)
class representativeOfPage(RdfProperty):
    term = RdfTerm('representativeOfPage', 'https://schema.org/representativeOfPage', [])
    object: Boolean

@dataclass(frozen=True)
class restockingFee(RdfProperty):
    term = RdfTerm('restockingFee', 'https://schema.org/restockingFee', [])
    object: schemaorg.MonetaryAmount | Number

@dataclass(frozen=True)
class value(RdfProperty):
    term = RdfTerm('value', 'https://schema.org/value', [])
    object: Number | Boolean | Text | schemaorg.StructuredValue

@dataclass(frozen=True)
class applicationSuite(RdfProperty):
    term = RdfTerm('applicationSuite', 'https://schema.org/applicationSuite', [])
    object: Text

@dataclass(frozen=True)
class archivedAt(RdfProperty):
    term = RdfTerm('archivedAt', 'https://schema.org/archivedAt', [])
    object: URL | schemaorg.WebPage

@dataclass(frozen=True)
class breadcrumb(RdfProperty):
    term = RdfTerm('breadcrumb', 'https://schema.org/breadcrumb', [])
    object: schemaorg.BreadcrumbList | Text

@dataclass(frozen=True)
class isSimilarTo(RdfProperty):
    term = RdfTerm('isSimilarTo', 'https://schema.org/isSimilarTo', [])
    object: schemaorg.Product | schemaorg.Service

@dataclass(frozen=True)
class validThrough(RdfProperty):
    term = RdfTerm('validThrough', 'https://schema.org/validThrough', [])
    object: Date | DateTime

@dataclass(frozen=True)
class members(RdfProperty):
    term = RdfTerm('members', 'https://schema.org/members', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class primaryPrevention(RdfProperty):
    term = RdfTerm('primaryPrevention', 'https://schema.org/primaryPrevention', [])
    object: schemaorg.MedicalTherapy

@dataclass(frozen=True)
class pregnancyWarning(RdfProperty):
    term = RdfTerm('pregnancyWarning', 'https://schema.org/pregnancyWarning', [])
    object: Text

@dataclass(frozen=True)
class usageInfo(RdfProperty):
    term = RdfTerm('usageInfo', 'https://schema.org/usageInfo', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class payload(RdfProperty):
    term = RdfTerm('payload', 'https://schema.org/payload', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class modelDate(RdfProperty):
    term = RdfTerm('modelDate', 'https://schema.org/modelDate', [])
    object: Date

@dataclass(frozen=True)
class addOn(RdfProperty):
    term = RdfTerm('addOn', 'https://schema.org/addOn', [])
    object: schemaorg.Offer

@dataclass(frozen=True)
class funder(RdfProperty):
    term = RdfTerm('funder', 'https://schema.org/funder', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class actor(RdfProperty):
    term = RdfTerm('actor', 'https://schema.org/actor', [])
    object: schemaorg.Person | schemaorg.PerformingGroup

@dataclass(frozen=True)
class guideline(RdfProperty):
    term = RdfTerm('guideline', 'https://schema.org/guideline', [])
    object: schemaorg.MedicalGuideline

@dataclass(frozen=True)
class translationOfWork(RdfProperty):
    term = RdfTerm('translationOfWork', 'https://schema.org/translationOfWork', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class query(RdfProperty):
    term = RdfTerm('query', 'https://schema.org/query', [])
    object: Text

@dataclass(frozen=True)
class foundingDate(RdfProperty):
    term = RdfTerm('foundingDate', 'https://schema.org/foundingDate', [])
    object: Date

@dataclass(frozen=True)
class deathDate(RdfProperty):
    term = RdfTerm('deathDate', 'https://schema.org/deathDate', [])
    object: Date

@dataclass(frozen=True)
class bioChemSimilarity(RdfProperty):
    term = RdfTerm('bioChemSimilarity', 'https://schema.org/bioChemSimilarity', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class sameAs(RdfProperty):
    term = RdfTerm('sameAs', 'https://schema.org/sameAs', [])
    object: URL

@dataclass(frozen=True)
class toRecipient(RdfProperty):
    term = RdfTerm('toRecipient', 'https://schema.org/toRecipient', [])
    object: schemaorg.Person | schemaorg.Audience | schemaorg.Organization | schemaorg.ContactPoint

@dataclass(frozen=True)
class issueNumber(RdfProperty):
    term = RdfTerm('issueNumber', 'https://schema.org/issueNumber', [])
    object: Integer | Text

@dataclass(frozen=True)
class polygon(RdfProperty):
    term = RdfTerm('polygon', 'https://schema.org/polygon', [])
    object: Text

@dataclass(frozen=True)
class isAvailableGenerically(RdfProperty):
    term = RdfTerm('isAvailableGenerically', 'https://schema.org/isAvailableGenerically', [])
    object: Boolean

@dataclass(frozen=True)
class hasAdultConsideration(RdfProperty):
    term = RdfTerm('hasAdultConsideration', 'https://schema.org/hasAdultConsideration', [])
    object: schemaorg.AdultOrientedEnumeration

@dataclass(frozen=True)
class address(RdfProperty):
    term = RdfTerm('address', 'https://schema.org/address', [])
    object: schemaorg.PostalAddress | Text

@dataclass(frozen=True)
class numberOfBeds(RdfProperty):
    term = RdfTerm('numberOfBeds', 'https://schema.org/numberOfBeds', [])
    object: Number

@dataclass(frozen=True)
class sizeGroup(RdfProperty):
    term = RdfTerm('sizeGroup', 'https://schema.org/sizeGroup', [])
    object: schemaorg.SizeGroupEnumeration | Text

@dataclass(frozen=True)
class variableMeasured(RdfProperty):
    term = RdfTerm('variableMeasured', 'https://schema.org/variableMeasured', [])
    object: schemaorg.Property | schemaorg.PropertyValue | schemaorg.StatisticalVariable | Text

@dataclass(frozen=True)
class about(RdfProperty):
    term = RdfTerm('about', 'https://schema.org/about', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class procedureType(RdfProperty):
    term = RdfTerm('procedureType', 'https://schema.org/procedureType', [])
    object: schemaorg.MedicalProcedureType

@dataclass(frozen=True)
class beforeMedia(RdfProperty):
    term = RdfTerm('beforeMedia', 'https://schema.org/beforeMedia', [])
    object: URL | schemaorg.MediaObject

@dataclass(frozen=True)
class legislationType(RdfProperty):
    term = RdfTerm('legislationType', 'https://schema.org/legislationType', [])
    object: schemaorg.CategoryCode | Text

@dataclass(frozen=True)
class cvdNumC19HospPats(RdfProperty):
    term = RdfTerm('cvdNumC19HospPats', 'https://schema.org/cvdNumC19HospPats', [])
    object: Number

@dataclass(frozen=True)
class serialNumber(RdfProperty):
    term = RdfTerm('serialNumber', 'https://schema.org/serialNumber', [])
    object: Text

@dataclass(frozen=True)
class statType(RdfProperty):
    term = RdfTerm('statType', 'https://schema.org/statType', [])
    object: URL | schemaorg.Property | Text

@dataclass(frozen=True)
class numberOfCredits(RdfProperty):
    term = RdfTerm('numberOfCredits', 'https://schema.org/numberOfCredits', [])
    object: Integer | schemaorg.StructuredValue

@dataclass(frozen=True)
class numberOfAccommodationUnits(RdfProperty):
    term = RdfTerm('numberOfAccommodationUnits', 'https://schema.org/numberOfAccommodationUnits', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class openingHours(RdfProperty):
    term = RdfTerm('openingHours', 'https://schema.org/openingHours', [])
    object: Text

@dataclass(frozen=True)
class dateline(RdfProperty):
    term = RdfTerm('dateline', 'https://schema.org/dateline', [])
    object: Text

@dataclass(frozen=True)
class infectiousAgentClass(RdfProperty):
    term = RdfTerm('infectiousAgentClass', 'https://schema.org/infectiousAgentClass', [])
    object: schemaorg.InfectiousAgentClass

@dataclass(frozen=True)
class insertion(RdfProperty):
    term = RdfTerm('insertion', 'https://schema.org/insertion', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class tributary(RdfProperty):
    term = RdfTerm('tributary', 'https://schema.org/tributary', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class rxcui(RdfProperty):
    term = RdfTerm('rxcui', 'https://schema.org/rxcui', [])
    object: Text

@dataclass(frozen=True)
class temporal(RdfProperty):
    term = RdfTerm('temporal', 'https://schema.org/temporal', [])
    object: DateTime | Text

@dataclass(frozen=True)
class homeLocation(RdfProperty):
    term = RdfTerm('homeLocation', 'https://schema.org/homeLocation', [])
    object: schemaorg.Place | schemaorg.ContactPoint

@dataclass(frozen=True)
class target(RdfProperty):
    term = RdfTerm('target', 'https://schema.org/target', [])
    object: URL | schemaorg.EntryPoint

@dataclass(frozen=True)
class performTime(RdfProperty):
    term = RdfTerm('performTime', 'https://schema.org/performTime', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class secondaryPrevention(RdfProperty):
    term = RdfTerm('secondaryPrevention', 'https://schema.org/secondaryPrevention', [])
    object: schemaorg.MedicalTherapy

@dataclass(frozen=True)
class diagnosis(RdfProperty):
    term = RdfTerm('diagnosis', 'https://schema.org/diagnosis', [])
    object: schemaorg.MedicalCondition

@dataclass(frozen=True)
class vehicleInteriorType(RdfProperty):
    term = RdfTerm('vehicleInteriorType', 'https://schema.org/vehicleInteriorType', [])
    object: Text

@dataclass(frozen=True)
class coach(RdfProperty):
    term = RdfTerm('coach', 'https://schema.org/coach', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class isFamilyFriendly(RdfProperty):
    term = RdfTerm('isFamilyFriendly', 'https://schema.org/isFamilyFriendly', [])
    object: Boolean

@dataclass(frozen=True)
class tripOrigin(RdfProperty):
    term = RdfTerm('tripOrigin', 'https://schema.org/tripOrigin', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class numberOfAxles(RdfProperty):
    term = RdfTerm('numberOfAxles', 'https://schema.org/numberOfAxles', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class naturalProgression(RdfProperty):
    term = RdfTerm('naturalProgression', 'https://schema.org/naturalProgression', [])
    object: Text

@dataclass(frozen=True)
class distribution(RdfProperty):
    term = RdfTerm('distribution', 'https://schema.org/distribution', [])
    object: schemaorg.DataDownload

@dataclass(frozen=True)
class broadcastFrequency(RdfProperty):
    term = RdfTerm('broadcastFrequency', 'https://schema.org/broadcastFrequency', [])
    object: schemaorg.BroadcastFrequencySpecification | Text

@dataclass(frozen=True)
class size(RdfProperty):
    term = RdfTerm('size', 'https://schema.org/size', [])
    object: Text | schemaorg.QuantitativeValue | schemaorg.SizeSpecification | schemaorg.DefinedTerm

@dataclass(frozen=True)
class colorist(RdfProperty):
    term = RdfTerm('colorist', 'https://schema.org/colorist', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class parent(RdfProperty):
    term = RdfTerm('parent', 'https://schema.org/parent', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class contributor(RdfProperty):
    term = RdfTerm('contributor', 'https://schema.org/contributor', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class marginOfError(RdfProperty):
    term = RdfTerm('marginOfError', 'https://schema.org/marginOfError', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class servicePhone(RdfProperty):
    term = RdfTerm('servicePhone', 'https://schema.org/servicePhone', [])
    object: schemaorg.ContactPoint

@dataclass(frozen=True)
class suggestedMaxAge(RdfProperty):
    term = RdfTerm('suggestedMaxAge', 'https://schema.org/suggestedMaxAge', [])
    object: Number

@dataclass(frozen=True)
class partOfTrip(RdfProperty):
    term = RdfTerm('partOfTrip', 'https://schema.org/partOfTrip', [])
    object: schemaorg.Trip

@dataclass(frozen=True)
class targetUrl(RdfProperty):
    term = RdfTerm('targetUrl', 'https://schema.org/targetUrl', [])
    object: URL

@dataclass(frozen=True)
class geoCoveredBy(RdfProperty):
    term = RdfTerm('geoCoveredBy', 'https://schema.org/geoCoveredBy', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class associatedArticle(RdfProperty):
    term = RdfTerm('associatedArticle', 'https://schema.org/associatedArticle', [])
    object: schemaorg.NewsArticle

@dataclass(frozen=True)
class usesHealthPlanIdStandard(RdfProperty):
    term = RdfTerm('usesHealthPlanIdStandard', 'https://schema.org/usesHealthPlanIdStandard', [])
    object: Text | URL

@dataclass(frozen=True)
class educationalRole(RdfProperty):
    term = RdfTerm('educationalRole', 'https://schema.org/educationalRole', [])
    object: Text

@dataclass(frozen=True)
class vendor(RdfProperty):
    term = RdfTerm('vendor', 'https://schema.org/vendor', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class playMode(RdfProperty):
    term = RdfTerm('playMode', 'https://schema.org/playMode', [])
    object: schemaorg.GamePlayMode

@dataclass(frozen=True)
class drugUnit(RdfProperty):
    term = RdfTerm('drugUnit', 'https://schema.org/drugUnit', [])
    object: Text

@dataclass(frozen=True)
class buyer(RdfProperty):
    term = RdfTerm('buyer', 'https://schema.org/buyer', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class sampleType(RdfProperty):
    term = RdfTerm('sampleType', 'https://schema.org/sampleType', [])
    object: Text

@dataclass(frozen=True)
class trainName(RdfProperty):
    term = RdfTerm('trainName', 'https://schema.org/trainName', [])
    object: Text

@dataclass(frozen=True)
class awards(RdfProperty):
    term = RdfTerm('awards', 'https://schema.org/awards', [])
    object: Text

@dataclass(frozen=True)
class disambiguatingDescription(RdfProperty):
    term = RdfTerm('disambiguatingDescription', 'https://schema.org/disambiguatingDescription', [])
    object: Text

@dataclass(frozen=True)
class resultComment(RdfProperty):
    term = RdfTerm('resultComment', 'https://schema.org/resultComment', [])
    object: schemaorg.Comment

@dataclass(frozen=True)
class countryOfAssembly(RdfProperty):
    term = RdfTerm('countryOfAssembly', 'https://schema.org/countryOfAssembly', [])
    object: Text

@dataclass(frozen=True)
class temporalCoverage(RdfProperty):
    term = RdfTerm('temporalCoverage', 'https://schema.org/temporalCoverage', [])
    object: DateTime | Text | URL

@dataclass(frozen=True)
class activityFrequency(RdfProperty):
    term = RdfTerm('activityFrequency', 'https://schema.org/activityFrequency', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class iupacName(RdfProperty):
    term = RdfTerm('iupacName', 'https://schema.org/iupacName', [])
    object: Text

@dataclass(frozen=True)
class albumReleaseType(RdfProperty):
    term = RdfTerm('albumReleaseType', 'https://schema.org/albumReleaseType', [])
    object: schemaorg.MusicAlbumReleaseType

@dataclass(frozen=True)
class review(RdfProperty):
    term = RdfTerm('review', 'https://schema.org/review', [])
    object: schemaorg.Review

@dataclass(frozen=True)
class requiredQuantity(RdfProperty):
    term = RdfTerm('requiredQuantity', 'https://schema.org/requiredQuantity', [])
    object: Text | Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class jobTitle(RdfProperty):
    term = RdfTerm('jobTitle', 'https://schema.org/jobTitle', [])
    object: Text | schemaorg.DefinedTerm

@dataclass(frozen=True)
class downloadUrl(RdfProperty):
    term = RdfTerm('downloadUrl', 'https://schema.org/downloadUrl', [])
    object: URL

@dataclass(frozen=True)
class urlTemplate(RdfProperty):
    term = RdfTerm('urlTemplate', 'https://schema.org/urlTemplate', [])
    object: Text

@dataclass(frozen=True)
class contentUrl(RdfProperty):
    term = RdfTerm('contentUrl', 'https://schema.org/contentUrl', [])
    object: URL

@dataclass(frozen=True)
class claimReviewed(RdfProperty):
    term = RdfTerm('claimReviewed', 'https://schema.org/claimReviewed', [])
    object: Text

@dataclass(frozen=True)
class requiredCollateral(RdfProperty):
    term = RdfTerm('requiredCollateral', 'https://schema.org/requiredCollateral', [])
    object: Text | schemaorg.Thing

@dataclass(frozen=True)
class contraindication(RdfProperty):
    term = RdfTerm('contraindication', 'https://schema.org/contraindication', [])
    object: schemaorg.MedicalContraindication | Text

@dataclass(frozen=True)
class sourcedFrom(RdfProperty):
    term = RdfTerm('sourcedFrom', 'https://schema.org/sourcedFrom', [])
    object: schemaorg.BrainStructure

@dataclass(frozen=True)
class programmingLanguage(RdfProperty):
    term = RdfTerm('programmingLanguage', 'https://schema.org/programmingLanguage', [])
    object: schemaorg.ComputerLanguage | Text

@dataclass(frozen=True)
class issuedBy(RdfProperty):
    term = RdfTerm('issuedBy', 'https://schema.org/issuedBy', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class liveBlogUpdate(RdfProperty):
    term = RdfTerm('liveBlogUpdate', 'https://schema.org/liveBlogUpdate', [])
    object: schemaorg.BlogPosting

@dataclass(frozen=True)
class colleague(RdfProperty):
    term = RdfTerm('colleague', 'https://schema.org/colleague', [])
    object: URL | schemaorg.Person

@dataclass(frozen=True)
class torque(RdfProperty):
    term = RdfTerm('torque', 'https://schema.org/torque', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class providesService(RdfProperty):
    term = RdfTerm('providesService', 'https://schema.org/providesService', [])
    object: schemaorg.Service

@dataclass(frozen=True)
class postOfficeBoxNumber(RdfProperty):
    term = RdfTerm('postOfficeBoxNumber', 'https://schema.org/postOfficeBoxNumber', [])
    object: Text

@dataclass(frozen=True)
class durationOfWarranty(RdfProperty):
    term = RdfTerm('durationOfWarranty', 'https://schema.org/durationOfWarranty', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class publicAccess(RdfProperty):
    term = RdfTerm('publicAccess', 'https://schema.org/publicAccess', [])
    object: Boolean

@dataclass(frozen=True)
class brand(RdfProperty):
    term = RdfTerm('brand', 'https://schema.org/brand', [])
    object: schemaorg.Organization | schemaorg.Brand

@dataclass(frozen=True)
class cvdNumC19HOPats(RdfProperty):
    term = RdfTerm('cvdNumC19HOPats', 'https://schema.org/cvdNumC19HOPats', [])
    object: Number

@dataclass(frozen=True)
class courseCode(RdfProperty):
    term = RdfTerm('courseCode', 'https://schema.org/courseCode', [])
    object: Text

@dataclass(frozen=True)
class firstPerformance(RdfProperty):
    term = RdfTerm('firstPerformance', 'https://schema.org/firstPerformance', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class iso6523Code(RdfProperty):
    term = RdfTerm('iso6523Code', 'https://schema.org/iso6523Code', [])
    object: Text

@dataclass(frozen=True)
class maximumIntake(RdfProperty):
    term = RdfTerm('maximumIntake', 'https://schema.org/maximumIntake', [])
    object: schemaorg.MaximumDoseSchedule

@dataclass(frozen=True)
class sku(RdfProperty):
    term = RdfTerm('sku', 'https://schema.org/sku', [])
    object: Text

@dataclass(frozen=True)
class pickupTime(RdfProperty):
    term = RdfTerm('pickupTime', 'https://schema.org/pickupTime', [])
    object: DateTime

@dataclass(frozen=True)
class abstract(RdfProperty):
    term = RdfTerm('abstract', 'https://schema.org/abstract', [])
    object: Text

@dataclass(frozen=True)
class timeOfDay(RdfProperty):
    term = RdfTerm('timeOfDay', 'https://schema.org/timeOfDay', [])
    object: Text

@dataclass(frozen=True)
class aspect(RdfProperty):
    term = RdfTerm('aspect', 'https://schema.org/aspect', [])
    object: Text

@dataclass(frozen=True)
class geographicArea(RdfProperty):
    term = RdfTerm('geographicArea', 'https://schema.org/geographicArea', [])
    object: schemaorg.AdministrativeArea

@dataclass(frozen=True)
class bccRecipient(RdfProperty):
    term = RdfTerm('bccRecipient', 'https://schema.org/bccRecipient', [])
    object: schemaorg.ContactPoint | schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class cargoVolume(RdfProperty):
    term = RdfTerm('cargoVolume', 'https://schema.org/cargoVolume', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class measuredProperty(RdfProperty):
    term = RdfTerm('measuredProperty', 'https://schema.org/measuredProperty', [])
    object: schemaorg.Property

@dataclass(frozen=True)
class floorLimit(RdfProperty):
    term = RdfTerm('floorLimit', 'https://schema.org/floorLimit', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class accessCode(RdfProperty):
    term = RdfTerm('accessCode', 'https://schema.org/accessCode', [])
    object: Text

@dataclass(frozen=True)
class guidelineDate(RdfProperty):
    term = RdfTerm('guidelineDate', 'https://schema.org/guidelineDate', [])
    object: Date

@dataclass(frozen=True)
class numConstraints(RdfProperty):
    term = RdfTerm('numConstraints', 'https://schema.org/numConstraints', [])
    object: Integer

@dataclass(frozen=True)
class epidemiology(RdfProperty):
    term = RdfTerm('epidemiology', 'https://schema.org/epidemiology', [])
    object: Text

@dataclass(frozen=True)
class playerType(RdfProperty):
    term = RdfTerm('playerType', 'https://schema.org/playerType', [])
    object: Text

@dataclass(frozen=True)
class dateModified(RdfProperty):
    term = RdfTerm('dateModified', 'https://schema.org/dateModified', [])
    object: DateTime | Date

@dataclass(frozen=True)
class downvoteCount(RdfProperty):
    term = RdfTerm('downvoteCount', 'https://schema.org/downvoteCount', [])
    object: Integer

@dataclass(frozen=True)
class servingSize(RdfProperty):
    term = RdfTerm('servingSize', 'https://schema.org/servingSize', [])
    object: Text

@dataclass(frozen=True)
class recordedIn(RdfProperty):
    term = RdfTerm('recordedIn', 'https://schema.org/recordedIn', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class blogPosts(RdfProperty):
    term = RdfTerm('blogPosts', 'https://schema.org/blogPosts', [])
    object: schemaorg.BlogPosting

@dataclass(frozen=True)
class legislationTransposes(RdfProperty):
    term = RdfTerm('legislationTransposes', 'https://schema.org/legislationTransposes', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class observationAbout(RdfProperty):
    term = RdfTerm('observationAbout', 'https://schema.org/observationAbout', [])
    object: schemaorg.Place | schemaorg.Thing

@dataclass(frozen=True)
class materialExtent(RdfProperty):
    term = RdfTerm('materialExtent', 'https://schema.org/materialExtent', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class itemListOrder(RdfProperty):
    term = RdfTerm('itemListOrder', 'https://schema.org/itemListOrder', [])
    object: Text | schemaorg.ItemListOrderType

@dataclass(frozen=True)
class containsPlace(RdfProperty):
    term = RdfTerm('containsPlace', 'https://schema.org/containsPlace', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class previousItem(RdfProperty):
    term = RdfTerm('previousItem', 'https://schema.org/previousItem', [])
    object: schemaorg.ListItem

@dataclass(frozen=True)
class longitude(RdfProperty):
    term = RdfTerm('longitude', 'https://schema.org/longitude', [])
    object: Text | Number

@dataclass(frozen=True)
class targetName(RdfProperty):
    term = RdfTerm('targetName', 'https://schema.org/targetName', [])
    object: Text

@dataclass(frozen=True)
class isConsumableFor(RdfProperty):
    term = RdfTerm('isConsumableFor', 'https://schema.org/isConsumableFor', [])
    object: schemaorg.Product

@dataclass(frozen=True)
class orderItemNumber(RdfProperty):
    term = RdfTerm('orderItemNumber', 'https://schema.org/orderItemNumber', [])
    object: Text

@dataclass(frozen=True)
class inChIKey(RdfProperty):
    term = RdfTerm('inChIKey', 'https://schema.org/inChIKey', [])
    object: Text

@dataclass(frozen=True)
class readonlyValue(RdfProperty):
    term = RdfTerm('readonlyValue', 'https://schema.org/readonlyValue', [])
    object: Boolean

@dataclass(frozen=True)
class domiciledMortgage(RdfProperty):
    term = RdfTerm('domiciledMortgage', 'https://schema.org/domiciledMortgage', [])
    object: Boolean

@dataclass(frozen=True)
class artMedium(RdfProperty):
    term = RdfTerm('artMedium', 'https://schema.org/artMedium', [])
    object: Text | URL

@dataclass(frozen=True)
class parentService(RdfProperty):
    term = RdfTerm('parentService', 'https://schema.org/parentService', [])
    object: schemaorg.BroadcastService

@dataclass(frozen=True)
class flightNumber(RdfProperty):
    term = RdfTerm('flightNumber', 'https://schema.org/flightNumber', [])
    object: Text

@dataclass(frozen=True)
class softwareRequirements(RdfProperty):
    term = RdfTerm('softwareRequirements', 'https://schema.org/softwareRequirements', [])
    object: Text | URL

@dataclass(frozen=True)
class cashBack(RdfProperty):
    term = RdfTerm('cashBack', 'https://schema.org/cashBack', [])
    object: Number | Boolean

@dataclass(frozen=True)
class subEvents(RdfProperty):
    term = RdfTerm('subEvents', 'https://schema.org/subEvents', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class browserRequirements(RdfProperty):
    term = RdfTerm('browserRequirements', 'https://schema.org/browserRequirements', [])
    object: Text

@dataclass(frozen=True)
class lesser(RdfProperty):
    term = RdfTerm('lesser', 'https://schema.org/lesser', [])
    object: schemaorg.QualitativeValue

@dataclass(frozen=True)
class termCode(RdfProperty):
    term = RdfTerm('termCode', 'https://schema.org/termCode', [])
    object: Text

@dataclass(frozen=True)
class discussionUrl(RdfProperty):
    term = RdfTerm('discussionUrl', 'https://schema.org/discussionUrl', [])
    object: URL

@dataclass(frozen=True)
class valueName(RdfProperty):
    term = RdfTerm('valueName', 'https://schema.org/valueName', [])
    object: Text

@dataclass(frozen=True)
class elevation(RdfProperty):
    term = RdfTerm('elevation', 'https://schema.org/elevation', [])
    object: Number | Text

@dataclass(frozen=True)
class offeredBy(RdfProperty):
    term = RdfTerm('offeredBy', 'https://schema.org/offeredBy', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class hasBioPolymerSequence(RdfProperty):
    term = RdfTerm('hasBioPolymerSequence', 'https://schema.org/hasBioPolymerSequence', [])
    object: Text

@dataclass(frozen=True)
class typicalAgeRange(RdfProperty):
    term = RdfTerm('typicalAgeRange', 'https://schema.org/typicalAgeRange', [])
    object: Text

@dataclass(frozen=True)
class discount(RdfProperty):
    term = RdfTerm('discount', 'https://schema.org/discount', [])
    object: Text | Number

@dataclass(frozen=True)
class accessibilityHazard(RdfProperty):
    term = RdfTerm('accessibilityHazard', 'https://schema.org/accessibilityHazard', [])
    object: Text

@dataclass(frozen=True)
class fuelType(RdfProperty):
    term = RdfTerm('fuelType', 'https://schema.org/fuelType', [])
    object: schemaorg.QualitativeValue | Text | URL

@dataclass(frozen=True)
class specialCommitments(RdfProperty):
    term = RdfTerm('specialCommitments', 'https://schema.org/specialCommitments', [])
    object: Text

@dataclass(frozen=True)
class hasShippingService(RdfProperty):
    term = RdfTerm('hasShippingService', 'https://schema.org/hasShippingService', [])
    object: schemaorg.ShippingService

@dataclass(frozen=True)
class returnPolicyCountry(RdfProperty):
    term = RdfTerm('returnPolicyCountry', 'https://schema.org/returnPolicyCountry', [])
    object: schemaorg.Country | Text

@dataclass(frozen=True)
class color(RdfProperty):
    term = RdfTerm('color', 'https://schema.org/color', [])
    object: Text

@dataclass(frozen=True)
class orderPercentage(RdfProperty):
    term = RdfTerm('orderPercentage', 'https://schema.org/orderPercentage', [])
    object: Number

@dataclass(frozen=True)
class gtin(RdfProperty):
    term = RdfTerm('gtin', 'https://schema.org/gtin', [])
    object: Text | URL

@dataclass(frozen=True)
class customerRemorseReturnLabelSource(RdfProperty):
    term = RdfTerm('customerRemorseReturnLabelSource', 'https://schema.org/customerRemorseReturnLabelSource', [])
    object: schemaorg.ReturnLabelSourceEnumeration

@dataclass(frozen=True)
class numChildren(RdfProperty):
    term = RdfTerm('numChildren', 'https://schema.org/numChildren', [])
    object: schemaorg.QuantitativeValue | Integer

@dataclass(frozen=True)
class labelDetails(RdfProperty):
    term = RdfTerm('labelDetails', 'https://schema.org/labelDetails', [])
    object: URL

@dataclass(frozen=True)
class attendees(RdfProperty):
    term = RdfTerm('attendees', 'https://schema.org/attendees', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class circle(RdfProperty):
    term = RdfTerm('circle', 'https://schema.org/circle', [])
    object: Text

@dataclass(frozen=True)
class busNumber(RdfProperty):
    term = RdfTerm('busNumber', 'https://schema.org/busNumber', [])
    object: Text

@dataclass(frozen=True)
class audienceType(RdfProperty):
    term = RdfTerm('audienceType', 'https://schema.org/audienceType', [])
    object: Text

@dataclass(frozen=True)
class smokingAllowed(RdfProperty):
    term = RdfTerm('smokingAllowed', 'https://schema.org/smokingAllowed', [])
    object: Boolean

@dataclass(frozen=True)
class providesBroadcastService(RdfProperty):
    term = RdfTerm('providesBroadcastService', 'https://schema.org/providesBroadcastService', [])
    object: schemaorg.BroadcastService

@dataclass(frozen=True)
class inCodeSet(RdfProperty):
    term = RdfTerm('inCodeSet', 'https://schema.org/inCodeSet', [])
    object: schemaorg.CategoryCodeSet | URL

@dataclass(frozen=True)
class variablesMeasured(RdfProperty):
    term = RdfTerm('variablesMeasured', 'https://schema.org/variablesMeasured', [])
    object: schemaorg.PropertyValue | Text

@dataclass(frozen=True)
class diseaseSpreadStatistics(RdfProperty):
    term = RdfTerm('diseaseSpreadStatistics', 'https://schema.org/diseaseSpreadStatistics', [])
    object: schemaorg.Observation | schemaorg.Dataset | URL | schemaorg.WebContent

@dataclass(frozen=True)
class renegotiableLoan(RdfProperty):
    term = RdfTerm('renegotiableLoan', 'https://schema.org/renegotiableLoan', [])
    object: Boolean

@dataclass(frozen=True)
class drugClass(RdfProperty):
    term = RdfTerm('drugClass', 'https://schema.org/drugClass', [])
    object: schemaorg.DrugClass

@dataclass(frozen=True)
class aggregateElement(RdfProperty):
    term = RdfTerm('aggregateElement', 'https://schema.org/aggregateElement', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class hasCertification(RdfProperty):
    term = RdfTerm('hasCertification', 'https://schema.org/hasCertification', [])
    object: schemaorg.Certification

@dataclass(frozen=True)
class map(RdfProperty):
    term = RdfTerm('map', 'https://schema.org/map', [])
    object: URL

@dataclass(frozen=True)
class ownershipFundingInfo(RdfProperty):
    term = RdfTerm('ownershipFundingInfo', 'https://schema.org/ownershipFundingInfo', [])
    object: schemaorg.AboutPage | schemaorg.CreativeWork | Text | URL

@dataclass(frozen=True)
class postalCodePrefix(RdfProperty):
    term = RdfTerm('postalCodePrefix', 'https://schema.org/postalCodePrefix', [])
    object: Text

@dataclass(frozen=True)
class deliveryAddress(RdfProperty):
    term = RdfTerm('deliveryAddress', 'https://schema.org/deliveryAddress', [])
    object: schemaorg.PostalAddress

@dataclass(frozen=True)
class itemDefectReturnLabelSource(RdfProperty):
    term = RdfTerm('itemDefectReturnLabelSource', 'https://schema.org/itemDefectReturnLabelSource', [])
    object: schemaorg.ReturnLabelSourceEnumeration

@dataclass(frozen=True)
class orderValue(RdfProperty):
    term = RdfTerm('orderValue', 'https://schema.org/orderValue', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class itemOffered(RdfProperty):
    term = RdfTerm('itemOffered', 'https://schema.org/itemOffered', [])
    object: schemaorg.AggregateOffer | schemaorg.MenuItem | schemaorg.Event | schemaorg.Product | schemaorg.CreativeWork | schemaorg.Trip | schemaorg.Service

@dataclass(frozen=True)
class stepValue(RdfProperty):
    term = RdfTerm('stepValue', 'https://schema.org/stepValue', [])
    object: Number

@dataclass(frozen=True)
class arrivalTerminal(RdfProperty):
    term = RdfTerm('arrivalTerminal', 'https://schema.org/arrivalTerminal', [])
    object: Text

@dataclass(frozen=True)
class recipe(RdfProperty):
    term = RdfTerm('recipe', 'https://schema.org/recipe', [])
    object: schemaorg.Recipe

@dataclass(frozen=True)
class minValue(RdfProperty):
    term = RdfTerm('minValue', 'https://schema.org/minValue', [])
    object: Number

@dataclass(frozen=True)
class coverageEndTime(RdfProperty):
    term = RdfTerm('coverageEndTime', 'https://schema.org/coverageEndTime', [])
    object: DateTime

@dataclass(frozen=True)
class availableDeliveryMethod(RdfProperty):
    term = RdfTerm('availableDeliveryMethod', 'https://schema.org/availableDeliveryMethod', [])
    object: schemaorg.DeliveryMethod

@dataclass(frozen=True)
class maximumPhysicalAttendeeCapacity(RdfProperty):
    term = RdfTerm('maximumPhysicalAttendeeCapacity', 'https://schema.org/maximumPhysicalAttendeeCapacity', [])
    object: Integer

@dataclass(frozen=True)
class geoCovers(RdfProperty):
    term = RdfTerm('geoCovers', 'https://schema.org/geoCovers', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class executableLibraryName(RdfProperty):
    term = RdfTerm('executableLibraryName', 'https://schema.org/executableLibraryName', [])
    object: Text

@dataclass(frozen=True)
class permissionType(RdfProperty):
    term = RdfTerm('permissionType', 'https://schema.org/permissionType', [])
    object: schemaorg.DigitalDocumentPermissionType

@dataclass(frozen=True)
class includesAttraction(RdfProperty):
    term = RdfTerm('includesAttraction', 'https://schema.org/includesAttraction', [])
    object: schemaorg.TouristAttraction

@dataclass(frozen=True)
class dateVehicleFirstRegistered(RdfProperty):
    term = RdfTerm('dateVehicleFirstRegistered', 'https://schema.org/dateVehicleFirstRegistered', [])
    object: Date

@dataclass(frozen=True)
class valueAddedTaxIncluded(RdfProperty):
    term = RdfTerm('valueAddedTaxIncluded', 'https://schema.org/valueAddedTaxIncluded', [])
    object: Boolean

@dataclass(frozen=True)
class defaultValue(RdfProperty):
    term = RdfTerm('defaultValue', 'https://schema.org/defaultValue', [])
    object: schemaorg.Thing | Text

@dataclass(frozen=True)
class hasCourse(RdfProperty):
    term = RdfTerm('hasCourse', 'https://schema.org/hasCourse', [])
    object: schemaorg.Course

@dataclass(frozen=True)
class nonProprietaryName(RdfProperty):
    term = RdfTerm('nonProprietaryName', 'https://schema.org/nonProprietaryName', [])
    object: Text

@dataclass(frozen=True)
class serviceArea(RdfProperty):
    term = RdfTerm('serviceArea', 'https://schema.org/serviceArea', [])
    object: schemaorg.Place | schemaorg.AdministrativeArea | schemaorg.GeoShape

@dataclass(frozen=True)
class seeks(RdfProperty):
    term = RdfTerm('seeks', 'https://schema.org/seeks', [])
    object: schemaorg.Demand

@dataclass(frozen=True)
class storageRequirements(RdfProperty):
    term = RdfTerm('storageRequirements', 'https://schema.org/storageRequirements', [])
    object: URL | Text

@dataclass(frozen=True)
class album(RdfProperty):
    term = RdfTerm('album', 'https://schema.org/album', [])
    object: schemaorg.MusicAlbum

@dataclass(frozen=True)
class travelBans(RdfProperty):
    term = RdfTerm('travelBans', 'https://schema.org/travelBans', [])
    object: URL | schemaorg.WebContent

@dataclass(frozen=True)
class itemDefectReturnFees(RdfProperty):
    term = RdfTerm('itemDefectReturnFees', 'https://schema.org/itemDefectReturnFees', [])
    object: schemaorg.ReturnFeesEnumeration

@dataclass(frozen=True)
class includedComposition(RdfProperty):
    term = RdfTerm('includedComposition', 'https://schema.org/includedComposition', [])
    object: schemaorg.MusicComposition

@dataclass(frozen=True)
class signOrSymptom(RdfProperty):
    term = RdfTerm('signOrSymptom', 'https://schema.org/signOrSymptom', [])
    object: schemaorg.MedicalSignOrSymptom

@dataclass(frozen=True)
class handlingTime(RdfProperty):
    term = RdfTerm('handlingTime', 'https://schema.org/handlingTime', [])
    object: schemaorg.QuantitativeValue | schemaorg.ServicePeriod

@dataclass(frozen=True)
class shippingDestination(RdfProperty):
    term = RdfTerm('shippingDestination', 'https://schema.org/shippingDestination', [])
    object: schemaorg.DefinedRegion

@dataclass(frozen=True)
class customerRemorseReturnShippingFeesAmount(RdfProperty):
    term = RdfTerm('customerRemorseReturnShippingFeesAmount', 'https://schema.org/customerRemorseReturnShippingFeesAmount', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class broadcastTimezone(RdfProperty):
    term = RdfTerm('broadcastTimezone', 'https://schema.org/broadcastTimezone', [])
    object: Text

@dataclass(frozen=True)
class encodingType(RdfProperty):
    term = RdfTerm('encodingType', 'https://schema.org/encodingType', [])
    object: Text

@dataclass(frozen=True)
class foodWarning(RdfProperty):
    term = RdfTerm('foodWarning', 'https://schema.org/foodWarning', [])
    object: Text

@dataclass(frozen=True)
class resultReview(RdfProperty):
    term = RdfTerm('resultReview', 'https://schema.org/resultReview', [])
    object: schemaorg.Review

@dataclass(frozen=True)
class interactionCount(RdfProperty):
    term = RdfTerm('interactionCount', 'https://schema.org/interactionCount', [])
    object: Identifier

@dataclass(frozen=True)
class potentialUse(RdfProperty):
    term = RdfTerm('potentialUse', 'https://schema.org/potentialUse', [])
    object: schemaorg.DefinedTerm

@dataclass(frozen=True)
class directors(RdfProperty):
    term = RdfTerm('directors', 'https://schema.org/directors', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class byDay(RdfProperty):
    term = RdfTerm('byDay', 'https://schema.org/byDay', [])
    object: Text | schemaorg.DayOfWeek

@dataclass(frozen=True)
class carrierRequirements(RdfProperty):
    term = RdfTerm('carrierRequirements', 'https://schema.org/carrierRequirements', [])
    object: Text

@dataclass(frozen=True)
class multipleValues(RdfProperty):
    term = RdfTerm('multipleValues', 'https://schema.org/multipleValues', [])
    object: Boolean

@dataclass(frozen=True)
class accelerationTime(RdfProperty):
    term = RdfTerm('accelerationTime', 'https://schema.org/accelerationTime', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class observationDate(RdfProperty):
    term = RdfTerm('observationDate', 'https://schema.org/observationDate', [])
    object: DateTime

@dataclass(frozen=True)
class step(RdfProperty):
    term = RdfTerm('step', 'https://schema.org/step', [])
    object: Text | schemaorg.HowToSection | schemaorg.CreativeWork | schemaorg.HowToStep

@dataclass(frozen=True)
class afterMedia(RdfProperty):
    term = RdfTerm('afterMedia', 'https://schema.org/afterMedia', [])
    object: URL | schemaorg.MediaObject

@dataclass(frozen=True)
class requiredGender(RdfProperty):
    term = RdfTerm('requiredGender', 'https://schema.org/requiredGender', [])
    object: Text

@dataclass(frozen=True)
class dateSent(RdfProperty):
    term = RdfTerm('dateSent', 'https://schema.org/dateSent', [])
    object: DateTime

@dataclass(frozen=True)
class partOfSeries(RdfProperty):
    term = RdfTerm('partOfSeries', 'https://schema.org/partOfSeries', [])
    object: schemaorg.CreativeWorkSeries

@dataclass(frozen=True)
class releasedEvent(RdfProperty):
    term = RdfTerm('releasedEvent', 'https://schema.org/releasedEvent', [])
    object: schemaorg.PublicationEvent

@dataclass(frozen=True)
class nonEqual(RdfProperty):
    term = RdfTerm('nonEqual', 'https://schema.org/nonEqual', [])
    object: schemaorg.QualitativeValue

@dataclass(frozen=True)
class includedInHealthInsurancePlan(RdfProperty):
    term = RdfTerm('includedInHealthInsurancePlan', 'https://schema.org/includedInHealthInsurancePlan', [])
    object: schemaorg.HealthInsurancePlan

@dataclass(frozen=True)
class error(RdfProperty):
    term = RdfTerm('error', 'https://schema.org/error', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class bookFormat(RdfProperty):
    term = RdfTerm('bookFormat', 'https://schema.org/bookFormat', [])
    object: schemaorg.BookFormatType

@dataclass(frozen=True)
class relatedTherapy(RdfProperty):
    term = RdfTerm('relatedTherapy', 'https://schema.org/relatedTherapy', [])
    object: schemaorg.MedicalTherapy

@dataclass(frozen=True)
class coverageStartTime(RdfProperty):
    term = RdfTerm('coverageStartTime', 'https://schema.org/coverageStartTime', [])
    object: DateTime

@dataclass(frozen=True)
class diseasePreventionInfo(RdfProperty):
    term = RdfTerm('diseasePreventionInfo', 'https://schema.org/diseasePreventionInfo', [])
    object: schemaorg.WebContent | URL

@dataclass(frozen=True)
class textValue(RdfProperty):
    term = RdfTerm('textValue', 'https://schema.org/textValue', [])
    object: Text

@dataclass(frozen=True)
class hasMerchantReturnPolicy(RdfProperty):
    term = RdfTerm('hasMerchantReturnPolicy', 'https://schema.org/hasMerchantReturnPolicy', [])
    object: schemaorg.MerchantReturnPolicy

@dataclass(frozen=True)
class ccRecipient(RdfProperty):
    term = RdfTerm('ccRecipient', 'https://schema.org/ccRecipient', [])
    object: schemaorg.ContactPoint | schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class includesHealthPlanFormulary(RdfProperty):
    term = RdfTerm('includesHealthPlanFormulary', 'https://schema.org/includesHealthPlanFormulary', [])
    object: schemaorg.HealthPlanFormulary

@dataclass(frozen=True)
class priceComponent(RdfProperty):
    term = RdfTerm('priceComponent', 'https://schema.org/priceComponent', [])
    object: schemaorg.UnitPriceSpecification

@dataclass(frozen=True)
class relevantSpecialty(RdfProperty):
    term = RdfTerm('relevantSpecialty', 'https://schema.org/relevantSpecialty', [])
    object: schemaorg.MedicalSpecialty

@dataclass(frozen=True)
class modifiedTime(RdfProperty):
    term = RdfTerm('modifiedTime', 'https://schema.org/modifiedTime', [])
    object: DateTime

@dataclass(frozen=True)
class currency(RdfProperty):
    term = RdfTerm('currency', 'https://schema.org/currency', [])
    object: Text

@dataclass(frozen=True)
class bodyType(RdfProperty):
    term = RdfTerm('bodyType', 'https://schema.org/bodyType', [])
    object: URL | schemaorg.QualitativeValue | Text

@dataclass(frozen=True)
class molecularWeight(RdfProperty):
    term = RdfTerm('molecularWeight', 'https://schema.org/molecularWeight', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class publisherImprint(RdfProperty):
    term = RdfTerm('publisherImprint', 'https://schema.org/publisherImprint', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class exampleOfWork(RdfProperty):
    term = RdfTerm('exampleOfWork', 'https://schema.org/exampleOfWork', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class hasMolecularFunction(RdfProperty):
    term = RdfTerm('hasMolecularFunction', 'https://schema.org/hasMolecularFunction', [])
    object: URL | schemaorg.PropertyValue | schemaorg.DefinedTerm

@dataclass(frozen=True)
class numberOfAirbags(RdfProperty):
    term = RdfTerm('numberOfAirbags', 'https://schema.org/numberOfAirbags', [])
    object: Number | Text

@dataclass(frozen=True)
class estimatesRiskOf(RdfProperty):
    term = RdfTerm('estimatesRiskOf', 'https://schema.org/estimatesRiskOf', [])
    object: schemaorg.MedicalEntity

@dataclass(frozen=True)
class cvdNumC19Died(RdfProperty):
    term = RdfTerm('cvdNumC19Died', 'https://schema.org/cvdNumC19Died', [])
    object: Number

@dataclass(frozen=True)
class hasVariant(RdfProperty):
    term = RdfTerm('hasVariant', 'https://schema.org/hasVariant', [])
    object: schemaorg.Product

@dataclass(frozen=True)
class issuedThrough(RdfProperty):
    term = RdfTerm('issuedThrough', 'https://schema.org/issuedThrough', [])
    object: schemaorg.Service

@dataclass(frozen=True)
class isGift(RdfProperty):
    term = RdfTerm('isGift', 'https://schema.org/isGift', [])
    object: Boolean

@dataclass(frozen=True)
class recipient(RdfProperty):
    term = RdfTerm('recipient', 'https://schema.org/recipient', [])
    object: schemaorg.ContactPoint | schemaorg.Person | schemaorg.Audience | schemaorg.Organization

@dataclass(frozen=True)
class reviews(RdfProperty):
    term = RdfTerm('reviews', 'https://schema.org/reviews', [])
    object: schemaorg.Review

@dataclass(frozen=True)
class byMonth(RdfProperty):
    term = RdfTerm('byMonth', 'https://schema.org/byMonth', [])
    object: Integer

@dataclass(frozen=True)
class creator(RdfProperty):
    term = RdfTerm('creator', 'https://schema.org/creator', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class regionsAllowed(RdfProperty):
    term = RdfTerm('regionsAllowed', 'https://schema.org/regionsAllowed', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class telephone(RdfProperty):
    term = RdfTerm('telephone', 'https://schema.org/telephone', [])
    object: Text

@dataclass(frozen=True)
class vehicleConfiguration(RdfProperty):
    term = RdfTerm('vehicleConfiguration', 'https://schema.org/vehicleConfiguration', [])
    object: Text

@dataclass(frozen=True)
class percentile90(RdfProperty):
    term = RdfTerm('percentile90', 'https://schema.org/percentile90', [])
    object: Number

@dataclass(frozen=True)
class numberOfAvailableAccommodationUnits(RdfProperty):
    term = RdfTerm('numberOfAvailableAccommodationUnits', 'https://schema.org/numberOfAvailableAccommodationUnits', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class transcript(RdfProperty):
    term = RdfTerm('transcript', 'https://schema.org/transcript', [])
    object: Text

@dataclass(frozen=True)
class sportsEvent(RdfProperty):
    term = RdfTerm('sportsEvent', 'https://schema.org/sportsEvent', [])
    object: schemaorg.SportsEvent

@dataclass(frozen=True)
class expires(RdfProperty):
    term = RdfTerm('expires', 'https://schema.org/expires', [])
    object: Date | DateTime

@dataclass(frozen=True)
class eligibleQuantity(RdfProperty):
    term = RdfTerm('eligibleQuantity', 'https://schema.org/eligibleQuantity', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class experienceRequirements(RdfProperty):
    term = RdfTerm('experienceRequirements', 'https://schema.org/experienceRequirements', [])
    object: schemaorg.OccupationalExperienceRequirements | Text

@dataclass(frozen=True)
class email(RdfProperty):
    term = RdfTerm('email', 'https://schema.org/email', [])
    object: Text

@dataclass(frozen=True)
class eligibilityToWorkRequirement(RdfProperty):
    term = RdfTerm('eligibilityToWorkRequirement', 'https://schema.org/eligibilityToWorkRequirement', [])
    object: Text

@dataclass(frozen=True)
class thumbnailUrl(RdfProperty):
    term = RdfTerm('thumbnailUrl', 'https://schema.org/thumbnailUrl', [])
    object: URL

@dataclass(frozen=True)
class unitText(RdfProperty):
    term = RdfTerm('unitText', 'https://schema.org/unitText', [])
    object: Text

@dataclass(frozen=True)
class playersOnline(RdfProperty):
    term = RdfTerm('playersOnline', 'https://schema.org/playersOnline', [])
    object: Integer

@dataclass(frozen=True)
class award(RdfProperty):
    term = RdfTerm('award', 'https://schema.org/award', [])
    object: Text

@dataclass(frozen=True)
class legislationResponsible(RdfProperty):
    term = RdfTerm('legislationResponsible', 'https://schema.org/legislationResponsible', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class subTest(RdfProperty):
    term = RdfTerm('subTest', 'https://schema.org/subTest', [])
    object: schemaorg.MedicalTest

@dataclass(frozen=True)
class tongueWeight(RdfProperty):
    term = RdfTerm('tongueWeight', 'https://schema.org/tongueWeight', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class ticketedSeat(RdfProperty):
    term = RdfTerm('ticketedSeat', 'https://schema.org/ticketedSeat', [])
    object: schemaorg.Seat

@dataclass(frozen=True)
class isUnlabelledFallback(RdfProperty):
    term = RdfTerm('isUnlabelledFallback', 'https://schema.org/isUnlabelledFallback', [])
    object: Boolean

@dataclass(frozen=True)
class merchant(RdfProperty):
    term = RdfTerm('merchant', 'https://schema.org/merchant', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class characterAttribute(RdfProperty):
    term = RdfTerm('characterAttribute', 'https://schema.org/characterAttribute', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class mentions(RdfProperty):
    term = RdfTerm('mentions', 'https://schema.org/mentions', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class postalCode(RdfProperty):
    term = RdfTerm('postalCode', 'https://schema.org/postalCode', [])
    object: Text

@dataclass(frozen=True)
class asin(RdfProperty):
    term = RdfTerm('asin', 'https://schema.org/asin', [])
    object: URL | Text

@dataclass(frozen=True)
class vehicleEngine(RdfProperty):
    term = RdfTerm('vehicleEngine', 'https://schema.org/vehicleEngine', [])
    object: schemaorg.EngineSpecification

@dataclass(frozen=True)
class vatID(RdfProperty):
    term = RdfTerm('vatID', 'https://schema.org/vatID', [])
    object: Text

@dataclass(frozen=True)
class course(RdfProperty):
    term = RdfTerm('course', 'https://schema.org/course', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class hoursAvailable(RdfProperty):
    term = RdfTerm('hoursAvailable', 'https://schema.org/hoursAvailable', [])
    object: schemaorg.OpeningHoursSpecification

@dataclass(frozen=True)
class cvdCollectionDate(RdfProperty):
    term = RdfTerm('cvdCollectionDate', 'https://schema.org/cvdCollectionDate', [])
    object: DateTime | Text

@dataclass(frozen=True)
class qualifiedExpense(RdfProperty):
    term = RdfTerm('qualifiedExpense', 'https://schema.org/qualifiedExpense', [])
    object: schemaorg.IncentiveQualifiedExpenseType

@dataclass(frozen=True)
class healthPlanPharmacyCategory(RdfProperty):
    term = RdfTerm('healthPlanPharmacyCategory', 'https://schema.org/healthPlanPharmacyCategory', [])
    object: Text

@dataclass(frozen=True)
class restPeriods(RdfProperty):
    term = RdfTerm('restPeriods', 'https://schema.org/restPeriods', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class participant(RdfProperty):
    term = RdfTerm('participant', 'https://schema.org/participant', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class albumRelease(RdfProperty):
    term = RdfTerm('albumRelease', 'https://schema.org/albumRelease', [])
    object: schemaorg.MusicRelease

@dataclass(frozen=True)
class acceptedAnswer(RdfProperty):
    term = RdfTerm('acceptedAnswer', 'https://schema.org/acceptedAnswer', [])
    object: schemaorg.ItemList | schemaorg.Answer

@dataclass(frozen=True)
class estimatedFlightDuration(RdfProperty):
    term = RdfTerm('estimatedFlightDuration', 'https://schema.org/estimatedFlightDuration', [])
    object: schemaorg.Duration | Text

@dataclass(frozen=True)
class schoolClosuresInfo(RdfProperty):
    term = RdfTerm('schoolClosuresInfo', 'https://schema.org/schoolClosuresInfo', [])
    object: schemaorg.WebContent | URL

@dataclass(frozen=True)
class isPartOfBioChemEntity(RdfProperty):
    term = RdfTerm('isPartOfBioChemEntity', 'https://schema.org/isPartOfBioChemEntity', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class acquireLicensePage(RdfProperty):
    term = RdfTerm('acquireLicensePage', 'https://schema.org/acquireLicensePage', [])
    object: URL | schemaorg.CreativeWork

@dataclass(frozen=True)
class jurisdiction(RdfProperty):
    term = RdfTerm('jurisdiction', 'https://schema.org/jurisdiction', [])
    object: schemaorg.AdministrativeArea | Text

@dataclass(frozen=True)
class reportNumber(RdfProperty):
    term = RdfTerm('reportNumber', 'https://schema.org/reportNumber', [])
    object: Text

@dataclass(frozen=True)
class httpMethod(RdfProperty):
    term = RdfTerm('httpMethod', 'https://schema.org/httpMethod', [])
    object: Text

@dataclass(frozen=True)
class readBy(RdfProperty):
    term = RdfTerm('readBy', 'https://schema.org/readBy', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class lesserOrEqual(RdfProperty):
    term = RdfTerm('lesserOrEqual', 'https://schema.org/lesserOrEqual', [])
    object: schemaorg.QualitativeValue

@dataclass(frozen=True)
class scheduledPaymentDate(RdfProperty):
    term = RdfTerm('scheduledPaymentDate', 'https://schema.org/scheduledPaymentDate', [])
    object: Date

@dataclass(frozen=True)
class certificationIdentification(RdfProperty):
    term = RdfTerm('certificationIdentification', 'https://schema.org/certificationIdentification', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class hasDigitalDocumentPermission(RdfProperty):
    term = RdfTerm('hasDigitalDocumentPermission', 'https://schema.org/hasDigitalDocumentPermission', [])
    object: schemaorg.DigitalDocumentPermission

@dataclass(frozen=True)
class loanPaymentFrequency(RdfProperty):
    term = RdfTerm('loanPaymentFrequency', 'https://schema.org/loanPaymentFrequency', [])
    object: Number

@dataclass(frozen=True)
class arrivalBoatTerminal(RdfProperty):
    term = RdfTerm('arrivalBoatTerminal', 'https://schema.org/arrivalBoatTerminal', [])
    object: schemaorg.BoatTerminal

@dataclass(frozen=True)
class accountMinimumInflow(RdfProperty):
    term = RdfTerm('accountMinimumInflow', 'https://schema.org/accountMinimumInflow', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class infectiousAgent(RdfProperty):
    term = RdfTerm('infectiousAgent', 'https://schema.org/infectiousAgent', [])
    object: Text

@dataclass(frozen=True)
class postalCodeEnd(RdfProperty):
    term = RdfTerm('postalCodeEnd', 'https://schema.org/postalCodeEnd', [])
    object: Text

@dataclass(frozen=True)
class vehicleSeatingCapacity(RdfProperty):
    term = RdfTerm('vehicleSeatingCapacity', 'https://schema.org/vehicleSeatingCapacity', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class additionalNumberOfGuests(RdfProperty):
    term = RdfTerm('additionalNumberOfGuests', 'https://schema.org/additionalNumberOfGuests', [])
    object: Number

@dataclass(frozen=True)
class incentiveStatus(RdfProperty):
    term = RdfTerm('incentiveStatus', 'https://schema.org/incentiveStatus', [])
    object: schemaorg.IncentiveStatus

@dataclass(frozen=True)
class category(RdfProperty):
    term = RdfTerm('category', 'https://schema.org/category', [])
    object: Text | schemaorg.CategoryCode | URL | schemaorg.PhysicalActivityCategory | schemaorg.Thing

@dataclass(frozen=True)
class geoEquals(RdfProperty):
    term = RdfTerm('geoEquals', 'https://schema.org/geoEquals', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class spokenByCharacter(RdfProperty):
    term = RdfTerm('spokenByCharacter', 'https://schema.org/spokenByCharacter', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class evidenceOrigin(RdfProperty):
    term = RdfTerm('evidenceOrigin', 'https://schema.org/evidenceOrigin', [])
    object: Text

@dataclass(frozen=True)
class photos(RdfProperty):
    term = RdfTerm('photos', 'https://schema.org/photos', [])
    object: schemaorg.ImageObject | schemaorg.Photograph

@dataclass(frozen=True)
class normalRange(RdfProperty):
    term = RdfTerm('normalRange', 'https://schema.org/normalRange', [])
    object: schemaorg.MedicalEnumeration | Text

@dataclass(frozen=True)
class roofLoad(RdfProperty):
    term = RdfTerm('roofLoad', 'https://schema.org/roofLoad', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class gtin14(RdfProperty):
    term = RdfTerm('gtin14', 'https://schema.org/gtin14', [])
    object: Text

@dataclass(frozen=True)
class incentives(RdfProperty):
    term = RdfTerm('incentives', 'https://schema.org/incentives', [])
    object: Text

@dataclass(frozen=True)
class tocEntry(RdfProperty):
    term = RdfTerm('tocEntry', 'https://schema.org/tocEntry', [])
    object: schemaorg.HyperTocEntry

@dataclass(frozen=True)
class catalog(RdfProperty):
    term = RdfTerm('catalog', 'https://schema.org/catalog', [])
    object: schemaorg.DataCatalog

@dataclass(frozen=True)
class inChI(RdfProperty):
    term = RdfTerm('inChI', 'https://schema.org/inChI', [])
    object: Text

@dataclass(frozen=True)
class fromLocation(RdfProperty):
    term = RdfTerm('fromLocation', 'https://schema.org/fromLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class membershipNumber(RdfProperty):
    term = RdfTerm('membershipNumber', 'https://schema.org/membershipNumber', [])
    object: Text

@dataclass(frozen=True)
class musicReleaseFormat(RdfProperty):
    term = RdfTerm('musicReleaseFormat', 'https://schema.org/musicReleaseFormat', [])
    object: schemaorg.MusicReleaseFormatType

@dataclass(frozen=True)
class geoIntersects(RdfProperty):
    term = RdfTerm('geoIntersects', 'https://schema.org/geoIntersects', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class musicCompositionForm(RdfProperty):
    term = RdfTerm('musicCompositionForm', 'https://schema.org/musicCompositionForm', [])
    object: Text

@dataclass(frozen=True)
class dietFeatures(RdfProperty):
    term = RdfTerm('dietFeatures', 'https://schema.org/dietFeatures', [])
    object: Text

@dataclass(frozen=True)
class startTime(RdfProperty):
    term = RdfTerm('startTime', 'https://schema.org/startTime', [])
    object: DateTime | Time

@dataclass(frozen=True)
class accessibilityFeature(RdfProperty):
    term = RdfTerm('accessibilityFeature', 'https://schema.org/accessibilityFeature', [])
    object: Text

@dataclass(frozen=True)
class accessibilityAPI(RdfProperty):
    term = RdfTerm('accessibilityAPI', 'https://schema.org/accessibilityAPI', [])
    object: Text

@dataclass(frozen=True)
class monthsOfExperience(RdfProperty):
    term = RdfTerm('monthsOfExperience', 'https://schema.org/monthsOfExperience', [])
    object: Number

@dataclass(frozen=True)
class colorSwatch(RdfProperty):
    term = RdfTerm('colorSwatch', 'https://schema.org/colorSwatch', [])
    object: URL | schemaorg.ImageObject

@dataclass(frozen=True)
class propertyID(RdfProperty):
    term = RdfTerm('propertyID', 'https://schema.org/propertyID', [])
    object: URL | Text

@dataclass(frozen=True)
class offersPrescriptionByMail(RdfProperty):
    term = RdfTerm('offersPrescriptionByMail', 'https://schema.org/offersPrescriptionByMail', [])
    object: Boolean

@dataclass(frozen=True)
class legislationDateVersion(RdfProperty):
    term = RdfTerm('legislationDateVersion', 'https://schema.org/legislationDateVersion', [])
    object: Date

@dataclass(frozen=True)
class shippingRate(RdfProperty):
    term = RdfTerm('shippingRate', 'https://schema.org/shippingRate', [])
    object: schemaorg.MonetaryAmount | schemaorg.ShippingRateSettings

@dataclass(frozen=True)
class alternativeHeadline(RdfProperty):
    term = RdfTerm('alternativeHeadline', 'https://schema.org/alternativeHeadline', [])
    object: Text

@dataclass(frozen=True)
class preOp(RdfProperty):
    term = RdfTerm('preOp', 'https://schema.org/preOp', [])
    object: Text

@dataclass(frozen=True)
class associatedDisease(RdfProperty):
    term = RdfTerm('associatedDisease', 'https://schema.org/associatedDisease', [])
    object: URL | schemaorg.PropertyValue | schemaorg.MedicalCondition

@dataclass(frozen=True)
class sibling(RdfProperty):
    term = RdfTerm('sibling', 'https://schema.org/sibling', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class author(RdfProperty):
    term = RdfTerm('author', 'https://schema.org/author', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class dayOfWeek(RdfProperty):
    term = RdfTerm('dayOfWeek', 'https://schema.org/dayOfWeek', [])
    object: schemaorg.DayOfWeek

@dataclass(frozen=True)
class dependencies(RdfProperty):
    term = RdfTerm('dependencies', 'https://schema.org/dependencies', [])
    object: Text

@dataclass(frozen=True)
class proteinContent(RdfProperty):
    term = RdfTerm('proteinContent', 'https://schema.org/proteinContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class legislationPassedBy(RdfProperty):
    term = RdfTerm('legislationPassedBy', 'https://schema.org/legislationPassedBy', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class inLanguage(RdfProperty):
    term = RdfTerm('inLanguage', 'https://schema.org/inLanguage', [])
    object: Text | schemaorg.Language

@dataclass(frozen=True)
class provider(RdfProperty):
    term = RdfTerm('provider', 'https://schema.org/provider', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class bankAccountType(RdfProperty):
    term = RdfTerm('bankAccountType', 'https://schema.org/bankAccountType', [])
    object: Text | URL

@dataclass(frozen=True)
class tickerSymbol(RdfProperty):
    term = RdfTerm('tickerSymbol', 'https://schema.org/tickerSymbol', [])
    object: Text

@dataclass(frozen=True)
class legislationLegalValue(RdfProperty):
    term = RdfTerm('legislationLegalValue', 'https://schema.org/legislationLegalValue', [])
    object: schemaorg.LegalValueLevel

@dataclass(frozen=True)
class url(RdfProperty):
    term = RdfTerm('url', 'https://schema.org/url', [])
    object: URL

@dataclass(frozen=True)
class applicableLocation(RdfProperty):
    term = RdfTerm('applicableLocation', 'https://schema.org/applicableLocation', [])
    object: schemaorg.AdministrativeArea

@dataclass(frozen=True)
class commentText(RdfProperty):
    term = RdfTerm('commentText', 'https://schema.org/commentText', [])
    object: Text

@dataclass(frozen=True)
class maximumEnrollment(RdfProperty):
    term = RdfTerm('maximumEnrollment', 'https://schema.org/maximumEnrollment', [])
    object: Integer

@dataclass(frozen=True)
class wordCount(RdfProperty):
    term = RdfTerm('wordCount', 'https://schema.org/wordCount', [])
    object: Integer

@dataclass(frozen=True)
class comprisedOf(RdfProperty):
    term = RdfTerm('comprisedOf', 'https://schema.org/comprisedOf', [])
    object: schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem

@dataclass(frozen=True)
class usesDevice(RdfProperty):
    term = RdfTerm('usesDevice', 'https://schema.org/usesDevice', [])
    object: schemaorg.MedicalDevice

@dataclass(frozen=True)
class cvdFacilityCounty(RdfProperty):
    term = RdfTerm('cvdFacilityCounty', 'https://schema.org/cvdFacilityCounty', [])
    object: Text

@dataclass(frozen=True)
class parents(RdfProperty):
    term = RdfTerm('parents', 'https://schema.org/parents', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class video(RdfProperty):
    term = RdfTerm('video', 'https://schema.org/video', [])
    object: schemaorg.VideoObject | schemaorg.Clip

@dataclass(frozen=True)
class printPage(RdfProperty):
    term = RdfTerm('printPage', 'https://schema.org/printPage', [])
    object: Text

@dataclass(frozen=True)
class duplicateTherapy(RdfProperty):
    term = RdfTerm('duplicateTherapy', 'https://schema.org/duplicateTherapy', [])
    object: schemaorg.MedicalTherapy

@dataclass(frozen=True)
class leiCode(RdfProperty):
    term = RdfTerm('leiCode', 'https://schema.org/leiCode', [])
    object: Text

@dataclass(frozen=True)
class awayTeam(RdfProperty):
    term = RdfTerm('awayTeam', 'https://schema.org/awayTeam', [])
    object: schemaorg.SportsTeam | schemaorg.Person

@dataclass(frozen=True)
class serviceAudience(RdfProperty):
    term = RdfTerm('serviceAudience', 'https://schema.org/serviceAudience', [])
    object: schemaorg.Audience

@dataclass(frozen=True)
class maximumAttendeeCapacity(RdfProperty):
    term = RdfTerm('maximumAttendeeCapacity', 'https://schema.org/maximumAttendeeCapacity', [])
    object: Integer

@dataclass(frozen=True)
class postalCodeBegin(RdfProperty):
    term = RdfTerm('postalCodeBegin', 'https://schema.org/postalCodeBegin', [])
    object: Text

@dataclass(frozen=True)
class workload(RdfProperty):
    term = RdfTerm('workload', 'https://schema.org/workload', [])
    object: schemaorg.Energy | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class exercisePlan(RdfProperty):
    term = RdfTerm('exercisePlan', 'https://schema.org/exercisePlan', [])
    object: schemaorg.ExercisePlan

@dataclass(frozen=True)
class totalJobOpenings(RdfProperty):
    term = RdfTerm('totalJobOpenings', 'https://schema.org/totalJobOpenings', [])
    object: Integer

@dataclass(frozen=True)
class totalPrice(RdfProperty):
    term = RdfTerm('totalPrice', 'https://schema.org/totalPrice', [])
    object: Text | Number | schemaorg.PriceSpecification

@dataclass(frozen=True)
class device(RdfProperty):
    term = RdfTerm('device', 'https://schema.org/device', [])
    object: Text

@dataclass(frozen=True)
class weightPercentage(RdfProperty):
    term = RdfTerm('weightPercentage', 'https://schema.org/weightPercentage', [])
    object: Number

@dataclass(frozen=True)
class hasMenu(RdfProperty):
    term = RdfTerm('hasMenu', 'https://schema.org/hasMenu', [])
    object: schemaorg.Menu | Text | URL

@dataclass(frozen=True)
class signDetected(RdfProperty):
    term = RdfTerm('signDetected', 'https://schema.org/signDetected', [])
    object: schemaorg.MedicalSign

@dataclass(frozen=True)
class item(RdfProperty):
    term = RdfTerm('item', 'https://schema.org/item', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class legalStatus(RdfProperty):
    term = RdfTerm('legalStatus', 'https://schema.org/legalStatus', [])
    object: schemaorg.DrugLegalStatus | schemaorg.MedicalEnumeration | Text

@dataclass(frozen=True)
class aircraft(RdfProperty):
    term = RdfTerm('aircraft', 'https://schema.org/aircraft', [])
    object: schemaorg.Vehicle | Text

@dataclass(frozen=True)
class familyName(RdfProperty):
    term = RdfTerm('familyName', 'https://schema.org/familyName', [])
    object: Text

@dataclass(frozen=True)
class teaches(RdfProperty):
    term = RdfTerm('teaches', 'https://schema.org/teaches', [])
    object: Text | schemaorg.DefinedTerm

@dataclass(frozen=True)
class serviceOutput(RdfProperty):
    term = RdfTerm('serviceOutput', 'https://schema.org/serviceOutput', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class reservationId(RdfProperty):
    term = RdfTerm('reservationId', 'https://schema.org/reservationId', [])
    object: Text

@dataclass(frozen=True)
class priceRange(RdfProperty):
    term = RdfTerm('priceRange', 'https://schema.org/priceRange', [])
    object: Text

@dataclass(frozen=True)
class numberOfBedrooms(RdfProperty):
    term = RdfTerm('numberOfBedrooms', 'https://schema.org/numberOfBedrooms', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class seriousAdverseOutcome(RdfProperty):
    term = RdfTerm('seriousAdverseOutcome', 'https://schema.org/seriousAdverseOutcome', [])
    object: schemaorg.MedicalEntity

@dataclass(frozen=True)
class availabilityStarts(RdfProperty):
    term = RdfTerm('availabilityStarts', 'https://schema.org/availabilityStarts', [])
    object: Date | DateTime | Time

@dataclass(frozen=True)
class hasHealthAspect(RdfProperty):
    term = RdfTerm('hasHealthAspect', 'https://schema.org/hasHealthAspect', [])
    object: schemaorg.HealthAspectEnumeration

@dataclass(frozen=True)
class byMonthDay(RdfProperty):
    term = RdfTerm('byMonthDay', 'https://schema.org/byMonthDay', [])
    object: Integer

@dataclass(frozen=True)
class videoFormat(RdfProperty):
    term = RdfTerm('videoFormat', 'https://schema.org/videoFormat', [])
    object: Text

@dataclass(frozen=True)
class reviewRating(RdfProperty):
    term = RdfTerm('reviewRating', 'https://schema.org/reviewRating', [])
    object: schemaorg.Rating

@dataclass(frozen=True)
class estimatedSalary(RdfProperty):
    term = RdfTerm('estimatedSalary', 'https://schema.org/estimatedSalary', [])
    object: schemaorg.MonetaryAmount | Number | schemaorg.MonetaryAmountDistribution

@dataclass(frozen=True)
class associatedReview(RdfProperty):
    term = RdfTerm('associatedReview', 'https://schema.org/associatedReview', [])
    object: schemaorg.Review

@dataclass(frozen=True)
class geoMidpoint(RdfProperty):
    term = RdfTerm('geoMidpoint', 'https://schema.org/geoMidpoint', [])
    object: schemaorg.GeoCoordinates

@dataclass(frozen=True)
class acquiredFrom(RdfProperty):
    term = RdfTerm('acquiredFrom', 'https://schema.org/acquiredFrom', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class seasonalOverride(RdfProperty):
    term = RdfTerm('seasonalOverride', 'https://schema.org/seasonalOverride', [])
    object: schemaorg.OpeningHoursSpecification

@dataclass(frozen=True)
class originatesFrom(RdfProperty):
    term = RdfTerm('originatesFrom', 'https://schema.org/originatesFrom', [])
    object: schemaorg.Vessel

@dataclass(frozen=True)
class clincalPharmacology(RdfProperty):
    term = RdfTerm('clincalPharmacology', 'https://schema.org/clincalPharmacology', [])
    object: Text

@dataclass(frozen=True)
class healthPlanDrugOption(RdfProperty):
    term = RdfTerm('healthPlanDrugOption', 'https://schema.org/healthPlanDrugOption', [])
    object: Text

@dataclass(frozen=True)
class currentExchangeRate(RdfProperty):
    term = RdfTerm('currentExchangeRate', 'https://schema.org/currentExchangeRate', [])
    object: schemaorg.UnitPriceSpecification

@dataclass(frozen=True)
class associatedMedia(RdfProperty):
    term = RdfTerm('associatedMedia', 'https://schema.org/associatedMedia', [])
    object: schemaorg.MediaObject

@dataclass(frozen=True)
class videoQuality(RdfProperty):
    term = RdfTerm('videoQuality', 'https://schema.org/videoQuality', [])
    object: Text

@dataclass(frozen=True)
class childMaxAge(RdfProperty):
    term = RdfTerm('childMaxAge', 'https://schema.org/childMaxAge', [])
    object: Number

@dataclass(frozen=True)
class spatialCoverage(RdfProperty):
    term = RdfTerm('spatialCoverage', 'https://schema.org/spatialCoverage', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class cvdNumBedsOcc(RdfProperty):
    term = RdfTerm('cvdNumBedsOcc', 'https://schema.org/cvdNumBedsOcc', [])
    object: Number

@dataclass(frozen=True)
class numberedPosition(RdfProperty):
    term = RdfTerm('numberedPosition', 'https://schema.org/numberedPosition', [])
    object: Number

@dataclass(frozen=True)
class benefitsSummaryUrl(RdfProperty):
    term = RdfTerm('benefitsSummaryUrl', 'https://schema.org/benefitsSummaryUrl', [])
    object: URL

@dataclass(frozen=True)
class repetitions(RdfProperty):
    term = RdfTerm('repetitions', 'https://schema.org/repetitions', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class authenticator(RdfProperty):
    term = RdfTerm('authenticator', 'https://schema.org/authenticator', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class height(RdfProperty):
    term = RdfTerm('height', 'https://schema.org/height', [])
    object: schemaorg.Distance | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class expectedPrognosis(RdfProperty):
    term = RdfTerm('expectedPrognosis', 'https://schema.org/expectedPrognosis', [])
    object: Text

@dataclass(frozen=True)
class includedDataCatalog(RdfProperty):
    term = RdfTerm('includedDataCatalog', 'https://schema.org/includedDataCatalog', [])
    object: schemaorg.DataCatalog

@dataclass(frozen=True)
class numberOfPreviousOwners(RdfProperty):
    term = RdfTerm('numberOfPreviousOwners', 'https://schema.org/numberOfPreviousOwners', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class boardingPolicy(RdfProperty):
    term = RdfTerm('boardingPolicy', 'https://schema.org/boardingPolicy', [])
    object: schemaorg.BoardingPolicyType

@dataclass(frozen=True)
class regionDrained(RdfProperty):
    term = RdfTerm('regionDrained', 'https://schema.org/regionDrained', [])
    object: schemaorg.AnatomicalSystem | schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class performers(RdfProperty):
    term = RdfTerm('performers', 'https://schema.org/performers', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class encoding(RdfProperty):
    term = RdfTerm('encoding', 'https://schema.org/encoding', [])
    object: schemaorg.MediaObject

@dataclass(frozen=True)
class gameTip(RdfProperty):
    term = RdfTerm('gameTip', 'https://schema.org/gameTip', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class valueRequired(RdfProperty):
    term = RdfTerm('valueRequired', 'https://schema.org/valueRequired', [])
    object: Boolean

@dataclass(frozen=True)
class eligibleDuration(RdfProperty):
    term = RdfTerm('eligibleDuration', 'https://schema.org/eligibleDuration', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class xpath(RdfProperty):
    term = RdfTerm('xpath', 'https://schema.org/xpath', [])
    object: XPathType

@dataclass(frozen=True)
class lowPrice(RdfProperty):
    term = RdfTerm('lowPrice', 'https://schema.org/lowPrice', [])
    object: Text | Number

@dataclass(frozen=True)
class honorificPrefix(RdfProperty):
    term = RdfTerm('honorificPrefix', 'https://schema.org/honorificPrefix', [])
    object: Text

@dataclass(frozen=True)
class termDuration(RdfProperty):
    term = RdfTerm('termDuration', 'https://schema.org/termDuration', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class seatNumber(RdfProperty):
    term = RdfTerm('seatNumber', 'https://schema.org/seatNumber', [])
    object: Text

@dataclass(frozen=True)
class customerRemorseReturnFees(RdfProperty):
    term = RdfTerm('customerRemorseReturnFees', 'https://schema.org/customerRemorseReturnFees', [])
    object: schemaorg.ReturnFeesEnumeration

@dataclass(frozen=True)
class publicationType(RdfProperty):
    term = RdfTerm('publicationType', 'https://schema.org/publicationType', [])
    object: Text

@dataclass(frozen=True)
class businessFunction(RdfProperty):
    term = RdfTerm('businessFunction', 'https://schema.org/businessFunction', [])
    object: schemaorg.BusinessFunction

@dataclass(frozen=True)
class cvdNumVent(RdfProperty):
    term = RdfTerm('cvdNumVent', 'https://schema.org/cvdNumVent', [])
    object: Number

@dataclass(frozen=True)
class courseWorkload(RdfProperty):
    term = RdfTerm('courseWorkload', 'https://schema.org/courseWorkload', [])
    object: Text

@dataclass(frozen=True)
class engineDisplacement(RdfProperty):
    term = RdfTerm('engineDisplacement', 'https://schema.org/engineDisplacement', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class successorOf(RdfProperty):
    term = RdfTerm('successorOf', 'https://schema.org/successorOf', [])
    object: schemaorg.ProductModel

@dataclass(frozen=True)
class uploadDate(RdfProperty):
    term = RdfTerm('uploadDate', 'https://schema.org/uploadDate', [])
    object: Date | DateTime

@dataclass(frozen=True)
class departureBoatTerminal(RdfProperty):
    term = RdfTerm('departureBoatTerminal', 'https://schema.org/departureBoatTerminal', [])
    object: schemaorg.BoatTerminal

@dataclass(frozen=True)
class yearBuilt(RdfProperty):
    term = RdfTerm('yearBuilt', 'https://schema.org/yearBuilt', [])
    object: Number

@dataclass(frozen=True)
class amount(RdfProperty):
    term = RdfTerm('amount', 'https://schema.org/amount', [])
    object: schemaorg.MonetaryAmount | Number

@dataclass(frozen=True)
class sender(RdfProperty):
    term = RdfTerm('sender', 'https://schema.org/sender', [])
    object: schemaorg.Person | schemaorg.Audience | schemaorg.Organization

@dataclass(frozen=True)
class faxNumber(RdfProperty):
    term = RdfTerm('faxNumber', 'https://schema.org/faxNumber', [])
    object: Text

@dataclass(frozen=True)
class validForMemberTier(RdfProperty):
    term = RdfTerm('validForMemberTier', 'https://schema.org/validForMemberTier', [])
    object: schemaorg.MemberProgramTier

@dataclass(frozen=True)
class termsOfService(RdfProperty):
    term = RdfTerm('termsOfService', 'https://schema.org/termsOfService', [])
    object: Text | URL

@dataclass(frozen=True)
class fundedItem(RdfProperty):
    term = RdfTerm('fundedItem', 'https://schema.org/fundedItem', [])
    object: schemaorg.MedicalEntity | schemaorg.Product | schemaorg.CreativeWork | schemaorg.Organization | schemaorg.BioChemEntity | schemaorg.Event | schemaorg.Person

@dataclass(frozen=True)
class operatingSystem(RdfProperty):
    term = RdfTerm('operatingSystem', 'https://schema.org/operatingSystem', [])
    object: Text

@dataclass(frozen=True)
class availableStrength(RdfProperty):
    term = RdfTerm('availableStrength', 'https://schema.org/availableStrength', [])
    object: schemaorg.DrugStrength

@dataclass(frozen=True)
class functionalClass(RdfProperty):
    term = RdfTerm('functionalClass', 'https://schema.org/functionalClass', [])
    object: Text | schemaorg.MedicalEntity

@dataclass(frozen=True)
class sha256(RdfProperty):
    term = RdfTerm('sha256', 'https://schema.org/sha256', [])
    object: Text

@dataclass(frozen=True)
class domainIncludes(RdfProperty):
    term = RdfTerm('domainIncludes', 'https://schema.org/domainIncludes', [])
    object: schemaorg.Class

@dataclass(frozen=True)
class legislationApplies(RdfProperty):
    term = RdfTerm('legislationApplies', 'https://schema.org/legislationApplies', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class byMonthWeek(RdfProperty):
    term = RdfTerm('byMonthWeek', 'https://schema.org/byMonthWeek', [])
    object: Integer

@dataclass(frozen=True)
class linkRelationship(RdfProperty):
    term = RdfTerm('linkRelationship', 'https://schema.org/linkRelationship', [])
    object: Text

@dataclass(frozen=True)
class hasDeliveryMethod(RdfProperty):
    term = RdfTerm('hasDeliveryMethod', 'https://schema.org/hasDeliveryMethod', [])
    object: schemaorg.DeliveryMethod

@dataclass(frozen=True)
class departureAirport(RdfProperty):
    term = RdfTerm('departureAirport', 'https://schema.org/departureAirport', [])
    object: schemaorg.Airport

@dataclass(frozen=True)
class subTrip(RdfProperty):
    term = RdfTerm('subTrip', 'https://schema.org/subTrip', [])
    object: schemaorg.Trip

@dataclass(frozen=True)
class workFeatured(RdfProperty):
    term = RdfTerm('workFeatured', 'https://schema.org/workFeatured', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class subStructure(RdfProperty):
    term = RdfTerm('subStructure', 'https://schema.org/subStructure', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class suggestedMinAge(RdfProperty):
    term = RdfTerm('suggestedMinAge', 'https://schema.org/suggestedMinAge', [])
    object: Number

@dataclass(frozen=True)
class mpn(RdfProperty):
    term = RdfTerm('mpn', 'https://schema.org/mpn', [])
    object: Text

@dataclass(frozen=True)
class measurementQualifier(RdfProperty):
    term = RdfTerm('measurementQualifier', 'https://schema.org/measurementQualifier', [])
    object: schemaorg.Enumeration

@dataclass(frozen=True)
class assembly(RdfProperty):
    term = RdfTerm('assembly', 'https://schema.org/assembly', [])
    object: Text

@dataclass(frozen=True)
class recipeCuisine(RdfProperty):
    term = RdfTerm('recipeCuisine', 'https://schema.org/recipeCuisine', [])
    object: Text

@dataclass(frozen=True)
class certificationRating(RdfProperty):
    term = RdfTerm('certificationRating', 'https://schema.org/certificationRating', [])
    object: schemaorg.Rating

@dataclass(frozen=True)
class subStageSuffix(RdfProperty):
    term = RdfTerm('subStageSuffix', 'https://schema.org/subStageSuffix', [])
    object: Text

@dataclass(frozen=True)
class associatedMediaReview(RdfProperty):
    term = RdfTerm('associatedMediaReview', 'https://schema.org/associatedMediaReview', [])
    object: schemaorg.Review

@dataclass(frozen=True)
class availability(RdfProperty):
    term = RdfTerm('availability', 'https://schema.org/availability', [])
    object: schemaorg.ItemAvailability

@dataclass(frozen=True)
class dosageForm(RdfProperty):
    term = RdfTerm('dosageForm', 'https://schema.org/dosageForm', [])
    object: Text

@dataclass(frozen=True)
class stageAsNumber(RdfProperty):
    term = RdfTerm('stageAsNumber', 'https://schema.org/stageAsNumber', [])
    object: Number

@dataclass(frozen=True)
class shippingDetails(RdfProperty):
    term = RdfTerm('shippingDetails', 'https://schema.org/shippingDetails', [])
    object: schemaorg.OfferShippingDetails

@dataclass(frozen=True)
class cvdNumBeds(RdfProperty):
    term = RdfTerm('cvdNumBeds', 'https://schema.org/cvdNumBeds', [])
    object: Number

@dataclass(frozen=True)
class releaseDate(RdfProperty):
    term = RdfTerm('releaseDate', 'https://schema.org/releaseDate', [])
    object: Date

@dataclass(frozen=True)
class partOfSeason(RdfProperty):
    term = RdfTerm('partOfSeason', 'https://schema.org/partOfSeason', [])
    object: schemaorg.CreativeWorkSeason

@dataclass(frozen=True)
class postalCodeRange(RdfProperty):
    term = RdfTerm('postalCodeRange', 'https://schema.org/postalCodeRange', [])
    object: schemaorg.PostalCodeRangeSpecification

@dataclass(frozen=True)
class roleName(RdfProperty):
    term = RdfTerm('roleName', 'https://schema.org/roleName', [])
    object: Text | URL

@dataclass(frozen=True)
class hasTiers(RdfProperty):
    term = RdfTerm('hasTiers', 'https://schema.org/hasTiers', [])
    object: schemaorg.MemberProgramTier

@dataclass(frozen=True)
class adverseOutcome(RdfProperty):
    term = RdfTerm('adverseOutcome', 'https://schema.org/adverseOutcome', [])
    object: schemaorg.MedicalEntity

@dataclass(frozen=True)
class utterances(RdfProperty):
    term = RdfTerm('utterances', 'https://schema.org/utterances', [])
    object: Text

@dataclass(frozen=True)
class skills(RdfProperty):
    term = RdfTerm('skills', 'https://schema.org/skills', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class isAccessibleForFree(RdfProperty):
    term = RdfTerm('isAccessibleForFree', 'https://schema.org/isAccessibleForFree', [])
    object: Boolean

@dataclass(frozen=True)
class measurementDenominator(RdfProperty):
    term = RdfTerm('measurementDenominator', 'https://schema.org/measurementDenominator', [])
    object: schemaorg.StatisticalVariable

@dataclass(frozen=True)
class children(RdfProperty):
    term = RdfTerm('children', 'https://schema.org/children', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class birthDate(RdfProperty):
    term = RdfTerm('birthDate', 'https://schema.org/birthDate', [])
    object: Date

@dataclass(frozen=True)
class speakable(RdfProperty):
    term = RdfTerm('speakable', 'https://schema.org/speakable', [])
    object: schemaorg.SpeakableSpecification | URL

@dataclass(frozen=True)
class eligibleWithSupplier(RdfProperty):
    term = RdfTerm('eligibleWithSupplier', 'https://schema.org/eligibleWithSupplier', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class webFeed(RdfProperty):
    term = RdfTerm('webFeed', 'https://schema.org/webFeed', [])
    object: URL | schemaorg.DataFeed

@dataclass(frozen=True)
class characterName(RdfProperty):
    term = RdfTerm('characterName', 'https://schema.org/characterName', [])
    object: Text

@dataclass(frozen=True)
class legalName(RdfProperty):
    term = RdfTerm('legalName', 'https://schema.org/legalName', [])
    object: Text

@dataclass(frozen=True)
class sdDatePublished(RdfProperty):
    term = RdfTerm('sdDatePublished', 'https://schema.org/sdDatePublished', [])
    object: Date

@dataclass(frozen=True)
class transitTime(RdfProperty):
    term = RdfTerm('transitTime', 'https://schema.org/transitTime', [])
    object: schemaorg.ServicePeriod | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class employmentUnit(RdfProperty):
    term = RdfTerm('employmentUnit', 'https://schema.org/employmentUnit', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class quest(RdfProperty):
    term = RdfTerm('quest', 'https://schema.org/quest', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class dateDeleted(RdfProperty):
    term = RdfTerm('dateDeleted', 'https://schema.org/dateDeleted', [])
    object: Date | DateTime

@dataclass(frozen=True)
class primaryImageOfPage(RdfProperty):
    term = RdfTerm('primaryImageOfPage', 'https://schema.org/primaryImageOfPage', [])
    object: schemaorg.ImageObject

@dataclass(frozen=True)
class availableOnDevice(RdfProperty):
    term = RdfTerm('availableOnDevice', 'https://schema.org/availableOnDevice', [])
    object: Text

@dataclass(frozen=True)
class busName(RdfProperty):
    term = RdfTerm('busName', 'https://schema.org/busName', [])
    object: Text

@dataclass(frozen=True)
class itinerary(RdfProperty):
    term = RdfTerm('itinerary', 'https://schema.org/itinerary', [])
    object: schemaorg.Place | schemaorg.ItemList

@dataclass(frozen=True)
class workTranslation(RdfProperty):
    term = RdfTerm('workTranslation', 'https://schema.org/workTranslation', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class releaseNotes(RdfProperty):
    term = RdfTerm('releaseNotes', 'https://schema.org/releaseNotes', [])
    object: Text | URL

@dataclass(frozen=True)
class requiredMaxAge(RdfProperty):
    term = RdfTerm('requiredMaxAge', 'https://schema.org/requiredMaxAge', [])
    object: Integer

@dataclass(frozen=True)
class programName(RdfProperty):
    term = RdfTerm('programName', 'https://schema.org/programName', [])
    object: Text

@dataclass(frozen=True)
class bloodSupply(RdfProperty):
    term = RdfTerm('bloodSupply', 'https://schema.org/bloodSupply', [])
    object: schemaorg.Vessel

@dataclass(frozen=True)
class evidenceLevel(RdfProperty):
    term = RdfTerm('evidenceLevel', 'https://schema.org/evidenceLevel', [])
    object: schemaorg.MedicalEvidenceLevel

@dataclass(frozen=True)
class physiologicalBenefits(RdfProperty):
    term = RdfTerm('physiologicalBenefits', 'https://schema.org/physiologicalBenefits', [])
    object: Text

@dataclass(frozen=True)
class chemicalComposition(RdfProperty):
    term = RdfTerm('chemicalComposition', 'https://schema.org/chemicalComposition', [])
    object: Text

@dataclass(frozen=True)
class alumni(RdfProperty):
    term = RdfTerm('alumni', 'https://schema.org/alumni', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class hasTierRequirement(RdfProperty):
    term = RdfTerm('hasTierRequirement', 'https://schema.org/hasTierRequirement', [])
    object: schemaorg.UnitPriceSpecification | schemaorg.CreditCard | Text | schemaorg.MonetaryAmount

@dataclass(frozen=True)
class audience(RdfProperty):
    term = RdfTerm('audience', 'https://schema.org/audience', [])
    object: schemaorg.Audience

@dataclass(frozen=True)
class supersededBy(RdfProperty):
    term = RdfTerm('supersededBy', 'https://schema.org/supersededBy', [])
    object: schemaorg.Property | schemaorg.Enumeration | schemaorg.Class

@dataclass(frozen=True)
class applicationSubCategory(RdfProperty):
    term = RdfTerm('applicationSubCategory', 'https://schema.org/applicationSubCategory', [])
    object: Text | URL

@dataclass(frozen=True)
class alcoholWarning(RdfProperty):
    term = RdfTerm('alcoholWarning', 'https://schema.org/alcoholWarning', [])
    object: Text

@dataclass(frozen=True)
class position(RdfProperty):
    term = RdfTerm('position', 'https://schema.org/position', [])
    object: Text | Integer

@dataclass(frozen=True)
class recordedAt(RdfProperty):
    term = RdfTerm('recordedAt', 'https://schema.org/recordedAt', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class departureStation(RdfProperty):
    term = RdfTerm('departureStation', 'https://schema.org/departureStation', [])
    object: schemaorg.TrainStation

@dataclass(frozen=True)
class sdPublisher(RdfProperty):
    term = RdfTerm('sdPublisher', 'https://schema.org/sdPublisher', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class screenCount(RdfProperty):
    term = RdfTerm('screenCount', 'https://schema.org/screenCount', [])
    object: Number

@dataclass(frozen=True)
class actionStatus(RdfProperty):
    term = RdfTerm('actionStatus', 'https://schema.org/actionStatus', [])
    object: schemaorg.ActionStatusType

@dataclass(frozen=True)
class option(RdfProperty):
    term = RdfTerm('option', 'https://schema.org/option', [])
    object: schemaorg.Thing | Text

@dataclass(frozen=True)
class unitCode(RdfProperty):
    term = RdfTerm('unitCode', 'https://schema.org/unitCode', [])
    object: Text | URL

@dataclass(frozen=True)
class legislationJurisdiction(RdfProperty):
    term = RdfTerm('legislationJurisdiction', 'https://schema.org/legislationJurisdiction', [])
    object: Text | schemaorg.AdministrativeArea

@dataclass(frozen=True)
class makesOffer(RdfProperty):
    term = RdfTerm('makesOffer', 'https://schema.org/makesOffer', [])
    object: schemaorg.Offer

@dataclass(frozen=True)
class educationalUse(RdfProperty):
    term = RdfTerm('educationalUse', 'https://schema.org/educationalUse', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class hiringOrganization(RdfProperty):
    term = RdfTerm('hiringOrganization', 'https://schema.org/hiringOrganization', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class opponent(RdfProperty):
    term = RdfTerm('opponent', 'https://schema.org/opponent', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class subOrganization(RdfProperty):
    term = RdfTerm('subOrganization', 'https://schema.org/subOrganization', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class mediaAuthenticityCategory(RdfProperty):
    term = RdfTerm('mediaAuthenticityCategory', 'https://schema.org/mediaAuthenticityCategory', [])
    object: schemaorg.MediaManipulationRatingEnumeration

@dataclass(frozen=True)
class subEvent(RdfProperty):
    term = RdfTerm('subEvent', 'https://schema.org/subEvent', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class costCurrency(RdfProperty):
    term = RdfTerm('costCurrency', 'https://schema.org/costCurrency', [])
    object: Text

@dataclass(frozen=True)
class emissionsCO2(RdfProperty):
    term = RdfTerm('emissionsCO2', 'https://schema.org/emissionsCO2', [])
    object: Number

@dataclass(frozen=True)
class branchCode(RdfProperty):
    term = RdfTerm('branchCode', 'https://schema.org/branchCode', [])
    object: Text

@dataclass(frozen=True)
class netWorth(RdfProperty):
    term = RdfTerm('netWorth', 'https://schema.org/netWorth', [])
    object: schemaorg.MonetaryAmount | schemaorg.PriceSpecification

@dataclass(frozen=True)
class entertainmentBusiness(RdfProperty):
    term = RdfTerm('entertainmentBusiness', 'https://schema.org/entertainmentBusiness', [])
    object: schemaorg.EntertainmentBusiness

@dataclass(frozen=True)
class arrivalPlatform(RdfProperty):
    term = RdfTerm('arrivalPlatform', 'https://schema.org/arrivalPlatform', [])
    object: Text

@dataclass(frozen=True)
class track(RdfProperty):
    term = RdfTerm('track', 'https://schema.org/track', [])
    object: schemaorg.MusicRecording | schemaorg.ItemList

@dataclass(frozen=True)
class vehicleSpecialUsage(RdfProperty):
    term = RdfTerm('vehicleSpecialUsage', 'https://schema.org/vehicleSpecialUsage', [])
    object: schemaorg.CarUsageType | Text

@dataclass(frozen=True)
class sizeSystem(RdfProperty):
    term = RdfTerm('sizeSystem', 'https://schema.org/sizeSystem', [])
    object: Text | schemaorg.SizeSystemEnumeration

@dataclass(frozen=True)
class serviceType(RdfProperty):
    term = RdfTerm('serviceType', 'https://schema.org/serviceType', [])
    object: Text | schemaorg.GovernmentBenefitsType

@dataclass(frozen=True)
class isLiveBroadcast(RdfProperty):
    term = RdfTerm('isLiveBroadcast', 'https://schema.org/isLiveBroadcast', [])
    object: Boolean

@dataclass(frozen=True)
class firstAppearance(RdfProperty):
    term = RdfTerm('firstAppearance', 'https://schema.org/firstAppearance', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class numberOfItems(RdfProperty):
    term = RdfTerm('numberOfItems', 'https://schema.org/numberOfItems', [])
    object: Integer

@dataclass(frozen=True)
class typeOfGood(RdfProperty):
    term = RdfTerm('typeOfGood', 'https://schema.org/typeOfGood', [])
    object: schemaorg.Product | schemaorg.Service

@dataclass(frozen=True)
class tissueSample(RdfProperty):
    term = RdfTerm('tissueSample', 'https://schema.org/tissueSample', [])
    object: Text

@dataclass(frozen=True)
class recordLabel(RdfProperty):
    term = RdfTerm('recordLabel', 'https://schema.org/recordLabel', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class itemListElement(RdfProperty):
    term = RdfTerm('itemListElement', 'https://schema.org/itemListElement', [])
    object: schemaorg.Thing | Text | schemaorg.ListItem

@dataclass(frozen=True)
class inker(RdfProperty):
    term = RdfTerm('inker', 'https://schema.org/inker', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class musicBy(RdfProperty):
    term = RdfTerm('musicBy', 'https://schema.org/musicBy', [])
    object: schemaorg.Person | schemaorg.MusicGroup

@dataclass(frozen=True)
class correction(RdfProperty):
    term = RdfTerm('correction', 'https://schema.org/correction', [])
    object: schemaorg.CorrectionComment | Text | URL

@dataclass(frozen=True)
class deliveryTime(RdfProperty):
    term = RdfTerm('deliveryTime', 'https://schema.org/deliveryTime', [])
    object: schemaorg.ShippingDeliveryTime

@dataclass(frozen=True)
class artform(RdfProperty):
    term = RdfTerm('artform', 'https://schema.org/artform', [])
    object: Text | URL

@dataclass(frozen=True)
class wheelbase(RdfProperty):
    term = RdfTerm('wheelbase', 'https://schema.org/wheelbase', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class warranty(RdfProperty):
    term = RdfTerm('warranty', 'https://schema.org/warranty', [])
    object: schemaorg.WarrantyPromise

@dataclass(frozen=True)
class educationalCredentialAwarded(RdfProperty):
    term = RdfTerm('educationalCredentialAwarded', 'https://schema.org/educationalCredentialAwarded', [])
    object: Text | URL | schemaorg.EducationalOccupationalCredential

@dataclass(frozen=True)
class mechanismOfAction(RdfProperty):
    term = RdfTerm('mechanismOfAction', 'https://schema.org/mechanismOfAction', [])
    object: Text

@dataclass(frozen=True)
class hasMeasurement(RdfProperty):
    term = RdfTerm('hasMeasurement', 'https://schema.org/hasMeasurement', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class embedUrl(RdfProperty):
    term = RdfTerm('embedUrl', 'https://schema.org/embedUrl', [])
    object: URL

@dataclass(frozen=True)
class frequency(RdfProperty):
    term = RdfTerm('frequency', 'https://schema.org/frequency', [])
    object: Text

@dataclass(frozen=True)
class availableService(RdfProperty):
    term = RdfTerm('availableService', 'https://schema.org/availableService', [])
    object: schemaorg.MedicalProcedure | schemaorg.MedicalTest | schemaorg.MedicalTherapy

@dataclass(frozen=True)
class healthPlanNetworkId(RdfProperty):
    term = RdfTerm('healthPlanNetworkId', 'https://schema.org/healthPlanNetworkId', [])
    object: Text

@dataclass(frozen=True)
class model(RdfProperty):
    term = RdfTerm('model', 'https://schema.org/model', [])
    object: Text | schemaorg.ProductModel

@dataclass(frozen=True)
class itemShipped(RdfProperty):
    term = RdfTerm('itemShipped', 'https://schema.org/itemShipped', [])
    object: schemaorg.Product

@dataclass(frozen=True)
class closes(RdfProperty):
    term = RdfTerm('closes', 'https://schema.org/closes', [])
    object: Time

@dataclass(frozen=True)
class screenshot(RdfProperty):
    term = RdfTerm('screenshot', 'https://schema.org/screenshot', [])
    object: URL | schemaorg.ImageObject

@dataclass(frozen=True)
class webCheckinTime(RdfProperty):
    term = RdfTerm('webCheckinTime', 'https://schema.org/webCheckinTime', [])
    object: DateTime

@dataclass(frozen=True)
class collectionSize(RdfProperty):
    term = RdfTerm('collectionSize', 'https://schema.org/collectionSize', [])
    object: Integer

@dataclass(frozen=True)
class mainEntityOfPage(RdfProperty):
    term = RdfTerm('mainEntityOfPage', 'https://schema.org/mainEntityOfPage', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class energyEfficiencyScaleMin(RdfProperty):
    term = RdfTerm('energyEfficiencyScaleMin', 'https://schema.org/energyEfficiencyScaleMin', [])
    object: schemaorg.EUEnergyEfficiencyEnumeration

@dataclass(frozen=True)
class loanRepaymentForm(RdfProperty):
    term = RdfTerm('loanRepaymentForm', 'https://schema.org/loanRepaymentForm', [])
    object: schemaorg.RepaymentSpecification

@dataclass(frozen=True)
class purchaseDate(RdfProperty):
    term = RdfTerm('purchaseDate', 'https://schema.org/purchaseDate', [])
    object: Date

@dataclass(frozen=True)
class datasetTimeInterval(RdfProperty):
    term = RdfTerm('datasetTimeInterval', 'https://schema.org/datasetTimeInterval', [])
    object: DateTime

@dataclass(frozen=True)
class healthPlanId(RdfProperty):
    term = RdfTerm('healthPlanId', 'https://schema.org/healthPlanId', [])
    object: Text

@dataclass(frozen=True)
class inPlaylist(RdfProperty):
    term = RdfTerm('inPlaylist', 'https://schema.org/inPlaylist', [])
    object: schemaorg.MusicPlaylist

@dataclass(frozen=True)
class healthPlanCopayOption(RdfProperty):
    term = RdfTerm('healthPlanCopayOption', 'https://schema.org/healthPlanCopayOption', [])
    object: Text

@dataclass(frozen=True)
class acceptedPaymentMethod(RdfProperty):
    term = RdfTerm('acceptedPaymentMethod', 'https://schema.org/acceptedPaymentMethod', [])
    object: Text | schemaorg.PaymentMethod | schemaorg.LoanOrCredit

@dataclass(frozen=True)
class printSection(RdfProperty):
    term = RdfTerm('printSection', 'https://schema.org/printSection', [])
    object: Text

@dataclass(frozen=True)
class inSupportOf(RdfProperty):
    term = RdfTerm('inSupportOf', 'https://schema.org/inSupportOf', [])
    object: Text

@dataclass(frozen=True)
class callSign(RdfProperty):
    term = RdfTerm('callSign', 'https://schema.org/callSign', [])
    object: Text

@dataclass(frozen=True)
class securityClearanceRequirement(RdfProperty):
    term = RdfTerm('securityClearanceRequirement', 'https://schema.org/securityClearanceRequirement', [])
    object: Text | URL

@dataclass(frozen=True)
class costCategory(RdfProperty):
    term = RdfTerm('costCategory', 'https://schema.org/costCategory', [])
    object: schemaorg.DrugCostCategory

@dataclass(frozen=True)
class contentSize(RdfProperty):
    term = RdfTerm('contentSize', 'https://schema.org/contentSize', [])
    object: Text

@dataclass(frozen=True)
class accessModeSufficient(RdfProperty):
    term = RdfTerm('accessModeSufficient', 'https://schema.org/accessModeSufficient', [])
    object: schemaorg.ItemList

@dataclass(frozen=True)
class healthPlanCopay(RdfProperty):
    term = RdfTerm('healthPlanCopay', 'https://schema.org/healthPlanCopay', [])
    object: schemaorg.PriceSpecification

@dataclass(frozen=True)
class reservationFor(RdfProperty):
    term = RdfTerm('reservationFor', 'https://schema.org/reservationFor', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class availableThrough(RdfProperty):
    term = RdfTerm('availableThrough', 'https://schema.org/availableThrough', [])
    object: DateTime

@dataclass(frozen=True)
class antagonist(RdfProperty):
    term = RdfTerm('antagonist', 'https://schema.org/antagonist', [])
    object: schemaorg.Muscle

@dataclass(frozen=True)
class cvdNumC19OFMechVentPats(RdfProperty):
    term = RdfTerm('cvdNumC19OFMechVentPats', 'https://schema.org/cvdNumC19OFMechVentPats', [])
    object: Number

@dataclass(frozen=True)
class editEIDR(RdfProperty):
    term = RdfTerm('editEIDR', 'https://schema.org/editEIDR', [])
    object: Text | URL

@dataclass(frozen=True)
class hasCredential(RdfProperty):
    term = RdfTerm('hasCredential', 'https://schema.org/hasCredential', [])
    object: schemaorg.EducationalOccupationalCredential

@dataclass(frozen=True)
class annualPercentageRate(RdfProperty):
    term = RdfTerm('annualPercentageRate', 'https://schema.org/annualPercentageRate', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class accommodationCategory(RdfProperty):
    term = RdfTerm('accommodationCategory', 'https://schema.org/accommodationCategory', [])
    object: Text

@dataclass(frozen=True)
class productReturnLink(RdfProperty):
    term = RdfTerm('productReturnLink', 'https://schema.org/productReturnLink', [])
    object: URL

@dataclass(frozen=True)
class orderedItem(RdfProperty):
    term = RdfTerm('orderedItem', 'https://schema.org/orderedItem', [])
    object: schemaorg.Service | schemaorg.OrderItem | schemaorg.Product

@dataclass(frozen=True)
class deliveryStatus(RdfProperty):
    term = RdfTerm('deliveryStatus', 'https://schema.org/deliveryStatus', [])
    object: schemaorg.DeliveryEvent

@dataclass(frozen=True)
class actionPlatform(RdfProperty):
    term = RdfTerm('actionPlatform', 'https://schema.org/actionPlatform', [])
    object: URL | Text | schemaorg.DigitalPlatformEnumeration

@dataclass(frozen=True)
class variesBy(RdfProperty):
    term = RdfTerm('variesBy', 'https://schema.org/variesBy', [])
    object: Text | schemaorg.DefinedTerm

@dataclass(frozen=True)
class tracks(RdfProperty):
    term = RdfTerm('tracks', 'https://schema.org/tracks', [])
    object: schemaorg.MusicRecording

@dataclass(frozen=True)
class recipeCategory(RdfProperty):
    term = RdfTerm('recipeCategory', 'https://schema.org/recipeCategory', [])
    object: Text

@dataclass(frozen=True)
class recourseLoan(RdfProperty):
    term = RdfTerm('recourseLoan', 'https://schema.org/recourseLoan', [])
    object: Boolean

@dataclass(frozen=True)
class doesNotShip(RdfProperty):
    term = RdfTerm('doesNotShip', 'https://schema.org/doesNotShip', [])
    object: Boolean

@dataclass(frozen=True)
class deliveryLeadTime(RdfProperty):
    term = RdfTerm('deliveryLeadTime', 'https://schema.org/deliveryLeadTime', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class numTracks(RdfProperty):
    term = RdfTerm('numTracks', 'https://schema.org/numTracks', [])
    object: Integer

@dataclass(frozen=True)
class tourBookingPage(RdfProperty):
    term = RdfTerm('tourBookingPage', 'https://schema.org/tourBookingPage', [])
    object: URL

@dataclass(frozen=True)
class itemDefectReturnShippingFeesAmount(RdfProperty):
    term = RdfTerm('itemDefectReturnShippingFeesAmount', 'https://schema.org/itemDefectReturnShippingFeesAmount', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class codingSystem(RdfProperty):
    term = RdfTerm('codingSystem', 'https://schema.org/codingSystem', [])
    object: Text

@dataclass(frozen=True)
class validFor(RdfProperty):
    term = RdfTerm('validFor', 'https://schema.org/validFor', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class prescribingInfo(RdfProperty):
    term = RdfTerm('prescribingInfo', 'https://schema.org/prescribingInfo', [])
    object: URL

@dataclass(frozen=True)
class recipeIngredient(RdfProperty):
    term = RdfTerm('recipeIngredient', 'https://schema.org/recipeIngredient', [])
    object: Text

@dataclass(frozen=True)
class usedToDiagnose(RdfProperty):
    term = RdfTerm('usedToDiagnose', 'https://schema.org/usedToDiagnose', [])
    object: schemaorg.MedicalCondition

@dataclass(frozen=True)
class biomechnicalClass(RdfProperty):
    term = RdfTerm('biomechnicalClass', 'https://schema.org/biomechnicalClass', [])
    object: Text

@dataclass(frozen=True)
class administrationRoute(RdfProperty):
    term = RdfTerm('administrationRoute', 'https://schema.org/administrationRoute', [])
    object: Text

@dataclass(frozen=True)
class amenityFeature(RdfProperty):
    term = RdfTerm('amenityFeature', 'https://schema.org/amenityFeature', [])
    object: schemaorg.LocationFeatureSpecification

@dataclass(frozen=True)
class follows(RdfProperty):
    term = RdfTerm('follows', 'https://schema.org/follows', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class lyrics(RdfProperty):
    term = RdfTerm('lyrics', 'https://schema.org/lyrics', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class departurePlatform(RdfProperty):
    term = RdfTerm('departurePlatform', 'https://schema.org/departurePlatform', [])
    object: Text

@dataclass(frozen=True)
class holdingArchive(RdfProperty):
    term = RdfTerm('holdingArchive', 'https://schema.org/holdingArchive', [])
    object: schemaorg.ArchiveOrganization

@dataclass(frozen=True)
class availableLanguage(RdfProperty):
    term = RdfTerm('availableLanguage', 'https://schema.org/availableLanguage', [])
    object: Text | schemaorg.Language

@dataclass(frozen=True)
class comment(RdfProperty):
    term = RdfTerm('comment', 'https://schema.org/comment', [])
    object: schemaorg.Comment

@dataclass(frozen=True)
class endorsee(RdfProperty):
    term = RdfTerm('endorsee', 'https://schema.org/endorsee', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class reservationStatus(RdfProperty):
    term = RdfTerm('reservationStatus', 'https://schema.org/reservationStatus', [])
    object: schemaorg.ReservationStatusType

@dataclass(frozen=True)
class legislationDateOfApplicability(RdfProperty):
    term = RdfTerm('legislationDateOfApplicability', 'https://schema.org/legislationDateOfApplicability', [])
    object: Date

@dataclass(frozen=True)
class maxValue(RdfProperty):
    term = RdfTerm('maxValue', 'https://schema.org/maxValue', [])
    object: Number

@dataclass(frozen=True)
class accountablePerson(RdfProperty):
    term = RdfTerm('accountablePerson', 'https://schema.org/accountablePerson', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class identifier(RdfProperty):
    term = RdfTerm('identifier', 'https://schema.org/identifier', [])
    object: schemaorg.PropertyValue | Text | URL

@dataclass(frozen=True)
class lender(RdfProperty):
    term = RdfTerm('lender', 'https://schema.org/lender', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class logo(RdfProperty):
    term = RdfTerm('logo', 'https://schema.org/logo', [])
    object: URL | schemaorg.ImageObject

@dataclass(frozen=True)
class broadcastFrequencyValue(RdfProperty):
    term = RdfTerm('broadcastFrequencyValue', 'https://schema.org/broadcastFrequencyValue', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class constraintProperty(RdfProperty):
    term = RdfTerm('constraintProperty', 'https://schema.org/constraintProperty', [])
    object: schemaorg.Property | URL

@dataclass(frozen=True)
class additionalType(RdfProperty):
    term = RdfTerm('additionalType', 'https://schema.org/additionalType', [])
    object: Text | URL

@dataclass(frozen=True)
class occupationLocation(RdfProperty):
    term = RdfTerm('occupationLocation', 'https://schema.org/occupationLocation', [])
    object: schemaorg.AdministrativeArea

@dataclass(frozen=True)
class streetAddress(RdfProperty):
    term = RdfTerm('streetAddress', 'https://schema.org/streetAddress', [])
    object: Text

@dataclass(frozen=True)
class specialty(RdfProperty):
    term = RdfTerm('specialty', 'https://schema.org/specialty', [])
    object: schemaorg.Specialty

@dataclass(frozen=True)
class percentile10(RdfProperty):
    term = RdfTerm('percentile10', 'https://schema.org/percentile10', [])
    object: Number

@dataclass(frozen=True)
class gameLocation(RdfProperty):
    term = RdfTerm('gameLocation', 'https://schema.org/gameLocation', [])
    object: URL | schemaorg.PostalAddress | schemaorg.Place

@dataclass(frozen=True)
class industry(RdfProperty):
    term = RdfTerm('industry', 'https://schema.org/industry', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class codeSampleType(RdfProperty):
    term = RdfTerm('codeSampleType', 'https://schema.org/codeSampleType', [])
    object: Text

@dataclass(frozen=True)
class permissions(RdfProperty):
    term = RdfTerm('permissions', 'https://schema.org/permissions', [])
    object: Text

@dataclass(frozen=True)
class specialOpeningHoursSpecification(RdfProperty):
    term = RdfTerm('specialOpeningHoursSpecification', 'https://schema.org/specialOpeningHoursSpecification', [])
    object: schemaorg.OpeningHoursSpecification

@dataclass(frozen=True)
class loanPaymentAmount(RdfProperty):
    term = RdfTerm('loanPaymentAmount', 'https://schema.org/loanPaymentAmount', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class observationPeriod(RdfProperty):
    term = RdfTerm('observationPeriod', 'https://schema.org/observationPeriod', [])
    object: Text

@dataclass(frozen=True)
class nerve(RdfProperty):
    term = RdfTerm('nerve', 'https://schema.org/nerve', [])
    object: schemaorg.Nerve

@dataclass(frozen=True)
class artworkSurface(RdfProperty):
    term = RdfTerm('artworkSurface', 'https://schema.org/artworkSurface', [])
    object: Text | URL

@dataclass(frozen=True)
class alternativeOf(RdfProperty):
    term = RdfTerm('alternativeOf', 'https://schema.org/alternativeOf', [])
    object: schemaorg.Gene

@dataclass(frozen=True)
class scheduledTime(RdfProperty):
    term = RdfTerm('scheduledTime', 'https://schema.org/scheduledTime', [])
    object: Date | DateTime

@dataclass(frozen=True)
class ticketToken(RdfProperty):
    term = RdfTerm('ticketToken', 'https://schema.org/ticketToken', [])
    object: Text | URL

@dataclass(frozen=True)
class contactOption(RdfProperty):
    term = RdfTerm('contactOption', 'https://schema.org/contactOption', [])
    object: schemaorg.ContactPointOption

@dataclass(frozen=True)
class datePublished(RdfProperty):
    term = RdfTerm('datePublished', 'https://schema.org/datePublished', [])
    object: Date | DateTime

@dataclass(frozen=True)
class cvdNumC19MechVentPats(RdfProperty):
    term = RdfTerm('cvdNumC19MechVentPats', 'https://schema.org/cvdNumC19MechVentPats', [])
    object: Number

@dataclass(frozen=True)
class seller(RdfProperty):
    term = RdfTerm('seller', 'https://schema.org/seller', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class reviewCount(RdfProperty):
    term = RdfTerm('reviewCount', 'https://schema.org/reviewCount', [])
    object: Integer

@dataclass(frozen=True)
class cvdNumICUBedsOcc(RdfProperty):
    term = RdfTerm('cvdNumICUBedsOcc', 'https://schema.org/cvdNumICUBedsOcc', [])
    object: Number

@dataclass(frozen=True)
class issn(RdfProperty):
    term = RdfTerm('issn', 'https://schema.org/issn', [])
    object: Text

@dataclass(frozen=True)
class transitTimeLabel(RdfProperty):
    term = RdfTerm('transitTimeLabel', 'https://schema.org/transitTimeLabel', [])
    object: Text

@dataclass(frozen=True)
class childTaxon(RdfProperty):
    term = RdfTerm('childTaxon', 'https://schema.org/childTaxon', [])
    object: Text | URL | schemaorg.Taxon

@dataclass(frozen=True)
class sugarContent(RdfProperty):
    term = RdfTerm('sugarContent', 'https://schema.org/sugarContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class nextItem(RdfProperty):
    term = RdfTerm('nextItem', 'https://schema.org/nextItem', [])
    object: schemaorg.ListItem

@dataclass(frozen=True)
class foodEvent(RdfProperty):
    term = RdfTerm('foodEvent', 'https://schema.org/foodEvent', [])
    object: schemaorg.FoodEvent

@dataclass(frozen=True)
class inProductGroupWithID(RdfProperty):
    term = RdfTerm('inProductGroupWithID', 'https://schema.org/inProductGroupWithID', [])
    object: Text

@dataclass(frozen=True)
class numberOfForwardGears(RdfProperty):
    term = RdfTerm('numberOfForwardGears', 'https://schema.org/numberOfForwardGears', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class recognizedBy(RdfProperty):
    term = RdfTerm('recognizedBy', 'https://schema.org/recognizedBy', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class arrivalTime(RdfProperty):
    term = RdfTerm('arrivalTime', 'https://schema.org/arrivalTime', [])
    object: DateTime | Time

@dataclass(frozen=True)
class material(RdfProperty):
    term = RdfTerm('material', 'https://schema.org/material', [])
    object: schemaorg.Product | Text | URL

@dataclass(frozen=True)
class valueReference(RdfProperty):
    term = RdfTerm('valueReference', 'https://schema.org/valueReference', [])
    object: schemaorg.PropertyValue | schemaorg.StructuredValue | Text | schemaorg.Enumeration | schemaorg.QualitativeValue | schemaorg.MeasurementTypeEnumeration | schemaorg.QuantitativeValue | schemaorg.DefinedTerm

@dataclass(frozen=True)
class commentCount(RdfProperty):
    term = RdfTerm('commentCount', 'https://schema.org/commentCount', [])
    object: Integer

@dataclass(frozen=True)
class codeRepository(RdfProperty):
    term = RdfTerm('codeRepository', 'https://schema.org/codeRepository', [])
    object: URL

@dataclass(frozen=True)
class sourceOrganization(RdfProperty):
    term = RdfTerm('sourceOrganization', 'https://schema.org/sourceOrganization', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class naics(RdfProperty):
    term = RdfTerm('naics', 'https://schema.org/naics', [])
    object: Text

@dataclass(frozen=True)
class shippingSettingsLink(RdfProperty):
    term = RdfTerm('shippingSettingsLink', 'https://schema.org/shippingSettingsLink', [])
    object: URL

@dataclass(frozen=True)
class headline(RdfProperty):
    term = RdfTerm('headline', 'https://schema.org/headline', [])
    object: Text

@dataclass(frozen=True)
class foodEstablishment(RdfProperty):
    term = RdfTerm('foodEstablishment', 'https://schema.org/foodEstablishment', [])
    object: schemaorg.FoodEstablishment | schemaorg.Place

@dataclass(frozen=True)
class gender(RdfProperty):
    term = RdfTerm('gender', 'https://schema.org/gender', [])
    object: Text | schemaorg.GenderType

@dataclass(frozen=True)
class endDate(RdfProperty):
    term = RdfTerm('endDate', 'https://schema.org/endDate', [])
    object: Date | DateTime

@dataclass(frozen=True)
class letterer(RdfProperty):
    term = RdfTerm('letterer', 'https://schema.org/letterer', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class itemReviewed(RdfProperty):
    term = RdfTerm('itemReviewed', 'https://schema.org/itemReviewed', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class targetPlatform(RdfProperty):
    term = RdfTerm('targetPlatform', 'https://schema.org/targetPlatform', [])
    object: Text

@dataclass(frozen=True)
class suggestedGender(RdfProperty):
    term = RdfTerm('suggestedGender', 'https://schema.org/suggestedGender', [])
    object: Text | schemaorg.GenderType

@dataclass(frozen=True)
class percentile75(RdfProperty):
    term = RdfTerm('percentile75', 'https://schema.org/percentile75', [])
    object: Number

@dataclass(frozen=True)
class doorTime(RdfProperty):
    term = RdfTerm('doorTime', 'https://schema.org/doorTime', [])
    object: DateTime | Time

@dataclass(frozen=True)
class priceSpecification(RdfProperty):
    term = RdfTerm('priceSpecification', 'https://schema.org/priceSpecification', [])
    object: schemaorg.PriceSpecification

@dataclass(frozen=True)
class numberOfPartialBathrooms(RdfProperty):
    term = RdfTerm('numberOfPartialBathrooms', 'https://schema.org/numberOfPartialBathrooms', [])
    object: Number

@dataclass(frozen=True)
class colleagues(RdfProperty):
    term = RdfTerm('colleagues', 'https://schema.org/colleagues', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class interestRate(RdfProperty):
    term = RdfTerm('interestRate', 'https://schema.org/interestRate', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class vehicleModelDate(RdfProperty):
    term = RdfTerm('vehicleModelDate', 'https://schema.org/vehicleModelDate', [])
    object: Date

@dataclass(frozen=True)
class businessDays(RdfProperty):
    term = RdfTerm('businessDays', 'https://schema.org/businessDays', [])
    object: schemaorg.DayOfWeek | schemaorg.OpeningHoursSpecification

@dataclass(frozen=True)
class sport(RdfProperty):
    term = RdfTerm('sport', 'https://schema.org/sport', [])
    object: Text | URL

@dataclass(frozen=True)
class dateCreated(RdfProperty):
    term = RdfTerm('dateCreated', 'https://schema.org/dateCreated', [])
    object: Date | DateTime

@dataclass(frozen=True)
class broadcastServiceTier(RdfProperty):
    term = RdfTerm('broadcastServiceTier', 'https://schema.org/broadcastServiceTier', [])
    object: Text

@dataclass(frozen=True)
class repeatFrequency(RdfProperty):
    term = RdfTerm('repeatFrequency', 'https://schema.org/repeatFrequency', [])
    object: schemaorg.Duration | Text

@dataclass(frozen=True)
class arrivalGate(RdfProperty):
    term = RdfTerm('arrivalGate', 'https://schema.org/arrivalGate', [])
    object: Text

@dataclass(frozen=True)
class increasesRiskOf(RdfProperty):
    term = RdfTerm('increasesRiskOf', 'https://schema.org/increasesRiskOf', [])
    object: schemaorg.MedicalEntity

@dataclass(frozen=True)
class namedPosition(RdfProperty):
    term = RdfTerm('namedPosition', 'https://schema.org/namedPosition', [])
    object: Text | URL

@dataclass(frozen=True)
class answerExplanation(RdfProperty):
    term = RdfTerm('answerExplanation', 'https://schema.org/answerExplanation', [])
    object: schemaorg.Comment | schemaorg.WebContent

@dataclass(frozen=True)
class workHours(RdfProperty):
    term = RdfTerm('workHours', 'https://schema.org/workHours', [])
    object: Text

@dataclass(frozen=True)
class newsUpdatesAndGuidelines(RdfProperty):
    term = RdfTerm('newsUpdatesAndGuidelines', 'https://schema.org/newsUpdatesAndGuidelines', [])
    object: schemaorg.WebContent | URL

@dataclass(frozen=True)
class geoTouches(RdfProperty):
    term = RdfTerm('geoTouches', 'https://schema.org/geoTouches', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class competitor(RdfProperty):
    term = RdfTerm('competitor', 'https://schema.org/competitor', [])
    object: schemaorg.SportsTeam | schemaorg.Person

@dataclass(frozen=True)
class targetProduct(RdfProperty):
    term = RdfTerm('targetProduct', 'https://schema.org/targetProduct', [])
    object: schemaorg.SoftwareApplication

@dataclass(frozen=True)
class lodgingUnitDescription(RdfProperty):
    term = RdfTerm('lodgingUnitDescription', 'https://schema.org/lodgingUnitDescription', [])
    object: Text

@dataclass(frozen=True)
class providerMobility(RdfProperty):
    term = RdfTerm('providerMobility', 'https://schema.org/providerMobility', [])
    object: Text

@dataclass(frozen=True)
class duringMedia(RdfProperty):
    term = RdfTerm('duringMedia', 'https://schema.org/duringMedia', [])
    object: schemaorg.MediaObject | URL

@dataclass(frozen=True)
class masthead(RdfProperty):
    term = RdfTerm('masthead', 'https://schema.org/masthead', [])
    object: URL | schemaorg.CreativeWork

@dataclass(frozen=True)
class availableAtOrFrom(RdfProperty):
    term = RdfTerm('availableAtOrFrom', 'https://schema.org/availableAtOrFrom', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class programmingModel(RdfProperty):
    term = RdfTerm('programmingModel', 'https://schema.org/programmingModel', [])
    object: Text

@dataclass(frozen=True)
class embeddedTextCaption(RdfProperty):
    term = RdfTerm('embeddedTextCaption', 'https://schema.org/embeddedTextCaption', [])
    object: Text

@dataclass(frozen=True)
class hasMenuSection(RdfProperty):
    term = RdfTerm('hasMenuSection', 'https://schema.org/hasMenuSection', [])
    object: schemaorg.MenuSection

@dataclass(frozen=True)
class nationality(RdfProperty):
    term = RdfTerm('nationality', 'https://schema.org/nationality', [])
    object: schemaorg.Country

@dataclass(frozen=True)
class steps(RdfProperty):
    term = RdfTerm('steps', 'https://schema.org/steps', [])
    object: schemaorg.ItemList | schemaorg.CreativeWork | Text

@dataclass(frozen=True)
class noBylinesPolicy(RdfProperty):
    term = RdfTerm('noBylinesPolicy', 'https://schema.org/noBylinesPolicy', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class timeRequired(RdfProperty):
    term = RdfTerm('timeRequired', 'https://schema.org/timeRequired', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class areaServed(RdfProperty):
    term = RdfTerm('areaServed', 'https://schema.org/areaServed', [])
    object: schemaorg.AdministrativeArea | Text | schemaorg.GeoShape | schemaorg.Place

@dataclass(frozen=True)
class superEvent(RdfProperty):
    term = RdfTerm('superEvent', 'https://schema.org/superEvent', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class sportsActivityLocation(RdfProperty):
    term = RdfTerm('sportsActivityLocation', 'https://schema.org/sportsActivityLocation', [])
    object: schemaorg.SportsActivityLocation

@dataclass(frozen=True)
class hasOccupation(RdfProperty):
    term = RdfTerm('hasOccupation', 'https://schema.org/hasOccupation', [])
    object: schemaorg.Occupation

@dataclass(frozen=True)
class baseSalary(RdfProperty):
    term = RdfTerm('baseSalary', 'https://schema.org/baseSalary', [])
    object: schemaorg.PriceSpecification | schemaorg.MonetaryAmount | Number

@dataclass(frozen=True)
class founders(RdfProperty):
    term = RdfTerm('founders', 'https://schema.org/founders', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class claimInterpreter(RdfProperty):
    term = RdfTerm('claimInterpreter', 'https://schema.org/claimInterpreter', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class quarantineGuidelines(RdfProperty):
    term = RdfTerm('quarantineGuidelines', 'https://schema.org/quarantineGuidelines', [])
    object: URL | schemaorg.WebContent

@dataclass(frozen=True)
class price(RdfProperty):
    term = RdfTerm('price', 'https://schema.org/price', [])
    object: Text | Number

@dataclass(frozen=True)
class location(RdfProperty):
    term = RdfTerm('location', 'https://schema.org/location', [])
    object: Text | schemaorg.Place | schemaorg.PostalAddress | schemaorg.VirtualLocation

@dataclass(frozen=True)
class artEdition(RdfProperty):
    term = RdfTerm('artEdition', 'https://schema.org/artEdition', [])
    object: Text | Integer

@dataclass(frozen=True)
class petsAllowed(RdfProperty):
    term = RdfTerm('petsAllowed', 'https://schema.org/petsAllowed', [])
    object: Boolean | Text

@dataclass(frozen=True)
class endorsers(RdfProperty):
    term = RdfTerm('endorsers', 'https://schema.org/endorsers', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class affiliation(RdfProperty):
    term = RdfTerm('affiliation', 'https://schema.org/affiliation', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class dissolutionDate(RdfProperty):
    term = RdfTerm('dissolutionDate', 'https://schema.org/dissolutionDate', [])
    object: Date

@dataclass(frozen=True)
class isBasedOn(RdfProperty):
    term = RdfTerm('isBasedOn', 'https://schema.org/isBasedOn', [])
    object: schemaorg.Product | schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class employee(RdfProperty):
    term = RdfTerm('employee', 'https://schema.org/employee', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class hasProductReturnPolicy(RdfProperty):
    term = RdfTerm('hasProductReturnPolicy', 'https://schema.org/hasProductReturnPolicy', [])
    object: schemaorg.ProductReturnPolicy

@dataclass(frozen=True)
class syllabusSections(RdfProperty):
    term = RdfTerm('syllabusSections', 'https://schema.org/syllabusSections', [])
    object: schemaorg.Syllabus

@dataclass(frozen=True)
class ratingValue(RdfProperty):
    term = RdfTerm('ratingValue', 'https://schema.org/ratingValue', [])
    object: Text | Number

@dataclass(frozen=True)
class meetsEmissionStandard(RdfProperty):
    term = RdfTerm('meetsEmissionStandard', 'https://schema.org/meetsEmissionStandard', [])
    object: Text | URL | schemaorg.QualitativeValue

@dataclass(frozen=True)
class acrissCode(RdfProperty):
    term = RdfTerm('acrissCode', 'https://schema.org/acrissCode', [])
    object: Text

@dataclass(frozen=True)
class knowsLanguage(RdfProperty):
    term = RdfTerm('knowsLanguage', 'https://schema.org/knowsLanguage', [])
    object: Text | schemaorg.Language

@dataclass(frozen=True)
class hasCategoryCode(RdfProperty):
    term = RdfTerm('hasCategoryCode', 'https://schema.org/hasCategoryCode', [])
    object: schemaorg.CategoryCode

@dataclass(frozen=True)
class athlete(RdfProperty):
    term = RdfTerm('athlete', 'https://schema.org/athlete', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class maps(RdfProperty):
    term = RdfTerm('maps', 'https://schema.org/maps', [])
    object: URL

@dataclass(frozen=True)
class targetPopulation(RdfProperty):
    term = RdfTerm('targetPopulation', 'https://schema.org/targetPopulation', [])
    object: Text

@dataclass(frozen=True)
class commentTime(RdfProperty):
    term = RdfTerm('commentTime', 'https://schema.org/commentTime', [])
    object: Date | DateTime

@dataclass(frozen=True)
class broadcaster(RdfProperty):
    term = RdfTerm('broadcaster', 'https://schema.org/broadcaster', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class actionProcess(RdfProperty):
    term = RdfTerm('actionProcess', 'https://schema.org/actionProcess', [])
    object: schemaorg.HowTo

@dataclass(frozen=True)
class isTierOf(RdfProperty):
    term = RdfTerm('isTierOf', 'https://schema.org/isTierOf', [])
    object: schemaorg.MemberProgram

@dataclass(frozen=True)
class broadcastDisplayName(RdfProperty):
    term = RdfTerm('broadcastDisplayName', 'https://schema.org/broadcastDisplayName', [])
    object: Text

@dataclass(frozen=True)
class causeOf(RdfProperty):
    term = RdfTerm('causeOf', 'https://schema.org/causeOf', [])
    object: schemaorg.MedicalEntity

@dataclass(frozen=True)
class salaryUponCompletion(RdfProperty):
    term = RdfTerm('salaryUponCompletion', 'https://schema.org/salaryUponCompletion', [])
    object: schemaorg.MonetaryAmountDistribution

@dataclass(frozen=True)
class hasEnergyConsumptionDetails(RdfProperty):
    term = RdfTerm('hasEnergyConsumptionDetails', 'https://schema.org/hasEnergyConsumptionDetails', [])
    object: schemaorg.EnergyConsumptionDetails

@dataclass(frozen=True)
class landlord(RdfProperty):
    term = RdfTerm('landlord', 'https://schema.org/landlord', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class relatedDrug(RdfProperty):
    term = RdfTerm('relatedDrug', 'https://schema.org/relatedDrug', [])
    object: schemaorg.Drug

@dataclass(frozen=True)
class latitude(RdfProperty):
    term = RdfTerm('latitude', 'https://schema.org/latitude', [])
    object: Text | Number

@dataclass(frozen=True)
class suggestedAnswer(RdfProperty):
    term = RdfTerm('suggestedAnswer', 'https://schema.org/suggestedAnswer', [])
    object: schemaorg.ItemList | schemaorg.Answer

@dataclass(frozen=True)
class partOfOrder(RdfProperty):
    term = RdfTerm('partOfOrder', 'https://schema.org/partOfOrder', [])
    object: schemaorg.Order

@dataclass(frozen=True)
class monoisotopicMolecularWeight(RdfProperty):
    term = RdfTerm('monoisotopicMolecularWeight', 'https://schema.org/monoisotopicMolecularWeight', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class instructor(RdfProperty):
    term = RdfTerm('instructor', 'https://schema.org/instructor', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class exchangeRateSpread(RdfProperty):
    term = RdfTerm('exchangeRateSpread', 'https://schema.org/exchangeRateSpread', [])
    object: schemaorg.MonetaryAmount | Number

@dataclass(frozen=True)
class feesAndCommissionsSpecification(RdfProperty):
    term = RdfTerm('feesAndCommissionsSpecification', 'https://schema.org/feesAndCommissionsSpecification', [])
    object: Text | URL

@dataclass(frozen=True)
class serverStatus(RdfProperty):
    term = RdfTerm('serverStatus', 'https://schema.org/serverStatus', [])
    object: schemaorg.GameServerStatus

@dataclass(frozen=True)
class requiredMinAge(RdfProperty):
    term = RdfTerm('requiredMinAge', 'https://schema.org/requiredMinAge', [])
    object: Integer

@dataclass(frozen=True)
class identifyingTest(RdfProperty):
    term = RdfTerm('identifyingTest', 'https://schema.org/identifyingTest', [])
    object: schemaorg.MedicalTest

@dataclass(frozen=True)
class differentialDiagnosis(RdfProperty):
    term = RdfTerm('differentialDiagnosis', 'https://schema.org/differentialDiagnosis', [])
    object: schemaorg.DDxElement

@dataclass(frozen=True)
class orderNumber(RdfProperty):
    term = RdfTerm('orderNumber', 'https://schema.org/orderNumber', [])
    object: Text

@dataclass(frozen=True)
class conditionsOfAccess(RdfProperty):
    term = RdfTerm('conditionsOfAccess', 'https://schema.org/conditionsOfAccess', [])
    object: Text

@dataclass(frozen=True)
class codeValue(RdfProperty):
    term = RdfTerm('codeValue', 'https://schema.org/codeValue', [])
    object: Text

@dataclass(frozen=True)
class installUrl(RdfProperty):
    term = RdfTerm('installUrl', 'https://schema.org/installUrl', [])
    object: URL

@dataclass(frozen=True)
class sensoryRequirement(RdfProperty):
    term = RdfTerm('sensoryRequirement', 'https://schema.org/sensoryRequirement', [])
    object: schemaorg.DefinedTerm | Text | URL

@dataclass(frozen=True)
class countryOfOrigin(RdfProperty):
    term = RdfTerm('countryOfOrigin', 'https://schema.org/countryOfOrigin', [])
    object: schemaorg.Country

@dataclass(frozen=True)
class contentRating(RdfProperty):
    term = RdfTerm('contentRating', 'https://schema.org/contentRating', [])
    object: Text | schemaorg.Rating

@dataclass(frozen=True)
class globalLocationNumber(RdfProperty):
    term = RdfTerm('globalLocationNumber', 'https://schema.org/globalLocationNumber', [])
    object: Text

@dataclass(frozen=True)
class seatingType(RdfProperty):
    term = RdfTerm('seatingType', 'https://schema.org/seatingType', [])
    object: Text | schemaorg.QualitativeValue

@dataclass(frozen=True)
class line(RdfProperty):
    term = RdfTerm('line', 'https://schema.org/line', [])
    object: Text

@dataclass(frozen=True)
class availableTest(RdfProperty):
    term = RdfTerm('availableTest', 'https://schema.org/availableTest', [])
    object: schemaorg.MedicalTest

@dataclass(frozen=True)
class object(RdfProperty):
    term = RdfTerm('object', 'https://schema.org/object', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class interactionType(RdfProperty):
    term = RdfTerm('interactionType', 'https://schema.org/interactionType', [])
    object: schemaorg.Action

@dataclass(frozen=True)
class permittedUsage(RdfProperty):
    term = RdfTerm('permittedUsage', 'https://schema.org/permittedUsage', [])
    object: Text

@dataclass(frozen=True)
class expectsAcceptanceOf(RdfProperty):
    term = RdfTerm('expectsAcceptanceOf', 'https://schema.org/expectsAcceptanceOf', [])
    object: schemaorg.Offer

@dataclass(frozen=True)
class inAlbum(RdfProperty):
    term = RdfTerm('inAlbum', 'https://schema.org/inAlbum', [])
    object: schemaorg.MusicAlbum

@dataclass(frozen=True)
class originalMediaLink(RdfProperty):
    term = RdfTerm('originalMediaLink', 'https://schema.org/originalMediaLink', [])
    object: schemaorg.WebPage | URL | schemaorg.MediaObject

@dataclass(frozen=True)
class openingHoursSpecification(RdfProperty):
    term = RdfTerm('openingHoursSpecification', 'https://schema.org/openingHoursSpecification', [])
    object: schemaorg.OpeningHoursSpecification

@dataclass(frozen=True)
class auditDate(RdfProperty):
    term = RdfTerm('auditDate', 'https://schema.org/auditDate', [])
    object: Date | DateTime

@dataclass(frozen=True)
class jobImmediateStart(RdfProperty):
    term = RdfTerm('jobImmediateStart', 'https://schema.org/jobImmediateStart', [])
    object: Boolean

@dataclass(frozen=True)
class version(RdfProperty):
    term = RdfTerm('version', 'https://schema.org/version', [])
    object: Text | Number

@dataclass(frozen=True)
class valueMaxLength(RdfProperty):
    term = RdfTerm('valueMaxLength', 'https://schema.org/valueMaxLength', [])
    object: Number

@dataclass(frozen=True)
class hasPOS(RdfProperty):
    term = RdfTerm('hasPOS', 'https://schema.org/hasPOS', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class educationalAlignment(RdfProperty):
    term = RdfTerm('educationalAlignment', 'https://schema.org/educationalAlignment', [])
    object: schemaorg.AlignmentObject

@dataclass(frozen=True)
class worksFor(RdfProperty):
    term = RdfTerm('worksFor', 'https://schema.org/worksFor', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class salaryCurrency(RdfProperty):
    term = RdfTerm('salaryCurrency', 'https://schema.org/salaryCurrency', [])
    object: Text

@dataclass(frozen=True)
class maintainer(RdfProperty):
    term = RdfTerm('maintainer', 'https://schema.org/maintainer', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class isBasedOnUrl(RdfProperty):
    term = RdfTerm('isBasedOnUrl', 'https://schema.org/isBasedOnUrl', [])
    object: schemaorg.CreativeWork | schemaorg.Product | URL

@dataclass(frozen=True)
class billingPeriod(RdfProperty):
    term = RdfTerm('billingPeriod', 'https://schema.org/billingPeriod', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class freeShippingThreshold(RdfProperty):
    term = RdfTerm('freeShippingThreshold', 'https://schema.org/freeShippingThreshold', [])
    object: schemaorg.MonetaryAmount | schemaorg.DeliveryChargeSpecification

@dataclass(frozen=True)
class diversityStaffingReport(RdfProperty):
    term = RdfTerm('diversityStaffingReport', 'https://schema.org/diversityStaffingReport', [])
    object: schemaorg.Article | URL

@dataclass(frozen=True)
class birthPlace(RdfProperty):
    term = RdfTerm('birthPlace', 'https://schema.org/birthPlace', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class incomeLimit(RdfProperty):
    term = RdfTerm('incomeLimit', 'https://schema.org/incomeLimit', [])
    object: Text | schemaorg.MonetaryAmount

@dataclass(frozen=True)
class additionalProperty(RdfProperty):
    term = RdfTerm('additionalProperty', 'https://schema.org/additionalProperty', [])
    object: schemaorg.PropertyValue

@dataclass(frozen=True)
class tool(RdfProperty):
    term = RdfTerm('tool', 'https://schema.org/tool', [])
    object: schemaorg.HowToTool | Text

@dataclass(frozen=True)
class musicGroupMember(RdfProperty):
    term = RdfTerm('musicGroupMember', 'https://schema.org/musicGroupMember', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class physicalRequirement(RdfProperty):
    term = RdfTerm('physicalRequirement', 'https://schema.org/physicalRequirement', [])
    object: schemaorg.DefinedTerm | Text | URL

@dataclass(frozen=True)
class returnPolicySeasonalOverride(RdfProperty):
    term = RdfTerm('returnPolicySeasonalOverride', 'https://schema.org/returnPolicySeasonalOverride', [])
    object: schemaorg.MerchantReturnPolicySeasonalOverride

@dataclass(frozen=True)
class equal(RdfProperty):
    term = RdfTerm('equal', 'https://schema.org/equal', [])
    object: schemaorg.QualitativeValue

@dataclass(frozen=True)
class jobBenefits(RdfProperty):
    term = RdfTerm('jobBenefits', 'https://schema.org/jobBenefits', [])
    object: Text

@dataclass(frozen=True)
class usNPI(RdfProperty):
    term = RdfTerm('usNPI', 'https://schema.org/usNPI', [])
    object: Text

@dataclass(frozen=True)
class currenciesAccepted(RdfProperty):
    term = RdfTerm('currenciesAccepted', 'https://schema.org/currenciesAccepted', [])
    object: Text

@dataclass(frozen=True)
class medicalSpecialty(RdfProperty):
    term = RdfTerm('medicalSpecialty', 'https://schema.org/medicalSpecialty', [])
    object: schemaorg.MedicalSpecialty

@dataclass(frozen=True)
class warrantyPromise(RdfProperty):
    term = RdfTerm('warrantyPromise', 'https://schema.org/warrantyPromise', [])
    object: schemaorg.WarrantyPromise

@dataclass(frozen=True)
class owns(RdfProperty):
    term = RdfTerm('owns', 'https://schema.org/owns', [])
    object: schemaorg.OwnershipInfo | schemaorg.Product

@dataclass(frozen=True)
class populationType(RdfProperty):
    term = RdfTerm('populationType', 'https://schema.org/populationType', [])
    object: schemaorg.Class

@dataclass(frozen=True)
class application(RdfProperty):
    term = RdfTerm('application', 'https://schema.org/application', [])
    object: schemaorg.SoftwareApplication

@dataclass(frozen=True)
class eventStatus(RdfProperty):
    term = RdfTerm('eventStatus', 'https://schema.org/eventStatus', [])
    object: schemaorg.EventStatusType

@dataclass(frozen=True)
class cutoffTime(RdfProperty):
    term = RdfTerm('cutoffTime', 'https://schema.org/cutoffTime', [])
    object: Time

@dataclass(frozen=True)
class clinicalPharmacology(RdfProperty):
    term = RdfTerm('clinicalPharmacology', 'https://schema.org/clinicalPharmacology', [])
    object: Text

@dataclass(frozen=True)
class fuelConsumption(RdfProperty):
    term = RdfTerm('fuelConsumption', 'https://schema.org/fuelConsumption', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class significantLink(RdfProperty):
    term = RdfTerm('significantLink', 'https://schema.org/significantLink', [])
    object: URL

@dataclass(frozen=True)
class assemblyVersion(RdfProperty):
    term = RdfTerm('assemblyVersion', 'https://schema.org/assemblyVersion', [])
    object: Text

@dataclass(frozen=True)
class parentTaxon(RdfProperty):
    term = RdfTerm('parentTaxon', 'https://schema.org/parentTaxon', [])
    object: URL | Text | schemaorg.Taxon

@dataclass(frozen=True)
class accountId(RdfProperty):
    term = RdfTerm('accountId', 'https://schema.org/accountId', [])
    object: Text

@dataclass(frozen=True)
class runsTo(RdfProperty):
    term = RdfTerm('runsTo', 'https://schema.org/runsTo', [])
    object: schemaorg.Vessel

@dataclass(frozen=True)
class supply(RdfProperty):
    term = RdfTerm('supply', 'https://schema.org/supply', [])
    object: Text | schemaorg.HowToSupply

@dataclass(frozen=True)
class nsn(RdfProperty):
    term = RdfTerm('nsn', 'https://schema.org/nsn', [])
    object: Text

@dataclass(frozen=True)
class typicalTest(RdfProperty):
    term = RdfTerm('typicalTest', 'https://schema.org/typicalTest', [])
    object: schemaorg.MedicalTest

@dataclass(frozen=True)
class documentation(RdfProperty):
    term = RdfTerm('documentation', 'https://schema.org/documentation', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class hasTierBenefit(RdfProperty):
    term = RdfTerm('hasTierBenefit', 'https://schema.org/hasTierBenefit', [])
    object: schemaorg.TierBenefitEnumeration

@dataclass(frozen=True)
class overdosage(RdfProperty):
    term = RdfTerm('overdosage', 'https://schema.org/overdosage', [])
    object: Text

@dataclass(frozen=True)
class energyEfficiencyScaleMax(RdfProperty):
    term = RdfTerm('energyEfficiencyScaleMax', 'https://schema.org/energyEfficiencyScaleMax', [])
    object: schemaorg.EUEnergyEfficiencyEnumeration

@dataclass(frozen=True)
class contentType(RdfProperty):
    term = RdfTerm('contentType', 'https://schema.org/contentType', [])
    object: Text

@dataclass(frozen=True)
class contactlessPayment(RdfProperty):
    term = RdfTerm('contactlessPayment', 'https://schema.org/contactlessPayment', [])
    object: Boolean

@dataclass(frozen=True)
class publication(RdfProperty):
    term = RdfTerm('publication', 'https://schema.org/publication', [])
    object: schemaorg.PublicationEvent

@dataclass(frozen=True)
class affectedBy(RdfProperty):
    term = RdfTerm('affectedBy', 'https://schema.org/affectedBy', [])
    object: schemaorg.Drug

@dataclass(frozen=True)
class doseSchedule(RdfProperty):
    term = RdfTerm('doseSchedule', 'https://schema.org/doseSchedule', [])
    object: schemaorg.DoseSchedule

@dataclass(frozen=True)
class copyrightYear(RdfProperty):
    term = RdfTerm('copyrightYear', 'https://schema.org/copyrightYear', [])
    object: Number

@dataclass(frozen=True)
class includedRiskFactor(RdfProperty):
    term = RdfTerm('includedRiskFactor', 'https://schema.org/includedRiskFactor', [])
    object: schemaorg.MedicalRiskFactor

@dataclass(frozen=True)
class passengerPriorityStatus(RdfProperty):
    term = RdfTerm('passengerPriorityStatus', 'https://schema.org/passengerPriorityStatus', [])
    object: Text | schemaorg.QualitativeValue

@dataclass(frozen=True)
class stage(RdfProperty):
    term = RdfTerm('stage', 'https://schema.org/stage', [])
    object: schemaorg.MedicalConditionStage

@dataclass(frozen=True)
class enginePower(RdfProperty):
    term = RdfTerm('enginePower', 'https://schema.org/enginePower', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class member(RdfProperty):
    term = RdfTerm('member', 'https://schema.org/member', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class speed(RdfProperty):
    term = RdfTerm('speed', 'https://schema.org/speed', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class yearlyRevenue(RdfProperty):
    term = RdfTerm('yearlyRevenue', 'https://schema.org/yearlyRevenue', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class suggestedMeasurement(RdfProperty):
    term = RdfTerm('suggestedMeasurement', 'https://schema.org/suggestedMeasurement', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class typeOfBed(RdfProperty):
    term = RdfTerm('typeOfBed', 'https://schema.org/typeOfBed', [])
    object: Text | schemaorg.BedType

@dataclass(frozen=True)
class workLocation(RdfProperty):
    term = RdfTerm('workLocation', 'https://schema.org/workLocation', [])
    object: schemaorg.Place | schemaorg.ContactPoint

@dataclass(frozen=True)
class numItems(RdfProperty):
    term = RdfTerm('numItems', 'https://schema.org/numItems', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class knownVehicleDamages(RdfProperty):
    term = RdfTerm('knownVehicleDamages', 'https://schema.org/knownVehicleDamages', [])
    object: Text

@dataclass(frozen=True)
class deathPlace(RdfProperty):
    term = RdfTerm('deathPlace', 'https://schema.org/deathPlace', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class touristType(RdfProperty):
    term = RdfTerm('touristType', 'https://schema.org/touristType', [])
    object: Text | schemaorg.Audience

@dataclass(frozen=True)
class unnamedSourcesPolicy(RdfProperty):
    term = RdfTerm('unnamedSourcesPolicy', 'https://schema.org/unnamedSourcesPolicy', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class possibleTreatment(RdfProperty):
    term = RdfTerm('possibleTreatment', 'https://schema.org/possibleTreatment', [])
    object: schemaorg.MedicalTherapy

@dataclass(frozen=True)
class legislationIdentifier(RdfProperty):
    term = RdfTerm('legislationIdentifier', 'https://schema.org/legislationIdentifier', [])
    object: Text | URL

@dataclass(frozen=True)
class reviewedBy(RdfProperty):
    term = RdfTerm('reviewedBy', 'https://schema.org/reviewedBy', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class siblings(RdfProperty):
    term = RdfTerm('siblings', 'https://schema.org/siblings', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class interactionService(RdfProperty):
    term = RdfTerm('interactionService', 'https://schema.org/interactionService', [])
    object: schemaorg.SoftwareApplication | schemaorg.WebSite

@dataclass(frozen=True)
class governmentBenefitsInfo(RdfProperty):
    term = RdfTerm('governmentBenefitsInfo', 'https://schema.org/governmentBenefitsInfo', [])
    object: schemaorg.GovernmentService

@dataclass(frozen=True)
class isicV4(RdfProperty):
    term = RdfTerm('isicV4', 'https://schema.org/isicV4', [])
    object: Text

@dataclass(frozen=True)
class arrivalBusStop(RdfProperty):
    term = RdfTerm('arrivalBusStop', 'https://schema.org/arrivalBusStop', [])
    object: schemaorg.BusStation | schemaorg.BusStop

@dataclass(frozen=True)
class howPerformed(RdfProperty):
    term = RdfTerm('howPerformed', 'https://schema.org/howPerformed', [])
    object: Text

@dataclass(frozen=True)
class archiveHeld(RdfProperty):
    term = RdfTerm('archiveHeld', 'https://schema.org/archiveHeld', [])
    object: schemaorg.ArchiveComponent

@dataclass(frozen=True)
class healthPlanCoinsuranceOption(RdfProperty):
    term = RdfTerm('healthPlanCoinsuranceOption', 'https://schema.org/healthPlanCoinsuranceOption', [])
    object: Text

@dataclass(frozen=True)
class featureList(RdfProperty):
    term = RdfTerm('featureList', 'https://schema.org/featureList', [])
    object: Text | URL

@dataclass(frozen=True)
class billingStart(RdfProperty):
    term = RdfTerm('billingStart', 'https://schema.org/billingStart', [])
    object: Number

@dataclass(frozen=True)
class hasGS1DigitalLink(RdfProperty):
    term = RdfTerm('hasGS1DigitalLink', 'https://schema.org/hasGS1DigitalLink', [])
    object: URL

@dataclass(frozen=True)
class relatedLink(RdfProperty):
    term = RdfTerm('relatedLink', 'https://schema.org/relatedLink', [])
    object: URL

@dataclass(frozen=True)
class dropoffLocation(RdfProperty):
    term = RdfTerm('dropoffLocation', 'https://schema.org/dropoffLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class realEstateAgent(RdfProperty):
    term = RdfTerm('realEstateAgent', 'https://schema.org/realEstateAgent', [])
    object: schemaorg.RealEstateAgent

@dataclass(frozen=True)
class membershipPointsEarned(RdfProperty):
    term = RdfTerm('membershipPointsEarned', 'https://schema.org/membershipPointsEarned', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class seasonNumber(RdfProperty):
    term = RdfTerm('seasonNumber', 'https://schema.org/seasonNumber', [])
    object: Integer | Text

@dataclass(frozen=True)
class prescriptionStatus(RdfProperty):
    term = RdfTerm('prescriptionStatus', 'https://schema.org/prescriptionStatus', [])
    object: schemaorg.DrugPrescriptionStatus | Text

@dataclass(frozen=True)
class genre(RdfProperty):
    term = RdfTerm('genre', 'https://schema.org/genre', [])
    object: Text | URL

@dataclass(frozen=True)
class diagram(RdfProperty):
    term = RdfTerm('diagram', 'https://schema.org/diagram', [])
    object: schemaorg.ImageObject

@dataclass(frozen=True)
class checkinTime(RdfProperty):
    term = RdfTerm('checkinTime', 'https://schema.org/checkinTime', [])
    object: DateTime | Time

@dataclass(frozen=True)
class shippingOrigin(RdfProperty):
    term = RdfTerm('shippingOrigin', 'https://schema.org/shippingOrigin', [])
    object: schemaorg.DefinedRegion

@dataclass(frozen=True)
class accommodationFloorPlan(RdfProperty):
    term = RdfTerm('accommodationFloorPlan', 'https://schema.org/accommodationFloorPlan', [])
    object: schemaorg.FloorPlan

@dataclass(frozen=True)
class processingTime(RdfProperty):
    term = RdfTerm('processingTime', 'https://schema.org/processingTime', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class license(RdfProperty):
    term = RdfTerm('license', 'https://schema.org/license', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class events(RdfProperty):
    term = RdfTerm('events', 'https://schema.org/events', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class addressCountry(RdfProperty):
    term = RdfTerm('addressCountry', 'https://schema.org/addressCountry', [])
    object: schemaorg.Country | Text

@dataclass(frozen=True)
class downPayment(RdfProperty):
    term = RdfTerm('downPayment', 'https://schema.org/downPayment', [])
    object: schemaorg.MonetaryAmount | Number

@dataclass(frozen=True)
class acceptedOffer(RdfProperty):
    term = RdfTerm('acceptedOffer', 'https://schema.org/acceptedOffer', [])
    object: schemaorg.Offer

@dataclass(frozen=True)
class relatedAnatomy(RdfProperty):
    term = RdfTerm('relatedAnatomy', 'https://schema.org/relatedAnatomy', [])
    object: schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem

@dataclass(frozen=True)
class merchantReturnLink(RdfProperty):
    term = RdfTerm('merchantReturnLink', 'https://schema.org/merchantReturnLink', [])
    object: URL

@dataclass(frozen=True)
class pathophysiology(RdfProperty):
    term = RdfTerm('pathophysiology', 'https://schema.org/pathophysiology', [])
    object: Text

@dataclass(frozen=True)
class certificationStatus(RdfProperty):
    term = RdfTerm('certificationStatus', 'https://schema.org/certificationStatus', [])
    object: schemaorg.CertificationStatusEnumeration

@dataclass(frozen=True)
class bookEdition(RdfProperty):
    term = RdfTerm('bookEdition', 'https://schema.org/bookEdition', [])
    object: Text

@dataclass(frozen=True)
class publicTransportClosuresInfo(RdfProperty):
    term = RdfTerm('publicTransportClosuresInfo', 'https://schema.org/publicTransportClosuresInfo', [])
    object: schemaorg.WebContent | URL

@dataclass(frozen=True)
class previousStartDate(RdfProperty):
    term = RdfTerm('previousStartDate', 'https://schema.org/previousStartDate', [])
    object: Date

@dataclass(frozen=True)
class processorRequirements(RdfProperty):
    term = RdfTerm('processorRequirements', 'https://schema.org/processorRequirements', [])
    object: Text

@dataclass(frozen=True)
class departureTime(RdfProperty):
    term = RdfTerm('departureTime', 'https://schema.org/departureTime', [])
    object: DateTime | Time

@dataclass(frozen=True)
class schemaVersion(RdfProperty):
    term = RdfTerm('schemaVersion', 'https://schema.org/schemaVersion', [])
    object: Text | URL

@dataclass(frozen=True)
class departureBusStop(RdfProperty):
    term = RdfTerm('departureBusStop', 'https://schema.org/departureBusStop', [])
    object: schemaorg.BusStation | schemaorg.BusStop

@dataclass(frozen=True)
class referenceQuantity(RdfProperty):
    term = RdfTerm('referenceQuantity', 'https://schema.org/referenceQuantity', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class geoDisjoint(RdfProperty):
    term = RdfTerm('geoDisjoint', 'https://schema.org/geoDisjoint', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class algorithm(RdfProperty):
    term = RdfTerm('algorithm', 'https://schema.org/algorithm', [])
    object: Text

@dataclass(frozen=True)
class earlyPrepaymentPenalty(RdfProperty):
    term = RdfTerm('earlyPrepaymentPenalty', 'https://schema.org/earlyPrepaymentPenalty', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class interactingDrug(RdfProperty):
    term = RdfTerm('interactingDrug', 'https://schema.org/interactingDrug', [])
    object: schemaorg.Drug

@dataclass(frozen=True)
class mainEntity(RdfProperty):
    term = RdfTerm('mainEntity', 'https://schema.org/mainEntity', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class upvoteCount(RdfProperty):
    term = RdfTerm('upvoteCount', 'https://schema.org/upvoteCount', [])
    object: Integer

@dataclass(frozen=True)
class bioChemInteraction(RdfProperty):
    term = RdfTerm('bioChemInteraction', 'https://schema.org/bioChemInteraction', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class messageAttachment(RdfProperty):
    term = RdfTerm('messageAttachment', 'https://schema.org/messageAttachment', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class educationalLevel(RdfProperty):
    term = RdfTerm('educationalLevel', 'https://schema.org/educationalLevel', [])
    object: schemaorg.DefinedTerm | Text | URL

@dataclass(frozen=True)
class givenName(RdfProperty):
    term = RdfTerm('givenName', 'https://schema.org/givenName', [])
    object: Text

@dataclass(frozen=True)
class foundingLocation(RdfProperty):
    term = RdfTerm('foundingLocation', 'https://schema.org/foundingLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class trackingNumber(RdfProperty):
    term = RdfTerm('trackingNumber', 'https://schema.org/trackingNumber', [])
    object: Text

@dataclass(frozen=True)
class appliesToPaymentMethod(RdfProperty):
    term = RdfTerm('appliesToPaymentMethod', 'https://schema.org/appliesToPaymentMethod', [])
    object: schemaorg.PaymentMethod

@dataclass(frozen=True)
class leaseLength(RdfProperty):
    term = RdfTerm('leaseLength', 'https://schema.org/leaseLength', [])
    object: schemaorg.Duration | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class validFrom(RdfProperty):
    term = RdfTerm('validFrom', 'https://schema.org/validFrom', [])
    object: Date | DateTime

@dataclass(frozen=True)
class recordingOf(RdfProperty):
    term = RdfTerm('recordingOf', 'https://schema.org/recordingOf', [])
    object: schemaorg.MusicComposition

@dataclass(frozen=True)
class geoContains(RdfProperty):
    term = RdfTerm('geoContains', 'https://schema.org/geoContains', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class geoOverlaps(RdfProperty):
    term = RdfTerm('geoOverlaps', 'https://schema.org/geoOverlaps', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class appliesToDeliveryMethod(RdfProperty):
    term = RdfTerm('appliesToDeliveryMethod', 'https://schema.org/appliesToDeliveryMethod', [])
    object: schemaorg.DeliveryMethod

@dataclass(frozen=True)
class drainsTo(RdfProperty):
    term = RdfTerm('drainsTo', 'https://schema.org/drainsTo', [])
    object: schemaorg.Vessel

@dataclass(frozen=True)
class borrower(RdfProperty):
    term = RdfTerm('borrower', 'https://schema.org/borrower', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class broadcastAffiliateOf(RdfProperty):
    term = RdfTerm('broadcastAffiliateOf', 'https://schema.org/broadcastAffiliateOf', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class startDate(RdfProperty):
    term = RdfTerm('startDate', 'https://schema.org/startDate', [])
    object: Date | DateTime

@dataclass(frozen=True)
class icaoCode(RdfProperty):
    term = RdfTerm('icaoCode', 'https://schema.org/icaoCode', [])
    object: Text

@dataclass(frozen=True)
class addressLocality(RdfProperty):
    term = RdfTerm('addressLocality', 'https://schema.org/addressLocality', [])
    object: Text

@dataclass(frozen=True)
class articleBody(RdfProperty):
    term = RdfTerm('articleBody', 'https://schema.org/articleBody', [])
    object: Text

@dataclass(frozen=True)
class isPlanForApartment(RdfProperty):
    term = RdfTerm('isPlanForApartment', 'https://schema.org/isPlanForApartment', [])
    object: schemaorg.Accommodation

@dataclass(frozen=True)
class activityDuration(RdfProperty):
    term = RdfTerm('activityDuration', 'https://schema.org/activityDuration', [])
    object: schemaorg.Duration | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class competencyRequired(RdfProperty):
    term = RdfTerm('competencyRequired', 'https://schema.org/competencyRequired', [])
    object: schemaorg.DefinedTerm | Text | URL

@dataclass(frozen=True)
class spouse(RdfProperty):
    term = RdfTerm('spouse', 'https://schema.org/spouse', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class includesHealthPlanNetwork(RdfProperty):
    term = RdfTerm('includesHealthPlanNetwork', 'https://schema.org/includesHealthPlanNetwork', [])
    object: schemaorg.HealthPlanNetwork

@dataclass(frozen=True)
class repeatCount(RdfProperty):
    term = RdfTerm('repeatCount', 'https://schema.org/repeatCount', [])
    object: Integer

@dataclass(frozen=True)
class gameEdition(RdfProperty):
    term = RdfTerm('gameEdition', 'https://schema.org/gameEdition', [])
    object: Text

@dataclass(frozen=True)
class geoCrosses(RdfProperty):
    term = RdfTerm('geoCrosses', 'https://schema.org/geoCrosses', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class trackingUrl(RdfProperty):
    term = RdfTerm('trackingUrl', 'https://schema.org/trackingUrl', [])
    object: URL

@dataclass(frozen=True)
class gameAvailabilityType(RdfProperty):
    term = RdfTerm('gameAvailabilityType', 'https://schema.org/gameAvailabilityType', [])
    object: Text | schemaorg.GameAvailabilityEnumeration

@dataclass(frozen=True)
class subReservation(RdfProperty):
    term = RdfTerm('subReservation', 'https://schema.org/subReservation', [])
    object: schemaorg.Reservation

@dataclass(frozen=True)
class depth(RdfProperty):
    term = RdfTerm('depth', 'https://schema.org/depth', [])
    object: schemaorg.Distance | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class incentiveAmount(RdfProperty):
    term = RdfTerm('incentiveAmount', 'https://schema.org/incentiveAmount', [])
    object: schemaorg.LoanOrCredit | schemaorg.QuantitativeValue | schemaorg.UnitPriceSpecification

@dataclass(frozen=True)
class purchaseType(RdfProperty):
    term = RdfTerm('purchaseType', 'https://schema.org/purchaseType', [])
    object: schemaorg.PurchaseType

@dataclass(frozen=True)
class educationRequirements(RdfProperty):
    term = RdfTerm('educationRequirements', 'https://schema.org/educationRequirements', [])
    object: Text | schemaorg.EducationalOccupationalCredential

@dataclass(frozen=True)
class sensoryUnit(RdfProperty):
    term = RdfTerm('sensoryUnit', 'https://schema.org/sensoryUnit', [])
    object: schemaorg.AnatomicalStructure | schemaorg.SuperficialAnatomy

@dataclass(frozen=True)
class floorSize(RdfProperty):
    term = RdfTerm('floorSize', 'https://schema.org/floorSize', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class isInvolvedInBiologicalProcess(RdfProperty):
    term = RdfTerm('isInvolvedInBiologicalProcess', 'https://schema.org/isInvolvedInBiologicalProcess', [])
    object: schemaorg.PropertyValue | schemaorg.DefinedTerm | URL

@dataclass(frozen=True)
class incentiveType(RdfProperty):
    term = RdfTerm('incentiveType', 'https://schema.org/incentiveType', [])
    object: schemaorg.IncentiveType

@dataclass(frozen=True)
class measurementMethod(RdfProperty):
    term = RdfTerm('measurementMethod', 'https://schema.org/measurementMethod', [])
    object: schemaorg.DefinedTerm | Text | URL | schemaorg.MeasurementMethodEnum

@dataclass(frozen=True)
class acceptsReservations(RdfProperty):
    term = RdfTerm('acceptsReservations', 'https://schema.org/acceptsReservations', [])
    object: Boolean | Text | URL

@dataclass(frozen=True)
class printEdition(RdfProperty):
    term = RdfTerm('printEdition', 'https://schema.org/printEdition', [])
    object: Text

@dataclass(frozen=True)
class legislationCommences(RdfProperty):
    term = RdfTerm('legislationCommences', 'https://schema.org/legislationCommences', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class titleEIDR(RdfProperty):
    term = RdfTerm('titleEIDR', 'https://schema.org/titleEIDR', [])
    object: Text | URL

@dataclass(frozen=True)
class loanTerm(RdfProperty):
    term = RdfTerm('loanTerm', 'https://schema.org/loanTerm', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class dataset(RdfProperty):
    term = RdfTerm('dataset', 'https://schema.org/dataset', [])
    object: schemaorg.Dataset

@dataclass(frozen=True)
class cssSelector(RdfProperty):
    term = RdfTerm('cssSelector', 'https://schema.org/cssSelector', [])
    object: CssSelectorType

@dataclass(frozen=True)
class isLocatedInSubcellularLocation(RdfProperty):
    term = RdfTerm('isLocatedInSubcellularLocation', 'https://schema.org/isLocatedInSubcellularLocation', [])
    object: schemaorg.PropertyValue | schemaorg.DefinedTerm | URL

@dataclass(frozen=True)
class minimumPaymentDue(RdfProperty):
    term = RdfTerm('minimumPaymentDue', 'https://schema.org/minimumPaymentDue', [])
    object: schemaorg.PriceSpecification | schemaorg.MonetaryAmount

@dataclass(frozen=True)
class knowsAbout(RdfProperty):
    term = RdfTerm('knowsAbout', 'https://schema.org/knowsAbout', [])
    object: schemaorg.Thing | Text | URL

@dataclass(frozen=True)
class legislationCountersignedBy(RdfProperty):
    term = RdfTerm('legislationCountersignedBy', 'https://schema.org/legislationCountersignedBy', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class creditText(RdfProperty):
    term = RdfTerm('creditText', 'https://schema.org/creditText', [])
    object: Text

@dataclass(frozen=True)
class composer(RdfProperty):
    term = RdfTerm('composer', 'https://schema.org/composer', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class startOffset(RdfProperty):
    term = RdfTerm('startOffset', 'https://schema.org/startOffset', [])
    object: schemaorg.HyperTocEntry | Number

@dataclass(frozen=True)
class termsPerYear(RdfProperty):
    term = RdfTerm('termsPerYear', 'https://schema.org/termsPerYear', [])
    object: Number

@dataclass(frozen=True)
class hasBroadcastChannel(RdfProperty):
    term = RdfTerm('hasBroadcastChannel', 'https://schema.org/hasBroadcastChannel', [])
    object: schemaorg.BroadcastChannel

@dataclass(frozen=True)
class significance(RdfProperty):
    term = RdfTerm('significance', 'https://schema.org/significance', [])
    object: Text

@dataclass(frozen=True)
class accessMode(RdfProperty):
    term = RdfTerm('accessMode', 'https://schema.org/accessMode', [])
    object: Text

@dataclass(frozen=True)
class jobLocation(RdfProperty):
    term = RdfTerm('jobLocation', 'https://schema.org/jobLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class proficiencyLevel(RdfProperty):
    term = RdfTerm('proficiencyLevel', 'https://schema.org/proficiencyLevel', [])
    object: Text

@dataclass(frozen=True)
class minPrice(RdfProperty):
    term = RdfTerm('minPrice', 'https://schema.org/minPrice', [])
    object: Number

@dataclass(frozen=True)
class discountCurrency(RdfProperty):
    term = RdfTerm('discountCurrency', 'https://schema.org/discountCurrency', [])
    object: Text

@dataclass(frozen=True)
class expertConsiderations(RdfProperty):
    term = RdfTerm('expertConsiderations', 'https://schema.org/expertConsiderations', [])
    object: Text

@dataclass(frozen=True)
class nutrition(RdfProperty):
    term = RdfTerm('nutrition', 'https://schema.org/nutrition', [])
    object: schemaorg.NutritionInformation

@dataclass(frozen=True)
class identifyingExam(RdfProperty):
    term = RdfTerm('identifyingExam', 'https://schema.org/identifyingExam', [])
    object: schemaorg.PhysicalExam

@dataclass(frozen=True)
class serviceUrl(RdfProperty):
    term = RdfTerm('serviceUrl', 'https://schema.org/serviceUrl', [])
    object: URL

@dataclass(frozen=True)
class nonprofitStatus(RdfProperty):
    term = RdfTerm('nonprofitStatus', 'https://schema.org/nonprofitStatus', [])
    object: schemaorg.NonprofitType

@dataclass(frozen=True)
class healthPlanCoinsuranceRate(RdfProperty):
    term = RdfTerm('healthPlanCoinsuranceRate', 'https://schema.org/healthPlanCoinsuranceRate', [])
    object: Number

@dataclass(frozen=True)
class branchOf(RdfProperty):
    term = RdfTerm('branchOf', 'https://schema.org/branchOf', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class numberOfDoors(RdfProperty):
    term = RdfTerm('numberOfDoors', 'https://schema.org/numberOfDoors', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class audio(RdfProperty):
    term = RdfTerm('audio', 'https://schema.org/audio', [])
    object: schemaorg.Clip | schemaorg.MusicRecording | schemaorg.AudioObject

@dataclass(frozen=True)
class itemCondition(RdfProperty):
    term = RdfTerm('itemCondition', 'https://schema.org/itemCondition', [])
    object: schemaorg.OfferItemCondition

@dataclass(frozen=True)
class ineligibleRegion(RdfProperty):
    term = RdfTerm('ineligibleRegion', 'https://schema.org/ineligibleRegion', [])
    object: schemaorg.GeoShape | Text | schemaorg.Place

@dataclass(frozen=True)
class directApply(RdfProperty):
    term = RdfTerm('directApply', 'https://schema.org/directApply', [])
    object: Boolean

@dataclass(frozen=True)
class iataCode(RdfProperty):
    term = RdfTerm('iataCode', 'https://schema.org/iataCode', [])
    object: Text

@dataclass(frozen=True)
class lastReviewed(RdfProperty):
    term = RdfTerm('lastReviewed', 'https://schema.org/lastReviewed', [])
    object: Date

@dataclass(frozen=True)
class lyricist(RdfProperty):
    term = RdfTerm('lyricist', 'https://schema.org/lyricist', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class countryOfLastProcessing(RdfProperty):
    term = RdfTerm('countryOfLastProcessing', 'https://schema.org/countryOfLastProcessing', [])
    object: Text

@dataclass(frozen=True)
class programMembershipUsed(RdfProperty):
    term = RdfTerm('programMembershipUsed', 'https://schema.org/programMembershipUsed', [])
    object: schemaorg.ProgramMembership

@dataclass(frozen=True)
class discountCode(RdfProperty):
    term = RdfTerm('discountCode', 'https://schema.org/discountCode', [])
    object: Text

@dataclass(frozen=True)
class isPartOf(RdfProperty):
    term = RdfTerm('isPartOf', 'https://schema.org/isPartOf', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class workPerformed(RdfProperty):
    term = RdfTerm('workPerformed', 'https://schema.org/workPerformed', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class positiveNotes(RdfProperty):
    term = RdfTerm('positiveNotes', 'https://schema.org/positiveNotes', [])
    object: schemaorg.WebContent | Text | schemaorg.ListItem | schemaorg.ItemList

@dataclass(frozen=True)
class warrantyScope(RdfProperty):
    term = RdfTerm('warrantyScope', 'https://schema.org/warrantyScope', [])
    object: schemaorg.WarrantyScope

@dataclass(frozen=True)
class typicalCreditsPerTerm(RdfProperty):
    term = RdfTerm('typicalCreditsPerTerm', 'https://schema.org/typicalCreditsPerTerm', [])
    object: Integer | schemaorg.StructuredValue

@dataclass(frozen=True)
class locationCreated(RdfProperty):
    term = RdfTerm('locationCreated', 'https://schema.org/locationCreated', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class recipeYield(RdfProperty):
    term = RdfTerm('recipeYield', 'https://schema.org/recipeYield', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class image(RdfProperty):
    term = RdfTerm('image', 'https://schema.org/image', [])
    object: URL | schemaorg.ImageObject

@dataclass(frozen=True)
class printColumn(RdfProperty):
    term = RdfTerm('printColumn', 'https://schema.org/printColumn', [])
    object: Text

@dataclass(frozen=True)
class programType(RdfProperty):
    term = RdfTerm('programType', 'https://schema.org/programType', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class applicationContact(RdfProperty):
    term = RdfTerm('applicationContact', 'https://schema.org/applicationContact', [])
    object: schemaorg.ContactPoint

@dataclass(frozen=True)
class isrcCode(RdfProperty):
    term = RdfTerm('isrcCode', 'https://schema.org/isrcCode', [])
    object: Text

@dataclass(frozen=True)
class thumbnail(RdfProperty):
    term = RdfTerm('thumbnail', 'https://schema.org/thumbnail', [])
    object: schemaorg.ImageObject

@dataclass(frozen=True)
class mediaItemAppearance(RdfProperty):
    term = RdfTerm('mediaItemAppearance', 'https://schema.org/mediaItemAppearance', [])
    object: schemaorg.MediaObject

@dataclass(frozen=True)
class ingredients(RdfProperty):
    term = RdfTerm('ingredients', 'https://schema.org/ingredients', [])
    object: Text

@dataclass(frozen=True)
class sdLicense(RdfProperty):
    term = RdfTerm('sdLicense', 'https://schema.org/sdLicense', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class carbohydrateContent(RdfProperty):
    term = RdfTerm('carbohydrateContent', 'https://schema.org/carbohydrateContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class inDefinedTermSet(RdfProperty):
    term = RdfTerm('inDefinedTermSet', 'https://schema.org/inDefinedTermSet', [])
    object: schemaorg.DefinedTermSet | URL

@dataclass(frozen=True)
class gracePeriod(RdfProperty):
    term = RdfTerm('gracePeriod', 'https://schema.org/gracePeriod', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class coursePrerequisites(RdfProperty):
    term = RdfTerm('coursePrerequisites', 'https://schema.org/coursePrerequisites', [])
    object: Text | schemaorg.AlignmentObject | schemaorg.Course

@dataclass(frozen=True)
class hasCourseInstance(RdfProperty):
    term = RdfTerm('hasCourseInstance', 'https://schema.org/hasCourseInstance', [])
    object: schemaorg.CourseInstance

@dataclass(frozen=True)
class code(RdfProperty):
    term = RdfTerm('code', 'https://schema.org/code', [])
    object: schemaorg.MedicalCode

@dataclass(frozen=True)
class checkoutPageURLTemplate(RdfProperty):
    term = RdfTerm('checkoutPageURLTemplate', 'https://schema.org/checkoutPageURLTemplate', [])
    object: Text

@dataclass(frozen=True)
class healthPlanNetworkTier(RdfProperty):
    term = RdfTerm('healthPlanNetworkTier', 'https://schema.org/healthPlanNetworkTier', [])
    object: Text

@dataclass(frozen=True)
class studySubject(RdfProperty):
    term = RdfTerm('studySubject', 'https://schema.org/studySubject', [])
    object: schemaorg.MedicalEntity

@dataclass(frozen=True)
class eligibleRegion(RdfProperty):
    term = RdfTerm('eligibleRegion', 'https://schema.org/eligibleRegion', [])
    object: Text | schemaorg.GeoShape | schemaorg.Place

@dataclass(frozen=True)
class healthPlanMarketingUrl(RdfProperty):
    term = RdfTerm('healthPlanMarketingUrl', 'https://schema.org/healthPlanMarketingUrl', [])
    object: URL

@dataclass(frozen=True)
class contactType(RdfProperty):
    term = RdfTerm('contactType', 'https://schema.org/contactType', [])
    object: Text

@dataclass(frozen=True)
class strengthUnit(RdfProperty):
    term = RdfTerm('strengthUnit', 'https://schema.org/strengthUnit', [])
    object: Text

@dataclass(frozen=True)
class cvdNumC19OverflowPats(RdfProperty):
    term = RdfTerm('cvdNumC19OverflowPats', 'https://schema.org/cvdNumC19OverflowPats', [])
    object: Number

@dataclass(frozen=True)
class hasBioChemEntityPart(RdfProperty):
    term = RdfTerm('hasBioChemEntityPart', 'https://schema.org/hasBioChemEntityPart', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class itemLocation(RdfProperty):
    term = RdfTerm('itemLocation', 'https://schema.org/itemLocation', [])
    object: Text | schemaorg.PostalAddress | schemaorg.Place

@dataclass(frozen=True)
class courseMode(RdfProperty):
    term = RdfTerm('courseMode', 'https://schema.org/courseMode', [])
    object: Text | URL

@dataclass(frozen=True)
class occupationalCredentialAwarded(RdfProperty):
    term = RdfTerm('occupationalCredentialAwarded', 'https://schema.org/occupationalCredentialAwarded', [])
    object: Text | URL | schemaorg.EducationalOccupationalCredential

@dataclass(frozen=True)
class refundType(RdfProperty):
    term = RdfTerm('refundType', 'https://schema.org/refundType', [])
    object: schemaorg.RefundTypeEnumeration

@dataclass(frozen=True)
class applicationStartDate(RdfProperty):
    term = RdfTerm('applicationStartDate', 'https://schema.org/applicationStartDate', [])
    object: Date

@dataclass(frozen=True)
class productSupported(RdfProperty):
    term = RdfTerm('productSupported', 'https://schema.org/productSupported', [])
    object: schemaorg.Product | Text

@dataclass(frozen=True)
class includesObject(RdfProperty):
    term = RdfTerm('includesObject', 'https://schema.org/includesObject', [])
    object: schemaorg.TypeAndQuantityNode

@dataclass(frozen=True)
class cookingMethod(RdfProperty):
    term = RdfTerm('cookingMethod', 'https://schema.org/cookingMethod', [])
    object: Text

@dataclass(frozen=True)
class grantee(RdfProperty):
    term = RdfTerm('grantee', 'https://schema.org/grantee', [])
    object: schemaorg.Audience | schemaorg.Organization | schemaorg.ContactPoint | schemaorg.Person

@dataclass(frozen=True)
class calories(RdfProperty):
    term = RdfTerm('calories', 'https://schema.org/calories', [])
    object: schemaorg.Energy

@dataclass(frozen=True)
class cvdNumTotBeds(RdfProperty):
    term = RdfTerm('cvdNumTotBeds', 'https://schema.org/cvdNumTotBeds', [])
    object: Number

@dataclass(frozen=True)
class box(RdfProperty):
    term = RdfTerm('box', 'https://schema.org/box', [])
    object: Text

@dataclass(frozen=True)
class memberOf(RdfProperty):
    term = RdfTerm('memberOf', 'https://schema.org/memberOf', [])
    object: schemaorg.ProgramMembership | schemaorg.Organization | schemaorg.MemberProgramTier

@dataclass(frozen=True)
class dateRead(RdfProperty):
    term = RdfTerm('dateRead', 'https://schema.org/dateRead', [])
    object: Date | DateTime

@dataclass(frozen=True)
class musicArrangement(RdfProperty):
    term = RdfTerm('musicArrangement', 'https://schema.org/musicArrangement', [])
    object: schemaorg.MusicComposition

@dataclass(frozen=True)
class contactPoint(RdfProperty):
    term = RdfTerm('contactPoint', 'https://schema.org/contactPoint', [])
    object: schemaorg.ContactPoint

@dataclass(frozen=True)
class structuralClass(RdfProperty):
    term = RdfTerm('structuralClass', 'https://schema.org/structuralClass', [])
    object: Text

@dataclass(frozen=True)
class applicableCountry(RdfProperty):
    term = RdfTerm('applicableCountry', 'https://schema.org/applicableCountry', [])
    object: schemaorg.Country | Text

@dataclass(frozen=True)
class pregnancyCategory(RdfProperty):
    term = RdfTerm('pregnancyCategory', 'https://schema.org/pregnancyCategory', [])
    object: schemaorg.DrugPregnancyCategory

@dataclass(frozen=True)
class pageEnd(RdfProperty):
    term = RdfTerm('pageEnd', 'https://schema.org/pageEnd', [])
    object: Text | Integer

@dataclass(frozen=True)
class question(RdfProperty):
    term = RdfTerm('question', 'https://schema.org/question', [])
    object: schemaorg.Question

@dataclass(frozen=True)
class jobLocationType(RdfProperty):
    term = RdfTerm('jobLocationType', 'https://schema.org/jobLocationType', [])
    object: Text

@dataclass(frozen=True)
class runtimePlatform(RdfProperty):
    term = RdfTerm('runtimePlatform', 'https://schema.org/runtimePlatform', [])
    object: Text

@dataclass(frozen=True)
class legislationEnsuresImplementationOf(RdfProperty):
    term = RdfTerm('legislationEnsuresImplementationOf', 'https://schema.org/legislationEnsuresImplementationOf', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class priceCurrency(RdfProperty):
    term = RdfTerm('priceCurrency', 'https://schema.org/priceCurrency', [])
    object: Text

@dataclass(frozen=True)
class catalogNumber(RdfProperty):
    term = RdfTerm('catalogNumber', 'https://schema.org/catalogNumber', [])
    object: Text

@dataclass(frozen=True)
class event(RdfProperty):
    term = RdfTerm('event', 'https://schema.org/event', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class nerveMotor(RdfProperty):
    term = RdfTerm('nerveMotor', 'https://schema.org/nerveMotor', [])
    object: schemaorg.Muscle

@dataclass(frozen=True)
class employerOverview(RdfProperty):
    term = RdfTerm('employerOverview', 'https://schema.org/employerOverview', [])
    object: Text

@dataclass(frozen=True)
class medicalAudience(RdfProperty):
    term = RdfTerm('medicalAudience', 'https://schema.org/medicalAudience', [])
    object: schemaorg.MedicalAudienceType | schemaorg.MedicalAudience

@dataclass(frozen=True)
class rangeIncludes(RdfProperty):
    term = RdfTerm('rangeIncludes', 'https://schema.org/rangeIncludes', [])
    object: schemaorg.Class

@dataclass(frozen=True)
class publishedBy(RdfProperty):
    term = RdfTerm('publishedBy', 'https://schema.org/publishedBy', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class incentiveCompensation(RdfProperty):
    term = RdfTerm('incentiveCompensation', 'https://schema.org/incentiveCompensation', [])
    object: Text

@dataclass(frozen=True)
class illustrator(RdfProperty):
    term = RdfTerm('illustrator', 'https://schema.org/illustrator', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class paymentDueDate(RdfProperty):
    term = RdfTerm('paymentDueDate', 'https://schema.org/paymentDueDate', [])
    object: Date | DateTime

@dataclass(frozen=True)
class exceptDate(RdfProperty):
    term = RdfTerm('exceptDate', 'https://schema.org/exceptDate', [])
    object: Date | DateTime

@dataclass(frozen=True)
class legislationRepeals(RdfProperty):
    term = RdfTerm('legislationRepeals', 'https://schema.org/legislationRepeals', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class albumProductionType(RdfProperty):
    term = RdfTerm('albumProductionType', 'https://schema.org/albumProductionType', [])
    object: schemaorg.MusicAlbumProductionType

@dataclass(frozen=True)
class serviceOperator(RdfProperty):
    term = RdfTerm('serviceOperator', 'https://schema.org/serviceOperator', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class followup(RdfProperty):
    term = RdfTerm('followup', 'https://schema.org/followup', [])
    object: Text

@dataclass(frozen=True)
class numberOfRooms(RdfProperty):
    term = RdfTerm('numberOfRooms', 'https://schema.org/numberOfRooms', [])
    object: schemaorg.QuantitativeValue | Number

@dataclass(frozen=True)
class area(RdfProperty):
    term = RdfTerm('area', 'https://schema.org/area', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class reviewAspect(RdfProperty):
    term = RdfTerm('reviewAspect', 'https://schema.org/reviewAspect', [])
    object: Text

@dataclass(frozen=True)
class volumeNumber(RdfProperty):
    term = RdfTerm('volumeNumber', 'https://schema.org/volumeNumber', [])
    object: Integer | Text

@dataclass(frozen=True)
class bodyLocation(RdfProperty):
    term = RdfTerm('bodyLocation', 'https://schema.org/bodyLocation', [])
    object: Text

@dataclass(frozen=True)
class surface(RdfProperty):
    term = RdfTerm('surface', 'https://schema.org/surface', [])
    object: Text | URL

@dataclass(frozen=True)
class program(RdfProperty):
    term = RdfTerm('program', 'https://schema.org/program', [])
    object: schemaorg.MemberProgram

@dataclass(frozen=True)
class targetCollection(RdfProperty):
    term = RdfTerm('targetCollection', 'https://schema.org/targetCollection', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class loanType(RdfProperty):
    term = RdfTerm('loanType', 'https://schema.org/loanType', [])
    object: Text | URL

@dataclass(frozen=True)
class associatedAnatomy(RdfProperty):
    term = RdfTerm('associatedAnatomy', 'https://schema.org/associatedAnatomy', [])
    object: schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem | schemaorg.SuperficialAnatomy

@dataclass(frozen=True)
class numberOfFullBathrooms(RdfProperty):
    term = RdfTerm('numberOfFullBathrooms', 'https://schema.org/numberOfFullBathrooms', [])
    object: Number

@dataclass(frozen=True)
class arterialBranch(RdfProperty):
    term = RdfTerm('arterialBranch', 'https://schema.org/arterialBranch', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class costPerUnit(RdfProperty):
    term = RdfTerm('costPerUnit', 'https://schema.org/costPerUnit', [])
    object: schemaorg.QualitativeValue | Number | Text

@dataclass(frozen=True)
class correctionsPolicy(RdfProperty):
    term = RdfTerm('correctionsPolicy', 'https://schema.org/correctionsPolicy', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class serviceLocation(RdfProperty):
    term = RdfTerm('serviceLocation', 'https://schema.org/serviceLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class activeIngredient(RdfProperty):
    term = RdfTerm('activeIngredient', 'https://schema.org/activeIngredient', [])
    object: Text

@dataclass(frozen=True)
class additionalName(RdfProperty):
    term = RdfTerm('additionalName', 'https://schema.org/additionalName', [])
    object: Text

@dataclass(frozen=True)
class isAcceptingNewPatients(RdfProperty):
    term = RdfTerm('isAcceptingNewPatients', 'https://schema.org/isAcceptingNewPatients', [])
    object: Boolean

@dataclass(frozen=True)
class taxID(RdfProperty):
    term = RdfTerm('taxID', 'https://schema.org/taxID', [])
    object: Text

@dataclass(frozen=True)
class department(RdfProperty):
    term = RdfTerm('department', 'https://schema.org/department', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class legislationCorrects(RdfProperty):
    term = RdfTerm('legislationCorrects', 'https://schema.org/legislationCorrects', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class smiles(RdfProperty):
    term = RdfTerm('smiles', 'https://schema.org/smiles', [])
    object: Text

@dataclass(frozen=True)
class worstRating(RdfProperty):
    term = RdfTerm('worstRating', 'https://schema.org/worstRating', [])
    object: Text | Number

@dataclass(frozen=True)
class originalMediaContextDescription(RdfProperty):
    term = RdfTerm('originalMediaContextDescription', 'https://schema.org/originalMediaContextDescription', [])
    object: Text

@dataclass(frozen=True)
class workPresented(RdfProperty):
    term = RdfTerm('workPresented', 'https://schema.org/workPresented', [])
    object: schemaorg.Movie

@dataclass(frozen=True)
class study(RdfProperty):
    term = RdfTerm('study', 'https://schema.org/study', [])
    object: schemaorg.MedicalStudy

@dataclass(frozen=True)
class gameServer(RdfProperty):
    term = RdfTerm('gameServer', 'https://schema.org/gameServer', [])
    object: schemaorg.GameServer

@dataclass(frozen=True)
class broadcastOfEvent(RdfProperty):
    term = RdfTerm('broadcastOfEvent', 'https://schema.org/broadcastOfEvent', [])
    object: schemaorg.Event

@dataclass(frozen=True)
class gettingTestedInfo(RdfProperty):
    term = RdfTerm('gettingTestedInfo', 'https://schema.org/gettingTestedInfo', [])
    object: schemaorg.WebContent | URL

@dataclass(frozen=True)
class cheatCode(RdfProperty):
    term = RdfTerm('cheatCode', 'https://schema.org/cheatCode', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class shippingConditions(RdfProperty):
    term = RdfTerm('shippingConditions', 'https://schema.org/shippingConditions', [])
    object: schemaorg.ShippingConditions

@dataclass(frozen=True)
class collection(RdfProperty):
    term = RdfTerm('collection', 'https://schema.org/collection', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class fuelCapacity(RdfProperty):
    term = RdfTerm('fuelCapacity', 'https://schema.org/fuelCapacity', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class endOffset(RdfProperty):
    term = RdfTerm('endOffset', 'https://schema.org/endOffset', [])
    object: schemaorg.HyperTocEntry | Number

@dataclass(frozen=True)
class fileFormat(RdfProperty):
    term = RdfTerm('fileFormat', 'https://schema.org/fileFormat', [])
    object: Text | URL

@dataclass(frozen=True)
class financialAidEligible(RdfProperty):
    term = RdfTerm('financialAidEligible', 'https://schema.org/financialAidEligible', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class gtin13(RdfProperty):
    term = RdfTerm('gtin13', 'https://schema.org/gtin13', [])
    object: Text

@dataclass(frozen=True)
class shippingLabel(RdfProperty):
    term = RdfTerm('shippingLabel', 'https://schema.org/shippingLabel', [])
    object: Text

@dataclass(frozen=True)
class containedInPlace(RdfProperty):
    term = RdfTerm('containedInPlace', 'https://schema.org/containedInPlace', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class vehicleTransmission(RdfProperty):
    term = RdfTerm('vehicleTransmission', 'https://schema.org/vehicleTransmission', [])
    object: Text | URL | schemaorg.QualitativeValue

@dataclass(frozen=True)
class proprietaryName(RdfProperty):
    term = RdfTerm('proprietaryName', 'https://schema.org/proprietaryName', [])
    object: Text

@dataclass(frozen=True)
class breastfeedingWarning(RdfProperty):
    term = RdfTerm('breastfeedingWarning', 'https://schema.org/breastfeedingWarning', [])
    object: Text

@dataclass(frozen=True)
class episode(RdfProperty):
    term = RdfTerm('episode', 'https://schema.org/episode', [])
    object: schemaorg.Episode

@dataclass(frozen=True)
class hasDriveThroughService(RdfProperty):
    term = RdfTerm('hasDriveThroughService', 'https://schema.org/hasDriveThroughService', [])
    object: Boolean

@dataclass(frozen=True)
class vehicleIdentificationNumber(RdfProperty):
    term = RdfTerm('vehicleIdentificationNumber', 'https://schema.org/vehicleIdentificationNumber', [])
    object: Text

@dataclass(frozen=True)
class interpretedAsClaim(RdfProperty):
    term = RdfTerm('interpretedAsClaim', 'https://schema.org/interpretedAsClaim', [])
    object: schemaorg.Claim

@dataclass(frozen=True)
class founder(RdfProperty):
    term = RdfTerm('founder', 'https://schema.org/founder', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class applicationCategory(RdfProperty):
    term = RdfTerm('applicationCategory', 'https://schema.org/applicationCategory', [])
    object: Text | URL

@dataclass(frozen=True)
class passengerSequenceNumber(RdfProperty):
    term = RdfTerm('passengerSequenceNumber', 'https://schema.org/passengerSequenceNumber', [])
    object: Text

@dataclass(frozen=True)
class returnPolicyCategory(RdfProperty):
    term = RdfTerm('returnPolicyCategory', 'https://schema.org/returnPolicyCategory', [])
    object: schemaorg.MerchantReturnEnumeration

@dataclass(frozen=True)
class loanMortgageMandateAmount(RdfProperty):
    term = RdfTerm('loanMortgageMandateAmount', 'https://schema.org/loanMortgageMandateAmount', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class albums(RdfProperty):
    term = RdfTerm('albums', 'https://schema.org/albums', [])
    object: schemaorg.MusicAlbum

@dataclass(frozen=True)
class employmentType(RdfProperty):
    term = RdfTerm('employmentType', 'https://schema.org/employmentType', [])
    object: Text

@dataclass(frozen=True)
class geoWithin(RdfProperty):
    term = RdfTerm('geoWithin', 'https://schema.org/geoWithin', [])
    object: schemaorg.GeospatialGeometry | schemaorg.Place

@dataclass(frozen=True)
class subtitleLanguage(RdfProperty):
    term = RdfTerm('subtitleLanguage', 'https://schema.org/subtitleLanguage', [])
    object: Text | schemaorg.Language

@dataclass(frozen=True)
class applicationDeadline(RdfProperty):
    term = RdfTerm('applicationDeadline', 'https://schema.org/applicationDeadline', [])
    object: Date | Text

@dataclass(frozen=True)
class seasons(RdfProperty):
    term = RdfTerm('seasons', 'https://schema.org/seasons', [])
    object: schemaorg.CreativeWorkSeason

@dataclass(frozen=True)
class paymentStatus(RdfProperty):
    term = RdfTerm('paymentStatus', 'https://schema.org/paymentStatus', [])
    object: schemaorg.PaymentStatusType | Text

@dataclass(frozen=True)
class inStoreReturnsOffered(RdfProperty):
    term = RdfTerm('inStoreReturnsOffered', 'https://schema.org/inStoreReturnsOffered', [])
    object: Boolean

@dataclass(frozen=True)
class fileSize(RdfProperty):
    term = RdfTerm('fileSize', 'https://schema.org/fileSize', [])
    object: Text

@dataclass(frozen=True)
class softwareHelp(RdfProperty):
    term = RdfTerm('softwareHelp', 'https://schema.org/softwareHelp', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class clipNumber(RdfProperty):
    term = RdfTerm('clipNumber', 'https://schema.org/clipNumber', [])
    object: Text | Integer

@dataclass(frozen=True)
class broker(RdfProperty):
    term = RdfTerm('broker', 'https://schema.org/broker', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class distinguishingSign(RdfProperty):
    term = RdfTerm('distinguishingSign', 'https://schema.org/distinguishingSign', [])
    object: schemaorg.MedicalSignOrSymptom

@dataclass(frozen=True)
class exerciseCourse(RdfProperty):
    term = RdfTerm('exerciseCourse', 'https://schema.org/exerciseCourse', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class containsSeason(RdfProperty):
    term = RdfTerm('containsSeason', 'https://schema.org/containsSeason', [])
    object: schemaorg.CreativeWorkSeason

@dataclass(frozen=True)
class rsvpResponse(RdfProperty):
    term = RdfTerm('rsvpResponse', 'https://schema.org/rsvpResponse', [])
    object: schemaorg.RsvpResponseType

@dataclass(frozen=True)
class incentivizedItem(RdfProperty):
    term = RdfTerm('incentivizedItem', 'https://schema.org/incentivizedItem', [])
    object: schemaorg.DefinedTerm | schemaorg.Product

@dataclass(frozen=True)
class pattern(RdfProperty):
    term = RdfTerm('pattern', 'https://schema.org/pattern', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class tocContinuation(RdfProperty):
    term = RdfTerm('tocContinuation', 'https://schema.org/tocContinuation', [])
    object: schemaorg.HyperTocEntry

@dataclass(frozen=True)
class description(RdfProperty):
    term = RdfTerm('description', 'https://schema.org/description', [])
    object: schemaorg.TextObject | Text

@dataclass(frozen=True)
class relatedCondition(RdfProperty):
    term = RdfTerm('relatedCondition', 'https://schema.org/relatedCondition', [])
    object: schemaorg.MedicalCondition

@dataclass(frozen=True)
class doseUnit(RdfProperty):
    term = RdfTerm('doseUnit', 'https://schema.org/doseUnit', [])
    object: Text

@dataclass(frozen=True)
class interactionStatistic(RdfProperty):
    term = RdfTerm('interactionStatistic', 'https://schema.org/interactionStatistic', [])
    object: schemaorg.InteractionCounter

@dataclass(frozen=True)
class drug(RdfProperty):
    term = RdfTerm('drug', 'https://schema.org/drug', [])
    object: schemaorg.Drug

@dataclass(frozen=True)
class steeringPosition(RdfProperty):
    term = RdfTerm('steeringPosition', 'https://schema.org/steeringPosition', [])
    object: schemaorg.SteeringPositionValue

@dataclass(frozen=True)
class hasDefinedTerm(RdfProperty):
    term = RdfTerm('hasDefinedTerm', 'https://schema.org/hasDefinedTerm', [])
    object: schemaorg.DefinedTerm

@dataclass(frozen=True)
class dateReceived(RdfProperty):
    term = RdfTerm('dateReceived', 'https://schema.org/dateReceived', [])
    object: DateTime

@dataclass(frozen=True)
class paymentMethodType(RdfProperty):
    term = RdfTerm('paymentMethodType', 'https://schema.org/paymentMethodType', [])
    object: schemaorg.PaymentMethodType

@dataclass(frozen=True)
class trailerWeight(RdfProperty):
    term = RdfTerm('trailerWeight', 'https://schema.org/trailerWeight', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class safetyConsideration(RdfProperty):
    term = RdfTerm('safetyConsideration', 'https://schema.org/safetyConsideration', [])
    object: Text

@dataclass(frozen=True)
class seatingCapacity(RdfProperty):
    term = RdfTerm('seatingCapacity', 'https://schema.org/seatingCapacity', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class productionDate(RdfProperty):
    term = RdfTerm('productionDate', 'https://schema.org/productionDate', [])
    object: Date

@dataclass(frozen=True)
class phoneticText(RdfProperty):
    term = RdfTerm('phoneticText', 'https://schema.org/phoneticText', [])
    object: Text

@dataclass(frozen=True)
class departureTerminal(RdfProperty):
    term = RdfTerm('departureTerminal', 'https://schema.org/departureTerminal', [])
    object: Text

@dataclass(frozen=True)
class encodesBioChemEntity(RdfProperty):
    term = RdfTerm('encodesBioChemEntity', 'https://schema.org/encodesBioChemEntity', [])
    object: schemaorg.BioChemEntity

@dataclass(frozen=True)
class orderQuantity(RdfProperty):
    term = RdfTerm('orderQuantity', 'https://schema.org/orderQuantity', [])
    object: Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class yearsInOperation(RdfProperty):
    term = RdfTerm('yearsInOperation', 'https://schema.org/yearsInOperation', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class manufacturer(RdfProperty):
    term = RdfTerm('manufacturer', 'https://schema.org/manufacturer', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class timeToComplete(RdfProperty):
    term = RdfTerm('timeToComplete', 'https://schema.org/timeToComplete', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class director(RdfProperty):
    term = RdfTerm('director', 'https://schema.org/director', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class isbn(RdfProperty):
    term = RdfTerm('isbn', 'https://schema.org/isbn', [])
    object: Text

@dataclass(frozen=True)
class relatedTo(RdfProperty):
    term = RdfTerm('relatedTo', 'https://schema.org/relatedTo', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class announcementLocation(RdfProperty):
    term = RdfTerm('announcementLocation', 'https://schema.org/announcementLocation', [])
    object: schemaorg.LocalBusiness | schemaorg.CivicStructure

@dataclass(frozen=True)
class parentItem(RdfProperty):
    term = RdfTerm('parentItem', 'https://schema.org/parentItem', [])
    object: schemaorg.CreativeWork | schemaorg.Comment

@dataclass(frozen=True)
class season(RdfProperty):
    term = RdfTerm('season', 'https://schema.org/season', [])
    object: schemaorg.CreativeWorkSeason | URL

@dataclass(frozen=True)
class availableIn(RdfProperty):
    term = RdfTerm('availableIn', 'https://schema.org/availableIn', [])
    object: schemaorg.AdministrativeArea

@dataclass(frozen=True)
class orderItemStatus(RdfProperty):
    term = RdfTerm('orderItemStatus', 'https://schema.org/orderItemStatus', [])
    object: schemaorg.OrderStatus

@dataclass(frozen=True)
class cvdFacilityId(RdfProperty):
    term = RdfTerm('cvdFacilityId', 'https://schema.org/cvdFacilityId', [])
    object: Text

@dataclass(frozen=True)
class blogPost(RdfProperty):
    term = RdfTerm('blogPost', 'https://schema.org/blogPost', [])
    object: schemaorg.BlogPosting

@dataclass(frozen=True)
class validUntil(RdfProperty):
    term = RdfTerm('validUntil', 'https://schema.org/validUntil', [])
    object: Date

@dataclass(frozen=True)
class duns(RdfProperty):
    term = RdfTerm('duns', 'https://schema.org/duns', [])
    object: Text

@dataclass(frozen=True)
class totalTime(RdfProperty):
    term = RdfTerm('totalTime', 'https://schema.org/totalTime', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class maximumVirtualAttendeeCapacity(RdfProperty):
    term = RdfTerm('maximumVirtualAttendeeCapacity', 'https://schema.org/maximumVirtualAttendeeCapacity', [])
    object: Integer

@dataclass(frozen=True)
class exerciseType(RdfProperty):
    term = RdfTerm('exerciseType', 'https://schema.org/exerciseType', [])
    object: Text

@dataclass(frozen=True)
class amountOfThisGood(RdfProperty):
    term = RdfTerm('amountOfThisGood', 'https://schema.org/amountOfThisGood', [])
    object: Number

@dataclass(frozen=True)
class paymentUrl(RdfProperty):
    term = RdfTerm('paymentUrl', 'https://schema.org/paymentUrl', [])
    object: URL

@dataclass(frozen=True)
class artist(RdfProperty):
    term = RdfTerm('artist', 'https://schema.org/artist', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class language(RdfProperty):
    term = RdfTerm('language', 'https://schema.org/language', [])
    object: schemaorg.Language

@dataclass(frozen=True)
class connectedTo(RdfProperty):
    term = RdfTerm('connectedTo', 'https://schema.org/connectedTo', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class name(RdfProperty):
    term = RdfTerm('name', 'https://schema.org/name', [])
    object: Text

@dataclass(frozen=True)
class hasOfferCatalog(RdfProperty):
    term = RdfTerm('hasOfferCatalog', 'https://schema.org/hasOfferCatalog', [])
    object: schemaorg.OfferCatalog

@dataclass(frozen=True)
class ticketNumber(RdfProperty):
    term = RdfTerm('ticketNumber', 'https://schema.org/ticketNumber', [])
    object: Text

@dataclass(frozen=True)
class eligibleCustomerType(RdfProperty):
    term = RdfTerm('eligibleCustomerType', 'https://schema.org/eligibleCustomerType', [])
    object: schemaorg.BusinessEntityType

@dataclass(frozen=True)
class inventoryLevel(RdfProperty):
    term = RdfTerm('inventoryLevel', 'https://schema.org/inventoryLevel', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class broadcastSubChannel(RdfProperty):
    term = RdfTerm('broadcastSubChannel', 'https://schema.org/broadcastSubChannel', [])
    object: Text

@dataclass(frozen=True)
class sportsTeam(RdfProperty):
    term = RdfTerm('sportsTeam', 'https://schema.org/sportsTeam', [])
    object: schemaorg.SportsTeam

@dataclass(frozen=True)
class layoutImage(RdfProperty):
    term = RdfTerm('layoutImage', 'https://schema.org/layoutImage', [])
    object: schemaorg.ImageObject | URL

@dataclass(frozen=True)
class translator(RdfProperty):
    term = RdfTerm('translator', 'https://schema.org/translator', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class softwareAddOn(RdfProperty):
    term = RdfTerm('softwareAddOn', 'https://schema.org/softwareAddOn', [])
    object: schemaorg.SoftwareApplication

@dataclass(frozen=True)
class targetDescription(RdfProperty):
    term = RdfTerm('targetDescription', 'https://schema.org/targetDescription', [])
    object: Text

@dataclass(frozen=True)
class actionApplication(RdfProperty):
    term = RdfTerm('actionApplication', 'https://schema.org/actionApplication', [])
    object: schemaorg.SoftwareApplication

@dataclass(frozen=True)
class knows(RdfProperty):
    term = RdfTerm('knows', 'https://schema.org/knows', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class occupancy(RdfProperty):
    term = RdfTerm('occupancy', 'https://schema.org/occupancy', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class warning(RdfProperty):
    term = RdfTerm('warning', 'https://schema.org/warning', [])
    object: Text | URL

@dataclass(frozen=True)
class suggestedAge(RdfProperty):
    term = RdfTerm('suggestedAge', 'https://schema.org/suggestedAge', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class merchantReturnDays(RdfProperty):
    term = RdfTerm('merchantReturnDays', 'https://schema.org/merchantReturnDays', [])
    object: Date | Integer | DateTime

@dataclass(frozen=True)
class publishingPrinciples(RdfProperty):
    term = RdfTerm('publishingPrinciples', 'https://schema.org/publishingPrinciples', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class discusses(RdfProperty):
    term = RdfTerm('discusses', 'https://schema.org/discusses', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class hospitalAffiliation(RdfProperty):
    term = RdfTerm('hospitalAffiliation', 'https://schema.org/hospitalAffiliation', [])
    object: schemaorg.Hospital

@dataclass(frozen=True)
class medicineSystem(RdfProperty):
    term = RdfTerm('medicineSystem', 'https://schema.org/medicineSystem', [])
    object: schemaorg.MedicineSystem

@dataclass(frozen=True)
class accessibilitySummary(RdfProperty):
    term = RdfTerm('accessibilitySummary', 'https://schema.org/accessibilitySummary', [])
    object: Text

@dataclass(frozen=True)
class eligibleTransactionVolume(RdfProperty):
    term = RdfTerm('eligibleTransactionVolume', 'https://schema.org/eligibleTransactionVolume', [])
    object: schemaorg.PriceSpecification

@dataclass(frozen=True)
class encodingFormat(RdfProperty):
    term = RdfTerm('encodingFormat', 'https://schema.org/encodingFormat', [])
    object: Text | URL

@dataclass(frozen=True)
class musicalKey(RdfProperty):
    term = RdfTerm('musicalKey', 'https://schema.org/musicalKey', [])
    object: Text

@dataclass(frozen=True)
class referencesOrder(RdfProperty):
    term = RdfTerm('referencesOrder', 'https://schema.org/referencesOrder', [])
    object: schemaorg.Order

@dataclass(frozen=True)
class ratingExplanation(RdfProperty):
    term = RdfTerm('ratingExplanation', 'https://schema.org/ratingExplanation', [])
    object: Text

@dataclass(frozen=True)
class partySize(RdfProperty):
    term = RdfTerm('partySize', 'https://schema.org/partySize', [])
    object: schemaorg.QuantitativeValue | Integer

@dataclass(frozen=True)
class publishedOn(RdfProperty):
    term = RdfTerm('publishedOn', 'https://schema.org/publishedOn', [])
    object: schemaorg.BroadcastService

@dataclass(frozen=True)
class recommendedIntake(RdfProperty):
    term = RdfTerm('recommendedIntake', 'https://schema.org/recommendedIntake', [])
    object: schemaorg.RecommendedDoseSchedule

@dataclass(frozen=True)
class taxonomicRange(RdfProperty):
    term = RdfTerm('taxonomicRange', 'https://schema.org/taxonomicRange', [])
    object: schemaorg.DefinedTerm | Text | URL | schemaorg.Taxon

@dataclass(frozen=True)
class boardingGroup(RdfProperty):
    term = RdfTerm('boardingGroup', 'https://schema.org/boardingGroup', [])
    object: Text

@dataclass(frozen=True)
class additionalVariable(RdfProperty):
    term = RdfTerm('additionalVariable', 'https://schema.org/additionalVariable', [])
    object: Text

@dataclass(frozen=True)
class sodiumContent(RdfProperty):
    term = RdfTerm('sodiumContent', 'https://schema.org/sodiumContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class preparation(RdfProperty):
    term = RdfTerm('preparation', 'https://schema.org/preparation', [])
    object: schemaorg.MedicalEntity | Text

@dataclass(frozen=True)
class abridged(RdfProperty):
    term = RdfTerm('abridged', 'https://schema.org/abridged', [])
    object: Boolean

@dataclass(frozen=True)
class releaseOf(RdfProperty):
    term = RdfTerm('releaseOf', 'https://schema.org/releaseOf', [])
    object: schemaorg.MusicAlbum

@dataclass(frozen=True)
class pagination(RdfProperty):
    term = RdfTerm('pagination', 'https://schema.org/pagination', [])
    object: Text

@dataclass(frozen=True)
class ownedFrom(RdfProperty):
    term = RdfTerm('ownedFrom', 'https://schema.org/ownedFrom', [])
    object: DateTime

@dataclass(frozen=True)
class isVariantOf(RdfProperty):
    term = RdfTerm('isVariantOf', 'https://schema.org/isVariantOf', [])
    object: schemaorg.ProductGroup | schemaorg.ProductModel

@dataclass(frozen=True)
class homeTeam(RdfProperty):
    term = RdfTerm('homeTeam', 'https://schema.org/homeTeam', [])
    object: schemaorg.SportsTeam | schemaorg.Person

@dataclass(frozen=True)
class expectedArrivalFrom(RdfProperty):
    term = RdfTerm('expectedArrivalFrom', 'https://schema.org/expectedArrivalFrom', [])
    object: Date | DateTime

@dataclass(frozen=True)
class studyLocation(RdfProperty):
    term = RdfTerm('studyLocation', 'https://schema.org/studyLocation', [])
    object: schemaorg.AdministrativeArea

@dataclass(frozen=True)
class arrivalAirport(RdfProperty):
    term = RdfTerm('arrivalAirport', 'https://schema.org/arrivalAirport', [])
    object: schemaorg.Airport

@dataclass(frozen=True)
class imagingTechnique(RdfProperty):
    term = RdfTerm('imagingTechnique', 'https://schema.org/imagingTechnique', [])
    object: schemaorg.MedicalImagingTechnique

@dataclass(frozen=True)
class pickupLocation(RdfProperty):
    term = RdfTerm('pickupLocation', 'https://schema.org/pickupLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class userInteractionCount(RdfProperty):
    term = RdfTerm('userInteractionCount', 'https://schema.org/userInteractionCount', [])
    object: Integer

@dataclass(frozen=True)
class requiresSubscription(RdfProperty):
    term = RdfTerm('requiresSubscription', 'https://schema.org/requiresSubscription', [])
    object: schemaorg.MediaSubscription | Boolean

@dataclass(frozen=True)
class episodeNumber(RdfProperty):
    term = RdfTerm('episodeNumber', 'https://schema.org/episodeNumber', [])
    object: Integer | Text

@dataclass(frozen=True)
class spatial(RdfProperty):
    term = RdfTerm('spatial', 'https://schema.org/spatial', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class photo(RdfProperty):
    term = RdfTerm('photo', 'https://schema.org/photo', [])
    object: schemaorg.ImageObject | schemaorg.Photograph

@dataclass(frozen=True)
class penciler(RdfProperty):
    term = RdfTerm('penciler', 'https://schema.org/penciler', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class actionOption(RdfProperty):
    term = RdfTerm('actionOption', 'https://schema.org/actionOption', [])
    object: schemaorg.Thing | Text

@dataclass(frozen=True)
class assesses(RdfProperty):
    term = RdfTerm('assesses', 'https://schema.org/assesses', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class numberOfSeasons(RdfProperty):
    term = RdfTerm('numberOfSeasons', 'https://schema.org/numberOfSeasons', [])
    object: Integer

@dataclass(frozen=True)
class associatedPathophysiology(RdfProperty):
    term = RdfTerm('associatedPathophysiology', 'https://schema.org/associatedPathophysiology', [])
    object: Text

@dataclass(frozen=True)
class toLocation(RdfProperty):
    term = RdfTerm('toLocation', 'https://schema.org/toLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class countriesNotSupported(RdfProperty):
    term = RdfTerm('countriesNotSupported', 'https://schema.org/countriesNotSupported', [])
    object: Text

@dataclass(frozen=True)
class courseSchedule(RdfProperty):
    term = RdfTerm('courseSchedule', 'https://schema.org/courseSchedule', [])
    object: schemaorg.Schedule

@dataclass(frozen=True)
class orderDelivery(RdfProperty):
    term = RdfTerm('orderDelivery', 'https://schema.org/orderDelivery', [])
    object: schemaorg.ParcelDelivery

@dataclass(frozen=True)
class fiberContent(RdfProperty):
    term = RdfTerm('fiberContent', 'https://schema.org/fiberContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class partOfSystem(RdfProperty):
    term = RdfTerm('partOfSystem', 'https://schema.org/partOfSystem', [])
    object: schemaorg.AnatomicalSystem

@dataclass(frozen=True)
class associatedClaimReview(RdfProperty):
    term = RdfTerm('associatedClaimReview', 'https://schema.org/associatedClaimReview', [])
    object: schemaorg.Review

@dataclass(frozen=True)
class partOfEpisode(RdfProperty):
    term = RdfTerm('partOfEpisode', 'https://schema.org/partOfEpisode', [])
    object: schemaorg.Episode

@dataclass(frozen=True)
class hostingOrganization(RdfProperty):
    term = RdfTerm('hostingOrganization', 'https://schema.org/hostingOrganization', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class isEncodedByBioChemEntity(RdfProperty):
    term = RdfTerm('isEncodedByBioChemEntity', 'https://schema.org/isEncodedByBioChemEntity', [])
    object: schemaorg.Gene

@dataclass(frozen=True)
class status(RdfProperty):
    term = RdfTerm('status', 'https://schema.org/status', [])
    object: Text | schemaorg.EventStatusType | schemaorg.MedicalStudyStatus

@dataclass(frozen=True)
class greaterOrEqual(RdfProperty):
    term = RdfTerm('greaterOrEqual', 'https://schema.org/greaterOrEqual', [])
    object: schemaorg.QualitativeValue

@dataclass(frozen=True)
class answerCount(RdfProperty):
    term = RdfTerm('answerCount', 'https://schema.org/answerCount', [])
    object: Integer

@dataclass(frozen=True)
class geoRadius(RdfProperty):
    term = RdfTerm('geoRadius', 'https://schema.org/geoRadius', [])
    object: schemaorg.Distance | Number | Text

@dataclass(frozen=True)
class gtin8(RdfProperty):
    term = RdfTerm('gtin8', 'https://schema.org/gtin8', [])
    object: Text

@dataclass(frozen=True)
class studyDesign(RdfProperty):
    term = RdfTerm('studyDesign', 'https://schema.org/studyDesign', [])
    object: schemaorg.MedicalObservationalStudyDesign

@dataclass(frozen=True)
class actors(RdfProperty):
    term = RdfTerm('actors', 'https://schema.org/actors', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class weightTotal(RdfProperty):
    term = RdfTerm('weightTotal', 'https://schema.org/weightTotal', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class mathExpression(RdfProperty):
    term = RdfTerm('mathExpression', 'https://schema.org/mathExpression', [])
    object: Text | schemaorg.SolveMathAction

@dataclass(frozen=True)
class responsibilities(RdfProperty):
    term = RdfTerm('responsibilities', 'https://schema.org/responsibilities', [])
    object: Text

@dataclass(frozen=True)
class cookTime(RdfProperty):
    term = RdfTerm('cookTime', 'https://schema.org/cookTime', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class experienceInPlaceOfEducation(RdfProperty):
    term = RdfTerm('experienceInPlaceOfEducation', 'https://schema.org/experienceInPlaceOfEducation', [])
    object: Boolean

@dataclass(frozen=True)
class productGroupID(RdfProperty):
    term = RdfTerm('productGroupID', 'https://schema.org/productGroupID', [])
    object: Text

@dataclass(frozen=True)
class text(RdfProperty):
    term = RdfTerm('text', 'https://schema.org/text', [])
    object: Text

@dataclass(frozen=True)
class occupationalCategory(RdfProperty):
    term = RdfTerm('occupationalCategory', 'https://schema.org/occupationalCategory', [])
    object: Text | schemaorg.CategoryCode

@dataclass(frozen=True)
class practicesAt(RdfProperty):
    term = RdfTerm('practicesAt', 'https://schema.org/practicesAt', [])
    object: schemaorg.MedicalOrganization

@dataclass(frozen=True)
class availableFrom(RdfProperty):
    term = RdfTerm('availableFrom', 'https://schema.org/availableFrom', [])
    object: DateTime

@dataclass(frozen=True)
class eduQuestionType(RdfProperty):
    term = RdfTerm('eduQuestionType', 'https://schema.org/eduQuestionType', [])
    object: Text

@dataclass(frozen=True)
class availabilityEnds(RdfProperty):
    term = RdfTerm('availabilityEnds', 'https://schema.org/availabilityEnds', [])
    object: Date | DateTime | Time

@dataclass(frozen=True)
class mealService(RdfProperty):
    term = RdfTerm('mealService', 'https://schema.org/mealService', [])
    object: Text

@dataclass(frozen=True)
class deliveryMethod(RdfProperty):
    term = RdfTerm('deliveryMethod', 'https://schema.org/deliveryMethod', [])
    object: schemaorg.DeliveryMethod

@dataclass(frozen=True)
class numberOfBathroomsTotal(RdfProperty):
    term = RdfTerm('numberOfBathroomsTotal', 'https://schema.org/numberOfBathroomsTotal', [])
    object: Integer

@dataclass(frozen=True)
class trailer(RdfProperty):
    term = RdfTerm('trailer', 'https://schema.org/trailer', [])
    object: schemaorg.VideoObject

@dataclass(frozen=True)
class copyrightHolder(RdfProperty):
    term = RdfTerm('copyrightHolder', 'https://schema.org/copyrightHolder', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class possibleComplication(RdfProperty):
    term = RdfTerm('possibleComplication', 'https://schema.org/possibleComplication', [])
    object: Text

@dataclass(frozen=True)
class vehicleInteriorColor(RdfProperty):
    term = RdfTerm('vehicleInteriorColor', 'https://schema.org/vehicleInteriorColor', [])
    object: Text

@dataclass(frozen=True)
class parentOrganization(RdfProperty):
    term = RdfTerm('parentOrganization', 'https://schema.org/parentOrganization', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class advanceBookingRequirement(RdfProperty):
    term = RdfTerm('advanceBookingRequirement', 'https://schema.org/advanceBookingRequirement', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class customer(RdfProperty):
    term = RdfTerm('customer', 'https://schema.org/customer', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class mobileUrl(RdfProperty):
    term = RdfTerm('mobileUrl', 'https://schema.org/mobileUrl', [])
    object: Text

@dataclass(frozen=True)
class beneficiaryBank(RdfProperty):
    term = RdfTerm('beneficiaryBank', 'https://schema.org/beneficiaryBank', [])
    object: schemaorg.BankOrCreditUnion | Text

@dataclass(frozen=True)
class fatContent(RdfProperty):
    term = RdfTerm('fatContent', 'https://schema.org/fatContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class digitalSourceType(RdfProperty):
    term = RdfTerm('digitalSourceType', 'https://schema.org/digitalSourceType', [])
    object: schemaorg.IPTCDigitalSourceEnumeration

@dataclass(frozen=True)
class memoryRequirements(RdfProperty):
    term = RdfTerm('memoryRequirements', 'https://schema.org/memoryRequirements', [])
    object: Text | URL

@dataclass(frozen=True)
class partOfTVSeries(RdfProperty):
    term = RdfTerm('partOfTVSeries', 'https://schema.org/partOfTVSeries', [])
    object: schemaorg.TVSeries

@dataclass(frozen=True)
class seatRow(RdfProperty):
    term = RdfTerm('seatRow', 'https://schema.org/seatRow', [])
    object: Text

@dataclass(frozen=True)
class replacer(RdfProperty):
    term = RdfTerm('replacer', 'https://schema.org/replacer', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class learningResourceType(RdfProperty):
    term = RdfTerm('learningResourceType', 'https://schema.org/learningResourceType', [])
    object: schemaorg.DefinedTerm | Text

@dataclass(frozen=True)
class runtime(RdfProperty):
    term = RdfTerm('runtime', 'https://schema.org/runtime', [])
    object: Text

@dataclass(frozen=True)
class game(RdfProperty):
    term = RdfTerm('game', 'https://schema.org/game', [])
    object: schemaorg.VideoGame

@dataclass(frozen=True)
class numAdults(RdfProperty):
    term = RdfTerm('numAdults', 'https://schema.org/numAdults', [])
    object: schemaorg.QuantitativeValue | Integer

@dataclass(frozen=True)
class strengthValue(RdfProperty):
    term = RdfTerm('strengthValue', 'https://schema.org/strengthValue', [])
    object: Number

@dataclass(frozen=True)
class educationalFramework(RdfProperty):
    term = RdfTerm('educationalFramework', 'https://schema.org/educationalFramework', [])
    object: Text

@dataclass(frozen=True)
class requirements(RdfProperty):
    term = RdfTerm('requirements', 'https://schema.org/requirements', [])
    object: Text | URL

@dataclass(frozen=True)
class funding(RdfProperty):
    term = RdfTerm('funding', 'https://schema.org/funding', [])
    object: schemaorg.Grant

@dataclass(frozen=True)
class trainNumber(RdfProperty):
    term = RdfTerm('trainNumber', 'https://schema.org/trainNumber', [])
    object: Text

@dataclass(frozen=True)
class weight(RdfProperty):
    term = RdfTerm('weight', 'https://schema.org/weight', [])
    object: schemaorg.QuantitativeValue | schemaorg.Mass

@dataclass(frozen=True)
class accountOverdraftLimit(RdfProperty):
    term = RdfTerm('accountOverdraftLimit', 'https://schema.org/accountOverdraftLimit', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class legislationAmends(RdfProperty):
    term = RdfTerm('legislationAmends', 'https://schema.org/legislationAmends', [])
    object: schemaorg.Legislation

@dataclass(frozen=True)
class diet(RdfProperty):
    term = RdfTerm('diet', 'https://schema.org/diet', [])
    object: schemaorg.Diet

@dataclass(frozen=True)
class highPrice(RdfProperty):
    term = RdfTerm('highPrice', 'https://schema.org/highPrice', [])
    object: Number | Text

@dataclass(frozen=True)
class containedIn(RdfProperty):
    term = RdfTerm('containedIn', 'https://schema.org/containedIn', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class servicePostalAddress(RdfProperty):
    term = RdfTerm('servicePostalAddress', 'https://schema.org/servicePostalAddress', [])
    object: schemaorg.PostalAddress

@dataclass(frozen=True)
class character(RdfProperty):
    term = RdfTerm('character', 'https://schema.org/character', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class arrivalStation(RdfProperty):
    term = RdfTerm('arrivalStation', 'https://schema.org/arrivalStation', [])
    object: schemaorg.TrainStation

@dataclass(frozen=True)
class workExample(RdfProperty):
    term = RdfTerm('workExample', 'https://schema.org/workExample', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class replyToUrl(RdfProperty):
    term = RdfTerm('replyToUrl', 'https://schema.org/replyToUrl', [])
    object: URL

@dataclass(frozen=True)
class contentReferenceTime(RdfProperty):
    term = RdfTerm('contentReferenceTime', 'https://schema.org/contentReferenceTime', [])
    object: DateTime

@dataclass(frozen=True)
class productionCompany(RdfProperty):
    term = RdfTerm('productionCompany', 'https://schema.org/productionCompany', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class greater(RdfProperty):
    term = RdfTerm('greater', 'https://schema.org/greater', [])
    object: schemaorg.QualitativeValue

@dataclass(frozen=True)
class permitAudience(RdfProperty):
    term = RdfTerm('permitAudience', 'https://schema.org/permitAudience', [])
    object: schemaorg.Audience

@dataclass(frozen=True)
class datePosted(RdfProperty):
    term = RdfTerm('datePosted', 'https://schema.org/datePosted', [])
    object: Date | DateTime

@dataclass(frozen=True)
class hasMap(RdfProperty):
    term = RdfTerm('hasMap', 'https://schema.org/hasMap', [])
    object: URL | schemaorg.Map

@dataclass(frozen=True)
class hasRepresentation(RdfProperty):
    term = RdfTerm('hasRepresentation', 'https://schema.org/hasRepresentation', [])
    object: schemaorg.PropertyValue | Text | URL

@dataclass(frozen=True)
class median(RdfProperty):
    term = RdfTerm('median', 'https://schema.org/median', [])
    object: Number

@dataclass(frozen=True)
class confirmationNumber(RdfProperty):
    term = RdfTerm('confirmationNumber', 'https://schema.org/confirmationNumber', [])
    object: Text

@dataclass(frozen=True)
class productID(RdfProperty):
    term = RdfTerm('productID', 'https://schema.org/productID', [])
    object: Text

@dataclass(frozen=True)
class actionAccessibilityRequirement(RdfProperty):
    term = RdfTerm('actionAccessibilityRequirement', 'https://schema.org/actionAccessibilityRequirement', [])
    object: schemaorg.ActionAccessSpecification

@dataclass(frozen=True)
class numberOfPages(RdfProperty):
    term = RdfTerm('numberOfPages', 'https://schema.org/numberOfPages', [])
    object: Integer

@dataclass(frozen=True)
class expectedArrivalUntil(RdfProperty):
    term = RdfTerm('expectedArrivalUntil', 'https://schema.org/expectedArrivalUntil', [])
    object: Date | DateTime

@dataclass(frozen=True)
class inverseOf(RdfProperty):
    term = RdfTerm('inverseOf', 'https://schema.org/inverseOf', [])
    object: schemaorg.Property

@dataclass(frozen=True)
class encodings(RdfProperty):
    term = RdfTerm('encodings', 'https://schema.org/encodings', [])
    object: schemaorg.MediaObject

@dataclass(frozen=True)
class muscleAction(RdfProperty):
    term = RdfTerm('muscleAction', 'https://schema.org/muscleAction', [])
    object: Text

@dataclass(frozen=True)
class unsaturatedFatContent(RdfProperty):
    term = RdfTerm('unsaturatedFatContent', 'https://schema.org/unsaturatedFatContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class chemicalRole(RdfProperty):
    term = RdfTerm('chemicalRole', 'https://schema.org/chemicalRole', [])
    object: schemaorg.DefinedTerm

@dataclass(frozen=True)
class employees(RdfProperty):
    term = RdfTerm('employees', 'https://schema.org/employees', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class caption(RdfProperty):
    term = RdfTerm('caption', 'https://schema.org/caption', [])
    object: Text | schemaorg.MediaObject

@dataclass(frozen=True)
class guidelineSubject(RdfProperty):
    term = RdfTerm('guidelineSubject', 'https://schema.org/guidelineSubject', [])
    object: schemaorg.MedicalEntity

@dataclass(frozen=True)
class agent(RdfProperty):
    term = RdfTerm('agent', 'https://schema.org/agent', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class departureGate(RdfProperty):
    term = RdfTerm('departureGate', 'https://schema.org/departureGate', [])
    object: Text

@dataclass(frozen=True)
class result(RdfProperty):
    term = RdfTerm('result', 'https://schema.org/result', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class measurementTechnique(RdfProperty):
    term = RdfTerm('measurementTechnique', 'https://schema.org/measurementTechnique', [])
    object: schemaorg.DefinedTerm | Text | schemaorg.MeasurementMethodEnum | URL

@dataclass(frozen=True)
class includedInDataCatalog(RdfProperty):
    term = RdfTerm('includedInDataCatalog', 'https://schema.org/includedInDataCatalog', [])
    object: schemaorg.DataCatalog

@dataclass(frozen=True)
class costOrigin(RdfProperty):
    term = RdfTerm('costOrigin', 'https://schema.org/costOrigin', [])
    object: Text

@dataclass(frozen=True)
class hasEnergyEfficiencyCategory(RdfProperty):
    term = RdfTerm('hasEnergyEfficiencyCategory', 'https://schema.org/hasEnergyEfficiencyCategory', [])
    object: schemaorg.EnergyEfficiencyEnumeration

@dataclass(frozen=True)
class mileageFromOdometer(RdfProperty):
    term = RdfTerm('mileageFromOdometer', 'https://schema.org/mileageFromOdometer', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class trainingSalary(RdfProperty):
    term = RdfTerm('trainingSalary', 'https://schema.org/trainingSalary', [])
    object: schemaorg.MonetaryAmountDistribution

@dataclass(frozen=True)
class doseValue(RdfProperty):
    term = RdfTerm('doseValue', 'https://schema.org/doseValue', [])
    object: schemaorg.QualitativeValue | Number

@dataclass(frozen=True)
class qualifications(RdfProperty):
    term = RdfTerm('qualifications', 'https://schema.org/qualifications', [])
    object: Text | schemaorg.EducationalOccupationalCredential

@dataclass(frozen=True)
class credentialCategory(RdfProperty):
    term = RdfTerm('credentialCategory', 'https://schema.org/credentialCategory', [])
    object: schemaorg.DefinedTerm | Text | URL

@dataclass(frozen=True)
class isRelatedTo(RdfProperty):
    term = RdfTerm('isRelatedTo', 'https://schema.org/isRelatedTo', [])
    object: schemaorg.Product | schemaorg.Service

@dataclass(frozen=True)
class valuePattern(RdfProperty):
    term = RdfTerm('valuePattern', 'https://schema.org/valuePattern', [])
    object: Text

@dataclass(frozen=True)
class isResizable(RdfProperty):
    term = RdfTerm('isResizable', 'https://schema.org/isResizable', [])
    object: Boolean

@dataclass(frozen=True)
class relevantOccupation(RdfProperty):
    term = RdfTerm('relevantOccupation', 'https://schema.org/relevantOccupation', [])
    object: schemaorg.Occupation

@dataclass(frozen=True)
class taxonRank(RdfProperty):
    term = RdfTerm('taxonRank', 'https://schema.org/taxonRank', [])
    object: schemaorg.PropertyValue | Text | URL

@dataclass(frozen=True)
class offerCount(RdfProperty):
    term = RdfTerm('offerCount', 'https://schema.org/offerCount', [])
    object: Integer

@dataclass(frozen=True)
class serviceSmsNumber(RdfProperty):
    term = RdfTerm('serviceSmsNumber', 'https://schema.org/serviceSmsNumber', [])
    object: schemaorg.ContactPoint

@dataclass(frozen=True)
class citation(RdfProperty):
    term = RdfTerm('citation', 'https://schema.org/citation', [])
    object: schemaorg.CreativeWork | Text

@dataclass(frozen=True)
class recommendationStrength(RdfProperty):
    term = RdfTerm('recommendationStrength', 'https://schema.org/recommendationStrength', [])
    object: Text

@dataclass(frozen=True)
class originAddress(RdfProperty):
    term = RdfTerm('originAddress', 'https://schema.org/originAddress', [])
    object: schemaorg.PostalAddress

@dataclass(frozen=True)
class agentInteractionStatistic(RdfProperty):
    term = RdfTerm('agentInteractionStatistic', 'https://schema.org/agentInteractionStatistic', [])
    object: schemaorg.InteractionCounter

@dataclass(frozen=True)
class followee(RdfProperty):
    term = RdfTerm('followee', 'https://schema.org/followee', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class subjectOf(RdfProperty):
    term = RdfTerm('subjectOf', 'https://schema.org/subjectOf', [])
    object: schemaorg.Event | schemaorg.CreativeWork

@dataclass(frozen=True)
class paymentDue(RdfProperty):
    term = RdfTerm('paymentDue', 'https://schema.org/paymentDue', [])
    object: DateTime

@dataclass(frozen=True)
class duration(RdfProperty):
    term = RdfTerm('duration', 'https://schema.org/duration', [])
    object: schemaorg.QuantitativeValue | schemaorg.Duration

@dataclass(frozen=True)
class prepTime(RdfProperty):
    term = RdfTerm('prepTime', 'https://schema.org/prepTime', [])
    object: schemaorg.Duration

@dataclass(frozen=True)
class reviewBody(RdfProperty):
    term = RdfTerm('reviewBody', 'https://schema.org/reviewBody', [])
    object: Text

@dataclass(frozen=True)
class availableChannel(RdfProperty):
    term = RdfTerm('availableChannel', 'https://schema.org/availableChannel', [])
    object: schemaorg.ServiceChannel

@dataclass(frozen=True)
class contentLocation(RdfProperty):
    term = RdfTerm('contentLocation', 'https://schema.org/contentLocation', [])
    object: schemaorg.Place

@dataclass(frozen=True)
class expressedIn(RdfProperty):
    term = RdfTerm('expressedIn', 'https://schema.org/expressedIn', [])
    object: schemaorg.BioChemEntity | schemaorg.DefinedTerm | schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem

@dataclass(frozen=True)
class publisher(RdfProperty):
    term = RdfTerm('publisher', 'https://schema.org/publisher', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class healthPlanDrugTier(RdfProperty):
    term = RdfTerm('healthPlanDrugTier', 'https://schema.org/healthPlanDrugTier', [])
    object: Text

@dataclass(frozen=True)
class numberOfEpisodes(RdfProperty):
    term = RdfTerm('numberOfEpisodes', 'https://schema.org/numberOfEpisodes', [])
    object: Integer

@dataclass(frozen=True)
class intensity(RdfProperty):
    term = RdfTerm('intensity', 'https://schema.org/intensity', [])
    object: schemaorg.QuantitativeValue | Text

@dataclass(frozen=True)
class floorLevel(RdfProperty):
    term = RdfTerm('floorLevel', 'https://schema.org/floorLevel', [])
    object: Text

@dataclass(frozen=True)
class recognizingAuthority(RdfProperty):
    term = RdfTerm('recognizingAuthority', 'https://schema.org/recognizingAuthority', [])
    object: schemaorg.Organization

@dataclass(frozen=True)
class billingAddress(RdfProperty):
    term = RdfTerm('billingAddress', 'https://schema.org/billingAddress', [])
    object: schemaorg.PostalAddress

@dataclass(frozen=True)
class contactPoints(RdfProperty):
    term = RdfTerm('contactPoints', 'https://schema.org/contactPoints', [])
    object: schemaorg.ContactPoint

@dataclass(frozen=True)
class accessibilityControl(RdfProperty):
    term = RdfTerm('accessibilityControl', 'https://schema.org/accessibilityControl', [])
    object: Text

@dataclass(frozen=True)
class driveWheelConfiguration(RdfProperty):
    term = RdfTerm('driveWheelConfiguration', 'https://schema.org/driveWheelConfiguration', [])
    object: Text | schemaorg.DriveWheelConfigurationValue

@dataclass(frozen=True)
class legislationLegalForce(RdfProperty):
    term = RdfTerm('legislationLegalForce', 'https://schema.org/legislationLegalForce', [])
    object: schemaorg.LegalForceStatus

@dataclass(frozen=True)
class byArtist(RdfProperty):
    term = RdfTerm('byArtist', 'https://schema.org/byArtist', [])
    object: schemaorg.Person | schemaorg.MusicGroup

@dataclass(frozen=True)
class replacee(RdfProperty):
    term = RdfTerm('replacee', 'https://schema.org/replacee', [])
    object: schemaorg.Thing

@dataclass(frozen=True)
class interactivityType(RdfProperty):
    term = RdfTerm('interactivityType', 'https://schema.org/interactivityType', [])
    object: Text

@dataclass(frozen=True)
class molecularFormula(RdfProperty):
    term = RdfTerm('molecularFormula', 'https://schema.org/molecularFormula', [])
    object: Text

@dataclass(frozen=True)
class supportingData(RdfProperty):
    term = RdfTerm('supportingData', 'https://schema.org/supportingData', [])
    object: schemaorg.DataFeed

@dataclass(frozen=True)
class loser(RdfProperty):
    term = RdfTerm('loser', 'https://schema.org/loser', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class sharedContent(RdfProperty):
    term = RdfTerm('sharedContent', 'https://schema.org/sharedContent', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class offers(RdfProperty):
    term = RdfTerm('offers', 'https://schema.org/offers', [])
    object: schemaorg.Demand | schemaorg.Offer

@dataclass(frozen=True)
class hasMenuItem(RdfProperty):
    term = RdfTerm('hasMenuItem', 'https://schema.org/hasMenuItem', [])
    object: schemaorg.MenuItem

@dataclass(frozen=True)
class percentile25(RdfProperty):
    term = RdfTerm('percentile25', 'https://schema.org/percentile25', [])
    object: Number

@dataclass(frozen=True)
class bookingTime(RdfProperty):
    term = RdfTerm('bookingTime', 'https://schema.org/bookingTime', [])
    object: DateTime

@dataclass(frozen=True)
class alignmentType(RdfProperty):
    term = RdfTerm('alignmentType', 'https://schema.org/alignmentType', [])
    object: Text

@dataclass(frozen=True)
class pageStart(RdfProperty):
    term = RdfTerm('pageStart', 'https://schema.org/pageStart', [])
    object: Integer | Text

@dataclass(frozen=True)
class bookingAgent(RdfProperty):
    term = RdfTerm('bookingAgent', 'https://schema.org/bookingAgent', [])
    object: schemaorg.Organization | schemaorg.Person

@dataclass(frozen=True)
class softwareVersion(RdfProperty):
    term = RdfTerm('softwareVersion', 'https://schema.org/softwareVersion', [])
    object: Text

@dataclass(frozen=True)
class checkoutTime(RdfProperty):
    term = RdfTerm('checkoutTime', 'https://schema.org/checkoutTime', [])
    object: DateTime | Time

@dataclass(frozen=True)
class starRating(RdfProperty):
    term = RdfTerm('starRating', 'https://schema.org/starRating', [])
    object: schemaorg.Rating

@dataclass(frozen=True)
class variantCover(RdfProperty):
    term = RdfTerm('variantCover', 'https://schema.org/variantCover', [])
    object: Text

@dataclass(frozen=True)
class jobStartDate(RdfProperty):
    term = RdfTerm('jobStartDate', 'https://schema.org/jobStartDate', [])
    object: Date | Text

@dataclass(frozen=True)
class ownedThrough(RdfProperty):
    term = RdfTerm('ownedThrough', 'https://schema.org/ownedThrough', [])
    object: DateTime

@dataclass(frozen=True)
class programPrerequisites(RdfProperty):
    term = RdfTerm('programPrerequisites', 'https://schema.org/programPrerequisites', [])
    object: schemaorg.AlignmentObject | schemaorg.Course | Text | schemaorg.EducationalOccupationalCredential

@dataclass(frozen=True)
class inBroadcastLineup(RdfProperty):
    term = RdfTerm('inBroadcastLineup', 'https://schema.org/inBroadcastLineup', [])
    object: schemaorg.CableOrSatelliteService

@dataclass(frozen=True)
class healthPlanCostSharing(RdfProperty):
    term = RdfTerm('healthPlanCostSharing', 'https://schema.org/healthPlanCostSharing', [])
    object: Boolean

@dataclass(frozen=True)
class postOp(RdfProperty):
    term = RdfTerm('postOp', 'https://schema.org/postOp', [])
    object: Text

@dataclass(frozen=True)
class cvdNumVentUse(RdfProperty):
    term = RdfTerm('cvdNumVentUse', 'https://schema.org/cvdNumVentUse', [])
    object: Number

@dataclass(frozen=True)
class flightDistance(RdfProperty):
    term = RdfTerm('flightDistance', 'https://schema.org/flightDistance', [])
    object: Text | schemaorg.Distance

@dataclass(frozen=True)
class sponsor(RdfProperty):
    term = RdfTerm('sponsor', 'https://schema.org/sponsor', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class paymentMethod(RdfProperty):
    term = RdfTerm('paymentMethod', 'https://schema.org/paymentMethod', [])
    object: schemaorg.PaymentMethod | Text

@dataclass(frozen=True)
class applicantLocationRequirements(RdfProperty):
    term = RdfTerm('applicantLocationRequirements', 'https://schema.org/applicantLocationRequirements', [])
    object: schemaorg.AdministrativeArea

@dataclass(frozen=True)
class transFatContent(RdfProperty):
    term = RdfTerm('transFatContent', 'https://schema.org/transFatContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class healthcareReportingData(RdfProperty):
    term = RdfTerm('healthcareReportingData', 'https://schema.org/healthcareReportingData', [])
    object: schemaorg.CDCPMDRecord | schemaorg.Dataset

@dataclass(frozen=True)
class negativeNotes(RdfProperty):
    term = RdfTerm('negativeNotes', 'https://schema.org/negativeNotes', [])
    object: schemaorg.ListItem | schemaorg.ItemList | schemaorg.WebContent | Text

@dataclass(frozen=True)
class cvdNumICUBeds(RdfProperty):
    term = RdfTerm('cvdNumICUBeds', 'https://schema.org/cvdNumICUBeds', [])
    object: Number

@dataclass(frozen=True)
class lodgingUnitType(RdfProperty):
    term = RdfTerm('lodgingUnitType', 'https://schema.org/lodgingUnitType', [])
    object: Text | schemaorg.QualitativeValue

@dataclass(frozen=True)
class keywords(RdfProperty):
    term = RdfTerm('keywords', 'https://schema.org/keywords', [])
    object: schemaorg.DefinedTerm | URL | Text

@dataclass(frozen=True)
class numberOfPlayers(RdfProperty):
    term = RdfTerm('numberOfPlayers', 'https://schema.org/numberOfPlayers', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class creditedTo(RdfProperty):
    term = RdfTerm('creditedTo', 'https://schema.org/creditedTo', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class producer(RdfProperty):
    term = RdfTerm('producer', 'https://schema.org/producer', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class purchasePriceLimit(RdfProperty):
    term = RdfTerm('purchasePriceLimit', 'https://schema.org/purchasePriceLimit', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class performer(RdfProperty):
    term = RdfTerm('performer', 'https://schema.org/performer', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class suitableForDiet(RdfProperty):
    term = RdfTerm('suitableForDiet', 'https://schema.org/suitableForDiet', [])
    object: schemaorg.RestrictedDiet

@dataclass(frozen=True)
class cholesterolContent(RdfProperty):
    term = RdfTerm('cholesterolContent', 'https://schema.org/cholesterolContent', [])
    object: schemaorg.Mass

@dataclass(frozen=True)
class fulfillmentType(RdfProperty):
    term = RdfTerm('fulfillmentType', 'https://schema.org/fulfillmentType', [])
    object: schemaorg.FulfillmentTypeEnumeration

@dataclass(frozen=True)
class recordedAs(RdfProperty):
    term = RdfTerm('recordedAs', 'https://schema.org/recordedAs', [])
    object: schemaorg.MusicRecording

@dataclass(frozen=True)
class encodesCreativeWork(RdfProperty):
    term = RdfTerm('encodesCreativeWork', 'https://schema.org/encodesCreativeWork', [])
    object: schemaorg.CreativeWork

@dataclass(frozen=True)
class valueMinLength(RdfProperty):
    term = RdfTerm('valueMinLength', 'https://schema.org/valueMinLength', [])
    object: Number

@dataclass(frozen=True)
class winner(RdfProperty):
    term = RdfTerm('winner', 'https://schema.org/winner', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class width(RdfProperty):
    term = RdfTerm('width', 'https://schema.org/width', [])
    object: schemaorg.QuantitativeValue | schemaorg.Distance

@dataclass(frozen=True)
class menu(RdfProperty):
    term = RdfTerm('menu', 'https://schema.org/menu', [])
    object: schemaorg.Menu | URL | Text

@dataclass(frozen=True)
class speechToTextMarkup(RdfProperty):
    term = RdfTerm('speechToTextMarkup', 'https://schema.org/speechToTextMarkup', [])
    object: Text

@dataclass(frozen=True)
class remainingAttendeeCapacity(RdfProperty):
    term = RdfTerm('remainingAttendeeCapacity', 'https://schema.org/remainingAttendeeCapacity', [])
    object: Integer

@dataclass(frozen=True)
class editor(RdfProperty):
    term = RdfTerm('editor', 'https://schema.org/editor', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class predecessorOf(RdfProperty):
    term = RdfTerm('predecessorOf', 'https://schema.org/predecessorOf', [])
    object: schemaorg.ProductModel

@dataclass(frozen=True)
class stupidProperty(RdfProperty):
    term = RdfTerm('stupidProperty', 'https://schema.org/stupidProperty', [])
    object: schemaorg.QuantitativeValue

@dataclass(frozen=True)
class transmissionMethod(RdfProperty):
    term = RdfTerm('transmissionMethod', 'https://schema.org/transmissionMethod', [])
    object: Text

@dataclass(frozen=True)
class honorificSuffix(RdfProperty):
    term = RdfTerm('honorificSuffix', 'https://schema.org/honorificSuffix', [])
    object: Text

@dataclass(frozen=True)
class monthlyMinimumRepaymentAmount(RdfProperty):
    term = RdfTerm('monthlyMinimumRepaymentAmount', 'https://schema.org/monthlyMinimumRepaymentAmount', [])
    object: Number | schemaorg.MonetaryAmount

@dataclass(frozen=True)
class hasMemberProgram(RdfProperty):
    term = RdfTerm('hasMemberProgram', 'https://schema.org/hasMemberProgram', [])
    object: schemaorg.MemberProgram

@dataclass(frozen=True)
class relatedStructure(RdfProperty):
    term = RdfTerm('relatedStructure', 'https://schema.org/relatedStructure', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class copyrightNotice(RdfProperty):
    term = RdfTerm('copyrightNotice', 'https://schema.org/copyrightNotice', [])
    object: Text

@dataclass(frozen=True)
class exerciseRelatedDiet(RdfProperty):
    term = RdfTerm('exerciseRelatedDiet', 'https://schema.org/exerciseRelatedDiet', [])
    object: schemaorg.Diet

@dataclass(frozen=True)
class priceComponentType(RdfProperty):
    term = RdfTerm('priceComponentType', 'https://schema.org/priceComponentType', [])
    object: schemaorg.PriceComponentTypeEnumeration

@dataclass(frozen=True)
class attendee(RdfProperty):
    term = RdfTerm('attendee', 'https://schema.org/attendee', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class totalPaymentDue(RdfProperty):
    term = RdfTerm('totalPaymentDue', 'https://schema.org/totalPaymentDue', [])
    object: schemaorg.PriceSpecification | schemaorg.MonetaryAmount

@dataclass(frozen=True)
class maxPrice(RdfProperty):
    term = RdfTerm('maxPrice', 'https://schema.org/maxPrice', [])
    object: Number

@dataclass(frozen=True)
class partOfInvoice(RdfProperty):
    term = RdfTerm('partOfInvoice', 'https://schema.org/partOfInvoice', [])
    object: schemaorg.Invoice

@dataclass(frozen=True)
class returnFees(RdfProperty):
    term = RdfTerm('returnFees', 'https://schema.org/returnFees', [])
    object: schemaorg.ReturnFeesEnumeration

@dataclass(frozen=True)
class countriesSupported(RdfProperty):
    term = RdfTerm('countriesSupported', 'https://schema.org/countriesSupported', [])
    object: Text

@dataclass(frozen=True)
class candidate(RdfProperty):
    term = RdfTerm('candidate', 'https://schema.org/candidate', [])
    object: schemaorg.Person

@dataclass(frozen=True)
class returnLabelSource(RdfProperty):
    term = RdfTerm('returnLabelSource', 'https://schema.org/returnLabelSource', [])
    object: schemaorg.ReturnLabelSourceEnumeration

@dataclass(frozen=True)
class seatSection(RdfProperty):
    term = RdfTerm('seatSection', 'https://schema.org/seatSection', [])
    object: Text

@dataclass(frozen=True)
class validIn(RdfProperty):
    term = RdfTerm('validIn', 'https://schema.org/validIn', [])
    object: schemaorg.AdministrativeArea

@dataclass(frozen=True)
class ethicsPolicy(RdfProperty):
    term = RdfTerm('ethicsPolicy', 'https://schema.org/ethicsPolicy', [])
    object: schemaorg.CreativeWork | URL

@dataclass(frozen=True)
class returnShippingFeesAmount(RdfProperty):
    term = RdfTerm('returnShippingFeesAmount', 'https://schema.org/returnShippingFeesAmount', [])
    object: schemaorg.MonetaryAmount

@dataclass(frozen=True)
class slogan(RdfProperty):
    term = RdfTerm('slogan', 'https://schema.org/slogan', [])
    object: Text

@dataclass(frozen=True)
class priceType(RdfProperty):
    term = RdfTerm('priceType', 'https://schema.org/priceType', [])
    object: schemaorg.PriceTypeEnumeration | Text

@dataclass(frozen=True)
class orderStatus(RdfProperty):
    term = RdfTerm('orderStatus', 'https://schema.org/orderStatus', [])
    object: schemaorg.OrderStatus

@dataclass(frozen=True)
class billingDuration(RdfProperty):
    term = RdfTerm('billingDuration', 'https://schema.org/billingDuration', [])
    object: schemaorg.Duration | Number | schemaorg.QuantitativeValue

@dataclass(frozen=True)
class supplyTo(RdfProperty):
    term = RdfTerm('supplyTo', 'https://schema.org/supplyTo', [])
    object: schemaorg.AnatomicalStructure

@dataclass(frozen=True)
class estimatedCost(RdfProperty):
    term = RdfTerm('estimatedCost', 'https://schema.org/estimatedCost', [])
    object: Text | schemaorg.MonetaryAmount

@dataclass(frozen=True)
class organizer(RdfProperty):
    term = RdfTerm('organizer', 'https://schema.org/organizer', [])
    object: schemaorg.Person | schemaorg.Organization

@dataclass(frozen=True)
class orderDate(RdfProperty):
    term = RdfTerm('orderDate', 'https://schema.org/orderDate', [])
    object: Date | DateTime

@dataclass(frozen=True)
class paymentMethodId(RdfProperty):
    term = RdfTerm('paymentMethodId', 'https://schema.org/paymentMethodId', [])
    object: Text

@dataclass(frozen=True)
class gtin12(RdfProperty):
    term = RdfTerm('gtin12', 'https://schema.org/gtin12', [])
    object: Text

@dataclass(frozen=True)
class returnMethod(RdfProperty):
    term = RdfTerm('returnMethod', 'https://schema.org/returnMethod', [])
    object: schemaorg.ReturnMethodEnumeration

@dataclass(frozen=True)
class distance(RdfProperty):
    term = RdfTerm('distance', 'https://schema.org/distance', [])
    object: schemaorg.Distance

@dataclass(frozen=True)
class articleSection(RdfProperty):
    term = RdfTerm('articleSection', 'https://schema.org/articleSection', [])
    object: Text

@dataclass(frozen=True)
class bitrate(RdfProperty):
    term = RdfTerm('bitrate', 'https://schema.org/bitrate', [])
    object: Text

@dataclass(frozen=True)
class riskFactor(RdfProperty):
    term = RdfTerm('riskFactor', 'https://schema.org/riskFactor', [])
    object: schemaorg.MedicalRiskFactor

class DateTime(RdfDataType):
    term = RdfTerm('DateTime', 'https://schema.org/DateTime', [])

class Date(RdfDataType):
    term = RdfTerm('Date', 'https://schema.org/Date', [])

class Number(RdfDataType):
    term = RdfTerm('Number', 'https://schema.org/Number', [])

class Float(RdfDataType):
    term = RdfTerm('Float', 'https://schema.org/Float', [])

class Integer(RdfDataType):
    term = RdfTerm('Integer', 'https://schema.org/Integer', [])

class Time(RdfDataType):
    term = RdfTerm('Time', 'https://schema.org/Time', [])

class Text(RdfDataType):
    term = RdfTerm('Text', 'https://schema.org/Text', [])

class PronounceableText(RdfDataType):
    term = RdfTerm('PronounceableText', 'https://schema.org/PronounceableText', [])

class XPathType(RdfDataType):
    term = RdfTerm('XPathType', 'https://schema.org/XPathType', [])

class URL(RdfDataType):
    term = RdfTerm('URL', 'https://schema.org/URL', [])

class CssSelectorType(RdfDataType):
    term = RdfTerm('CssSelectorType', 'https://schema.org/CssSelectorType', [])

class Boolean(RdfDataType):
    term = RdfTerm('Boolean', 'https://schema.org/Boolean', [])