

# RdfCrate

RO-Crate builder that uses RDF concepts.

**[Detailed documentation available
here](https://wehi-soda-hub.github.io/RdfCrate/)**.

## Advantages

- Simple API that doesn’t require understanding JSON-LD
- Library of types and properties to speed up development and ensure
  correctness
- Valid JSON-LD guaranteed
- Type checker friendly

## Example

Let’s say you have a directory with one file in it, which you want to
document. Here’s how you could make an RO-Crate using RdfCrate:

``` python
from rdfcrate import AttachedCrate, uris
from rdflib import Literal

crate = AttachedCrate("/path/to/crate")
crate.register_file("salvatore.jpg", [
    (uris.name, Literal("Salvatore the Seal"))
])
print(crate.compile())
```

    {
      "@context": "https://w3id.org/ro/crate/1.1/context",
      "@graph": [
        {
          "@id": ".",
          "@type": "Dataset"
        },
        {
          "@id": "salvatore.jpg",
          "@type": "File",
          "encodingFormat": "image/jpeg",
          "name": "Salvatore the Seal"
        },
        {
          "@id": "ro-crate-metadata.json",
          "@type": "File",
          "about": {
            "@id": "."
          },
          "conformsTo": {
            "@id": "https://w3id.org/ro/crate/1.1"
          },
          "encodingFormat": "application/json"
        }
      ]
    }
