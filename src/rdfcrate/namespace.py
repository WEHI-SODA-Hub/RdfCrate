from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, ClassVar, Literal, TypeAlias

from rdflib import URIRef

if TYPE_CHECKING:
    from rdfcrate.context_builder import ContextBuilder

ContextMode: TypeAlias = Literal[
    "standard", "prefix", "prefix_collision", "curie", "omit"
]


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
    _prefix: ClassVar[str | None] = None
    #: The mode used for prefixing terms in the context.
    _mode: ClassVar[ContextMode] = "standard"
    #: A dictionary version of the terms in this namespace
    _terms_to_iris: ClassVar[dict[str, URIRef]] = {}
    #: Inverse mapping from IRIs to term labels.
    _iris_to_terms: ClassVar[dict[URIRef, str]] = {}

    def __init_subclass__(
        cls,
        /,
        prefix: str | None = None,
        mode: ContextMode = "standard",
        **kwargs: Any,
    ):
        """
        Params:
            mode: The mode used for prefixing terms in the JSON-LD context.
                In "standard" mode, terms map to their full IRIs without any prefix.
                In "prefix" mode, the specified prefix is prepended to each term label to avoid collisions.
                In "curie" mode, terms are written as CURIEs using the prefix.
                In "omit" mode, no terms are included in the context, because they must be defined by the external context passed to `ContextBuilder`.
                In "prefix_collision" mode, the specified prefix is prepended to a term label only if that term is already in use in the context.
            prefix: A prefix that will be prepended to each term label in "prefix" and "curie" modes.
        """
        super().__init_subclass__(**kwargs)
        cls._prefix = prefix
        cls._mode = mode
        # Walk the MRO from base to subclass so that subclasses inherit and can override terms
        cls._terms_to_iris = {
            attr: value
            for klass in reversed(cls.__mro__)
            for attr, value in vars(klass).items()
            if not attr.startswith("_") and isinstance(value, URIRef)
        }
        cls._iris_to_terms = {value: attr for attr, value in cls._terms_to_iris.items()}

    @classmethod
    def terms(cls) -> Iterable[tuple[str, URIRef]]:
        """
        Yields all IRIs defined as terms in this namespace.
        """
        yield from cls._terms_to_iris.items()

    @classmethod
    def has_iri(cls, iri: URIRef) -> bool:
        """
        Returns `True` if the given IRI is defined as a term in this namespace.
        """
        return iri in cls._iris_to_terms

    @classmethod
    def add_term(cls, iri: URIRef, builder: ContextBuilder):
        """
        Adds terms to `builder` in order to label `iri`.
        IRIs from "omit" namespaces only reach this method if the builder's external context doesn't define them.
        """
        # At this point we know that the IRI is defined as a term in this namespace.
        term = cls._iris_to_terms[iri]
        match cls._mode:
            case "omit":
                raise ValueError(
                    f"IRI {iri} is from omit namespace {cls.__name__}, but the external context doesn't define it."
                )
            case "standard":
                # Add terms for each utilised IRI
                builder.claim(term, iri)
            case "prefix":
                if cls._prefix is None:
                    raise ValueError("Context prefix must be set for prefix mode.")
                # Add an extra prefix to the term label
                builder.claim(f"{cls._prefix}{term}", iri)
            case "prefix_collision":
                # Only add the prefix if the unprefixed label is already taken
                label = term
                existing = builder.lookup(term)
                if existing is not None and existing != iri.toPython():
                    if cls._prefix is None:
                        raise ValueError(
                            "Context prefix must be set for prefix_collision mode when a collision occurs."
                        )
                    label = f"{cls._prefix}{term}"
                builder.claim(label, iri)
            case "curie":
                if cls._base is None:
                    raise ValueError("Base IRI must be set for CURIE mode.")
                if cls._prefix is None:
                    raise ValueError("Context prefix must be set for CURIE mode.")

                # In CURIE mode, we only add the base IRI, and let the serializer construct CURIEs for us
                builder.claim(cls._prefix, cls._base)

    # @classmethod
    # def jsonld_context(cls, iris: Iterable[URIRef]) -> dict[str, str]:
    #     """
    #     Returns a flat JSON-LD context for the given IRIs.
    #     If a given IRI is not defined as a term in this namespace, it will be ignored.

    #     This approach avoids adding unused terms to the JSON-LD context.
    #     """
    #     return {}


__all__ = [
    "ContextNamespace",
]
