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


@pytest.fixture
def mock_organizations_error(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.side_effect = requests.HTTPError(
        "https://organizations.fellestestkatalog.no/organizations/123456789",
        404,
        "Not Found",
        {},
        None,
    )
    return mock
