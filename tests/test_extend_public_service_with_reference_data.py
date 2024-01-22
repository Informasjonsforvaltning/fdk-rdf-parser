from fdk_rdf_parser.classes import (
    Organization,
    Participation,
    PublicService,
    ReferenceDataCode,
    Service,
)
from fdk_rdf_parser.reference_data import extend_cpsvno_service_with_reference_data
from .testdata import public_service_reference_data


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


def test_extend_participation_with_role() -> None:
    parsed_public_service = PublicService(
        participatingAgents=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                playsRole=[
                    Participation(
                        uri="https://testdirektoratet.no/participations/1",
                        role=[
                            ReferenceDataCode(
                                uri="https://data.norge.no/vocabulary/role-type#data-consumer",
                            )
                        ],
                    )
                ],
            ),
        ]
    )

    expected = PublicService(
        participatingAgents=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                playsRole=[
                    Participation(
                        uri="https://testdirektoratet.no/participations/1",
                        role=[
                            ReferenceDataCode(
                                uri="https://data.norge.no/vocabulary/role-type#data-consumer",
                                code="data-consumer",
                                prefLabel={
                                    "nb": "datakonsument",
                                    "en": "data consumer",
                                },
                            ),
                        ],
                    )
                ],
            )
        ]
    )

    assert (
        extend_cpsvno_service_with_reference_data(
            parsed_public_service, public_service_reference_data
        )
        == expected
    )


def test_extend_agent_participations_with_missing_values() -> None:
    parsed_public_service = PublicService(
        participatingAgents=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
            ),
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/222333444",
                playsRole=[
                    Participation(
                        uri="https://testdirektoratet.no/participations/1",
                        role=None,
                    )
                ],
            ),
        ]
    )

    expected = PublicService(
        participatingAgents=[
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
            ),
            Organization(
                uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/222333444",
                playsRole=[
                    Participation(
                        uri="https://testdirektoratet.no/participations/1",
                        role=None,
                    )
                ],
            ),
        ]
    )

    assert (
        extend_cpsvno_service_with_reference_data(
            parsed_public_service, public_service_reference_data
        )
        == expected
    )


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
