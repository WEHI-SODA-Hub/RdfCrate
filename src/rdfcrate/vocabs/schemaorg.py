from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfLiteral
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import schemaorg
from rdfcrate.rdftype import RdfType


class DateTime(RdfLiteral):
    term = RdfTerm("http://schema.org/DateTime", "DateTime")


class Time(RdfLiteral):
    term = RdfTerm("http://schema.org/Time", "Time")


class Number(RdfLiteral):
    term = RdfTerm("http://schema.org/Number", "Number")


class Integer(RdfLiteral):
    term = RdfTerm("http://schema.org/Integer", "Integer")


class Float(RdfLiteral):
    term = RdfTerm("http://schema.org/Float", "Float")


class Boolean(RdfLiteral):
    term = RdfTerm("http://schema.org/Boolean", "Boolean")


class Text(RdfLiteral):
    term = RdfTerm("http://schema.org/Text", "Text")


class CssSelectorType(RdfLiteral):
    term = RdfTerm("http://schema.org/CssSelectorType", "CssSelectorType")


class PronounceableText(RdfLiteral):
    term = RdfTerm("http://schema.org/PronounceableText", "PronounceableText")


class URL(RdfLiteral):
    term = RdfTerm("http://schema.org/URL", "URL")


class XPathType(RdfLiteral):
    term = RdfTerm("http://schema.org/XPathType", "XPathType")


class Date(RdfLiteral):
    term = RdfTerm("http://schema.org/Date", "Date")


class DataType(rdfs.Class):
    term = RdfTerm("http://schema.org/DataType", "DataType")


class Thing(RdfClass):
    term = RdfTerm("http://schema.org/Thing", "Thing")


class Person(Thing):
    term = RdfTerm("http://schema.org/Person", "Person")


class Action(Thing):
    term = RdfTerm("http://schema.org/Action", "Action")


class Product(Thing):
    term = RdfTerm("http://schema.org/Product", "Product")


class BioChemEntity(Thing):
    term = RdfTerm("http://schema.org/BioChemEntity", "BioChemEntity")


class Intangible(Thing):
    term = RdfTerm("http://schema.org/Intangible", "Intangible")


class Organization(Thing):
    term = RdfTerm("http://schema.org/Organization", "Organization")


class StupidType(Thing):
    term = RdfTerm("http://schema.org/StupidType", "StupidType")


class Place(Thing):
    term = RdfTerm("http://schema.org/Place", "Place")


class MedicalEntity(Thing):
    term = RdfTerm("http://schema.org/MedicalEntity", "MedicalEntity")


class Taxon(Thing):
    term = RdfTerm("http://schema.org/Taxon", "Taxon")


class CreativeWork(Thing):
    term = RdfTerm("http://schema.org/CreativeWork", "CreativeWork")


class Event(Thing):
    term = RdfTerm("http://schema.org/Event", "Event")


class InteractAction(Action):
    term = RdfTerm("http://schema.org/InteractAction", "InteractAction")


class UpdateAction(Action):
    term = RdfTerm("http://schema.org/UpdateAction", "UpdateAction")


class CreateAction(Action):
    term = RdfTerm("http://schema.org/CreateAction", "CreateAction")


class MoveAction(Action):
    term = RdfTerm("http://schema.org/MoveAction", "MoveAction")


class ControlAction(Action):
    term = RdfTerm("http://schema.org/ControlAction", "ControlAction")


class SolveMathAction(Action):
    term = RdfTerm("http://schema.org/SolveMathAction", "SolveMathAction")


class OrganizeAction(Action):
    term = RdfTerm("http://schema.org/OrganizeAction", "OrganizeAction")


class SearchAction(Action):
    term = RdfTerm("http://schema.org/SearchAction", "SearchAction")


class AssessAction(Action):
    term = RdfTerm("http://schema.org/AssessAction", "AssessAction")


class FindAction(Action):
    term = RdfTerm("http://schema.org/FindAction", "FindAction")


class TransferAction(Action):
    term = RdfTerm("http://schema.org/TransferAction", "TransferAction")


class ConsumeAction(Action):
    term = RdfTerm("http://schema.org/ConsumeAction", "ConsumeAction")


class SeekToAction(Action):
    term = RdfTerm("http://schema.org/SeekToAction", "SeekToAction")


class PlayAction(Action):
    term = RdfTerm("http://schema.org/PlayAction", "PlayAction")


class TradeAction(Action):
    term = RdfTerm("http://schema.org/TradeAction", "TradeAction")


class AchieveAction(Action):
    term = RdfTerm("http://schema.org/AchieveAction", "AchieveAction")


class Vehicle(Product):
    term = RdfTerm("http://schema.org/Vehicle", "Vehicle")


class IndividualProduct(Product):
    term = RdfTerm("http://schema.org/IndividualProduct", "IndividualProduct")


class ProductModel(Product):
    term = RdfTerm("http://schema.org/ProductModel", "ProductModel")


class ProductGroup(Product):
    term = RdfTerm("http://schema.org/ProductGroup", "ProductGroup")


class SomeProducts(Product):
    term = RdfTerm("http://schema.org/SomeProducts", "SomeProducts")


class ChemicalSubstance(BioChemEntity):
    term = RdfTerm("http://schema.org/ChemicalSubstance", "ChemicalSubstance")


class Gene(BioChemEntity):
    term = RdfTerm("http://schema.org/Gene", "Gene")


class MolecularEntity(BioChemEntity):
    term = RdfTerm("http://schema.org/MolecularEntity", "MolecularEntity")


class Protein(BioChemEntity):
    term = RdfTerm("http://schema.org/Protein", "Protein")


class HealthPlanNetwork(Intangible):
    term = RdfTerm("http://schema.org/HealthPlanNetwork", "HealthPlanNetwork")


class ListItem(Intangible):
    term = RdfTerm("http://schema.org/ListItem", "ListItem")


class Quantity(Intangible):
    term = RdfTerm("http://schema.org/Quantity", "Quantity")


class Order(Intangible):
    term = RdfTerm("http://schema.org/Order", "Order")


class Property(Intangible):
    term = RdfTerm("http://schema.org/Property", "Property")


class PaymentMethod(Intangible):
    term = RdfTerm("http://schema.org/PaymentMethod", "PaymentMethod")


class SpeakableSpecification(Intangible):
    term = RdfTerm("http://schema.org/SpeakableSpecification", "SpeakableSpecification")


class AlignmentObject(Intangible):
    term = RdfTerm("http://schema.org/AlignmentObject", "AlignmentObject")


class Seat(Intangible):
    term = RdfTerm("http://schema.org/Seat", "Seat")


class StructuredValue(Intangible):
    term = RdfTerm("http://schema.org/StructuredValue", "StructuredValue")


class Schedule(Intangible):
    term = RdfTerm("http://schema.org/Schedule", "Schedule")


class OrderItem(Intangible):
    term = RdfTerm("http://schema.org/OrderItem", "OrderItem")


class DataFeedItem(Intangible):
    term = RdfTerm("http://schema.org/DataFeedItem", "DataFeedItem")


class Invoice(Intangible):
    term = RdfTerm("http://schema.org/Invoice", "Invoice")


class Class(Intangible):
    term = RdfTerm("http://schema.org/Class", "Class")


class MenuItem(Intangible):
    term = RdfTerm("http://schema.org/MenuItem", "MenuItem")


class EntryPoint(Intangible):
    term = RdfTerm("http://schema.org/EntryPoint", "EntryPoint")


class HealthInsurancePlan(Intangible):
    term = RdfTerm("http://schema.org/HealthInsurancePlan", "HealthInsurancePlan")


class ActionAccessSpecification(Intangible):
    term = RdfTerm(
        "http://schema.org/ActionAccessSpecification", "ActionAccessSpecification"
    )


class DefinedTerm(Intangible):
    term = RdfTerm("http://schema.org/DefinedTerm", "DefinedTerm")


class MerchantReturnPolicy(Intangible):
    term = RdfTerm("http://schema.org/MerchantReturnPolicy", "MerchantReturnPolicy")


class Demand(Intangible):
    term = RdfTerm("http://schema.org/Demand", "Demand")


class ProgramMembership(Intangible):
    term = RdfTerm("http://schema.org/ProgramMembership", "ProgramMembership")


class Service(Intangible):
    term = RdfTerm("http://schema.org/Service", "Service")


class ConstraintNode(Intangible):
    term = RdfTerm("http://schema.org/ConstraintNode", "ConstraintNode")


class HealthPlanCostSharingSpecification(Intangible):
    term = RdfTerm(
        "http://schema.org/HealthPlanCostSharingSpecification",
        "HealthPlanCostSharingSpecification",
    )


class JobPosting(Intangible):
    term = RdfTerm("http://schema.org/JobPosting", "JobPosting")


class EnergyConsumptionDetails(Intangible):
    term = RdfTerm(
        "http://schema.org/EnergyConsumptionDetails", "EnergyConsumptionDetails"
    )


class ParcelDelivery(Intangible):
    term = RdfTerm("http://schema.org/ParcelDelivery", "ParcelDelivery")


class MemberProgram(Intangible):
    term = RdfTerm("http://schema.org/MemberProgram", "MemberProgram")


class PropertyValueSpecification(Intangible):
    term = RdfTerm(
        "http://schema.org/PropertyValueSpecification", "PropertyValueSpecification"
    )


class FloorPlan(Intangible):
    term = RdfTerm("http://schema.org/FloorPlan", "FloorPlan")


class HealthPlanFormulary(Intangible):
    term = RdfTerm("http://schema.org/HealthPlanFormulary", "HealthPlanFormulary")


class VirtualLocation(Intangible):
    term = RdfTerm("http://schema.org/VirtualLocation", "VirtualLocation")


class Trip(Intangible):
    term = RdfTerm("http://schema.org/Trip", "Trip")


class StatisticalPopulation(Intangible):
    term = RdfTerm("http://schema.org/StatisticalPopulation", "StatisticalPopulation")


class MerchantReturnPolicySeasonalOverride(Intangible):
    term = RdfTerm(
        "http://schema.org/MerchantReturnPolicySeasonalOverride",
        "MerchantReturnPolicySeasonalOverride",
    )


class OccupationalExperienceRequirements(Intangible):
    term = RdfTerm(
        "http://schema.org/OccupationalExperienceRequirements",
        "OccupationalExperienceRequirements",
    )


class MediaSubscription(Intangible):
    term = RdfTerm("http://schema.org/MediaSubscription", "MediaSubscription")


class Ticket(Intangible):
    term = RdfTerm("http://schema.org/Ticket", "Ticket")


class GeospatialGeometry(Intangible):
    term = RdfTerm("http://schema.org/GeospatialGeometry", "GeospatialGeometry")


class BedDetails(Intangible):
    term = RdfTerm("http://schema.org/BedDetails", "BedDetails")


class Grant(Intangible):
    term = RdfTerm("http://schema.org/Grant", "Grant")


class BroadcastChannel(Intangible):
    term = RdfTerm("http://schema.org/BroadcastChannel", "BroadcastChannel")


class Occupation(Intangible):
    term = RdfTerm("http://schema.org/Occupation", "Occupation")


class DigitalDocumentPermission(Intangible):
    term = RdfTerm(
        "http://schema.org/DigitalDocumentPermission", "DigitalDocumentPermission"
    )


class EducationalOccupationalProgram(Intangible):
    term = RdfTerm(
        "http://schema.org/EducationalOccupationalProgram",
        "EducationalOccupationalProgram",
    )


class ServiceChannel(Intangible):
    term = RdfTerm("http://schema.org/ServiceChannel", "ServiceChannel")


class Permit(Intangible):
    term = RdfTerm("http://schema.org/Permit", "Permit")


class MemberProgramTier(Intangible):
    term = RdfTerm("http://schema.org/MemberProgramTier", "MemberProgramTier")


class FinancialIncentive(Intangible):
    term = RdfTerm("http://schema.org/FinancialIncentive", "FinancialIncentive")


class Enumeration(Intangible):
    term = RdfTerm("http://schema.org/Enumeration", "Enumeration")


class BroadcastFrequencySpecification(Intangible):
    term = RdfTerm(
        "http://schema.org/BroadcastFrequencySpecification",
        "BroadcastFrequencySpecification",
    )


class Rating(Intangible):
    term = RdfTerm("http://schema.org/Rating", "Rating")


class Brand(Intangible):
    term = RdfTerm("http://schema.org/Brand", "Brand")


class ComputerLanguage(Intangible):
    term = RdfTerm("http://schema.org/ComputerLanguage", "ComputerLanguage")


class ItemList(Intangible):
    term = RdfTerm("http://schema.org/ItemList", "ItemList")


class Series(Intangible):
    term = RdfTerm("http://schema.org/Series", "Series")


class Audience(Intangible):
    term = RdfTerm("http://schema.org/Audience", "Audience")


class Language(Intangible):
    term = RdfTerm("http://schema.org/Language", "Language")


class ProductReturnPolicy(Intangible):
    term = RdfTerm("http://schema.org/ProductReturnPolicy", "ProductReturnPolicy")


class Offer(Intangible):
    term = RdfTerm("http://schema.org/Offer", "Offer")


class Role(Intangible):
    term = RdfTerm("http://schema.org/Role", "Role")


class Reservation(Intangible):
    term = RdfTerm("http://schema.org/Reservation", "Reservation")


class GameServer(Intangible):
    term = RdfTerm("http://schema.org/GameServer", "GameServer")


class GovernmentOrganization(Organization):
    term = RdfTerm("http://schema.org/GovernmentOrganization", "GovernmentOrganization")


class Consortium(Organization):
    term = RdfTerm("http://schema.org/Consortium", "Consortium")


class PerformingGroup(Organization):
    term = RdfTerm("http://schema.org/PerformingGroup", "PerformingGroup")


class OnlineBusiness(Organization):
    term = RdfTerm("http://schema.org/OnlineBusiness", "OnlineBusiness")


class LibrarySystem(Organization):
    term = RdfTerm("http://schema.org/LibrarySystem", "LibrarySystem")


class SearchRescueOrganization(Organization):
    term = RdfTerm(
        "http://schema.org/SearchRescueOrganization", "SearchRescueOrganization"
    )


class PoliticalParty(Organization):
    term = RdfTerm("http://schema.org/PoliticalParty", "PoliticalParty")


class Corporation(Organization):
    term = RdfTerm("http://schema.org/Corporation", "Corporation")


class Project(Organization):
    term = RdfTerm("http://schema.org/Project", "Project")


class NewsMediaOrganization(Organization):
    term = RdfTerm("http://schema.org/NewsMediaOrganization", "NewsMediaOrganization")


class MedicalOrganization(Organization):
    term = RdfTerm("http://schema.org/MedicalOrganization", "MedicalOrganization")


class NGO(Organization):
    term = RdfTerm("http://schema.org/NGO", "NGO")


class Cooperative(Organization):
    term = RdfTerm("http://schema.org/Cooperative", "Cooperative")


class WorkersUnion(Organization):
    term = RdfTerm("http://schema.org/WorkersUnion", "WorkersUnion")


class SportsOrganization(Organization):
    term = RdfTerm("http://schema.org/SportsOrganization", "SportsOrganization")


class ResearchOrganization(Organization):
    term = RdfTerm("http://schema.org/ResearchOrganization", "ResearchOrganization")


class FundingScheme(Organization):
    term = RdfTerm("http://schema.org/FundingScheme", "FundingScheme")


class Airline(Organization):
    term = RdfTerm("http://schema.org/Airline", "Airline")


class Accommodation(Place):
    term = RdfTerm("http://schema.org/Accommodation", "Accommodation")


class LocalBusiness(Organization, Place):
    term = RdfTerm("http://schema.org/LocalBusiness", "LocalBusiness")


class TouristDestination(Place):
    term = RdfTerm("http://schema.org/TouristDestination", "TouristDestination")


class Residence(Place):
    term = RdfTerm("http://schema.org/Residence", "Residence")


class CivicStructure(Place):
    term = RdfTerm("http://schema.org/CivicStructure", "CivicStructure")


class Landform(Place):
    term = RdfTerm("http://schema.org/Landform", "Landform")


class AdministrativeArea(Place):
    term = RdfTerm("http://schema.org/AdministrativeArea", "AdministrativeArea")


class LandmarksOrHistoricalBuildings(Place):
    term = RdfTerm(
        "http://schema.org/LandmarksOrHistoricalBuildings",
        "LandmarksOrHistoricalBuildings",
    )


class TouristAttraction(Place):
    term = RdfTerm("http://schema.org/TouristAttraction", "TouristAttraction")


class AnatomicalSystem(MedicalEntity):
    term = RdfTerm("http://schema.org/AnatomicalSystem", "AnatomicalSystem")


class DrugClass(MedicalEntity):
    term = RdfTerm("http://schema.org/DrugClass", "DrugClass")


class LifestyleModification(MedicalEntity):
    term = RdfTerm("http://schema.org/LifestyleModification", "LifestyleModification")


class MedicalIntangible(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalIntangible", "MedicalIntangible")


class MedicalProcedure(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalProcedure", "MedicalProcedure")


class MedicalRiskEstimator(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalRiskEstimator", "MedicalRiskEstimator")


class SuperficialAnatomy(MedicalEntity):
    term = RdfTerm("http://schema.org/SuperficialAnatomy", "SuperficialAnatomy")


class MedicalIndication(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalIndication", "MedicalIndication")


class MedicalRiskFactor(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalRiskFactor", "MedicalRiskFactor")


class MedicalCause(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalCause", "MedicalCause")


class AnatomicalStructure(MedicalEntity):
    term = RdfTerm("http://schema.org/AnatomicalStructure", "AnatomicalStructure")


class MedicalContraindication(MedicalEntity):
    term = RdfTerm(
        "http://schema.org/MedicalContraindication", "MedicalContraindication"
    )


class MedicalStudy(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalStudy", "MedicalStudy")


class MedicalDevice(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalDevice", "MedicalDevice")


class MedicalGuideline(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalGuideline", "MedicalGuideline")


class Substance(MedicalEntity):
    term = RdfTerm("http://schema.org/Substance", "Substance")


class MedicalCondition(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalCondition", "MedicalCondition")


class DrugCost(MedicalEntity):
    term = RdfTerm("http://schema.org/DrugCost", "DrugCost")


class MedicalTest(MedicalEntity):
    term = RdfTerm("http://schema.org/MedicalTest", "MedicalTest")


class MusicComposition(CreativeWork):
    term = RdfTerm("http://schema.org/MusicComposition", "MusicComposition")


class Article(CreativeWork):
    term = RdfTerm("http://schema.org/Article", "Article")


class Guide(CreativeWork):
    term = RdfTerm("http://schema.org/Guide", "Guide")


class Legislation(CreativeWork):
    term = RdfTerm("http://schema.org/Legislation", "Legislation")


class HowTo(CreativeWork):
    term = RdfTerm("http://schema.org/HowTo", "HowTo")


class Conversation(CreativeWork):
    term = RdfTerm("http://schema.org/Conversation", "Conversation")


class MediaReviewItem(CreativeWork):
    term = RdfTerm("http://schema.org/MediaReviewItem", "MediaReviewItem")


class Review(CreativeWork):
    term = RdfTerm("http://schema.org/Review", "Review")


class Statement(CreativeWork):
    term = RdfTerm("http://schema.org/Statement", "Statement")


class ComicStory(CreativeWork):
    term = RdfTerm("http://schema.org/ComicStory", "ComicStory")


class Quotation(CreativeWork):
    term = RdfTerm("http://schema.org/Quotation", "Quotation")


class WebSite(CreativeWork):
    term = RdfTerm("http://schema.org/WebSite", "WebSite")


class Certification(CreativeWork):
    term = RdfTerm("http://schema.org/Certification", "Certification")


class SheetMusic(CreativeWork):
    term = RdfTerm("http://schema.org/SheetMusic", "SheetMusic")


class DefinedTermSet(CreativeWork):
    term = RdfTerm("http://schema.org/DefinedTermSet", "DefinedTermSet")


class MediaObject(CreativeWork):
    term = RdfTerm("http://schema.org/MediaObject", "MediaObject")


class Episode(CreativeWork):
    term = RdfTerm("http://schema.org/Episode", "Episode")


class Season(CreativeWork):
    term = RdfTerm("http://schema.org/Season", "Season")


class Menu(CreativeWork):
    term = RdfTerm("http://schema.org/Menu", "Menu")


class Book(CreativeWork):
    term = RdfTerm("http://schema.org/Book", "Book")


class Poster(CreativeWork):
    term = RdfTerm("http://schema.org/Poster", "Poster")


class EducationalOccupationalCredential(CreativeWork):
    term = RdfTerm(
        "http://schema.org/EducationalOccupationalCredential",
        "EducationalOccupationalCredential",
    )


class WebContent(CreativeWork):
    term = RdfTerm("http://schema.org/WebContent", "WebContent")


class Painting(CreativeWork):
    term = RdfTerm("http://schema.org/Painting", "Painting")


class SoftwareSourceCode(CreativeWork):
    term = RdfTerm("http://schema.org/SoftwareSourceCode", "SoftwareSourceCode")


class ShortStory(CreativeWork):
    term = RdfTerm("http://schema.org/ShortStory", "ShortStory")


class CreativeWorkSeason(CreativeWork):
    term = RdfTerm("http://schema.org/CreativeWorkSeason", "CreativeWorkSeason")


class MusicPlaylist(CreativeWork):
    term = RdfTerm("http://schema.org/MusicPlaylist", "MusicPlaylist")


class Play(CreativeWork):
    term = RdfTerm("http://schema.org/Play", "Play")


class MenuSection(CreativeWork):
    term = RdfTerm("http://schema.org/MenuSection", "MenuSection")


class SoftwareApplication(CreativeWork):
    term = RdfTerm("http://schema.org/SoftwareApplication", "SoftwareApplication")


class SpecialAnnouncement(CreativeWork):
    term = RdfTerm("http://schema.org/SpecialAnnouncement", "SpecialAnnouncement")


class Thesis(CreativeWork):
    term = RdfTerm("http://schema.org/Thesis", "Thesis")


class HyperToc(CreativeWork):
    term = RdfTerm("http://schema.org/HyperToc", "HyperToc")


class Sculpture(CreativeWork):
    term = RdfTerm("http://schema.org/Sculpture", "Sculpture")


class Atlas(CreativeWork):
    term = RdfTerm("http://schema.org/Atlas", "Atlas")


class ArchiveComponent(CreativeWork):
    term = RdfTerm("http://schema.org/ArchiveComponent", "ArchiveComponent")


class Clip(CreativeWork):
    term = RdfTerm("http://schema.org/Clip", "Clip")


class Blog(CreativeWork):
    term = RdfTerm("http://schema.org/Blog", "Blog")


class Claim(CreativeWork):
    term = RdfTerm("http://schema.org/Claim", "Claim")


class MathSolver(CreativeWork):
    term = RdfTerm("http://schema.org/MathSolver", "MathSolver")


class Game(CreativeWork):
    term = RdfTerm("http://schema.org/Game", "Game")


class DigitalDocument(CreativeWork):
    term = RdfTerm("http://schema.org/DigitalDocument", "DigitalDocument")


class Collection(CreativeWork):
    term = RdfTerm("http://schema.org/Collection", "Collection")


class Photograph(CreativeWork):
    term = RdfTerm("http://schema.org/Photograph", "Photograph")


class Dataset(CreativeWork):
    term = RdfTerm("http://schema.org/Dataset", "Dataset")


class LearningResource(CreativeWork):
    term = RdfTerm("http://schema.org/LearningResource", "LearningResource")


class DataCatalog(CreativeWork):
    term = RdfTerm("http://schema.org/DataCatalog", "DataCatalog")


class VisualArtwork(CreativeWork):
    term = RdfTerm("http://schema.org/VisualArtwork", "VisualArtwork")


class HyperTocEntry(CreativeWork):
    term = RdfTerm("http://schema.org/HyperTocEntry", "HyperTocEntry")


class MusicRecording(CreativeWork):
    term = RdfTerm("http://schema.org/MusicRecording", "MusicRecording")


class Manuscript(CreativeWork):
    term = RdfTerm("http://schema.org/Manuscript", "Manuscript")


class WebPageElement(CreativeWork):
    term = RdfTerm("http://schema.org/WebPageElement", "WebPageElement")


class PublicationIssue(CreativeWork):
    term = RdfTerm("http://schema.org/PublicationIssue", "PublicationIssue")


class Drawing(CreativeWork):
    term = RdfTerm("http://schema.org/Drawing", "Drawing")


class Code(CreativeWork):
    term = RdfTerm("http://schema.org/Code", "Code")


class Map(CreativeWork):
    term = RdfTerm("http://schema.org/Map", "Map")


class WebPage(CreativeWork):
    term = RdfTerm("http://schema.org/WebPage", "WebPage")


class Chapter(CreativeWork):
    term = RdfTerm("http://schema.org/Chapter", "Chapter")


class Message(CreativeWork):
    term = RdfTerm("http://schema.org/Message", "Message")


class PublicationVolume(CreativeWork):
    term = RdfTerm("http://schema.org/PublicationVolume", "PublicationVolume")


class Movie(CreativeWork):
    term = RdfTerm("http://schema.org/Movie", "Movie")


class Comment(CreativeWork):
    term = RdfTerm("http://schema.org/Comment", "Comment")


class ComedyEvent(Event):
    term = RdfTerm("http://schema.org/ComedyEvent", "ComedyEvent")


class BusinessEvent(Event):
    term = RdfTerm("http://schema.org/BusinessEvent", "BusinessEvent")


class LiteraryEvent(Event):
    term = RdfTerm("http://schema.org/LiteraryEvent", "LiteraryEvent")


class UserInteraction(Event):
    term = RdfTerm("http://schema.org/UserInteraction", "UserInteraction")


class DanceEvent(Event):
    term = RdfTerm("http://schema.org/DanceEvent", "DanceEvent")


class MusicEvent(Event):
    term = RdfTerm("http://schema.org/MusicEvent", "MusicEvent")


class ScreeningEvent(Event):
    term = RdfTerm("http://schema.org/ScreeningEvent", "ScreeningEvent")


class PublicationEvent(Event):
    term = RdfTerm("http://schema.org/PublicationEvent", "PublicationEvent")


class Hackathon(Event):
    term = RdfTerm("http://schema.org/Hackathon", "Hackathon")


class FoodEvent(Event):
    term = RdfTerm("http://schema.org/FoodEvent", "FoodEvent")


class SaleEvent(Event):
    term = RdfTerm("http://schema.org/SaleEvent", "SaleEvent")


class SocialEvent(Event):
    term = RdfTerm("http://schema.org/SocialEvent", "SocialEvent")


class EducationEvent(Event):
    term = RdfTerm("http://schema.org/EducationEvent", "EducationEvent")


class VisualArtsEvent(Event):
    term = RdfTerm("http://schema.org/VisualArtsEvent", "VisualArtsEvent")


class TheaterEvent(Event):
    term = RdfTerm("http://schema.org/TheaterEvent", "TheaterEvent")


class ExhibitionEvent(Event):
    term = RdfTerm("http://schema.org/ExhibitionEvent", "ExhibitionEvent")


class SportsEvent(Event):
    term = RdfTerm("http://schema.org/SportsEvent", "SportsEvent")


class CourseInstance(Event):
    term = RdfTerm("http://schema.org/CourseInstance", "CourseInstance")


class ChildrensEvent(Event):
    term = RdfTerm("http://schema.org/ChildrensEvent", "ChildrensEvent")


class DeliveryEvent(Event):
    term = RdfTerm("http://schema.org/DeliveryEvent", "DeliveryEvent")


class Festival(Event):
    term = RdfTerm("http://schema.org/Festival", "Festival")


class BefriendAction(InteractAction):
    term = RdfTerm("http://schema.org/BefriendAction", "BefriendAction")


class RegisterAction(InteractAction):
    term = RdfTerm("http://schema.org/RegisterAction", "RegisterAction")


class UnRegisterAction(InteractAction):
    term = RdfTerm("http://schema.org/UnRegisterAction", "UnRegisterAction")


class MarryAction(InteractAction):
    term = RdfTerm("http://schema.org/MarryAction", "MarryAction")


class CommunicateAction(InteractAction):
    term = RdfTerm("http://schema.org/CommunicateAction", "CommunicateAction")


class SubscribeAction(InteractAction):
    term = RdfTerm("http://schema.org/SubscribeAction", "SubscribeAction")


class LeaveAction(InteractAction):
    term = RdfTerm("http://schema.org/LeaveAction", "LeaveAction")


class FollowAction(InteractAction):
    term = RdfTerm("http://schema.org/FollowAction", "FollowAction")


class JoinAction(InteractAction):
    term = RdfTerm("http://schema.org/JoinAction", "JoinAction")


class AddAction(UpdateAction):
    term = RdfTerm("http://schema.org/AddAction", "AddAction")


class DeleteAction(UpdateAction):
    term = RdfTerm("http://schema.org/DeleteAction", "DeleteAction")


class ReplaceAction(UpdateAction):
    term = RdfTerm("http://schema.org/ReplaceAction", "ReplaceAction")


class CookAction(CreateAction):
    term = RdfTerm("http://schema.org/CookAction", "CookAction")


class PhotographAction(CreateAction):
    term = RdfTerm("http://schema.org/PhotographAction", "PhotographAction")


class PaintAction(CreateAction):
    term = RdfTerm("http://schema.org/PaintAction", "PaintAction")


class WriteAction(CreateAction):
    term = RdfTerm("http://schema.org/WriteAction", "WriteAction")


class FilmAction(CreateAction):
    term = RdfTerm("http://schema.org/FilmAction", "FilmAction")


class DrawAction(CreateAction):
    term = RdfTerm("http://schema.org/DrawAction", "DrawAction")


class TravelAction(MoveAction):
    term = RdfTerm("http://schema.org/TravelAction", "TravelAction")


class DepartAction(MoveAction):
    term = RdfTerm("http://schema.org/DepartAction", "DepartAction")


class ArriveAction(MoveAction):
    term = RdfTerm("http://schema.org/ArriveAction", "ArriveAction")


class ActivateAction(ControlAction):
    term = RdfTerm("http://schema.org/ActivateAction", "ActivateAction")


class SuspendAction(ControlAction):
    term = RdfTerm("http://schema.org/SuspendAction", "SuspendAction")


class DeactivateAction(ControlAction):
    term = RdfTerm("http://schema.org/DeactivateAction", "DeactivateAction")


class ResumeAction(ControlAction):
    term = RdfTerm("http://schema.org/ResumeAction", "ResumeAction")


class ApplyAction(OrganizeAction):
    term = RdfTerm("http://schema.org/ApplyAction", "ApplyAction")


class PlanAction(OrganizeAction):
    term = RdfTerm("http://schema.org/PlanAction", "PlanAction")


class AllocateAction(OrganizeAction):
    term = RdfTerm("http://schema.org/AllocateAction", "AllocateAction")


class BookmarkAction(OrganizeAction):
    term = RdfTerm("http://schema.org/BookmarkAction", "BookmarkAction")


class IgnoreAction(AssessAction):
    term = RdfTerm("http://schema.org/IgnoreAction", "IgnoreAction")


class ReactAction(AssessAction):
    term = RdfTerm("http://schema.org/ReactAction", "ReactAction")


class ChooseAction(AssessAction):
    term = RdfTerm("http://schema.org/ChooseAction", "ChooseAction")


class ReviewAction(AssessAction):
    term = RdfTerm("http://schema.org/ReviewAction", "ReviewAction")


class TrackAction(FindAction):
    term = RdfTerm("http://schema.org/TrackAction", "TrackAction")


class DiscoverAction(FindAction):
    term = RdfTerm("http://schema.org/DiscoverAction", "DiscoverAction")


class CheckAction(FindAction):
    term = RdfTerm("http://schema.org/CheckAction", "CheckAction")


class TakeAction(TransferAction):
    term = RdfTerm("http://schema.org/TakeAction", "TakeAction")


class LendAction(TransferAction):
    term = RdfTerm("http://schema.org/LendAction", "LendAction")


class ReturnAction(TransferAction):
    term = RdfTerm("http://schema.org/ReturnAction", "ReturnAction")


class DownloadAction(TransferAction):
    term = RdfTerm("http://schema.org/DownloadAction", "DownloadAction")


class GiveAction(TransferAction):
    term = RdfTerm("http://schema.org/GiveAction", "GiveAction")


class MoneyTransfer(TransferAction):
    term = RdfTerm("http://schema.org/MoneyTransfer", "MoneyTransfer")


class ReceiveAction(TransferAction):
    term = RdfTerm("http://schema.org/ReceiveAction", "ReceiveAction")


class DonateAction(TransferAction):
    term = RdfTerm("http://schema.org/DonateAction", "DonateAction")


class BorrowAction(TransferAction):
    term = RdfTerm("http://schema.org/BorrowAction", "BorrowAction")


class SendAction(TransferAction):
    term = RdfTerm("http://schema.org/SendAction", "SendAction")


class UseAction(ConsumeAction):
    term = RdfTerm("http://schema.org/UseAction", "UseAction")


class InstallAction(ConsumeAction):
    term = RdfTerm("http://schema.org/InstallAction", "InstallAction")


class WatchAction(ConsumeAction):
    term = RdfTerm("http://schema.org/WatchAction", "WatchAction")


class PlayGameAction(ConsumeAction):
    term = RdfTerm("http://schema.org/PlayGameAction", "PlayGameAction")


class DrinkAction(ConsumeAction):
    term = RdfTerm("http://schema.org/DrinkAction", "DrinkAction")


class EatAction(ConsumeAction):
    term = RdfTerm("http://schema.org/EatAction", "EatAction")


class ListenAction(ConsumeAction):
    term = RdfTerm("http://schema.org/ListenAction", "ListenAction")


class ReadAction(ConsumeAction):
    term = RdfTerm("http://schema.org/ReadAction", "ReadAction")


class ViewAction(ConsumeAction):
    term = RdfTerm("http://schema.org/ViewAction", "ViewAction")


class ExerciseAction(PlayAction):
    term = RdfTerm("http://schema.org/ExerciseAction", "ExerciseAction")


class PerformAction(PlayAction):
    term = RdfTerm("http://schema.org/PerformAction", "PerformAction")


class BuyAction(TradeAction):
    term = RdfTerm("http://schema.org/BuyAction", "BuyAction")


class QuoteAction(TradeAction):
    term = RdfTerm("http://schema.org/QuoteAction", "QuoteAction")


class OrderAction(TradeAction):
    term = RdfTerm("http://schema.org/OrderAction", "OrderAction")


class SellAction(TradeAction):
    term = RdfTerm("http://schema.org/SellAction", "SellAction")


class RentAction(TradeAction):
    term = RdfTerm("http://schema.org/RentAction", "RentAction")


class TipAction(TradeAction):
    term = RdfTerm("http://schema.org/TipAction", "TipAction")


class PreOrderAction(TradeAction):
    term = RdfTerm("http://schema.org/PreOrderAction", "PreOrderAction")


class PayAction(TradeAction):
    term = RdfTerm("http://schema.org/PayAction", "PayAction")


class LoseAction(AchieveAction):
    term = RdfTerm("http://schema.org/LoseAction", "LoseAction")


class WinAction(AchieveAction):
    term = RdfTerm("http://schema.org/WinAction", "WinAction")


class TieAction(AchieveAction):
    term = RdfTerm("http://schema.org/TieAction", "TieAction")


class Motorcycle(Vehicle):
    term = RdfTerm("http://schema.org/Motorcycle", "Motorcycle")


class BusOrCoach(Vehicle):
    term = RdfTerm("http://schema.org/BusOrCoach", "BusOrCoach")


class MotorizedBicycle(Vehicle):
    term = RdfTerm("http://schema.org/MotorizedBicycle", "MotorizedBicycle")


class Car(Vehicle):
    term = RdfTerm("http://schema.org/Car", "Car")


class HowToTip(ListItem, CreativeWork):
    term = RdfTerm("http://schema.org/HowToTip", "HowToTip")


class HowToDirection(ListItem, CreativeWork):
    term = RdfTerm("http://schema.org/HowToDirection", "HowToDirection")


class HowToItem(ListItem):
    term = RdfTerm("http://schema.org/HowToItem", "HowToItem")


class Duration(Quantity):
    term = RdfTerm("http://schema.org/Duration", "Duration")


class Energy(Quantity):
    term = RdfTerm("http://schema.org/Energy", "Energy")


class Mass(Quantity):
    term = RdfTerm("http://schema.org/Mass", "Mass")


class Distance(Quantity):
    term = RdfTerm("http://schema.org/Distance", "Distance")


class ShippingService(StructuredValue):
    term = RdfTerm("http://schema.org/ShippingService", "ShippingService")


class CDCPMDRecord(StructuredValue):
    term = RdfTerm("http://schema.org/CDCPMDRecord", "CDCPMDRecord")


class OpeningHoursSpecification(StructuredValue):
    term = RdfTerm(
        "http://schema.org/OpeningHoursSpecification", "OpeningHoursSpecification"
    )


class PostalCodeRangeSpecification(StructuredValue):
    term = RdfTerm(
        "http://schema.org/PostalCodeRangeSpecification", "PostalCodeRangeSpecification"
    )


class GeoCoordinates(StructuredValue):
    term = RdfTerm("http://schema.org/GeoCoordinates", "GeoCoordinates")


class DeliveryTimeSettings(StructuredValue):
    term = RdfTerm("http://schema.org/DeliveryTimeSettings", "DeliveryTimeSettings")


class ShippingDeliveryTime(StructuredValue):
    term = RdfTerm("http://schema.org/ShippingDeliveryTime", "ShippingDeliveryTime")


class MonetaryAmount(StructuredValue):
    term = RdfTerm("http://schema.org/MonetaryAmount", "MonetaryAmount")


class ExchangeRateSpecification(StructuredValue):
    term = RdfTerm(
        "http://schema.org/ExchangeRateSpecification", "ExchangeRateSpecification"
    )


class ShippingConditions(StructuredValue):
    term = RdfTerm("http://schema.org/ShippingConditions", "ShippingConditions")


class ContactPoint(StructuredValue):
    term = RdfTerm("http://schema.org/ContactPoint", "ContactPoint")


class DatedMoneySpecification(StructuredValue):
    term = RdfTerm(
        "http://schema.org/DatedMoneySpecification", "DatedMoneySpecification"
    )


class DefinedRegion(StructuredValue):
    term = RdfTerm("http://schema.org/DefinedRegion", "DefinedRegion")


class ShippingRateSettings(StructuredValue):
    term = RdfTerm("http://schema.org/ShippingRateSettings", "ShippingRateSettings")


class QuantitativeValue(StructuredValue):
    term = RdfTerm("http://schema.org/QuantitativeValue", "QuantitativeValue")


class TypeAndQuantityNode(StructuredValue):
    term = RdfTerm("http://schema.org/TypeAndQuantityNode", "TypeAndQuantityNode")


class WarrantyPromise(StructuredValue):
    term = RdfTerm("http://schema.org/WarrantyPromise", "WarrantyPromise")


class PriceSpecification(StructuredValue):
    term = RdfTerm("http://schema.org/PriceSpecification", "PriceSpecification")


class ServicePeriod(StructuredValue):
    term = RdfTerm("http://schema.org/ServicePeriod", "ServicePeriod")


class OfferShippingDetails(StructuredValue):
    term = RdfTerm("http://schema.org/OfferShippingDetails", "OfferShippingDetails")


class RepaymentSpecification(StructuredValue):
    term = RdfTerm("http://schema.org/RepaymentSpecification", "RepaymentSpecification")


class OwnershipInfo(StructuredValue):
    term = RdfTerm("http://schema.org/OwnershipInfo", "OwnershipInfo")


class PropertyValue(StructuredValue):
    term = RdfTerm("http://schema.org/PropertyValue", "PropertyValue")


class EngineSpecification(StructuredValue):
    term = RdfTerm("http://schema.org/EngineSpecification", "EngineSpecification")


class NutritionInformation(StructuredValue):
    term = RdfTerm("http://schema.org/NutritionInformation", "NutritionInformation")


class GeoShape(StructuredValue):
    term = RdfTerm("http://schema.org/GeoShape", "GeoShape")


class QuantitativeValueDistribution(StructuredValue):
    term = RdfTerm(
        "http://schema.org/QuantitativeValueDistribution",
        "QuantitativeValueDistribution",
    )


class InteractionCounter(StructuredValue):
    term = RdfTerm("http://schema.org/InteractionCounter", "InteractionCounter")


class CategoryCode(DefinedTerm):
    term = RdfTerm("http://schema.org/CategoryCode", "CategoryCode")


class GovernmentService(Service):
    term = RdfTerm("http://schema.org/GovernmentService", "GovernmentService")


class WebAPI(Service):
    term = RdfTerm("http://schema.org/WebAPI", "WebAPI")


class Taxi(Service):
    term = RdfTerm("http://schema.org/Taxi", "Taxi")


class FinancialProduct(Service):
    term = RdfTerm("http://schema.org/FinancialProduct", "FinancialProduct")


class CableOrSatelliteService(Service):
    term = RdfTerm(
        "http://schema.org/CableOrSatelliteService", "CableOrSatelliteService"
    )


class TaxiService(Service):
    term = RdfTerm("http://schema.org/TaxiService", "TaxiService")


class BroadcastService(Service):
    term = RdfTerm("http://schema.org/BroadcastService", "BroadcastService")


class FoodService(Service):
    term = RdfTerm("http://schema.org/FoodService", "FoodService")


class StatisticalVariable(ConstraintNode):
    term = RdfTerm("http://schema.org/StatisticalVariable", "StatisticalVariable")


class TouristTrip(Trip):
    term = RdfTerm("http://schema.org/TouristTrip", "TouristTrip")


class Flight(Trip):
    term = RdfTerm("http://schema.org/Flight", "Flight")


class BoatTrip(Trip):
    term = RdfTerm("http://schema.org/BoatTrip", "BoatTrip")


class TrainTrip(Trip):
    term = RdfTerm("http://schema.org/TrainTrip", "TrainTrip")


class BusTrip(Trip):
    term = RdfTerm("http://schema.org/BusTrip", "BusTrip")


class MonetaryGrant(Grant):
    term = RdfTerm("http://schema.org/MonetaryGrant", "MonetaryGrant")


class TelevisionChannel(BroadcastChannel):
    term = RdfTerm("http://schema.org/TelevisionChannel", "TelevisionChannel")


class RadioChannel(BroadcastChannel):
    term = RdfTerm("http://schema.org/RadioChannel", "RadioChannel")


class WorkBasedProgram(EducationalOccupationalProgram):
    term = RdfTerm("http://schema.org/WorkBasedProgram", "WorkBasedProgram")


class GovernmentPermit(Permit):
    term = RdfTerm("http://schema.org/GovernmentPermit", "GovernmentPermit")


class MapCategoryType(Enumeration):
    term = RdfTerm("http://schema.org/MapCategoryType", "MapCategoryType")


class CarUsageType(Enumeration):
    term = RdfTerm("http://schema.org/CarUsageType", "CarUsageType")


class GovernmentBenefitsType(Enumeration):
    term = RdfTerm("http://schema.org/GovernmentBenefitsType", "GovernmentBenefitsType")


class RestrictedDiet(Enumeration):
    term = RdfTerm("http://schema.org/RestrictedDiet", "RestrictedDiet")


class BookFormatType(Enumeration):
    term = RdfTerm("http://schema.org/BookFormatType", "BookFormatType")


class Specialty(Enumeration):
    term = RdfTerm("http://schema.org/Specialty", "Specialty")


class LegalValueLevel(Enumeration):
    term = RdfTerm("http://schema.org/LegalValueLevel", "LegalValueLevel")


class MedicalEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/MedicalEnumeration", "MedicalEnumeration")


class AdultOrientedEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/AdultOrientedEnumeration", "AdultOrientedEnumeration"
    )


class FulfillmentTypeEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/FulfillmentTypeEnumeration", "FulfillmentTypeEnumeration"
    )


class EventAttendanceModeEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/EventAttendanceModeEnumeration",
        "EventAttendanceModeEnumeration",
    )


class IncentiveStatus(Enumeration):
    term = RdfTerm("http://schema.org/IncentiveStatus", "IncentiveStatus")


class BusinessFunction(Enumeration):
    term = RdfTerm("http://schema.org/BusinessFunction", "BusinessFunction")


class DeliveryMethod(Enumeration):
    term = RdfTerm("http://schema.org/DeliveryMethod", "DeliveryMethod")


class MusicAlbumProductionType(Enumeration):
    term = RdfTerm(
        "http://schema.org/MusicAlbumProductionType", "MusicAlbumProductionType"
    )


class ProductReturnEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/ProductReturnEnumeration", "ProductReturnEnumeration"
    )


class GameAvailabilityEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/GameAvailabilityEnumeration", "GameAvailabilityEnumeration"
    )


class ReturnLabelSourceEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/ReturnLabelSourceEnumeration", "ReturnLabelSourceEnumeration"
    )


class ItemAvailability(Enumeration):
    term = RdfTerm("http://schema.org/ItemAvailability", "ItemAvailability")


class GamePlayMode(Enumeration):
    term = RdfTerm("http://schema.org/GamePlayMode", "GamePlayMode")


class HealthAspectEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/HealthAspectEnumeration", "HealthAspectEnumeration"
    )


class RsvpResponseType(Enumeration):
    term = RdfTerm("http://schema.org/RsvpResponseType", "RsvpResponseType")


class OfferItemCondition(Enumeration):
    term = RdfTerm("http://schema.org/OfferItemCondition", "OfferItemCondition")


class ReturnMethodEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/ReturnMethodEnumeration", "ReturnMethodEnumeration"
    )


class SizeSystemEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/SizeSystemEnumeration", "SizeSystemEnumeration")


class RefundTypeEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/RefundTypeEnumeration", "RefundTypeEnumeration")


class MediaEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/MediaEnumeration", "MediaEnumeration")


class ReturnFeesEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/ReturnFeesEnumeration", "ReturnFeesEnumeration")


class TierBenefitEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/TierBenefitEnumeration", "TierBenefitEnumeration")


class PhysicalActivityCategory(Enumeration):
    term = RdfTerm(
        "http://schema.org/PhysicalActivityCategory", "PhysicalActivityCategory"
    )


class NonprofitType(Enumeration):
    term = RdfTerm("http://schema.org/NonprofitType", "NonprofitType")


class StatusEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/StatusEnumeration", "StatusEnumeration")


class MeasurementMethodEnum(Enumeration):
    term = RdfTerm("http://schema.org/MeasurementMethodEnum", "MeasurementMethodEnum")


class BusinessEntityType(Enumeration):
    term = RdfTerm("http://schema.org/BusinessEntityType", "BusinessEntityType")


class IncentiveQualifiedExpenseType(Enumeration):
    term = RdfTerm(
        "http://schema.org/IncentiveQualifiedExpenseType",
        "IncentiveQualifiedExpenseType",
    )


class EnergyEfficiencyEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/EnergyEfficiencyEnumeration", "EnergyEfficiencyEnumeration"
    )


class MerchantReturnEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/MerchantReturnEnumeration", "MerchantReturnEnumeration"
    )


