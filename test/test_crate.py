from pathlib import Path
from rdfcrate import uris, AttachedCrate
from rdflib import RDF, Literal, URIRef, Graph

TEST_CRATE = Path(__file__).parent / "test_crate"

def test_single_file():
    crate = AttachedCrate(path=TEST_CRATE)
    crate.register_file("text.txt")

    # Check that the graph has the expected structure
    assert set(crate.graph.subjects()) == {URIRef("."), URIRef("ro-crate-metadata.json"), URIRef("text.txt")}
    assert set(crate.graph.predicates()) >= {RDF.type, uris.about, uris.conformsTo}
    assert set(crate.graph.objects()) >= {uris.File, uris.Dataset}

    # Check that we can round-trip the graph
    Graph().parse(data=crate.compile(), format="json-ld")

def test_recursive_add():
    crate = AttachedCrate(path=TEST_CRATE, recursive_init=True)
    assert set(crate.graph.subjects()) == {URIRef("."), URIRef("ro-crate-metadata.json"), URIRef("text.txt"), URIRef("binary.bin"), URIRef("subdir"), URIRef("subdir/more_text.txt")}, "All files and directories should be in the crate"
    assert set(crate.graph.objects(URIRef("."), uris.hasPart)) == {URIRef("ro-crate-metadata.json"), URIRef("text.txt"), URIRef("binary.bin"), URIRef("subdir")}, "Root should have all files and directories as parts"

def test_mime_type():
    crate = AttachedCrate(path=TEST_CRATE, recursive_init=True)
    
    assert crate.graph.value(URIRef("text.txt"), uris.encodingFormat) == Literal("text/plain")
    assert crate.graph.value(URIRef("ro-crate-metadata.json"), uris.encodingFormat) == Literal("application/json")
