from unittest.mock import Mock

from fdk_rdf_parser import parse_public_services
from fdk_rdf_parser.classes import (
    Agent,
    HarvestMetaData,
    Organization,
    Participation,
    PublicService,
    ReferenceDataCode,
)


def test_multiple_participations_one_agent(
    mock_reference_data_client: Mock,
) -> None:
    src = """
            @prefix rov:   <http://www.w3.org/ns/regorg#> .
            @prefix cpsv:  <http://purl.org/vocab/cpsv#> .
            @prefix dct:   <http://purl.org/dc/terms/> .
            @prefix cv:    <http://data.europa.eu/m8g/> .
            @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
            @prefix dcat:  <http://www.w3.org/ns/dcat#> .
            @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
                    a cpsv:PublicService ;
                    dct:identifier "1" ;
                    cv:hasParticipation <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> ,
                                        <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1>
                    a               cv:Participation ;
                    cv:role         <https://data.norge.no/vocabulary/role-type#data-consumer> ;
                    dct:description "Statistisk sentralbyrås Virksomhets- og foretaksregister"@nb ;
                    dct:identifier  "1" ;
                    cv:hasParticipant <https://data.brreg.no/enhetsregisteret/api/enheter/971526920> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2>
                    a                cv:Participation ;
                    cv:role          <https://data.norge.no/concepts/15> ;
                    dct:description  "Mattilsynet"@nb ;
                    dct:identifier   "2" ;
                    cv:hasParticipant <https://data.brreg.no/enhetsregisteret/api/enheter/971526920> .

            <https://data.brreg.no/enhetsregisteret/api/enheter/971526920>
                    a foaf:Agent ;
                    dct:identifier "971526920" ;
                    dct:title "Statistisk sentralbyrå"@nb ;
                    cv:participates <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> ,
                                    <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2> .

            <http://localhost:5000/services/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .
            """

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            hasParticipation=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2",
            ],
            harvest=HarvestMetaData(),
            participatingAgents=[
                Agent(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                    identifier="971526920",
                    name={"nb": "Statistisk sentralbyrå"},
                    playsRole=[
                        Participation(
                            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                            identifier="1",
                            description={
                                "nb": "Statistisk sentralbyrås Virksomhets- og foretaksregister"
                            },
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
                            agent="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                        ),
                        Participation(
                            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2",
                            identifier="2",
                            description={"nb": "Mattilsynet"},
                            role=[
                                ReferenceDataCode(
                                    uri="https://data.norge.no/concepts/15",
                                )
                            ],
                            agent="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                        ),
                    ],
                )
            ],
            type="publicservices",
        )
    }

    assert parse_public_services(src) == expected


