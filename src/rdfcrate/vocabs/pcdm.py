from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import pcdm
from rdfcrate.rdftype import RdfType


class Collection(RdfClass):
    term = RdfTerm("http://pcdm.org/models#Collection", "Collection")


class Object(RdfClass):
    term = RdfTerm("http://pcdm.org/models#Object", "Object")


class File(RdfClass):
    term = RdfTerm("http://pcdm.org/models#File", "File")


class AlternateOrder(Object):
    term = RdfTerm("http://pcdm.org/models#AlternateOrder", "AlternateOrder")


class hasFile(RdfProperty[pcdm.File]):
    term = RdfTerm("http://pcdm.org/models#hasFile", "hasFile")


class fileOf(RdfProperty[pcdm.Object]):
    term = RdfTerm("http://pcdm.org/models#fileOf", "fileOf")


class hasMember(RdfProperty[RdfType]):
    term = RdfTerm("http://pcdm.org/models#hasMember", "hasMember")


class memberOf(RdfProperty[RdfType]):
    term = RdfTerm("http://pcdm.org/models#memberOf", "memberOf")


class hasRelatedObject(RdfProperty[pcdm.Object]):
    term = RdfTerm("http://pcdm.org/models#hasRelatedObject", "hasRelatedObject")


class relatedObjectOf(RdfProperty[RdfType]):
    term = RdfTerm("http://pcdm.org/models#relatedObjectOf", "relatedObjectOf")