class GenderType(Enumeration):
    term = RdfTerm("http://schema.org/GenderType", "GenderType")


class MusicAlbumReleaseType(Enumeration):
    term = RdfTerm("http://schema.org/MusicAlbumReleaseType", "MusicAlbumReleaseType")


class WarrantyScope(Enumeration):
    term = RdfTerm("http://schema.org/WarrantyScope", "WarrantyScope")


class QualitativeValue(Enumeration):
    term = RdfTerm("http://schema.org/QualitativeValue", "QualitativeValue")


class ItemListOrderType(Enumeration):
    term = RdfTerm("http://schema.org/ItemListOrderType", "ItemListOrderType")


class MusicReleaseFormatType(Enumeration):
    term = RdfTerm("http://schema.org/MusicReleaseFormatType", "MusicReleaseFormatType")


class ContactPointOption(Enumeration):
    term = RdfTerm("http://schema.org/ContactPointOption", "ContactPointOption")


class MeasurementTypeEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/MeasurementTypeEnumeration", "MeasurementTypeEnumeration"
    )


class CertificationStatusEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/CertificationStatusEnumeration",
        "CertificationStatusEnumeration",
    )


class DigitalPlatformEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/DigitalPlatformEnumeration", "DigitalPlatformEnumeration"
    )


class PriceComponentTypeEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/PriceComponentTypeEnumeration",
        "PriceComponentTypeEnumeration",
    )


class DigitalDocumentPermissionType(Enumeration):
    term = RdfTerm(
        "http://schema.org/DigitalDocumentPermissionType",
        "DigitalDocumentPermissionType",
    )


class PurchaseType(Enumeration):
    term = RdfTerm("http://schema.org/PurchaseType", "PurchaseType")


class PriceTypeEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/PriceTypeEnumeration", "PriceTypeEnumeration")


class IncentiveType(Enumeration):
    term = RdfTerm("http://schema.org/IncentiveType", "IncentiveType")


class DayOfWeek(Enumeration):
    term = RdfTerm("http://schema.org/DayOfWeek", "DayOfWeek")


class MediaManipulationRatingEnumeration(Enumeration):
    term = RdfTerm(
        "http://schema.org/MediaManipulationRatingEnumeration",
        "MediaManipulationRatingEnumeration",
    )


class BoardingPolicyType(Enumeration):
    term = RdfTerm("http://schema.org/BoardingPolicyType", "BoardingPolicyType")


class SizeGroupEnumeration(Enumeration):
    term = RdfTerm("http://schema.org/SizeGroupEnumeration", "SizeGroupEnumeration")


class PaymentMethodType(Enumeration):
    term = RdfTerm("http://schema.org/PaymentMethodType", "PaymentMethodType")


class AggregateRating(Rating):
    term = RdfTerm("http://schema.org/AggregateRating", "AggregateRating")


class EndorsementRating(Rating):
    term = RdfTerm("http://schema.org/EndorsementRating", "EndorsementRating")


class HowToStep(ListItem, ItemList, CreativeWork):
    term = RdfTerm("http://schema.org/HowToStep", "HowToStep")


class HowToSection(ListItem, ItemList, CreativeWork):
    term = RdfTerm("http://schema.org/HowToSection", "HowToSection")


class BreadcrumbList(ItemList):
    term = RdfTerm("http://schema.org/BreadcrumbList", "BreadcrumbList")


class OfferCatalog(ItemList):
    term = RdfTerm("http://schema.org/OfferCatalog", "OfferCatalog")


class EventSeries(Series, Event):
    term = RdfTerm("http://schema.org/EventSeries", "EventSeries")


class CreativeWorkSeries(Series, CreativeWork):
    term = RdfTerm("http://schema.org/CreativeWorkSeries", "CreativeWorkSeries")


class Researcher(Audience):
    term = RdfTerm("http://schema.org/Researcher", "Researcher")


class EducationalAudience(Audience):
    term = RdfTerm("http://schema.org/EducationalAudience", "EducationalAudience")


class BusinessAudience(Audience):
    term = RdfTerm("http://schema.org/BusinessAudience", "BusinessAudience")


class PeopleAudience(Audience):
    term = RdfTerm("http://schema.org/PeopleAudience", "PeopleAudience")


class OfferForPurchase(Offer):
    term = RdfTerm("http://schema.org/OfferForPurchase", "OfferForPurchase")


class AggregateOffer(Offer):
    term = RdfTerm("http://schema.org/AggregateOffer", "AggregateOffer")


class OfferForLease(Offer):
    term = RdfTerm("http://schema.org/OfferForLease", "OfferForLease")


class PerformanceRole(Role):
    term = RdfTerm("http://schema.org/PerformanceRole", "PerformanceRole")


class OrganizationRole(Role):
    term = RdfTerm("http://schema.org/OrganizationRole", "OrganizationRole")


class LinkRole(Role):
    term = RdfTerm("http://schema.org/LinkRole", "LinkRole")


class TrainReservation(Reservation):
    term = RdfTerm("http://schema.org/TrainReservation", "TrainReservation")


class BoatReservation(Reservation):
    term = RdfTerm("http://schema.org/BoatReservation", "BoatReservation")


class FlightReservation(Reservation):
    term = RdfTerm("http://schema.org/FlightReservation", "FlightReservation")


class ReservationPackage(Reservation):
    term = RdfTerm("http://schema.org/ReservationPackage", "ReservationPackage")


class TaxiReservation(Reservation):
    term = RdfTerm("http://schema.org/TaxiReservation", "TaxiReservation")


class LodgingReservation(Reservation):
    term = RdfTerm("http://schema.org/LodgingReservation", "LodgingReservation")


class FoodEstablishmentReservation(Reservation):
    term = RdfTerm(
        "http://schema.org/FoodEstablishmentReservation", "FoodEstablishmentReservation"
    )


class BusReservation(Reservation):
    term = RdfTerm("http://schema.org/BusReservation", "BusReservation")


class RentalCarReservation(Reservation):
    term = RdfTerm("http://schema.org/RentalCarReservation", "RentalCarReservation")


class EventReservation(Reservation):
    term = RdfTerm("http://schema.org/EventReservation", "EventReservation")


class TheaterGroup(PerformingGroup):
    term = RdfTerm("http://schema.org/TheaterGroup", "TheaterGroup")


class MusicGroup(PerformingGroup):
    term = RdfTerm("http://schema.org/MusicGroup", "MusicGroup")


class DanceGroup(PerformingGroup):
    term = RdfTerm("http://schema.org/DanceGroup", "DanceGroup")


class OnlineStore(OnlineBusiness):
    term = RdfTerm("http://schema.org/OnlineStore", "OnlineStore")


class FundingAgency(Project):
    term = RdfTerm("http://schema.org/FundingAgency", "FundingAgency")


class ResearchProject(Project):
    term = RdfTerm("http://schema.org/ResearchProject", "ResearchProject")


class DiagnosticLab(MedicalOrganization):
    term = RdfTerm("http://schema.org/DiagnosticLab", "DiagnosticLab")


class VeterinaryCare(MedicalOrganization):
    term = RdfTerm("http://schema.org/VeterinaryCare", "VeterinaryCare")


class SportsTeam(SportsOrganization):
    term = RdfTerm("http://schema.org/SportsTeam", "SportsTeam")


class CampingPitch(Accommodation):
    term = RdfTerm("http://schema.org/CampingPitch", "CampingPitch")


class House(Accommodation):
    term = RdfTerm("http://schema.org/House", "House")


class Room(Accommodation):
    term = RdfTerm("http://schema.org/Room", "Room")


class Suite(Accommodation):
    term = RdfTerm("http://schema.org/Suite", "Suite")


class Apartment(Accommodation):
    term = RdfTerm("http://schema.org/Apartment", "Apartment")


class Library(LocalBusiness):
    term = RdfTerm("http://schema.org/Library", "Library")


class GovernmentOffice(LocalBusiness):
    term = RdfTerm("http://schema.org/GovernmentOffice", "GovernmentOffice")


class Store(LocalBusiness):
    term = RdfTerm("http://schema.org/Store", "Store")


class RecyclingCenter(LocalBusiness):
    term = RdfTerm("http://schema.org/RecyclingCenter", "RecyclingCenter")


class FinancialService(LocalBusiness):
    term = RdfTerm("http://schema.org/FinancialService", "FinancialService")


class EmergencyService(LocalBusiness):
    term = RdfTerm("http://schema.org/EmergencyService", "EmergencyService")


class FoodEstablishment(LocalBusiness):
    term = RdfTerm("http://schema.org/FoodEstablishment", "FoodEstablishment")


class EntertainmentBusiness(LocalBusiness):
    term = RdfTerm("http://schema.org/EntertainmentBusiness", "EntertainmentBusiness")


class InternetCafe(LocalBusiness):
    term = RdfTerm("http://schema.org/InternetCafe", "InternetCafe")


class ChildCare(LocalBusiness):
    term = RdfTerm("http://schema.org/ChildCare", "ChildCare")


class MedicalBusiness(LocalBusiness):
    term = RdfTerm("http://schema.org/MedicalBusiness", "MedicalBusiness")


class HomeAndConstructionBusiness(LocalBusiness):
    term = RdfTerm(
        "http://schema.org/HomeAndConstructionBusiness", "HomeAndConstructionBusiness"
    )


class TravelAgency(LocalBusiness):
    term = RdfTerm("http://schema.org/TravelAgency", "TravelAgency")


class SportsActivityLocation(LocalBusiness):
    term = RdfTerm("http://schema.org/SportsActivityLocation", "SportsActivityLocation")


class TouristInformationCenter(LocalBusiness):
    term = RdfTerm(
        "http://schema.org/TouristInformationCenter", "TouristInformationCenter"
    )


class ProfessionalService(LocalBusiness):
    term = RdfTerm("http://schema.org/ProfessionalService", "ProfessionalService")


class RadioStation(LocalBusiness):
    term = RdfTerm("http://schema.org/RadioStation", "RadioStation")


class HealthAndBeautyBusiness(LocalBusiness):
    term = RdfTerm(
        "http://schema.org/HealthAndBeautyBusiness", "HealthAndBeautyBusiness"
    )


class DryCleaningOrLaundry(LocalBusiness):
    term = RdfTerm("http://schema.org/DryCleaningOrLaundry", "DryCleaningOrLaundry")


class ArchiveOrganization(LocalBusiness):
    term = RdfTerm("http://schema.org/ArchiveOrganization", "ArchiveOrganization")


class LodgingBusiness(LocalBusiness):
    term = RdfTerm("http://schema.org/LodgingBusiness", "LodgingBusiness")


class AutomotiveBusiness(LocalBusiness):
    term = RdfTerm("http://schema.org/AutomotiveBusiness", "AutomotiveBusiness")


class AnimalShelter(LocalBusiness):
    term = RdfTerm("http://schema.org/AnimalShelter", "AnimalShelter")


class ShoppingCenter(LocalBusiness):
    term = RdfTerm("http://schema.org/ShoppingCenter", "ShoppingCenter")


class TelevisionStation(LocalBusiness):
    term = RdfTerm("http://schema.org/TelevisionStation", "TelevisionStation")


class SelfStorage(LocalBusiness):
    term = RdfTerm("http://schema.org/SelfStorage", "SelfStorage")


class RealEstateAgent(LocalBusiness):
    term = RdfTerm("http://schema.org/RealEstateAgent", "RealEstateAgent")


class LegalService(LocalBusiness):
    term = RdfTerm("http://schema.org/LegalService", "LegalService")


class EmploymentAgency(LocalBusiness):
    term = RdfTerm("http://schema.org/EmploymentAgency", "EmploymentAgency")


class GatedResidenceCommunity(Residence):
    term = RdfTerm(
        "http://schema.org/GatedResidenceCommunity", "GatedResidenceCommunity"
    )


class ApartmentComplex(Residence):
    term = RdfTerm("http://schema.org/ApartmentComplex", "ApartmentComplex")


class EventVenue(CivicStructure):
    term = RdfTerm("http://schema.org/EventVenue", "EventVenue")


class BusStop(CivicStructure):
    term = RdfTerm("http://schema.org/BusStop", "BusStop")


class Bridge(CivicStructure):
    term = RdfTerm("http://schema.org/Bridge", "Bridge")


class ParkingFacility(CivicStructure):
    term = RdfTerm("http://schema.org/ParkingFacility", "ParkingFacility")


class EducationalOrganization(CivicStructure, Organization):
    term = RdfTerm(
        "http://schema.org/EducationalOrganization", "EducationalOrganization"
    )


class SubwayStation(CivicStructure):
    term = RdfTerm("http://schema.org/SubwayStation", "SubwayStation")


class TaxiStand(CivicStructure):
    term = RdfTerm("http://schema.org/TaxiStand", "TaxiStand")


class Beach(CivicStructure):
    term = RdfTerm("http://schema.org/Beach", "Beach")


class PublicToilet(CivicStructure):
    term = RdfTerm("http://schema.org/PublicToilet", "PublicToilet")


class BoatTerminal(CivicStructure):
    term = RdfTerm("http://schema.org/BoatTerminal", "BoatTerminal")


class Playground(CivicStructure):
    term = RdfTerm("http://schema.org/Playground", "Playground")


class BusStation(CivicStructure):
    term = RdfTerm("http://schema.org/BusStation", "BusStation")


class PlaceOfWorship(CivicStructure):
    term = RdfTerm("http://schema.org/PlaceOfWorship", "PlaceOfWorship")


class Crematorium(CivicStructure):
    term = RdfTerm("http://schema.org/Crematorium", "Crematorium")


class Museum(CivicStructure):
    term = RdfTerm("http://schema.org/Museum", "Museum")


class RVPark(CivicStructure):
    term = RdfTerm("http://schema.org/RVPark", "RVPark")


class MusicVenue(CivicStructure):
    term = RdfTerm("http://schema.org/MusicVenue", "MusicVenue")


class Airport(CivicStructure):
    term = RdfTerm("http://schema.org/Airport", "Airport")


class Zoo(CivicStructure):
    term = RdfTerm("http://schema.org/Zoo", "Zoo")


class Park(CivicStructure):
    term = RdfTerm("http://schema.org/Park", "Park")


class GovernmentBuilding(CivicStructure):
    term = RdfTerm("http://schema.org/GovernmentBuilding", "GovernmentBuilding")


class TrainStation(CivicStructure):
    term = RdfTerm("http://schema.org/TrainStation", "TrainStation")


class Cemetery(CivicStructure):
    term = RdfTerm("http://schema.org/Cemetery", "Cemetery")


class Aquarium(CivicStructure):
    term = RdfTerm("http://schema.org/Aquarium", "Aquarium")


class PerformingArtsTheater(CivicStructure):
    term = RdfTerm("http://schema.org/PerformingArtsTheater", "PerformingArtsTheater")


class BodyOfWater(Landform):
    term = RdfTerm("http://schema.org/BodyOfWater", "BodyOfWater")


class Volcano(Landform):
    term = RdfTerm("http://schema.org/Volcano", "Volcano")


class Continent(Landform):
    term = RdfTerm("http://schema.org/Continent", "Continent")


class Mountain(Landform):
    term = RdfTerm("http://schema.org/Mountain", "Mountain")


class State(AdministrativeArea):
    term = RdfTerm("http://schema.org/State", "State")


class City(AdministrativeArea):
    term = RdfTerm("http://schema.org/City", "City")


class Country(AdministrativeArea):
    term = RdfTerm("http://schema.org/Country", "Country")


class SchoolDistrict(AdministrativeArea):
    term = RdfTerm("http://schema.org/SchoolDistrict", "SchoolDistrict")


class Diet(LifestyleModification, CreativeWork):
    term = RdfTerm("http://schema.org/Diet", "Diet")


class PhysicalActivity(LifestyleModification):
    term = RdfTerm("http://schema.org/PhysicalActivity", "PhysicalActivity")


class DrugStrength(MedicalIntangible):
    term = RdfTerm("http://schema.org/DrugStrength", "DrugStrength")


class DoseSchedule(MedicalIntangible):
    term = RdfTerm("http://schema.org/DoseSchedule", "DoseSchedule")


class MedicalConditionStage(MedicalIntangible):
    term = RdfTerm("http://schema.org/MedicalConditionStage", "MedicalConditionStage")


class DrugLegalStatus(MedicalIntangible):
    term = RdfTerm("http://schema.org/DrugLegalStatus", "DrugLegalStatus")


class DDxElement(MedicalIntangible):
    term = RdfTerm("http://schema.org/DDxElement", "DDxElement")


class SurgicalProcedure(MedicalProcedure):
    term = RdfTerm("http://schema.org/SurgicalProcedure", "SurgicalProcedure")


class TherapeuticProcedure(MedicalProcedure):
    term = RdfTerm("http://schema.org/TherapeuticProcedure", "TherapeuticProcedure")


class DiagnosticProcedure(MedicalProcedure):
    term = RdfTerm("http://schema.org/DiagnosticProcedure", "DiagnosticProcedure")


class MedicalRiskCalculator(MedicalRiskEstimator):
    term = RdfTerm("http://schema.org/MedicalRiskCalculator", "MedicalRiskCalculator")


class MedicalRiskScore(MedicalRiskEstimator):
    term = RdfTerm("http://schema.org/MedicalRiskScore", "MedicalRiskScore")


class PreventionIndication(MedicalIndication):
    term = RdfTerm("http://schema.org/PreventionIndication", "PreventionIndication")


class TreatmentIndication(MedicalIndication):
    term = RdfTerm("http://schema.org/TreatmentIndication", "TreatmentIndication")


class ApprovedIndication(MedicalIndication):
    term = RdfTerm("http://schema.org/ApprovedIndication", "ApprovedIndication")


class Nerve(AnatomicalStructure):
    term = RdfTerm("http://schema.org/Nerve", "Nerve")


class Vessel(AnatomicalStructure):
    term = RdfTerm("http://schema.org/Vessel", "Vessel")


class Muscle(AnatomicalStructure):
    term = RdfTerm("http://schema.org/Muscle", "Muscle")


class Ligament(AnatomicalStructure):
    term = RdfTerm("http://schema.org/Ligament", "Ligament")


class Joint(AnatomicalStructure):
    term = RdfTerm("http://schema.org/Joint", "Joint")


class Bone(AnatomicalStructure):
    term = RdfTerm("http://schema.org/Bone", "Bone")


class BrainStructure(AnatomicalStructure):
    term = RdfTerm("http://schema.org/BrainStructure", "BrainStructure")


class MedicalTrial(MedicalStudy):
    term = RdfTerm("http://schema.org/MedicalTrial", "MedicalTrial")


class MedicalObservationalStudy(MedicalStudy):
    term = RdfTerm(
        "http://schema.org/MedicalObservationalStudy", "MedicalObservationalStudy"
    )


class MedicalGuidelineContraindication(MedicalGuideline):
    term = RdfTerm(
        "http://schema.org/MedicalGuidelineContraindication",
        "MedicalGuidelineContraindication",
    )


class MedicalGuidelineRecommendation(MedicalGuideline):
    term = RdfTerm(
        "http://schema.org/MedicalGuidelineRecommendation",
        "MedicalGuidelineRecommendation",
    )


class Drug(Substance, Product):
    term = RdfTerm("http://schema.org/Drug", "Drug")


class DietarySupplement(Substance, Product):
    term = RdfTerm("http://schema.org/DietarySupplement", "DietarySupplement")


class MedicalSignOrSymptom(MedicalCondition):
    term = RdfTerm("http://schema.org/MedicalSignOrSymptom", "MedicalSignOrSymptom")


class InfectiousDisease(MedicalCondition):
    term = RdfTerm("http://schema.org/InfectiousDisease", "InfectiousDisease")


class BloodTest(MedicalTest):
    term = RdfTerm("http://schema.org/BloodTest", "BloodTest")


class ImagingTest(MedicalTest):
    term = RdfTerm("http://schema.org/ImagingTest", "ImagingTest")


class MedicalTestPanel(MedicalTest):
    term = RdfTerm("http://schema.org/MedicalTestPanel", "MedicalTestPanel")