def test_participation_with_agent_and_organization(
    mock_reference_data_client: Mock,
) -> None:
    src = """
            @prefix rov:   <http://www.w3.org/ns/regorg#> .
            @prefix cpsv:  <http://purl.org/vocab/cpsv#> .
            @prefix dct:   <http://purl.org/dc/terms/> .
            @prefix cv:    <http://data.europa.eu/m8g/> .
            @prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
            @prefix dcat:  <http://www.w3.org/ns/dcat#> .
            @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
            @prefix rov:   <http://www.w3.org/ns/regorg#> .
            @prefix org:   <http://www.w3.org/ns/org#> .
            @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
            @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
            @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
                    a cpsv:PublicService ;
                    dct:identifier "1" ;
                    cv:hasParticipation <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> ,
                                        <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2> ,
                                        <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/3> ,
                                        <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/4> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1>
                    a               cv:Participation ;
                    cv:role         <https://data.norge.no/vocabulary/role-type#data-consumer> ;
                    dct:description "Statistisk sentralbyrås Virksomhets- og foretaksregister"@nb ;
                    dct:identifier  "1" ;
                    cv:hasParticipant <https://data.brreg.no/enhetsregisteret/api/enheter/971526920> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2>
                    a                cv:Participation ;
                    cv:role          <https://data.norge.no/concepts/15> ;
                    dct:description  "Mattilsynet"@nb ;
                    dct:identifier   "2" ;
                    cv:hasParticipant <https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/3>
                    a                cv:Participation ;
                    cv:role          <https://data.norge.no/concepts/15> ;
                    dct:description  "Deltagelse med Digitaliseringsdirektoratet"@nb ;
                    dct:identifier   "3" ;
                    cv:hasParticipant <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/4>
                    a                cv:Participation ;
                    cv:role          <https://data.norge.no/vocabulary/role-type#data-consumer> ;
                    dct:description  "Deltagelse med Offentlig Organisasjon"@nb ;
                    dct:identifier   "4" ;
                    cv:hasParticipant <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321> .

            <https://data.brreg.no/enhetsregisteret/api/enheter/971526920>
                    a foaf:Agent ;
                    dct:identifier "971526920" ;
                    dct:title "Statistisk sentralbyrå"@nb ;
                    cv:participates <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> ; .

            <https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced>
                    a              org:Organization;
                    dct:identifier "https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced"^^xsd:anyURI ;
                    dct:title      "Organisasjon i Brønnøysund"@nb ;
                    cv:participates <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2> .

            <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789>
                    a                      rov:RegisteredOrganization ;
                    dct:identifier         "123456789" ;
                    rov:legalName          "Digitaliseringsdirektoratet"@nb ;
                    br:orgPath             "/STAT/987654321/123456789" ;
                    cv:participates <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/3> .

            <https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321>
                    a              cv:PublicOrganisation;
                    dct:identifier "https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321"^^xsd:anyURI ;
                    dct:title      "En offentlig organisasjon"@nb ;
                    cv:participates <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/4> .

            <http://localhost:5000/services/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .
            """

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            hasParticipation=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2",
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/3",
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/4",
            ],
            harvest=HarvestMetaData(),
            participatingAgents=[
                Agent(
                    uri="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                    identifier="971526920",
                    name={"nb": "Statistisk sentralbyrå"},
                    playsRole=[
                        Participation(
                            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1",
                            identifier="1",
                            description={
                                "nb": "Statistisk sentralbyrås Virksomhets- og foretaksregister"
                            },
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
                            agent="https://data.brreg.no/enhetsregisteret/api/enheter/971526920",
                        ),
                    ],
                ),
                Organization(
                    uri="https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced",
                    identifier="https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced",
                    name={"nb": "Organisasjon i Brønnøysund"},
                    playsRole=[
                        Participation(
                            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/2",
                            identifier="2",
                            description={"nb": "Mattilsynet"},
                            role=[
                                ReferenceDataCode(
                                    uri="https://data.norge.no/concepts/15",
                                )
                            ],
                            agent="https://www.staging.fellesdatakatalog.digdir.no/organizations/exOrganisasjonReduced",
                        )
                    ],
                ),
                Organization(
                    uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                    identifier="123456789",
                    name={"nb": "Digitaliseringsdirektoratet"},
                    orgPath="/STAT/987654321/123456789",
                    playsRole=[
                        Participation(
                            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/3",
                            identifier="3",
                            description={
                                "nb": "Deltagelse med Digitaliseringsdirektoratet"
                            },
                            role=[
                                ReferenceDataCode(
                                    uri="https://data.norge.no/concepts/15",
                                )
                            ],
                            agent="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/123456789",
                        )
                    ],
                ),
                Organization(
                    uri="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321",
                    identifier="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321",
                    name={"nb": "En offentlig organisasjon"},
                    playsRole=[
                        Participation(
                            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/participation/4",
                            identifier="4",
                            description={"nb": "Deltagelse med Offentlig Organisasjon"},
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
                            agent="https://organization-catalog.fellesdatakatalog.digdir.no/organizations/987654321",
                        )
                    ],
                ),
            ],
            type="publicservices",
        )
    }

    assert parse_public_services(src) == expected


def test_invalid_agent_in_participation(
    mock_reference_data_client: Mock,
) -> None:
    src = """
            @prefix cpsv:  <http://purl.org/vocab/cpsv#> .
            @prefix dct:   <http://purl.org/dc/terms/> .
            @prefix cv:    <http://data.europa.eu/m8g/> .
            @prefix dcat:  <http://www.w3.org/ns/dcat#> .
            @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1>
                    a cpsv:PublicService ;
                    dct:identifier "1" ;
                    cv:hasParticipation <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> .

            <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1>
                    a               cv:Participation ;
                    dct:description "Statistisk sentralbyrås Virksomhets- og foretaksregister"@nb ;
                    dct:identifier  "1" ;
                    cv:hasParticipant <https://data.brreg.no/enhetsregisteret/api/enheter/971526920> .

            <https://data.brreg.no/enhetsregisteret/api/enheter/971526920>
                    a foaf:invalidAgentType ;
                    dct:identifier "1" ;
                    dct:title "Invalid Agent"@nb ;
                    cv:participates <http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1> .

            <http://localhost:5000/services/fdk-1>
                    a                  dcat:CatalogRecord ;
                    dct:identifier     "fdk-1" ;
                    foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .
            """

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            hasParticipation=[
                "http://public-service-publisher.fellesdatakatalog.digdir.no/participation/1"
            ],
            harvest=HarvestMetaData(),
            participatingAgents=None,
            type="publicservices",
        )
    }

    assert parse_public_services(src) == expected
