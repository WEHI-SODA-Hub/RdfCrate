"""
Tests for ContextGraph, ie those that aren't RO-Crate specific.
"""

import datetime
import json
from dataclasses import dataclass

import pytest
from rdflib import DCTERMS, RDF, SDO, XSD, BNode, Graph, Literal, URIRef
from rdflib.compare import isomorphic
from rdflib.plugins.shared.jsonld.context import Context

from rdfcrate import ContextGraph, ContextNamespace
from rdfcrate.context_builder import ContextBuilder


class Sdo(ContextNamespace, mode="omit"):
    _base = URIRef("http://schema.org/")
    Thing = _base + "Thing"
    dateCreated = _base + "dateCreated"
    description = _base + "description"
    duration = _base + "duration"
    hasPart = _base + "hasPart"
    name = _base + "name"


class BioschemasDrafts(ContextNamespace):
    _base = URIRef("https://bioschemas.org/draft_terms/")
    LabProtocol = _base + "LabProtocol"
    Enzyme = _base + "Enzyme"
    labEquipment = _base + "labEquipment"


class Dcterms(ContextNamespace):
    _base = URIRef(str(DCTERMS))
    description = _base + "description"


class Obi(ContextNamespace, prefix="obi", mode="prefix_collision"):
    _base = URIRef("http://purl.obolibrary.org/obo/")
    Image = _base + "IAO_0000101"
    Assay = _base + "OBI_0000070"
    hasPart = _base + "BFO_0000051"


class Xsd(ContextNamespace, prefix="xsd", mode="prefix"):
    _base = URIRef(str(XSD))
    date = _base + "date"
    duration = _base + "duration"


class Edam(ContextNamespace, prefix="edam", mode="curie"):
    _base = URIRef("http://edamontology.org/")
    Sequence = _base + "data_2044"
    Image = _base + "data_2968"


class RoCrate(ContextNamespace, mode="omit"):
    # Unlike the other namespaces, this has no base IRI and is set to omit mode
    # This is because the context is already included as a URL
    File = SDO.MediaObject


class NoPrefix(ContextNamespace, mode="prefix"):
    _base = URIRef("https://example.org/")
    name = _base + "name"


class NoBaseCurie(ContextNamespace, prefix="ex", mode="curie"):
    name = URIRef("https://example.org/name")


class ExternalContextGraph(ContextGraph):
    """
    A `ContextGraph` whose external context defines the terms of the "omit" namespaces above, like the RO-Crate context does for `RoCrate`.
    """

    external = Context(
        {term: str(iri) for vocab in [Sdo, RoCrate] for term, iri in vocab.terms()}
    )

    def context_builder(self) -> ContextBuilder:
        return ContextBuilder(external=self.external)


def test_custom_vocab():
    """
    Only the vocab terms that are used in the graph should be in the context, and they should be used to shorten IRIs.
    """
    crate = ExternalContextGraph(vocabs=[Sdo, BioschemasDrafts])
    crate.add_entity(
        "#some_protocol",
        (RDF.type, BioschemasDrafts.LabProtocol),
        (Sdo.name, Literal("Some Protocol")),
    )
    entity_json = json.loads(crate.compile())
    assert entity_json["@context"] == {
        "LabProtocol": "https://bioschemas.org/draft_terms/LabProtocol",
    }
    assert entity_json["@type"] == "LabProtocol"


def test_curies():
    """
    Namespaces in "curie" mode should only add their prefix to the context, and IRIs should be shortened to CURIEs.
    """
    crate = ExternalContextGraph(vocabs=[Sdo, Edam])
    crate.add_entity("#sequence", (RDF.type, Edam.Sequence))
    entity_json = json.loads(crate.compile())
    assert entity_json["@context"] == {
        "edam": "http://edamontology.org/",
    }
    assert entity_json["@type"] == "edam:data_2044"


def test_round_trip():
    """
    The compiled JSON-LD should parse back to the same graph, including CURIEs and prefixed terms.
    """
    crate = ExternalContextGraph(vocabs=[Sdo, Obi, Edam])
    crate.add_entity(
        "http://example.org/image",
        (RDF.type, Edam.Image),
        (Sdo.hasPart, URIRef("http://example.org/part")),
        (Obi.hasPart, Obi.Assay),
        (Sdo.name, Literal("An image")),
    )
    assert isomorphic(
        Graph().parse(data=crate.compile(), format="json-ld"), crate.graph
    )


