from pathlib import Path

from rdfcrate import AttachedCrate
from rdfcrate.vocabs import dc, sdo, roc, rdf, bioschemas_drafts, rdfs
from rdflib import Literal, Graph
import json
from datetime import datetime
import tempfile

TEST_CRATE = Path(__file__).parent / "test_crate"

MIT = sdo.CreativeWork("https://opensource.org/license/mit")
ME = sdo.Person("https://orcid.org/0000-0002-8965-2595")
WEHI_RCP = sdo.Organization("https://github.com/WEHI-ResearchComputing")

BASE_SUBJECTS = [MIT, ME, WEHI_RCP]

def make_test_crate(recursive: bool = False):
    crate = AttachedCrate(
        TEST_CRATE
    )

    crate.add_root_entity(
        sdo.name(sdo.Text("Test Crate")),
        sdo.description(sdo.Text("Crate for validating RdfCrate")),
        sdo.datePublished(sdo.DateTime(datetime.now().isoformat())),
        sdo.license(crate.add_entity(MIT, sdo.CreativeWork, sdo.name(sdo.Text("MIT License")))),
        sdo.version(sdo.Text("1.0")),
        sdo.publisher(wehi:=crate.add_entity(
            WEHI_RCP,
            sdo.Organization,
            sdo.name(sdo.Text("WEHI Research Computing Platform")),
            sdo.url(sdo.URL(WEHI_RCP))
        )),
        sdo.author(crate.add_entity(
            ME,
            sdo.Person,
            sdo.name(sdo.Text("Michael")),
            sdo.affiliation(wehi)
        )),
        recursive=recursive
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
        sdo.Dataset("./"),
        sdo.CreativeWork("ro-crate-metadata.json"),
        roc.File("text.txt"),
        *BASE_SUBJECTS
    }
    assert set(crate.graph.predicates()) >= {rdf.type.term.uri, sdo.about.term.uri, dc.conformsTo.term.uri}
    assert set(crate.graph.objects()) >= {roc.File.term.uri, sdo.Dataset.term.uri}

    crate.validate()

    # Check that we can round-trip the graph
    Graph().parse(data=crate.compile(), format="json-ld")


def test_recursive_add():
    crate = make_test_crate(recursive=True)
    assert set(crate.graph.subjects()) == {
        sdo.Dataset("./"),
        sdo.CreativeWork("ro-crate-metadata.json"),
        roc.File("text.txt"),
        roc.File("binary.bin"),
        sdo.Dataset("subdir/"),
        roc.File("subdir/more_text.txt"),
        *BASE_SUBJECTS
    }, "All files and directories should be in the crate"
    assert crate.graph.value(predicate=sdo.hasPart.term.uri, object=roc.File("subdir/more_text.txt")) == sdo.Dataset("subdir/"), "Recursive add should link the immediate child and parent via hasPart"
    crate.validate()


def test_mime_type():
    crate = make_test_crate(recursive=True)

    assert crate.graph.value(roc.File("text.txt"), sdo.encodingFormat.term.uri) == Literal(
        "text/plain"
    )

def test_bioschemas():
    crate = make_test_crate(recursive=False)
    crate.add_entity(
        "#some_protocol",
        bioschemas_drafts.LabProtocol,
        sdo.name(sdo.Text("Some Protocol")),
    )
    crate.validate()
    crate_json = json.loads(crate.compile())
    for entity in crate_json["@graph"]:
        assert "http" not in entity["@type"], "All terms should be shortened"

    assert crate_json["@context"] == [
        "https://w3id.org/ro/crate/1.1/context",
        {
            "LabProtocol": str(bioschemas_drafts.LabProtocol.term.uri)
        }
    ], "Only the terms that are used in the crate should be in the context"

def test_multi_type():
    with tempfile.TemporaryDirectory() as tmpdir:
        crate = AttachedCrate(tmpdir)
        crate.add_entity(
            "#multi_type_entity",
            bioschemas_drafts.LabProtocol,
            rdf.type(rdfs.Class("https://example.org/SomeOtherType")),
        )

        # We never want to redefine rdf:type
        assert str(rdf.type.term.uri) not in crate.context.to_dict().values()
