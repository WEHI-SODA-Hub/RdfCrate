"""
Tests for ContextGraph, ie those that aren't RO-Crate specific.
"""

from rdfcrate.context_graph import ContextGraph
from rdfcrate import RdfProperty, owl, RdfClass
from rdflib import RDF, Literal, BNode, URIRef, Graph
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import dc, sdo, rdf, bioschemas_drafts, rdfs
import json
import pytest


def test_bioschemas():
    graph = ContextGraph()
    graph.add_entity(
        bioschemas_drafts.LabProtocol("#some_protocol"),
        sdo.name(sdo.Text("Some Protocol")),
    )
    entity_json = json.loads(graph.compile())
    assert "http" not in entity_json["@type"], "All terms should be shortened"

    assert entity_json["@context"]["LabProtocol"] == str(
        bioschemas_drafts.LabProtocol.term.uri
    ), "Only the terms that are used in the graph should be in the context"


def test_bnode():
    graph = ContextGraph()
    graph.add_entity(bioschemas_drafts.LabProtocol(BNode()))
    assert any(isinstance(id, BNode) for id in graph.graph.subjects())


def test_multi_type():
    class CustomType(rdfs.Class):
        term = RdfTerm("https://example.org/SomeOtherType")

    graph = ContextGraph()
    graph.add_entity(
        bioschemas_drafts.LabProtocol("#multi_type_entity"),
        CustomType.to_type_property(),
    )

    # We never want to redefine rdf:type
    assert str(rdf.type.term.uri) not in graph._custom_terms
    # But we should have the custom type in the context
    assert "https://example.org/SomeOtherType" in graph.full_context.to_dict().values()


def test_redefine_term():
    graph = ContextGraph(unique_terms=True)
    graph.register_term(
        RdfTerm("https://schema.org/Thing", "Thing"),
    )
    with pytest.raises(ValueError):
        graph.register_term(
            RdfTerm("https://example.org/Thing", "Thing"),
        )


def test_add_metadata_term():
    """
    Test that terms used in `add_metadata` are registered in the context.
    """
    graph = ContextGraph()
    graph.add_metadata(
        sdo.Thing("#thing"),
        dc.valid(rdfs.Literal(Literal(True))),
    )
    # If valid can expand, it means it was correctly registered
    assert graph.full_context.expand("valid") == "http://purl.org/dc/terms/valid"


def test_reverse_prop():
    """
    Test that we can add a reverse property to an entity.
    """
    graph = ContextGraph()
    thing = graph.add_entity(
        sdo.Thing("#thing"),
    )
    other_thing = graph.add_entity(
        sdo.Thing("#other-thing"), sdo.hasPart.reverse(thing)
    )
    assert (
        thing.id,
        sdo.hasPart.term.uri,
        other_thing.id,
    ) in graph.graph


def test_adhoc_term():
    """
    Test that we can define terms on the fly and use them in properties.
    """
    graph = ContextGraph()
    thing = graph.add_entity(
        sdo.Thing("#thing"),
        RdfProperty.adhoc(
            term=RdfTerm("https://example.org/myProp"), object=sdo.Text("value")
        ),
    )
    assert (
        thing.id,
        URIRef("https://example.org/myProp"),
        Literal("value"),
    ) in graph.graph


def test_cls_with_term_label():
    """
    Test that we can use two types with the same term label, by renaming one of them.
    """
    graph = ContextGraph()
    thing = graph.add_entity(
        sdo.Class("#thing"), owl.Class.with_term_label("owlClass").to_type_property()
    )
    assert (thing.id, RDF.type, sdo.Class.term.uri) in graph.graph
    assert (thing.id, RDF.type, owl.Class.term.uri) in graph.graph


def test_prop_with_term_label():
    """
    Test that we can use two properties with the same term label, by renaming one of them.
    """
    graph = ContextGraph()

    class exHasPart(RdfProperty):
        term = RdfTerm("https://example.org/hasPart", "hasPart")

    part = sdo.CreativeWork("https://example.org/part")

    with pytest.raises(ValueError):
        graph.add_entity(
            sdo.Thing("#thing"),
            sdo.hasPart(part),
            exHasPart(part),
        )

    graph.add_entity(
        sdo.Thing("#thing"),
        sdo.hasPart(part),
        exHasPart.with_term_label("exHasPart")(part),
    )


def test_adhoc_class():
    """
    Test that we can use two types with the same term label, by renaming one of them.
    """
    graph = ContextGraph()
    ExampleClass = RdfClass.adhoc(RdfTerm("https://example.org/thing"))
    graph.add_entity(
        ExampleClass("#thing"),
    )
    assert (URIRef("#thing"), RDF.type, ExampleClass.term.uri) in graph.graph


def test_add_contextgraph():
    a = ContextGraph()
    a.add_entity(sdo.Thing("#sub"))

    b = ContextGraph()

    b.add(a)

    assert URIRef("#sub") in set(b.graph.subjects()), (
        "Subgraph should be added to the main graph"
    )
    assert b.full_context.expand("Thing") == str(sdo.Thing.term.uri), (
        "Context should be preserved"
    )


def test_add_graph():
    graph = ContextGraph()
    g2 = Graph()
    g2.add((URIRef("#g2"), RDF.type, sdo.Thing.term.uri))
    graph.add(g2)
    assert (URIRef("#g2"), RDF.type, sdo.Thing.term.uri) in graph.graph


def test_add_triple():
    graph = ContextGraph()
    triple = (URIRef("#triple"), RDF.type, sdo.Thing.term.uri)
    graph.add(triple)
    assert triple in graph.graph


def test_navigate_and_navigate_to():
    """
    Test ContextGraph.navigate and navigate_to, skipping if rdfnav is not installed.
    """
    pytest.importorskip("rdfnav")

    graph = ContextGraph()
    thing = graph.add_entity(sdo.Thing("#thing"))

    navigator = graph.navigate()
    assert navigator.instance(sdo.Thing.term.uri).iri == thing.id

    node = graph.navigate_to(thing.id)
    assert node.is_instance_of(sdo.Thing.term.uri)
