import json
from typing import Any
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
import requests


def reference_effect(*args: Any, **kwargs: Any) -> Mock:
    rsp = Mock(spec=requests.Response)
    rsp.status_code = 200
    rsp.raise_for_status.return_value = None

    return add_reference_response_to_mock(rsp, args[0])


def add_reference_response_to_mock(mock: Mock, url: str) -> Mock:
    if "eu/main-activities" in url:
        mock.json.return_value = json.load(open("./tests/json_data/types.json"))
    elif "digdir/evidence-types" in url:
        mock.json.return_value = json.load(open("./tests/json_data/evidencetypes.json"))
    elif "/digdir/service-channel-types" in url:
        mock.json.return_value = json.load(
            open("./tests/json_data/serviceChannelTypes.json")
        )
    elif "adms/publisher-types" in url:
        mock.json.return_value = json.load(
            open("./tests/json_data/publishertypes.json")
        )
    elif "digdir/role-types" in url:
        mock.json.return_value = json.load(open("./tests/json_data/roletypes.json"))

    return mock


@pytest.fixture
def mock_reference_data_client(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = reference_effect
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
