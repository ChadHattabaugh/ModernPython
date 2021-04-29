
import pytest

@pytest.fixture
def mock_request_get(mocker):
    mock =  mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
            "title": "Lorem Ipsum"
            ,"extract":"Lorem Ipsum dolor sit amet"
    }
    return mock