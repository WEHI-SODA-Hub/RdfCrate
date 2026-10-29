from rdflib import RDF, URIRef

from rdfcrate.namespace import ContextNamespace


class Obi(ContextNamespace, prefix="obi"):
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


def test_terms():
    """
    `terms()` should yield each public URIRef attribute with its absolute IRI.
    """
    assert dict(Obi.terms()) == {
        "Image": URIRef("http://purl.obolibrary.org/obo/IAO_0000101"),
        "plasmaCell": URIRef("http://purl.obolibrary.org/obo/CL_0000786"),
        "external": URIRef("https://example.org/external"),
    }
    assert dict(Sdo.terms()) == {
        "name": URIRef("http://schema.org/name"),
        "description": URIRef("http://schema.org/description"),
    }


def test_terms_keep_trailing_underscore():
    """
    Attribute names are yielded as written, including trailing underscores.
    """
    assert dict(Unprefixed.terms()) == {"type_": URIRef("https://example.org/type")}
    assert dict(Rdf.terms()) == {
        "type_": RDF.type,
        "Property": RDF.Property,
    }


def test_terms_exclude_internal_attributes():
    """
    Attributes starting with "_" should not be yielded.
    """
    assert all(not term.startswith("_") for term, _ in Obi.terms())


def test_subclass_inherits_terms():
    """
    Subclassing a namespace should keep its terms, allowing it to be extended.
    """

    class ObiExtended(Obi):
        Assay = Obi._base + "OBI_0000070"

    assert dict(ObiExtended.terms()) == {
        **dict(Obi.terms()),
        "Assay": URIRef("http://purl.obolibrary.org/obo/OBI_0000070"),
    }
