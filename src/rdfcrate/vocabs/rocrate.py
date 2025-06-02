from __future__ import annotations
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import schemaorg
from rdfcrate.rdftype import RdfType


class _False(RdfClass):
    term = RdfTerm("http://schema.org/False", "False")


class HTML(rdfs.Literal):
    term = RdfTerm("http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML", "HTML")


class File(schemaorg.CreativeWork):
    term = RdfTerm("http://schema.org/MediaObject", "File")


class Journal(schemaorg.CreativeWorkSeries):
    term = RdfTerm("http://schema.org/Periodical", "Journal")


class _True(RdfClass):
    term = RdfTerm("http://schema.org/True", "True")


class path(RdfProperty):
    term = RdfTerm("http://schema.org/contentUrl", "path")
    object: schemaorg.URL


class cite_as(RdfProperty):
    term = RdfTerm("http://www.iana.org/assignments/relation/cite-as", "cite-as")
    object: RdfType


class RepositoryCollection(RdfClass):
    term = RdfTerm("http://pcdm.org/models#Collection", "RepositoryCollection")


class RepositoryObject(RdfClass):
    term = RdfTerm("http://pcdm.org/models#Object", "RepositoryObject")


class RepositoryFile(RdfClass):
    term = RdfTerm("http://pcdm.org/models#File", "RepositoryFile")


class ComputationalWorkflow(RdfClass):
    term = RdfTerm(
        "https://bioschemas.org/ComputationalWorkflow", "ComputationalWorkflow"
    )


class input(RdfProperty):
    term = RdfTerm("https://bioschemas.org/properties/input", "input")
    object: RdfType


class output(RdfProperty):
    term = RdfTerm("https://bioschemas.org/properties/output", "output")
    object: RdfType


class FormalParameter(RdfClass):
    term = RdfTerm("https://bioschemas.org/FormalParameter", "FormalParameter")


class ResourceDescriptor(RdfClass):
    term = RdfTerm(
        "http://www.w3.org/ns/dx/prof/ResourceDescriptor", "ResourceDescriptor"
    )


class ResourceRole(RdfClass):
    term = RdfTerm("http://www.w3.org/ns/dx/prof/ResourceRole", "ResourceRole")


class softwareSuggestions(RdfProperty):
    term = RdfTerm(
        "https://codemeta.github.io/terms/softwareSuggestions", "softwareSuggestions"
    )
    object: RdfType


class continuousIntegration(RdfProperty):
    term = RdfTerm(
        "https://codemeta.github.io/terms/continuousIntegration",
        "continuousIntegration",
    )
    object: RdfType


class buildInstructions(RdfProperty):
    term = RdfTerm(
        "https://codemeta.github.io/terms/buildInstructions", "buildInstructions"
    )
    object: RdfType


class developmentStatus(RdfProperty):
    term = RdfTerm(
        "https://codemeta.github.io/terms/developmentStatus", "developmentStatus"
    )
    object: RdfType


class embargoEndDate(RdfProperty):
    term = RdfTerm("https://codemeta.github.io/terms/embargoEndDate", "embargoEndDate")
    object: RdfType


class readme(RdfProperty):
    term = RdfTerm("https://codemeta.github.io/terms/readme", "readme")
    object: RdfType


class issueTracker(RdfProperty):
    term = RdfTerm("https://codemeta.github.io/terms/issueTracker", "issueTracker")
    object: RdfType


class referencePublication(RdfProperty):
    term = RdfTerm(
        "https://codemeta.github.io/terms/referencePublication", "referencePublication"
    )
    object: RdfType


class hasSourceCode(RdfProperty):
    term = RdfTerm("https://codemeta.github.io/terms/hasSourceCode", "hasSourceCode")
    object: RdfType


class isSourceCodeOf(RdfProperty):
    term = RdfTerm("https://codemeta.github.io/terms/isSourceCodeOf", "isSourceCodeOf")
    object: RdfType


class localPath(RdfProperty):
    term = RdfTerm("https://w3id.org/ro/terms#localPath", "localPath")
    object: RdfType
