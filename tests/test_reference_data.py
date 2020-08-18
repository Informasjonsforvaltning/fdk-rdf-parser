from unittest.mock import Mock

from fdk_rdf_parser.reference_data import (
    DataServiceReferenceData,
    DatasetReferenceData,
    getDataServiceReferenceData,
    getDatasetReferenceData,
)
from .testdata import data_service_reference_data, dataset_reference_data


def test_get_data_service_reference_data(mock_reference_data_client: Mock) -> None:

    expected = data_service_reference_data

    actual = getDataServiceReferenceData()

    assert actual == expected


def test_get_dataset_reference_data(mock_reference_data_client: Mock) -> None:

    expected = dataset_reference_data

    actual = getDatasetReferenceData()

    assert actual == expected


def test_get_reference_data_http_error(
    mock_reference_data_client_http_error: Mock,
) -> None:

    expected_dataset = DatasetReferenceData()
    expected_data_service = DataServiceReferenceData()

    assert getDatasetReferenceData() == expected_dataset
    assert getDataServiceReferenceData() == expected_data_service


def test_get_reference_data_parse_error(
    mock_reference_data_client_parse_error: Mock,
) -> None:

    expected_dataset = DatasetReferenceData()
    expected_data_service = DataServiceReferenceData()

    assert getDatasetReferenceData() == expected_dataset
    assert getDataServiceReferenceData() == expected_data_service
