from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, ClassVar, Literal, TypeAlias

from rdflib import URIRef

if TYPE_CHECKING:
    from rdfcrate.context_builder import ContextBuilder

ContextMode: TypeAlias = Literal[
    "standard", "prefix", "prefix_collision", "curie", "external"
]


class ContextNamespace:
    """
    An RDF namespace that can also generate a JSON-LD context for the terms it defines.

    Subclasses should define each term as a class attribute holding a `URIRef`.
    The attribute name becomes the term label in the JSON-LD context.

    Example:
        ```python
        from rdflib import URIRef
        from rdfcrate import ContextNamespace

        class Obi(ContextNamespace):
            _base = URIRef("http://purl.obolibrary.org/obo/")
            Image = _base + "IAO_0000101"

        dict(Obi.terms())
        # {"Image": URIRef("http://purl.obolibrary.org/obo/IAO_0000101")}
        ```
    """

    _base: ClassVar[URIRef | None] = None
    """IRI that the terms in this namespace share. Required in "curie" mode, where it is added to the context under `_prefix`. Can also be used to construct IRIs for terms in the namespace, e.g. `MyNamespace._base + "MyTerm"`."""
    _prefix: ClassVar[str | None] = None
    """Prefix used by the "prefix", "prefix_collision" and "curie" modes."""
    _mode: ClassVar[ContextMode] = "standard"
    """The mode used for prefixing terms in the context."""
    _terms_to_iris: ClassVar[dict[str, URIRef]] = {}
    """A dictionary version of the terms in this namespace"""
    _iris_to_terms: ClassVar[dict[URIRef, str]] = {}
    """Inverse mapping from IRIs to term labels."""

    def __init_subclass__(
        cls,
        /,
        prefix: str | None = None,
        mode: ContextMode | None = None,
        **kwargs: Any,
    ):
        """
        Params:
            mode: The mode used for prefixing terms in the JSON-LD context.
                In "standard" mode (the default), the attribute name is used as the term label.
                This suits a vocabulary with opaque IRIs such as OBI, since it lets us label `BFO_0000051` as `hasPart`.
                In "prefix" mode, `prefix` is prepended to every term label.
                This suits when you don't want to use CURIE mode, and you also know clashes between your vocabularies are likely.
                In "prefix_collision" mode, `prefix` is prepended to a term label only if that label is already in use in the context.
                In "curie" mode, `prefix` is added to the context as a CURIE prefix for `_base`, and terms are written as CURIEs e.g. `schema:Thing`.
                This suits a vocabulary whose IRIs are human-readable, e.g. `schema:name`
                In "external" mode, terms are only labelled by the external context passed to `ContextBuilder`, and using a term it doesn't define raises an error.
                This suits a vocabulary that the external context already covers, such as schema.org with the RO-Crate context.
            prefix: Prepended to term labels in "prefix" and "prefix_collision" modes, and used as the CURIE prefix in "curie" mode. Ignored in "standard" and "external" modes.
        """
        super().__init_subclass__(**kwargs)
        # Only override the inherited values if explicitly provided
        if prefix is not None:
            cls._prefix = prefix
        if mode is not None:
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
        IRIs from "external" namespaces only reach this method if the builder's external context doesn't define them.
        """
        # At this point we know that the IRI is defined as a term in this namespace.
        term = cls._iris_to_terms[iri]
        match cls._mode:
            case "external":
                raise ValueError(
                    f"IRI {iri} is from external namespace {cls.__name__}, but the external context doesn't define it."
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


__all__ = [
    "ContextNamespace",
]
