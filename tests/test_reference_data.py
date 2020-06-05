from unittest.mock import Mock

from fdk_rdf_parser.reference_data import getAllReferenceData, ReferenceData
from .testdata import reference_data


def test_get_all_reference_data(mock_reference_data_client: Mock) -> None:

    expected = reference_data

    actual = getAllReferenceData()

    assert actual == expected


def test_get_all_reference_data_http_error(
    mock_reference_data_client_http_error: Mock,
) -> None:

    expected = ReferenceData()

    assert getAllReferenceData() == expected


def test_get_all_reference_data_parse_error(
    mock_reference_data_client_parse_error: Mock,
) -> None:

    expected = ReferenceData()

    assert getAllReferenceData() == expected
