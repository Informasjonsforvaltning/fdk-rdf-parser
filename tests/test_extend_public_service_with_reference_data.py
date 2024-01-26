from fdk_rdf_parser.classes import (
    PublicService,
    ReferenceDataCode,
)
from fdk_rdf_parser.reference_data import extend_cpsvno_service_with_reference_data
from .testdata import public_service_reference_data


def test_extend_type() -> None:
    parsed_public_service = PublicService(
        dctType=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/main-activity/defence",
            ),
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/main-activity/non-existing",
            ),
        ]
    )

    expected = PublicService(
        dctType=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/main-activity/defence",
                code="defence",
                prefLabel={"en": "Defence"},
            ),
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/main-activity/non-existing",
            ),
        ]
    )

    assert (
        extend_cpsvno_service_with_reference_data(
            parsed_public_service, public_service_reference_data
        )
        == expected
    )
