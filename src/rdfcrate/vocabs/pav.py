from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass

@dataclass(frozen=True)
class authoredOn(RdfProperty):
    term = RdfTerm('authoredOn', 'http://purl.org/pav/authoredOn', [])
    object: Identifier

@dataclass(frozen=True)
class contributedOn(RdfProperty):
    term = RdfTerm('contributedOn', 'http://purl.org/pav/contributedOn', [])
    object: Identifier

@dataclass(frozen=True)
class createdOn(RdfProperty):
    term = RdfTerm('createdOn', 'http://purl.org/pav/createdOn', [])
    object: Identifier

@dataclass(frozen=True)
class curatedOn(RdfProperty):
    term = RdfTerm('curatedOn', 'http://purl.org/pav/curatedOn', [])
    object: Identifier

@dataclass(frozen=True)
class importedOn(RdfProperty):
    term = RdfTerm('importedOn', 'http://purl.org/pav/importedOn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class lastRefreshedOn(RdfProperty):
    term = RdfTerm('lastRefreshedOn', 'http://purl.org/pav/lastRefreshedOn', [])
    object: Identifier

@dataclass(frozen=True)
class lastUpdateOn(RdfProperty):
    term = RdfTerm('lastUpdateOn', 'http://purl.org/pav/lastUpdateOn', [])
    object: Identifier

@dataclass(frozen=True)
class retrievedOn(RdfProperty):
    term = RdfTerm('retrievedOn', 'http://purl.org/pav/retrievedOn', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class sourceAccessedOn(RdfProperty):
    term = RdfTerm('sourceAccessedOn', 'http://purl.org/pav/sourceAccessedOn', [])
    object: Identifier

@dataclass(frozen=True)
class sourceLastAccessedOn(RdfProperty):
    term = RdfTerm('sourceLastAccessedOn', 'http://purl.org/pav/sourceLastAccessedOn', [])
    object: Identifier

@dataclass(frozen=True)
class version(RdfProperty):
    term = RdfTerm('version', 'http://purl.org/pav/version', [])
    object: Identifier

@dataclass(frozen=True)
class authoredBy(RdfProperty):
    term = RdfTerm('authoredBy', 'http://purl.org/pav/authoredBy', [])
    object: Identifier

@dataclass(frozen=True)
class contributedBy(RdfProperty):
    term = RdfTerm('contributedBy', 'http://purl.org/pav/contributedBy', [])
    object: Identifier

@dataclass(frozen=True)
class createdAt(RdfProperty):
    term = RdfTerm('createdAt', 'http://purl.org/pav/createdAt', [])
    object: Identifier

@dataclass(frozen=True)
class createdBy(RdfProperty):
    term = RdfTerm('createdBy', 'http://purl.org/pav/createdBy', [])
    object: Identifier

@dataclass(frozen=True)
class createdWith(RdfProperty):
    term = RdfTerm('createdWith', 'http://purl.org/pav/createdWith', [])
    object: Identifier

@dataclass(frozen=True)
class curatedBy(RdfProperty):
    term = RdfTerm('curatedBy', 'http://purl.org/pav/curatedBy', [])
    object: Identifier

@dataclass(frozen=True)
class curates(RdfProperty):
    term = RdfTerm('curates', 'http://purl.org/pav/curates', [])
    object: Identifier

@dataclass(frozen=True)
class derivedFrom(RdfProperty):
    term = RdfTerm('derivedFrom', 'http://purl.org/pav/derivedFrom', [])
    object: Identifier

@dataclass(frozen=True)
class hasCurrentVersion(RdfProperty):
    term = RdfTerm('hasCurrentVersion', 'http://purl.org/pav/hasCurrentVersion', [])
    object: Identifier

@dataclass(frozen=True)
class hasEarlierVersion(RdfProperty):
    term = RdfTerm('hasEarlierVersion', 'http://purl.org/pav/hasEarlierVersion', [])
    object: Identifier

@dataclass(frozen=True)
class hasVersion(RdfProperty):
    term = RdfTerm('hasVersion', 'http://purl.org/pav/hasVersion', [])
    object: Identifier

@dataclass(frozen=True)
class importedBy(RdfProperty):
    term = RdfTerm('importedBy', 'http://purl.org/pav/importedBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class importedFrom(RdfProperty):
    term = RdfTerm('importedFrom', 'http://purl.org/pav/importedFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class previousVersion(RdfProperty):
    term = RdfTerm('previousVersion', 'http://purl.org/pav/previousVersion', [])
    object: Identifier

@dataclass(frozen=True)
class providedBy(RdfProperty):
    term = RdfTerm('providedBy', 'http://purl.org/pav/providedBy', [])
    object: Identifier

@dataclass(frozen=True)
class retrievedBy(RdfProperty):
    term = RdfTerm('retrievedBy', 'http://purl.org/pav/retrievedBy', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class retrievedFrom(RdfProperty):
    term = RdfTerm('retrievedFrom', 'http://purl.org/pav/retrievedFrom', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
    object: Identifier

@dataclass(frozen=True)
class sourceAccessedAt(RdfProperty):
    term = RdfTerm('sourceAccessedAt', 'http://purl.org/pav/sourceAccessedAt', [])
    object: Identifier

@dataclass(frozen=True)
class sourceAccessedBy(RdfProperty):
    term = RdfTerm('sourceAccessedBy', 'http://purl.org/pav/sourceAccessedBy', [])
    object: Identifier

@dataclass(frozen=True)
class generalizationOf(RdfProperty):
    term = RdfTerm('generalizationOf', 'http://www.w3.org/ns/prov#generalizationOf', [])
    object: Identifier