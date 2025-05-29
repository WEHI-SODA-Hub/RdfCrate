## Building Docs

```bash
quarto render README.qmd
mkdocs build
```

## Regenerating Vocabs

```bash
for file in bioschemas.py bioschemas_drafts.py dc.py geo.py owl.py pav.py pcdm.py prof.py prov.py rdf.py rdfs.py rocrate.py schemaorg.py; do
    truncate -s 0 "src/rdfcrate/vocabs/${file}"
done
uv run -m rdfcrate.codegen
```
