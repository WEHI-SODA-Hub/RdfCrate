"""
Tests for BaseCrate, ie those that aren't RO-Crate specific.
"""

import datetime
import json

import pytest
from rdflib import RDF, XSD, BNode, Graph, Literal, URIRef
from rdflib.compare import isomorphic

from rdfcrate import BaseCrate, ContextNamespace
from rdfcrate.vocabs import Rdf


class Sdo(ContextNamespace):
    _base = URIRef("http://schema.org/")
    Thing = _base + "Thing"
    dateCreated = _base + "dateCreated"
    hasPart = _base + "hasPart"
    name = _base + "name"


class BioschemasDrafts(ContextNamespace):
    _base = URIRef("https://bioschemas.org/draft_terms/")
    LabProtocol = _base + "LabProtocol"
    Enzyme = _base + "Enzyme"


class Obi(ContextNamespace, context_prefix="obi"):
    _base = URIRef("http://purl.obolibrary.org/obo/")
    Image = _base + "IAO_0000101"
    Assay = _base + "OBI_0000070"


class Xsd(ContextNamespace, context_prefix="xsd"):
    _base = URIRef(str(XSD))
    date = _base + "date"


def test_custom_vocab():
    """
    Only the vocab terms that are used in the graph should be in the context, and they should be used to shorten IRIs.
    """
    crate = BaseCrate(vocabs=[Sdo, BioschemasDrafts])
    crate.add_entity(
        "#some_protocol",
        (Rdf.type_, BioschemasDrafts.LabProtocol),
        (Sdo.name, Literal("Some Protocol")),
    )
    entity_json = json.loads(crate.compile())
    assert entity_json["@context"] == {
        "LabProtocol": "https://bioschemas.org/draft_terms/LabProtocol",
        "name": "http://schema.org/name",
    }
    assert entity_json["@type"] == "LabProtocol"
    assert entity_json["name"] == "Some Protocol"


def test_curies():
    """
    Namespaces with a `context_prefix` and `_base` should use CURIEs, both in the context and in `@id` values.
    """
    crate = BaseCrate(vocabs=[Sdo, Obi])
    crate.add_entity(
        "#image",
        (Rdf.type_, Obi.Image),
        (Sdo.hasPart, Obi.Assay),
    )
    entity_json = json.loads(crate.compile())
    assert entity_json["@context"] == {
        "obi": "http://purl.obolibrary.org/obo/",
        "obiImage": "obi:IAO_0000101",
        "hasPart": "http://schema.org/hasPart",
    }
    assert entity_json["@type"] == "obiImage"
    assert entity_json["hasPart"] == {"@id": "obi:OBI_0000070"}


def test_round_trip():
    """
    The compiled JSON-LD should parse back to the same graph, including CURIEs.
    """
    crate = BaseCrate(vocabs=[Sdo, Obi])
    crate.add_entity(
        "http://example.org/image",
        (Rdf.type_, Obi.Image),
        (Sdo.hasPart, Obi.Assay),
        (Sdo.name, Literal("An image")),
    )
    assert isomorphic(
        Graph().parse(data=crate.compile(), format="json-ld"), crate.graph
    )


def test_rdf_type_not_in_context():
    """
    rdf:type should never be redefined, since JSON-LD uses `@type`.
    """
    crate = BaseCrate(vocabs=[Sdo, Rdf])
    crate.add_entity("#thing", (Rdf.type_, Sdo.Thing))
    assert json.loads(crate.compile())["@context"] == {
        "Thing": "http://schema.org/Thing"
    }


def test_missing_term():
    """
    IRIs that aren't defined in any vocab should raise an error.
    """
    crate = BaseCrate(vocabs=[Sdo])
    crate.add_entity("#thing", (Rdf.type_, BioschemasDrafts.Enzyme))
    with pytest.raises(ValueError, match=str(BioschemasDrafts.Enzyme)):
        crate.compile()


def test_vocab_clash():
    """
    Two vocabs that use the same label for different IRIs should raise an error.
    """

    class Example(ContextNamespace):
        name = URIRef("https://example.org/name")

    crate = BaseCrate(vocabs=[Sdo, Example])
    crate.add_entity("#thing", (Sdo.name, Literal("a")), (Example.name, Literal("b")))
    with pytest.raises(ValueError, match="context_prefix"):
        crate.compile()


def test_datatype():
    """
    Datatypes that are serialized as JSON-LD `@type` need a term, but native JSON types don't.
    """
    crate = BaseCrate(vocabs=[Sdo])
    crate.add_entity("#thing", (Sdo.name, Literal(True)), (Sdo.name, Literal(1)))
    crate.compile()

    crate.add_entity("#thing", (Sdo.dateCreated, Literal(datetime.date(2023, 1, 1))))
    with pytest.raises(ValueError, match=str(XSD.date)):
        crate.compile()

    crate.vocabs.append(Xsd)
    assert crate.full_context.expand("xsdDate") == str(XSD.date)


def test_bnode():
    crate = BaseCrate(vocabs=[BioschemasDrafts])
    crate.add_entity(BNode(), (Rdf.type_, BioschemasDrafts.LabProtocol))
    assert any(isinstance(id, BNode) for id in crate.graph.subjects())


def test_strip_datatypes():
    """
    Test that `base_crate.strip_datatypes()` works as expected.
    """
    crate = BaseCrate()
    crate.add_entity("#thing", (Sdo.dateCreated, Literal(datetime.date(2023, 1, 1))))
    stripped_graph = crate.strip_datatypes()
    date_value = stripped_graph.value(URIRef("#thing"), Sdo.dateCreated)
    assert isinstance(date_value, Literal), "The date value should be a Literal"
    assert date_value.value == datetime.date(2023, 1, 1)
    assert date_value.datatype is None, "The date value should not have a datatype"


def test_add_entity_returns_id():
    crate = BaseCrate()
    assert crate.add_entity("#thing") == URIRef("#thing")
    node = BNode()
    assert crate.add_entity(node) == node


def test_add_basecrate():
    """
    Adding a BaseCrate should merge both its graph and its vocabs.
    """
    a = BaseCrate(vocabs=[Sdo])
    b = BaseCrate(vocabs=[Sdo, BioschemasDrafts])
    b.add_entity("#sub", (Rdf.type_, BioschemasDrafts.LabProtocol))
    a.add(b)

    assert URIRef("#sub") in set(a.graph.subjects()), (
        "Subgraph should be added to the main graph"
    )
    assert a.vocabs == [Sdo, BioschemasDrafts], "Vocabs should be merged"
    assert a.full_context.expand("LabProtocol") == str(BioschemasDrafts.LabProtocol)


def test_add_graph():
    crate = BaseCrate()
    g2 = Graph()
    g2.add((URIRef("#g2"), RDF.type, Sdo.Thing))
    crate.add(g2)
    assert (URIRef("#g2"), RDF.type, Sdo.Thing) in crate.graph


def test_add_triple():
    """
    Plain triples can be used in place of reverse properties.
    """
    crate = BaseCrate()
    triple = (URIRef("#parent"), Sdo.hasPart, URIRef("#child"))
    crate.add(triple)
    assert triple in crate.graph


def test_navigate_and_navigate_to():
    """
    Test BaseCrate.navigate and navigate_to, skipping if rdfnav is not installed.
    """
    pytest.importorskip("rdfnav")

    crate = BaseCrate()
    thing = crate.add_entity("#thing", (Rdf.type_, Sdo.Thing))

    navigator = crate.navigate()
    assert navigator.instance(Sdo.Thing).iri == thing

    node = crate.navigate_to(thing)
    assert node.is_instance_of(Sdo.Thing)
