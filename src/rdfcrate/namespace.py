from __future__ import annotations

from collections.abc import Iterable
from typing import Any, ClassVar

from rdflib import RDF, URIRef


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

    def __init_subclass__(cls, /, context_prefix: str | None = None, **kwargs: Any):
        """
        Params:
            context_prefix: A prefix that will be prepended to each term label in the JSON-LD context.
                If `_base` is also set, it will be defined as a prefix in the context, and terms will be written as CURIEs.
        """
        super().__init_subclass__(**kwargs)
        if context_prefix is not None:
            cls._context_prefix = context_prefix

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
        prefix = cls._context_prefix
        base = cls._base
        included = None if iris is None else set(iris)
        context: dict[str, str] = {}

        for attr in dir(cls):
            if attr.startswith("_"):
                continue
            iri = getattr(cls, attr)
            if not isinstance(iri, URIRef) or iri == RDF.type:
                continue
            if included is not None and iri not in included:
                continue

            label = attr.removesuffix("_")
            if prefix is not None:
                label = prefix + label[0].upper() + label[1:]

            if prefix is not None and base is not None and iri.startswith(base):
                context[prefix] = str(base)
                context[label] = f"{prefix}:{iri[len(base) :]}"
            else:
                context[label] = str(iri)

        return context


__all__ = [
    "ContextNamespace",
]
