from unittest.mock import Mock
from urllib import error

import pytest
from pytest_mock import MockFixture

from .testdata import org_response_0


@pytest.fixture
def mock_organizations_client(mocker: MockFixture) -> Mock:
    mock = mocker.patch("urllib.request.urlopen")
    mock.return_value.__enter__.return_value.read.return_value = org_response_0
    return mock


@pytest.fixture
def mock_organizations_error(mocker: MockFixture) -> Mock:
    mock = mocker.patch("urllib.request.urlopen")
    mock.side_effect = error.HTTPError(
        "https://organizations.fellestestkatalog.no/organizations/123456789",
        404,
        "Not Found",
        {},
        None,
    )
    return mock
