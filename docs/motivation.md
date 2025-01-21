# Motivation

RO-Crate is stored as JSON-LD, which seems user-friendly to people who are used to working with JSON.
Unfortunately, once you get beyond the basics, JSON-LD is actually quite complex.
It has special keys like `@context`, `@id` and `@type`, it has multiple ways to represent relationships, it has multiple forms like framed, flattened and expanded, and it uses URL prefixes.
Because of this, you might find it easier to just embrace RDF concepts directly, where everything is just a triple of subject (the thing being described), predicate (the relationship) and object (the value), that's it!

RdfCrate provide some helpful utilities for creating RO-Crates on top of RDF, but it never tries to disguise it.
