from rdflib import URIRef
from urllib.parse import urlparse, parse_qsl

def guess_term_from_uri(uri: str) -> str:
    """
    Guess the term from a URI by extracting the last part of the path.
    """
    parsed = urlparse(uri)
    if parsed.fragment:
        return parsed.fragment
    elif parsed.query:
        return parse_qsl(parsed.query)[-1][-1]
    elif split := parsed.path.split("/")[-1]:
        return split
    raise ValueError(f"Cannot guess term from URI: {uri}")


class RdfTerm:
    """
    Wrapper for a term with a label and URI.
    This is needed because RO-Crate bans the use of full URIs in JSON-LD.
    """

    #: The short name of the term
    label: str
    #: The URI of the term
    uri: URIRef
    #: List of RO-Crate versions numbers for which this term is automatically included in the context
    specs: list[str]

    def __init__(self, uri: str, term: str | None = None, specs: list[str] = []) -> None:
        self.uri = URIRef(uri)
        if term is None:
            self.label = guess_term_from_uri(uri)
        else:
            self.label = term
        self.specs = specs
