from __future__ import annotations

from dataclasses import InitVar, dataclass, field

from rdflib import URIRef
from rdflib.plugins.shared.jsonld.context import Context


@dataclass
class ContextBuilder:
    """
    State used while generating a JSON-LD context for a graph.
    Every term label in use is either in `context` or `external`, but never both.

    This is kept separate from `ContextGraph` because it only lives for a single context generation,
    whereas a graph is long-lived and may change between compiles.
    It also means that `ContextNamespace` only depends on the few term-claiming methods it needs, rather than the whole graph.

    Params:
        external_context: An existing JSON-LD context whose terms are added to `external`.
    """

    # The reason why `external_context` is not just inferred from the mode="external" vocabularies is that these vocabs only contain manually-defined terms which are a subset of all the terms defined by a remote context.
    # For example if my custom Schema.org Namespace has only `schema:name` defined but then I try to use `owl:Class` in my graph, we need to avoid re-defining `Class` since it's in the RO-Crate context despite not being in my namespace.
    # `external_context` also reserves labels that are not valid Python identifiers, which can't be added to namespaces.

    context: dict[str, str] = field(default_factory=dict)
    """Generated terms, which will be serialized as the JSON-LD context."""
    external: dict[str, str] = field(default_factory=dict)
    """
    Terms that are defined by the external context.
    These are never serialized, but other namespaces can't redefine them.
    """
    external_context: InitVar[Context | None] = None

    def __post_init__(self, external_context: Context | None):
        if external_context is not None:
            for label, term in external_context.terms.items():
                self.add_external_term(label, URIRef(term.id))

    def lookup(self, label: str) -> str | None:
        """
        Returns the IRI that `label` expands to, or `None` if it is unused.
        """
        if label in self.context:
            return self.context[label]
        return self.external.get(label)

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
        if label not in self.external:
            self.context[label] = iri.toPython()

    def add_external_term(self, label: str, iri: URIRef):
        """
        Records that `label` maps to `iri` in a context defined elsewhere, so it is not added to the generated context.
        """
        self._check_collision(label, iri)
        self.external[label] = iri.toPython()

    def is_external(self, iri: URIRef) -> bool:
        """
        Returns `True` if `iri` already has a term defined outside the generated context.
        """
        return iri.toPython() in self.external.values()

    def jsonld_context(self) -> dict[str, str]:
        """
        Returns the generated JSON-LD context.
        """
        return dict(self.context)
