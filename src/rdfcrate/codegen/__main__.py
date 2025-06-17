import ast
from pathlib import Path
import typer
from typing import Annotated
from rdfcrate.codegen import CodegenState, core_vocab, generate_modules
from rdflib.plugins.shared.jsonld.context import Context

app = typer.Typer()

@app.command()
def core_vocab():
    """
    Updates the core vocabulary inside RDFCrate.
    """
    core_vocab()

@app.command()
def custom_context(context: Path, ontologies: Annotated[list[Path], typer.Option(help="Extra ontology files to load")] = []):
    """
    Generates a Python file that contains classes for the given context.

    Params:
        context: Path to the context file to generate.
        ontologies: List of ontology files to include in the context. Currently not implemented.
    """
    state = CodegenState()
    module = state.process_context(Context(str(context)))
    print(ast.unparse(module))

@app.command()
def custom_vocab(vocab: Path, ontologies: Annotated[list[Path], typer.Option(help="Extra ontology files to load")] = []):
    """
    Generates a Python file that contains classes for the given context.

    Params:
        vocab: Path to the vocabulary file to generate code for.
        ontologies: List of ontology files to include in the context. Currently not implemented.
    """
    state = CodegenState()
    module = state.process_rdf(
        base_module="",
        vocab_uri=str(vocab),
        vocab_name=""
    )
    print(ast.unparse(module))

if __name__ == "__main__":
    app()
