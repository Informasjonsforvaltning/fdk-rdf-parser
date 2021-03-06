from fdk_rdf_parser.classes import PublicService, SkosCode
from fdk_rdf_parser.reference_data import extend_public_service_with_reference_data
from .testdata import public_service_reference_data


def test_extend_media_types() -> None:
    parsed_public_service = PublicService(
        language=[
            SkosCode(
                uri="http://publications.europa.eu/resource/authority/language/NOB"
            ),
        ],
    )

    expected = PublicService(
        language=[
            SkosCode(
                uri="http://publications.europa.eu/resource/authority/language/NOB",
                code="NOB",
                prefLabel={
                    "en": "Norwegian Bokmål",
                    "nb": "Norsk Bokmål",
                    "nn": "Norsk Bokmål",
                    "no": "Norsk Bokmål",
                },
            ),
        ]
    )

    assert (
        extend_public_service_with_reference_data(
            parsed_public_service, public_service_reference_data
        )
        == expected
    )
