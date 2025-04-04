from __future__ import annotations
from dataclasses import Field, dataclass, field, fields
from enum import Enum
from typing import Annotated, Any, ClassVar, Mapping, NewType, Protocol, Self, TypedDict, cast, get_args, get_type_hints
# from _typeshed import DataclassInstance

from rdflib import Graph, Literal, URIRef, RDF
from rdflib.term import Identifier

from rdfcrate.rdfterm import RdfTerm

class PropertyList(Protocol):
    """
    A protocol that is satisfied only by dataclasses whose fields are all `list[RdfTerm]`.
    """
    __annotations__: dict[str, type[list[RdfType]]]
    # This is stolen from _typeshed
    __dataclass_fields__: ClassVar[dict[str, Field[list[RdfType]]]]

class RdfType[FieldType: PropertyList](URIRef):
    """
    A class that represents an RDF type.
    """
    term: ClassVar[RdfTerm]
    def __new__(
        cls,
        graph: Graph,
        uri: URIRef,
        # objects and subjects are deliberately not restricted by class, which allows the user to use custom properties on any object
        objects: FieldType | None = None,
        subjects: PropertyList | None = None,
    ) -> Self:
        """
        Instantiating this will create a new entity in the graph with the given URI and add triples to it.

        Params:
            graph: The graph to which the triples will be added
            uri: The URI of the new entity.
            objects: The objects of the triples to be added to the graph. These are the typical properties of the class: `uri` will be the subject of the triple.
            subjects: The subjects of the triples to be added to the graph. These are more like reverse properties, because this `uri` will be the object of the triple.

        Returns:
            A URIRef subclass for this RDF type
        """
        if not isinstance(cls.term, RdfTerm):
            raise ValueError("The `term` class variable must be an instance of `RdfTerm`.")
        graph.add((uri, RDF.type, cls.term.uri))
        if objects is not None:
            hints: dict[str, Any] = get_type_hints(objects, localns=globals(), include_extras=True)
            for field in fields(objects):
                values = getattr(objects, field.name)
                # Pick the type hint for this field: list[input]
                # Pick the first type, using `get_args`, giving `input`
                # Evaluate the type alias using `__value))`, giving `Annotated[FormalParameter, RdfTerm()]``
                # Extract the annotation with `__metadata__`, giving `(RdfTerm(),)`
                # Get the first element of the tuple, giving `RdfTerm()`
                term = get_args(hints[field.name])[0].__value__.__metadata__[0]
                if not isinstance(term, RdfTerm):
                    raise ValueError(f"The objects parameter must be a TypedDict whose values are a list of `RdfType`, annotated with an `RdfTerm`.")
                if not isinstance(values, list):
                    raise ValueError(f"All values in the property list must be lists. Got {values}")
                for value in values:
                    graph.add((uri, term.uri, value))

        if subjects is not None:
            for key, values in subjects.items():
                for value in values:
                    term = value.__metadata__
                    if not isinstance(term, RdfTerm):
                        raise ValueError(f"All values in the property list must be annotated with an RdfTerm. Got {term}")
                    graph.add((value, term.uri, uri))
        
        return super().__new__(cls, uri)
        