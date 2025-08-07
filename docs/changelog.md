# Changelog

## 1.1.0

* Added `ContextGraph`, a superclass of `RoCrate` which isn't tied to any RO-Crate specifics. This is designed to be a better API target for more general manipulations
* Added `navigate()` and `navigate_to()` functions to `ContextGraph` which are therefore also accessible as `RoCrate` methods. These use the optional `rdfnav` dependency to allow for easy querying and mutation of the graph. Both will throw an exception if `rdfnav` is not installed.
* Added `register_term()` method to `ContextGraph` and subclasses, for registering a single term. 
* Both `register_term()` and `register_terms()` now support `rdflib` `Term` classes now
* Created a `PropertyProtocol` which is implemented by both `RdfProperty` and `ReverseProperty`. This allows APIs to more easily target both simultaneously
* `RdfProp` and `RdfType` subclasses are now responsible for registering their own terms. Previously this was the responsibility of `RoCrate`
* `ContextGraph` and subclasses are no longer dataclasses
* `ContextGraph.context_source` and `ContextGraph.full_context` provide different APIs for accessing the context


## 1.0.0

### Breaking

- Refactored the way types and properties are specified.
    - Creating a new entity is done using `crate.add_entity(ClassType(IRI), *properties)`
    - Rather than being tuples of `(predicate, object)`, properties themselves are now also classes that you instantiate: `sdo.name(sdo.Text("WEHI Research Computing Platform"))`
    - Mandatory fields are no longer keyword arguments
- `RdfClass` and `RdfDataType` are classes that capture a single IRI with its inheritance hierarchy and terms. Typically you pre-generate them from a vocabulary or use the built-in classes, and then call its constructor with an IRI to make an instance of that class. For example: `sdo.Thing("#my_iri")`
- The root data entity entity is no longer added automatically, and instead should be created using `crate.add_root_entity`
- The bundled vocabularies have been moved from `rdfcrate.uris` and `rdfcrate.bioschemas` into `rdfcrate.vocabs`. There are quite a number more now, including Dublin Core, `prof`, etc

### Miscellaneous

- It is now much easier to nest complex graphs in one statement, especially using the walrus operation (`:=`) and the `RdfProperty.reverse()` methods
- Custom classes and properties will automatically be added to the JSON-LD context
- All IRIs now have an associated label, which is better compatible with RO-Crate's requirement to not use raw IRIs
- Relaxed the requirement for IRIs to be provided as `URIRef()` when creating entities
- Added `ruff` linter
- Added `.validate()` and `.get_issues()` methods for easy validation of the crate [[#22](https://github.com/WEHI-SODA-Hub/RdfCrate/pull/22)]
- Added `.to_type_property()` to `RdfType` subclasses, to facilitate multi-class entities (see `test_multi_type`)
- Added `RdfProperty.adhoc(term=RdfTerm(...), object=...)` for defining single-use properties

## 0.3.0

- Data entities created using `register_*` are now always linked to a `Dataset` via `hasPart`. By default this is the root dataset, but it can be configured using the `dataset=` keyword argument
- Added three mandatory arguments to the crate constructor: `name`, `description` and `licence`. This ensures [conformance with the spec](https://www.researchobject.org/ro-crate/specification/1.1/root-data-entity.html#direct-properties-of-the-root-data-entity).

## 0.2.0

- Use trailing slashes in all `Dataset` IDs, such as `./`
- Make `ro-crate-metadata.json` a `CreativeWork`
- Add `datePublished` to the root dataset
