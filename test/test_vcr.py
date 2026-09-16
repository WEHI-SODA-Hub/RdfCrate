"""
Tests for `rdfcrate.vcr`.
"""

from datetime import datetime
from unittest.mock import patch

from rdfcrate import AttachedCrate
from rdfcrate.vcr import patch_rocrate_context
from rdfcrate.vocabs import sdo


def test_patch_rocrate_context_reads_cassette_from_disk(tmp_path):
    """
    When `patch_rocrate_context` is used, `urlopen` should not be called, and the crate should be able to be compiled without network access.
    """
    with patch("urllib.request.urlopen") as mock_urlopen:
        with patch_rocrate_context():
            crate = AttachedCrate(tmp_path)
            crate.add_root_entity(
                sdo.name(sdo.Text("Test Crate")),
                sdo.description(sdo.Text("Crate for validating RdfCrate")),
                sdo.datePublished(sdo.DateTime(datetime.now().isoformat())),
                sdo.license(
                    crate.add_entity(
                        sdo.CreativeWork("https://opensource.org/license/mit"),
                        sdo.name(sdo.Text("MIT License")),
                    )
                ),
            )
            crate.compile()

        mock_urlopen.assert_not_called()
