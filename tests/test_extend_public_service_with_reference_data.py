from fdk_rdf_parser.classes import (
    Organization,
    PublicService,
    ReferenceDataCode,
    Service,
)
from fdk_rdf_parser.reference_data import extend_cpsvno_service_with_reference_data
from .testdata import public_service_reference_data


def test_extend_media_types() -> None:
    parsed_public_service = PublicService(
        language=[
            ReferenceDataCode(
                uri="http://publications.europa.eu/resource/authority/language/NOB"
            ),
        ],
    )

    expected = PublicService(
        language=[
            ReferenceDataCode(
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
        extend_cpsvno_service_with_reference_data(
            parsed_public_service, public_service_reference_data
        )
        == expected
    )


def test_extend_owned_by_organization_types() -> None:
    parsed_service = Service(
        ownedBy=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                orgType=ReferenceDataCode(
                    uri="http://purl.org/adms/publishertype/IndustryConsortium"
                ),
            )
        ]
    )

    expected = Service(
        ownedBy=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                orgType=ReferenceDataCode(
                    uri="http://purl.org/adms/publishertype/IndustryConsortium",
                    code="IndustryConsortium",
                    prefLabel={
                        "nn": "Industrikonsortium",
                        "nb": "Industrikonsortium",
                        "en": "Industry consortium",
                    },
                ),
            ),
        ]
    )

    assert (
        extend_cpsvno_service_with_reference_data(
            parsed_service, public_service_reference_data
        )
        == expected
    )


def test_extend_competent_authority_organization_types() -> None:
    parsed_public_service = PublicService(
        hasCompetentAuthority=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                orgType=ReferenceDataCode(
                    uri="http://purl.org/adms/publishertype/NationalAuthority",
                ),
            )
        ]
    )

    expected = PublicService(
        hasCompetentAuthority=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                orgType=ReferenceDataCode(
                    uri="http://purl.org/adms/publishertype/NationalAuthority",
                    code="NationalAuthority",
                    prefLabel={
                        "nn": "Nasjonal myndigheit",
                        "nb": "Nasjonal myndighet",
                        "en": "National authority",
                    },
                ),
            )
        ]
    )

    assert (
        extend_cpsvno_service_with_reference_data(
            parsed_public_service, public_service_reference_data
        )
        == expected
    )
