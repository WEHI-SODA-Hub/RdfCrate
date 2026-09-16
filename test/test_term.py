import pytest
from rdfcrate.rdfterm import guess_term_from_uri


def test_guess_term_from_uri_with_fragment():
    uri = "http://example.org/path#fragment"
    assert guess_term_from_uri(uri) == "fragment"


def test_guess_term_from_uri_with_query():
    uri = "http://example.org/path?query=value"
    assert guess_term_from_uri(uri) == "value"


def test_guess_term_from_uri_with_path():
    uri = "http://example.org/path/to/resource"
    assert guess_term_from_uri(uri) == "resource"


def test_guess_term_from_uri_with_empty_path():
    uri = "http://example.org/"
    with pytest.raises(Exception):
        guess_term_from_uri(uri)


def test_guess_term_from_uri_with_fragment_and_query():
    # Fragment should take precedence over query
    uri = "http://example.org/path?query=value#fragment"
    assert guess_term_from_uri(uri) == "fragment"
