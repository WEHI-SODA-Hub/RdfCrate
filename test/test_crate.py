from pathlib import Path
from rdfcrate import AttachedCrate, RdfProperty, owl, RdfClass
from rdflib import RDF, Literal, Graph, BNode, URIRef
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import dc, sdo, roc, rdf, bioschemas_drafts, rdfs
import json
from datetime import datetime
import tempfile
import pytest
from rdfcrate.test_helpers import patch_rocrate_context

TEST_CRATE = Path(__file__).parent / "test_crate"

MIT = URIRef("https://opensource.org/license/mit")
ME = URIRef("https://orcid.org/0000-0002-8965-2595")
WEHI_RCP = URIRef("https://github.com/WEHI-ResearchComputing")

BASE_SUBJECTS = [MIT, ME, WEHI_RCP]

@pytest.fixture()
def empty_crate():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield AttachedCrate(path=tmpdir)

@pytest.fixture(scope="function", autouse=True)
def rocrate_context():
    with patch_rocrate_context():
        yield


def make_test_crate(recursive: bool = False):
    crate = AttachedCrate(TEST_CRATE)

    crate.add_root_entity(
        sdo.name(sdo.Text("Test Crate")),
        sdo.description(sdo.Text("Crate for validating RdfCrate")),
        sdo.datePublished(sdo.DateTime(datetime.now().isoformat())),
        sdo.license(
            crate.add_entity(sdo.CreativeWork(MIT), sdo.name(sdo.Text("MIT License")))
        ),
        sdo.version(sdo.Text("1.0")),
        sdo.publisher(
            wehi := crate.add_entity(
                sdo.Organization(WEHI_RCP),
                sdo.name(sdo.Text("WEHI Research Computing Platform")),
                sdo.url(sdo.URL(WEHI_RCP)),
            )
        ),
        sdo.author(
            crate.add_entity(
                sdo.Person(ME), sdo.name(sdo.Text("Michael")), sdo.affiliation(wehi)
            )
        ),
        recursive=recursive,
    )
    crate.add_metadata_entity()
    return crate


def test_spec_conformant():
    crate = make_test_crate(recursive=True)

    # Normally checking JSON-LD using JSON is a bad idea, but RO-Crate mandates a specific structure that
    # goes beyond standard JSON-LD
    crate_json = json.loads(crate.compile())
    assert crate_json["@context"] == "https://w3id.org/ro/crate/1.1/context"

    found_metadata = False
    found_root = False
    for entity in crate_json["@graph"]:
        if entity["@id"] == "ro-crate-metadata.json":
            found_metadata = True
            # The RO-Crate JSON-LD MUST contain a self-describing RO-Crate Metadata File Descriptor with the @id value ro-crate-metadata.json (or ro-crate-metadata.jsonld in legacy crates) and @type CreativeWork
            assert entity["@type"] == "CreativeWork"
            # This descriptor MUST have an about property referencing the Root Data Entity, which SHOULD have an @id of ./.
            assert entity["about"] == {"@id": "./"}
            # The conformsTo of the RO-Crate Metadata File Descriptor SHOULD be a versioned permalink URI of the RO-Crate specification that the RO-Crate JSON-LD conforms to. The URI SHOULD start with https://w3id.org/ro/crate/.
            assert entity["conformsTo"] == {"@id": "https://w3id.org/ro/crate/1.1"}
        elif entity["@id"] == "./":
            found_root = True
            # @type: MUST be Dataset
            assert entity["@type"] == "Dataset"
            # datePublished: MUST be a string in ISO 8601 date format and SHOULD be specified to at least the precision of a day, MAY be a timestamp down to the millisecond.
            datetime.fromisoformat(entity["datePublished"])

    assert found_metadata
    assert found_root


def test_single_file():
    crate = make_test_crate(recursive=False)
    crate.register_file("text.txt")

    # Check that the graph has the expected structure
    assert set(crate.graph.subjects()) == {
        URIRef("./"),
        URIRef("ro-crate-metadata.json"),
        URIRef("text.txt"),
        *BASE_SUBJECTS,
    }
    assert set(crate.graph.predicates()) >= {
        rdf.type.term.uri,
        sdo.about.term.uri,
        dc.conformsTo.term.uri,
    }
    assert set(crate.graph.objects()) >= {roc.File.term.uri, sdo.Dataset.term.uri}

    crate.validate()

    # Check that we can round-trip the graph
    Graph().parse(data=crate.compile(), format="json-ld")


def test_recursive_add():
    crate = make_test_crate(recursive=True)
    assert set(crate.graph.subjects()) == {
        URIRef("./"),
        URIRef("ro-crate-metadata.json"),
        URIRef("text.txt"),
        URIRef("binary.bin"),
        URIRef("subdir/"),
        URIRef("subdir/more_text.txt"),
        *BASE_SUBJECTS,
    }, "All files and directories should be in the crate"
    assert crate.graph.value(
        predicate=sdo.hasPart.term.uri, object=URIRef("subdir/more_text.txt")
    ) == URIRef("subdir/"), (
        "Recursive add should link the immediate child and parent via hasPart"
    )
    crate.validate()


