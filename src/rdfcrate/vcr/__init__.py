import contextlib
import json
from pathlib import Path
from typing import Any
from urllib.request import urlopen
import vcr
import yaml

HERE = Path(__file__).parent
CONTEXT_CASSETTE = HERE / "context.yml"

class PrettyYamlSerializer:
    @staticmethod
    def serialize(cassette_dict: dict[str, Any]):
        # Parse the body if it's JSON
        for interaction in cassette_dict["interactions"]:
            body = interaction["response"]["body"]
            # Content-Type is a list
            for header in interaction["response"]["headers"]["Content-Type"]:
                if "json" in header:
                    interaction["response"]["body"] = json.loads(body["string"])
                    break

        return yaml.dump(cassette_dict, default_flow_style=False)

    @staticmethod
    def deserialize(cassette_str: str):
        parsed = yaml.load(cassette_str, Loader=yaml.SafeLoader)

        # Deserialize the body if it's JSON
        for interaction in parsed["interactions"]:
            body = interaction["response"]["body"]
            for header in interaction["response"]["headers"]["Content-Type"]:
                if "json" in header:
                    interaction["response"]["body"] = { "string": json.dumps(body) }
                    break

        return parsed

vcr = vcr.VCR()
vcr.register_serializer("prettyyaml", PrettyYamlSerializer)

def filter_headers(response: dict[str, Any]) -> dict[str, Any]:
    """
    Filters out irrelevant headers from the cassette.
    """
    # Only preserve Content-Type and Content-Length response headers
    response["headers"] = {
        k: v for k, v in response["headers"].items() if k in ["Content-Type", "Content-Length"]
    }
    return response


def generate_cassettes():
    """
    To be used as a CLI script, via `uv run regenerate-cassettes`.
    """
    CONTEXT_CASSETTE.unlink(missing_ok=True)
    with vcr.use_cassette(CONTEXT_CASSETTE, record_mode="all", serializer="prettyyaml", before_record_response=filter_headers):
        # urlopen("https://www.researchobject.org/ro-crate/specification/1.1/context.jsonld")
        # urlopen("https://www.researchobject.org/ro-crate/specification/1.2/context.jsonld")
        # urlopen("https://www.researchobject.org/ro-crate/specification/1.3/context.jsonld")
        urlopen("https://w3id.org/ro/crate/1.1/context")
        urlopen("https://w3id.org/ro/crate/1.2/context")
        urlopen("https://w3id.org/ro/crate/1.3/context")

    # # Rewrite the URLs to use the W3ID URIs
    # with CONTEXT_CASSETTE.open("r") as f:
    #     cassette = yaml.load(f, Loader=yaml.SafeLoader)
    # for interaction in cassette["interactions"]:
    #     interaction["request"]["uri"] = interaction["request"]["uri"].replace(
    #         "https://www.researchobject.org/ro-crate/specification/",
    #         "https://w3id.org/ro/crate/"
    #     ).replace(".jsonld", "")
    # with CONTEXT_CASSETTE.open("w") as f:
    #     yaml.dump(cassette, f, default_flow_style=False)

@contextlib.contextmanager
def patch_rocrate_context():
    """
    Patches HTTP requests to return a local context file instead of fetching it from the network.
    This is useful for tests that require the RO-Crate context without making network requests.
    """
    # Intercept any HTTP requests to the RO-Crate context and return a local file instead
    with (
        vcr.use_cassette(
            CONTEXT_CASSETTE,
            record_mode="none",
            serializer="prettyyaml",
            match_on=['path'],
            allow_playback_repeats=True
        ),
    ):
        yield
