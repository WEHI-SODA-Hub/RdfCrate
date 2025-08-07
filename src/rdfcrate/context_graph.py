from typing import Iterable, TypeVar, TYPE_CHECKING, TypedDict
from typing_extensions import Annotated, Doc, Unpack

from rdflib import RDF, Graph, IdentifiedNode
from rdflib.plugins.shared.jsonld.context import Context, Term, _ContextSourceType

from rdfcrate.rdfprop import PropertyProtocol
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfClass

if TYPE_CHECKING:
    from rdfnav import GraphNavigator, UriNode
    from rdflib.graph import _TripleType


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
    # custom_terms: dict[str, str]
    "Set of custom terms not in the standard RO-Crate context that need to be in the final JSON-LD context."

    @property
    def context_source(self) -> _ContextSourceType:
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

    def navigate(self) -> "GraphNavigator":
        """
        Returns a navigator that can be used to traverse and mutate the graph.
        """
        try:
            from rdfnav import GraphNavigator

            return GraphNavigator(self.graph)
        except ImportError:
            raise ImportError(
                "The 'rdfnav' package is required for navigation. Please install it with 'pip install rdfnav'."
            )

    def navigate_to(self, iri: IdentifiedNode | RdfClass) -> "UriNode":
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

    def add(self, subgraph: "ContextGraph | Graph | _TripleType") -> None:
        """
        Adds a subgraph to this context graph.
        If the subgraph is a ContextGraph, it will also merge the context.
        """
        if isinstance(subgraph, ContextGraph):
            self.graph += subgraph.graph
            term: Term
            for term in subgraph.full_context.terms.values():
                self.full_context.add_term(**term._asdict())
        elif isinstance(subgraph, Graph):
            self.graph += subgraph
        elif isinstance(subgraph, tuple):
            # If it's a triple, add it directly
            self.graph.add(subgraph)
        else:
            raise TypeError("Subgraph must be a ContextGraph or a Graph instance.")

    def compile(self) -> str:
        """
        Compiles the RO-Crate to a JSON-LD string
        """
        # Serializer kwargs are annoyingly not listed in the docs.
        # See them here: https://github.com/RDFLib/rdflib/blob/d220ee3bcba10a7af6630c4faaa37ca9cee33554/rdflib/plugins/serializers/jsonld.py#L76-L84
        return self.graph.serialize(format="json-ld", context=self.context_source)
