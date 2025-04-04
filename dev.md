## Building Docs

```bash
quarto render README.qmd
quarto render docs/guide.qmd
mkdocs build
```

## Regenerating URIs

* Comment out the contents of `__init__.py`
* `doit`
* Uncomment out the contents of `__init__.py`

## Typed Dict Design

* `TypedDicts` or dataclasses would help detect type errors
* LinkML isn't currently ideal for this because of https://github.com/WEHI-SODA-Hub/proclaim/blob/main/linkml_issues.md
* Difficulties are:
    * We don't want to be too strict because any property can be used with any type
    * Classes need to accept multiple types
* The only real constraints: 
    * The range of properties, because these are constrained e.g. in RDFS
    * The RO-Crate restrictions like the mandatory license for the root data entity
