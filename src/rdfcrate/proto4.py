from __future__ import annotations
from dataclasses import dataclass
from typing import Annotated, ClassVar

from rdflib import URIRef


@dataclass(frozen=True)
class RdfType:
    class_uri: ClassVar[URIRef]
    uri: str
    input: list[input] = []
    output: list[output] = []


class AMRadioChannel(RdfType):
    class_uri = URIRef("http://schema.org/AMRadioChannel")


class RootDataEntity(RdfType):
    class_uri = URIRef("https://schema.org/Dataset")


class FormalParameter(RdfType):
    class_uri = URIRef("https://bioschemas.org/FormalParameter")


@dataclass
class RdfProperty:
    prop_uri: str


type input = Annotated[
    FormalParameter, RdfProperty("https://bioschemas.org/properties/input")
]
type output = Annotated[
    FormalParameter, RdfProperty("https://bioschemas.org/properties/input")
]

RootDataEntity("#bar", output=[FormalParameter("#foo")])

""""
Issues:
- New properties defined by the user can't be added to existing classes"
- It's not using IRIs. This is bad because it means the graph must be a tree.
- We can't do "reverse" properties"
"""
