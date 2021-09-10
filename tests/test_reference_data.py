from unittest.mock import Mock

from fdk_rdf_parser.reference_data import (
    DataServiceReferenceData,
    DatasetReferenceData,
    get_data_service_reference_data,
    get_dataset_reference_data,
)
from fdk_rdf_parser.reference_data.utils import remove_scheme_and_trailing_slash
from .testdata import data_service_reference_data, dataset_reference_data


def test_get_data_service_reference_data(mock_reference_data_client: Mock) -> None:

    expected = data_service_reference_data

    actual = get_data_service_reference_data()

    assert actual == expected


def test_get_dataset_reference_data(mock_reference_data_client: Mock) -> None:

    expected = dataset_reference_data

    actual = get_dataset_reference_data()

    assert actual == expected


def test_get_reference_data_http_error(
    mock_reference_data_client_http_error: Mock,
) -> None:

    expected_dataset = DatasetReferenceData()
    expected_data_service = DataServiceReferenceData()

    assert get_dataset_reference_data() == expected_dataset
    assert get_data_service_reference_data() == expected_data_service


def test_get_reference_data_parse_error(
    mock_reference_data_client_parse_error: Mock,
) -> None:

    expected_dataset = DatasetReferenceData()
    expected_data_service = DataServiceReferenceData()

    assert get_dataset_reference_data() == expected_dataset
    assert get_data_service_reference_data() == expected_data_service


def test_remove_scheme_and_trailing_slash() -> None:

    assert remove_scheme_and_trailing_slash("http://my.uri/") == "my.uri"
    assert remove_scheme_and_trailing_slash("https://my.uri") == "my.uri"
    assert remove_scheme_and_trailing_slash("ftp://my.uri/") == "ftp://my.uri"
    assert remove_scheme_and_trailing_slash("my.uri/") == "my.uri"
    assert remove_scheme_and_trailing_slash(None) == ""
    assert remove_scheme_and_trailing_slash("") == ""
