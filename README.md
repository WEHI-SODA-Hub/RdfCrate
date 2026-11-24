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

from rdflib import DCMITYPE, RDF, Literal, URIRef
from rdfcrate import SCHEMA, AttachedCrate, ContextNamespace


# Terms outside of the RO-Crate context are defined in a ContextNamespace
class DcmiType(ContextNamespace):
    StillImage = DCMITYPE.StillImage


crate = AttachedCrate("crate/", vocabs=[DcmiType])
crate.register_file(
    "monty.jpg",
    (SCHEMA.name, Literal("Montague Street Bridge")),
    (RDF.type, DcmiType.StillImage),
)
crate.add_root_entity(
    "Melbourne Bridges",
    "Photo gallery of iconic bridges in Melbourne",
    date.today(),
    URIRef("https://creativecommons.org/licenses/by/4.0/"),
)
crate.add_metadata_entity()
print(crate.compile())
```

    {
      "@context": [
        "https://w3id.org/ro/crate/1.3/context",
        {
          "StillImage": "http://purl.org/dc/dcmitype/StillImage"
        }
      ],
      "@graph": [
        {
          "@id": "ro-crate-metadata.json",
          "@type": "CreativeWork",
          "about": {
            "@id": "./"
          },
          "conformsTo": {
            "@id": "https://w3id.org/ro/crate/1.3"
          }
        },
        {
          "@id": "monty.jpg",
          "@type": [
            "File",
            "StillImage"
          ],
          "encodingFormat": "image/jpeg",
          "name": "Montague Street Bridge"
        },
        {
          "@id": "./",
          "@type": "Dataset",
          "datePublished": "2026-11-23",
          "description": "Photo gallery of iconic bridges in Melbourne",
          "hasPart": {
            "@id": "monty.jpg"
          },
          "license": {
            "@id": "https://creativecommons.org/licenses/by/4.0/"
          },
          "name": "Melbourne Bridges"
        }
      ]
    }