class PathologyTest(MedicalTest):
    term = RdfTerm("http://schema.org/PathologyTest", "PathologyTest")


class Report(Article):
    term = RdfTerm("http://schema.org/Report", "Report")


class TechArticle(Article):
    term = RdfTerm("http://schema.org/TechArticle", "TechArticle")


class SatiricalArticle(Article):
    term = RdfTerm("http://schema.org/SatiricalArticle", "SatiricalArticle")


class NewsArticle(Article):
    term = RdfTerm("http://schema.org/NewsArticle", "NewsArticle")


class SocialMediaPosting(Article):
    term = RdfTerm("http://schema.org/SocialMediaPosting", "SocialMediaPosting")


class AdvertiserContentArticle(Article):
    term = RdfTerm(
        "http://schema.org/AdvertiserContentArticle", "AdvertiserContentArticle"
    )


class ScholarlyArticle(Article):
    term = RdfTerm("http://schema.org/ScholarlyArticle", "ScholarlyArticle")


class Recipe(HowTo):
    term = RdfTerm("http://schema.org/Recipe", "Recipe")


class ClaimReview(Review):
    term = RdfTerm("http://schema.org/ClaimReview", "ClaimReview")


class MediaReview(Review):
    term = RdfTerm("http://schema.org/MediaReview", "MediaReview")


class UserReview(Review):
    term = RdfTerm("http://schema.org/UserReview", "UserReview")


class CriticReview(Review):
    term = RdfTerm("http://schema.org/CriticReview", "CriticReview")


class Recommendation(Review):
    term = RdfTerm("http://schema.org/Recommendation", "Recommendation")


class EmployerReview(Review):
    term = RdfTerm("http://schema.org/EmployerReview", "EmployerReview")


class CategoryCodeSet(DefinedTermSet):
    term = RdfTerm("http://schema.org/CategoryCodeSet", "CategoryCodeSet")


class VideoObject(MediaObject):
    term = RdfTerm("http://schema.org/VideoObject", "VideoObject")


class LegislationObject(Legislation, MediaObject):
    term = RdfTerm("http://schema.org/LegislationObject", "LegislationObject")


class AudioObject(MediaObject):
    term = RdfTerm("http://schema.org/AudioObject", "AudioObject")


class DataDownload(MediaObject):
    term = RdfTerm("http://schema.org/DataDownload", "DataDownload")


class AmpStory(MediaObject, CreativeWork):
    term = RdfTerm("http://schema.org/AmpStory", "AmpStory")


class ImageObject(MediaObject):
    term = RdfTerm("http://schema.org/ImageObject", "ImageObject")


class MusicVideoObject(MediaObject):
    term = RdfTerm("http://schema.org/MusicVideoObject", "MusicVideoObject")


class TextObject(MediaObject):
    term = RdfTerm("http://schema.org/TextObject", "TextObject")


class _3DModel(MediaObject):
    term = RdfTerm("http://schema.org/3DModel", "3DModel")


class PodcastEpisode(Episode):
    term = RdfTerm("http://schema.org/PodcastEpisode", "PodcastEpisode")


class RadioEpisode(Episode):
    term = RdfTerm("http://schema.org/RadioEpisode", "RadioEpisode")


class TVEpisode(Episode):
    term = RdfTerm("http://schema.org/TVEpisode", "TVEpisode")


class HealthTopicContent(WebContent):
    term = RdfTerm("http://schema.org/HealthTopicContent", "HealthTopicContent")


class PodcastSeason(CreativeWorkSeason):
    term = RdfTerm("http://schema.org/PodcastSeason", "PodcastSeason")


class TVSeason(CreativeWorkSeason, CreativeWork):
    term = RdfTerm("http://schema.org/TVSeason", "TVSeason")


class RadioSeason(CreativeWorkSeason):
    term = RdfTerm("http://schema.org/RadioSeason", "RadioSeason")


class MusicRelease(MusicPlaylist):
    term = RdfTerm("http://schema.org/MusicRelease", "MusicRelease")


class MusicAlbum(MusicPlaylist):
    term = RdfTerm("http://schema.org/MusicAlbum", "MusicAlbum")


class MobileApplication(SoftwareApplication):
    term = RdfTerm("http://schema.org/MobileApplication", "MobileApplication")


class WebApplication(SoftwareApplication):
    term = RdfTerm("http://schema.org/WebApplication", "WebApplication")


class VideoGameClip(Clip):
    term = RdfTerm("http://schema.org/VideoGameClip", "VideoGameClip")


class MovieClip(Clip):
    term = RdfTerm("http://schema.org/MovieClip", "MovieClip")


class TVClip(Clip):
    term = RdfTerm("http://schema.org/TVClip", "TVClip")


class RadioClip(Clip):
    term = RdfTerm("http://schema.org/RadioClip", "RadioClip")


class VideoGame(Game, SoftwareApplication):
    term = RdfTerm("http://schema.org/VideoGame", "VideoGame")


class PresentationDigitalDocument(DigitalDocument):
    term = RdfTerm(
        "http://schema.org/PresentationDigitalDocument", "PresentationDigitalDocument"
    )


class TextDigitalDocument(DigitalDocument):
    term = RdfTerm("http://schema.org/TextDigitalDocument", "TextDigitalDocument")


class SpreadsheetDigitalDocument(DigitalDocument):
    term = RdfTerm(
        "http://schema.org/SpreadsheetDigitalDocument", "SpreadsheetDigitalDocument"
    )


class NoteDigitalDocument(DigitalDocument):
    term = RdfTerm("http://schema.org/NoteDigitalDocument", "NoteDigitalDocument")


class ProductCollection(Collection, Product):
    term = RdfTerm("http://schema.org/ProductCollection", "ProductCollection")


class DataFeed(Dataset):
    term = RdfTerm("http://schema.org/DataFeed", "DataFeed")


class Course(LearningResource, CreativeWork):
    term = RdfTerm("http://schema.org/Course", "Course")


class Quiz(LearningResource):
    term = RdfTerm("http://schema.org/Quiz", "Quiz")


class Syllabus(LearningResource):
    term = RdfTerm("http://schema.org/Syllabus", "Syllabus")


class CoverArt(VisualArtwork):
    term = RdfTerm("http://schema.org/CoverArt", "CoverArt")


class WPFooter(WebPageElement):
    term = RdfTerm("http://schema.org/WPFooter", "WPFooter")


class WPSideBar(WebPageElement):
    term = RdfTerm("http://schema.org/WPSideBar", "WPSideBar")


class WPHeader(WebPageElement):
    term = RdfTerm("http://schema.org/WPHeader", "WPHeader")


class SiteNavigationElement(WebPageElement):
    term = RdfTerm("http://schema.org/SiteNavigationElement", "SiteNavigationElement")


class Table(WebPageElement):
    term = RdfTerm("http://schema.org/Table", "Table")


class WPAdBlock(WebPageElement):
    term = RdfTerm("http://schema.org/WPAdBlock", "WPAdBlock")


class ComicIssue(PublicationIssue):
    term = RdfTerm("http://schema.org/ComicIssue", "ComicIssue")


class ContactPage(WebPage):
    term = RdfTerm("http://schema.org/ContactPage", "ContactPage")


class CollectionPage(WebPage):
    term = RdfTerm("http://schema.org/CollectionPage", "CollectionPage")


class QAPage(WebPage):
    term = RdfTerm("http://schema.org/QAPage", "QAPage")


class MedicalWebPage(WebPage):
    term = RdfTerm("http://schema.org/MedicalWebPage", "MedicalWebPage")


class RealEstateListing(WebPage):
    term = RdfTerm("http://schema.org/RealEstateListing", "RealEstateListing")


class SearchResultsPage(WebPage):
    term = RdfTerm("http://schema.org/SearchResultsPage", "SearchResultsPage")


class AboutPage(WebPage):
    term = RdfTerm("http://schema.org/AboutPage", "AboutPage")


class FAQPage(WebPage):
    term = RdfTerm("http://schema.org/FAQPage", "FAQPage")


class CheckoutPage(WebPage):
    term = RdfTerm("http://schema.org/CheckoutPage", "CheckoutPage")


class ProfilePage(WebPage):
    term = RdfTerm("http://schema.org/ProfilePage", "ProfilePage")


class ItemPage(WebPage):
    term = RdfTerm("http://schema.org/ItemPage", "ItemPage")


class EmailMessage(Message):
    term = RdfTerm("http://schema.org/EmailMessage", "EmailMessage")


class Question(Comment):
    term = RdfTerm("http://schema.org/Question", "Question")


class CorrectionComment(Comment):
    term = RdfTerm("http://schema.org/CorrectionComment", "CorrectionComment")


class Answer(Comment):
    term = RdfTerm("http://schema.org/Answer", "Answer")


class UserPlusOnes(UserInteraction):
    term = RdfTerm("http://schema.org/UserPlusOnes", "UserPlusOnes")


class UserDownloads(UserInteraction):
    term = RdfTerm("http://schema.org/UserDownloads", "UserDownloads")


class UserComments(UserInteraction):
    term = RdfTerm("http://schema.org/UserComments", "UserComments")


class UserBlocks(UserInteraction):
    term = RdfTerm("http://schema.org/UserBlocks", "UserBlocks")


class UserPlays(UserInteraction):
    term = RdfTerm("http://schema.org/UserPlays", "UserPlays")


class UserTweets(UserInteraction):
    term = RdfTerm("http://schema.org/UserTweets", "UserTweets")


class UserCheckins(UserInteraction):
    term = RdfTerm("http://schema.org/UserCheckins", "UserCheckins")


class UserPageVisits(UserInteraction):
    term = RdfTerm("http://schema.org/UserPageVisits", "UserPageVisits")


class UserLikes(UserInteraction):
    term = RdfTerm("http://schema.org/UserLikes", "UserLikes")


class OnDemandEvent(PublicationEvent):
    term = RdfTerm("http://schema.org/OnDemandEvent", "OnDemandEvent")


class BroadcastEvent(PublicationEvent):
    term = RdfTerm("http://schema.org/BroadcastEvent", "BroadcastEvent")


class ShareAction(CommunicateAction):
    term = RdfTerm("http://schema.org/ShareAction", "ShareAction")


class CommentAction(CommunicateAction):
    term = RdfTerm("http://schema.org/CommentAction", "CommentAction")


class InformAction(CommunicateAction):
    term = RdfTerm("http://schema.org/InformAction", "InformAction")


class CheckInAction(CommunicateAction):
    term = RdfTerm("http://schema.org/CheckInAction", "CheckInAction")


class InviteAction(CommunicateAction):
    term = RdfTerm("http://schema.org/InviteAction", "InviteAction")


class CheckOutAction(CommunicateAction):
    term = RdfTerm("http://schema.org/CheckOutAction", "CheckOutAction")


class ReplyAction(CommunicateAction):
    term = RdfTerm("http://schema.org/ReplyAction", "ReplyAction")


class AskAction(CommunicateAction):
    term = RdfTerm("http://schema.org/AskAction", "AskAction")


class InsertAction(AddAction):
    term = RdfTerm("http://schema.org/InsertAction", "InsertAction")


class CancelAction(PlanAction):
    term = RdfTerm("http://schema.org/CancelAction", "CancelAction")


class ScheduleAction(PlanAction):
    term = RdfTerm("http://schema.org/ScheduleAction", "ScheduleAction")


class ReserveAction(PlanAction):
    term = RdfTerm("http://schema.org/ReserveAction", "ReserveAction")


class AuthorizeAction(AllocateAction):
    term = RdfTerm("http://schema.org/AuthorizeAction", "AuthorizeAction")


class AssignAction(AllocateAction):
    term = RdfTerm("http://schema.org/AssignAction", "AssignAction")


class AcceptAction(AllocateAction):
    term = RdfTerm("http://schema.org/AcceptAction", "AcceptAction")


class RejectAction(AllocateAction):
    term = RdfTerm("http://schema.org/RejectAction", "RejectAction")


class AgreeAction(ReactAction):
    term = RdfTerm("http://schema.org/AgreeAction", "AgreeAction")


class DisagreeAction(ReactAction):
    term = RdfTerm("http://schema.org/DisagreeAction", "DisagreeAction")


class EndorseAction(ReactAction):
    term = RdfTerm("http://schema.org/EndorseAction", "EndorseAction")


class WantAction(ReactAction):
    term = RdfTerm("http://schema.org/WantAction", "WantAction")


class LikeAction(ReactAction):
    term = RdfTerm("http://schema.org/LikeAction", "LikeAction")


class DislikeAction(ReactAction):
    term = RdfTerm("http://schema.org/DislikeAction", "DislikeAction")


class VoteAction(ChooseAction):
    term = RdfTerm("http://schema.org/VoteAction", "VoteAction")


class WearAction(UseAction):
    term = RdfTerm("http://schema.org/WearAction", "WearAction")


class HowToSupply(HowToItem):
    term = RdfTerm("http://schema.org/HowToSupply", "HowToSupply")


class HowToTool(HowToItem):
    term = RdfTerm("http://schema.org/HowToTool", "HowToTool")


class PostalAddress(ContactPoint):
    term = RdfTerm("http://schema.org/PostalAddress", "PostalAddress")


class Observation(QuantitativeValue, Intangible):
    term = RdfTerm("http://schema.org/Observation", "Observation")


class PaymentChargeSpecification(PriceSpecification):
    term = RdfTerm(
        "http://schema.org/PaymentChargeSpecification", "PaymentChargeSpecification"
    )


class CompoundPriceSpecification(PriceSpecification):
    term = RdfTerm(
        "http://schema.org/CompoundPriceSpecification", "CompoundPriceSpecification"
    )


class UnitPriceSpecification(PriceSpecification):
    term = RdfTerm("http://schema.org/UnitPriceSpecification", "UnitPriceSpecification")


class DeliveryChargeSpecification(PriceSpecification):
    term = RdfTerm(
        "http://schema.org/DeliveryChargeSpecification", "DeliveryChargeSpecification"
    )


class LocationFeatureSpecification(PropertyValue):
    term = RdfTerm(
        "http://schema.org/LocationFeatureSpecification", "LocationFeatureSpecification"
    )


class GeoCircle(GeoShape):
    term = RdfTerm("http://schema.org/GeoCircle", "GeoCircle")


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    term = RdfTerm(
        "http://schema.org/MonetaryAmountDistribution", "MonetaryAmountDistribution"
    )


class MedicalCode(CategoryCode, MedicalIntangible):
    term = RdfTerm("http://schema.org/MedicalCode", "MedicalCode")


class LoanOrCredit(FinancialProduct):
    term = RdfTerm("http://schema.org/LoanOrCredit", "LoanOrCredit")


class PaymentService(FinancialProduct, PaymentMethod):
    term = RdfTerm("http://schema.org/PaymentService", "PaymentService")


class PaymentCard(FinancialProduct, PaymentMethod):
    term = RdfTerm("http://schema.org/PaymentCard", "PaymentCard")


class CurrencyConversionService(FinancialProduct):
    term = RdfTerm(
        "http://schema.org/CurrencyConversionService", "CurrencyConversionService"
    )


class BankAccount(FinancialProduct):
    term = RdfTerm("http://schema.org/BankAccount", "BankAccount")


class InvestmentOrDeposit(FinancialProduct):
    term = RdfTerm("http://schema.org/InvestmentOrDeposit", "InvestmentOrDeposit")


class RadioBroadcastService(BroadcastService):
    term = RdfTerm("http://schema.org/RadioBroadcastService", "RadioBroadcastService")


class AMRadioChannel(RadioChannel):
    term = RdfTerm("http://schema.org/AMRadioChannel", "AMRadioChannel")


class FMRadioChannel(RadioChannel):
    term = RdfTerm("http://schema.org/FMRadioChannel", "FMRadioChannel")


class DrugCostCategory(MedicalEnumeration):
    term = RdfTerm("http://schema.org/DrugCostCategory", "DrugCostCategory")


class InfectiousAgentClass(MedicalEnumeration):
    term = RdfTerm("http://schema.org/InfectiousAgentClass", "InfectiousAgentClass")


class MedicalImagingTechnique(MedicalEnumeration):
    term = RdfTerm(
        "http://schema.org/MedicalImagingTechnique", "MedicalImagingTechnique"
    )


