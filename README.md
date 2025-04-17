

# RdfCrate

`rdfcrate` is a Python package for working with RO-Crates which treats
RO-Crates as RDF graphs rather than JSON objects.

**[Detailed documentation available
here](https://wehi-soda-hub.github.io/RdfCrate/)**.

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
print(crate.root)
crate.register_file(
    "salvatore.jpg", 
    sdo.name(sdo.Text("Salvatore the Seal"))
)
crate.add_root_entity(
    sdo.name(sdo.Text("Melbourne Photos")),
    sdo.description(sdo.Text("Photo gallery of iconic things in Melbourne")),
    sdo.datePublished(sdo.Date(date.today())),
    sdo.license(sdo.URL("https://creativecommons.org/licenses/by/4.0/"))
)
print(crate.compile())
```

    /Users/milton.m/Programming/RdfCrate/crate
    {
      "@context": "https://w3id.org/ro/crate/1.1/context",
      "@graph": [
        {
          "@id": "./",
          "@type": "Dataset",
          "datePublished": {
            "@type": "http://www.w3.org/2001/XMLSchema#date",
            "@value": "2025-04-17"
          },
          "description": "Photo gallery of iconic things in Melbourne",
          "hasPart": {
            "@id": "salvatore.jpg"
          },
          "license": "https://creativecommons.org/licenses/by/4.0/",
          "name": "Melbourne Photos"
        },
        {
          "@id": "salvatore.jpg",
          "@type": "File",
          "encodingFormat": "image/jpeg",
          "name": "Salvatore the Seal"
        }
      ]
    }
