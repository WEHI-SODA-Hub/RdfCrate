from __future__ import annotations

from collections.abc import Iterable
from typing import Any, ClassVar, Literal, TypeAlias

from rdflib import URIRef

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
                In "omit" mode, no terms are included in the context, because they are defined elsewhere, but other namespaces can't reuse their labels.
                In "prefix_collision" mode, the specified prefix is prepended to a term label only if that term is already in use in the context.
            prefix: A prefix that will be prepended to each term label in "prefix" and "curie" modes.
        """
        super().__init_subclass__(**kwargs)
        cls._prefix = prefix
        cls._mode = mode
        cls._terms_to_iris = {
            attr: value
            for attr, value in vars(cls).items()
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
    def reserve_terms(cls, claimed: dict[str, str]):
        """
        Claims the labels of terms that are defined outside of the generated context, whether or not they are used in the graph.
        In "omit" mode this is every term in the namespace, since they are already defined elsewhere, e.g. in a remote context.
        """
        if cls._mode == "omit":
            for term, iri in cls.terms():
                cls._claim(term, iri, claimed)

    @classmethod
    def add_term(cls, iri: URIRef, context: dict[str, str], claimed: dict[str, str]):
        """
        Updates the JSON-LD context `context` with terms in order to label `iri`

        Params:
            context: The JSON-LD context to update.
            claimed: Every term label in use, mapped to the IRI it expands to.
                This is a superset of `context`, since it also includes the terms of "omit" namespaces, which are defined elsewhere but must not be redefined.
        """
        # At this point we know that the IRI is defined as a term in this namespace.
        term = cls._iris_to_terms[iri]
        match cls._mode:
            case "omit":
                # In omit mode, we do not include any terms in the JSON-LD context. Their labels are claimed by `reserve_terms`.
                pass
            case "standard":
                # Add terms for each utilised IRI
                cls._claim(term, iri, claimed)
                context[term] = iri.toPython()
            case "prefix":
                if cls._prefix is None:
                    raise ValueError("Context prefix must be set for prefix mode.")
                # Add an extra prefix to the term label
                label = f"{cls._prefix}{term}"
                cls._claim(label, iri, claimed)
                context[label] = iri.toPython()
            case "prefix_collision":
                # Only add the prefix if the unprefixed label is already taken
                label = term
                if term in claimed and claimed[term] != iri.toPython():
                    if cls._prefix is None:
                        raise ValueError(
                            "Context prefix must be set for prefix_collision mode when a collision occurs."
                        )
                    label = f"{cls._prefix}{term}"
                cls._claim(label, iri, claimed)
                context[label] = iri.toPython()
            case "curie":
                if cls._base is None:
                    raise ValueError("Base IRI must be set for CURIE mode.")
                if cls._prefix is None:
                    raise ValueError("Context prefix must be set for CURIE mode.")

                # In CURIE mode, we only add the base IRI, and let the serializer construct CURIEs for us
                cls._claim(cls._prefix, cls._base, claimed)
                context[cls._prefix] = cls._base.toPython()

    @staticmethod
    def _claim(label: str, iri: URIRef, claimed: dict[str, str]):
        """
        Records that `label` expands to `iri`, or raises an error if it is already claimed by a different IRI.
        """
        if label in claimed and claimed[label] != iri.toPython():
            raise ValueError(
                f"Collision detected for term {label} with IRI {iri.toPython()}, which is already used for {claimed[label]}."
            )
        claimed[label] = iri.toPython()

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
