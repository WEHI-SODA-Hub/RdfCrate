from rdflib import Graph, RDF, URIRef
from rdflib.plugins.shared.jsonld.context import Context

url = Context("https://w3id.org/ro/crate/1.1/context")
extra = Context(
    {
        "LabProtocol": "https://bioschemas.org/draft_terms/LabProtocol",
        "Enzyme": "https://bioschemas.org/draft_terms/Enzyme",
    }
)
combined = Context([url, extra])

graph = Graph()
graph.add(
    (URIRef("http://example.org/howto"), RDF.type, URIRef("http://schema.org/HowTo"))
)
graph.add(
    (
        URIRef("http://example.org/LabProtocol"),
        RDF.type,
        URIRef("https://bioschemas.org/draft_terms/LabProtocol"),
    )
)