def test_rdf_type_not_in_context():
    """
    rdf:type should never be redefined, since JSON-LD uses `@type`.
    """

    class Rdf(ContextNamespace):
        _base = URIRef(str(RDF))
        type_ = _base + "type"

    crate = ContextGraph(vocabs=[BioschemasDrafts, Rdf])
    crate.add_entity("#thing", (RDF.type, BioschemasDrafts.LabProtocol))
    assert json.loads(crate.compile())["@context"] == {
        "LabProtocol": "https://bioschemas.org/draft_terms/LabProtocol"
    }


def test_datatype():
    """
    Datatypes that are serialized as JSON-LD `@type` need a term, but native JSON types don't.
    """
    crate = ExternalContextGraph(vocabs=[Sdo])
    crate.add_entity("#thing", (Sdo.name, Literal(True)), (Sdo.name, Literal(1)))
    assert crate.vocab_context() == {}

    crate.add_entity("#thing", (Sdo.dateCreated, Literal(datetime.date(2023, 1, 1))))
    with pytest.raises(ValueError, match=str(XSD.date)):
        crate.vocab_context()

    crate.vocabs.append(Xsd)
    assert crate.full_context.expand("xsddate") == str(XSD.date)


def test_bnode():
    crate = ContextGraph(vocabs=[BioschemasDrafts])
    crate.add_entity(BNode(), (RDF.type, BioschemasDrafts.LabProtocol))
    assert any(isinstance(id, BNode) for id in crate.graph.subjects())


def test_strip_datatypes():
    """
    Test that `context_graph.strip_datatypes()` works as expected.
    """
    crate = ContextGraph()
    crate.add_entity("#thing", (Sdo.dateCreated, Literal(datetime.date(2023, 1, 1))))
    stripped_graph = crate.strip_datatypes()
    date_value = stripped_graph.value(URIRef("#thing"), Sdo.dateCreated)
    assert isinstance(date_value, Literal), "The date value should be a Literal"
    assert date_value.value == datetime.date(2023, 1, 1)
    assert date_value.datatype is None, "The date value should not have a datatype"


def test_add_entity_returns_id():
    crate = ContextGraph()
    assert crate.add_entity("#thing") == URIRef("#thing")
    node = BNode()
    assert crate.add_entity(node) == node


def test_add_basecrate():
    """
    Adding a ContextGraph should merge both its graph and its vocabs.
    """
    a = ContextGraph(vocabs=[Sdo])
    b = ContextGraph(vocabs=[Sdo, BioschemasDrafts])
    b.add_entity("#sub", (RDF.type, BioschemasDrafts.LabProtocol))
    a.add(b)

    assert URIRef("#sub") in set(a.graph.subjects()), (
        "Subgraph should be added to the main graph"
    )
    assert a.vocabs == [Sdo, BioschemasDrafts], "Vocabs should be merged"
    assert a.full_context.expand("LabProtocol") == str(BioschemasDrafts.LabProtocol)


def test_add_graph():
    crate = ContextGraph()
    g2 = Graph()
    g2.add((URIRef("#g2"), RDF.type, Sdo.Thing))
    crate.add(g2)
    assert (URIRef("#g2"), RDF.type, Sdo.Thing) in crate.graph


def test_add_triple():
    """
    Plain triples can be used in place of reverse properties.
    """
    crate = ContextGraph()
    triple = (URIRef("#parent"), Sdo.hasPart, URIRef("#child"))
    crate.add(triple)
    assert triple in crate.graph


def test_navigate_and_navigate_to():
    """
    Test ContextGraph.navigate and navigate_to, skipping if rdfnav is not installed.
    """
    pytest.importorskip("rdfnav")

    crate = ContextGraph()
    thing = crate.add_entity("#thing", (RDF.type, Sdo.Thing))

    navigator = crate.navigate()
    assert navigator.instance(Sdo.Thing).iri == thing

    node = crate.navigate_to(thing)
    assert node.is_instance_of(Sdo.Thing)


@dataclass
class VocabContextCase:
    #: Vocabs to provide to the `ContextGraph`, in priority order
    vocabs: list[type[ContextNamespace]]
    #: Properties of a single entity in the graph
    props: list[tuple[URIRef, URIRef | Literal]]
    #: Expected result of `.vocab_context()`, or the exception it should raise
    expected: dict[str, str] | type[Exception]