class MedicalSpecialty(Specialty, MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicalSpecialty", "MedicalSpecialty")


class DrugPrescriptionStatus(MedicalEnumeration):
    term = RdfTerm("http://schema.org/DrugPrescriptionStatus", "DrugPrescriptionStatus")


class MedicalProcedureType(MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicalProcedureType", "MedicalProcedureType")


class MedicalDevicePurpose(MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicalDevicePurpose", "MedicalDevicePurpose")


class MedicalObservationalStudyDesign(MedicalEnumeration):
    term = RdfTerm(
        "http://schema.org/MedicalObservationalStudyDesign",
        "MedicalObservationalStudyDesign",
    )


class MedicalEvidenceLevel(MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicalEvidenceLevel", "MedicalEvidenceLevel")


class MedicalAudienceType(MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicalAudienceType", "MedicalAudienceType")


class DrugPregnancyCategory(MedicalEnumeration):
    term = RdfTerm("http://schema.org/DrugPregnancyCategory", "DrugPregnancyCategory")


class MedicineSystem(MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicineSystem", "MedicineSystem")


class PhysicalExam(MedicalEnumeration, MedicalProcedure):
    term = RdfTerm("http://schema.org/PhysicalExam", "PhysicalExam")


class MedicalTrialDesign(MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicalTrialDesign", "MedicalTrialDesign")


class MedicalStudyStatus(MedicalEnumeration):
    term = RdfTerm("http://schema.org/MedicalStudyStatus", "MedicalStudyStatus")


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    term = RdfTerm(
        "http://schema.org/WearableSizeSystemEnumeration",
        "WearableSizeSystemEnumeration",
    )


class IPTCDigitalSourceEnumeration(MediaEnumeration):
    term = RdfTerm(
        "http://schema.org/IPTCDigitalSourceEnumeration", "IPTCDigitalSourceEnumeration"
    )


class NLNonprofitType(NonprofitType):
    term = RdfTerm("http://schema.org/NLNonprofitType", "NLNonprofitType")


class UKNonprofitType(NonprofitType):
    term = RdfTerm("http://schema.org/UKNonprofitType", "UKNonprofitType")


class USNonprofitType(NonprofitType):
    term = RdfTerm("http://schema.org/USNonprofitType", "USNonprofitType")


class ReservationStatusType(StatusEnumeration):
    term = RdfTerm("http://schema.org/ReservationStatusType", "ReservationStatusType")


class EventStatusType(StatusEnumeration):
    term = RdfTerm("http://schema.org/EventStatusType", "EventStatusType")


class OrderStatus(StatusEnumeration):
    term = RdfTerm("http://schema.org/OrderStatus", "OrderStatus")


class ActionStatusType(StatusEnumeration):
    term = RdfTerm("http://schema.org/ActionStatusType", "ActionStatusType")


class PaymentStatusType(StatusEnumeration):
    term = RdfTerm("http://schema.org/PaymentStatusType", "PaymentStatusType")


class LegalForceStatus(StatusEnumeration):
    term = RdfTerm("http://schema.org/LegalForceStatus", "LegalForceStatus")


class GameServerStatus(StatusEnumeration):
    term = RdfTerm("http://schema.org/GameServerStatus", "GameServerStatus")


class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm(
        "http://schema.org/EnergyStarEnergyEfficiencyEnumeration",
        "EnergyStarEnergyEfficiencyEnumeration",
    )


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    term = RdfTerm(
        "http://schema.org/EUEnergyEfficiencyEnumeration",
        "EUEnergyEfficiencyEnumeration",
    )


class SizeSpecification(QualitativeValue):
    term = RdfTerm("http://schema.org/SizeSpecification", "SizeSpecification")


class DriveWheelConfigurationValue(QualitativeValue):
    term = RdfTerm(
        "http://schema.org/DriveWheelConfigurationValue", "DriveWheelConfigurationValue"
    )


class SteeringPositionValue(QualitativeValue):
    term = RdfTerm("http://schema.org/SteeringPositionValue", "SteeringPositionValue")


class BedType(QualitativeValue):
    term = RdfTerm("http://schema.org/BedType", "BedType")


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm(
        "http://schema.org/BodyMeasurementTypeEnumeration",
        "BodyMeasurementTypeEnumeration",
    )


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    term = RdfTerm(
        "http://schema.org/WearableMeasurementTypeEnumeration",
        "WearableMeasurementTypeEnumeration",
    )


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    term = RdfTerm(
        "http://schema.org/WearableSizeGroupEnumeration", "WearableSizeGroupEnumeration"
    )


class EmployerAggregateRating(AggregateRating):
    term = RdfTerm(
        "http://schema.org/EmployerAggregateRating", "EmployerAggregateRating"
    )


class RadioSeries(CreativeWorkSeries):
    term = RdfTerm("http://schema.org/RadioSeries", "RadioSeries")


class Periodical(CreativeWorkSeries):
    term = RdfTerm("http://schema.org/Periodical", "Periodical")


class BookSeries(CreativeWorkSeries):
    term = RdfTerm("http://schema.org/BookSeries", "BookSeries")


class MovieSeries(CreativeWorkSeries):
    term = RdfTerm("http://schema.org/MovieSeries", "MovieSeries")


class PodcastSeries(CreativeWorkSeries):
    term = RdfTerm("http://schema.org/PodcastSeries", "PodcastSeries")


class TVSeries(CreativeWorkSeries, CreativeWork):
    term = RdfTerm("http://schema.org/TVSeries", "TVSeries")


class VideoGameSeries(CreativeWorkSeries):
    term = RdfTerm("http://schema.org/VideoGameSeries", "VideoGameSeries")


class MedicalAudience(PeopleAudience, Audience):
    term = RdfTerm("http://schema.org/MedicalAudience", "MedicalAudience")


class ParentAudience(PeopleAudience):
    term = RdfTerm("http://schema.org/ParentAudience", "ParentAudience")


class EmployeeRole(OrganizationRole):
    term = RdfTerm("http://schema.org/EmployeeRole", "EmployeeRole")


class SingleFamilyResidence(House):
    term = RdfTerm("http://schema.org/SingleFamilyResidence", "SingleFamilyResidence")


class HotelRoom(Room):
    term = RdfTerm("http://schema.org/HotelRoom", "HotelRoom")


class MeetingRoom(Room):
    term = RdfTerm("http://schema.org/MeetingRoom", "MeetingRoom")


class PostOffice(GovernmentOffice):
    term = RdfTerm("http://schema.org/PostOffice", "PostOffice")


class ClothingStore(Store):
    term = RdfTerm("http://schema.org/ClothingStore", "ClothingStore")


class OfficeEquipmentStore(Store):
    term = RdfTerm("http://schema.org/OfficeEquipmentStore", "OfficeEquipmentStore")


class ConvenienceStore(Store):
    term = RdfTerm("http://schema.org/ConvenienceStore", "ConvenienceStore")


class MusicStore(Store):
    term = RdfTerm("http://schema.org/MusicStore", "MusicStore")


class LiquorStore(Store):
    term = RdfTerm("http://schema.org/LiquorStore", "LiquorStore")


class Florist(Store):
    term = RdfTerm("http://schema.org/Florist", "Florist")


class ElectronicsStore(Store):
    term = RdfTerm("http://schema.org/ElectronicsStore", "ElectronicsStore")


class ToyStore(Store):
    term = RdfTerm("http://schema.org/ToyStore", "ToyStore")


class HobbyShop(Store):
    term = RdfTerm("http://schema.org/HobbyShop", "HobbyShop")


class HardwareStore(Store):
    term = RdfTerm("http://schema.org/HardwareStore", "HardwareStore")


class HomeGoodsStore(Store):
    term = RdfTerm("http://schema.org/HomeGoodsStore", "HomeGoodsStore")


class FurnitureStore(Store):
    term = RdfTerm("http://schema.org/FurnitureStore", "FurnitureStore")


class MovieRentalStore(Store):
    term = RdfTerm("http://schema.org/MovieRentalStore", "MovieRentalStore")


class GroceryStore(Store):
    term = RdfTerm("http://schema.org/GroceryStore", "GroceryStore")


class TireShop(Store):
    term = RdfTerm("http://schema.org/TireShop", "TireShop")


class MobilePhoneStore(Store):
    term = RdfTerm("http://schema.org/MobilePhoneStore", "MobilePhoneStore")


class BikeStore(Store):
    term = RdfTerm("http://schema.org/BikeStore", "BikeStore")


class PetStore(Store):
    term = RdfTerm("http://schema.org/PetStore", "PetStore")


class JewelryStore(Store):
    term = RdfTerm("http://schema.org/JewelryStore", "JewelryStore")


class ComputerStore(Store):
    term = RdfTerm("http://schema.org/ComputerStore", "ComputerStore")


class GardenStore(Store):
    term = RdfTerm("http://schema.org/GardenStore", "GardenStore")


class OutletStore(Store):
    term = RdfTerm("http://schema.org/OutletStore", "OutletStore")


class DepartmentStore(Store):
    term = RdfTerm("http://schema.org/DepartmentStore", "DepartmentStore")


class SportingGoodsStore(Store):
    term = RdfTerm("http://schema.org/SportingGoodsStore", "SportingGoodsStore")


class WholesaleStore(Store):
    term = RdfTerm("http://schema.org/WholesaleStore", "WholesaleStore")


class MensClothingStore(Store):
    term = RdfTerm("http://schema.org/MensClothingStore", "MensClothingStore")


class ShoeStore(Store):
    term = RdfTerm("http://schema.org/ShoeStore", "ShoeStore")


class PawnShop(Store):
    term = RdfTerm("http://schema.org/PawnShop", "PawnShop")


class BookStore(Store):
    term = RdfTerm("http://schema.org/BookStore", "BookStore")


class AutomatedTeller(FinancialService):
    term = RdfTerm("http://schema.org/AutomatedTeller", "AutomatedTeller")


class AccountingService(FinancialService):
    term = RdfTerm("http://schema.org/AccountingService", "AccountingService")


class InsuranceAgency(FinancialService):
    term = RdfTerm("http://schema.org/InsuranceAgency", "InsuranceAgency")


class BankOrCreditUnion(FinancialService):
    term = RdfTerm("http://schema.org/BankOrCreditUnion", "BankOrCreditUnion")


class FireStation(EmergencyService, CivicStructure):
    term = RdfTerm("http://schema.org/FireStation", "FireStation")


class PoliceStation(EmergencyService, CivicStructure):
    term = RdfTerm("http://schema.org/PoliceStation", "PoliceStation")


class Hospital(EmergencyService, MedicalOrganization, CivicStructure):
    term = RdfTerm("http://schema.org/Hospital", "Hospital")


class CafeOrCoffeeShop(FoodEstablishment):
    term = RdfTerm("http://schema.org/CafeOrCoffeeShop", "CafeOrCoffeeShop")


class IceCreamShop(FoodEstablishment):
    term = RdfTerm("http://schema.org/IceCreamShop", "IceCreamShop")


class Bakery(FoodEstablishment):
    term = RdfTerm("http://schema.org/Bakery", "Bakery")


class Winery(FoodEstablishment):
    term = RdfTerm("http://schema.org/Winery", "Winery")


class Restaurant(FoodEstablishment):
    term = RdfTerm("http://schema.org/Restaurant", "Restaurant")


class Brewery(FoodEstablishment):
    term = RdfTerm("http://schema.org/Brewery", "Brewery")


class Distillery(FoodEstablishment):
    term = RdfTerm("http://schema.org/Distillery", "Distillery")


class BarOrPub(FoodEstablishment):
    term = RdfTerm("http://schema.org/BarOrPub", "BarOrPub")


class FastFoodRestaurant(FoodEstablishment):
    term = RdfTerm("http://schema.org/FastFoodRestaurant", "FastFoodRestaurant")


class ComedyClub(EntertainmentBusiness):
    term = RdfTerm("http://schema.org/ComedyClub", "ComedyClub")


class MovieTheater(EntertainmentBusiness, CivicStructure):
    term = RdfTerm("http://schema.org/MovieTheater", "MovieTheater")


class Casino(EntertainmentBusiness):
    term = RdfTerm("http://schema.org/Casino", "Casino")


class NightClub(EntertainmentBusiness):
    term = RdfTerm("http://schema.org/NightClub", "NightClub")


class ArtGallery(EntertainmentBusiness):
    term = RdfTerm("http://schema.org/ArtGallery", "ArtGallery")


class AmusementPark(EntertainmentBusiness):
    term = RdfTerm("http://schema.org/AmusementPark", "AmusementPark")


class AdultEntertainment(EntertainmentBusiness):
    term = RdfTerm("http://schema.org/AdultEntertainment", "AdultEntertainment")


class Dentist(MedicalBusiness, LocalBusiness, MedicalOrganization):
    term = RdfTerm("http://schema.org/Dentist", "Dentist")


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    term = RdfTerm("http://schema.org/MedicalClinic", "MedicalClinic")


class Pharmacy(MedicalBusiness, MedicalOrganization):
    term = RdfTerm("http://schema.org/Pharmacy", "Pharmacy")


class Physician(MedicalBusiness, MedicalOrganization):
    term = RdfTerm("http://schema.org/Physician", "Physician")


class Podiatric(MedicalBusiness):
    term = RdfTerm("http://schema.org/Podiatric", "Podiatric")


class PublicHealth(MedicalBusiness):
    term = RdfTerm("http://schema.org/PublicHealth", "PublicHealth")


class Psychiatric(MedicalBusiness):
    term = RdfTerm("http://schema.org/Psychiatric", "Psychiatric")


class Obstetric(MedicalBusiness):
    term = RdfTerm("http://schema.org/Obstetric", "Obstetric")


class Otolaryngologic(MedicalBusiness):
    term = RdfTerm("http://schema.org/Otolaryngologic", "Otolaryngologic")


class Oncologic(MedicalBusiness):
    term = RdfTerm("http://schema.org/Oncologic", "Oncologic")


class PlasticSurgery(MedicalBusiness):
    term = RdfTerm("http://schema.org/PlasticSurgery", "PlasticSurgery")


class Optometric(MedicalBusiness):
    term = RdfTerm("http://schema.org/Optometric", "Optometric")


class Pediatric(MedicalBusiness):
    term = RdfTerm("http://schema.org/Pediatric", "Pediatric")


class Optician(MedicalBusiness):
    term = RdfTerm("http://schema.org/Optician", "Optician")


class Emergency(MedicalBusiness):
    term = RdfTerm("http://schema.org/Emergency", "Emergency")


class DietNutrition(MedicalBusiness):
    term = RdfTerm("http://schema.org/DietNutrition", "DietNutrition")


class PrimaryCare(MedicalBusiness):
    term = RdfTerm("http://schema.org/PrimaryCare", "PrimaryCare")


class Physiotherapy(MedicalBusiness):
    term = RdfTerm("http://schema.org/Physiotherapy", "Physiotherapy")


class CommunityHealth(MedicalBusiness):
    term = RdfTerm("http://schema.org/CommunityHealth", "CommunityHealth")


class Geriatric(MedicalBusiness):
    term = RdfTerm("http://schema.org/Geriatric", "Geriatric")


class Gynecologic(MedicalBusiness):
    term = RdfTerm("http://schema.org/Gynecologic", "Gynecologic")


class Dermatology(MedicalBusiness):
    term = RdfTerm("http://schema.org/Dermatology", "Dermatology")


class Midwifery(MedicalBusiness):
    term = RdfTerm("http://schema.org/Midwifery", "Midwifery")


class Nursing(MedicalBusiness):
    term = RdfTerm("http://schema.org/Nursing", "Nursing")


class HVACBusiness(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/HVACBusiness", "HVACBusiness")


class RoofingContractor(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/RoofingContractor", "RoofingContractor")


class Locksmith(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/Locksmith", "Locksmith")


class Electrician(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/Electrician", "Electrician")


class HousePainter(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/HousePainter", "HousePainter")


class GeneralContractor(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/GeneralContractor", "GeneralContractor")


class MovingCompany(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/MovingCompany", "MovingCompany")


class Plumber(HomeAndConstructionBusiness):
    term = RdfTerm("http://schema.org/Plumber", "Plumber")


class SportsClub(SportsActivityLocation):
    term = RdfTerm("http://schema.org/SportsClub", "SportsClub")


class GolfCourse(SportsActivityLocation):
    term = RdfTerm("http://schema.org/GolfCourse", "GolfCourse")


class BowlingAlley(SportsActivityLocation):
    term = RdfTerm("http://schema.org/BowlingAlley", "BowlingAlley")


class TennisComplex(SportsActivityLocation):
    term = RdfTerm("http://schema.org/TennisComplex", "TennisComplex")


class StadiumOrArena(SportsActivityLocation, CivicStructure):
    term = RdfTerm("http://schema.org/StadiumOrArena", "StadiumOrArena")


class ExerciseGym(SportsActivityLocation):
    term = RdfTerm("http://schema.org/ExerciseGym", "ExerciseGym")


class PublicSwimmingPool(SportsActivityLocation):
    term = RdfTerm("http://schema.org/PublicSwimmingPool", "PublicSwimmingPool")


class TattooParlor(HealthAndBeautyBusiness):
    term = RdfTerm("http://schema.org/TattooParlor", "TattooParlor")


class HairSalon(HealthAndBeautyBusiness):
    term = RdfTerm("http://schema.org/HairSalon", "HairSalon")


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    term = RdfTerm("http://schema.org/HealthClub", "HealthClub")


class NailSalon(HealthAndBeautyBusiness):
    term = RdfTerm("http://schema.org/NailSalon", "NailSalon")


class DaySpa(HealthAndBeautyBusiness):
    term = RdfTerm("http://schema.org/DaySpa", "DaySpa")


class BeautySalon(HealthAndBeautyBusiness):
    term = RdfTerm("http://schema.org/BeautySalon", "BeautySalon")


class Campground(LodgingBusiness, CivicStructure):
    term = RdfTerm("http://schema.org/Campground", "Campground")


class Hostel(LodgingBusiness):
    term = RdfTerm("http://schema.org/Hostel", "Hostel")


class Resort(LodgingBusiness):
    term = RdfTerm("http://schema.org/Resort", "Resort")


class Hotel(LodgingBusiness):
    term = RdfTerm("http://schema.org/Hotel", "Hotel")


class VacationRental(LodgingBusiness):
    term = RdfTerm("http://schema.org/VacationRental", "VacationRental")


class BedAndBreakfast(LodgingBusiness):
    term = RdfTerm("http://schema.org/BedAndBreakfast", "BedAndBreakfast")


class Motel(LodgingBusiness):
    term = RdfTerm("http://schema.org/Motel", "Motel")


class GasStation(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/GasStation", "GasStation")


class AutoPartsStore(AutomotiveBusiness, Store):
    term = RdfTerm("http://schema.org/AutoPartsStore", "AutoPartsStore")


class MotorcycleDealer(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/MotorcycleDealer", "MotorcycleDealer")


class AutoRental(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/AutoRental", "AutoRental")


class AutoWash(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/AutoWash", "AutoWash")


class AutoRepair(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/AutoRepair", "AutoRepair")


class AutoDealer(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/AutoDealer", "AutoDealer")


class MotorcycleRepair(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/MotorcycleRepair", "MotorcycleRepair")


class AutoBodyShop(AutomotiveBusiness):
    term = RdfTerm("http://schema.org/AutoBodyShop", "AutoBodyShop")


class Attorney(LegalService):
    term = RdfTerm("http://schema.org/Attorney", "Attorney")


class Notary(LegalService):
    term = RdfTerm("http://schema.org/Notary", "Notary")


class HighSchool(EducationalOrganization):
    term = RdfTerm("http://schema.org/HighSchool", "HighSchool")


class CollegeOrUniversity(EducationalOrganization):
    term = RdfTerm("http://schema.org/CollegeOrUniversity", "CollegeOrUniversity")


class Preschool(EducationalOrganization):
    term = RdfTerm("http://schema.org/Preschool", "Preschool")


class ElementarySchool(EducationalOrganization):
    term = RdfTerm("http://schema.org/ElementarySchool", "ElementarySchool")


class MiddleSchool(EducationalOrganization):
    term = RdfTerm("http://schema.org/MiddleSchool", "MiddleSchool")


class School(EducationalOrganization):
    term = RdfTerm("http://schema.org/School", "School")


class BuddhistTemple(PlaceOfWorship):
    term = RdfTerm("http://schema.org/BuddhistTemple", "BuddhistTemple")


class Synagogue(PlaceOfWorship):
    term = RdfTerm("http://schema.org/Synagogue", "Synagogue")


class Mosque(PlaceOfWorship):
    term = RdfTerm("http://schema.org/Mosque", "Mosque")


class Church(PlaceOfWorship):
    term = RdfTerm("http://schema.org/Church", "Church")


class HinduTemple(PlaceOfWorship):
    term = RdfTerm("http://schema.org/HinduTemple", "HinduTemple")


class DefenceEstablishment(GovernmentBuilding):
    term = RdfTerm("http://schema.org/DefenceEstablishment", "DefenceEstablishment")


class CityHall(GovernmentBuilding):
    term = RdfTerm("http://schema.org/CityHall", "CityHall")


class Courthouse(GovernmentBuilding):
    term = RdfTerm("http://schema.org/Courthouse", "Courthouse")


class Embassy(GovernmentBuilding):
    term = RdfTerm("http://schema.org/Embassy", "Embassy")


class LegislativeBuilding(GovernmentBuilding):
    term = RdfTerm("http://schema.org/LegislativeBuilding", "LegislativeBuilding")


class SeaBodyOfWater(BodyOfWater):
    term = RdfTerm("http://schema.org/SeaBodyOfWater", "SeaBodyOfWater")


class OceanBodyOfWater(BodyOfWater):
    term = RdfTerm("http://schema.org/OceanBodyOfWater", "OceanBodyOfWater")


class Waterfall(BodyOfWater):
    term = RdfTerm("http://schema.org/Waterfall", "Waterfall")


class Pond(BodyOfWater):
    term = RdfTerm("http://schema.org/Pond", "Pond")


class LakeBodyOfWater(BodyOfWater):
    term = RdfTerm("http://schema.org/LakeBodyOfWater", "LakeBodyOfWater")


class Reservoir(BodyOfWater):
    term = RdfTerm("http://schema.org/Reservoir", "Reservoir")


class RiverBodyOfWater(BodyOfWater):
    term = RdfTerm("http://schema.org/RiverBodyOfWater", "RiverBodyOfWater")


class Canal(BodyOfWater):
    term = RdfTerm("http://schema.org/Canal", "Canal")


class ExercisePlan(PhysicalActivity, CreativeWork):
    term = RdfTerm("http://schema.org/ExercisePlan", "ExercisePlan")


class ReportedDoseSchedule(DoseSchedule):
    term = RdfTerm("http://schema.org/ReportedDoseSchedule", "ReportedDoseSchedule")


class MaximumDoseSchedule(DoseSchedule):
    term = RdfTerm("http://schema.org/MaximumDoseSchedule", "MaximumDoseSchedule")


class RecommendedDoseSchedule(DoseSchedule):
    term = RdfTerm(
        "http://schema.org/RecommendedDoseSchedule", "RecommendedDoseSchedule"
    )


class MedicalTherapy(TherapeuticProcedure):
    term = RdfTerm("http://schema.org/MedicalTherapy", "MedicalTherapy")


class PsychologicalTreatment(TherapeuticProcedure):
    term = RdfTerm("http://schema.org/PsychologicalTreatment", "PsychologicalTreatment")


class LymphaticVessel(Vessel):
    term = RdfTerm("http://schema.org/LymphaticVessel", "LymphaticVessel")


class Artery(Vessel):
    term = RdfTerm("http://schema.org/Artery", "Artery")


class Vein(Vessel):
    term = RdfTerm("http://schema.org/Vein", "Vein")


class MedicalSymptom(MedicalSignOrSymptom):
    term = RdfTerm("http://schema.org/MedicalSymptom", "MedicalSymptom")


class MedicalSign(MedicalSignOrSymptom):
    term = RdfTerm("http://schema.org/MedicalSign", "MedicalSign")


class APIReference(TechArticle):
    term = RdfTerm("http://schema.org/APIReference", "APIReference")


class AnalysisNewsArticle(NewsArticle):
    term = RdfTerm("http://schema.org/AnalysisNewsArticle", "AnalysisNewsArticle")


class BackgroundNewsArticle(NewsArticle):
    term = RdfTerm("http://schema.org/BackgroundNewsArticle", "BackgroundNewsArticle")


class AskPublicNewsArticle(NewsArticle):
    term = RdfTerm("http://schema.org/AskPublicNewsArticle", "AskPublicNewsArticle")


class ReportageNewsArticle(NewsArticle):
    term = RdfTerm("http://schema.org/ReportageNewsArticle", "ReportageNewsArticle")


class OpinionNewsArticle(NewsArticle):
    term = RdfTerm("http://schema.org/OpinionNewsArticle", "OpinionNewsArticle")


class DiscussionForumPosting(SocialMediaPosting):
    term = RdfTerm("http://schema.org/DiscussionForumPosting", "DiscussionForumPosting")


class BlogPosting(SocialMediaPosting):
    term = RdfTerm("http://schema.org/BlogPosting", "BlogPosting")


class MedicalScholarlyArticle(ScholarlyArticle):
    term = RdfTerm(
        "http://schema.org/MedicalScholarlyArticle", "MedicalScholarlyArticle"
    )


class ReviewNewsArticle(NewsArticle, CriticReview):
    term = RdfTerm("http://schema.org/ReviewNewsArticle", "ReviewNewsArticle")


class VideoObjectSnapshot(VideoObject):
    term = RdfTerm("http://schema.org/VideoObjectSnapshot", "VideoObjectSnapshot")


class Audiobook(AudioObject, Book):
    term = RdfTerm("http://schema.org/Audiobook", "Audiobook")


class AudioObjectSnapshot(AudioObject):
    term = RdfTerm("http://schema.org/AudioObjectSnapshot", "AudioObjectSnapshot")


class ImageObjectSnapshot(ImageObject):
    term = RdfTerm("http://schema.org/ImageObjectSnapshot", "ImageObjectSnapshot")


class Barcode(ImageObject):
    term = RdfTerm("http://schema.org/Barcode", "Barcode")


class CompleteDataFeed(DataFeed):
    term = RdfTerm("http://schema.org/CompleteDataFeed", "CompleteDataFeed")


class ComicCoverArt(CoverArt, ComicStory):
    term = RdfTerm("http://schema.org/ComicCoverArt", "ComicCoverArt")


class MediaGallery(CollectionPage):
    term = RdfTerm("http://schema.org/MediaGallery", "MediaGallery")


class ConfirmAction(InformAction):
    term = RdfTerm("http://schema.org/ConfirmAction", "ConfirmAction")


class RsvpAction(InformAction):
    term = RdfTerm("http://schema.org/RsvpAction", "RsvpAction")


class AppendAction(InsertAction):
    term = RdfTerm("http://schema.org/AppendAction", "AppendAction")


class PrependAction(InsertAction):
    term = RdfTerm("http://schema.org/PrependAction", "PrependAction")


class MortgageLoan(LoanOrCredit):
    term = RdfTerm("http://schema.org/MortgageLoan", "MortgageLoan")


class CreditCard(PaymentCard, LoanOrCredit):
    term = RdfTerm("http://schema.org/CreditCard", "CreditCard")


class DepositAccount(BankAccount, InvestmentOrDeposit):
    term = RdfTerm("http://schema.org/DepositAccount", "DepositAccount")


class BrokerageAccount(InvestmentOrDeposit):
    term = RdfTerm("http://schema.org/BrokerageAccount", "BrokerageAccount")


class InvestmentFund(InvestmentOrDeposit):
    term = RdfTerm("http://schema.org/InvestmentFund", "InvestmentFund")


class ComicSeries(Periodical):
    term = RdfTerm("http://schema.org/ComicSeries", "ComicSeries")


class Newspaper(Periodical):
    term = RdfTerm("http://schema.org/Newspaper", "Newspaper")


class Patient(MedicalAudience, Person):
    term = RdfTerm("http://schema.org/Patient", "Patient")


class CovidTestingFacility(MedicalClinic):
    term = RdfTerm("http://schema.org/CovidTestingFacility", "CovidTestingFacility")


class IndividualPhysician(Physician):
    term = RdfTerm("http://schema.org/IndividualPhysician", "IndividualPhysician")


class PhysiciansOffice(Physician):
    term = RdfTerm("http://schema.org/PhysiciansOffice", "PhysiciansOffice")


class SkiResort(Resort, SportsActivityLocation):
    term = RdfTerm("http://schema.org/SkiResort", "SkiResort")


class CatholicChurch(Church):
    term = RdfTerm("http://schema.org/CatholicChurch", "CatholicChurch")


class OccupationalTherapy(MedicalTherapy):
    term = RdfTerm("http://schema.org/OccupationalTherapy", "OccupationalTherapy")


class RespiratoryTherapy(MedicalTherapy):
    term = RdfTerm("http://schema.org/RespiratoryTherapy", "RespiratoryTherapy")


class PhysicalTherapy(MedicalTherapy):
    term = RdfTerm("http://schema.org/PhysicalTherapy", "PhysicalTherapy")


class RadiationTherapy(MedicalTherapy):
    term = RdfTerm("http://schema.org/RadiationTherapy", "RadiationTherapy")


class PalliativeProcedure(MedicalTherapy, MedicalProcedure):
    term = RdfTerm("http://schema.org/PalliativeProcedure", "PalliativeProcedure")


class VitalSign(MedicalSign):
    term = RdfTerm("http://schema.org/VitalSign", "VitalSign")


class LiveBlogPosting(BlogPosting):
    term = RdfTerm("http://schema.org/LiveBlogPosting", "LiveBlogPosting")


class VideoGallery(MediaGallery):
    term = RdfTerm("http://schema.org/VideoGallery", "VideoGallery")


class ImageGallery(MediaGallery):
    term = RdfTerm("http://schema.org/ImageGallery", "ImageGallery")


class repeatCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/repeatCount", "repeatCount")


class executableLibraryName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/executableLibraryName", "executableLibraryName")


class inChIKey(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/inChIKey", "inChIKey")


class opens(RdfProperty[schemaorg.Time]):
    term = RdfTerm("http://schema.org/opens", "opens")


class healthPlanNetworkId(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/healthPlanNetworkId", "healthPlanNetworkId")


class jobTitle(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/jobTitle", "jobTitle")


class hasPart(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/hasPart", "hasPart")


class totalTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/totalTime", "totalTime")


class preOp(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/preOp", "preOp")


class billingIncrement(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/billingIncrement", "billingIncrement")


class byMonthDay(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/byMonthDay", "byMonthDay")


class broadcastAffiliateOf(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/broadcastAffiliateOf", "broadcastAffiliateOf")


class permittedUsage(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/permittedUsage", "permittedUsage")


class printColumn(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/printColumn", "printColumn")


class color(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/color", "color")


class member(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/member", "member")


class paymentMethodId(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/paymentMethodId", "paymentMethodId")


class beforeMedia(RdfProperty[schemaorg.MediaObject | schemaorg.URL]):
    term = RdfTerm("http://schema.org/beforeMedia", "beforeMedia")


class expectedArrivalUntil(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/expectedArrivalUntil", "expectedArrivalUntil")


class nerve(RdfProperty[schemaorg.Nerve]):
    term = RdfTerm("http://schema.org/nerve", "nerve")


class award(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/award", "award")


class availableFrom(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/availableFrom", "availableFrom")


class superEvent(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/superEvent", "superEvent")


class contactlessPayment(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/contactlessPayment", "contactlessPayment")


class experienceRequirements(
    RdfProperty[schemaorg.OccupationalExperienceRequirements | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/experienceRequirements", "experienceRequirements")


class catalogNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/catalogNumber", "catalogNumber")


class game(RdfProperty[schemaorg.VideoGame]):
    term = RdfTerm("http://schema.org/game", "game")


class floorLimit(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/floorLimit", "floorLimit")


class menu(RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.Menu]):
    term = RdfTerm("http://schema.org/menu", "menu")


class warranty(RdfProperty[schemaorg.WarrantyPromise]):
    term = RdfTerm("http://schema.org/warranty", "warranty")


class isicV4(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/isicV4", "isicV4")


class musicGroupMember(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/musicGroupMember", "musicGroupMember")


class usedToDiagnose(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm("http://schema.org/usedToDiagnose", "usedToDiagnose")


class cvdCollectionDate(RdfProperty[schemaorg.Text | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/cvdCollectionDate", "cvdCollectionDate")


class identifyingTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm("http://schema.org/identifyingTest", "identifyingTest")


class amountOfThisGood(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/amountOfThisGood", "amountOfThisGood")


class variablesMeasured(RdfProperty[schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/variablesMeasured", "variablesMeasured")


class agentInteractionStatistic(RdfProperty[schemaorg.InteractionCounter]):
    term = RdfTerm(
        "http://schema.org/agentInteractionStatistic", "agentInteractionStatistic"
    )


class highPrice(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/highPrice", "highPrice")


class entertainmentBusiness(RdfProperty[schemaorg.EntertainmentBusiness]):
    term = RdfTerm("http://schema.org/entertainmentBusiness", "entertainmentBusiness")


class accessModeSufficient(RdfProperty[schemaorg.ItemList]):
    term = RdfTerm("http://schema.org/accessModeSufficient", "accessModeSufficient")


class floorLevel(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/floorLevel", "floorLevel")


class gtin8(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/gtin8", "gtin8")


class isRelatedTo(RdfProperty[schemaorg.Service | schemaorg.Product]):
    term = RdfTerm("http://schema.org/isRelatedTo", "isRelatedTo")


class arrivalStation(RdfProperty[schemaorg.TrainStation]):
    term = RdfTerm("http://schema.org/arrivalStation", "arrivalStation")


class deliveryTime(RdfProperty[schemaorg.ShippingDeliveryTime]):
    term = RdfTerm("http://schema.org/deliveryTime", "deliveryTime")


class itemLocation(
    RdfProperty[schemaorg.PostalAddress | schemaorg.Place | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/itemLocation", "itemLocation")


class jobImmediateStart(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/jobImmediateStart", "jobImmediateStart")


class isAcceptingNewPatients(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isAcceptingNewPatients", "isAcceptingNewPatients")


class fuelType(
    RdfProperty[schemaorg.QualitativeValue | schemaorg.URL | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/fuelType", "fuelType")


class molecularWeight(RdfProperty[schemaorg.Text | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/molecularWeight", "molecularWeight")


class marginOfError(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/marginOfError", "marginOfError")


class artist(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/artist", "artist")


class numberedPosition(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberedPosition", "numberedPosition")


class incentivizedItem(RdfProperty[schemaorg.Product | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/incentivizedItem", "incentivizedItem")


class performers(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/performers", "performers")


class bookEdition(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/bookEdition", "bookEdition")


class asin(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/asin", "asin")


class image(RdfProperty[schemaorg.ImageObject | schemaorg.URL]):
    term = RdfTerm("http://schema.org/image", "image")


class termDuration(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/termDuration", "termDuration")


class isProprietary(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isProprietary", "isProprietary")


class branchCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/branchCode", "branchCode")


class screenshot(RdfProperty[schemaorg.URL | schemaorg.ImageObject]):
    term = RdfTerm("http://schema.org/screenshot", "screenshot")


class itemDefectReturnShippingFeesAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm(
        "http://schema.org/itemDefectReturnShippingFeesAmount",
        "itemDefectReturnShippingFeesAmount",
    )


class isrcCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/isrcCode", "isrcCode")


class activityFrequency(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/activityFrequency", "activityFrequency")


class hasVariant(RdfProperty[schemaorg.Product]):
    term = RdfTerm("http://schema.org/hasVariant", "hasVariant")


class downloadUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/downloadUrl", "downloadUrl")


class coach(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/coach", "coach")


class holdingArchive(RdfProperty[schemaorg.ArchiveOrganization]):
    term = RdfTerm("http://schema.org/holdingArchive", "holdingArchive")


class serviceOutput(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/serviceOutput", "serviceOutput")


class subEvent(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/subEvent", "subEvent")


class lodgingUnitType(RdfProperty[schemaorg.QualitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/lodgingUnitType", "lodgingUnitType")


class purchasePriceLimit(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/purchasePriceLimit", "purchasePriceLimit")


class step(
    RdfProperty[
        schemaorg.CreativeWork
        | schemaorg.Text
        | schemaorg.HowToSection
        | schemaorg.HowToStep
    ]
):
    term = RdfTerm("http://schema.org/step", "step")


class serviceArea(
    RdfProperty[schemaorg.Place | schemaorg.AdministrativeArea | schemaorg.GeoShape]
):
    term = RdfTerm("http://schema.org/serviceArea", "serviceArea")


class alumni(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/alumni", "alumni")


class yearBuilt(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/yearBuilt", "yearBuilt")


class diversityPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/diversityPolicy", "diversityPolicy")


class relatedAnatomy(
    RdfProperty[schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem]
):
    term = RdfTerm("http://schema.org/relatedAnatomy", "relatedAnatomy")


class musicCompositionForm(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/musicCompositionForm", "musicCompositionForm")


class taxonomicRange(
    RdfProperty[
        schemaorg.Taxon | schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm
    ]
):
    term = RdfTerm("http://schema.org/taxonomicRange", "taxonomicRange")


class replacee(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/replacee", "replacee")


class responsibilities(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/responsibilities", "responsibilities")


class flightNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/flightNumber", "flightNumber")


class parentItem(RdfProperty[schemaorg.Comment | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/parentItem", "parentItem")


class medicalAudience(
    RdfProperty[schemaorg.MedicalAudienceType | schemaorg.MedicalAudience]
):
    term = RdfTerm("http://schema.org/medicalAudience", "medicalAudience")


class codingSystem(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/codingSystem", "codingSystem")


class accommodationFloorPlan(RdfProperty[schemaorg.FloorPlan]):
    term = RdfTerm("http://schema.org/accommodationFloorPlan", "accommodationFloorPlan")


class realEstateAgent(RdfProperty[schemaorg.RealEstateAgent]):
    term = RdfTerm("http://schema.org/realEstateAgent", "realEstateAgent")


class reviews(RdfProperty[schemaorg.Review]):
    term = RdfTerm("http://schema.org/reviews", "reviews")


class appearance(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/appearance", "appearance")


class jobStartDate(RdfProperty[schemaorg.Date | schemaorg.Text]):
    term = RdfTerm("http://schema.org/jobStartDate", "jobStartDate")


class area(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/area", "area")


class scheduledTime(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/scheduledTime", "scheduledTime")


class eventStatus(RdfProperty[schemaorg.EventStatusType]):
    term = RdfTerm("http://schema.org/eventStatus", "eventStatus")


class startTime(RdfProperty[schemaorg.DateTime | schemaorg.Time]):
    term = RdfTerm("http://schema.org/startTime", "startTime")


class numberOfCredits(RdfProperty[schemaorg.StructuredValue | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numberOfCredits", "numberOfCredits")


class saturatedFatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/saturatedFatContent", "saturatedFatContent")


class linkRelationship(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/linkRelationship", "linkRelationship")


class taxonRank(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/taxonRank", "taxonRank")


class primaryPrevention(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm("http://schema.org/primaryPrevention", "primaryPrevention")


class duns(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/duns", "duns")


class numberOfFullBathrooms(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfFullBathrooms", "numberOfFullBathrooms")


class postalCodeEnd(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/postalCodeEnd", "postalCodeEnd")


class legislationResponsible(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/legislationResponsible", "legislationResponsible")


class beneficiaryBank(RdfProperty[schemaorg.Text | schemaorg.BankOrCreditUnion]):
    term = RdfTerm("http://schema.org/beneficiaryBank", "beneficiaryBank")


class colleague(RdfProperty[schemaorg.Person | schemaorg.URL]):
    term = RdfTerm("http://schema.org/colleague", "colleague")


class targetProduct(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm("http://schema.org/targetProduct", "targetProduct")


class longitude(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/longitude", "longitude")


class issuedBy(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/issuedBy", "issuedBy")


class loser(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/loser", "loser")


class geoTouches(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm("http://schema.org/geoTouches", "geoTouches")


class minimumPaymentDue(
    RdfProperty[schemaorg.PriceSpecification | schemaorg.MonetaryAmount]
):
    term = RdfTerm("http://schema.org/minimumPaymentDue", "minimumPaymentDue")


class subStructure(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/subStructure", "subStructure")


class maximumPhysicalAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm(
        "http://schema.org/maximumPhysicalAttendeeCapacity",
        "maximumPhysicalAttendeeCapacity",
    )


class unsaturatedFatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/unsaturatedFatContent", "unsaturatedFatContent")


class fuelConsumption(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/fuelConsumption", "fuelConsumption")


class tool(RdfProperty[schemaorg.HowToTool | schemaorg.Text]):
    term = RdfTerm("http://schema.org/tool", "tool")


class mealService(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/mealService", "mealService")


class postOfficeBoxNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/postOfficeBoxNumber", "postOfficeBoxNumber")


class hasBioChemEntityPart(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm("http://schema.org/hasBioChemEntityPart", "hasBioChemEntityPart")


class measuredProperty(RdfProperty[schemaorg.Property]):
    term = RdfTerm("http://schema.org/measuredProperty", "measuredProperty")


class billingAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm("http://schema.org/billingAddress", "billingAddress")


class workFeatured(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/workFeatured", "workFeatured")


class percentile25(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/percentile25", "percentile25")


class eligibleRegion(
    RdfProperty[schemaorg.Place | schemaorg.GeoShape | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/eligibleRegion", "eligibleRegion")


class hasEnergyConsumptionDetails(RdfProperty[schemaorg.EnergyConsumptionDetails]):
    term = RdfTerm(
        "http://schema.org/hasEnergyConsumptionDetails", "hasEnergyConsumptionDetails"
    )


class currency(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/currency", "currency")


class activeIngredient(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/activeIngredient", "activeIngredient")


class closes(RdfProperty[schemaorg.Time]):
    term = RdfTerm("http://schema.org/closes", "closes")


class mileageFromOdometer(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/mileageFromOdometer", "mileageFromOdometer")


class valueMaxLength(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/valueMaxLength", "valueMaxLength")


class answerCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/answerCount", "answerCount")


class bitrate(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/bitrate", "bitrate")


class operatingSystem(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/operatingSystem", "operatingSystem")


class numConstraints(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numConstraints", "numConstraints")


class option(RdfProperty[schemaorg.Text | schemaorg.Thing]):
    term = RdfTerm("http://schema.org/option", "option")


class tickerSymbol(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/tickerSymbol", "tickerSymbol")


class mainContentOfPage(RdfProperty[schemaorg.WebPageElement]):
    term = RdfTerm("http://schema.org/mainContentOfPage", "mainContentOfPage")


class estimatedFlightDuration(RdfProperty[schemaorg.Text | schemaorg.Duration]):
    term = RdfTerm(
        "http://schema.org/estimatedFlightDuration", "estimatedFlightDuration"
    )


class episodes(RdfProperty[schemaorg.Episode]):
    term = RdfTerm("http://schema.org/episodes", "episodes")


class eligibleTransactionVolume(RdfProperty[schemaorg.PriceSpecification]):
    term = RdfTerm(
        "http://schema.org/eligibleTransactionVolume", "eligibleTransactionVolume"
    )


class providesService(RdfProperty[schemaorg.Service]):
    term = RdfTerm("http://schema.org/providesService", "providesService")


class shippingRate(
    RdfProperty[schemaorg.ShippingRateSettings | schemaorg.MonetaryAmount]
):
    term = RdfTerm("http://schema.org/shippingRate", "shippingRate")


class utterances(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/utterances", "utterances")


class priceType(RdfProperty[schemaorg.PriceTypeEnumeration | schemaorg.Text]):
    term = RdfTerm("http://schema.org/priceType", "priceType")


class applicationStartDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/applicationStartDate", "applicationStartDate")


class remainingAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm(
        "http://schema.org/remainingAttendeeCapacity", "remainingAttendeeCapacity"
    )


class pregnancyWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/pregnancyWarning", "pregnancyWarning")


class scheduledPaymentDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/scheduledPaymentDate", "scheduledPaymentDate")


class suggestedAnswer(RdfProperty[schemaorg.ItemList | schemaorg.Answer]):
    term = RdfTerm("http://schema.org/suggestedAnswer", "suggestedAnswer")


class confirmationNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/confirmationNumber", "confirmationNumber")


class isLiveBroadcast(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isLiveBroadcast", "isLiveBroadcast")


class biomechnicalClass(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/biomechnicalClass", "biomechnicalClass")


class manufacturer(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/manufacturer", "manufacturer")


class dateModified(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/dateModified", "dateModified")


class signOrSymptom(RdfProperty[schemaorg.MedicalSignOrSymptom]):
    term = RdfTerm("http://schema.org/signOrSymptom", "signOrSymptom")


class associatedDisease(
    RdfProperty[schemaorg.URL | schemaorg.PropertyValue | schemaorg.MedicalCondition]
):
    term = RdfTerm("http://schema.org/associatedDisease", "associatedDisease")


class diagnosis(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm("http://schema.org/diagnosis", "diagnosis")


class offers(RdfProperty[schemaorg.Demand | schemaorg.Offer]):
    term = RdfTerm("http://schema.org/offers", "offers")


class contentLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/contentLocation", "contentLocation")


class travelBans(RdfProperty[schemaorg.WebContent | schemaorg.URL]):
    term = RdfTerm("http://schema.org/travelBans", "travelBans")


class review(RdfProperty[schemaorg.Review]):
    term = RdfTerm("http://schema.org/review", "review")


class playersOnline(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/playersOnline", "playersOnline")


class members(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/members", "members")


class additionalName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/additionalName", "additionalName")


class legislationCommences(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm("http://schema.org/legislationCommences", "legislationCommences")


class associatedPathophysiology(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/associatedPathophysiology", "associatedPathophysiology"
    )


class relevantSpecialty(RdfProperty[schemaorg.MedicalSpecialty]):
    term = RdfTerm("http://schema.org/relevantSpecialty", "relevantSpecialty")


class exercisePlan(RdfProperty[schemaorg.ExercisePlan]):
    term = RdfTerm("http://schema.org/exercisePlan", "exercisePlan")


class availability(RdfProperty[schemaorg.ItemAvailability]):
    term = RdfTerm("http://schema.org/availability", "availability")


class departureBoatTerminal(RdfProperty[schemaorg.BoatTerminal]):
    term = RdfTerm("http://schema.org/departureBoatTerminal", "departureBoatTerminal")


class geoCrosses(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm("http://schema.org/geoCrosses", "geoCrosses")


class loanPaymentFrequency(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/loanPaymentFrequency", "loanPaymentFrequency")


class additionalVariable(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/additionalVariable", "additionalVariable")


class attendee(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/attendee", "attendee")


class legislationDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/legislationDate", "legislationDate")


class incentiveStatus(RdfProperty[schemaorg.IncentiveStatus]):
    term = RdfTerm("http://schema.org/incentiveStatus", "incentiveStatus")


class instructor(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/instructor", "instructor")


class url(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/url", "url")


class contentRating(RdfProperty[schemaorg.Rating | schemaorg.Text]):
    term = RdfTerm("http://schema.org/contentRating", "contentRating")


class applicableCountry(RdfProperty[schemaorg.Text | schemaorg.Country]):
    term = RdfTerm("http://schema.org/applicableCountry", "applicableCountry")


class titleEIDR(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/titleEIDR", "titleEIDR")


class lyricist(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/lyricist", "lyricist")


class accessibilityControl(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accessibilityControl", "accessibilityControl")


class lowPrice(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/lowPrice", "lowPrice")


class status(
    RdfProperty[
        schemaorg.MedicalStudyStatus | schemaorg.Text | schemaorg.EventStatusType
    ]
):
    term = RdfTerm("http://schema.org/status", "status")


class educationalRole(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/educationalRole", "educationalRole")


class checkoutPageURLTemplate(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/checkoutPageURLTemplate", "checkoutPageURLTemplate"
    )


class penciler(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/penciler", "penciler")


class releasedEvent(RdfProperty[schemaorg.PublicationEvent]):
    term = RdfTerm("http://schema.org/releasedEvent", "releasedEvent")


class pageStart(RdfProperty[schemaorg.Text | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/pageStart", "pageStart")


class email(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/email", "email")


class aggregateElement(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/aggregateElement", "aggregateElement")


class subTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm("http://schema.org/subTest", "subTest")


class returnPolicyCountry(RdfProperty[schemaorg.Text | schemaorg.Country]):
    term = RdfTerm("http://schema.org/returnPolicyCountry", "returnPolicyCountry")


class contributor(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/contributor", "contributor")


class textValue(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/textValue", "textValue")


class cvdNumVent(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumVent", "cvdNumVent")


class paymentMethod(RdfProperty[schemaorg.Text | schemaorg.PaymentMethod]):
    term = RdfTerm("http://schema.org/paymentMethod", "paymentMethod")


class businessFunction(RdfProperty[schemaorg.BusinessFunction]):
    term = RdfTerm("http://schema.org/businessFunction", "businessFunction")


class requirements(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/requirements", "requirements")


class educationalAlignment(RdfProperty[schemaorg.AlignmentObject]):
    term = RdfTerm("http://schema.org/educationalAlignment", "educationalAlignment")


class countryOfAssembly(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/countryOfAssembly", "countryOfAssembly")


class webCheckinTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/webCheckinTime", "webCheckinTime")


class readonlyValue(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/readonlyValue", "readonlyValue")


class polygon(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/polygon", "polygon")


class naturalProgression(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/naturalProgression", "naturalProgression")


class isbn(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/isbn", "isbn")


class duration(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Duration]):
    term = RdfTerm("http://schema.org/duration", "duration")


class printSection(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/printSection", "printSection")


class translator(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/translator", "translator")


class datePosted(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/datePosted", "datePosted")


class hasProductReturnPolicy(RdfProperty[schemaorg.ProductReturnPolicy]):
    term = RdfTerm("http://schema.org/hasProductReturnPolicy", "hasProductReturnPolicy")


class encodesCreativeWork(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/encodesCreativeWork", "encodesCreativeWork")


class inventoryLevel(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/inventoryLevel", "inventoryLevel")


class contentUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/contentUrl", "contentUrl")


class foodWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/foodWarning", "foodWarning")


class performer(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/performer", "performer")


class mobileUrl(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/mobileUrl", "mobileUrl")


class hasTierBenefit(RdfProperty[schemaorg.TierBenefitEnumeration]):
    term = RdfTerm("http://schema.org/hasTierBenefit", "hasTierBenefit")


class smiles(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/smiles", "smiles")


class offersPrescriptionByMail(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm(
        "http://schema.org/offersPrescriptionByMail", "offersPrescriptionByMail"
    )


class countryOfLastProcessing(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/countryOfLastProcessing", "countryOfLastProcessing"
    )


class cheatCode(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/cheatCode", "cheatCode")


class maximumAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm(
        "http://schema.org/maximumAttendeeCapacity", "maximumAttendeeCapacity"
    )


class dateReceived(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/dateReceived", "dateReceived")


class downPayment(RdfProperty[schemaorg.Number | schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/downPayment", "downPayment")


class archiveHeld(RdfProperty[schemaorg.ArchiveComponent]):
    term = RdfTerm("http://schema.org/archiveHeld", "archiveHeld")


class vehicleInteriorType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/vehicleInteriorType", "vehicleInteriorType")


class encodesBioChemEntity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm("http://schema.org/encodesBioChemEntity", "encodesBioChemEntity")


class normalRange(RdfProperty[schemaorg.Text | schemaorg.MedicalEnumeration]):
    term = RdfTerm("http://schema.org/normalRange", "normalRange")


class broadcastTimezone(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/broadcastTimezone", "broadcastTimezone")


class trailer(RdfProperty[schemaorg.VideoObject]):
    term = RdfTerm("http://schema.org/trailer", "trailer")


class about(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/about", "about")


class recognizedBy(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/recognizedBy", "recognizedBy")


class fuelEfficiency(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/fuelEfficiency", "fuelEfficiency")


class relatedDrug(RdfProperty[schemaorg.Drug]):
    term = RdfTerm("http://schema.org/relatedDrug", "relatedDrug")


class valueRequired(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/valueRequired", "valueRequired")


class softwareHelp(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/softwareHelp", "softwareHelp")


class xpath(RdfProperty[schemaorg.XPathType]):
    term = RdfTerm("http://schema.org/xpath", "xpath")


class addOn(RdfProperty[schemaorg.Offer]):
    term = RdfTerm("http://schema.org/addOn", "addOn")


class streetAddress(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/streetAddress", "streetAddress")


class auditDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/auditDate", "auditDate")


class deliveryStatus(RdfProperty[schemaorg.DeliveryEvent]):
    term = RdfTerm("http://schema.org/deliveryStatus", "deliveryStatus")


class contactType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/contactType", "contactType")


class copyrightNotice(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/copyrightNotice", "copyrightNotice")


class musicArrangement(RdfProperty[schemaorg.MusicComposition]):
    term = RdfTerm("http://schema.org/musicArrangement", "musicArrangement")


class parents(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/parents", "parents")


class aspect(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/aspect", "aspect")


class currenciesAccepted(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/currenciesAccepted", "currenciesAccepted")


class tripOrigin(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/tripOrigin", "tripOrigin")


class characterName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/characterName", "characterName")


class advanceBookingRequirement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm(
        "http://schema.org/advanceBookingRequirement", "advanceBookingRequirement"
    )


class artEdition(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm("http://schema.org/artEdition", "artEdition")


class serverStatus(RdfProperty[schemaorg.GameServerStatus]):
    term = RdfTerm("http://schema.org/serverStatus", "serverStatus")


class collectionSize(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/collectionSize", "collectionSize")


class coverageEndTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/coverageEndTime", "coverageEndTime")


class supersededBy(
    RdfProperty[schemaorg.Enumeration | schemaorg.Class | schemaorg.Property]
):
    term = RdfTerm("http://schema.org/supersededBy", "supersededBy")


class stage(RdfProperty[schemaorg.MedicalConditionStage]):
    term = RdfTerm("http://schema.org/stage", "stage")


class typicalAgeRange(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/typicalAgeRange", "typicalAgeRange")


class eduQuestionType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/eduQuestionType", "eduQuestionType")


class numberOfLoanPayments(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfLoanPayments", "numberOfLoanPayments")


class includedInDataCatalog(RdfProperty[schemaorg.DataCatalog]):
    term = RdfTerm("http://schema.org/includedInDataCatalog", "includedInDataCatalog")


class parent(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/parent", "parent")


class distinguishingSign(RdfProperty[schemaorg.MedicalSignOrSymptom]):
    term = RdfTerm("http://schema.org/distinguishingSign", "distinguishingSign")


class contactOption(RdfProperty[schemaorg.ContactPointOption]):
    term = RdfTerm("http://schema.org/contactOption", "contactOption")


class educationalCredentialAwarded(
    RdfProperty[
        schemaorg.EducationalOccupationalCredential | schemaorg.Text | schemaorg.URL
    ]
):
    term = RdfTerm(
        "http://schema.org/educationalCredentialAwarded", "educationalCredentialAwarded"
    )


class nonEqual(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm("http://schema.org/nonEqual", "nonEqual")


class gender(RdfProperty[schemaorg.GenderType | schemaorg.Text]):
    term = RdfTerm("http://schema.org/gender", "gender")


class pickupLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/pickupLocation", "pickupLocation")


class unitText(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/unitText", "unitText")


class riskFactor(RdfProperty[schemaorg.MedicalRiskFactor]):
    term = RdfTerm("http://schema.org/riskFactor", "riskFactor")


class actor(RdfProperty[schemaorg.PerformingGroup | schemaorg.Person]):
    term = RdfTerm("http://schema.org/actor", "actor")


class season(RdfProperty[schemaorg.CreativeWorkSeason | schemaorg.URL]):
    term = RdfTerm("http://schema.org/season", "season")


class keywords(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/keywords", "keywords")


class founders(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/founders", "founders")


class trackingNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/trackingNumber", "trackingNumber")


class recipeCuisine(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/recipeCuisine", "recipeCuisine")


class caption(RdfProperty[schemaorg.MediaObject | schemaorg.Text]):
    term = RdfTerm("http://schema.org/caption", "caption")


class publishingPrinciples(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/publishingPrinciples", "publishingPrinciples")


class statType(RdfProperty[schemaorg.Text | schemaorg.Property | schemaorg.URL]):
    term = RdfTerm("http://schema.org/statType", "statType")


class boardingPolicy(RdfProperty[schemaorg.BoardingPolicyType]):
    term = RdfTerm("http://schema.org/boardingPolicy", "boardingPolicy")


class discusses(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/discusses", "discusses")


class ticketToken(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/ticketToken", "ticketToken")


class permissions(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/permissions", "permissions")


class occupancy(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/occupancy", "occupancy")


class ticketNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/ticketNumber", "ticketNumber")


class trialDesign(RdfProperty[schemaorg.MedicalTrialDesign]):
    term = RdfTerm("http://schema.org/trialDesign", "trialDesign")


class performTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/performTime", "performTime")


class shippingDestination(RdfProperty[schemaorg.DefinedRegion]):
    term = RdfTerm("http://schema.org/shippingDestination", "shippingDestination")


class authenticator(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/authenticator", "authenticator")


class orderItemNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/orderItemNumber", "orderItemNumber")


class blogPost(RdfProperty[schemaorg.BlogPosting]):
    term = RdfTerm("http://schema.org/blogPost", "blogPost")


class diagram(RdfProperty[schemaorg.ImageObject]):
    term = RdfTerm("http://schema.org/diagram", "diagram")


class suggestedGender(RdfProperty[schemaorg.GenderType | schemaorg.Text]):
    term = RdfTerm("http://schema.org/suggestedGender", "suggestedGender")


class gameServer(RdfProperty[schemaorg.GameServer]):
    term = RdfTerm("http://schema.org/gameServer", "gameServer")


class alternateName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/alternateName", "alternateName")


class healthPlanPharmacyCategory(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/healthPlanPharmacyCategory", "healthPlanPharmacyCategory"
    )


class purchaseType(RdfProperty[schemaorg.PurchaseType]):
    term = RdfTerm("http://schema.org/purchaseType", "purchaseType")


class unnamedSourcesPolicy(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("http://schema.org/unnamedSourcesPolicy", "unnamedSourcesPolicy")


class installUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/installUrl", "installUrl")


class vehicleModelDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/vehicleModelDate", "vehicleModelDate")


class cutoffTime(RdfProperty[schemaorg.Time]):
    term = RdfTerm("http://schema.org/cutoffTime", "cutoffTime")


class applicationContact(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm("http://schema.org/applicationContact", "applicationContact")


class postOp(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/postOp", "postOp")


class transitTime(RdfProperty[schemaorg.QuantitativeValue | schemaorg.ServicePeriod]):
    term = RdfTerm("http://schema.org/transitTime", "transitTime")


class arrivalBusStop(RdfProperty[schemaorg.BusStop | schemaorg.BusStation]):
    term = RdfTerm("http://schema.org/arrivalBusStop", "arrivalBusStop")


class molecularFormula(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/molecularFormula", "molecularFormula")


class leaseLength(RdfProperty[schemaorg.Duration | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/leaseLength", "leaseLength")


class healthcareReportingData(RdfProperty[schemaorg.CDCPMDRecord | schemaorg.Dataset]):
    term = RdfTerm(
        "http://schema.org/healthcareReportingData", "healthcareReportingData"
    )


class supply(RdfProperty[schemaorg.HowToSupply | schemaorg.Text]):
    term = RdfTerm("http://schema.org/supply", "supply")


class departureStation(RdfProperty[schemaorg.TrainStation]):
    term = RdfTerm("http://schema.org/departureStation", "departureStation")


class colleagues(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/colleagues", "colleagues")


class structuralClass(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/structuralClass", "structuralClass")


class colorSwatch(RdfProperty[schemaorg.URL | schemaorg.ImageObject]):
    term = RdfTerm("http://schema.org/colorSwatch", "colorSwatch")


class membershipNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/membershipNumber", "membershipNumber")


class funding(RdfProperty[schemaorg.Grant]):
    term = RdfTerm("http://schema.org/funding", "funding")


class exerciseRelatedDiet(RdfProperty[schemaorg.Diet]):
    term = RdfTerm("http://schema.org/exerciseRelatedDiet", "exerciseRelatedDiet")


class uploadDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/uploadDate", "uploadDate")


class numberOfPartialBathrooms(RdfProperty[schemaorg.Number]):
    term = RdfTerm(
        "http://schema.org/numberOfPartialBathrooms", "numberOfPartialBathrooms"
    )


class itemListOrder(RdfProperty[schemaorg.Text | schemaorg.ItemListOrderType]):
    term = RdfTerm("http://schema.org/itemListOrder", "itemListOrder")


class discountCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/discountCurrency", "discountCurrency")


class sportsActivityLocation(RdfProperty[schemaorg.SportsActivityLocation]):
    term = RdfTerm("http://schema.org/sportsActivityLocation", "sportsActivityLocation")


class dayOfWeek(RdfProperty[schemaorg.DayOfWeek]):
    term = RdfTerm("http://schema.org/dayOfWeek", "dayOfWeek")


class encodings(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm("http://schema.org/encodings", "encodings")


class enginePower(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/enginePower", "enginePower")


class duringMedia(RdfProperty[schemaorg.URL | schemaorg.MediaObject]):
    term = RdfTerm("http://schema.org/duringMedia", "duringMedia")


class provider(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/provider", "provider")


class seatSection(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/seatSection", "seatSection")


class numberOfItems(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numberOfItems", "numberOfItems")


class isPartOf(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/isPartOf", "isPartOf")


class encoding(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm("http://schema.org/encoding", "encoding")


class hasCourseInstance(RdfProperty[schemaorg.CourseInstance]):
    term = RdfTerm("http://schema.org/hasCourseInstance", "hasCourseInstance")


class video(RdfProperty[schemaorg.Clip | schemaorg.VideoObject]):
    term = RdfTerm("http://schema.org/video", "video")


class recipeInstructions(
    RdfProperty[schemaorg.ItemList | schemaorg.CreativeWork | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/recipeInstructions", "recipeInstructions")


class successorOf(RdfProperty[schemaorg.ProductModel]):
    term = RdfTerm("http://schema.org/successorOf", "successorOf")


class bioChemInteraction(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm("http://schema.org/bioChemInteraction", "bioChemInteraction")


class collection(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/collection", "collection")


class subTrip(RdfProperty[schemaorg.Trip]):
    term = RdfTerm("http://schema.org/subTrip", "subTrip")


class potentialAction(RdfProperty[schemaorg.Action]):
    term = RdfTerm("http://schema.org/potentialAction", "potentialAction")


class thumbnail(RdfProperty[schemaorg.ImageObject]):
    term = RdfTerm("http://schema.org/thumbnail", "thumbnail")


class weightPercentage(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/weightPercentage", "weightPercentage")


class applicationCategory(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/applicationCategory", "applicationCategory")


class interactionCount(RdfProperty[RdfType]):
    term = RdfTerm("http://schema.org/interactionCount", "interactionCount")


class memoryRequirements(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/memoryRequirements", "memoryRequirements")


class associatedMediaReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm("http://schema.org/associatedMediaReview", "associatedMediaReview")


class servesCuisine(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/servesCuisine", "servesCuisine")


class benefits(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/benefits", "benefits")


class memberOf(
    RdfProperty[
        schemaorg.ProgramMembership
        | schemaorg.MemberProgramTier
        | schemaorg.Organization
    ]
):
    term = RdfTerm("http://schema.org/memberOf", "memberOf")


class legislationCountersignedBy(
    RdfProperty[schemaorg.Organization | schemaorg.Person]
):
    term = RdfTerm(
        "http://schema.org/legislationCountersignedBy", "legislationCountersignedBy"
    )


class credentialCategory(
    RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm]
):
    term = RdfTerm("http://schema.org/credentialCategory", "credentialCategory")


class acceptedAnswer(RdfProperty[schemaorg.ItemList | schemaorg.Answer]):
    term = RdfTerm("http://schema.org/acceptedAnswer", "acceptedAnswer")


class dissolutionDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/dissolutionDate", "dissolutionDate")


class guidelineSubject(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/guidelineSubject", "guidelineSubject")


class videoQuality(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/videoQuality", "videoQuality")


class broadcastDisplayName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/broadcastDisplayName", "broadcastDisplayName")


class eligibleDuration(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/eligibleDuration", "eligibleDuration")


class prepTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/prepTime", "prepTime")


class amount(RdfProperty[schemaorg.Number | schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/amount", "amount")


class toRecipient(
    RdfProperty[
        schemaorg.Audience
        | schemaorg.Organization
        | schemaorg.ContactPoint
        | schemaorg.Person
    ]
):
    term = RdfTerm("http://schema.org/toRecipient", "toRecipient")


class discussionUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/discussionUrl", "discussionUrl")


class creditedTo(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/creditedTo", "creditedTo")


class interactivityType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/interactivityType", "interactivityType")


class worksFor(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/worksFor", "worksFor")


class hasShippingService(RdfProperty[schemaorg.ShippingService]):
    term = RdfTerm("http://schema.org/hasShippingService", "hasShippingService")


class ingredients(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/ingredients", "ingredients")


class totalPrice(
    RdfProperty[schemaorg.Text | schemaorg.Number | schemaorg.PriceSpecification]
):
    term = RdfTerm("http://schema.org/totalPrice", "totalPrice")


class tourBookingPage(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/tourBookingPage", "tourBookingPage")


class tracks(RdfProperty[schemaorg.MusicRecording]):
    term = RdfTerm("http://schema.org/tracks", "tracks")


class cargoVolume(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/cargoVolume", "cargoVolume")


class sameAs(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/sameAs", "sameAs")


class hasDigitalDocumentPermission(RdfProperty[schemaorg.DigitalDocumentPermission]):
    term = RdfTerm(
        "http://schema.org/hasDigitalDocumentPermission", "hasDigitalDocumentPermission"
    )


class steps(RdfProperty[schemaorg.Text | schemaorg.ItemList | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/steps", "steps")


class openingHoursSpecification(RdfProperty[schemaorg.OpeningHoursSpecification]):
    term = RdfTerm(
        "http://schema.org/openingHoursSpecification", "openingHoursSpecification"
    )


class sodiumContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/sodiumContent", "sodiumContent")


class cashBack(RdfProperty[schemaorg.Number | schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/cashBack", "cashBack")


class termsOfService(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/termsOfService", "termsOfService")


class inBroadcastLineup(RdfProperty[schemaorg.CableOrSatelliteService]):
    term = RdfTerm("http://schema.org/inBroadcastLineup", "inBroadcastLineup")


class reviewCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/reviewCount", "reviewCount")


class webFeed(RdfProperty[schemaorg.URL | schemaorg.DataFeed]):
    term = RdfTerm("http://schema.org/webFeed", "webFeed")


class timeRequired(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/timeRequired", "timeRequired")


class validFrom(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/validFrom", "validFrom")


class safetyConsideration(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/safetyConsideration", "safetyConsideration")


class sender(
    RdfProperty[schemaorg.Person | schemaorg.Audience | schemaorg.Organization]
):
    term = RdfTerm("http://schema.org/sender", "sender")


class maxPrice(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/maxPrice", "maxPrice")


class height(RdfProperty[schemaorg.Distance | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/height", "height")


class relatedTherapy(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm("http://schema.org/relatedTherapy", "relatedTherapy")


class fatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/fatContent", "fatContent")


class skills(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm("http://schema.org/skills", "skills")


class specialty(RdfProperty[schemaorg.Specialty]):
    term = RdfTerm("http://schema.org/specialty", "specialty")


class transFatContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/transFatContent", "transFatContent")


class itemReviewed(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/itemReviewed", "itemReviewed")


class nonprofitStatus(RdfProperty[schemaorg.NonprofitType]):
    term = RdfTerm("http://schema.org/nonprofitStatus", "nonprofitStatus")


class employee(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/employee", "employee")


class issuedThrough(RdfProperty[schemaorg.Service]):
    term = RdfTerm("http://schema.org/issuedThrough", "issuedThrough")


class recordedIn(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/recordedIn", "recordedIn")


class servicePhone(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm("http://schema.org/servicePhone", "servicePhone")


class vehicleSeatingCapacity(
    RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]
):
    term = RdfTerm("http://schema.org/vehicleSeatingCapacity", "vehicleSeatingCapacity")


class recommendedIntake(RdfProperty[schemaorg.RecommendedDoseSchedule]):
    term = RdfTerm("http://schema.org/recommendedIntake", "recommendedIntake")


class givenName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/givenName", "givenName")


class characterAttribute(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/characterAttribute", "characterAttribute")


class carrier(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/carrier", "carrier")


class jurisdiction(RdfProperty[schemaorg.AdministrativeArea | schemaorg.Text]):
    term = RdfTerm("http://schema.org/jurisdiction", "jurisdiction")


class reviewRating(RdfProperty[schemaorg.Rating]):
    term = RdfTerm("http://schema.org/reviewRating", "reviewRating")


class worstRating(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/worstRating", "worstRating")


class fileSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/fileSize", "fileSize")


class applicationSubCategory(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/applicationSubCategory", "applicationSubCategory")


class identifier(RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/identifier", "identifier")


class nutrition(RdfProperty[schemaorg.NutritionInformation]):
    term = RdfTerm("http://schema.org/nutrition", "nutrition")


class orderedItem(
    RdfProperty[schemaorg.Service | schemaorg.OrderItem | schemaorg.Product]
):
    term = RdfTerm("http://schema.org/orderedItem", "orderedItem")


class httpMethod(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/httpMethod", "httpMethod")


class servingSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/servingSize", "servingSize")


class durationOfWarranty(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/durationOfWarranty", "durationOfWarranty")


class domainIncludes(RdfProperty[schemaorg.Class]):
    term = RdfTerm("http://schema.org/domainIncludes", "domainIncludes")


class bccRecipient(
    RdfProperty[schemaorg.Organization | schemaorg.ContactPoint | schemaorg.Person]
):
    term = RdfTerm("http://schema.org/bccRecipient", "bccRecipient")


class text(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/text", "text")


class tributary(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/tributary", "tributary")


class serviceUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/serviceUrl", "serviceUrl")


class priceValidUntil(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/priceValidUntil", "priceValidUntil")


class founder(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/founder", "founder")


class significantLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/significantLink", "significantLink")


class valueMinLength(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/valueMinLength", "valueMinLength")


class healthPlanDrugOption(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/healthPlanDrugOption", "healthPlanDrugOption")


class codeValue(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/codeValue", "codeValue")


class blogPosts(RdfProperty[schemaorg.BlogPosting]):
    term = RdfTerm("http://schema.org/blogPosts", "blogPosts")


class musicReleaseFormat(RdfProperty[schemaorg.MusicReleaseFormatType]):
    term = RdfTerm("http://schema.org/musicReleaseFormat", "musicReleaseFormat")


class numberOfAvailableAccommodationUnits(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm(
        "http://schema.org/numberOfAvailableAccommodationUnits",
        "numberOfAvailableAccommodationUnits",
    )


class playMode(RdfProperty[schemaorg.GamePlayMode]):
    term = RdfTerm("http://schema.org/playMode", "playMode")


class lesser(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm("http://schema.org/lesser", "lesser")


class naics(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/naics", "naics")


class requiredQuantity(
    RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/requiredQuantity", "requiredQuantity")


class isBasedOn(
    RdfProperty[schemaorg.CreativeWork | schemaorg.Product | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/isBasedOn", "isBasedOn")


class gameTip(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/gameTip", "gameTip")


class causeOf(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/causeOf", "causeOf")


class originalMediaLink(
    RdfProperty[schemaorg.MediaObject | schemaorg.WebPage | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/originalMediaLink", "originalMediaLink")


class awards(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/awards", "awards")


class employerOverview(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/employerOverview", "employerOverview")


class interactionStatistic(RdfProperty[schemaorg.InteractionCounter]):
    term = RdfTerm("http://schema.org/interactionStatistic", "interactionStatistic")


class seatRow(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/seatRow", "seatRow")


class conditionsOfAccess(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/conditionsOfAccess", "conditionsOfAccess")


class cvdNumVentUse(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumVentUse", "cvdNumVentUse")


class telephone(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/telephone", "telephone")


class jobBenefits(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/jobBenefits", "jobBenefits")


class publicTransportClosuresInfo(RdfProperty[schemaorg.WebContent | schemaorg.URL]):
    term = RdfTerm(
        "http://schema.org/publicTransportClosuresInfo", "publicTransportClosuresInfo"
    )


class actionStatus(RdfProperty[schemaorg.ActionStatusType]):
    term = RdfTerm("http://schema.org/actionStatus", "actionStatus")


class arrivalBoatTerminal(RdfProperty[schemaorg.BoatTerminal]):
    term = RdfTerm("http://schema.org/arrivalBoatTerminal", "arrivalBoatTerminal")


class temporalCoverage(
    RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.DateTime]
):
    term = RdfTerm("http://schema.org/temporalCoverage", "temporalCoverage")


class legalRepresentative(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/legalRepresentative", "legalRepresentative")


class question(RdfProperty[schemaorg.Question]):
    term = RdfTerm("http://schema.org/question", "question")


class numberOfForwardGears(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfForwardGears", "numberOfForwardGears")


class openingHours(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/openingHours", "openingHours")


class containedInPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/containedInPlace", "containedInPlace")


class director(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/director", "director")


class providerMobility(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/providerMobility", "providerMobility")


class geoIntersects(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm("http://schema.org/geoIntersects", "geoIntersects")


class accountOverdraftLimit(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/accountOverdraftLimit", "accountOverdraftLimit")


class netWorth(RdfProperty[schemaorg.PriceSpecification | schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/netWorth", "netWorth")


class version(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm("http://schema.org/version", "version")


class actionableFeedbackPolicy(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm(
        "http://schema.org/actionableFeedbackPolicy", "actionableFeedbackPolicy"
    )


class healthPlanId(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/healthPlanId", "healthPlanId")


class deathDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/deathDate", "deathDate")


class healthPlanCostSharing(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/healthPlanCostSharing", "healthPlanCostSharing")


class noBylinesPolicy(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("http://schema.org/noBylinesPolicy", "noBylinesPolicy")


class affiliation(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/affiliation", "affiliation")


class evidenceOrigin(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/evidenceOrigin", "evidenceOrigin")


class originalMediaContextDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/originalMediaContextDescription",
        "originalMediaContextDescription",
    )


class encodingFormat(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/encodingFormat", "encodingFormat")


class greaterOrEqual(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm("http://schema.org/greaterOrEqual", "greaterOrEqual")


class hasEnergyEfficiencyCategory(RdfProperty[schemaorg.EnergyEfficiencyEnumeration]):
    term = RdfTerm(
        "http://schema.org/hasEnergyEfficiencyCategory", "hasEnergyEfficiencyCategory"
    )


class softwareVersion(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/softwareVersion", "softwareVersion")


class legislationLegalForce(RdfProperty[schemaorg.LegalForceStatus]):
    term = RdfTerm("http://schema.org/legislationLegalForce", "legislationLegalForce")


class boardingGroup(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/boardingGroup", "boardingGroup")


class departureTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/departureTime", "departureTime")


class clinicalPharmacology(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/clinicalPharmacology", "clinicalPharmacology")


class firstAppearance(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/firstAppearance", "firstAppearance")


class inProductGroupWithID(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/inProductGroupWithID", "inProductGroupWithID")


class acquiredFrom(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/acquiredFrom", "acquiredFrom")


class broadcastFrequencyValue(
    RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]
):
    term = RdfTerm(
        "http://schema.org/broadcastFrequencyValue", "broadcastFrequencyValue"
    )


class validUntil(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/validUntil", "validUntil")


class iswcCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/iswcCode", "iswcCode")


class financialAidEligible(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/financialAidEligible", "financialAidEligible")


class increasesRiskOf(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/increasesRiskOf", "increasesRiskOf")


class seatingCapacity(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm("http://schema.org/seatingCapacity", "seatingCapacity")


class directApply(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/directApply", "directApply")


class workLocation(RdfProperty[schemaorg.ContactPoint | schemaorg.Place]):
    term = RdfTerm("http://schema.org/workLocation", "workLocation")


class publication(RdfProperty[schemaorg.PublicationEvent]):
    term = RdfTerm("http://schema.org/publication", "publication")


class suggestedAge(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/suggestedAge", "suggestedAge")


class numberOfSeasons(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numberOfSeasons", "numberOfSeasons")


class isFamilyFriendly(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isFamilyFriendly", "isFamilyFriendly")


class minValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/minValue", "minValue")


class merchant(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/merchant", "merchant")


class costCategory(RdfProperty[schemaorg.DrugCostCategory]):
    term = RdfTerm("http://schema.org/costCategory", "costCategory")


class relatedLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/relatedLink", "relatedLink")


class alcoholWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/alcoholWarning", "alcoholWarning")


class buyer(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/buyer", "buyer")


class study(RdfProperty[schemaorg.MedicalStudy]):
    term = RdfTerm("http://schema.org/study", "study")


class contraindication(RdfProperty[schemaorg.Text | schemaorg.MedicalContraindication]):
    term = RdfTerm("http://schema.org/contraindication", "contraindication")


class bookFormat(RdfProperty[schemaorg.BookFormatType]):
    term = RdfTerm("http://schema.org/bookFormat", "bookFormat")


class free(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/free", "free")


class processingTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/processingTime", "processingTime")


class numberOfAccommodationUnits(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm(
        "http://schema.org/numberOfAccommodationUnits", "numberOfAccommodationUnits"
    )


class event(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/event", "event")


class hasDeliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm("http://schema.org/hasDeliveryMethod", "hasDeliveryMethod")


class ownershipFundingInfo(
    RdfProperty[
        schemaorg.AboutPage | schemaorg.CreativeWork | schemaorg.Text | schemaorg.URL
    ]
):
    term = RdfTerm("http://schema.org/ownershipFundingInfo", "ownershipFundingInfo")


class materialExtent(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/materialExtent", "materialExtent")


class recommendationStrength(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/recommendationStrength", "recommendationStrength")


class drugClass(RdfProperty[schemaorg.DrugClass]):
    term = RdfTerm("http://schema.org/drugClass", "drugClass")


class siblings(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/siblings", "siblings")


class cvdNumICUBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumICUBeds", "cvdNumICUBeds")


class clipNumber(RdfProperty[schemaorg.Text | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/clipNumber", "clipNumber")


class directors(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/directors", "directors")


class foundingDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/foundingDate", "foundingDate")


class headline(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/headline", "headline")


class accessMode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accessMode", "accessMode")


class inverseOf(RdfProperty[schemaorg.Property]):
    term = RdfTerm("http://schema.org/inverseOf", "inverseOf")


class availableAtOrFrom(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/availableAtOrFrom", "availableAtOrFrom")


class hasMenuItem(RdfProperty[schemaorg.MenuItem]):
    term = RdfTerm("http://schema.org/hasMenuItem", "hasMenuItem")


class priceCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/priceCurrency", "priceCurrency")


class productReturnLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/productReturnLink", "productReturnLink")


class targetPlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/targetPlatform", "targetPlatform")


class expectedArrivalFrom(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/expectedArrivalFrom", "expectedArrivalFrom")


class seller(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/seller", "seller")


class additionalType(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/additionalType", "additionalType")


class resultComment(RdfProperty[schemaorg.Comment]):
    term = RdfTerm("http://schema.org/resultComment", "resultComment")


class geoRadius(RdfProperty[schemaorg.Text | schemaorg.Number | schemaorg.Distance]):
    term = RdfTerm("http://schema.org/geoRadius", "geoRadius")


class originatesFrom(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm("http://schema.org/originatesFrom", "originatesFrom")


class numberOfPages(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numberOfPages", "numberOfPages")


class variesBy(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/variesBy", "variesBy")


class itemOffered(
    RdfProperty[
        schemaorg.Service
        | schemaorg.AggregateOffer
        | schemaorg.CreativeWork
        | schemaorg.Event
        | schemaorg.MenuItem
        | schemaorg.Product
        | schemaorg.Trip
    ]
):
    term = RdfTerm("http://schema.org/itemOffered", "itemOffered")


class targetName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/targetName", "targetName")


class procedureType(RdfProperty[schemaorg.MedicalProcedureType]):
    term = RdfTerm("http://schema.org/procedureType", "procedureType")


class issn(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/issn", "issn")


class answerExplanation(RdfProperty[schemaorg.WebContent | schemaorg.Comment]):
    term = RdfTerm("http://schema.org/answerExplanation", "answerExplanation")


class trackingUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/trackingUrl", "trackingUrl")


class object(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/object", "object")


class albumReleaseType(RdfProperty[schemaorg.MusicAlbumReleaseType]):
    term = RdfTerm("http://schema.org/albumReleaseType", "albumReleaseType")


class artMedium(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/artMedium", "artMedium")


class publishedOn(RdfProperty[schemaorg.BroadcastService]):
    term = RdfTerm("http://schema.org/publishedOn", "publishedOn")


class value(
    RdfProperty[
        schemaorg.Text
        | schemaorg.Number
        | schemaorg.Boolean
        | schemaorg.StructuredValue
    ]
):
    term = RdfTerm("http://schema.org/value", "value")


class multipleValues(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/multipleValues", "multipleValues")


class course(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/course", "course")


class lodgingUnitDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/lodgingUnitDescription", "lodgingUnitDescription")


class recipeIngredient(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/recipeIngredient", "recipeIngredient")


class accountablePerson(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/accountablePerson", "accountablePerson")


class partOfInvoice(RdfProperty[schemaorg.Invoice]):
    term = RdfTerm("http://schema.org/partOfInvoice", "partOfInvoice")


class equal(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm("http://schema.org/equal", "equal")


class program(RdfProperty[schemaorg.MemberProgram]):
    term = RdfTerm("http://schema.org/program", "program")


class sugarContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/sugarContent", "sugarContent")


class costCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/costCurrency", "costCurrency")


class workHours(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/workHours", "workHours")


class busNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/busNumber", "busNumber")


class album(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm("http://schema.org/album", "album")


class preparation(RdfProperty[schemaorg.Text | schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/preparation", "preparation")


class landlord(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/landlord", "landlord")


class seasonalOverride(RdfProperty[schemaorg.OpeningHoursSpecification]):
    term = RdfTerm("http://schema.org/seasonalOverride", "seasonalOverride")


class hiringOrganization(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/hiringOrganization", "hiringOrganization")


class interestRate(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/interestRate", "interestRate")


class cvdNumC19OverflowPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumC19OverflowPats", "cvdNumC19OverflowPats")


class legalName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/legalName", "legalName")


class typeOfBed(RdfProperty[schemaorg.BedType | schemaorg.Text]):
    term = RdfTerm("http://schema.org/typeOfBed", "typeOfBed")


class knowsAbout(RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.Thing]):
    term = RdfTerm("http://schema.org/knowsAbout", "knowsAbout")


class inSupportOf(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/inSupportOf", "inSupportOf")


class touristType(RdfProperty[schemaorg.Audience | schemaorg.Text]):
    term = RdfTerm("http://schema.org/touristType", "touristType")


class returnPolicySeasonalOverride(
    RdfProperty[schemaorg.MerchantReturnPolicySeasonalOverride]
):
    term = RdfTerm(
        "http://schema.org/returnPolicySeasonalOverride", "returnPolicySeasonalOverride"
    )


class followee(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/followee", "followee")


class programPrerequisites(
    RdfProperty[
        schemaorg.EducationalOccupationalCredential
        | schemaorg.Text
        | schemaorg.AlignmentObject
        | schemaorg.Course
    ]
):
    term = RdfTerm("http://schema.org/programPrerequisites", "programPrerequisites")


class fundedItem(
    RdfProperty[
        schemaorg.Organization
        | schemaorg.CreativeWork
        | schemaorg.Person
        | schemaorg.Product
        | schemaorg.BioChemEntity
        | schemaorg.MedicalEntity
        | schemaorg.Event
    ]
):
    term = RdfTerm("http://schema.org/fundedItem", "fundedItem")


class ccRecipient(
    RdfProperty[schemaorg.Organization | schemaorg.ContactPoint | schemaorg.Person]
):
    term = RdfTerm("http://schema.org/ccRecipient", "ccRecipient")


class exerciseType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/exerciseType", "exerciseType")


class accessibilitySummary(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accessibilitySummary", "accessibilitySummary")


class shippingOrigin(RdfProperty[schemaorg.DefinedRegion]):
    term = RdfTerm("http://schema.org/shippingOrigin", "shippingOrigin")


class containsPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/containsPlace", "containsPlace")


class cvdNumBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumBeds", "cvdNumBeds")


class hasMap(RdfProperty[schemaorg.URL | schemaorg.Map]):
    term = RdfTerm("http://schema.org/hasMap", "hasMap")


class musicalKey(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/musicalKey", "musicalKey")


class cvdFacilityCounty(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/cvdFacilityCounty", "cvdFacilityCounty")


class areaServed(
    RdfProperty[
        schemaorg.AdministrativeArea
        | schemaorg.Place
        | schemaorg.GeoShape
        | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/areaServed", "areaServed")


class applicantLocationRequirements(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm(
        "http://schema.org/applicantLocationRequirements",
        "applicantLocationRequirements",
    )


class applicationSuite(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/applicationSuite", "applicationSuite")


class gamePlatform(RdfProperty[schemaorg.URL | schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm("http://schema.org/gamePlatform", "gamePlatform")


class energyEfficiencyScaleMax(RdfProperty[schemaorg.EUEnergyEfficiencyEnumeration]):
    term = RdfTerm(
        "http://schema.org/energyEfficiencyScaleMax", "energyEfficiencyScaleMax"
    )


class distance(RdfProperty[schemaorg.Distance]):
    term = RdfTerm("http://schema.org/distance", "distance")


class dosageForm(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/dosageForm", "dosageForm")


class endDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/endDate", "endDate")


class targetDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/targetDescription", "targetDescription")


class emissionsCO2(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/emissionsCO2", "emissionsCO2")


class arrivalGate(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/arrivalGate", "arrivalGate")


class map(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/map", "map")


class mpn(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/mpn", "mpn")


class productionDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/productionDate", "productionDate")


class modifiedTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/modifiedTime", "modifiedTime")


class appliesToPaymentMethod(RdfProperty[schemaorg.PaymentMethod]):
    term = RdfTerm("http://schema.org/appliesToPaymentMethod", "appliesToPaymentMethod")


class photos(RdfProperty[schemaorg.ImageObject | schemaorg.Photograph]):
    term = RdfTerm("http://schema.org/photos", "photos")


class hasCourse(RdfProperty[schemaorg.Course]):
    term = RdfTerm("http://schema.org/hasCourse", "hasCourse")


class printPage(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/printPage", "printPage")


class seasonNumber(RdfProperty[schemaorg.Text | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/seasonNumber", "seasonNumber")


class gameAvailabilityType(
    RdfProperty[schemaorg.Text | schemaorg.GameAvailabilityEnumeration]
):
    term = RdfTerm("http://schema.org/gameAvailabilityType", "gameAvailabilityType")


class geoCovers(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm("http://schema.org/geoCovers", "geoCovers")


class trainNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/trainNumber", "trainNumber")


class educationalUse(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/educationalUse", "educationalUse")


class syllabusSections(RdfProperty[schemaorg.Syllabus]):
    term = RdfTerm("http://schema.org/syllabusSections", "syllabusSections")


class restPeriods(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/restPeriods", "restPeriods")


class legislationEnsuresImplementationOf(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm(
        "http://schema.org/legislationEnsuresImplementationOf",
        "legislationEnsuresImplementationOf",
    )


class availableThrough(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/availableThrough", "availableThrough")


class storageRequirements(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/storageRequirements", "storageRequirements")


class isEncodedByBioChemEntity(RdfProperty[schemaorg.Gene]):
    term = RdfTerm(
        "http://schema.org/isEncodedByBioChemEntity", "isEncodedByBioChemEntity"
    )


class iso6523Code(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/iso6523Code", "iso6523Code")


class expressedIn(
    RdfProperty[
        schemaorg.AnatomicalStructure
        | schemaorg.DefinedTerm
        | schemaorg.BioChemEntity
        | schemaorg.AnatomicalSystem
    ]
):
    term = RdfTerm("http://schema.org/expressedIn", "expressedIn")


class measurementTechnique(
    RdfProperty[
        schemaorg.Text
        | schemaorg.DefinedTerm
        | schemaorg.URL
        | schemaorg.MeasurementMethodEnum
    ]
):
    term = RdfTerm("http://schema.org/measurementTechnique", "measurementTechnique")


class employees(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/employees", "employees")


class floorSize(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/floorSize", "floorSize")


class proteinContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/proteinContent", "proteinContent")


class totalPaymentDue(
    RdfProperty[schemaorg.PriceSpecification | schemaorg.MonetaryAmount]
):
    term = RdfTerm("http://schema.org/totalPaymentDue", "totalPaymentDue")


class productReturnDays(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/productReturnDays", "productReturnDays")


class secondaryPrevention(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm("http://schema.org/secondaryPrevention", "secondaryPrevention")


class usNPI(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/usNPI", "usNPI")


class recipeCategory(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/recipeCategory", "recipeCategory")


class totalJobOpenings(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/totalJobOpenings", "totalJobOpenings")


class numItems(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/numItems", "numItems")


class programmingModel(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/programmingModel", "programmingModel")


class workExample(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/workExample", "workExample")


class embedUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/embedUrl", "embedUrl")


class eligibilityToWorkRequirement(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/eligibilityToWorkRequirement", "eligibilityToWorkRequirement"
    )


class hasHealthAspect(RdfProperty[schemaorg.HealthAspectEnumeration]):
    term = RdfTerm("http://schema.org/hasHealthAspect", "hasHealthAspect")


class recordingOf(RdfProperty[schemaorg.MusicComposition]):
    term = RdfTerm("http://schema.org/recordingOf", "recordingOf")


class priceRange(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/priceRange", "priceRange")


class reviewBody(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/reviewBody", "reviewBody")


class doorTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/doorTime", "doorTime")


class requiresSubscription(
    RdfProperty[schemaorg.MediaSubscription | schemaorg.Boolean]
):
    term = RdfTerm("http://schema.org/requiresSubscription", "requiresSubscription")


class alternativeOf(RdfProperty[schemaorg.Gene]):
    term = RdfTerm("http://schema.org/alternativeOf", "alternativeOf")


class photo(RdfProperty[schemaorg.ImageObject | schemaorg.Photograph]):
    term = RdfTerm("http://schema.org/photo", "photo")


class isGift(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isGift", "isGift")


class isInvolvedInBiologicalProcess(
    RdfProperty[schemaorg.PropertyValue | schemaorg.DefinedTerm | schemaorg.URL]
):
    term = RdfTerm(
        "http://schema.org/isInvolvedInBiologicalProcess",
        "isInvolvedInBiologicalProcess",
    )


class requiredMaxAge(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/requiredMaxAge", "requiredMaxAge")


class loanPaymentAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/loanPaymentAmount", "loanPaymentAmount")


class typeOfGood(RdfProperty[schemaorg.Product | schemaorg.Service]):
    term = RdfTerm("http://schema.org/typeOfGood", "typeOfGood")


class seriousAdverseOutcome(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/seriousAdverseOutcome", "seriousAdverseOutcome")


class renegotiableLoan(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/renegotiableLoan", "renegotiableLoan")


class actionProcess(RdfProperty[schemaorg.HowTo]):
    term = RdfTerm("http://schema.org/actionProcess", "actionProcess")


class editor(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/editor", "editor")


class pronouns(
    RdfProperty[schemaorg.StructuredValue | schemaorg.Text | schemaorg.DefinedTerm]
):
    term = RdfTerm("http://schema.org/pronouns", "pronouns")


class includesAttraction(RdfProperty[schemaorg.TouristAttraction]):
    term = RdfTerm("http://schema.org/includesAttraction", "includesAttraction")


class numberOfEmployees(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/numberOfEmployees", "numberOfEmployees")


class legislationIdentifier(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/legislationIdentifier", "legislationIdentifier")


class affectedBy(RdfProperty[schemaorg.Drug]):
    term = RdfTerm("http://schema.org/affectedBy", "affectedBy")


class cvdFacilityId(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/cvdFacilityId", "cvdFacilityId")


class cookingMethod(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/cookingMethod", "cookingMethod")


class additionalProperty(RdfProperty[schemaorg.PropertyValue]):
    term = RdfTerm("http://schema.org/additionalProperty", "additionalProperty")


class defaultValue(RdfProperty[schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm("http://schema.org/defaultValue", "defaultValue")


class countriesSupported(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/countriesSupported", "countriesSupported")


class gtin12(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/gtin12", "gtin12")


class winner(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/winner", "winner")


class procedure(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/procedure", "procedure")


class warrantyPromise(RdfProperty[schemaorg.WarrantyPromise]):
    term = RdfTerm("http://schema.org/warrantyPromise", "warrantyPromise")


class orderDelivery(RdfProperty[schemaorg.ParcelDelivery]):
    term = RdfTerm("http://schema.org/orderDelivery", "orderDelivery")


class catalog(RdfProperty[schemaorg.DataCatalog]):
    term = RdfTerm("http://schema.org/catalog", "catalog")


class actionAccessibilityRequirement(RdfProperty[schemaorg.ActionAccessSpecification]):
    term = RdfTerm(
        "http://schema.org/actionAccessibilityRequirement",
        "actionAccessibilityRequirement",
    )


class interactingDrug(RdfProperty[schemaorg.Drug]):
    term = RdfTerm("http://schema.org/interactingDrug", "interactingDrug")


class steeringPosition(RdfProperty[schemaorg.SteeringPositionValue]):
    term = RdfTerm("http://schema.org/steeringPosition", "steeringPosition")


class rangeIncludes(RdfProperty[schemaorg.Class]):
    term = RdfTerm("http://schema.org/rangeIncludes", "rangeIncludes")


class countriesNotSupported(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/countriesNotSupported", "countriesNotSupported")


class healthPlanMarketingUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/healthPlanMarketingUrl", "healthPlanMarketingUrl")


class healthPlanDrugTier(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/healthPlanDrugTier", "healthPlanDrugTier")


class foundingLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/foundingLocation", "foundingLocation")


class ineligibleRegion(
    RdfProperty[schemaorg.Place | schemaorg.GeoShape | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/ineligibleRegion", "ineligibleRegion")


class transitTimeLabel(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/transitTimeLabel", "transitTimeLabel")


class regionDrained(
    RdfProperty[schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem]
):
    term = RdfTerm("http://schema.org/regionDrained", "regionDrained")


class departureTerminal(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/departureTerminal", "departureTerminal")


class hasMolecularFunction(
    RdfProperty[schemaorg.DefinedTerm | schemaorg.URL | schemaorg.PropertyValue]
):
    term = RdfTerm("http://schema.org/hasMolecularFunction", "hasMolecularFunction")


class eligibleQuantity(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/eligibleQuantity", "eligibleQuantity")


class specialCommitments(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/specialCommitments", "specialCommitments")


class studyLocation(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm("http://schema.org/studyLocation", "studyLocation")


class measurementDenominator(RdfProperty[schemaorg.StatisticalVariable]):
    term = RdfTerm("http://schema.org/measurementDenominator", "measurementDenominator")


class occupationalCategory(RdfProperty[schemaorg.CategoryCode | schemaorg.Text]):
    term = RdfTerm("http://schema.org/occupationalCategory", "occupationalCategory")


class antagonist(RdfProperty[schemaorg.Muscle]):
    term = RdfTerm("http://schema.org/antagonist", "antagonist")


class referenceQuantity(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/referenceQuantity", "referenceQuantity")


class monthsOfExperience(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/monthsOfExperience", "monthsOfExperience")


class isUnlabelledFallback(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isUnlabelledFallback", "isUnlabelledFallback")


class propertyID(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/propertyID", "propertyID")


class opponent(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/opponent", "opponent")


class servicePostalAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm("http://schema.org/servicePostalAddress", "servicePostalAddress")


class availableStrength(RdfProperty[schemaorg.DrugStrength]):
    term = RdfTerm("http://schema.org/availableStrength", "availableStrength")


class incentiveCompensation(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/incentiveCompensation", "incentiveCompensation")


class track(RdfProperty[schemaorg.MusicRecording | schemaorg.ItemList]):
    term = RdfTerm("http://schema.org/track", "track")


class calories(RdfProperty[schemaorg.Energy]):
    term = RdfTerm("http://schema.org/calories", "calories")


class subjectOf(RdfProperty[schemaorg.CreativeWork | schemaorg.Event]):
    term = RdfTerm("http://schema.org/subjectOf", "subjectOf")


class schemaVersion(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/schemaVersion", "schemaVersion")


class size(
    RdfProperty[
        schemaorg.Text
        | schemaorg.DefinedTerm
        | schemaorg.SizeSpecification
        | schemaorg.QuantitativeValue
    ]
):
    term = RdfTerm("http://schema.org/size", "size")


class arrivalAirport(RdfProperty[schemaorg.Airport]):
    term = RdfTerm("http://schema.org/arrivalAirport", "arrivalAirport")


class name(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/name", "name")


class address(RdfProperty[schemaorg.Text | schemaorg.PostalAddress]):
    term = RdfTerm("http://schema.org/address", "address")


class membershipPointsEarned(
    RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]
):
    term = RdfTerm("http://schema.org/membershipPointsEarned", "membershipPointsEarned")


class studyDesign(RdfProperty[schemaorg.MedicalObservationalStudyDesign]):
    term = RdfTerm("http://schema.org/studyDesign", "studyDesign")


class studySubject(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/studySubject", "studySubject")


class numberOfPlayers(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/numberOfPlayers", "numberOfPlayers")


class recipeYield(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/recipeYield", "recipeYield")


class hasBioPolymerSequence(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/hasBioPolymerSequence", "hasBioPolymerSequence")


class parentService(RdfProperty[schemaorg.BroadcastService]):
    term = RdfTerm("http://schema.org/parentService", "parentService")


class guidelineDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/guidelineDate", "guidelineDate")


class performerIn(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/performerIn", "performerIn")


class assesses(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/assesses", "assesses")


class contactPoints(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm("http://schema.org/contactPoints", "contactPoints")


class reservedTicket(RdfProperty[schemaorg.Ticket]):
    term = RdfTerm("http://schema.org/reservedTicket", "reservedTicket")


class events(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/events", "events")


class legislationChanges(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm("http://schema.org/legislationChanges", "legislationChanges")


class legislationPassedBy(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/legislationPassedBy", "legislationPassedBy")


class numberOfDoors(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfDoors", "numberOfDoors")


class accessCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accessCode", "accessCode")


class upvoteCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/upvoteCount", "upvoteCount")


class discountCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/discountCode", "discountCode")


class measurementMethod(
    RdfProperty[
        schemaorg.DefinedTerm
        | schemaorg.URL
        | schemaorg.MeasurementMethodEnum
        | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/measurementMethod", "measurementMethod")


class gtin13(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/gtin13", "gtin13")


class availabilityStarts(
    RdfProperty[schemaorg.Date | schemaorg.Time | schemaorg.DateTime]
):
    term = RdfTerm("http://schema.org/availabilityStarts", "availabilityStarts")


class isVariantOf(RdfProperty[schemaorg.ProductModel | schemaorg.ProductGroup]):
    term = RdfTerm("http://schema.org/isVariantOf", "isVariantOf")


class estimatesRiskOf(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/estimatesRiskOf", "estimatesRiskOf")


class surface(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/surface", "surface")


class department(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/department", "department")


class tocContinuation(RdfProperty[schemaorg.HyperTocEntry]):
    term = RdfTerm("http://schema.org/tocContinuation", "tocContinuation")


class possibleComplication(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/possibleComplication", "possibleComplication")


class broadcastFrequency(
    RdfProperty[schemaorg.BroadcastFrequencySpecification | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/broadcastFrequency", "broadcastFrequency")


class jobLocationType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/jobLocationType", "jobLocationType")


class audio(
    RdfProperty[schemaorg.MusicRecording | schemaorg.AudioObject | schemaorg.Clip]
):
    term = RdfTerm("http://schema.org/audio", "audio")


class legislationDateOfApplicability(RdfProperty[schemaorg.Date]):
    term = RdfTerm(
        "http://schema.org/legislationDateOfApplicability",
        "legislationDateOfApplicability",
    )


class departureGate(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/departureGate", "departureGate")


class associatedMedia(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm("http://schema.org/associatedMedia", "associatedMedia")


class description(RdfProperty[schemaorg.TextObject | schemaorg.Text]):
    term = RdfTerm("http://schema.org/description", "description")


class certificationIdentification(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm(
        "http://schema.org/certificationIdentification", "certificationIdentification"
    )


class gracePeriod(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/gracePeriod", "gracePeriod")


class endOffset(RdfProperty[schemaorg.Number | schemaorg.HyperTocEntry]):
    term = RdfTerm("http://schema.org/endOffset", "endOffset")


class produces(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/produces", "produces")


class dropoffTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/dropoffTime", "dropoffTime")


class partOfOrder(RdfProperty[schemaorg.Order]):
    term = RdfTerm("http://schema.org/partOfOrder", "partOfOrder")


class hasPOS(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/hasPOS", "hasPOS")


class target(RdfProperty[schemaorg.URL | schemaorg.EntryPoint]):
    term = RdfTerm("http://schema.org/target", "target")


class returnPolicyCategory(RdfProperty[schemaorg.MerchantReturnEnumeration]):
    term = RdfTerm("http://schema.org/returnPolicyCategory", "returnPolicyCategory")


class strengthUnit(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/strengthUnit", "strengthUnit")


class language(RdfProperty[schemaorg.Language]):
    term = RdfTerm("http://schema.org/language", "language")


class globalLocationNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/globalLocationNumber", "globalLocationNumber")


class roleName(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/roleName", "roleName")


class author(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/author", "author")


class recordedAs(RdfProperty[schemaorg.MusicRecording]):
    term = RdfTerm("http://schema.org/recordedAs", "recordedAs")


class parentTaxon(RdfProperty[schemaorg.Taxon | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/parentTaxon", "parentTaxon")


class maximumIntake(RdfProperty[schemaorg.MaximumDoseSchedule]):
    term = RdfTerm("http://schema.org/maximumIntake", "maximumIntake")


class episode(RdfProperty[schemaorg.Episode]):
    term = RdfTerm("http://schema.org/episode", "episode")


class employmentUnit(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/employmentUnit", "employmentUnit")


class gettingTestedInfo(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm("http://schema.org/gettingTestedInfo", "gettingTestedInfo")


class educationalFramework(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/educationalFramework", "educationalFramework")


class mentions(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/mentions", "mentions")


class numChildren(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numChildren", "numChildren")


class episodeNumber(RdfProperty[schemaorg.Text | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/episodeNumber", "episodeNumber")


class healthPlanCoinsuranceOption(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/healthPlanCoinsuranceOption", "healthPlanCoinsuranceOption"
    )


class iataCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/iataCode", "iataCode")


class relatedCondition(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm("http://schema.org/relatedCondition", "relatedCondition")


class publicAccess(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/publicAccess", "publicAccess")


class monthlyMinimumRepaymentAmount(
    RdfProperty[schemaorg.Number | schemaorg.MonetaryAmount]
):
    term = RdfTerm(
        "http://schema.org/monthlyMinimumRepaymentAmount",
        "monthlyMinimumRepaymentAmount",
    )


class employmentType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/employmentType", "employmentType")


class albums(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm("http://schema.org/albums", "albums")


class leiCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/leiCode", "leiCode")


class biologicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/biologicalRole", "biologicalRole")


class tongueWeight(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/tongueWeight", "tongueWeight")


class athlete(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/athlete", "athlete")


class numberOfBedrooms(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/numberOfBedrooms", "numberOfBedrooms")


class disambiguatingDescription(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/disambiguatingDescription", "disambiguatingDescription"
    )


class purchaseDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/purchaseDate", "purchaseDate")


class mediaAuthenticityCategory(
    RdfProperty[schemaorg.MediaManipulationRatingEnumeration]
):
    term = RdfTerm(
        "http://schema.org/mediaAuthenticityCategory", "mediaAuthenticityCategory"
    )


class abridged(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/abridged", "abridged")


class predecessorOf(RdfProperty[schemaorg.ProductModel]):
    term = RdfTerm("http://schema.org/predecessorOf", "predecessorOf")


class healthPlanNetworkTier(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/healthPlanNetworkTier", "healthPlanNetworkTier")


class readBy(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/readBy", "readBy")


class merchantReturnLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/merchantReturnLink", "merchantReturnLink")


class primaryImageOfPage(RdfProperty[schemaorg.ImageObject]):
    term = RdfTerm("http://schema.org/primaryImageOfPage", "primaryImageOfPage")


class fulfillmentType(RdfProperty[schemaorg.FulfillmentTypeEnumeration]):
    term = RdfTerm("http://schema.org/fulfillmentType", "fulfillmentType")


class productSupported(RdfProperty[schemaorg.Text | schemaorg.Product]):
    term = RdfTerm("http://schema.org/productSupported", "productSupported")


class fileFormat(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/fileFormat", "fileFormat")


class borrower(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/borrower", "borrower")


class spatialCoverage(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/spatialCoverage", "spatialCoverage")


class permissionType(RdfProperty[schemaorg.DigitalDocumentPermissionType]):
    term = RdfTerm("http://schema.org/permissionType", "permissionType")


class wordCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/wordCount", "wordCount")


class eligibleCustomerType(RdfProperty[schemaorg.BusinessEntityType]):
    term = RdfTerm("http://schema.org/eligibleCustomerType", "eligibleCustomerType")


class usesHealthPlanIdStandard(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/usesHealthPlanIdStandard", "usesHealthPlanIdStandard"
    )


class isAccessibleForFree(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isAccessibleForFree", "isAccessibleForFree")


class availableChannel(RdfProperty[schemaorg.ServiceChannel]):
    term = RdfTerm("http://schema.org/availableChannel", "availableChannel")


class cvdNumC19OFMechVentPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm(
        "http://schema.org/cvdNumC19OFMechVentPats", "cvdNumC19OFMechVentPats"
    )


class isAccessoryOrSparePartFor(RdfProperty[schemaorg.Product]):
    term = RdfTerm(
        "http://schema.org/isAccessoryOrSparePartFor", "isAccessoryOrSparePartFor"
    )


class taxID(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/taxID", "taxID")


class contentReferenceTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/contentReferenceTime", "contentReferenceTime")


class evidenceLevel(RdfProperty[schemaorg.MedicalEvidenceLevel]):
    term = RdfTerm("http://schema.org/evidenceLevel", "evidenceLevel")


class liveBlogUpdate(RdfProperty[schemaorg.BlogPosting]):
    term = RdfTerm("http://schema.org/liveBlogUpdate", "liveBlogUpdate")


class algorithm(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/algorithm", "algorithm")


class validFor(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/validFor", "validFor")


class infectiousAgentClass(RdfProperty[schemaorg.InfectiousAgentClass]):
    term = RdfTerm("http://schema.org/infectiousAgentClass", "infectiousAgentClass")


class vendor(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/vendor", "vendor")


class serviceType(RdfProperty[schemaorg.GovernmentBenefitsType | schemaorg.Text]):
    term = RdfTerm("http://schema.org/serviceType", "serviceType")


class recognizingAuthority(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/recognizingAuthority", "recognizingAuthority")


class typicalCreditsPerTerm(RdfProperty[schemaorg.Integer | schemaorg.StructuredValue]):
    term = RdfTerm("http://schema.org/typicalCreditsPerTerm", "typicalCreditsPerTerm")


class vehicleEngine(RdfProperty[schemaorg.EngineSpecification]):
    term = RdfTerm("http://schema.org/vehicleEngine", "vehicleEngine")


class partOfSeries(RdfProperty[schemaorg.CreativeWorkSeries]):
    term = RdfTerm("http://schema.org/partOfSeries", "partOfSeries")


class bookingAgent(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/bookingAgent", "bookingAgent")


class hasMerchantReturnPolicy(RdfProperty[schemaorg.MerchantReturnPolicy]):
    term = RdfTerm(
        "http://schema.org/hasMerchantReturnPolicy", "hasMerchantReturnPolicy"
    )


class reservationStatus(RdfProperty[schemaorg.ReservationStatusType]):
    term = RdfTerm("http://schema.org/reservationStatus", "reservationStatus")


class paymentDueDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/paymentDueDate", "paymentDueDate")


class nextItem(RdfProperty[schemaorg.ListItem]):
    term = RdfTerm("http://schema.org/nextItem", "nextItem")


class underName(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/underName", "underName")


class estimatedCost(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Text]):
    term = RdfTerm("http://schema.org/estimatedCost", "estimatedCost")


class legalAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm("http://schema.org/legalAddress", "legalAddress")


class runtime(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/runtime", "runtime")


class offeredBy(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/offeredBy", "offeredBy")


class hasDefinedTerm(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/hasDefinedTerm", "hasDefinedTerm")


class bioChemSimilarity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm("http://schema.org/bioChemSimilarity", "bioChemSimilarity")


class qualifications(
    RdfProperty[schemaorg.EducationalOccupationalCredential | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/qualifications", "qualifications")


class greater(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm("http://schema.org/greater", "greater")


class legislationDateVersion(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/legislationDateVersion", "legislationDateVersion")


class recordLabel(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/recordLabel", "recordLabel")


class includedComposition(RdfProperty[schemaorg.MusicComposition]):
    term = RdfTerm("http://schema.org/includedComposition", "includedComposition")


class securityScreening(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/securityScreening", "securityScreening")


class correctionsPolicy(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/correctionsPolicy", "correctionsPolicy")


class proficiencyLevel(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/proficiencyLevel", "proficiencyLevel")


class itinerary(RdfProperty[schemaorg.ItemList | schemaorg.Place]):
    term = RdfTerm("http://schema.org/itinerary", "itinerary")


class suitableForDiet(RdfProperty[schemaorg.RestrictedDiet]):
    term = RdfTerm("http://schema.org/suitableForDiet", "suitableForDiet")


class postalCodeRange(RdfProperty[schemaorg.PostalCodeRangeSpecification]):
    term = RdfTerm("http://schema.org/postalCodeRange", "postalCodeRange")


class reservationFor(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/reservationFor", "reservationFor")


class children(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/children", "children")


class broadcastServiceTier(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/broadcastServiceTier", "broadcastServiceTier")


class transcript(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/transcript", "transcript")


class percentile10(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/percentile10", "percentile10")


class position(RdfProperty[schemaorg.Text | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/position", "position")


class repetitions(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm("http://schema.org/repetitions", "repetitions")


class geographicArea(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm("http://schema.org/geographicArea", "geographicArea")


class activityDuration(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Duration]):
    term = RdfTerm("http://schema.org/activityDuration", "activityDuration")


class significantLinks(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/significantLinks", "significantLinks")


class hasGS1DigitalLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/hasGS1DigitalLink", "hasGS1DigitalLink")


class targetCollection(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/targetCollection", "targetCollection")


class exampleOfWork(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/exampleOfWork", "exampleOfWork")


class makesOffer(RdfProperty[schemaorg.Offer]):
    term = RdfTerm("http://schema.org/makesOffer", "makesOffer")


class maxValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/maxValue", "maxValue")


class verificationFactCheckingPolicy(
    RdfProperty[schemaorg.CreativeWork | schemaorg.URL]
):
    term = RdfTerm(
        "http://schema.org/verificationFactCheckingPolicy",
        "verificationFactCheckingPolicy",
    )


class datePublished(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/datePublished", "datePublished")


class passengerPriorityStatus(RdfProperty[schemaorg.QualitativeValue | schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/passengerPriorityStatus", "passengerPriorityStatus"
    )


class scheduleTimezone(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/scheduleTimezone", "scheduleTimezone")


class additionalNumberOfGuests(RdfProperty[schemaorg.Number]):
    term = RdfTerm(
        "http://schema.org/additionalNumberOfGuests", "additionalNumberOfGuests"
    )


class observationPeriod(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/observationPeriod", "observationPeriod")


class hasMenuSection(RdfProperty[schemaorg.MenuSection]):
    term = RdfTerm("http://schema.org/hasMenuSection", "hasMenuSection")


class shippingLabel(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/shippingLabel", "shippingLabel")


class material(RdfProperty[schemaorg.Product | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/material", "material")


class departurePlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/departurePlatform", "departurePlatform")


class parentOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/parentOrganization", "parentOrganization")


class producer(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/producer", "producer")


class recipe(RdfProperty[schemaorg.Recipe]):
    term = RdfTerm("http://schema.org/recipe", "recipe")


class menuAddOn(RdfProperty[schemaorg.MenuItem | schemaorg.MenuSection]):
    term = RdfTerm("http://schema.org/menuAddOn", "menuAddOn")


class dataset(RdfProperty[schemaorg.Dataset]):
    term = RdfTerm("http://schema.org/dataset", "dataset")


class valueReference(
    RdfProperty[
        schemaorg.QualitativeValue
        | schemaorg.Text
        | schemaorg.DefinedTerm
        | schemaorg.MeasurementTypeEnumeration
        | schemaorg.Enumeration
        | schemaorg.PropertyValue
        | schemaorg.StructuredValue
        | schemaorg.QuantitativeValue
    ]
):
    term = RdfTerm("http://schema.org/valueReference", "valueReference")


class associatedClaimReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm("http://schema.org/associatedClaimReview", "associatedClaimReview")


class referee(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/referee", "referee")


class abstract(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/abstract", "abstract")


class softwareRequirements(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/softwareRequirements", "softwareRequirements")


class frequency(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/frequency", "frequency")


class duplicateTherapy(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm("http://schema.org/duplicateTherapy", "duplicateTherapy")


class acquireLicensePage(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/acquireLicensePage", "acquireLicensePage")


class customerRemorseReturnShippingFeesAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm(
        "http://schema.org/customerRemorseReturnShippingFeesAmount",
        "customerRemorseReturnShippingFeesAmount",
    )


class nerveMotor(RdfProperty[schemaorg.Muscle]):
    term = RdfTerm("http://schema.org/nerveMotor", "nerveMotor")


class hasMemberProgram(RdfProperty[schemaorg.MemberProgram]):
    term = RdfTerm("http://schema.org/hasMemberProgram", "hasMemberProgram")


class healthPlanCopayOption(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/healthPlanCopayOption", "healthPlanCopayOption")


class phoneticText(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/phoneticText", "phoneticText")


class experienceInPlaceOfEducation(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm(
        "http://schema.org/experienceInPlaceOfEducation", "experienceInPlaceOfEducation"
    )


class interactionService(
    RdfProperty[schemaorg.WebSite | schemaorg.SoftwareApplication]
):
    term = RdfTerm("http://schema.org/interactionService", "interactionService")


class connectedTo(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/connectedTo", "connectedTo")


class partySize(RdfProperty[schemaorg.Integer | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/partySize", "partySize")


class actionPlatform(
    RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.DigitalPlatformEnumeration]
):
    term = RdfTerm("http://schema.org/actionPlatform", "actionPlatform")


class runtimePlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/runtimePlatform", "runtimePlatform")


class hasOccupation(RdfProperty[schemaorg.Occupation]):
    term = RdfTerm("http://schema.org/hasOccupation", "hasOccupation")


class median(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/median", "median")


class ratingValue(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/ratingValue", "ratingValue")


class includesHealthPlanFormulary(RdfProperty[schemaorg.HealthPlanFormulary]):
    term = RdfTerm(
        "http://schema.org/includesHealthPlanFormulary", "includesHealthPlanFormulary"
    )


class slogan(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/slogan", "slogan")


class medicineSystem(RdfProperty[schemaorg.MedicineSystem]):
    term = RdfTerm("http://schema.org/medicineSystem", "medicineSystem")


class courseSchedule(RdfProperty[schemaorg.Schedule]):
    term = RdfTerm("http://schema.org/courseSchedule", "courseSchedule")


class vehicleTransmission(
    RdfProperty[schemaorg.QualitativeValue | schemaorg.Text | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/vehicleTransmission", "vehicleTransmission")


class diseasePreventionInfo(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm("http://schema.org/diseasePreventionInfo", "diseasePreventionInfo")


class accountId(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accountId", "accountId")


class userInteractionCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/userInteractionCount", "userInteractionCount")


class accountMinimumInflow(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/accountMinimumInflow", "accountMinimumInflow")


class claimReviewed(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/claimReviewed", "claimReviewed")


class dateDeleted(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/dateDeleted", "dateDeleted")


class releaseNotes(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/releaseNotes", "releaseNotes")


class serviceOperator(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/serviceOperator", "serviceOperator")


class loanTerm(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/loanTerm", "loanTerm")


class returnMethod(RdfProperty[schemaorg.ReturnMethodEnumeration]):
    term = RdfTerm("http://schema.org/returnMethod", "returnMethod")


class eligibleWithSupplier(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/eligibleWithSupplier", "eligibleWithSupplier")


class passengerSequenceNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/passengerSequenceNumber", "passengerSequenceNumber"
    )


class roofLoad(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/roofLoad", "roofLoad")


class quarantineGuidelines(RdfProperty[schemaorg.WebContent | schemaorg.URL]):
    term = RdfTerm("http://schema.org/quarantineGuidelines", "quarantineGuidelines")


class billingDuration(
    RdfProperty[schemaorg.Duration | schemaorg.Number | schemaorg.QuantitativeValue]
):
    term = RdfTerm("http://schema.org/billingDuration", "billingDuration")


class usageInfo(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/usageInfo", "usageInfo")


class reportNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/reportNumber", "reportNumber")


class contactPoint(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm("http://schema.org/contactPoint", "contactPoint")


class query(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/query", "query")


class location(
    RdfProperty[
        schemaorg.VirtualLocation
        | schemaorg.PostalAddress
        | schemaorg.Place
        | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/location", "location")


class birthPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/birthPlace", "birthPlace")


class yearsInOperation(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/yearsInOperation", "yearsInOperation")


class playerType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/playerType", "playerType")


class valueName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/valueName", "valueName")


class downvoteCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/downvoteCount", "downvoteCount")


class payload(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/payload", "payload")


class orderItemStatus(RdfProperty[schemaorg.OrderStatus]):
    term = RdfTerm("http://schema.org/orderItemStatus", "orderItemStatus")


class cvdNumC19HospPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumC19HospPats", "cvdNumC19HospPats")


class processorRequirements(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/processorRequirements", "processorRequirements")


class expires(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm("http://schema.org/expires", "expires")


class vehicleIdentificationNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/vehicleIdentificationNumber", "vehicleIdentificationNumber"
    )


class alignmentType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/alignmentType", "alignmentType")


class startOffset(RdfProperty[schemaorg.Number | schemaorg.HyperTocEntry]):
    term = RdfTerm("http://schema.org/startOffset", "startOffset")


class mainEntity(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/mainEntity", "mainEntity")


class numAdults(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numAdults", "numAdults")


class gameItem(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/gameItem", "gameItem")


class ownedThrough(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/ownedThrough", "ownedThrough")


class instrument(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/instrument", "instrument")


class rxcui(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/rxcui", "rxcui")


class administrationRoute(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/administrationRoute", "administrationRoute")


class earlyPrepaymentPenalty(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/earlyPrepaymentPenalty", "earlyPrepaymentPenalty")


class gtin(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/gtin", "gtin")


class carbohydrateContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/carbohydrateContent", "carbohydrateContent")


class previousStartDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/previousStartDate", "previousStartDate")


class broker(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/broker", "broker")


class partOfEpisode(RdfProperty[schemaorg.Episode]):
    term = RdfTerm("http://schema.org/partOfEpisode", "partOfEpisode")


class width(RdfProperty[schemaorg.Distance | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/width", "width")


class cookTime(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/cookTime", "cookTime")


class serviceAudience(RdfProperty[schemaorg.Audience]):
    term = RdfTerm("http://schema.org/serviceAudience", "serviceAudience")


class availabilityEnds(
    RdfProperty[schemaorg.Date | schemaorg.DateTime | schemaorg.Time]
):
    term = RdfTerm("http://schema.org/availabilityEnds", "availabilityEnds")


class maps(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/maps", "maps")


class postalCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/postalCode", "postalCode")


class qualifiedExpense(RdfProperty[schemaorg.IncentiveQualifiedExpenseType]):
    term = RdfTerm("http://schema.org/qualifiedExpense", "qualifiedExpense")


class actionApplication(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm("http://schema.org/actionApplication", "actionApplication")


class copyrightHolder(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/copyrightHolder", "copyrightHolder")


class requiredCollateral(RdfProperty[schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm("http://schema.org/requiredCollateral", "requiredCollateral")


class supportingData(RdfProperty[schemaorg.DataFeed]):
    term = RdfTerm("http://schema.org/supportingData", "supportingData")


class numberOfEpisodes(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numberOfEpisodes", "numberOfEpisodes")


class recourseLoan(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/recourseLoan", "recourseLoan")


class inAlbum(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm("http://schema.org/inAlbum", "inAlbum")


class expectedPrognosis(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/expectedPrognosis", "expectedPrognosis")


class departureBusStop(RdfProperty[schemaorg.BusStop | schemaorg.BusStation]):
    term = RdfTerm("http://schema.org/departureBusStop", "departureBusStop")


class alternativeHeadline(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/alternativeHeadline", "alternativeHeadline")


class signDetected(RdfProperty[schemaorg.MedicalSign]):
    term = RdfTerm("http://schema.org/signDetected", "signDetected")


class numberOfRooms(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfRooms", "numberOfRooms")


class requiredMinAge(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/requiredMinAge", "requiredMinAge")


class dateIssued(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm("http://schema.org/dateIssued", "dateIssued")


class customerRemorseReturnLabelSource(
    RdfProperty[schemaorg.ReturnLabelSourceEnumeration]
):
    term = RdfTerm(
        "http://schema.org/customerRemorseReturnLabelSource",
        "customerRemorseReturnLabelSource",
    )


class providesBroadcastService(RdfProperty[schemaorg.BroadcastService]):
    term = RdfTerm(
        "http://schema.org/providesBroadcastService", "providesBroadcastService"
    )


class variableMeasured(
    RdfProperty[
        schemaorg.Property
        | schemaorg.StatisticalVariable
        | schemaorg.PropertyValue
        | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/variableMeasured", "variableMeasured")


class creator(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/creator", "creator")


class coursePrerequisites(
    RdfProperty[schemaorg.AlignmentObject | schemaorg.Course | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/coursePrerequisites", "coursePrerequisites")


class discount(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/discount", "discount")


class musicBy(RdfProperty[schemaorg.MusicGroup | schemaorg.Person]):
    term = RdfTerm("http://schema.org/musicBy", "musicBy")


class prescriptionStatus(
    RdfProperty[schemaorg.Text | schemaorg.DrugPrescriptionStatus]
):
    term = RdfTerm("http://schema.org/prescriptionStatus", "prescriptionStatus")


class trainName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/trainName", "trainName")


class grantee(
    RdfProperty[
        schemaorg.Audience
        | schemaorg.Organization
        | schemaorg.ContactPoint
        | schemaorg.Person
    ]
):
    term = RdfTerm("http://schema.org/grantee", "grantee")


class smokingAllowed(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/smokingAllowed", "smokingAllowed")


class intensity(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/intensity", "intensity")


class partOfSystem(RdfProperty[schemaorg.AnatomicalSystem]):
    term = RdfTerm("http://schema.org/partOfSystem", "partOfSystem")


class foodEstablishment(RdfProperty[schemaorg.Place | schemaorg.FoodEstablishment]):
    term = RdfTerm("http://schema.org/foodEstablishment", "foodEstablishment")


class dateVehicleFirstRegistered(RdfProperty[schemaorg.Date]):
    term = RdfTerm(
        "http://schema.org/dateVehicleFirstRegistered", "dateVehicleFirstRegistered"
    )


class observationDate(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/observationDate", "observationDate")


class startDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/startDate", "startDate")


class countryOfOrigin(RdfProperty[schemaorg.Country]):
    term = RdfTerm("http://schema.org/countryOfOrigin", "countryOfOrigin")


class practicesAt(RdfProperty[schemaorg.MedicalOrganization]):
    term = RdfTerm("http://schema.org/practicesAt", "practicesAt")


class courseWorkload(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/courseWorkload", "courseWorkload")


class healthPlanCoinsuranceRate(RdfProperty[schemaorg.Number]):
    term = RdfTerm(
        "http://schema.org/healthPlanCoinsuranceRate", "healthPlanCoinsuranceRate"
    )


class foodEvent(RdfProperty[schemaorg.FoodEvent]):
    term = RdfTerm("http://schema.org/foodEvent", "foodEvent")


class mediaItemAppearance(RdfProperty[schemaorg.MediaObject]):
    term = RdfTerm("http://schema.org/mediaItemAppearance", "mediaItemAppearance")


class expertConsiderations(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/expertConsiderations", "expertConsiderations")


class priceSpecification(RdfProperty[schemaorg.PriceSpecification]):
    term = RdfTerm("http://schema.org/priceSpecification", "priceSpecification")


class returnFees(RdfProperty[schemaorg.ReturnFeesEnumeration]):
    term = RdfTerm("http://schema.org/returnFees", "returnFees")


class teaches(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/teaches", "teaches")


class diet(RdfProperty[schemaorg.Diet]):
    term = RdfTerm("http://schema.org/diet", "diet")


class hasTierRequirement(
    RdfProperty[
        schemaorg.CreditCard
        | schemaorg.MonetaryAmount
        | schemaorg.UnitPriceSpecification
        | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/hasTierRequirement", "hasTierRequirement")


class rsvpResponse(RdfProperty[schemaorg.RsvpResponseType]):
    term = RdfTerm("http://schema.org/rsvpResponse", "rsvpResponse")


class hasAdultConsideration(RdfProperty[schemaorg.AdultOrientedEnumeration]):
    term = RdfTerm("http://schema.org/hasAdultConsideration", "hasAdultConsideration")


class gameLocation(
    RdfProperty[schemaorg.URL | schemaorg.Place | schemaorg.PostalAddress]
):
    term = RdfTerm("http://schema.org/gameLocation", "gameLocation")


class pagination(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/pagination", "pagination")


class issueNumber(RdfProperty[schemaorg.Text | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/issueNumber", "issueNumber")


class hasTiers(RdfProperty[schemaorg.MemberProgramTier]):
    term = RdfTerm("http://schema.org/hasTiers", "hasTiers")


class workPresented(RdfProperty[schemaorg.Movie]):
    term = RdfTerm("http://schema.org/workPresented", "workPresented")


class commentTime(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm("http://schema.org/commentTime", "commentTime")


class occupationalCredentialAwarded(
    RdfProperty[
        schemaorg.EducationalOccupationalCredential | schemaorg.Text | schemaorg.URL
    ]
):
    term = RdfTerm(
        "http://schema.org/occupationalCredentialAwarded",
        "occupationalCredentialAwarded",
    )


class itemDefectReturnLabelSource(RdfProperty[schemaorg.ReturnLabelSourceEnumeration]):
    term = RdfTerm(
        "http://schema.org/itemDefectReturnLabelSource", "itemDefectReturnLabelSource"
    )


class geoMidpoint(RdfProperty[schemaorg.GeoCoordinates]):
    term = RdfTerm("http://schema.org/geoMidpoint", "geoMidpoint")


class layoutImage(RdfProperty[schemaorg.URL | schemaorg.ImageObject]):
    term = RdfTerm("http://schema.org/layoutImage", "layoutImage")


class subStageSuffix(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/subStageSuffix", "subStageSuffix")


class sku(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/sku", "sku")


class breadcrumb(RdfProperty[schemaorg.BreadcrumbList | schemaorg.Text]):
    term = RdfTerm("http://schema.org/breadcrumb", "breadcrumb")


class model(RdfProperty[schemaorg.ProductModel | schemaorg.Text]):
    term = RdfTerm("http://schema.org/model", "model")


class educationalLevel(
    RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.DefinedTerm]
):
    term = RdfTerm("http://schema.org/educationalLevel", "educationalLevel")


class engineType(
    RdfProperty[schemaorg.QualitativeValue | schemaorg.Text | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/engineType", "engineType")


class quest(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/quest", "quest")


class certificationStatus(RdfProperty[schemaorg.CertificationStatusEnumeration]):
    term = RdfTerm("http://schema.org/certificationStatus", "certificationStatus")


class includedRiskFactor(RdfProperty[schemaorg.MedicalRiskFactor]):
    term = RdfTerm("http://schema.org/includedRiskFactor", "includedRiskFactor")


class organizer(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/organizer", "organizer")


class pageEnd(RdfProperty[schemaorg.Text | schemaorg.Integer]):
    term = RdfTerm("http://schema.org/pageEnd", "pageEnd")


class item(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/item", "item")


class negativeNotes(
    RdfProperty[
        schemaorg.ListItem | schemaorg.WebContent | schemaorg.ItemList | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/negativeNotes", "negativeNotes")


class inStoreReturnsOffered(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/inStoreReturnsOffered", "inStoreReturnsOffered")


class followup(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/followup", "followup")


class cvdNumBedsOcc(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumBedsOcc", "cvdNumBedsOcc")


class possibleTreatment(RdfProperty[schemaorg.MedicalTherapy]):
    term = RdfTerm("http://schema.org/possibleTreatment", "possibleTreatment")


class driveWheelConfiguration(
    RdfProperty[schemaorg.DriveWheelConfigurationValue | schemaorg.Text]
):
    term = RdfTerm(
        "http://schema.org/driveWheelConfiguration", "driveWheelConfiguration"
    )


class sibling(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/sibling", "sibling")


class seatingType(RdfProperty[schemaorg.QualitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/seatingType", "seatingType")


class codeRepository(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/codeRepository", "codeRepository")


class digitalSourceType(RdfProperty[schemaorg.IPTCDigitalSourceEnumeration]):
    term = RdfTerm("http://schema.org/digitalSourceType", "digitalSourceType")


class healthCondition(RdfProperty[schemaorg.MedicalCondition]):
    term = RdfTerm("http://schema.org/healthCondition", "healthCondition")


class minPrice(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/minPrice", "minPrice")


class relevantOccupation(RdfProperty[schemaorg.Occupation]):
    term = RdfTerm("http://schema.org/relevantOccupation", "relevantOccupation")


class vatID(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/vatID", "vatID")


class potentialUse(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/potentialUse", "potentialUse")


class commentText(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/commentText", "commentText")


class workPerformed(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/workPerformed", "workPerformed")


class legislationConsolidates(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm(
        "http://schema.org/legislationConsolidates", "legislationConsolidates"
    )


class customerRemorseReturnFees(RdfProperty[schemaorg.ReturnFeesEnumeration]):
    term = RdfTerm(
        "http://schema.org/customerRemorseReturnFees", "customerRemorseReturnFees"
    )


class speechToTextMarkup(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/speechToTextMarkup", "speechToTextMarkup")


class dietFeatures(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/dietFeatures", "dietFeatures")


class recordedAt(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/recordedAt", "recordedAt")


class subReservation(RdfProperty[schemaorg.Reservation]):
    term = RdfTerm("http://schema.org/subReservation", "subReservation")


class seeks(RdfProperty[schemaorg.Demand]):
    term = RdfTerm("http://schema.org/seeks", "seeks")


class feesAndCommissionsSpecification(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm(
        "http://schema.org/feesAndCommissionsSpecification",
        "feesAndCommissionsSpecification",
    )


class benefitsSummaryUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/benefitsSummaryUrl", "benefitsSummaryUrl")


class endTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/endTime", "endTime")


class category(
    RdfProperty[
        schemaorg.Thing
        | schemaorg.PhysicalActivityCategory
        | schemaorg.Text
        | schemaorg.URL
        | schemaorg.CategoryCode
    ]
):
    term = RdfTerm("http://schema.org/category", "category")


class learningResourceType(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/learningResourceType", "learningResourceType")


class yearlyRevenue(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/yearlyRevenue", "yearlyRevenue")


class courseCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/courseCode", "courseCode")


class resultReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm("http://schema.org/resultReview", "resultReview")


class assembly(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/assembly", "assembly")


class variantCover(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/variantCover", "variantCover")


class hasCategoryCode(RdfProperty[schemaorg.CategoryCode]):
    term = RdfTerm("http://schema.org/hasCategoryCode", "hasCategoryCode")


class constraintProperty(RdfProperty[schemaorg.Property | schemaorg.URL]):
    term = RdfTerm("http://schema.org/constraintProperty", "constraintProperty")


class screenCount(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/screenCount", "screenCount")


class workTranslation(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/workTranslation", "workTranslation")


class busName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/busName", "busName")


class orderValue(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/orderValue", "orderValue")


class currentExchangeRate(RdfProperty[schemaorg.UnitPriceSpecification]):
    term = RdfTerm("http://schema.org/currentExchangeRate", "currentExchangeRate")


class result(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/result", "result")


class mathExpression(RdfProperty[schemaorg.SolveMathAction | schemaorg.Text]):
    term = RdfTerm("http://schema.org/mathExpression", "mathExpression")


class fiberContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/fiberContent", "fiberContent")


class isBasedOnUrl(
    RdfProperty[schemaorg.CreativeWork | schemaorg.Product | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/isBasedOnUrl", "isBasedOnUrl")


class drugUnit(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/drugUnit", "drugUnit")


class error(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/error", "error")


class originAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm("http://schema.org/originAddress", "originAddress")


class maximumEnrollment(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/maximumEnrollment", "maximumEnrollment")


class orderDate(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm("http://schema.org/orderDate", "orderDate")


class gameEdition(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/gameEdition", "gameEdition")


class imagingTechnique(RdfProperty[schemaorg.MedicalImagingTechnique]):
    term = RdfTerm("http://schema.org/imagingTechnique", "imagingTechnique")


class reviewedBy(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/reviewedBy", "reviewedBy")


class inDefinedTermSet(RdfProperty[schemaorg.DefinedTermSet | schemaorg.URL]):
    term = RdfTerm("http://schema.org/inDefinedTermSet", "inDefinedTermSet")


class functionalClass(RdfProperty[schemaorg.Text | schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/functionalClass", "functionalClass")


class publisherImprint(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/publisherImprint", "publisherImprint")


class ratingCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/ratingCount", "ratingCount")


class speakable(RdfProperty[schemaorg.SpeakableSpecification | schemaorg.URL]):
    term = RdfTerm("http://schema.org/speakable", "speakable")


class incentiveAmount(
    RdfProperty[
        schemaorg.QuantitativeValue
        | schemaorg.UnitPriceSpecification
        | schemaorg.LoanOrCredit
    ]
):
    term = RdfTerm("http://schema.org/incentiveAmount", "incentiveAmount")


class meetsEmissionStandard(
    RdfProperty[schemaorg.QualitativeValue | schemaorg.Text | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/meetsEmissionStandard", "meetsEmissionStandard")


class geo(RdfProperty[schemaorg.GeoShape | schemaorg.GeoCoordinates]):
    term = RdfTerm("http://schema.org/geo", "geo")


class timeToComplete(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/timeToComplete", "timeToComplete")


class observationAbout(RdfProperty[schemaorg.Place | schemaorg.Thing]):
    term = RdfTerm("http://schema.org/observationAbout", "observationAbout")


class sponsor(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/sponsor", "sponsor")


class costOrigin(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/costOrigin", "costOrigin")


class fromLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/fromLocation", "fromLocation")


class shippingDetails(RdfProperty[schemaorg.OfferShippingDetails]):
    term = RdfTerm("http://schema.org/shippingDetails", "shippingDetails")


class applicableLocation(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm("http://schema.org/applicableLocation", "applicableLocation")


class replyToUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/replyToUrl", "replyToUrl")


class hasBroadcastChannel(RdfProperty[schemaorg.BroadcastChannel]):
    term = RdfTerm("http://schema.org/hasBroadcastChannel", "hasBroadcastChannel")


class partOfSeason(RdfProperty[schemaorg.CreativeWorkSeason]):
    term = RdfTerm("http://schema.org/partOfSeason", "partOfSeason")


class applicationDeadline(RdfProperty[schemaorg.Date | schemaorg.Text]):
    term = RdfTerm("http://schema.org/applicationDeadline", "applicationDeadline")


class relatedTo(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/relatedTo", "relatedTo")


class sport(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/sport", "sport")


class unitCode(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/unitCode", "unitCode")


class artworkSurface(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/artworkSurface", "artworkSurface")


class availableLanguage(RdfProperty[schemaorg.Text | schemaorg.Language]):
    term = RdfTerm("http://schema.org/availableLanguage", "availableLanguage")


class knows(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/knows", "knows")


class creativeWorkStatus(RdfProperty[schemaorg.Text | schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/creativeWorkStatus", "creativeWorkStatus")


class spouse(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/spouse", "spouse")


class eventAttendanceMode(RdfProperty[schemaorg.EventAttendanceModeEnumeration]):
    term = RdfTerm("http://schema.org/eventAttendanceMode", "eventAttendanceMode")


class checkoutTime(RdfProperty[schemaorg.DateTime | schemaorg.Time]):
    term = RdfTerm("http://schema.org/checkoutTime", "checkoutTime")


class audience(RdfProperty[schemaorg.Audience]):
    term = RdfTerm("http://schema.org/audience", "audience")


class broadcastSignalModulation(
    RdfProperty[schemaorg.QualitativeValue | schemaorg.Text]
):
    term = RdfTerm(
        "http://schema.org/broadcastSignalModulation", "broadcastSignalModulation"
    )


class numberOfBathroomsTotal(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numberOfBathroomsTotal", "numberOfBathroomsTotal")


class thumbnailUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/thumbnailUrl", "thumbnailUrl")


class timeOfDay(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/timeOfDay", "timeOfDay")


class programMembershipUsed(RdfProperty[schemaorg.ProgramMembership]):
    term = RdfTerm("http://schema.org/programMembershipUsed", "programMembershipUsed")


class code(RdfProperty[schemaorg.MedicalCode]):
    term = RdfTerm("http://schema.org/code", "code")


class annualPercentageRate(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/annualPercentageRate", "annualPercentageRate")


class masthead(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("http://schema.org/masthead", "masthead")


class hostingOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/hostingOrganization", "hostingOrganization")


class sampleType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/sampleType", "sampleType")


class honorificSuffix(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/honorificSuffix", "honorificSuffix")


class subEvents(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/subEvents", "subEvents")


class nationality(RdfProperty[schemaorg.Country]):
    term = RdfTerm("http://schema.org/nationality", "nationality")


class valueAddedTaxIncluded(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/valueAddedTaxIncluded", "valueAddedTaxIncluded")


class vehicleSpecialUsage(RdfProperty[schemaorg.Text | schemaorg.CarUsageType]):
    term = RdfTerm("http://schema.org/vehicleSpecialUsage", "vehicleSpecialUsage")


class repeatFrequency(RdfProperty[schemaorg.Text | schemaorg.Duration]):
    term = RdfTerm("http://schema.org/repeatFrequency", "repeatFrequency")


class dropoffLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/dropoffLocation", "dropoffLocation")


class legalStatus(
    RdfProperty[
        schemaorg.MedicalEnumeration | schemaorg.DrugLegalStatus | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/legalStatus", "legalStatus")


class geoWithin(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm("http://schema.org/geoWithin", "geoWithin")


class representativeOfPage(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/representativeOfPage", "representativeOfPage")


class volumeNumber(RdfProperty[schemaorg.Integer | schemaorg.Text]):
    term = RdfTerm("http://schema.org/volumeNumber", "volumeNumber")


class amenityFeature(RdfProperty[schemaorg.LocationFeatureSpecification]):
    term = RdfTerm("http://schema.org/amenityFeature", "amenityFeature")


class pregnancyCategory(RdfProperty[schemaorg.DrugPregnancyCategory]):
    term = RdfTerm("http://schema.org/pregnancyCategory", "pregnancyCategory")


class regionsAllowed(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/regionsAllowed", "regionsAllowed")


class incentiveType(RdfProperty[schemaorg.IncentiveType]):
    term = RdfTerm("http://schema.org/incentiveType", "incentiveType")


class orderQuantity(RdfProperty[schemaorg.Number | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/orderQuantity", "orderQuantity")


class maximumVirtualAttendeeCapacity(RdfProperty[schemaorg.Integer]):
    term = RdfTerm(
        "http://schema.org/maximumVirtualAttendeeCapacity",
        "maximumVirtualAttendeeCapacity",
    )


class funder(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/funder", "funder")


class cvdNumC19HOPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumC19HOPats", "cvdNumC19HOPats")


class legislationJurisdiction(
    RdfProperty[schemaorg.Text | schemaorg.AdministrativeArea]
):
    term = RdfTerm(
        "http://schema.org/legislationJurisdiction", "legislationJurisdiction"
    )


class fuelCapacity(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/fuelCapacity", "fuelCapacity")


class dateSent(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/dateSent", "dateSent")


class arrivalTime(RdfProperty[schemaorg.Time | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/arrivalTime", "arrivalTime")


class healthPlanCopay(RdfProperty[schemaorg.PriceSpecification]):
    term = RdfTerm("http://schema.org/healthPlanCopay", "healthPlanCopay")


class physiologicalBenefits(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/physiologicalBenefits", "physiologicalBenefits")


class programmingLanguage(RdfProperty[schemaorg.Text | schemaorg.ComputerLanguage]):
    term = RdfTerm("http://schema.org/programmingLanguage", "programmingLanguage")


class loanType(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/loanType", "loanType")


class sportsEvent(RdfProperty[schemaorg.SportsEvent]):
    term = RdfTerm("http://schema.org/sportsEvent", "sportsEvent")


class targetPopulation(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/targetPopulation", "targetPopulation")


class audienceType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/audienceType", "audienceType")


class arterialBranch(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/arterialBranch", "arterialBranch")


class chemicalComposition(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/chemicalComposition", "chemicalComposition")


class knownVehicleDamages(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/knownVehicleDamages", "knownVehicleDamages")


class occupationLocation(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm("http://schema.org/occupationLocation", "occupationLocation")


class diversityStaffingReport(RdfProperty[schemaorg.Article | schemaorg.URL]):
    term = RdfTerm(
        "http://schema.org/diversityStaffingReport", "diversityStaffingReport"
    )


class lastReviewed(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/lastReviewed", "lastReviewed")


class expectsAcceptanceOf(RdfProperty[schemaorg.Offer]):
    term = RdfTerm("http://schema.org/expectsAcceptanceOf", "expectsAcceptanceOf")


class billingStart(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/billingStart", "billingStart")


class distribution(RdfProperty[schemaorg.DataDownload]):
    term = RdfTerm("http://schema.org/distribution", "distribution")


class inLanguage(RdfProperty[schemaorg.Text | schemaorg.Language]):
    term = RdfTerm("http://schema.org/inLanguage", "inLanguage")


class offerCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/offerCount", "offerCount")


class letterer(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/letterer", "letterer")


class byArtist(RdfProperty[schemaorg.MusicGroup | schemaorg.Person]):
    term = RdfTerm("http://schema.org/byArtist", "byArtist")


class trainingSalary(RdfProperty[schemaorg.MonetaryAmountDistribution]):
    term = RdfTerm("http://schema.org/trainingSalary", "trainingSalary")


class subtitleLanguage(RdfProperty[schemaorg.Language | schemaorg.Text]):
    term = RdfTerm("http://schema.org/subtitleLanguage", "subtitleLanguage")


class diseaseSpreadStatistics(
    RdfProperty[
        schemaorg.URL | schemaorg.Observation | schemaorg.Dataset | schemaorg.WebContent
    ]
):
    term = RdfTerm(
        "http://schema.org/diseaseSpreadStatistics", "diseaseSpreadStatistics"
    )


class drug(RdfProperty[schemaorg.Drug]):
    term = RdfTerm("http://schema.org/drug", "drug")


class attendees(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/attendees", "attendees")


class pickupTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/pickupTime", "pickupTime")


class contentSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/contentSize", "contentSize")


class creditText(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/creditText", "creditText")


class geoOverlaps(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm("http://schema.org/geoOverlaps", "geoOverlaps")


class adverseOutcome(RdfProperty[schemaorg.MedicalEntity]):
    term = RdfTerm("http://schema.org/adverseOutcome", "adverseOutcome")


class warning(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/warning", "warning")


class publishedBy(RdfProperty[schemaorg.Person | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/publishedBy", "publishedBy")


class appliesToDeliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm(
        "http://schema.org/appliesToDeliveryMethod", "appliesToDeliveryMethod"
    )


class petsAllowed(RdfProperty[schemaorg.Boolean | schemaorg.Text]):
    term = RdfTerm("http://schema.org/petsAllowed", "petsAllowed")


class serviceLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/serviceLocation", "serviceLocation")


class trailerWeight(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/trailerWeight", "trailerWeight")


class softwareAddOn(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm("http://schema.org/softwareAddOn", "softwareAddOn")


class cvdNumICUBedsOcc(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumICUBedsOcc", "cvdNumICUBedsOcc")


class endorsers(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/endorsers", "endorsers")


class stepValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/stepValue", "stepValue")


class associatedAnatomy(
    RdfProperty[
        schemaorg.AnatomicalStructure
        | schemaorg.SuperficialAnatomy
        | schemaorg.AnatomicalSystem
    ]
):
    term = RdfTerm("http://schema.org/associatedAnatomy", "associatedAnatomy")


class bookingTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/bookingTime", "bookingTime")


class aircraft(RdfProperty[schemaorg.Vehicle | schemaorg.Text]):
    term = RdfTerm("http://schema.org/aircraft", "aircraft")


class copyrightYear(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/copyrightYear", "copyrightYear")


class price(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/price", "price")


class translationOfWork(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/translationOfWork", "translationOfWork")


class videoFrameSize(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/videoFrameSize", "videoFrameSize")


class associatedReview(RdfProperty[schemaorg.Review]):
    term = RdfTerm("http://schema.org/associatedReview", "associatedReview")


class printEdition(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/printEdition", "printEdition")


class overdosage(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/overdosage", "overdosage")


class sourceOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/sourceOrganization", "sourceOrganization")


class serviceSmsNumber(RdfProperty[schemaorg.ContactPoint]):
    term = RdfTerm("http://schema.org/serviceSmsNumber", "serviceSmsNumber")


class exerciseCourse(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/exerciseCourse", "exerciseCourse")


class bloodSupply(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm("http://schema.org/bloodSupply", "bloodSupply")


class paymentAccepted(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/paymentAccepted", "paymentAccepted")


class announcementLocation(
    RdfProperty[schemaorg.LocalBusiness | schemaorg.CivicStructure]
):
    term = RdfTerm("http://schema.org/announcementLocation", "announcementLocation")


class mapType(RdfProperty[schemaorg.MapCategoryType]):
    term = RdfTerm("http://schema.org/mapType", "mapType")


class warrantyScope(RdfProperty[schemaorg.WarrantyScope]):
    term = RdfTerm("http://schema.org/warrantyScope", "warrantyScope")


class claimInterpreter(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/claimInterpreter", "claimInterpreter")


class locationCreated(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/locationCreated", "locationCreated")


class illustrator(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/illustrator", "illustrator")


class numberOfBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfBeds", "numberOfBeds")


class billingPeriod(RdfProperty[schemaorg.Duration]):
    term = RdfTerm("http://schema.org/billingPeriod", "billingPeriod")


class comprisedOf(
    RdfProperty[schemaorg.AnatomicalStructure | schemaorg.AnatomicalSystem]
):
    term = RdfTerm("http://schema.org/comprisedOf", "comprisedOf")


class birthDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/birthDate", "birthDate")


class accessibilityAPI(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accessibilityAPI", "accessibilityAPI")


class certificationRating(RdfProperty[schemaorg.Rating]):
    term = RdfTerm("http://schema.org/certificationRating", "certificationRating")


class postalCodeBegin(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/postalCodeBegin", "postalCodeBegin")


class acceptedOffer(RdfProperty[schemaorg.Offer]):
    term = RdfTerm("http://schema.org/acceptedOffer", "acceptedOffer")


class videoFormat(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/videoFormat", "videoFormat")


class weightTotal(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/weightTotal", "weightTotal")


class mainEntityOfPage(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/mainEntityOfPage", "mainEntityOfPage")


class acrissCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/acrissCode", "acrissCode")


class deliveryAddress(RdfProperty[schemaorg.PostalAddress]):
    term = RdfTerm("http://schema.org/deliveryAddress", "deliveryAddress")


class companyRegistration(RdfProperty[schemaorg.Certification]):
    term = RdfTerm("http://schema.org/companyRegistration", "companyRegistration")


class ownedFrom(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/ownedFrom", "ownedFrom")


class broadcastSubChannel(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/broadcastSubChannel", "broadcastSubChannel")


class isResizable(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isResizable", "isResizable")


class stupidProperty(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/stupidProperty", "stupidProperty")


class gtin14(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/gtin14", "gtin14")


class sizeSystem(RdfProperty[schemaorg.Text | schemaorg.SizeSystemEnumeration]):
    term = RdfTerm("http://schema.org/sizeSystem", "sizeSystem")


class suggestedMinAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/suggestedMinAge", "suggestedMinAge")


class numberOfAirbags(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfAirbags", "numberOfAirbags")


class broadcastChannelId(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/broadcastChannelId", "broadcastChannelId")


class tocEntry(RdfProperty[schemaorg.HyperTocEntry]):
    term = RdfTerm("http://schema.org/tocEntry", "tocEntry")


class governmentBenefitsInfo(RdfProperty[schemaorg.GovernmentService]):
    term = RdfTerm("http://schema.org/governmentBenefitsInfo", "governmentBenefitsInfo")


class educationRequirements(
    RdfProperty[schemaorg.Text | schemaorg.EducationalOccupationalCredential]
):
    term = RdfTerm("http://schema.org/educationRequirements", "educationRequirements")


class shippingConditions(RdfProperty[schemaorg.ShippingConditions]):
    term = RdfTerm("http://schema.org/shippingConditions", "shippingConditions")


class exchangeRateSpread(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Number]):
    term = RdfTerm("http://schema.org/exchangeRateSpread", "exchangeRateSpread")


class sourcedFrom(RdfProperty[schemaorg.BrainStructure]):
    term = RdfTerm("http://schema.org/sourcedFrom", "sourcedFrom")


class embeddedTextCaption(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/embeddedTextCaption", "embeddedTextCaption")


class containedIn(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/containedIn", "containedIn")


class programType(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm("http://schema.org/programType", "programType")


class byMonthWeek(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/byMonthWeek", "byMonthWeek")


class competencyRequired(
    RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.DefinedTerm]
):
    term = RdfTerm("http://schema.org/competencyRequired", "competencyRequired")


class incomeLimit(RdfProperty[schemaorg.MonetaryAmount | schemaorg.Text]):
    term = RdfTerm("http://schema.org/incomeLimit", "incomeLimit")


class vehicleConfiguration(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/vehicleConfiguration", "vehicleConfiguration")


class guideline(RdfProperty[schemaorg.MedicalGuideline]):
    term = RdfTerm("http://schema.org/guideline", "guideline")


class cssSelector(RdfProperty[schemaorg.CssSelectorType]):
    term = RdfTerm("http://schema.org/cssSelector", "cssSelector")


class hasRepresentation(
    RdfProperty[schemaorg.PropertyValue | schemaorg.Text | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/hasRepresentation", "hasRepresentation")


class subOrganization(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/subOrganization", "subOrganization")


class participant(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/participant", "participant")


class freeShippingThreshold(
    RdfProperty[schemaorg.DeliveryChargeSpecification | schemaorg.MonetaryAmount]
):
    term = RdfTerm("http://schema.org/freeShippingThreshold", "freeShippingThreshold")


class eventSchedule(RdfProperty[schemaorg.Schedule]):
    term = RdfTerm("http://schema.org/eventSchedule", "eventSchedule")


class estimatedSalary(
    RdfProperty[
        schemaorg.MonetaryAmount
        | schemaorg.MonetaryAmountDistribution
        | schemaorg.Number
    ]
):
    term = RdfTerm("http://schema.org/estimatedSalary", "estimatedSalary")


class hasDriveThroughService(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/hasDriveThroughService", "hasDriveThroughService")


class firstPerformance(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/firstPerformance", "firstPerformance")


class childTaxon(RdfProperty[schemaorg.Taxon | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/childTaxon", "childTaxon")


class agent(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/agent", "agent")


class legislationTransposes(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm("http://schema.org/legislationTransposes", "legislationTransposes")


class backstory(RdfProperty[schemaorg.Text | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/backstory", "backstory")


class identifyingExam(RdfProperty[schemaorg.PhysicalExam]):
    term = RdfTerm("http://schema.org/identifyingExam", "identifyingExam")


class correction(
    RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.CorrectionComment]
):
    term = RdfTerm("http://schema.org/correction", "correction")


class availableOnDevice(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/availableOnDevice", "availableOnDevice")


class sha256(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/sha256", "sha256")


class sharedContent(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/sharedContent", "sharedContent")


class owns(RdfProperty[schemaorg.Product | schemaorg.OwnershipInfo]):
    term = RdfTerm("http://schema.org/owns", "owns")


class box(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/box", "box")


class containsSeason(RdfProperty[schemaorg.CreativeWorkSeason]):
    term = RdfTerm("http://schema.org/containsSeason", "containsSeason")


class missionCoveragePrioritiesPolicy(
    RdfProperty[schemaorg.CreativeWork | schemaorg.URL]
):
    term = RdfTerm(
        "http://schema.org/missionCoveragePrioritiesPolicy",
        "missionCoveragePrioritiesPolicy",
    )


class acceptsReservations(
    RdfProperty[schemaorg.Boolean | schemaorg.Text | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/acceptsReservations", "acceptsReservations")


class depth(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Distance]):
    term = RdfTerm("http://schema.org/depth", "depth")


class doseUnit(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/doseUnit", "doseUnit")


class byDay(RdfProperty[schemaorg.DayOfWeek | schemaorg.Text]):
    term = RdfTerm("http://schema.org/byDay", "byDay")


class albumProductionType(RdfProperty[schemaorg.MusicAlbumProductionType]):
    term = RdfTerm("http://schema.org/albumProductionType", "albumProductionType")


class homeTeam(RdfProperty[schemaorg.Person | schemaorg.SportsTeam]):
    term = RdfTerm("http://schema.org/homeTeam", "homeTeam")


class serialNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/serialNumber", "serialNumber")


class stageAsNumber(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/stageAsNumber", "stageAsNumber")


class accommodationCategory(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accommodationCategory", "accommodationCategory")


class valuePattern(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/valuePattern", "valuePattern")


class strengthValue(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/strengthValue", "strengthValue")


class logo(RdfProperty[schemaorg.URL | schemaorg.ImageObject]):
    term = RdfTerm("http://schema.org/logo", "logo")


class baseSalary(
    RdfProperty[
        schemaorg.PriceSpecification | schemaorg.MonetaryAmount | schemaorg.Number
    ]
):
    term = RdfTerm("http://schema.org/baseSalary", "baseSalary")


class exifData(RdfProperty[schemaorg.PropertyValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/exifData", "exifData")


class sdDatePublished(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/sdDatePublished", "sdDatePublished")


class customer(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/customer", "customer")


class availableIn(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm("http://schema.org/availableIn", "availableIn")


class suggestedMeasurement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/suggestedMeasurement", "suggestedMeasurement")


class extendedAddress(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/extendedAddress", "extendedAddress")


class character(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/character", "character")


class doseValue(RdfProperty[schemaorg.QualitativeValue | schemaorg.Number]):
    term = RdfTerm("http://schema.org/doseValue", "doseValue")


class isAvailableGenerically(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/isAvailableGenerically", "isAvailableGenerically")


class bankAccountType(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/bankAccountType", "bankAccountType")


class childMaxAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/childMaxAge", "childMaxAge")


class shippingSettingsLink(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/shippingSettingsLink", "shippingSettingsLink")


class availableDeliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm(
        "http://schema.org/availableDeliveryMethod", "availableDeliveryMethod"
    )


class workload(RdfProperty[schemaorg.Energy | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/workload", "workload")


class articleSection(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/articleSection", "articleSection")


class byMonth(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/byMonth", "byMonth")


class breastfeedingWarning(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/breastfeedingWarning", "breastfeedingWarning")


class priceComponent(RdfProperty[schemaorg.UnitPriceSpecification]):
    term = RdfTerm("http://schema.org/priceComponent", "priceComponent")


class urlTemplate(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/urlTemplate", "urlTemplate")


class merchantReturnDays(
    RdfProperty[schemaorg.Date | schemaorg.Integer | schemaorg.DateTime]
):
    term = RdfTerm("http://schema.org/merchantReturnDays", "merchantReturnDays")


class archivedAt(RdfProperty[schemaorg.WebPage | schemaorg.URL]):
    term = RdfTerm("http://schema.org/archivedAt", "archivedAt")


class loanMortgageMandateAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm(
        "http://schema.org/loanMortgageMandateAmount", "loanMortgageMandateAmount"
    )


class suggestedMaxAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/suggestedMaxAge", "suggestedMaxAge")


class iupacName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/iupacName", "iupacName")


class lender(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/lender", "lender")


class sportsTeam(RdfProperty[schemaorg.SportsTeam]):
    term = RdfTerm("http://schema.org/sportsTeam", "sportsTeam")


class acceptedPaymentMethod(
    RdfProperty[schemaorg.LoanOrCredit | schemaorg.Text | schemaorg.PaymentMethod]
):
    term = RdfTerm("http://schema.org/acceptedPaymentMethod", "acceptedPaymentMethod")


class coverageStartTime(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/coverageStartTime", "coverageStartTime")


class medicalSpecialty(RdfProperty[schemaorg.MedicalSpecialty]):
    term = RdfTerm("http://schema.org/medicalSpecialty", "medicalSpecialty")


class isTierOf(RdfProperty[schemaorg.MemberProgram]):
    term = RdfTerm("http://schema.org/isTierOf", "isTierOf")


class legislationApplies(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm("http://schema.org/legislationApplies", "legislationApplies")


class toLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/toLocation", "toLocation")


class termCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/termCode", "termCode")


class hoursAvailable(RdfProperty[schemaorg.OpeningHoursSpecification]):
    term = RdfTerm("http://schema.org/hoursAvailable", "hoursAvailable")


class courseMode(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/courseMode", "courseMode")


class termsPerYear(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/termsPerYear", "termsPerYear")


class muscleAction(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/muscleAction", "muscleAction")


class addressLocality(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/addressLocality", "addressLocality")


class incentives(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/incentives", "incentives")


class latitude(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/latitude", "latitude")


class alumniOf(RdfProperty[schemaorg.EducationalOrganization | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/alumniOf", "alumniOf")


class releaseDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/releaseDate", "releaseDate")


class competitor(RdfProperty[schemaorg.Person | schemaorg.SportsTeam]):
    term = RdfTerm("http://schema.org/competitor", "competitor")


class orderPercentage(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/orderPercentage", "orderPercentage")


class cvdNumC19Died(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumC19Died", "cvdNumC19Died")


class epidemiology(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/epidemiology", "epidemiology")


class torque(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/torque", "torque")


class productID(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/productID", "productID")


class returnLabelSource(RdfProperty[schemaorg.ReturnLabelSourceEnumeration]):
    term = RdfTerm("http://schema.org/returnLabelSource", "returnLabelSource")


class bestRating(RdfProperty[schemaorg.Number | schemaorg.Text]):
    term = RdfTerm("http://schema.org/bestRating", "bestRating")


class dependencies(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/dependencies", "dependencies")


class specialOpeningHoursSpecification(
    RdfProperty[schemaorg.OpeningHoursSpecification]
):
    term = RdfTerm(
        "http://schema.org/specialOpeningHoursSpecification",
        "specialOpeningHoursSpecification",
    )


class encodingType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/encodingType", "encodingType")


class weight(RdfProperty[schemaorg.Mass | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/weight", "weight")


class hospitalAffiliation(RdfProperty[schemaorg.Hospital]):
    term = RdfTerm("http://schema.org/hospitalAffiliation", "hospitalAffiliation")


class spatial(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/spatial", "spatial")


class actors(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/actors", "actors")


class afterMedia(RdfProperty[schemaorg.MediaObject | schemaorg.URL]):
    term = RdfTerm("http://schema.org/afterMedia", "afterMedia")


class cvdNumC19MechVentPats(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumC19MechVentPats", "cvdNumC19MechVentPats")


class faxNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/faxNumber", "faxNumber")


class businessDays(
    RdfProperty[schemaorg.DayOfWeek | schemaorg.OpeningHoursSpecification]
):
    term = RdfTerm("http://schema.org/businessDays", "businessDays")


class candidate(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/candidate", "candidate")


class industry(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm("http://schema.org/industry", "industry")


class numTracks(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/numTracks", "numTracks")


class restockingFee(RdfProperty[schemaorg.Number | schemaorg.MonetaryAmount]):
    term = RdfTerm("http://schema.org/restockingFee", "restockingFee")


class branchOf(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/branchOf", "branchOf")


class addressCountry(RdfProperty[schemaorg.Text | schemaorg.Country]):
    term = RdfTerm("http://schema.org/addressCountry", "addressCountry")


class refundType(RdfProperty[schemaorg.RefundTypeEnumeration]):
    term = RdfTerm("http://schema.org/refundType", "refundType")


class title(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/title", "title")


class dateRead(RdfProperty[schemaorg.DateTime | schemaorg.Date]):
    term = RdfTerm("http://schema.org/dateRead", "dateRead")


class seatNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/seatNumber", "seatNumber")


class infectiousAgent(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/infectiousAgent", "infectiousAgent")


class starRating(RdfProperty[schemaorg.Rating]):
    term = RdfTerm("http://schema.org/starRating", "starRating")


class itemDefectReturnFees(RdfProperty[schemaorg.ReturnFeesEnumeration]):
    term = RdfTerm("http://schema.org/itemDefectReturnFees", "itemDefectReturnFees")


class bed(RdfProperty[schemaorg.Text | schemaorg.BedDetails | schemaorg.BedType]):
    term = RdfTerm("http://schema.org/bed", "bed")


class insertion(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/insertion", "insertion")


class proprietaryName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/proprietaryName", "proprietaryName")


class exceptDate(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/exceptDate", "exceptDate")


class chemicalRole(RdfProperty[schemaorg.DefinedTerm]):
    term = RdfTerm("http://schema.org/chemicalRole", "chemicalRole")


class includedDataCatalog(RdfProperty[schemaorg.DataCatalog]):
    term = RdfTerm("http://schema.org/includedDataCatalog", "includedDataCatalog")


class dateline(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/dateline", "dateline")


class legislationAmends(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm("http://schema.org/legislationAmends", "legislationAmends")


class targetUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/targetUrl", "targetUrl")


class accessibilityFeature(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accessibilityFeature", "accessibilityFeature")


class includedInHealthInsurancePlan(RdfProperty[schemaorg.HealthInsurancePlan]):
    term = RdfTerm(
        "http://schema.org/includedInHealthInsurancePlan",
        "includedInHealthInsurancePlan",
    )


class sdPublisher(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/sdPublisher", "sdPublisher")


class nsn(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/nsn", "nsn")


class flightDistance(RdfProperty[schemaorg.Text | schemaorg.Distance]):
    term = RdfTerm("http://schema.org/flightDistance", "flightDistance")


class ticketedSeat(RdfProperty[schemaorg.Seat]):
    term = RdfTerm("http://schema.org/ticketedSeat", "ticketedSeat")


class legislationCorrects(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm("http://schema.org/legislationCorrects", "legislationCorrects")


class line(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/line", "line")


class ethicsPolicy(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("http://schema.org/ethicsPolicy", "ethicsPolicy")


class contentType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/contentType", "contentType")


class hasCredential(RdfProperty[schemaorg.EducationalOccupationalCredential]):
    term = RdfTerm("http://schema.org/hasCredential", "hasCredential")


class arrivalPlatform(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/arrivalPlatform", "arrivalPlatform")


class includesObject(RdfProperty[schemaorg.TypeAndQuantityNode]):
    term = RdfTerm("http://schema.org/includesObject", "includesObject")


class featureList(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/featureList", "featureList")


class datasetTimeInterval(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/datasetTimeInterval", "datasetTimeInterval")


class arrivalTerminal(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/arrivalTerminal", "arrivalTerminal")


class labelDetails(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/labelDetails", "labelDetails")


class sdLicense(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("http://schema.org/sdLicense", "sdLicense")


class seasons(RdfProperty[schemaorg.CreativeWorkSeason]):
    term = RdfTerm("http://schema.org/seasons", "seasons")


class departureAirport(RdfProperty[schemaorg.Airport]):
    term = RdfTerm("http://schema.org/departureAirport", "departureAirport")


class awayTeam(RdfProperty[schemaorg.Person | schemaorg.SportsTeam]):
    term = RdfTerm("http://schema.org/awayTeam", "awayTeam")


class isPartOfBioChemEntity(RdfProperty[schemaorg.BioChemEntity]):
    term = RdfTerm("http://schema.org/isPartOfBioChemEntity", "isPartOfBioChemEntity")


class salaryCurrency(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/salaryCurrency", "salaryCurrency")


class totalHistoricalEnrollment(RdfProperty[schemaorg.Integer]):
    term = RdfTerm(
        "http://schema.org/totalHistoricalEnrollment", "totalHistoricalEnrollment"
    )


class costPerUnit(
    RdfProperty[schemaorg.Number | schemaorg.QualitativeValue | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/costPerUnit", "costPerUnit")


class license(RdfProperty[schemaorg.CreativeWork | schemaorg.URL]):
    term = RdfTerm("http://schema.org/license", "license")


class priceComponentType(RdfProperty[schemaorg.PriceComponentTypeEnumeration]):
    term = RdfTerm("http://schema.org/priceComponentType", "priceComponentType")


class transmissionMethod(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/transmissionMethod", "transmissionMethod")


class editEIDR(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/editEIDR", "editEIDR")


class loanRepaymentForm(RdfProperty[schemaorg.RepaymentSpecification]):
    term = RdfTerm("http://schema.org/loanRepaymentForm", "loanRepaymentForm")


class populationType(RdfProperty[schemaorg.Class]):
    term = RdfTerm("http://schema.org/populationType", "populationType")


class salaryUponCompletion(RdfProperty[schemaorg.MonetaryAmountDistribution]):
    term = RdfTerm("http://schema.org/salaryUponCompletion", "salaryUponCompletion")


class ratingExplanation(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/ratingExplanation", "ratingExplanation")


class aggregateRating(RdfProperty[schemaorg.AggregateRating]):
    term = RdfTerm("http://schema.org/aggregateRating", "aggregateRating")


class itemShipped(RdfProperty[schemaorg.Product]):
    term = RdfTerm("http://schema.org/itemShipped", "itemShipped")


class validForMemberTier(RdfProperty[schemaorg.MemberProgramTier]):
    term = RdfTerm("http://schema.org/validForMemberTier", "validForMemberTier")


class interactionType(RdfProperty[schemaorg.Action]):
    term = RdfTerm("http://schema.org/interactionType", "interactionType")


class application(RdfProperty[schemaorg.SoftwareApplication]):
    term = RdfTerm("http://schema.org/application", "application")


class prescribingInfo(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/prescribingInfo", "prescribingInfo")


class handlingTime(RdfProperty[schemaorg.ServicePeriod | schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/handlingTime", "handlingTime")


class tissueSample(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/tissueSample", "tissueSample")


class doseSchedule(RdfProperty[schemaorg.DoseSchedule]):
    term = RdfTerm("http://schema.org/doseSchedule", "doseSchedule")


class codeSampleType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/codeSampleType", "codeSampleType")


class sensoryRequirement(
    RdfProperty[schemaorg.Text | schemaorg.URL | schemaorg.DefinedTerm]
):
    term = RdfTerm("http://schema.org/sensoryRequirement", "sensoryRequirement")


class associatedArticle(RdfProperty[schemaorg.NewsArticle]):
    term = RdfTerm("http://schema.org/associatedArticle", "associatedArticle")


class addressRegion(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/addressRegion", "addressRegion")


class device(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/device", "device")


class paymentUrl(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/paymentUrl", "paymentUrl")


class nonProprietaryName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/nonProprietaryName", "nonProprietaryName")


class percentile75(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/percentile75", "percentile75")


class significance(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/significance", "significance")


class newsUpdatesAndGuidelines(RdfProperty[schemaorg.WebContent | schemaorg.URL]):
    term = RdfTerm(
        "http://schema.org/newsUpdatesAndGuidelines", "newsUpdatesAndGuidelines"
    )


class pathophysiology(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/pathophysiology", "pathophysiology")


class availableTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm("http://schema.org/availableTest", "availableTest")


class partOfTrip(RdfProperty[schemaorg.Trip]):
    term = RdfTerm("http://schema.org/partOfTrip", "partOfTrip")


class doesNotShip(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/doesNotShip", "doesNotShip")


class legislationRepeals(RdfProperty[schemaorg.Legislation]):
    term = RdfTerm("http://schema.org/legislationRepeals", "legislationRepeals")


class relatedStructure(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/relatedStructure", "relatedStructure")


class colorist(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/colorist", "colorist")


class sensoryUnit(
    RdfProperty[schemaorg.AnatomicalStructure | schemaorg.SuperficialAnatomy]
):
    term = RdfTerm("http://schema.org/sensoryUnit", "sensoryUnit")


class itemListElement(
    RdfProperty[schemaorg.ListItem | schemaorg.Thing | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/itemListElement", "itemListElement")


class recipient(
    RdfProperty[
        schemaorg.Organization
        | schemaorg.Audience
        | schemaorg.ContactPoint
        | schemaorg.Person
    ]
):
    term = RdfTerm("http://schema.org/recipient", "recipient")


class postalCodePrefix(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/postalCodePrefix", "postalCodePrefix")


class follows(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/follows", "follows")


class jobLocation(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/jobLocation", "jobLocation")


class requiredGender(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/requiredGender", "requiredGender")


class spokenByCharacter(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/spokenByCharacter", "spokenByCharacter")


class itemCondition(RdfProperty[schemaorg.OfferItemCondition]):
    term = RdfTerm("http://schema.org/itemCondition", "itemCondition")


class broadcaster(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/broadcaster", "broadcaster")


class clincalPharmacology(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/clincalPharmacology", "clincalPharmacology")


class familyName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/familyName", "familyName")


class callSign(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/callSign", "callSign")


class accelerationTime(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/accelerationTime", "accelerationTime")


class dateCreated(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/dateCreated", "dateCreated")


class _yield(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]):
    term = RdfTerm("http://schema.org/yield", "yield")


class reviewAspect(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/reviewAspect", "reviewAspect")


class hasCertification(RdfProperty[schemaorg.Certification]):
    term = RdfTerm("http://schema.org/hasCertification", "hasCertification")


class accessibilityHazard(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/accessibilityHazard", "accessibilityHazard")


class includesHealthPlanNetwork(RdfProperty[schemaorg.HealthPlanNetwork]):
    term = RdfTerm(
        "http://schema.org/includesHealthPlanNetwork", "includesHealthPlanNetwork"
    )


class albumRelease(RdfProperty[schemaorg.MusicRelease]):
    term = RdfTerm("http://schema.org/albumRelease", "albumRelease")


class usesDevice(RdfProperty[schemaorg.MedicalDevice]):
    term = RdfTerm("http://schema.org/usesDevice", "usesDevice")


class releaseOf(RdfProperty[schemaorg.MusicAlbum]):
    term = RdfTerm("http://schema.org/releaseOf", "releaseOf")


class mechanismOfAction(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/mechanismOfAction", "mechanismOfAction")


class paymentStatus(RdfProperty[schemaorg.PaymentStatusType | schemaorg.Text]):
    term = RdfTerm("http://schema.org/paymentStatus", "paymentStatus")


class numberOfAxles(RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]):
    term = RdfTerm("http://schema.org/numberOfAxles", "numberOfAxles")


class howPerformed(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/howPerformed", "howPerformed")


class deliveryMethod(RdfProperty[schemaorg.DeliveryMethod]):
    term = RdfTerm("http://schema.org/deliveryMethod", "deliveryMethod")


class branch(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/branch", "branch")


class orderNumber(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/orderNumber", "orderNumber")


class publisher(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/publisher", "publisher")


class orderStatus(RdfProperty[schemaorg.OrderStatus]):
    term = RdfTerm("http://schema.org/orderStatus", "orderStatus")


class energyEfficiencyScaleMin(RdfProperty[schemaorg.EUEnergyEfficiencyEnumeration]):
    term = RdfTerm(
        "http://schema.org/energyEfficiencyScaleMin", "energyEfficiencyScaleMin"
    )


class checkinTime(RdfProperty[schemaorg.DateTime | schemaorg.Time]):
    term = RdfTerm("http://schema.org/checkinTime", "checkinTime")


class articleBody(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/articleBody", "articleBody")


class inCodeSet(RdfProperty[schemaorg.URL | schemaorg.CategoryCodeSet]):
    term = RdfTerm("http://schema.org/inCodeSet", "inCodeSet")


class risks(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/risks", "risks")


class inker(RdfProperty[schemaorg.Person]):
    term = RdfTerm("http://schema.org/inker", "inker")


class inChI(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/inChI", "inChI")


class citation(RdfProperty[schemaorg.CreativeWork | schemaorg.Text]):
    term = RdfTerm("http://schema.org/citation", "citation")


class measurementQualifier(RdfProperty[schemaorg.Enumeration]):
    term = RdfTerm("http://schema.org/measurementQualifier", "measurementQualifier")


class genre(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/genre", "genre")


class runsTo(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm("http://schema.org/runsTo", "runsTo")


class engineDisplacement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/engineDisplacement", "engineDisplacement")


class previousItem(RdfProperty[schemaorg.ListItem]):
    term = RdfTerm("http://schema.org/previousItem", "previousItem")


class maintainer(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/maintainer", "maintainer")


class brand(RdfProperty[schemaorg.Brand | schemaorg.Organization]):
    term = RdfTerm("http://schema.org/brand", "brand")


class geoContains(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm("http://schema.org/geoContains", "geoContains")


class knowsLanguage(RdfProperty[schemaorg.Text | schemaorg.Language]):
    term = RdfTerm("http://schema.org/knowsLanguage", "knowsLanguage")


class drainsTo(RdfProperty[schemaorg.Vessel]):
    term = RdfTerm("http://schema.org/drainsTo", "drainsTo")


class differentialDiagnosis(RdfProperty[schemaorg.DDxElement]):
    term = RdfTerm("http://schema.org/differentialDiagnosis", "differentialDiagnosis")


class positiveNotes(
    RdfProperty[
        schemaorg.ListItem | schemaorg.ItemList | schemaorg.WebContent | schemaorg.Text
    ]
):
    term = RdfTerm("http://schema.org/positiveNotes", "positiveNotes")


class productGroupID(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/productGroupID", "productGroupID")


class cvdNumTotBeds(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/cvdNumTotBeds", "cvdNumTotBeds")


class hasOfferCatalog(RdfProperty[schemaorg.OfferCatalog]):
    term = RdfTerm("http://schema.org/hasOfferCatalog", "hasOfferCatalog")


class isSimilarTo(RdfProperty[schemaorg.Product | schemaorg.Service]):
    term = RdfTerm("http://schema.org/isSimilarTo", "isSimilarTo")


class securityClearanceRequirement(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm(
        "http://schema.org/securityClearanceRequirement", "securityClearanceRequirement"
    )


class lyrics(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/lyrics", "lyrics")


class pattern(RdfProperty[schemaorg.DefinedTerm | schemaorg.Text]):
    term = RdfTerm("http://schema.org/pattern", "pattern")


class partOfTVSeries(RdfProperty[schemaorg.TVSeries]):
    term = RdfTerm("http://schema.org/partOfTVSeries", "partOfTVSeries")


class modelDate(RdfProperty[schemaorg.Date]):
    term = RdfTerm("http://schema.org/modelDate", "modelDate")


class isConsumableFor(RdfProperty[schemaorg.Product]):
    term = RdfTerm("http://schema.org/isConsumableFor", "isConsumableFor")


class schoolClosuresInfo(RdfProperty[schemaorg.URL | schemaorg.WebContent]):
    term = RdfTerm("http://schema.org/schoolClosuresInfo", "schoolClosuresInfo")


class replacer(RdfProperty[schemaorg.Thing]):
    term = RdfTerm("http://schema.org/replacer", "replacer")


class browserRequirements(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/browserRequirements", "browserRequirements")


class physicalRequirement(
    RdfProperty[schemaorg.URL | schemaorg.Text | schemaorg.DefinedTerm]
):
    term = RdfTerm("http://schema.org/physicalRequirement", "physicalRequirement")


class deliveryLeadTime(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/deliveryLeadTime", "deliveryLeadTime")


class bodyType(
    RdfProperty[schemaorg.QualitativeValue | schemaorg.Text | schemaorg.URL]
):
    term = RdfTerm("http://schema.org/bodyType", "bodyType")


class childMinAge(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/childMinAge", "childMinAge")


class reservationId(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/reservationId", "reservationId")


class hasMeasurement(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/hasMeasurement", "hasMeasurement")


class vehicleInteriorColor(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/vehicleInteriorColor", "vehicleInteriorColor")


class temporal(RdfProperty[schemaorg.Text | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/temporal", "temporal")


class validThrough(RdfProperty[schemaorg.Date | schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/validThrough", "validThrough")


class typicalTest(RdfProperty[schemaorg.MedicalTest]):
    term = RdfTerm("http://schema.org/typicalTest", "typicalTest")


class namedPosition(RdfProperty[schemaorg.URL | schemaorg.Text]):
    term = RdfTerm("http://schema.org/namedPosition", "namedPosition")


class referencesOrder(RdfProperty[schemaorg.Order]):
    term = RdfTerm("http://schema.org/referencesOrder", "referencesOrder")


class publicationType(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/publicationType", "publicationType")


class comment(RdfProperty[schemaorg.Comment]):
    term = RdfTerm("http://schema.org/comment", "comment")


class commentCount(RdfProperty[schemaorg.Integer]):
    term = RdfTerm("http://schema.org/commentCount", "commentCount")


class honorificPrefix(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/honorificPrefix", "honorificPrefix")


class artform(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/artform", "artform")


class deathPlace(RdfProperty[schemaorg.Place]):
    term = RdfTerm("http://schema.org/deathPlace", "deathPlace")


class domiciledMortgage(RdfProperty[schemaorg.Boolean]):
    term = RdfTerm("http://schema.org/domiciledMortgage", "domiciledMortgage")


class icaoCode(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/icaoCode", "icaoCode")


class returnShippingFeesAmount(RdfProperty[schemaorg.MonetaryAmount]):
    term = RdfTerm(
        "http://schema.org/returnShippingFeesAmount", "returnShippingFeesAmount"
    )


class geoEquals(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm("http://schema.org/geoEquals", "geoEquals")


class dataFeedElement(
    RdfProperty[schemaorg.DataFeedItem | schemaorg.Thing | schemaorg.Text]
):
    term = RdfTerm("http://schema.org/dataFeedElement", "dataFeedElement")


class legislationType(RdfProperty[schemaorg.CategoryCode | schemaorg.Text]):
    term = RdfTerm("http://schema.org/legislationType", "legislationType")


class geoDisjoint(RdfProperty[schemaorg.Place | schemaorg.GeospatialGeometry]):
    term = RdfTerm("http://schema.org/geoDisjoint", "geoDisjoint")


class documentation(RdfProperty[schemaorg.URL | schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/documentation", "documentation")


class composer(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/composer", "composer")


class isLocatedInSubcellularLocation(
    RdfProperty[schemaorg.PropertyValue | schemaorg.URL | schemaorg.DefinedTerm]
):
    term = RdfTerm(
        "http://schema.org/isLocatedInSubcellularLocation",
        "isLocatedInSubcellularLocation",
    )


class broadcastOfEvent(RdfProperty[schemaorg.Event]):
    term = RdfTerm("http://schema.org/broadcastOfEvent", "broadcastOfEvent")


class isPlanForApartment(RdfProperty[schemaorg.Accommodation]):
    term = RdfTerm("http://schema.org/isPlanForApartment", "isPlanForApartment")


class paymentMethodType(RdfProperty[schemaorg.PaymentMethodType]):
    term = RdfTerm("http://schema.org/paymentMethodType", "paymentMethodType")


class availableService(
    RdfProperty[
        schemaorg.MedicalProcedure | schemaorg.MedicalTest | schemaorg.MedicalTherapy
    ]
):
    term = RdfTerm("http://schema.org/availableService", "availableService")


class numberOfPreviousOwners(
    RdfProperty[schemaorg.QuantitativeValue | schemaorg.Number]
):
    term = RdfTerm("http://schema.org/numberOfPreviousOwners", "numberOfPreviousOwners")


class cholesterolContent(RdfProperty[schemaorg.Mass]):
    term = RdfTerm("http://schema.org/cholesterolContent", "cholesterolContent")


class actionOption(RdfProperty[schemaorg.Thing | schemaorg.Text]):
    term = RdfTerm("http://schema.org/actionOption", "actionOption")


class legislationLegalValue(RdfProperty[schemaorg.LegalValueLevel]):
    term = RdfTerm("http://schema.org/legislationLegalValue", "legislationLegalValue")


class monoisotopicMolecularWeight(
    RdfProperty[schemaorg.QuantitativeValue | schemaorg.Text]
):
    term = RdfTerm(
        "http://schema.org/monoisotopicMolecularWeight", "monoisotopicMolecularWeight"
    )


class productionCompany(RdfProperty[schemaorg.Organization]):
    term = RdfTerm("http://schema.org/productionCompany", "productionCompany")


class elevation(RdfProperty[schemaorg.Text | schemaorg.Number]):
    term = RdfTerm("http://schema.org/elevation", "elevation")


class supplyTo(RdfProperty[schemaorg.AnatomicalStructure]):
    term = RdfTerm("http://schema.org/supplyTo", "supplyTo")


class homeLocation(RdfProperty[schemaorg.ContactPoint | schemaorg.Place]):
    term = RdfTerm("http://schema.org/homeLocation", "homeLocation")


class paymentDue(RdfProperty[schemaorg.DateTime]):
    term = RdfTerm("http://schema.org/paymentDue", "paymentDue")


class lesserOrEqual(RdfProperty[schemaorg.QualitativeValue]):
    term = RdfTerm("http://schema.org/lesserOrEqual", "lesserOrEqual")


class programName(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/programName", "programName")


class circle(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/circle", "circle")


class validIn(RdfProperty[schemaorg.AdministrativeArea]):
    term = RdfTerm("http://schema.org/validIn", "validIn")


class wheelbase(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/wheelbase", "wheelbase")


class educationalProgramMode(RdfProperty[schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/educationalProgramMode", "educationalProgramMode")


class carrierRequirements(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/carrierRequirements", "carrierRequirements")


class bodyLocation(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/bodyLocation", "bodyLocation")


class hasMenu(RdfProperty[schemaorg.Menu | schemaorg.Text | schemaorg.URL]):
    term = RdfTerm("http://schema.org/hasMenu", "hasMenu")


class percentile90(RdfProperty[schemaorg.Number]):
    term = RdfTerm("http://schema.org/percentile90", "percentile90")


class interpretedAsClaim(RdfProperty[schemaorg.Claim]):
    term = RdfTerm("http://schema.org/interpretedAsClaim", "interpretedAsClaim")


class speed(RdfProperty[schemaorg.QuantitativeValue]):
    term = RdfTerm("http://schema.org/speed", "speed")


class endorsee(RdfProperty[schemaorg.Organization | schemaorg.Person]):
    term = RdfTerm("http://schema.org/endorsee", "endorsee")


class sizeGroup(RdfProperty[schemaorg.Text | schemaorg.SizeGroupEnumeration]):
    term = RdfTerm("http://schema.org/sizeGroup", "sizeGroup")


class permitAudience(RdfProperty[schemaorg.Audience]):
    term = RdfTerm("http://schema.org/permitAudience", "permitAudience")


class inPlaylist(RdfProperty[schemaorg.MusicPlaylist]):
    term = RdfTerm("http://schema.org/inPlaylist", "inPlaylist")


class geoCoveredBy(RdfProperty[schemaorg.GeospatialGeometry | schemaorg.Place]):
    term = RdfTerm("http://schema.org/geoCoveredBy", "geoCoveredBy")


class assemblyVersion(RdfProperty[schemaorg.Text]):
    term = RdfTerm("http://schema.org/assemblyVersion", "assemblyVersion")


class messageAttachment(RdfProperty[schemaorg.CreativeWork]):
    term = RdfTerm("http://schema.org/messageAttachment", "messageAttachment")
