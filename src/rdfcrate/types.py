from rdflib import IdentifiedNode, URIRef
from rdflib.term import Identifier

# These type definitions let us avoid depending in the private
# rdflib internal types like `_TripleType`
# Also, they allow us to conform better with the RDF spec than rdflib does: https://github.com/RDFLib/rdflib/issues/3172
Subject = IdentifiedNode
Predicate = URIRef
Object = Identifier
Triple = tuple[Subject, Predicate, Object]
