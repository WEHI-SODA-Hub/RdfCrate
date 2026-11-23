import contextlib
import os
from pathlib import Path
from unittest.mock import patch
from urllib.request import urlopen

import vcr
import yaml

HERE = Path(__file__).parent
CONTEXT_CASSETTE = HERE / "context.yml"


def generate_cassettes():
    """
    To be used as a CLI script, via `uv run regenerate-cassettes`.
    """
    # Record cassettes, bypassing the W3ID proxy
    with vcr.use_cassette(CONTEXT_CASSETTE, record_mode="always"):
        urlopen(
            "https://www.researchobject.org/ro-crate/specification/1.1/context.jsonld"
        )
        urlopen(
            "https://www.researchobject.org/ro-crate/specification/1.2/context.jsonld"
        )
        urlopen(
            "https://www.researchobject.org/ro-crate/specification/1.3/context.jsonld"
        )

    # Rewrite the URLs to use the W3ID URIs
    with CONTEXT_CASSETTE.open("r") as f:
        cassette = yaml.load(f, Loader=yaml.SafeLoader)
    for interaction in cassette["interactions"]:
        interaction["request"]["uri"] = (
            interaction["request"]["uri"]
            .replace(
                "https://www.researchobject.org/ro-crate/specification/",
                "https://w3id.org/ro/crate/",
            )
            .replace(".jsonld", "")
        )
    with CONTEXT_CASSETTE.open("w") as f:
        yaml.dump(cassette, f, default_flow_style=False)


@contextlib.contextmanager
def patch_rocrate_context():
    """
    Patches the `urlopen` function to return a local context file instead of fetching it from the network.
    This is useful for tests that require the RO-Crate context without making network requests.

    Params:
        import_path: The import path of the `urlopen` function to patch. Default is "rdflib._networking.urlopen".
    """
    # Intercept any HTTP requests to the RO-Crate context and return a local file instead
    with (
        vcr.use_cassette(
            CONTEXT_CASSETTE,
            record_mode="none",
            match_on=["path"],
            allow_playback_repeats=True,
        ),
        # Stop the validator from pre-fetching profile resources outside the cassette
        patch.dict(os.environ, {"ROCRATE_VALIDATOR_AUTO_WARM": "0"}),
    ):
        yield
