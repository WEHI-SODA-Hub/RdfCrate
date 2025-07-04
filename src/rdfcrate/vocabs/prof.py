from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import dc
from rdfcrate.rdftype import RdfType
from rdfcrate.vocabs import prof


class Profile(dc.Standard):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/Profile", "Profile")


class ResourceDescriptor(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/ns/dx/prof/ResourceDescriptor", "ResourceDescriptor"
    )


class ResourceRole(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/ResourceRole", "ResourceRole")


class hasToken(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/hasToken", "hasToken")


class hasArtifact(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/hasArtifact", "hasArtifact")


class isInheritedFrom(RdfProperty[prof.Profile]):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/isInheritedFrom", "isInheritedFrom")


class isProfileOf(RdfProperty[dc.Standard]):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/isProfileOf", "isProfileOf")


class isTransitiveProfileOf(RdfProperty[dc.Standard]):
    term = RdfTerm(
        "http://www.w3.org/ns/dx/prof/isTransitiveProfileOf", "isTransitiveProfileOf"
    )


class hasResource(RdfProperty[prof.ResourceDescriptor]):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/hasResource", "hasResource")


class hasRole(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/hasRole", "hasRole")
