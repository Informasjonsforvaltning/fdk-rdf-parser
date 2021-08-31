import json
from typing import Any
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
import requests

from .testdata import org_response_0


@pytest.fixture
def mock_organizations_client(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.return_value.text = org_response_0
    return mock


def org_path_from_arg(*args: Any, **kwargs: Any) -> str:
    rsp = Mock(spec=requests.Response)
    rsp.status_code = 200
    rsp.raise_for_status.return_value = None
    rsp.text = f"/ANNET/{str(args[0]).split('/').pop()}"
    return rsp


@pytest.fixture
def mock_orgpath_client(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = org_path_from_arg
    return mock


@pytest.fixture
def mock_organizations_error(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = requests.HTTPError(
        "https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
        404,
        "Not Found",
        {},
        None,
    )
    return mock


def reference_effect(*args: Any, **kwargs: Any) -> Mock:
    rsp = Mock(spec=requests.Response)
    rsp.status_code = 200
    rsp.raise_for_status.return_value = None

    return add_reference_response_to_mock(rsp, args[0])


def add_reference_response_to_mock(mock: Mock, url: str) -> Mock:
    if "provenancestatement" in url:
        mock.json.return_value = json.load(
            open("./tests/json_data/provenancestatement.json")
        )
    elif "rightsstatement" in url:
        mock.json.return_value = json.load(
            open("./tests/json_data/rightsstatement.json")
        )
    elif "frequency" in url:
        mock.json.return_value = json.load(open("./tests/json_data/frequency.json"))
    elif "linguisticsystem" in url:
        mock.json.return_value = json.load(
            open("./tests/json_data/linguisticsystem.json")
        )
    elif "referencetypes" in url:
        mock.json.return_value = json.load(
            open("./tests/json_data/referencetypes.json")
        )
    elif "openlicenses" in url:
        mock.json.return_value = json.load(open("./tests/json_data/openlicenses.json"))
    elif "location" in url:
        mock.json.return_value = json.load(open("./tests/json_data/location.json"))
    elif "los/themes-and-words" in url:
        mock.json.return_value = json.load(open("./tests/json_data/los.json"))
    elif "eu/data-themes" in url:
        mock.json.return_value = json.load(open("./tests/json_data/eudatatheme.json"))
    elif "iana/media-types" in url:
        mock.json.return_value = json.load(open("./tests/json_data/mediatypes.json"))

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
def mock_reference_data_client_parse_error(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = json.JSONDecodeError(msg="reference-parse-error", doc="", pos=0)
    return mock


def organizations_and_reference_effect(*args: Any, **kwargs: Any) -> Mock:
    rsp = Mock(spec=requests.Response)
    rsp.status_code = 200
    rsp.raise_for_status.return_value = None
    rsp.text = org_response_0
    return add_reference_response_to_mock(rsp, args[0])


@pytest.fixture
def mock_organizations_and_reference_data(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = organizations_and_reference_effect
    return mock
