## Building Docs

```bash
quarto render README.qmd
quarto render docs/guide.qmd
mkdocs build
```

## Regenerating Vocabs

```bash
 uv run src/rdfcrate/codegen.py
```
