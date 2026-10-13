"""
Minimal namespaces for the terms that RdfCrate uses internally to build RO-Crates.

These are all defined in the RO-Crate context, so they never add to the output context.
To use other terms, subclass these, or define your own `ContextNamespace`.
"""

from rdflib import RDF, URIRef

from rdfcrate.namespace import ContextNamespace
from rdfcrate.vocabs import (
    bioschemas,
    bioschemas_drafts,
    dc,
    geo,
    owl,
    pav,
    pcdm,
    prof,
    prov,
    rdf,
    rdfs,
    rocrate,
    schemaorg,
)


class Sdo(ContextNamespace):
    _base = URIRef("http://schema.org/")
    # Classes
    CreativeWork = _base + "CreativeWork"
    Dataset = _base + "Dataset"
    File = _base + "MediaObject"
    # Properties
    about = _base + "about"
    contentSize = _base + "contentSize"
    datePublished = _base + "datePublished"
    description = _base + "description"
    encodingFormat = _base + "encodingFormat"
    hasPart = _base + "hasPart"
    license = _base + "license"
    name = _base + "name"


class Dct(ContextNamespace):
    _base = URIRef("http://purl.org/dc/terms/")
    conformsTo = _base + "conformsTo"


class Rdf(ContextNamespace):
    _base = URIRef(str(RDF))
    type_ = _base + "type"


sdo = schemaorg
roc = rocrate

__all__ = [
    "Dct",
    "Rdf",
    "Sdo",
    "bioschemas",
    "bioschemas_drafts",
    "dc",
    "geo",
    "owl",
    "pav",
    "pcdm",
    "prof",
    "prov",
    "rdf",
    "rdfs",
    "roc",
    "rocrate",
    "schemaorg",
    "sdo",
]
