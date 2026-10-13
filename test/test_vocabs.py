import pytest
from rdflib.plugins.shared.jsonld.context import Context

from rdfcrate.spec_version import ROCrate1_1, ROCrate1_2, SpecVersion
from rdfcrate.test_helpers import patch_rocrate_context
from rdfcrate.vocabs import Dct, Rdf, Sdo


@pytest.fixture(scope="function", autouse=True)
def rocrate_context():
    with patch_rocrate_context():
        yield


@pytest.mark.parametrize("version", [ROCrate1_1, ROCrate1_2])
def test_internal_terms_in_rocrate_context(version: SpecVersion):
    """
    The internal namespaces should only contain terms that the RO-Crate context already defines, with the same label.
    """
    context = Context(version.context_url)
    for namespace in [Sdo, Dct, Rdf]:
        for label, iri in namespace.jsonld_context().items():
            term = context.find_term(iri)
            assert term is not None, f"{iri} is not in the RO-Crate context"
            assert context.expand(label) == iri
