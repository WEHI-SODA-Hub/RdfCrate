from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfType


class isPrimaryTopicOf(RdfProperty[RdfType]):
    term = RdfTerm("http://xmlns.com/foaf/0.1/isPrimaryTopicOf", "isPrimaryTopicOf")


class name(RdfProperty[RdfType]):
    term = RdfTerm("http://xmlns.com/foaf/0.1/name", "name")


class authoredOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/authoredOn", "authoredOn")


class contributedOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/contributedOn", "contributedOn")


class createdOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/createdOn", "createdOn")


class curatedOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/curatedOn", "curatedOn")


class importedOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/importedOn", "importedOn")


class lastRefreshedOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/lastRefreshedOn", "lastRefreshedOn")


class lastUpdateOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/lastUpdateOn", "lastUpdateOn")


class retrievedOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/retrievedOn", "retrievedOn")


class sourceAccessedOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/sourceAccessedOn", "sourceAccessedOn")


class sourceLastAccessedOn(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/sourceLastAccessedOn", "sourceLastAccessedOn")


class version(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/version", "version")


class authoredBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/authoredBy", "authoredBy")


class contributedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/contributedBy", "contributedBy")


class createdAt(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/createdAt", "createdAt")


class createdBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/createdBy", "createdBy")


class createdWith(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/createdWith", "createdWith")


class curatedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/curatedBy", "curatedBy")


class curates(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/curates", "curates")


class derivedFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/derivedFrom", "derivedFrom")


class hasCurrentVersion(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/hasCurrentVersion", "hasCurrentVersion")


class hasEarlierVersion(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/hasEarlierVersion", "hasEarlierVersion")


class hasVersion(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/hasVersion", "hasVersion")


class importedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/importedBy", "importedBy")


class importedFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/importedFrom", "importedFrom")


class previousVersion(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/previousVersion", "previousVersion")


class providedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/providedBy", "providedBy")


class retrievedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/retrievedBy", "retrievedBy")


class retrievedFrom(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/retrievedFrom", "retrievedFrom")


class sourceAccessedAt(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/sourceAccessedAt", "sourceAccessedAt")


class sourceAccessedBy(RdfProperty[RdfType]):
    term = RdfTerm("http://purl.org/pav/sourceAccessedBy", "sourceAccessedBy")


class generalizationOf(RdfProperty[RdfType]):
    term = RdfTerm("http://www.w3.org/ns/prov#generalizationOf", "generalizationOf")
