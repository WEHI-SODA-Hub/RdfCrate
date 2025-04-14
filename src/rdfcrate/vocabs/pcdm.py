from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import pcdm


class Collection(RdfClass):
    term = RdfTerm("Collection", "http://pcdm.org/models#Collection", [])


class Object(RdfClass):
    term = RdfTerm("Object", "http://pcdm.org/models#Object", [])


class File(RdfClass):
    term = RdfTerm("File", "http://pcdm.org/models#File", [])


class AlternateOrder(Object):
    term = RdfTerm("AlternateOrder", "http://pcdm.org/models#AlternateOrder", [])


@dataclass(frozen=True)
class hasFile(RdfProperty):
    term = RdfTerm(
        "hasFile", "http://pcdm.org/models#hasFile", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: pcdm.File


@dataclass(frozen=True)
class fileOf(RdfProperty):
    term = RdfTerm("fileOf", "http://pcdm.org/models#fileOf", [])
    object: pcdm.Object


@dataclass(frozen=True)
class hasMember(RdfProperty):
    term = RdfTerm(
        "hasMember",
        "http://pcdm.org/models#hasMember",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class memberOf(RdfProperty):
    term = RdfTerm("memberOf", "http://pcdm.org/models#memberOf", [])
    object: Identifier


@dataclass(frozen=True)
class hasRelatedObject(RdfProperty):
    term = RdfTerm("hasRelatedObject", "http://pcdm.org/models#hasRelatedObject", [])
    object: pcdm.Object


@dataclass(frozen=True)
class relatedObjectOf(RdfProperty):
    term = RdfTerm("relatedObjectOf", "http://pcdm.org/models#relatedObjectOf", [])
    object: Identifier
