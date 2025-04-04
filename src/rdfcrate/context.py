from types import ModuleType
from typing import TypeAlias
from rdflib import URIRef
from rdflib.namespace import DefinedNamespaceMeta

Context: TypeAlias = dict[str, str]
"""
A mapping from namespace prefixes to their URIs.
Can be used as an argument for [`RoCrate.compile`](rdfcrate.wrapper.RoCrate.compile).
"""

def from_namespace(namespace: DefinedNamespaceMeta) -> Context:
    """
    Make a context from an rdflib namespace.
    """
    prefix = namespace.__name__.lower()
    return namespace.as_jsonld_context(prefix)["@context"]

def from_module(module: ModuleType) -> Context:
    """
    Make a context from a module containing URIRefs.
    """
    return {
        name: str(value)
        for name, value in module.__dict__.items()
        if isinstance(value, URIRef)
    }
            
    
