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
    term = RdfTerm('Profile', 'http://www.w3.org/ns/dx/prof/Profile', [])

@dataclass(frozen=True)
class hasToken(RdfProperty):
    term = RdfTerm('hasToken', 'http://www.w3.org/ns/dx/prof/hasToken', ['1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class hasArtifact(RdfProperty):
    term = RdfTerm('hasArtifact', 'http://www.w3.org/ns/dx/prof/hasArtifact', ['1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class isInheritedFrom(RdfProperty):
    term = RdfTerm('isInheritedFrom', 'http://www.w3.org/ns/dx/prof/isInheritedFrom', [])
    object: prof.Profile

@dataclass(frozen=True)
class isProfileOf(RdfProperty):
    term = RdfTerm('isProfileOf', 'http://www.w3.org/ns/dx/prof/isProfileOf', ['1.2-DRAFT'])
    object: dc.Standard

@dataclass(frozen=True)
class isTransitiveProfileOf(RdfProperty):
    term = RdfTerm('isTransitiveProfileOf', 'http://www.w3.org/ns/dx/prof/isTransitiveProfileOf', [])
    object: dc.Standard

@dataclass(frozen=True)
class hasResource(RdfProperty):
    term = RdfTerm('hasResource', 'http://www.w3.org/ns/dx/prof/hasResource', ['1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class hasRole(RdfProperty):
    term = RdfTerm('hasRole', 'http://www.w3.org/ns/dx/prof/hasRole', ['1.2-DRAFT'])
    object: Identifier