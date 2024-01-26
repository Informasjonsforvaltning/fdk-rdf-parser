import json
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
import requests


@pytest.fixture
def mock_reference_data_client(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    return mock


@pytest.fixture
def mock_reference_data_client_http_error(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = requests.HTTPError(
        "reference-data-not-found",
        404,
        "Not Found",
        {},
        None,
    )
    return mock


@pytest.fixture
def mock_reference_data_client_timeout_error(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = TimeoutError("connection to reference-data timed out")
    return mock


@pytest.fixture
def mock_reference_data_client_parse_error(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = json.JSONDecodeError(msg="reference-parse-error", doc="", pos=0)
    return mock
