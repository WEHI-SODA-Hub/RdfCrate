# RdfCrate


`rdfcrate` is a Python package for working with RO-Crates which treats
RO-Crates as RDF graphs rather than JSON objects.

## Advantages

- Simple API that doesn’t require understanding JSON-LD
- Library of types and properties to speed up development and ensure
  correctness
- Valid JSON-LD guaranteed
- Type checker friendly

## Installation

``` bash
pip install rdfcrate
```

## Example

Let’s say you have a directory with one file in it, which you want to
document. Here’s how you could make an RO-Crate using RdfCrate:

``` python
from rdfcrate import AttachedCrate, sdo
from datetime import date

crate = AttachedCrate("crate/")
crate.register_file(
    "monty.jpg", 
    sdo.name(sdo.Text("Montague Street Bridge"))
)
crate.add_root_entity(
    sdo.name(sdo.Text("Melbourne Bridges")),
    sdo.description(sdo.Text("Photo gallery of iconic bridges in Melbourne")),
    sdo.datePublished(sdo.Date(date.today())),
    sdo.license(sdo.URL("https://creativecommons.org/licenses/by/4.0/"))
)
print(crate.compile())
```

    {
      "@context": "https://w3id.org/ro/crate/1.1/context",
      "@graph": [
        {
          "@id": "./",
          "@type": "Dataset",
          "datePublished": {
            "@type": "http://www.w3.org/2001/XMLSchema#date",
            "@value": "2025-10-10"
          },
          "description": "Photo gallery of iconic bridges in Melbourne",
          "hasPart": {
            "@id": "monty.jpg"
          },
          "license": "https://creativecommons.org/licenses/by/4.0/",
          "name": "Melbourne Bridges"
        },
        {
          "@id": "monty.jpg",
          "@type": "File",
          "encodingFormat": "image/jpeg",
          "name": "Montague Street Bridge"
        }
      ]
    }
