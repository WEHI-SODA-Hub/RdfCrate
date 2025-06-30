from __future__ import annotations
from typing import Annotated, Any, ClassVar, Generic, Self, TypeVar, TYPE_CHECKING, Union, cast
from typing_extensions import Doc

from rdflib import Graph, Literal, URIRef, RDF, IdentifiedNode
from rdfcrate.types import GraphId

if TYPE_CHECKING:
    from rdfcrate import RdfProperty, ReverseProperty, RdfTerm, rdf

EntityUri = Annotated[
    str,
    Doc(
        "The identifier of the new entity. This must be a valid IRI or a relative path within the crate root."
    ),
]
EntityArgs = Annotated[
    Union["RdfProperty", "ReverseProperty"],
    Doc(
        "Additional properties to add to the entity. Instances of `RdfProperty` will create triples with this new entity as the subject. Instances of `ReverseProperty` will create triples with this new entity as the object."
    ),
]

T = TypeVar("T", bound=GraphId)


class RdfType(Generic[T]):
    """
    An entity within the RDF graph.

    This is a thin wrapper around an `rdflib.IdentifiedNode` such as a `URIRef` or `BNode`, but which allows for static type checking.
    This is not a subclass of `URIRef` so that the ID can be either a URI or blank node.
    """

    id: T
    term: ClassVar[RdfTerm]

    def __init__(self, id: T):
        self.id = id

    def add(self, graph: Graph, *args: EntityArgs) -> None:
        """
        Adds triples to the graph with this entity as the subject.

        Params:
            graph: The graph to which the triples will be added
        Returns:
            A URIRef subclass for this RDF type
        """
        from rdfcrate import RdfTerm

        if not isinstance(self.term, RdfTerm):
            raise ValueError(
                "The `term` class variable must be an instance of `RdfTerm`."
            )
        graph.add((self.id, RDF.type, self.term.uri))
        for arg in args:
            arg.add_to_graph(graph, self.id)

    @classmethod
    def adhoc(cls: type[Self], term: RdfTerm) -> type[Self]:
        """
        Makes an ad-hoc type class from a term.
        """
        subclass = type(term.label, (cls,), {
            "term": term
        })
        return cast(type[Self], subclass)

    @classmethod
    def to_type_property(cls) -> rdf.type:
        """
        Converts this class wrapper to an instance of `RdfProperty` that can be used to tag entities with this type.
        """
        from rdfcrate import rdf, rdfs

        # TODO: use the specific metaclass such as owl.Class where appropriate
        # Create a new class dynamically with the same name as this class, but inheriting from `rdfs.Class`
        cls = type(cls.__name__, (rdfs.Class,), {"term": cls.term})
        return rdf.type(cls(cls.term.uri))

    @classmethod
    def with_term_label(cls, label: str) -> type[RdfType]:
        """
        Creates a new instance of this class with the given label.
        This is useful in cases where the term label is already defined by another vocabulary
        """
        from rdfcrate import RdfTerm

        # Create a new term with the given label
        term = RdfTerm(cls.term.uri, label)
        return type(cls.__name__, (cls,), {"term": term})


class RdfClass(RdfType[IdentifiedNode]):
    """
    An RDF entity that has a URI (or blank node).
    Typically these are instance of rdfs:Class or owl:Class.
    """

    def __init__(self, id: IdentifiedNode | str):
        if not isinstance(id, IdentifiedNode):
            # Assume an untagged string is an IRI
            id = URIRef(id)
        super().__init__(id)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, RdfClass):
            return False

        return value.id == self.id


class RdfLiteral(RdfType[Literal]):
    """
    An RDF entity that is a literal value.
    Typically these are instances of `rdfs:Literal`
    """

    def __init__(self, value: Any):
        # Convert any argument to a Literal, since this is the only legal type.
        # Users can still pass in a `Literal` instance directly if they want to e.g. tag it with a language or datatype.
        if not isinstance(value, Literal):
            value = Literal(value)

        super().__init__(value)
