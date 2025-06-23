import ast
from pathlib import Path
import typer
from typing import Annotated
from rdfcrate.codegen import CodegenState, core_vocab, generate_modules
from rdflib.plugins.shared.jsonld.context import Context

app = typer.Typer()


@app.command()
def core():
    """
    Updates the core vocabulary inside RDFCrate.
    """
    core_vocab()


@app.command()
def custom_context(
    context: Path,
    ontologies: Annotated[
        list[Path], typer.Option(help="Extra ontology files to load")
    ] = [],
):
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
def custom_vocabs(
    vocabs: Annotated[
        list[Path],
        typer.Argument(
            help="A list of vocabularies/ontologies to generate code for. Note that you will also need any dependencies to be included,  so for example OWL should often be included in this list. You can then delete the owl.py file that gets generated."
        ),
    ],
    output_dir: Annotated[
        Path, typer.Option(help="Output directory for generated code")
    ],
):
    """
    Generates a Python file that contains classes and properties for the given vocabularies.
    """
    generate_modules(
        vocabs={vocab.stem: str(vocab) for vocab in vocabs},
        out_dir=output_dir,
        base_module=".",
        contexts={},
    )


if __name__ == "__main__":
    app()
