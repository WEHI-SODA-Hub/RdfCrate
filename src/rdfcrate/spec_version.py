"""
Contains objects representing the different versions of the RO-Crate specification.

Attributes:
    ROCrate0_2: RO-Crate 0.2
    ROCrate1_0: RO-Crate 1.0
    ROCrate1_1: RO-Crate 1.1
    ROCrate1_2: RO-Crate 1.2
"""

from rdflib import URIRef
from requests import get


class SpecVersion:
    version: str
    context_url: URIRef
    conforms_to_url: URIRef

    def __init__(self, version: str, context_url: str, conforms_to_url: str):
        self.version = version
        self.context_url = URIRef(context_url)
        self.conforms_to_url = URIRef(conforms_to_url)

    def get_context(self) -> dict:
        """Loads the context from the context URL."""
        return get(self.context_url).json()["@context"]


ROCrate0_2: SpecVersion = SpecVersion(
    "0.2",
    context_url="https://w3id.org/ro/crate/0.2/context",
    conforms_to_url="https://w3id.org/ro/crate/0.2",
)
ROCrate1_0: SpecVersion = SpecVersion(
    "1.0",
    context_url="https://w3id.org/ro/crate/1.0/context",
    conforms_to_url="https://w3id.org/ro/crate/1.0",
)
ROCrate1_1: SpecVersion = SpecVersion(
    "1.1",
    context_url="https://w3id.org/ro/crate/1.1/context",
    conforms_to_url="https://w3id.org/ro/crate/1.1",
)
ROCrate1_2: SpecVersion = SpecVersion(
    "1.2-DRAFT",
    context_url="https://w3id.org/ro/crate/1.2-DRAFT/context",
    conforms_to_url="https://w3id.org/ro/crate/1.2-DRAFT",
)

all_specs = [ROCrate0_2, ROCrate1_0, ROCrate1_1, ROCrate1_2]
