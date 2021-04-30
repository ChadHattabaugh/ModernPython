"""General methods used across all test modules."""
from unittest.mock import Mock

import pytest
from _pytest.config import Config
from pytest_mock import MockFixture


@pytest.fixture
def mock_request_get(mocker: MockFixture) -> Mock:
    """Returns a mock of the Page element."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem Ipsum dolor sit amet",
    }
    return mock


def pytest_configure(config: Config) -> None:
    """Adds 'e2e' market to the configuration."""
    config.addinivalue_line("markers", "e2e: mark as end to end test")
