from __future__ import annotations
from typing import Any, Iterable, TypeVar, TYPE_CHECKING, TypedDict
from typing_extensions import Annotated, Doc, Unpack
from deprecated import deprecated

from rdflib import RDF, Graph, IdentifiedNode, Literal
from rdflib.plugins.shared.jsonld.context import Context, Term

from rdfcrate.rdfprop import PropertyProtocol
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfClass
from rdfcrate.types import Triple

if TYPE_CHECKING:
    from rdfnav import GraphNavigator, UriNode  # type: ignore


EntityClass = TypeVar("EntityClass", bound=RdfClass)
EntityArgs = Annotated[
    PropertyProtocol,
    Doc(
        "Additional properties to add to the entity. Instances of `RdfProperty` will create triples with this new entity as the subject. Instances of `ReverseProperty` will create triples with this new entity as the object."
    ),
]


class ContextGraphKwargs(TypedDict, total=False):
    graph: Graph
    unique_terms: bool
    require_terms: bool


class ContextGraph:
    """
    A graph and associated JSON-LD context

    Typical usage involves creating new subgraphs via `RdfType.add` and then merging them into this context graph.
    """

    def __init__(self, **kwargs: Unpack[ContextGraphKwargs]):
        """
        Initializes a new ContextGraph with an optional initial graph.
        If no graph is provided, an empty Graph is created.
        """
        self.graph = kwargs.get("graph", Graph())
        self.unique_terms = kwargs.get("unique_terms", True)
        self.require_terms = kwargs.get("require_terms", True)

        # We separately track custom terms so that we can compile the context according to the spec
        # If we just used the context directly, it would contain all terms as one dictionary and not use a remote context
        self._custom_terms = {}

    graph: Graph
    #: If True, trying to add a term that already exists will raise an error
    unique_terms: bool
    #: If True, the context will require terms for all properties and classes
    require_terms: bool
    #: Set of custom terms not in the standard RO-Crate context that need to be in the final JSON-LD context.
    _custom_terms: dict[str, Any]

    @property
    def context_source(
        self,
    ) -> list[dict[str, Any] | str | None] | dict[str, Any] | str | None:
        # Return type is quite general because JSON-LD defines @context quite flexibly
        """
        Returns the components that make up the context for this graph.
        """
        # This is a property so that subclasses can generate context without storing it directly.
        # This is separate from `.context` because passing that into the serializer will result in a combined dictionary
        return self._custom_terms

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

    def navigate_to(self, iri: IdentifiedNode | RdfClass) -> UriNode:
        """
        Returns a navigator for the given IRI.
        This lets you mutate and query the graph using the `rdfnav` package.
        """
        navigator = self.navigate()
        if isinstance(iri, IdentifiedNode):
            return navigator[iri]
        elif isinstance(iri, RdfClass):
            return navigator[iri.id]

    def register_terms(self, terms: Iterable[RdfTerm | Term]) -> None:
        # Added for backwards compatibility
        for term in terms:
            self.register_term(term)

    def register_term(self, term: RdfTerm | Term) -> None:
        """
        Adds a custom term to the context
        """

        if isinstance(term, RdfTerm):
            term = Term(name=term.label, id=str(term.uri))

        existing = self.full_context.expand(term.name)
        if existing == str(term.id):
            # Skip terms that are already in the RO-Crate context
            return
        if self.unique_terms and existing is not None:
            raise ValueError(
                f'Term "{term.name}" is already defined to mean {existing}. Cannot redefine to {term.id}.'
            )

        if str(term.id) == str(RDF.type):
            # rdf:type should never be re-defined
            return

        self._do_register(term)

    def _do_register(self, term: Term) -> None:
        # Allows subclasses to override the registration process
        self._custom_terms[term.name] = Context()._term_dict(term)

    def add(self, subgraph: ContextGraph | Graph | Triple) -> None:
        """
        Adds a subgraph or triple to this context graph.
        If the subgraph is a ContextGraph, it will also merge the context.
        """
        if isinstance(subgraph, ContextGraph):
            self.graph += subgraph.graph
            term: Term
            for term in subgraph.full_context.terms.values():
                self.register_term(term)
        elif isinstance(subgraph, Graph):
            self.graph += subgraph
        elif isinstance(subgraph, tuple):
            # If it's a triple, add it directly
            self.graph.add(subgraph)
        else:
            raise TypeError("Subgraph must be a ContextGraph or a Graph instance.")

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
        Compiles the RO-Crate to a JSON-LD string

        Params:
            strip_datatypes: If True, any datatypes or languages will be stripped from literals. This is useful for compatibility with systems that do not support datatypes.
            **kwargs: Additional keyword arguments to pass to the RDFLib serializer
        """
        # Serializer kwargs are annoyingly not listed in the docs.
        # See them here: https://github.com/RDFLib/rdflib/blob/d220ee3bcba10a7af6630c4faaa37ca9cee33554/rdflib/plugins/serializers/jsonld.py#L76-L84
        return self.graph.serialize(
            format="json-ld", context=self.context_source, **kwargs
        )

    @deprecated(
        "The `add_entity` method is deprecated. Instead use `add` on instances of `RdfType` instead to add entities"
    )
    def add_entity(self, entity: EntityClass, *args: EntityArgs) -> EntityClass:
        """
        Adds any type of entity to the crate

        Returns:
            The ID of the new entity
        """
        # Note: The reason we have use the (entity, *args) signature is so that we can enforce certain properties and their types
        # when we make specialized variants of the method like `add_root_entity` or `register_file`.
        # `entity.add()` handles the term registration and the triple creation
        entity.add(*args, graph=self)
        return entity

    @deprecated(
        "The `add_metadata` method is deprecated. Instead use `update` on instances of `RdfType` instead"
    )
    def add_metadata(self, entity: RdfClass, *args: EntityArgs) -> None:
        """
        Add metadata for an existing entity.

        Returns:
            The ID of the updated entity

        Params:
            uri: ID of the entity being described
        """
        for arg in args:
            arg.add_to_graph(self, entity.id)
