from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass


class isPrimaryTopicOf(RdfProperty[Identifier]):
    term = RdfTerm("isPrimaryTopicOf", "http://xmlns.com/foaf/0.1/isPrimaryTopicOf", [])


class name(RdfProperty[Identifier]):
    term = RdfTerm("name", "http://xmlns.com/foaf/0.1/name", [])


class authoredOn(RdfProperty[Identifier]):
    term = RdfTerm("authoredOn", "http://purl.org/pav/authoredOn", [])


class contributedOn(RdfProperty[Identifier]):
    term = RdfTerm("contributedOn", "http://purl.org/pav/contributedOn", [])


class createdOn(RdfProperty[Identifier]):
    term = RdfTerm("createdOn", "http://purl.org/pav/createdOn", [])


class curatedOn(RdfProperty[Identifier]):
    term = RdfTerm("curatedOn", "http://purl.org/pav/curatedOn", [])


class importedOn(RdfProperty[Identifier]):
    term = RdfTerm(
        "importedOn",
        "http://purl.org/pav/importedOn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class lastRefreshedOn(RdfProperty[Identifier]):
    term = RdfTerm("lastRefreshedOn", "http://purl.org/pav/lastRefreshedOn", [])


class lastUpdateOn(RdfProperty[Identifier]):
    term = RdfTerm("lastUpdateOn", "http://purl.org/pav/lastUpdateOn", [])


class retrievedOn(RdfProperty[Identifier]):
    term = RdfTerm(
        "retrievedOn",
        "http://purl.org/pav/retrievedOn",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class sourceAccessedOn(RdfProperty[Identifier]):
    term = RdfTerm("sourceAccessedOn", "http://purl.org/pav/sourceAccessedOn", [])


class sourceLastAccessedOn(RdfProperty[Identifier]):
    term = RdfTerm(
        "sourceLastAccessedOn", "http://purl.org/pav/sourceLastAccessedOn", []
    )


class version(RdfProperty[Identifier]):
    term = RdfTerm("version", "http://purl.org/pav/version", [])


class authoredBy(RdfProperty[Identifier]):
    term = RdfTerm("authoredBy", "http://purl.org/pav/authoredBy", [])


class contributedBy(RdfProperty[Identifier]):
    term = RdfTerm("contributedBy", "http://purl.org/pav/contributedBy", [])


class createdAt(RdfProperty[Identifier]):
    term = RdfTerm("createdAt", "http://purl.org/pav/createdAt", [])


class createdBy(RdfProperty[Identifier]):
    term = RdfTerm("createdBy", "http://purl.org/pav/createdBy", [])


class createdWith(RdfProperty[Identifier]):
    term = RdfTerm("createdWith", "http://purl.org/pav/createdWith", [])


class curatedBy(RdfProperty[Identifier]):
    term = RdfTerm("curatedBy", "http://purl.org/pav/curatedBy", [])


class curates(RdfProperty[Identifier]):
    term = RdfTerm("curates", "http://purl.org/pav/curates", [])


class derivedFrom(RdfProperty[Identifier]):
    term = RdfTerm("derivedFrom", "http://purl.org/pav/derivedFrom", [])


class hasCurrentVersion(RdfProperty[Identifier]):
    term = RdfTerm("hasCurrentVersion", "http://purl.org/pav/hasCurrentVersion", [])


class hasEarlierVersion(RdfProperty[Identifier]):
    term = RdfTerm("hasEarlierVersion", "http://purl.org/pav/hasEarlierVersion", [])


class hasVersion(RdfProperty[Identifier]):
    term = RdfTerm("hasVersion", "http://purl.org/pav/hasVersion", [])


class importedBy(RdfProperty[Identifier]):
    term = RdfTerm(
        "importedBy",
        "http://purl.org/pav/importedBy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class importedFrom(RdfProperty[Identifier]):
    term = RdfTerm(
        "importedFrom",
        "http://purl.org/pav/importedFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class previousVersion(RdfProperty[Identifier]):
    term = RdfTerm("previousVersion", "http://purl.org/pav/previousVersion", [])


class providedBy(RdfProperty[Identifier]):
    term = RdfTerm("providedBy", "http://purl.org/pav/providedBy", [])


class retrievedBy(RdfProperty[Identifier]):
    term = RdfTerm(
        "retrievedBy",
        "http://purl.org/pav/retrievedBy",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class retrievedFrom(RdfProperty[Identifier]):
    term = RdfTerm(
        "retrievedFrom",
        "http://purl.org/pav/retrievedFrom",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class sourceAccessedAt(RdfProperty[Identifier]):
    term = RdfTerm("sourceAccessedAt", "http://purl.org/pav/sourceAccessedAt", [])


class sourceAccessedBy(RdfProperty[Identifier]):
    term = RdfTerm("sourceAccessedBy", "http://purl.org/pav/sourceAccessedBy", [])


class generalizationOf(RdfProperty[Identifier]):
    term = RdfTerm("generalizationOf", "http://www.w3.org/ns/prov#generalizationOf", [])
