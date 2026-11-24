# Motivation

There are some existing approaches to handling RO-Crates in Python, but they all have disadvantages

## Treat them as JSON

This approach means manually handling the details of JSON-LD such as contexts, `@id` and `@type`, which are complex and confusing.

## Wrap them in generated Python classes

This approach was used by `RdfCrate` 1.x, but ultimately it was never a great fit because:

* RDF is "open". Any property can be used with any class, by default
* Entities can and should have multiple types
* RDF is a graph, meaning that the same entity can be referenced by multiple other entities, and even circular relationships are allowed
* Data types are optional in RDF, so enforcing them in Python is often a bad idea

## Use `rdflib`

`rdflib` is very close to the raw RDF, which is often great, but it has some weaknesses:

* Writing out triples is very repetitive, you have to repeat the subject many times when describing one object
* RO-Crate conventions are not handled by the library, so the `./` and `ro-crate-metadata.json` have to be manually written out
* The context/term rules of RO-Crate are quite difficult to get right. RO-Crate requires that you have a term for each IRI, but writing the context by hand is onerous and unnecessary

`RdfCrate` tries to strike a good balance by abstracting just a bit on top of `rdflib`, solving the above issues.

## Properties

Properties are `(predicate, object)` tuples, using `rdflib` terms directly.
```python
(SCHEMA.name, Literal("Michael"))
```
Is equivalent to
```json
{"name": "Michael"}
```

## Entities

Entities are just IRIs (or blank nodes).
You pass a list of properties to create or describe an entity, and types are added with `rdf:type` like any other property:
```python
me = crate.add_entity(
    URIRef("#me"),
    (RDF.type, SCHEMA.Person),
    (SCHEMA.name, Literal("Michael")),
    (SCHEMA.affiliation, wehi),
)
```
The return value from `crate.add_entity` is just the IRI, which you can then use as the object of other properties.
Properties only go from the entity being described to the object, so to make the entity the object of a property, add a plain triple:
```python
crate.add((parent, SCHEMA.hasPart, me))
```

## Mandatory Properties

Methods like `add_root_entity` take properties as `(predicate, object)` tuples, exactly like `add_entity`.
They don't check that the properties RO-Crate requires are present: that is left to validation, such as `crate.validate()`:
```python
crate.add_root_entity(
    (SCHEMA.name, Literal("Melbourne Bridges")),
    (SCHEMA.description, Literal("Photo gallery of iconic bridges in Melbourne")),
    (SCHEMA.datePublished, Literal(date.today().isoformat())),
    (SCHEMA.license, URIRef("https://creativecommons.org/licenses/by/4.0/")),
    (SCHEMA.keywords, Literal("bridges")),
)
```

## Terms

RO-Crate requires that each IRI has a short form (a term) in the JSON-LD context.
Terms in the RO-Crate context, such as `name` or `File`, are used automatically.
Any other terms must be defined in a `ContextNamespace`, and passed to the crate in `vocabs`:
```python
class Obi(ContextNamespace):
    _base = URIRef("http://purl.obolibrary.org/obo/")
    Image = _base + "IAO_0000101"


crate = AttachedCrate("crate/", vocabs=[Obi])
```
When the crate is compiled, the context will contain only the terms that are actually used.
Because the terms you use are listed explicitly, you only need to define the small subset of each ontology that you actually use, and it is easy to see which terms a project depends on.
