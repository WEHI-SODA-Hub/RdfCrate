# Motivation

RO-Crates are JSON-LD documents, but working with them as JSON means handling the details of JSON-LD such as contexts, `@id` and `@type`.
`rdfcrate` instead treats an RO-Crate as an RDF graph, so you work with plain `rdflib` triples and the JSON-LD is generated for you.

Previous versions of `rdfcrate` wrapped every RDF class, property and datatype in a Python class, so that a type checker could catch errors such as passing the wrong type of value to a property.
In practice this added a lot of complexity, and was never a good fit for RDF:

* RDF is "open". Any property can be used with any class, by default
* Entities can and should have multiple types
* RDF is a graph, meaning that the same entity can be referenced by multiple other entities, and even circular relationships are allowed

`rdfcrate` now leaves validation to tools designed for it, such as SHACL, and focuses on building the graph and its context.

## Properties

Properties are `(predicate, object)` tuples, using `rdflib` terms directly.
The examples here use `RDF` from `rdflib`, and `SCHEMA` from `rdfcrate.wrapper`, which is `Namespace("http://schema.org/")`.
Note that RO-Crate uses `http://schema.org/`, so `rdflib.SDO`, which uses `https://schema.org/`, should not be used.
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
    "#me",
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

Methods like `add_root_entity` take the properties that RO-Crate requires as positional arguments, and any others after them:
```python
crate.add_root_entity(
    "Melbourne Bridges",
    "Photo gallery of iconic bridges in Melbourne",
    date.today(),
    URIRef("https://creativecommons.org/licenses/by/4.0/"),
    (SCHEMA.keywords, Literal("bridges")),
)
```

## Terms

RO-Crate requires that each IRI has a short form (a term) in the JSON-LD context.
Terms in the RO-Crate context, such as `name` or `File`, are used automatically.
Any other terms must be defined in a `ContextNamespace`, and passed to the crate in `vocabs`:
```python
class Obi(ContextNamespace, context_prefix="obi"):
    _base = URIRef("http://purl.obolibrary.org/obo/")
    Image = _base + "IAO_0000101"

crate = AttachedCrate("crate/", vocabs=[Obi])
```
When the crate is compiled, the context will contain only the terms that are actually used.
If `context_prefix` is set, it is prepended to every term label to avoid clashes with other vocabularies, and if `_base` is also set, the context will use CURIEs:
```json
{"obi": "http://purl.obolibrary.org/obo/", "obiImage": "obi:IAO_0000101"}
```
Compiling a crate raises an error if two terms clash, or if an IRI used as a predicate, type or datatype has no term.

Because the terms you use are listed explicitly, you only need to define the small subset of each ontology that you actually use, and it is easy to see which terms a project depends on.
