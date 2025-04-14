from __future__ import annotations
from abc import ABCMeta
from typing import Annotated, Any, ClassVar, Self, cast
from typing_extensions import Doc

from rdflib import Graph, URIRef, RDF
from rdfcrate.rdfprop import RdfProperty, ReverseProperty

from rdfcrate.rdfterm import RdfTerm

class RdfClassMeta(ABCMeta):
    """
    Metaclass which picks the first base class of the class being created.
    This is needed to avoid the MRO issues with multiple inheritance, which we aren't actually using for method resolution.
    Its only purpose is static type checking
    """
    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any], /, **kwargs: Any):
        if len(bases) > 1:
            bases = (bases[0],)
        return super().__new__(mcls, name, bases, namespace, **kwargs)

type EntityUri = Annotated[str, Doc("The identifier of the new entity. This must be a valid IRI or a relative path within the crate root.")]
type EntityArgs = Annotated[RdfProperty | ReverseProperty, Doc("Additional properties to add to the entity. Instances of `RdfProperty` will create triples with this new entity as the subject. Instances of `ReverseProperty` will create triples with this new entity as the object.")]

class RdfClass(URIRef, metaclass=RdfClassMeta):
    """
    A class that represents an RDF type.
    """
    term: ClassVar[RdfTerm]

    @classmethod
    def add(
        cls,
        graph: Graph,
        uri: EntityUri,
        *args: EntityArgs
    ) -> Self:
        """
        Creates a new entity in the graph with the given URI and adds triples to it.

        Params:
            graph: The graph to which the triples will be added
        Returns:
            A URIRef subclass for this RDF type
        """
        uri = cls(uri)
        if not isinstance(cls.term, RdfTerm):
            raise ValueError("The `term` class variable must be an instance of `RdfTerm`.")
        graph.add((uri, RDF.type, cls.term.uri))
        for arg in args:
            arg.add_to_graph(graph, uri)
        
        # See https://github.com/RDFLib/rdflib/issues/3107
        return super().__new__(cls, uri) # type: ignore

    def __new__(cls, uri: str) -> Self:
        """
        Casts the given URI to the class type.
        """
        return cast(Self, super().__new__(cls, uri))
        