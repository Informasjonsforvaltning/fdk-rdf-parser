from fdk_rdf_parser.classes import DataService, SkosCode
from fdk_rdf_parser.reference_data import (
    DataServiceReferenceData,
    extendDataServiceWithReferenceData,
)
from .testdata import data_service_reference_data


def test_handles_missing_references() -> None:
    parsed_data_service = DataService(
        mediaType=[SkosCode(uri="http://example.com/media-type/text/csv")],
    )

    assert (
        extendDataServiceWithReferenceData(
            parsed_data_service, DataServiceReferenceData()
        )
        == DataService()
    )


def test_handles_empty_media_type() -> None:
    parsed_data_service = DataService(mediaType=[SkosCode()],)

    assert (
        extendDataServiceWithReferenceData(
            parsed_data_service, data_service_reference_data
        )
        == DataService()
    )


def test_extend_media_types() -> None:
    parsed_data_service = DataService(
        mediaType=[
            SkosCode(uri="http://example.com/media-type/text/csv"),
            SkosCode(uri="http://example.com/media-type/not/found"),
        ],
    )

    expected = DataService(
        mediaType=[SkosCode(uri=None, code="text/csv", prefLabel={"nb": "CSV"})]
    )

    assert (
        extendDataServiceWithReferenceData(
            parsed_data_service, data_service_reference_data
        )
        == expected
    )
