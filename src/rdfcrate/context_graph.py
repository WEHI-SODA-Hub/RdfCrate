from dataclasses import dataclass, field
from typing import Iterable, TypeVar, Union, TYPE_CHECKING
from typing_extensions import Annotated, Doc

from rdflib import RDF, Graph
from rdflib.plugins.shared.jsonld.context import Context, Term

from rdfcrate.rdfprop import PropertyProtocol
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.rdftype import RdfClass

if TYPE_CHECKING:
    from rdfnav import GraphNavigator


EntityClass = TypeVar("EntityClass", bound=RdfClass)
EntityArgs = Annotated[
    PropertyProtocol,
    Doc(
        "Additional properties to add to the entity. Instances of `RdfProperty` will create triples with this new entity as the subject. Instances of `ReverseProperty` will create triples with this new entity as the object."
    ),
]

@dataclass
class ContextGraph:
    """
    A graph and associated JSON-LD context

    Typical usage involves creating new subgraphs via `RdfType.add` and then merging them into this context graph.
    """
    graph: Graph = field(default_factory=Graph)
    context: Context = field(default_factory=Context)
    #: If True, trying to add a term that already exists will raise an error
    unique_terms: bool = field(default=True)
    #: If True, the context will require terms for all properties and classes
    require_terms: bool = field(default=True)

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

    def register_term(self, term: RdfTerm | Term) -> None:
        """
        Adds custom terms to the context
        """
        # Supports our local `RdfTerm` and also the rdflib `Term`.
        # It is hoped that `Term` will become a public interface of `rdflib` in the future and we can remove `RdfTerm`.
        if isinstance(term, RdfTerm):
            existing = self.context.expand(term.label)
            if existing == str(term.uri):
                # Skip terms that are already in the RO-Crate context
                return
            if self.unique_terms and existing is not None:
                raise ValueError(
                    f'Term "{term.label}" is already defined to mean {existing}. Cannot redefine to {term.uri}.'
                )

            if term.uri == RDF.type:
                # rdf:type should never be re-defined
                return

            # The context keeps track of all terms, including the base RO-Crate terms.
            self.context.add_term(term.label, str(term.uri))
            # Custom terms only tracks the non-standard terms
            # self.custom_terms[term.label] = str(term.uri)
        elif isinstance(term, Term):
            existing = self.context.expand(term.name)
            if existing == str(term.id):
                return
            if self.unique_terms and existing is not None:
                raise ValueError(
                    f'Term "{term.name}" is already defined to mean {existing}. Cannot redefine to {term.id}.'
                )

            if term.id == RDF.type:
                return
            self.context.add_term(**term._asdict())

    def add(self, subgraph: "ContextGraph | Graph") -> None:
        """
        Adds a subgraph to this context graph.
        If the subgraph is a ContextGraph, it will also merge the context.
        """
        if isinstance(subgraph, ContextGraph):
            self.graph += subgraph.graph
            term: Term
            for term in subgraph.context.terms.values():
                self.context.add_term(**term._asdict())
        elif isinstance(subgraph, Graph):
            self.graph += subgraph
        else:
            raise TypeError("Subgraph must be a ContextGraph or a Graph instance.")
