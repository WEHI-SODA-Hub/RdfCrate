# Motivation

The most user friendly interface for Python users is probably a library of classes with properties that can be composed together.
This is intuitive due to common usage in Python, and demonstrated by the popularity of Pydantic.
However, strictly following this design by generating actual Pydantic classes does not suit RDF (which underlies RO-Crate) because:

* RDF is "open". Any property can be used with any class, by default
* Entities can and should have multiple types
* RDF is a graph, meaning that the same entity can be referenced by multiple other entities, and even circular relationships are allowed. In contrast, a Pydantic graph is just a tree.

`rdfcrate` tries to make concessions for these aspects of RDF.

## Properties

Firstly, properties are defined as classes themselves, so this:
```python
sdo.name(sdo.Text("Michael")),
```
Is equivalent to
```json
{"name": "Michael"}
```
It is defined this way because properties need to be decoupled from classes.
Almost any property should be usable on any class, and users should be able to define custom properties and use them on built-in classes.
These properties do mandate certain types as their arguments, which allows you to catch basic type errors statically.

## Classes

While Python classes are generated for each RDF class, they do not define required properties.
Instead, you pass a list of these properties to construct a new entity:
```python
crate.add_entity(
    "#me",
    sdo.Person,
    sdo.name(sdo.Text("Michael")),
    sdo.affiliation(wehi)
)
```
The return value from `crate.add_entity` is just an ID (an IRI), not an actual object with properties.
This allows you to flexibly link entities in a graph.

## Positional Arguments
We don't use keyword arguments when constructing entities, because this is redundant when the properties themselves are classes.
Also, using position arguments allows us to define some properties as mandatory and others as optional, for example:
```python
def add_root_entity(
    self,
    name: schemaorg.name,
    description: schemaorg.description,
    date_published: schemaorg.datePublished,
    license: schemaorg.license,
    *props: RdfProperty | ReverseProperty,
    recursive: Recursive = False
) -> schemaorg.Dataset:
```
It wouldn't be possible to allow user-defined properties with specific types as well as allowing the class to define required properties, with keyword arguments.
Also, there would be no easy way to associate keywords with IRIs, since a `TypedDict` must have string keys. 

## Terms

RO-Crate requires that each IRI has a short form, and it also mandates the use of certain terms like `File` which are just aliases.
To support this, all classes and properties have an associated `RdfTerm` object, which tracks both the alias and the IRI.
