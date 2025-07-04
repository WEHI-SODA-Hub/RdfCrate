import ast
from rdflib import RDFS, Graph, RDF, PROV, URIRef

from rdfcrate.codegen import find_classes, find_datatypes, find_enum_values, find_properties, SDO, CodegenState


def test_find_classes_sdo():
    graph = Graph()
    graph.parse("https://schema.org/version/latest/schemaorg-current-http.jsonld")
    classes = set(str(x) for x in find_classes(graph))
    assert str(SDO.Person) in classes
    assert str(SDO.Text) not in classes

def test_find_classes_rdf():
    graph = Graph()
    graph.parse(RDF._NS)
    graph.parse(RDFS._NS)
    classes = set(str(x) for x in find_classes(graph))
    assert str(RDF.HTML) not in classes
    assert str(RDF.Statement) in classes

def test_find_datatypes_sdo():
    graph = Graph()
    graph.parse("https://schema.org/version/latest/schemaorg-current-http.jsonld")
    datatypes = set(str(x) for x in find_datatypes(graph))
    assert str(SDO.Text) in datatypes
    assert str(SDO.Person) not in datatypes

def test_find_properties_sdo():
    graph = Graph()
    graph.parse("https://schema.org/version/latest/schemaorg-current-http.jsonld")
    properties = set(str(x) for x in find_properties(graph))
    assert str(SDO.name) in properties
    assert str(SDO.Person) not in properties

def test_find_properties_prov():
    graph = Graph()
    # Prov uses owl
    graph.parse("https://www.w3.org/2002/07/owl")
    graph.parse("https://www.w3.org/ns/prov.ttl")
    properties = set(str(x) for x in find_properties(graph))
    assert str(PROV.influenced) in properties
    assert str(PROV.Quotation) not in properties

def test_find_enums_sdo():
    graph = Graph()
    graph.parse("https://schema.org/version/latest/schemaorg-current-http.jsonld")
    enums = set(str(x) for x in find_enum_values(graph))
    assert str(SDO.Hardcover) in enums
    assert str(SDO.Lung) in enums
    assert str(SDO.Person) not in enums

def test_classes_bioschemas():
    graph = Graph()
    graph.parse("https://bioschemas.org/types/bioschemas_draft_types.jsonld")
    classes = set(str(x) for x in find_classes(graph))    
    assert "https://bioschemas.org/draft_terms/LabProtocol" in classes

def test_obi_codegen():
    graph = Graph()
    graph.parse("https://www.w3.org/2002/07/owl")
    graph.parse("http://purl.obolibrary.org/obo/obi.owl")
    state = CodegenState(graph)

    # Check that Microscope's superclass is found to be ImageCreationDevice.
    # This checks that we can find classes defined as owl:Class
    (name,), (uri,) = state._find_superclasses(URIRef("http://purl.obolibrary.org/obo/OBI_0400169"))
    assert isinstance(name, ast.Name) and name.id == "ImageCreationDevice"
    assert str(uri) == "http://purl.obolibrary.org/obo/OBI_0000398"
