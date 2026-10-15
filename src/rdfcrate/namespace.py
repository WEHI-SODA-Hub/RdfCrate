from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any, ClassVar, Literal, Protocol

from rdflib import RDF, URIRef

class ContextBuilder(Protocol):
    def terms_to_dict(self, ns: ContextNamespace) -> dict[str, URIRef]:
        ...

@dataclass
class StandardContextBuilder(ContextBuilder):
    """
    Builds a JSON-LD context where terms are used directly
    """

    def terms_to_dict(self, ns: ContextNamespace) -> dict[str, URIRef]:
        return {
            attr: value for attr, value in ns.terms()
        }

@dataclass
class CurieContextBuilder(ContextBuilder):
    """
    Builds a JSON-LD context using CURIEs for the terms in a namespace.
    """
    #: The prefix term as a human-readable string, e.g., "obi" for OBI
    prefix: str
    #: The base IRI that the prefix maps to in the JSON-LD context, e.g. "http://purl.obolibrary.org/obo/" for OBI
    base: URIRef

    def terms_to_dict(self, ns: ContextNamespace) -> dict[str, URIRef]:
        # Only the prefix and base are included in the context.
        # The terms themselves will be represented as CURIEs using that prefix.
        return {self.prefix: self.base}


@dataclass
class PrefixContextBuilder(ContextBuilder):
    """
    Builds a JSON-LD context that prefixes each term to avoid naming conflicts.
    """
    #: The prefix term as a human-readable string, e.g., "obi" for OBI
    prefix: str

    def terms_to_dict(self, ns: ContextNamespace) -> dict[str, URIRef]:
        return {
            f"{self.prefix}{attr}": value for attr, value in ns.terms()
        }

class ContextNamespace:
    """
    An RDF namespace that can also generate a JSON-LD context for the terms it defines.

    Subclasses should define each term as a class attribute holding a `URIRef`.
    The attribute name becomes the term label in the JSON-LD context, with any trailing underscore removed, so that Python keywords such as `type_` can be used.

    Example:
        ```python
        from rdflib import URIRef
        from rdfcrate import ContextNamespace

        class Obi(ContextNamespace, context_prefix="obi"):
            _base = URIRef("http://purl.obolibrary.org/obo/")
            Image = _base + "IAO_0000101"

        Obi.jsonld_context()
        # {"obi": "http://purl.obolibrary.org/obo/", "obiImage": "obi:IAO_0000101"}
        ```
    """

    #: IRI that the terms in this namespace share. If this and `_context_prefix` are set, the context will use CURIEs.
    _base: ClassVar[URIRef | None] = None
    #: Prefix that is prepended to every term label in the context, and used as the CURIE prefix for `_base`.
    _context_prefix: ClassVar[str | None] = None
    #: The mode used for prefixing terms in the context.
    _prefix_mode: ClassVar[Literal["none", "prefix", "curie"]] = "none"
    #: A dictionary version of the terms in this namespace
    _terms: ClassVar[dict[str, URIRef]] = {}
    #: The set of all IRIs defined as terms in this namespace.
    _all_iris: ClassVar[set[URIRef]] = set()

    def __init_subclass__(cls, /, context_prefix: str | None = None, prefix_mode: Literal["none", "prefix", "curie"] = "none", **kwargs: Any):
        """
        Params:
            context_prefix: A prefix that will be prepended to each term label in the JSON-LD context.
                If `_base` is also set, it will be defined as a prefix in the context, and terms will be written as CURIEs.
        """
        super().__init_subclass__(**kwargs)
        cls._context_prefix = context_prefix
        cls._prefix_mode = prefix_mode
        cls._terms = {
            attr: value
            for attr, value in vars(cls).items()
            if not attr.startswith("_") and isinstance(value, URIRef)
        }
        cls._all_iris = set(cls._terms.values())

    @classmethod
    def terms(cls) -> Iterable[tuple[str, URIRef]]:
        """
        Returns all IRIs defined as terms in this namespace.
        """
        for attr, value in cls._terms.items():
            yield attr, value

    @classmethod
    def defines_iri(cls, iri: URIRef) -> bool:
        """
        Returns `True` if the given IRI is defined as a term in this namespace.
        """
        return iri in cls._all_iris

    @classmethod
    def jsonld_context(cls, iris: Iterable[URIRef] | None = None) -> dict[str, str]:
        """
        Returns a flat JSON-LD context for the terms in this namespace.

        If `context_prefix` is set, it is prepended to each term label, e.g. `{"obiImage": ...}`.
        This is designed to avoid collisions with other terms in the context.
        If `_base` is also set, the prefix is defined as `_base`, and terms are written as CURIEs, e.g. `{"obi": "http://purl.obolibrary.org/obo/", "obiImage": "obi:IAO_0000101"}`.
        Otherwise, terms are mapped to full IRIs.

        `rdf:type` is never included, because JSON-LD uses `@type` for it.

        Params:
            iris: If provided, only terms with these IRIs will be included in the context.
        """
        match cls._prefix_mode:
            case "none":
                prefix = None
            case "prefix" | "curie":
                prefix = cls._context_prefix
            case _:
                raise ValueError(f"Unknown prefix mode: {cls._prefix_mode}")
        
        prefix = cls._context_prefix
        base = cls._base
        included = set(iris or [])
        context: dict[str, str] = {}

        for attr, iri in cls._terms.items():
            if iri not in included:
                # Skip terms that aren't used in the graph
                continue

            label = attr.removesuffix("_")
            if prefix is not None:
                label = prefix + label[0].upper() + label[1:]

            if prefix is not None and base is not None and iri.startswith(base):
                # Using a CURIE
                context[prefix] = str(base)
                context[label] = f"{prefix}:{iri[len(base) :]}"
            else:
                context[label] = str(iri)

        return context


__all__ = [
    "ContextNamespace",
]
