from fdk_rdf_parser.classes import DataService, FDKFormatType, MediaType, SkosCode
from fdk_rdf_parser.reference_data import (
    DataServiceReferenceData,
    extend_data_service_with_reference_data,
)
from .testdata import data_service_reference_data


def test_handles_missing_references() -> None:
    parsed_data_service = DataService(
        mediaType=[SkosCode(uri="http://example.com/media-type/text/csv")],
        fdkFormat=[MediaType(code="http://example.com/media-type/text/csv")],
    )

    assert (
        extend_data_service_with_reference_data(
            parsed_data_service, DataServiceReferenceData()
        )
        == DataService()
    )


def test_handles_empty_media_type() -> None:
    parsed_data_service = DataService(
        mediaType=[SkosCode()],
        fdkFormat=[MediaType()],
    )

    assert (
        extend_data_service_with_reference_data(
            parsed_data_service, data_service_reference_data
        )
        == parsed_data_service
    )


def test_extend_media_types() -> None:
    parsed_data_service = DataService(
        mediaType=[
            SkosCode(uri="https://www.iana.org/assignments/media-types/text/csv"),
            SkosCode(
                uri="http://publications.europa.eu/resource/authority/file-type/XML"
            ),
            SkosCode(uri="http://example.com/media-type/not/found"),
        ],
        fdkFormat=[
            MediaType(uri="https://www.iana.org/assignments/media-types/text/csv"),
            MediaType(
                uri="http://publications.europa.eu/resource/authority/file-type/XML"
            ),
            MediaType(uri="http://example.com/media-type/not/found"),
            MediaType(code="some-type"),
        ],
    )

    expected = DataService(
        mediaType=[
            SkosCode(
                uri="https://www.iana.org/assignments/media-types/text/csv",
                code="text/csv",
                prefLabel={"nb": "text/csv"},
            ),
            SkosCode(
                uri="http://publications.europa.eu/resource/authority/file-type/XML",
                code="XML",
                prefLabel={"nb": "XML"},
            ),
        ],
        fdkFormat=[
            MediaType(
                uri="https://www.iana.org/assignments/media-types/text/csv",
                fdkType=FDKFormatType.MEDIA_TYPE,
                code="text/csv",
            ),
            MediaType(
                uri="http://publications.europa.eu/resource/authority/file-type/XML",
                fdkType=FDKFormatType.FILE_TYPE,
                code="XML",
            ),
            MediaType(
                code="some-type",
                fdkType=FDKFormatType.UNKNOWN,
            ),
        ],
    )

    assert (
        extend_data_service_with_reference_data(
            parsed_data_service, data_service_reference_data
        )
        == expected
    )
