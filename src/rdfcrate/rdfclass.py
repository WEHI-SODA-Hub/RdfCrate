from __future__ import annotations
from typing import Annotated, ClassVar
from typing_extensions import Doc

from rdflib import Graph, URIRef, RDF, IdentifiedNode
from rdfcrate.rdfprop import RdfProperty, ReverseProperty

from rdfcrate.rdfterm import RdfTerm
from rdfcrate.types import GraphId


EntityUri = Annotated[
    str,
    Doc(
        "The identifier of the new entity. This must be a valid IRI or a relative path within the crate root."
    ),
]
EntityArgs = Annotated[
    RdfProperty | ReverseProperty,
    Doc(
        "Additional properties to add to the entity. Instances of `RdfProperty` will create triples with this new entity as the subject. Instances of `ReverseProperty` will create triples with this new entity as the object."
    ),
]

class RdfClass:
    """
    An entity within the RDF graph.

    This is a thin wrapper around an `rdflib.IdentifiedNode` such as a `URIRef` or `BNode`, but which allows for static type checking.
    This is not a subclass of `URIRef` so that the ID can be either a URI or blank node.
    """
    id: GraphId
    term: ClassVar[RdfTerm]

    def __init__(self, id: GraphId | str):
        if not isinstance(id, IdentifiedNode):
            # Assume an untagged string is an IRI
            self.id = URIRef(id)
        else:
            self.id = id

    def add(self, graph: Graph, *args: EntityArgs) -> None:
        """
        Adds triples to the graph with this entity as the subject.

        Params:
            graph: The graph to which the triples will be added
        Returns:
            A URIRef subclass for this RDF type
        """
        if not isinstance(self.term, RdfTerm):
            raise ValueError(
                "The `term` class variable must be an instance of `RdfTerm`."
            )
        graph.add((self.id, RDF.type, self.term.uri))
        for arg in args:
            arg.add_to_graph(graph, self.id)
