from rdflib import RDF, URIRef

from rdfcrate.namespace import ContextNamespace


class Obi(ContextNamespace, context_prefix="obi"):
    _base = URIRef("http://purl.obolibrary.org/obo/")
    Image = _base + "IAO_0000101"
    plasmaCell = _base + "CL_0000786"
    external = URIRef("https://example.org/external")


class Sdo(ContextNamespace):
    _base = URIRef("http://schema.org/")
    name = _base + "name"
    description = _base + "description"


class Rdf(ContextNamespace):
    _base = URIRef(str(RDF))
    type_ = _base + "type"
    Property = _base + "Property"


class Unprefixed(ContextNamespace):
    _base = URIRef("https://example.org/")
    type_ = _base + "type"


def test_attribute_access():
    """
    Accessing the attributes of the namespace should return full absolute URIRefs.
    """
    assert Obi.Image == URIRef("http://purl.obolibrary.org/obo/IAO_0000101")
    assert isinstance(Obi.plasmaCell, URIRef)


def test_curies():
    """
    If both `context_prefix` and `_base` are set, terms should be CURIEs, with the prefix defined in the context.
    Terms not under `_base` should use full IRIs.
    """
    assert Obi.jsonld_context() == {
        "obi": "http://purl.obolibrary.org/obo/",
        "obiImage": "obi:IAO_0000101",
        "obiPlasmaCell": "obi:CL_0000786",
        "obiExternal": "https://example.org/external",
    }


def test_full_iris_without_prefix():
    """
    If `context_prefix` is not set, terms should use full IRIs and unprefixed labels.
    """
    assert Sdo.jsonld_context() == {
        "name": "http://schema.org/name",
        "description": "http://schema.org/description",
    }


def test_rdf_type_excluded():
    """
    `rdf:type` should never be in the context, since JSON-LD uses `@type`.
    """
    assert Rdf.jsonld_context() == {
        "Property": "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"
    }


def test_trailing_underscore():
    """
    Trailing underscores, which avoid clashes with Python names, should be removed from the label.
    """
    assert Unprefixed.jsonld_context() == {"type": "https://example.org/type"}


def test_iri_filter():
    """
    Only the requested IRIs should be included. The prefix should only be defined if a CURIE uses it.
    """
    assert Obi.jsonld_context(iris=[Obi.Image]) == {
        "obi": "http://purl.obolibrary.org/obo/",
        "obiImage": "obi:IAO_0000101",
    }
    assert Obi.jsonld_context(iris=[Obi.external]) == {
        "obiExternal": "https://example.org/external"
    }
    assert Obi.jsonld_context(iris=[]) == {}


def test_excludes_internal_attributes():
    """
    Attributes starting with "_" should not be included in the JSON-LD context.
    """
    context = Obi.jsonld_context()
    assert "_base" not in context
    assert "_context_prefix" not in context


def test_subclass_inherits_terms_and_prefix():
    """
    Subclassing a namespace should keep its terms and prefix, allowing it to be extended.
    """

    class ObiExtended(Obi):
        Assay = Obi._base + "OBI_0000070"

    assert ObiExtended.jsonld_context(iris=[ObiExtended.Assay, Obi.Image]) == {
        "obi": "http://purl.obolibrary.org/obo/",
        "obiAssay": "obi:OBI_0000070",
        "obiImage": "obi:IAO_0000101",
    }
