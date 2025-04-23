from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import dc
from rdfcrate.vocabs import prof


class Profile(dc.Standard):
    term = RdfTerm("Profile", "http://www.w3.org/ns/dx/prof/Profile", ["1.2-DRAFT"])


class hasToken(RdfProperty[Identifier]):
    term = RdfTerm("hasToken", "http://www.w3.org/ns/dx/prof/hasToken", ["1.2-DRAFT"])


class hasArtifact(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasArtifact", "http://www.w3.org/ns/dx/prof/hasArtifact", ["1.2-DRAFT"]
    )


class isInheritedFrom(RdfProperty[prof.Profile]):
    term = RdfTerm(
        "isInheritedFrom", "http://www.w3.org/ns/dx/prof/isInheritedFrom", []
    )


class isProfileOf(RdfProperty[dc.Standard]):
    term = RdfTerm(
        "isProfileOf", "http://www.w3.org/ns/dx/prof/isProfileOf", ["1.2-DRAFT"]
    )


class isTransitiveProfileOf(RdfProperty[dc.Standard]):
    term = RdfTerm(
        "isTransitiveProfileOf",
        "http://www.w3.org/ns/dx/prof/isTransitiveProfileOf",
        [],
    )


class hasResource(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasResource", "http://www.w3.org/ns/dx/prof/hasResource", ["1.2-DRAFT"]
    )


class hasRole(RdfProperty[Identifier]):
    term = RdfTerm("hasRole", "http://www.w3.org/ns/dx/prof/hasRole", ["1.2-DRAFT"])
