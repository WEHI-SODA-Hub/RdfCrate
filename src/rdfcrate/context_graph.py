from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Annotated, Any, TypedDict

from rdflib import RDF, XSD, Graph, IdentifiedNode, Literal, URIRef
from rdflib.plugins.shared.jsonld.context import Context
from typing_extensions import Doc, Unpack

from rdfcrate.namespace import ContextNamespace
from rdfcrate.types import Object, Predicate, Triple

if TYPE_CHECKING:
    from rdfnav import GraphNavigator, UriNode  # type: ignore


PropertyArg = Annotated[
    tuple[Predicate, Object],
    Doc(
        "A `(predicate, object)` pair, which will be added to the graph with the entity as the subject. For example `(Sdo.name, Literal('My Dataset'))`."
    ),
]

#: Datatypes that rdflib serializes as native JSON values, which therefore don't need a term in the context.
NATIVE_DATATYPES = {XSD.boolean, XSD.integer, XSD.double, XSD.string}


class ContextGraphKwargs(TypedDict, total=False):
    graph: Graph
    vocabs: Iterable[type[ContextNamespace]]


class ContextGraph:
    """
    A graph and associated JSON-LD context

    The context is generated when the graph is compiled, and contains only the terms from `vocabs` that are used in the graph.
    """

    def __init__(self, **kwargs: Unpack[ContextGraphKwargs]):
        """
        Initializes a new ContextGraph with an optional initial graph.
        If no graph is provided, an empty Graph is created.
        """
        self.graph = kwargs.get("graph", Graph())
        self.vocabs = list(kwargs.get("vocabs", []))
        self._resolved_base_context = None

    graph: Graph
    #: Namespaces whose terms can be used in the graph. Every predicate, type and datatype in the graph must be defined in one of these, or in the base context.
    vocabs: list[type[ContextNamespace]]
    #: Cache of the parsed base context, to avoid re-parsing it on every compile
    _resolved_base_context: Context | None

    @property
    def base_context(self) -> str | None:
        """
        A remote context that all terms are resolved against before falling back to `vocabs`.
        """
        return None

    def _base(self) -> Context:
        if self._resolved_base_context is None:
            self._resolved_base_context = Context(self.base_context)
        return self._resolved_base_context

    def _used_iris(self) -> set[URIRef]:
        """
        Returns all IRIs in the graph that need a term in the context.
        """
        iris: set[URIRef] = set()
        for _, predicate, object in self.graph:
            if predicate == RDF.type:
                if isinstance(object, URIRef):
                    iris.add(object)
            elif isinstance(predicate, URIRef):
                iris.add(predicate)
            if (
                isinstance(object, Literal)
                and object.datatype is not None
                and object.datatype not in NATIVE_DATATYPES
            ):
                iris.add(object.datatype)
        return iris

    def custom_context(self) -> dict[str, str]:
        """
        Returns the terms from `vocabs` that are used in the graph and aren't already in the base context.

        Raises:
            ValueError: If two terms have the same label, or if an IRI in the graph has no term.
        """
        base = self._base()
        missing = {iri for iri in self._used_iris() if base.find_term(str(iri)) is None}

        custom: dict[str, str] = {}
        for vocab in self.vocabs:
            vocab_context = vocab.jsonld_context(iris=missing)
            vocab_expander = Context(vocab_context)
            for label, value in vocab_context.items():
                iri = vocab_expander.expand(label)
                existing = custom.get(label)
                if existing is not None and existing != value:
                    raise ValueError(
                        f'Term "{label}" from {vocab.__name__} is defined as both {existing} and {value}. Use a `context_prefix` to distinguish them.'
                    )
                existing_base = base.expand(label)
                if existing_base is not None and existing_base != iri:
                    raise ValueError(
                        f'Term "{label}" from {vocab.__name__} is already defined to mean {existing_base} in the base context. Use a `context_prefix` to distinguish them.'
                    )
                custom[label] = value

        resolved = base.subcontext(custom)
        unresolved = sorted(
            str(iri) for iri in missing if resolved.find_term(str(iri)) is None
        )
        if unresolved:
            raise ValueError(
                f"No term is defined for the following IRIs: {', '.join(unresolved)}. Add them to a ContextNamespace in `vocabs`."
            )

        return custom

    @property
    def context_source(
        self,
    ) -> list[dict[str, Any] | str | None] | dict[str, Any] | str | None:
        # Return type is quite general because JSON-LD defines @context quite flexibly
        """
        Returns the components that make up the context for this graph.
        """
        # This is separate from `.full_context` because passing that into the serializer will result in a combined dictionary
        custom = self.custom_context()
        if self.base_context is None:
            return custom
        if len(custom) == 0:
            return self.base_context
        return [self.base_context, custom]

    @property
    def full_context(self) -> Context:
        """
        Returns a `Context` that can be used for resolving terms. It should *not* be used for serialization and `context_source` should be used instead.
        """
        return Context(self.context_source)

    def navigate(self) -> GraphNavigator:
        """
        Returns a navigator that can be used to traverse and mutate the graph.
        """
        try:
            from rdfnav import GraphNavigator  # type: ignore

            return GraphNavigator(self.graph)
        except ImportError:
            raise ImportError(
                "Please install the `nav` extra for rdfcrate if you want to use the `.navigate()` method."
            )

    def navigate_to(self, iri: IdentifiedNode) -> UriNode:
        """
        Returns a navigator for the given IRI.
        This lets you mutate and query the graph using the `rdfnav` package.
        """
        return self.navigate()[iri]

    def add(self, subgraph: ContextGraph | Graph | Triple) -> None:
        """
        Adds a subgraph or triple to this crate.
        If the subgraph is a ContextGraph, its vocabs will also be added.
        """
        if isinstance(subgraph, ContextGraph):
            self.graph += subgraph.graph
            for vocab in subgraph.vocabs:
                if vocab not in self.vocabs:
                    self.vocabs.append(vocab)
        elif isinstance(subgraph, Graph):
            self.graph += subgraph
        elif isinstance(subgraph, tuple):
            # If it's a triple, add it directly
            self.graph.add(subgraph)
        else:
            raise TypeError("Subgraph must be a ContextGraph or a Graph instance.")

    def add_entity(
        self, entity: IdentifiedNode | str, *props: PropertyArg
    ) -> IdentifiedNode:
        """
        Adds triples to the graph with `entity` as the subject.
        This can be used both to create new entities and to add metadata to existing ones.

        Returns:
            The ID of the entity

        Params:
            entity: ID of the entity. Strings are treated as IRIs.

        Example:
            ```python
            from rdflib import Literal
            from rdfcrate import ContextGraph
            from rdfcrate.vocabs import Rdf, Sdo

            ContextGraph().add_entity(
                "#thing",
                (Rdf.type_, Sdo.CreativeWork),
                (Sdo.name, Literal("My Thing")),
            )
            ```
        """
        if not isinstance(entity, IdentifiedNode):
            entity = URIRef(entity)
        for predicate, object in props:
            self.graph.add((entity, predicate, object))
        return entity

    def strip_datatypes(
        self, strip_datatypes: bool = True, strip_languages: bool = True
    ) -> Graph:
        """
        Returns a copy of the graph with datatypes and/or languages stripped from literals.

        Params:
            strip_datatypes: If True, any datatypes will be stripped from literals.
            strip_languages: If True, any languages will be stripped from literals.
        """
        output_graph = Graph()
        for s, p, o in self.graph:
            if isinstance(o, Literal):
                if strip_datatypes:
                    o._datatype = None
                if strip_languages:
                    o._language = None
            output_graph.add((s, p, o))
        return output_graph

    def compile(self, **kwargs) -> str:
        """
        Compiles the crate to a JSON-LD string

        Params:
            **kwargs: Additional keyword arguments to pass to the RDFLib serializer
        """
        # Serializer kwargs are annoyingly not listed in the docs.
        # See them here: https://github.com/RDFLib/rdflib/blob/d220ee3bcba10a7af6630c4faaa37ca9cee33554/rdflib/plugins/serializers/jsonld.py#L76-L84
        return self.graph.serialize(
            format="json-ld", context=self.context_source, **kwargs
        )
