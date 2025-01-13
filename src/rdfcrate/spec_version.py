from dataclasses import dataclass

@dataclass
class SpecVersion:
    context: str

ROCrate0_2 = SpecVersion(context="https://w3id.org/ro/crate/0.2/context")
ROCrate1_0 = SpecVersion(context="https://w3id.org/ro/crate/1.0/context")
ROCrate1_1 = SpecVersion(context="https://w3id.org/ro/crate/1.1/context")
ROCrate1_2 = SpecVersion(context="https://w3id.org/ro/crate/1.2-DRAFT/context")
