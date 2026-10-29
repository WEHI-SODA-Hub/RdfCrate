import json
import tempfile
from datetime import UTC, datetime
from pathlib import Path

import pytest
from rdflib import DCTERMS, RDF, Graph, Literal, URIRef

from rdfcrate import AttachedCrate, ContextNamespace
from rdfcrate.test_helpers import patch_rocrate_context
from rdfcrate.wrapper import SCHEMA

TEST_CRATE = Path(__file__).parent / "test_crate"

MIT = URIRef("https://opensource.org/license/mit")
ME = URIRef("https://orcid.org/0000-0002-8965-2595")
WEHI_RCP = URIRef("https://github.com/WEHI-ResearchComputing")

BASE_SUBJECTS = [MIT, ME, WEHI_RCP]


class Obi(ContextNamespace, prefix="obi"):
    _base = URIRef("http://purl.obolibrary.org/obo/")
    Image = _base + "IAO_0000101"


class OmeroCrate(ContextNamespace):
    _base = URIRef("https://w3id.org/WEHI-SODA-Hub/omerocrate/")
    upload = _base + "upload"


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

    wehi = crate.add_entity(
        WEHI_RCP,
        (RDF.type, SCHEMA.Organization),
        (SCHEMA.name, Literal("WEHI Research Computing Platform")),
        (SCHEMA.url, Literal(WEHI_RCP)),
    )
    crate.add_root_entity(
        "Test Crate",
        "Crate for validating RdfCrate",
        datetime.now(UTC),
        crate.add_entity(
            MIT, (RDF.type, SCHEMA.CreativeWork), (SCHEMA.name, Literal("MIT License"))
        ),
        (SCHEMA.version, Literal("1.0")),
        (SCHEMA.publisher, wehi),
        (
            SCHEMA.author,
            crate.add_entity(
                ME,
                (RDF.type, SCHEMA.Person),
                (SCHEMA.name, Literal("Michael")),
                (SCHEMA.affiliation, wehi),
            ),
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
        RDF.type,
        SCHEMA.about,
        DCTERMS.conformsTo,
    }
    assert set(crate.graph.objects()) >= {SCHEMA.MediaObject, SCHEMA.Dataset}

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
        predicate=SCHEMA.hasPart, object=URIRef("subdir/more_text.txt")
    ) == URIRef("subdir/"), (
        "Recursive add should link the immediate child and parent via hasPart"
    )
    crate.validate()


def test_mime_type():
    crate = make_test_crate(recursive=True)

    assert crate.graph.value(URIRef("text.txt"), SCHEMA.encodingFormat) == Literal(
        "text/plain"
    )


def test_spaces_in_path(empty_crate: AttachedCrate):
    """
    Test that we can register a file with spaces in the path.
    """
    path = empty_crate.root / "file with spaces.txt"
    path.touch()
    empty_crate.register_file(path)
    assert (
        URIRef("file%20with%20spaces.txt"),
        RDF.type,
        SCHEMA.MediaObject,
    ) in empty_crate.graph


def test_rocrate_terms_not_in_context():
    """
    Terms that are already in the RO-Crate context should not be added to the custom context.
    """
    crate = make_test_crate(recursive=True)
    crate_json = json.loads(crate.compile())
    assert crate_json["@context"] == "https://w3id.org/ro/crate/1.1/context"
    file = next(e for e in crate_json["@graph"] if e["@id"] == "text.txt")
    assert file["@type"] == "File"


def test_custom_vocabs():
    """
    Terms that aren't in the RO-Crate context should be added to the context from the crate's vocabs.
    """
    crate = make_test_crate()
    crate.vocabs += [Obi, OmeroCrate]
    crate.register_file(
        "text.txt",
        (SCHEMA.name, Literal("COMET Image")),
        (RDF.type, Obi.Image),
        (OmeroCrate.upload, Literal(True)),
    )
    crate_json = json.loads(crate.compile())

    assert crate_json["@context"] == [
        "https://w3id.org/ro/crate/1.1/context",
        {
            "Image": "http://purl.obolibrary.org/obo/IAO_0000101",
            "upload": "https://w3id.org/WEHI-SODA-Hub/omerocrate/upload",
        },
    ]
    file = next(e for e in crate_json["@graph"] if e["@id"] == "text.txt")
    assert set(file["@type"]) == {"File", "Image"}
    assert file["upload"] is True

    # Check that we can round-trip the graph
    assert len(Graph().parse(data=crate.compile(), format="json-ld")) == len(
        crate.graph
    )


def test_clash_with_rocrate_context():
    """
    A vocab term that has the same label as a different term in the RO-Crate context should raise an error.
    """

    class Example(ContextNamespace):
        name = URIRef("https://example.org/name")

    crate = make_test_crate()
    crate.vocabs.append(Example)
    crate.add_entity("./", (Example.name, Literal("Other name")))
    with pytest.raises(ValueError, match="already defined"):
        crate.compile()


def test_missing_term():
    """
    Using an IRI that isn't in the RO-Crate context or any vocab should raise an error.
    """
    crate = make_test_crate()
    crate.add_entity("./", (URIRef("https://example.org/undefined"), Literal("x")))
    with pytest.raises(ValueError, match="https://example.org/undefined"):
        crate.compile()
