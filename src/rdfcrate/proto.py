from dataclasses import dataclass
from typing import Annotated, TypedDict

from rdflib import URIRef
from rdflib.term import Identifier


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
