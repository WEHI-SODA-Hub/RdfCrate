from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import schemaorg


class _False(RdfClass):
    term = RdfTerm("False", "http://schema.org/False", ["1.0", "1.1", "1.2-DRAFT"])


class HTML(rdfs.Literal):
    term = RdfTerm("HTML", "http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML", [])


class File(schemaorg.CreativeWork):
    term = RdfTerm(
        "File", "http://schema.org/MediaObject", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )


class Journal(schemaorg.CreativeWorkSeries):
    term = RdfTerm(
        "Journal", "http://schema.org/Periodical", ["1.0", "1.1", "1.2-DRAFT"]
    )


class _True(RdfClass):
    term = RdfTerm("True", "http://schema.org/True", ["1.0", "1.1", "1.2-DRAFT"])


@dataclass(frozen=True)
class path(RdfProperty):
    term = RdfTerm(
        "path", "http://schema.org/contentUrl", ["0.2", "1.0", "1.1", "1.2-DRAFT"]
    )
    object: schemaorg.URL


@dataclass(frozen=True)
class cite_as(RdfProperty):
    term = RdfTerm(
        "cite-as", "http://www.iana.org/assignments/relation/cite-as", ["1.2-DRAFT"]
    )
    object: Identifier


class RepositoryCollection(RdfClass):
    term = RdfTerm(
        "RepositoryCollection",
        "http://pcdm.org/models#Collection",
        ["0.2", "1.0", "1.1", "1.2-DRAFT"],
    )


class RepositoryObject(RdfClass):
    term = RdfTerm(
        "RepositoryObject", "http://pcdm.org/models#Object", ["1.1", "1.2-DRAFT"]
    )


class RepositoryFile(RdfClass):
    term = RdfTerm("RepositoryFile", "http://pcdm.org/models#File", ["1.2-DRAFT"])


class ComputationalWorkflow(RdfClass):
    term = RdfTerm(
        "ComputationalWorkflow",
        "https://bioschemas.org/ComputationalWorkflow",
        ["1.1", "1.2-DRAFT"],
    )


@dataclass(frozen=True)
class input(RdfProperty):
    term = RdfTerm("input", "https://bioschemas.org/properties/input", ["1.2-DRAFT"])
    object: Identifier


@dataclass(frozen=True)
class output(RdfProperty):
    term = RdfTerm("output", "https://bioschemas.org/properties/output", ["1.2-DRAFT"])
    object: Identifier


class FormalParameter(RdfClass):
    term = RdfTerm(
        "FormalParameter",
        "https://bioschemas.org/FormalParameter",
        ["1.1", "1.2-DRAFT"],
    )


class ResourceDescriptor(RdfClass):
    term = RdfTerm(
        "ResourceDescriptor",
        "http://www.w3.org/ns/dx/prof/ResourceDescriptor",
        ["1.2-DRAFT"],
    )


class ResourceRole(RdfClass):
    term = RdfTerm(
        "ResourceRole", "http://www.w3.org/ns/dx/prof/ResourceRole", ["1.2-DRAFT"]
    )


@dataclass(frozen=True)
class softwareSuggestions(RdfProperty):
    term = RdfTerm(
        "softwareSuggestions",
        "https://codemeta.github.io/terms/softwareSuggestions",
        ["1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class continuousIntegration(RdfProperty):
    term = RdfTerm(
        "continuousIntegration",
        "https://codemeta.github.io/terms/continuousIntegration",
        ["1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class buildInstructions(RdfProperty):
    term = RdfTerm(
        "buildInstructions",
        "https://codemeta.github.io/terms/buildInstructions",
        ["1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class developmentStatus(RdfProperty):
    term = RdfTerm(
        "developmentStatus",
        "https://codemeta.github.io/terms/developmentStatus",
        ["1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class embargoEndDate(RdfProperty):
    term = RdfTerm(
        "embargoEndDate",
        "https://codemeta.github.io/terms/embargoEndDate",
        ["1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class readme(RdfProperty):
    term = RdfTerm("readme", "https://codemeta.github.io/terms/readme", ["1.2-DRAFT"])
    object: Identifier


@dataclass(frozen=True)
class issueTracker(RdfProperty):
    term = RdfTerm(
        "issueTracker", "https://codemeta.github.io/terms/issueTracker", ["1.2-DRAFT"]
    )
    object: Identifier


@dataclass(frozen=True)
class referencePublication(RdfProperty):
    term = RdfTerm(
        "referencePublication",
        "https://codemeta.github.io/terms/referencePublication",
        ["1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class hasSourceCode(RdfProperty):
    term = RdfTerm(
        "hasSourceCode", "https://codemeta.github.io/terms/hasSourceCode", ["1.2-DRAFT"]
    )
    object: Identifier


@dataclass(frozen=True)
class isSourceCodeOf(RdfProperty):
    term = RdfTerm(
        "isSourceCodeOf",
        "https://codemeta.github.io/terms/isSourceCodeOf",
        ["1.2-DRAFT"],
    )
    object: Identifier


@dataclass(frozen=True)
class localPath(RdfProperty):
    term = RdfTerm("localPath", "https://w3id.org/ro/terms#localPath", ["1.2-DRAFT"])
    object: Identifier
