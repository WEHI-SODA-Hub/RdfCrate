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


class path(RdfProperty[schemaorg.URL]):
    term = RdfTerm("http://schema.org/contentUrl", "path")


class cite_as(RdfProperty[RdfType]):
    term = RdfTerm("http://www.iana.org/assignments/relation/cite-as", "cite-as")


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


class input(RdfProperty[RdfType]):
    term = RdfTerm("https://bioschemas.org/properties/input", "input")


class output(RdfProperty[RdfType]):
    term = RdfTerm("https://bioschemas.org/properties/output", "output")


class FormalParameter(RdfClass):
    term = RdfTerm("https://bioschemas.org/FormalParameter", "FormalParameter")


class softwareSuggestions(RdfProperty[RdfType]):
    term = RdfTerm(
        "https://codemeta.github.io/terms/softwareSuggestions", "softwareSuggestions"
    )


class continuousIntegration(RdfProperty[RdfType]):
    term = RdfTerm(
        "https://codemeta.github.io/terms/continuousIntegration",
        "continuousIntegration",
    )


class buildInstructions(RdfProperty[RdfType]):
    term = RdfTerm(
        "https://codemeta.github.io/terms/buildInstructions", "buildInstructions"
    )


class developmentStatus(RdfProperty[RdfType]):
    term = RdfTerm(
        "https://codemeta.github.io/terms/developmentStatus", "developmentStatus"
    )


class embargoEndDate(RdfProperty[RdfType]):
    term = RdfTerm("https://codemeta.github.io/terms/embargoEndDate", "embargoEndDate")


class readme(RdfProperty[RdfType]):
    term = RdfTerm("https://codemeta.github.io/terms/readme", "readme")


class issueTracker(RdfProperty[RdfType]):
    term = RdfTerm("https://codemeta.github.io/terms/issueTracker", "issueTracker")


class referencePublication(RdfProperty[RdfType]):
    term = RdfTerm(
        "https://codemeta.github.io/terms/referencePublication", "referencePublication"
    )


class hasSourceCode(RdfProperty[RdfType]):
    term = RdfTerm("https://codemeta.github.io/terms/hasSourceCode", "hasSourceCode")


class isSourceCodeOf(RdfProperty[RdfType]):
    term = RdfTerm("https://codemeta.github.io/terms/isSourceCodeOf", "isSourceCodeOf")


class localPath(RdfProperty[RdfType]):
    term = RdfTerm("https://w3id.org/ro/terms#localPath", "localPath")
