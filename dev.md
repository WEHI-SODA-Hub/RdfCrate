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
