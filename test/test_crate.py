from pathlib import Path
from rdfcrate import uris, AttachedCrate, spec_version
from rdflib import RDF, Literal, URIRef, Graph
import json
from datetime import datetime

TEST_CRATE = Path(__file__).parent / "test_crate"

def test_spec_conformant():
    crate = AttachedCrate(path=TEST_CRATE, recursive_init=False, version=spec_version.ROCrate1_1)
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
    crate = AttachedCrate(path=TEST_CRATE)
    crate.register_file("text.txt")

    # Check that the graph has the expected structure
    assert set(crate.graph.subjects()) == {URIRef("./"), URIRef("ro-crate-metadata.json"), URIRef("text.txt")}
    assert set(crate.graph.predicates()) >= {RDF.type, uris.about, uris.conformsTo}
    assert set(crate.graph.objects()) >= {uris.File, uris.Dataset}

    # Check that we can round-trip the graph
    Graph().parse(data=crate.compile(), format="json-ld")

def test_recursive_add():
    crate = AttachedCrate(path=TEST_CRATE, recursive_init=True)
    assert set(crate.graph.subjects()) == {URIRef("./"), URIRef("ro-crate-metadata.json"), URIRef("text.txt"), URIRef("binary.bin"), URIRef("subdir/"), URIRef("subdir/more_text.txt")}, "All files and directories should be in the crate"
    assert set(crate.graph.objects(URIRef("./"), uris.hasPart)) == {URIRef("ro-crate-metadata.json"), URIRef("text.txt"), URIRef("binary.bin"), URIRef("subdir/")}, "Root should have all files and directories as parts"

def test_mime_type():
    crate = AttachedCrate(path=TEST_CRATE, recursive_init=True)
    
    assert crate.graph.value(URIRef("text.txt"), uris.encodingFormat) == Literal("text/plain")
    assert crate.graph.value(URIRef("ro-crate-metadata.json"), uris.encodingFormat) == Literal("application/json")