@pytest.mark.parametrize(
    "case",
    [
        # omit
        pytest.param(
            VocabContextCase(
                vocabs=[RoCrate, Sdo],
                props=[(RDF.type, RoCrate.File), (Sdo.name, Literal("a"))],
                expected={},
            ),
            id="omit",
        ),
        # standard
        pytest.param(
            VocabContextCase(
                vocabs=[Sdo, BioschemasDrafts],
                props=[
                    (RDF.type, BioschemasDrafts.LabProtocol),
                    # IRI objects don't need a term, only the predicate does
                    (
                        BioschemasDrafts.labEquipment,
                        URIRef("https://example.org/pipette"),
                    ),
                ],
                expected={
                    "LabProtocol": "https://bioschemas.org/draft_terms/LabProtocol",
                    "labEquipment": "https://bioschemas.org/draft_terms/labEquipment",
                },
            ),
            id="standard",
        ),
        # prefix
        pytest.param(
            VocabContextCase(
                vocabs=[Sdo, Xsd],
                props=[
                    (Sdo.dateCreated, Literal(datetime.date(2023, 1, 1))),
                    # "duration" is claimed by Sdo, but that doesn't matter because Xsd always prefixes
                    (Sdo.duration, Literal("PT1H", datatype=XSD.duration)),
                ],
                expected={
                    "xsddate": str(XSD.date),
                    "xsdduration": str(XSD.duration),
                },
            ),
            id="prefix",
        ),
        # prefix_collision
        pytest.param(
            VocabContextCase(
                vocabs=[Sdo, Obi],
                props=[(RDF.type, Obi.Image), (Obi.hasPart, Obi.Assay)],
                expected={
                    "Image": "http://purl.obolibrary.org/obo/IAO_0000101",
                    # "hasPart" is claimed by Sdo even though Sdo.hasPart isn't used
                    "obihasPart": "http://purl.obolibrary.org/obo/BFO_0000051",
                },
            ),
            id="prefix_collision",
        ),
        # curie
        pytest.param(
            VocabContextCase(
                vocabs=[Obi, Edam],
                # "Image" is claimed by Obi, but that doesn't matter because Edam only adds its prefix
                props=[(RDF.type, Obi.Image), (RDF.type, Edam.Image)],
                expected={
                    "Image": "http://purl.obolibrary.org/obo/IAO_0000101",
                    "edam": "http://edamontology.org/",
                },
            ),
            id="curie",
        ),
        # All modes together
        pytest.param(
            VocabContextCase(
                vocabs=[RoCrate, Sdo, BioschemasDrafts, Obi, Xsd, Edam],
                props=[
                    (RDF.type, RoCrate.File),
                    (RDF.type, BioschemasDrafts.LabProtocol),
                    (RDF.type, Obi.Image),
                    (RDF.type, Edam.Image),
                    (Sdo.name, Literal("a")),
                    (Sdo.hasPart, URIRef("https://example.org/part")),
                    (Obi.hasPart, Obi.Assay),
                    (Sdo.dateCreated, Literal(datetime.date(2023, 1, 1))),
                ],
                expected={
                    "LabProtocol": "https://bioschemas.org/draft_terms/LabProtocol",
                    "Image": "http://purl.obolibrary.org/obo/IAO_0000101",
                    "obihasPart": "http://purl.obolibrary.org/obo/BFO_0000051",
                    "xsddate": str(XSD.date),
                    "edam": "http://edamontology.org/",
                },
            ),
            id="all-modes",
        ),
    ],
)
def test_vocab_context(case: VocabContextCase):
    """
    Each namespace mode should contribute the right terms to the vocab context, both alone and alongside other namespaces.
    """
    crate = ExternalContextGraph(vocabs=case.vocabs)
    crate.add_entity("#thing", *case.props)
    assert crate.vocab_context() == case.expected


@pytest.mark.parametrize(
    "case",
    [
        pytest.param(
            VocabContextCase(
                vocabs=[Sdo],
                props=[(RDF.type, BioschemasDrafts.Enzyme)],
                expected=ValueError,
            ),
            id="missing-term",
        ),
        pytest.param(
            VocabContextCase(
                # "description" is claimed by Sdo even though Sdo.description isn't used, and Dcterms has no prefix to fall back on
                vocabs=[Sdo, Dcterms],
                props=[(Dcterms.description, Literal("a"))],
                expected=ValueError,
            ),
            id="standard-clashing-with-omit",
        ),
        pytest.param(
            VocabContextCase(
                vocabs=[NoPrefix],
                props=[(NoPrefix.name, Literal("a"))],
                expected=ValueError,
            ),
            id="prefix-without-prefix",
        ),
        pytest.param(
            VocabContextCase(
                vocabs=[NoBaseCurie],
                props=[(NoBaseCurie.name, Literal("a"))],
                expected=ValueError,
            ),
            id="curie-without-base",
        ),
    ],
)
def test_vocab_context_error(case: VocabContextCase):
    """
    Invalid combinations of graph contents and namespaces should raise an error from `.vocab_context()`.
    """
    crate = ExternalContextGraph(vocabs=case.vocabs)
    crate.add_entity("#thing", *case.props)
    assert isinstance(case.expected, type)
    with pytest.raises(case.expected):
        crate.vocab_context()
