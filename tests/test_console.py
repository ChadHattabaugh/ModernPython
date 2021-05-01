"""Test for the CLI interface."""
from unittest.mock import Mock

import pytest
import requests
from click.testing import CliRunner
from pytest_mock import MockFixture

from modern_python import console


@pytest.fixture
def runner() -> CliRunner:
    """Returns a Click CLI mock."""
    return CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """Returns a MockFixture for a Wikipedia page."""
    return mocker.patch("modern_python.wikipedia.random_page")


def test_main_succeeds(runner: CliRunner, mock_request_get: Mock) -> None:
    """It exists with a status code of 0."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_request_get: Mock) -> None:
    """It returns the text of a Page.title element."""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_request_get: Mock) -> None:
    """It calls the reguests.git function wihtout error."""
    runner.invoke(console.main)
    assert mock_request_get.called


def test_main_uses_en_wikioedia_org(runner: CliRunner, mock_request_get: Mock) -> None:
    """By default, it calls the en.wikipedia.org Url."""
    runner.invoke(console.main)
    args, _ = mock_request_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner: CliRunner, mock_request_get: Mock) -> None:
    """It returns an exit code of 1 when an error is encoutnered."""
    mock_request_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_requests_error(
    runner: CliRunner, mock_request_get: Mock
) -> None:
    """Prints an error message containing "ERROR" when an exception occurs."""
    mock_request_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_uses_specifiied_language(
    runner: CliRunner, mock_wikipedia_random_page: Mock
) -> None:
    """It uses the specified language argument."""
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


@pytest.mark.e2e
def test_main_successds_in_production_environment(runner: CliRunner) -> None:
    """End to end test to ensure it returns an exit code of 0."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
