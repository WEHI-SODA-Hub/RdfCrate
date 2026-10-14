# RdfCrate


`rdfcrate` is a Python package for working with RO-Crates which treats
RO-Crates as RDF graphs rather than JSON objects.

## Advantages

- Simple API that doesn’t require understanding JSON-LD
- Uses plain `rdflib` terms, so any RDF vocabulary can be used
- JSON-LD context generated automatically, containing only the terms you
  use
- Valid JSON-LD guaranteed

## Installation

``` bash
pip install rdfcrate
```

## Example

Let’s say you have a directory with one file in it, which you want to
document. Here’s how you could make an RO-Crate using RdfCrate:

``` python
from datetime import date

from rdflib import RDF, Literal, URIRef
from rdfcrate import AttachedCrate, ContextNamespace
from rdfcrate.wrapper import SCHEMA

# Terms outside of the RO-Crate context are defined in a ContextNamespace
class Wikidata(ContextNamespace, context_prefix="wd"):
    _base = URIRef("http://www.wikidata.org/entity/")
    Photograph = _base + "Q125191"

crate = AttachedCrate("crate/", vocabs=[Wikidata])
crate.register_file(
    "monty.jpg",
    (SCHEMA.name, Literal("Montague Street Bridge")),
    (RDF.type, Wikidata.Photograph),
)
crate.add_root_entity(
    "Melbourne Bridges",
    "Photo gallery of iconic bridges in Melbourne",
    date.today(),
    URIRef("https://creativecommons.org/licenses/by/4.0/"),
)
print(crate.compile())
```

    {
      "@context": [
        "https://w3id.org/ro/crate/1.1/context",
        {
          "wd": "http://www.wikidata.org/entity/",
          "wdPhotograph": "wd:Q125191"
        }
      ],
      "@graph": [
        {
          "@id": "./",
          "@type": "Dataset",
          "datePublished": "2026-10-14",
          "description": "Photo gallery of iconic bridges in Melbourne",
          "hasPart": {
            "@id": "monty.jpg"
          },
          "license": {
            "@id": "https://creativecommons.org/licenses/by/4.0/"
          },
          "name": "Melbourne Bridges"
        },
        {
          "@id": "monty.jpg",
          "@type": [
            "File",
            "wdPhotograph"
          ],
          "encodingFormat": "image/jpeg",
          "name": "Montague Street Bridge"
        }
      ]
    }
