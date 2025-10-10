from dataclasses import dataclass
from typing import Annotated, ClassVar

from rdflib import Literal, URIRef
from rdflib.term import Identifier

type ContextEntry[T: Literal] = Annotated[Identifier, T]


@dataclass
class RdfType:
    uri: ClassVar[URIRef]
    value: Identifier


@dataclass
class RdfProperty:
    uri: ClassVar[URIRef]
    value: RdfType


class AMRadioChannel(RdfType):
    uri = URIRef("http://schema.org/AMRadioChannel")


class APIReference(RdfType):
    uri = URIRef("http://schema.org/APIReference")


class addOn(RdfProperty):
    uri = URIRef("http://schema.org/addOn")


crate.add_root_entity(objects=[addOn(APIReference(URIRef("")))])
