# RdfCrate

RO-Crate builder that uses RDF concepts.

## Motivation

RO-Crate is stored as JSON-LD, which seems user-friendly to people who are used to working with JSON.
Unfortunately, once you get beyond the basics, JSON-LD is actually quite complex.
It has special keys like `@context`, `@id` and `@type`, it has multiple ways to represent relationships, it has multiple forms like framed, flattened and expanded, and it uses URL prefixes.
At this level, it becomes easier to just embrace RDF concepts directly, where everything is just a triple of subject (the thing being described), predicate (the relationship) and object (the value), that's it!

RdfCrate provide some helpful utilities for creating RO-Crates on top of RDF, but it never tries to disguise it.

## Example

Let's say you have a directory with one file in it, which you want to document.
Here's how you could make an RO-Crate using RdfCrate:

```python
from rdfcrate import AttachedCrate, uris
from rdflib import Literal

crate = AttachedCrate("/path/to/directory")
crate.register_file("photo.jpg", {
    uris.name: Literal("Cool cat photo")
})
crate.compile()
```
```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "photo.jpg",
      "@type": "File",
      "encodingFormat": "image/jpeg",
      "name": "Cool cat photo"
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
    },
    {
      "@id": ".",
      "@type": "Dataset"
    }
  ]
}
```
