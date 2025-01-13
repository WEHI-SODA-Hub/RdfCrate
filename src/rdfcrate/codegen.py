"""
Generates URIs for everything in the RO-Crate context
"""
import ast
import requests
import keyword

def make_module(context: dict) -> ast.Module:
    body: list[ast.stmt] = [
        ast.ImportFrom(module="rdflib", names=[ast.alias(name="URIRef")]),
    ]
    for key, value in context["@context"].items():
        # Workaround for invalid Python identifiers
        if (not key.isidentifier()) or keyword.iskeyword(key):
            key = "_" + key.replace("-", "_")
        body.append(ast.Assign(
            targets=[ast.Name(key)],
            value=ast.Call(
                func=ast.Name("URIRef"),
                args=[ast.Constant(value)],
                keywords=[]
            )
        ))

    return ast.Module(body=body, type_ignores=[])

def main():
    res = requests.get("https://www.researchobject.org/ro-crate/specification/1.2-DRAFT/context.jsonld")
    res.raise_for_status()
    module = make_module(res.json())
    ast.fix_missing_locations(module)
    print(ast.unparse(module))

if __name__ == "__main__":
    main()
