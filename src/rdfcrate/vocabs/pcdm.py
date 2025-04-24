from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import pcdm


class Collection(RdfClass):
    term = RdfTerm("Collection", "http://pcdm.org/models#Collection", [])


class Object(RdfClass):
    term = RdfTerm("Object", "http://pcdm.org/models#Object", [])


class File(RdfClass):
    term = RdfTerm("File", "http://pcdm.org/models#File", [])


class AlternateOrder(Object):
    term = RdfTerm("AlternateOrder", "http://pcdm.org/models#AlternateOrder", [])


class hasFile(RdfProperty[pcdm.File]):
    term = RdfTerm(
        "hasFile", "http://pcdm.org/models#hasFile", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class fileOf(RdfProperty[pcdm.Object]):
    term = RdfTerm("fileOf", "http://pcdm.org/models#fileOf", [])


class hasMember(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMember",
        "http://pcdm.org/models#hasMember",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class memberOf(RdfProperty[Identifier]):
    term = RdfTerm("memberOf", "http://pcdm.org/models#memberOf", [])


class hasRelatedObject(RdfProperty[pcdm.Object]):
    term = RdfTerm("hasRelatedObject", "http://pcdm.org/models#hasRelatedObject", [])


class relatedObjectOf(RdfProperty[Identifier]):
    term = RdfTerm("relatedObjectOf", "http://pcdm.org/models#relatedObjectOf", [])
