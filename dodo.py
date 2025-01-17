import json
from typing import Literal
from rdfcrate.codegen import module_from_context, module_from_rdfs, uris_from_rdfs
from ast import unparse, Constant, Expr, Module
from pathlib import Path
import requests

git_repo = Path("specifications").resolve()

DOIT_CONFIG = {
    'check_file_uptodate': 'timestamp'
}

def add_docstring(module: Module, docstring: str):
    module.body.insert(0, Expr(Constant(docstring)))

def task_clone_bioschemas():
    """
    Clones the BioSchemas specifications repository
    """
    return {
        "actions": ["git clone https://github.com/BioSchemas/specifications.git --depth 1"],
        "targets": [git_repo],
        # See https://pydoit.org/dependencies.html?highlight=uptodate#doit-up-to-date-definition
        "uptodate": [True]
    }

def task_bioschemas():
    """
    Generates a Python module with URIs from the BioSchemas specifications
    """
    dest_path = Path(__file__).parent / "src/rdfcrate/bioschemas.py"

    def _action():
        assignments = []
        for file in git_repo.rglob("*.jsonld"):
            try:
                assignments += list(uris_from_rdfs(file.read_text()))
            except json.JSONDecodeError:
                print(f"Failed to parse {file}")
        module = module_from_rdfs(assignments)
        add_docstring(module, "URIs for Bioschemas")
        dest_path.write_text(unparse(module))

    return {
        "actions": [_action],
        "file_dep": [git_repo],
        "targets": [dest_path],
    }

def task_rocrate_uris():
    """
    Generates a Python module with URIs from the RO-Crate context
    """
    dest_path = Path(__file__).parent / "src/rdfcrate/uris.py"

    def _task():
        module = module_from_context(requests.get("https://w3id.org/ro/crate/1.2-DRAFT/context").json())
        add_docstring(module, "URIs for RO-Crate")
        dest_path.write_text(unparse(module))

    return {
        "actions": [_task],
        "targets": [dest_path],
        "uptodate": [True]
    }
