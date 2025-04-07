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
    #: List of RO-Crate versions numbers for which this term is automatically included in the context 
    specs: list[str]

    def __init__(self, label: str, term: str, specs: list[str] = []) -> None:
        self.label = label
        self.uri = URIRef(term)
        self.specs = specs
