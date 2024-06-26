from dataclasses import asdict
from unittest.mock import Mock

from fdk_rdf_parser.classes import (
    Catalog,
    DataService,
    DCATContactPoint,
    HarvestMetaData,
    MediaTypeOrExtent,
    MediaTypeOrExtentType,
    Publisher,
    SkosConcept,
)
from fdk_rdf_parser.fdk_rdf_parser import (
    parse_data_service,
    parse_data_services,
    parse_dataservice_as_dict,
)


def test_parse_multiple_data_services(
    mock_reference_data_client: Mock,
) -> None:
    expected = {
        "https://testutgiver.no/data-services/2": DataService(
            publisher=Publisher(
                uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                id="123456789",
                name="Digitaliseringsdirektoratet",
                orgPath="/STAT/987654321/123456789",
                prefLabel={
                    "nb": "Digitaliseringsdirektoratet",
                    "nn": "Digitaliseringsdirektoratet",
                    "en": "Norwegian Digitalisation Agency",
                },
                organisasjonsform="ORGL",
            ),
            title={
                "nb": "Kaffe API",
                "en": "Kaffe API Nynorsk ENGELSK",
                "nn": "Kaffe API Nynorsk",
            },
            description={
                "nn": "Beskrivelse for å benytte seg av en kaffemaskin NYNORSK",
                "nb": "Beskrivelse for å benytte seg av en kaffemaskin",
                "en": "Beskrivelse for å benytte seg av en kaffemaskin ENGELSK",
            },
            descriptionFormatted={
                "nn": "Beskrivelse for å benytte seg av en kaffemaskin NYNORSK",
                "nb": "Beskrivelse for å benytte seg av en kaffemaskin",
                "en": "Beskrivelse for å benytte seg av en kaffemaskin ENGELSK",
            },
            uri="https://testutgiver.no/data-services/2",
            contactPoint=[
                DCATContactPoint(
                    fullname="Contact information",
                    email="kaffe@epost.no",
                    organizationName={"nb": "Kaffehuset"},
                    hasURL="http://www.kaffehuset.no",
                )
            ],
            id="2",
            harvest=HarvestMetaData(
                firstHarvested="2020-08-07T09:56:01Z", modified="2020-08-07T10:02:26Z"
            ),
            endpointDescription={
                "http://example.com/Dette%20er%20en%20test",
                "http://example.com/dette%20skal%20v%C3%A6re%20en%20lenke",
            },
            endpointURL={"http://kaffe.no", "https://kaffemaskin.no"},
            fdkFormat=[
                MediaTypeOrExtent(
                    uri="https://www.iana.org/assignments/media-types/text/turtle",
                    name="turtle",
                    code="text/turtle",
                    type=MediaTypeOrExtentType.MEDIA_TYPE,
                ),
            ],
            servesDataset={"http://testutgiver.no/datasets/abc"},
            conformsTo=[
                SkosConcept(
                    uri="https://data.norge.no/def/serviceType#CUSTOMER_RELATIONS"
                )
            ],
            page=["https://data4.norge.no"],
            catalog=Catalog(
                id="d07885d9-0925-339f-bb22-58c28dc30409",
                uri="https://testutgiver.no/catalogs/123456789",
                title={"en": "Data service catalog"},
                publisher=Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "nb": "Digitaliseringsdirektoratet",
                        "nn": "Digitaliseringsdirektoratet",
                        "en": "Norwegian Digitalisation Agency",
                    },
                    organisasjonsform="ORGL",
                ),
            ),
        ),
        "https://testutgiver.no/dataservices/0": DataService(
            publisher=Publisher(
                uri="https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321",
            ),
            uri="https://testutgiver.no/dataservices/0",
            id="d1d698ef-267a-3d57-949f-b2bc44657f3e",
            harvest=HarvestMetaData(
                firstHarvested="2020-06-22T13:39:27Z", modified="2020-06-22T13:39:27Z"
            ),
            endpointDescription={
                "https://raw.githubusercontent.com/Informasjonsforvaltning/fdk-api-harvester/master/src/main/resources/specification/fdk-api-harvester.yaml"
            },
            catalog=Catalog(
                id="d6199127-8835-33e1-9108-233cd81e92f9",
                uri="https://testutgiver.no/catalogs/987654321",
                title={"nb": "Dataservicekatalog2 for Digitaliseringsdirektoratet"},
                publisher=Publisher(
                    uri="https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321",
                ),
            ),
        ),
        "https://testutgiver.no/dataservices/1": DataService(
            publisher=Publisher(
                uri="https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321",
            ),
            title={"nb": "Testing Testing"},
            uri="https://testutgiver.no/dataservices/1",
            contactPoint=[
                DCATContactPoint(
                    fullname="Contact information",
                )
            ],
            id="1",
            harvest=HarvestMetaData(
                firstHarvested="2020-06-22T13:39:27Z", modified="2020-06-22T13:39:27Z"
            ),
            endpointDescription={"http://example.com/"},
            endpointURL={"https://vg.no"},
            fdkFormat=[
                MediaTypeOrExtent(
                    uri="https://www.iana.org/assignments/media-types/application/not.found"
                )
            ],
            catalog=Catalog(
                id="d6199127-8835-33e1-9108-233cd81e92f9",
                uri="https://testutgiver.no/catalogs/987654321",
                title={"nb": "Dataservicekatalog2 for Digitaliseringsdirektoratet"},
                publisher=Publisher(
                    uri="https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321",
                ),
            ),
        ),
    }

    with open("tests/test_data/dataservice0.ttl", "r") as src:
        assert parse_data_services(src.read()) == expected


