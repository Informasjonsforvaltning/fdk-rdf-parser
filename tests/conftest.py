from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture

from .testdata import org_response


@pytest.fixture
def mock_organizations_client(mocker: MockFixture) -> Mock:
    mock = mocker.patch("urllib.request.urlopen")
    mock.return_value.__enter__.return_value.read.return_value = org_response
    return mock
