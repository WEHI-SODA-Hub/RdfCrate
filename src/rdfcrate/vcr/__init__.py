import contextlib
from copy import deepcopy
from dataclasses import dataclass
from importlib.resources.abc import Traversable
from pathlib import Path
from typing import Any, TYPE_CHECKING
from urllib.request import urlopen
import vcr
import yaml
from importlib.resources import files

if TYPE_CHECKING:
    from vcr.cassette import Cassette
    from vcr.request import Request


HERE = files(__name__)
CONTEXT_CASSETTE = HERE / "context.yml"


@dataclass
class ExternalFileSerializer:
    """
    VCR serializer that stores large response bodies in external files instead of inline in the cassette.

    Params:
        write_path: Directory where external files will be stored.
        read_path: Directory where external files will be read from when deserializing. This may differ from the write path if e.g. you want to read from the package distribution
        min_size: Minimum size of the response body to be stored in an external file.
    """
    base_path: Traversable
    min_size: int = 1024

    def serialize(self, cassette_dict: dict[str, Any]):
        if not isinstance(self.base_path, Path):
            raise ValueError("When writing to external files, base_path must be a writeable path ie the package must be installed in editable mode.")

        for interaction in cassette_dict["interactions"]:
            body = interaction["response"]["body"]
            if isinstance(body, dict) and "string" in body and len(body["string"]) > self.min_size:
                # Write the body to an external file
                file_path = self.base_path / f"{interaction['request']['uri'].replace('/', '_').replace(':', '_')}.body"
                with file_path.open("w") as f:
                    f.write(body["string"])
                # Replace the body with a reference to the external file
                interaction["response"]["body"] = {
                    "external_file": str(file_path.relative_to(self.base_path))
                }
        return yaml.dump(cassette_dict, default_flow_style=False)

    def deserialize(self, cassette_str: str):
        parsed = yaml.load(cassette_str, Loader=yaml.SafeLoader)
        for interaction in parsed["interactions"]:
            body = interaction["response"]["body"]
            if isinstance(body, dict) and "external_file" in body:
                path = self.base_path / body["external_file"]
                interaction["response"]["body"] = {"string": path.read_text()}
        return parsed

vcr = vcr.VCR()
vcr.register_serializer("externalfile", ExternalFileSerializer(base_path=HERE, min_size=1024))

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
    if not isinstance(CONTEXT_CASSETTE, Path):
        raise ValueError("When regenerating cassettes, the package must be installed in editable mode.")

    CONTEXT_CASSETTE.unlink(missing_ok=True)

    cassette: "Cassette"
    with vcr.use_cassette(CONTEXT_CASSETTE, record_mode="all", serializer="externalfile", before_record_response=filter_headers) as cassette:
        urlopen("https://www.researchobject.org/ro-crate/specification/1.1/context.jsonld")
        urlopen("https://www.researchobject.org/ro-crate/specification/1.2/context.jsonld")
        urlopen("https://www.researchobject.org/ro-crate/specification/1.3/context.jsonld")

        extra_interactions = []
        for existing_request, response in cassette.data:
            w3id_request: "Request" = deepcopy(existing_request)
            w3id_request.uri = existing_request.uri.replace("https://www.researchobject.org/ro-crate/specification", "https://w3id.org/ro/crate").replace("context.jsonld", "context")
            w3id_request.headers["Host"] = ["w3id.org"]
            extra_interactions.append((w3id_request, response))
        for request, response in extra_interactions:
            cassette.append(request, response)

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
            serializer="externalfile",
            match_on=['uri'],
            allow_playback_repeats=True
        ),
    ):
        yield
