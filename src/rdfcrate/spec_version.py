from dataclasses import dataclass

@dataclass(frozen=True)
class SpecVersion:
    context: str
    conforms_to: str

ROCrate0_2 = SpecVersion(context="https://w3id.org/ro/crate/0.2/context", conforms_to="https://w3id.org/ro/crate/0.2")
ROCrate1_0 = SpecVersion(context="https://w3id.org/ro/crate/1.0/context", conforms_to="https://w3id.org/ro/crate/1.0")
ROCrate1_1 = SpecVersion(context="https://w3id.org/ro/crate/1.1/context", conforms_to="https://w3id.org/ro/crate/1.1")
ROCrate1_2 = SpecVersion(context="https://w3id.org/ro/crate/1.2-DRAFT/context", conforms_to="https://w3id.org/ro/crate/1.2-DRAFT")
