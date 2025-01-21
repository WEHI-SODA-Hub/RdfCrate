# Changelog

## 0.3.0

- Data entities created using `register_*` are now always linked to a `Dataset` via `hasPart`. By default this is the root dataset, but it can be configured using the `dataset=` keyword argument
- Added three mandatory arguments to the crate constructor: `name`, `description` and `licence`. This ensures [conformance with the spec](https://www.researchobject.org/ro-crate/specification/1.1/root-data-entity.html#direct-properties-of-the-root-data-entity).

## 0.2.0

- Use trailing slashes in all `Dataset` IDs, such as `./`
- Make `ro-crate-metadata.json` a `CreativeWork`
- Add `datePublished` to the root dataset
