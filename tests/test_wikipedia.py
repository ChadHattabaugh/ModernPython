"""Test for the Wikipedia Rest api module."""
from unittest.mock import Mock

import click
import pytest

from modern_python import wikipedia


def test_random_page_uses_given_language(mock_request_get: Mock) -> None:
    """It uses the language argument passed to it."""
    wikipedia.random_page(language="de")
    args, _ = mock_request_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_request_get: Mock) -> None:
    """It returns an instance of a page."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_valdiation_error(mock_request_get: Mock) -> None:
    """It handles validation errors with CLI exceptions."""
    mock_request_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()
