from rdflib import URIRef


class RdfTerm:
    """
    Wrapper for a term with a label and URI.
    This is needed because RO-Crate bans the use of full URIs in JSON-LD.
    """
    #: The short name of the term
    label: str
    #: The URI of the term
    uri: URIRef

    def __init__(self, label: str, term: str) -> None:
        self.label = label
        self.uri = URIRef(term)