def test_mime_type():
    crate = make_test_crate(recursive=True)

    assert crate.graph.value(
        URIRef("text.txt"), sdo.encodingFormat.term.uri
    ) == Literal("text/plain")


def test_bioschemas():
    crate = make_test_crate(recursive=False)
    crate.add_entity(
        bioschemas_drafts.LabProtocol("#some_protocol"),
        sdo.name(sdo.Text("Some Protocol")),
    )
    crate.validate()
    crate_json = json.loads(crate.compile())
    for entity in crate_json["@graph"]:
        assert "http" not in entity["@type"], "All terms should be shortened"

    assert crate_json["@context"] == [
        "https://w3id.org/ro/crate/1.1/context",
        {"LabProtocol": str(bioschemas_drafts.LabProtocol.term.uri)},
    ], "Only the terms that are used in the crate should be in the context"


def test_bnode():
    crate = make_test_crate(recursive=False)
    crate.add_entity(bioschemas_drafts.LabProtocol(BNode()))
    assert any(isinstance(id, BNode) for id in crate.graph.subjects())


def test_multi_type():
    class CustomType(rdfs.Class):
        term = RdfTerm("https://example.org/SomeOtherType")

    with tempfile.TemporaryDirectory() as tmpdir:
        crate = AttachedCrate(tmpdir)
        crate.add_entity(
            bioschemas_drafts.LabProtocol("#multi_type_entity"),
            CustomType.to_type_property(),
        )

        # We never want to redefine rdf:type
        assert str(rdf.type.term.uri) not in crate.context.to_dict().values()
        # But we should have the custom type in the context
        assert "https://example.org/SomeOtherType" in crate.context.to_dict().values()


def test_redefine_term(empty_crate: AttachedCrate):
    with pytest.raises(ValueError):
        empty_crate.register_term(
            RdfTerm("https://example.org/Thing", "Thing"),
        )


def test_add_metadata_term(empty_crate: AttachedCrate):
    """
    Test that terms used in `add_metadata` are registered in the context.
    """
    empty_crate.add_entity(
        sdo.Thing("#thing"),
        dc.valid(rdfs.Literal(Literal(True))),
    )
    # If valid can expand, it means it was correctly registered
    assert empty_crate.context.expand("valid") == "http://purl.org/dc/terms/valid"


def test_reverse_prop(empty_crate: AttachedCrate):
    """
    Test that we can add a reverse property to an entity.
    """
    empty_crate.add_entity(
        sdo.Thing("#thing"), sdo.hasPart.reverse(empty_crate.root_data_entity)
    )
    assert (
        empty_crate.root_data_entity.id,
        sdo.hasPart.term.uri,
        URIRef("#thing"),
    ) in empty_crate.graph


def test_adhoc_term(empty_crate: AttachedCrate):
    """
    Test that we can define terms on the fly and use them in properties.
    """
    thing = empty_crate.add_entity(
        sdo.Thing("#thing"),
        RdfProperty.adhoc(
            term=RdfTerm("https://example.org/myProp"), object=sdo.Text("value")
        ),
    )
    assert (
        thing.id,
        URIRef("https://example.org/myProp"),
        Literal("value"),
    ) in empty_crate.graph


def test_cls_with_term_label(empty_crate: AttachedCrate):
    """
    Test that we can use two types with the same term label, by renaming one of them.
    """
    thing = empty_crate.add_entity(
        sdo.Class("#thing"), owl.Class.with_term_label("owlClass").to_type_property()
    )
    assert (thing.id, RDF.type, sdo.Class.term.uri) in empty_crate.graph
    assert (thing.id, RDF.type, owl.Class.term.uri) in empty_crate.graph


def test_prop_with_term_label(empty_crate: AttachedCrate):
    """
    Test that we can use two properties with the same term label, by renaming one of them.
    """

    class exHasPart(RdfProperty):
        term = RdfTerm("https://example.org/hasPart", "hasPart")

    part = sdo.CreativeWork("https://example.org/part")

    with pytest.raises(ValueError):
        empty_crate.add_entity(
            sdo.Thing("#thing"),
            sdo.hasPart(part),
            exHasPart(part),
        )

    empty_crate.add_entity(
        sdo.Thing("#thing"),
        sdo.hasPart(part),
        exHasPart.with_term_label("exHasPart")(part),
    )


def test_adhoc_class(empty_crate: AttachedCrate):
    """
    Test that we can use two types with the same term label, by renaming one of them.
    """
    ExampleClass = RdfClass.adhoc(RdfTerm("https://example.org/thing"))
    empty_crate.add_entity(
        ExampleClass("#thing"),
    )
    assert (URIRef("#thing"), RDF.type, ExampleClass.term.uri) in empty_crate.graph


def test_spaces_in_path(empty_crate: AttachedCrate):
    """
    Test that we can register a file with spaces in the path.
    """
    path = empty_crate.root / "file with spaces.txt"
    path.touch()
    empty_crate.register_file(path)
    assert (
        URIRef("file%20with%20spaces.txt"),
        rdf.type.term.uri,
        roc.File.term.uri,
    ) in empty_crate.graph
