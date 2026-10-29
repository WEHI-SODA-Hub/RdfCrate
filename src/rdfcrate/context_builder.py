from __future__ import annotations

from dataclasses import InitVar, dataclass, field

from rdflib import URIRef
from rdflib.plugins.shared.jsonld.context import Context


@dataclass
class ContextBuilder:
    """
    State used while generating a JSON-LD context for a graph.
    Every term label in use is either in `context` or `omit`, but never both.

    This is kept separate from `ContextGraph` because it only lives for a single context generation,
    whereas a graph is long-lived and may change between compiles.
    It also means that `ContextNamespace` only depends on the few term-claiming methods it needs, rather than the whole graph.
    """

    #: Generated terms, which will be serialized as the JSON-LD context.
    context: dict[str, str] = field(default_factory=dict)
    #: Terms that are defined outside the generated context, such as by a remote context or by "omit" namespaces.
    #: These are never serialized, but other namespaces can't redefine them.
    omit: dict[str, str] = field(default_factory=dict)
    #: An existing JSON-LD context whose terms are added to `omit`.
    external: InitVar[Context | None] = None

    def __post_init__(self, external: Context | None):
        if external is not None:
            for label, term in external.terms.items():
                self.omit_term(label, URIRef(term.id))

    def lookup(self, label: str) -> str | None:
        """
        Returns the IRI that `label` expands to, or `None` if it is unused.
        """
        if label in self.context:
            return self.context[label]
        return self.omit.get(label)

    def _check_collision(self, label: str, iri: URIRef):
        """
        Raises an error if `label` is already used for an IRI other than `iri`.
        """
        existing = self.lookup(label)
        if existing is not None and existing != iri.toPython():
            raise ValueError(
                f"Term {label} can't be used for IRI {iri.toPython()}, because it is already defined as {existing}."
            )

    def claim(self, label: str, iri: URIRef):
        """
        Adds a term mapping `label` to `iri` to the generated context.
        """
        self._check_collision(label, iri)
        if label not in self.omit:
            self.context[label] = iri.toPython()

    def omit_term(self, label: str, iri: URIRef):
        """
        Records that `label` maps to `iri` in a context defined elsewhere, so it is not added to the generated context.
        """
        self._check_collision(label, iri)
        self.omit[label] = iri.toPython()

    def is_omitted(self, iri: URIRef) -> bool:
        """
        Returns `True` if `iri` already has a term defined outside the generated context.
        """
        return iri.toPython() in self.omit.values()

    def jsonld_context(self) -> dict[str, str]:
        """
        Returns the generated JSON-LD context.
        """
        return dict(self.context)
