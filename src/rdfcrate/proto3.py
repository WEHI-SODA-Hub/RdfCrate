from __future__ import annotations
from dataclasses import dataclass
from typing import Annotated, ClassVar, TypedDict

from rdflib import Literal, URIRef
from rdflib.term import Identifier

type ContextEntry[T: Literal] = Annotated[Identifier, T]


# Types
# AMRadioChannel = RdfType( URIRef, "http://schema.org/AMRadioChannel"]
AMRadioChannel = Annotated[URIRef, "http://schema.org/AMRadioChannel"]
APIReference = Annotated[Identifier, "http://schema.org/APIReference"]
Abdomen = Annotated[Identifier, "http://schema.org/Abdomen"]

# Properties
actors = ("http://schema.org/actors",)
addOn = ("http://schema.org/addOn",)


class RoCrateContext(TypedDict, total=False):
    AMRadioChannel: Annotated[Identifier, "http://schema.org/AMRadioChannel"]
    APIReference: Annotated[Identifier, "http://schema.org/APIReference"]
    Abdomen: Annotated[Identifier, "http://schema.org/Abdomen"]


class BioschemasContext(RoCrateContext, total=False):
    BioChemEntity: Annotated[Identifier, "https://bioschemas.org/terms/BioChemEntity"]
    BioSample: Annotated[Identifier, "https://bioschemas.org/terms/BioSample"]


@dataclass
class AbstractRoCrate[T: RoCrateContext]:
    context: type[T]

    def add_root_entity(
        self, id: URIRef, objects: T | None = None, subjects: T | None = None
    ): ...


# class RoCrate(AbstractRoCrate[RoCrateContext]):

crate = AbstractRoCrate(BioschemasContext)
crate.add_root_entity(
    URIRef(""),
    objects=BioschemasContext(APIReference=URIRef("")),
)


@dataclass(frozen=True)
class RdfType:
    class_uri: ClassVar[URIRef]


@dataclass(frozen=True)
class RdfProperty:
    uri: ClassVar[URIRef]
    value: RdfType


# @dataclass(frozen=True)
# class about(RdfProperty):
#     uri = URIRef("http://schema.org/about")
#     # range
#     value: Thing

about = Annotated["Thing", "http://schema.org/about"]


@dataclass(frozen=True)
class Thing(RdfType):
    class_uri = URIRef("http://schema.org/Thing")
    # Can list all properties here
    about: list[about] = []


Thing()


class AMRadioChannel(RdfType):
    uri = URIRef("http://schema.org/AMRadioChannel")


class APIReference(RdfType):
    uri = URIRef("http://schema.org/APIReference")


class addOn(RdfProperty):
    uri = URIRef("http://schema.org/addOn")
