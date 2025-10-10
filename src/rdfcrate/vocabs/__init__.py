"""
All objects in this module are re-exports from submodules.
"""

from rdfcrate.vocabs import (
    bioschemas,
    bioschemas_drafts,
    rocrate,
    dc,
    geo,
    owl,
    pav,
    pcdm,
    prof,
    prov,
    rdf,
    rdfs,
    schemaorg,
)

sdo = schemaorg
roc = rocrate

__all__ = [
    "bioschemas",
    "bioschemas_drafts",
    "rocrate",
    "dc",
    "geo",
    "owl",
    "pav",
    "pcdm",
    "prof",
    "prov",
    "rdf",
    "rdfs",
    "schemaorg",
    "sdo",
    "roc",
]