def test_parse_single_data_service(
    mock_reference_data_client: Mock,
) -> None:
    graph = """
        @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix dct:   <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix rov:   <http://www.w3.org/ns/regorg#> .

        <https://testutgiver.no/dataservices/0>
                a                         dcat:DataService ;
                dct:publisher             <https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321> ;
                dcat:endpointDescription  <https://raw.githubusercontent.com/Informasjonsforvaltning/fdk-api-harvester/master/src/main/resources/specification/fdk-api-harvester.yaml> .

        <https://testutgiver.no/catalogs/987654321>
                a              dcat:Catalog ;
                dct:publisher  <https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321> ;
                dct:title      "Dataservicekatalog2 for Digitaliseringsdirektoratet"@nb ;
                dcat:service   <https://testutgiver.no/dataservices/0> .

        <https://testdirektoratet.no/catalogs/321>
                a                  dcat:CatalogRecord ;
                dct:identifier     "d6199127-8835-33e1-9108-233cd81e92f9" ;
                dct:issued         "2020-06-22T13:39:27.334Z"^^xsd:dateTime ;
                dct:modified       "2020-06-22T13:39:27.334Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testutgiver.no/catalogs/987654321> .

        <https://testdirektoratet.no/dataservices/000>
                a                  dcat:CatalogRecord ;
                dct:identifier     "d1d698ef-267a-3d57-949f-b2bc44657f3e" ;
                dct:isPartOf       <https://testdirektoratet.no/catalogs/321> ;
                dct:issued         "2020-06-22T13:39:27.353Z"^^xsd:dateTime ;
                dct:modified       "2020-06-22T13:39:27.353Z"^^xsd:dateTime ;
                foaf:primaryTopic  <https://testutgiver.no/dataservices/0> .
    """
    expected = DataService(
        publisher=Publisher(
            uri="https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321",
        ),
        uri="https://testutgiver.no/dataservices/0",
        id="d1d698ef-267a-3d57-949f-b2bc44657f3e",
        harvest=HarvestMetaData(
            firstHarvested="2020-06-22T13:39:27Z", modified="2020-06-22T13:39:27Z"
        ),
        endpointDescription={
            "https://raw.githubusercontent.com/Informasjonsforvaltning/fdk-api-harvester/master/src/main/resources/specification/fdk-api-harvester.yaml"
        },
        catalog=Catalog(
            id="d6199127-8835-33e1-9108-233cd81e92f9",
            uri="https://testutgiver.no/catalogs/987654321",
            title={"nb": "Dataservicekatalog2 for Digitaliseringsdirektoratet"},
            publisher=Publisher(
                uri="https://organization-catalog.fellesdatakatalog.brreg.no/organizations/987654321",
            ),
        ),
    )

    assert parse_data_service(graph) == expected
    assert parse_dataservice_as_dict(graph) == asdict(expected)
