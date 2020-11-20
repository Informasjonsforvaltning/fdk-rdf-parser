from unittest.mock import Mock

from fdk_rdf_parser import parse_public_services
from fdk_rdf_parser.classes import HarvestMetaData, PublicService, Publisher


def test_parse_multiple_public_services(
    mock_organizations_and_reference_data: Mock,
) -> None:
    src = """
        @prefix cpsv: <http://purl.org/vocab/cpsv#> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix cv: <http://data.europa.eu/m8g/> .
        @prefix dcat:  <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> a cpsv:PublicService ;
                dct:identifier "1" ;
                dct:title "Ei offentleg teneste"@nb ;
                dct:description "Ei offentleg teneste som tener som døme til bruk i utvikling"@nn ;
                cv:hasCompetentAuthority <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/123456789> .

        <http://localhost:5000/services/fdk-1>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-1" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/1> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> a cpsv:PublicService ;
                dct:identifier "2" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ;
                cv:hasCompetentAuthority <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/991825827> .

        <http://localhost:5000/services/fdk-2>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-2" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/2> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> a cpsv:PublicService ;
                dct:identifier "3" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ; .

        <http://localhost:5000/services/fdk-3>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-3" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                foaf:primaryTopic  <http://public-service-publisher.fellesdatakatalog.digdir.no/services/3> .

        <http://public-service-publisher.fellesdatakatalog.digdir.no/services/4> a cpsv:PublicService ;
                dct:identifier "4" ;
                dct:title "Ei anna offentleg teneste"@nn ;
                dct:description "Ei anna offentleg teneste som tener som døme til bruk i utvikling"@nb ; .

        <http://localhost:5000/services/fdk-4>
                a                  dcat:CatalogRecord ;
                dct:identifier     "fdk-4" ;
                dct:issued         "2020-10-05T13:15:39.831Z"^^xsd:dateTime ;
                dct:modified       "2020-10-05T13:15:39.831Z"^^xsd:dateTime ."""

    expected = {
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/1": PublicService(
            id="fdk-1",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/1",
            identifier="1",
            title={"nb": "Ei offentleg teneste"},
            description={
                "nn": "Ei offentleg teneste som tener som døme til bruk i utvikling"
            },
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
                    id="123456789",
                    name="Digitaliseringsdirektoratet",
                    orgPath="/STAT/987654321/123456789",
                    prefLabel={
                        "en": "Norwegian Digitalisation Agency",
                        "nn": "Digitaliseringsdirektoratet",
                        "nb": "Digitaliseringsdirektoratet",
                    },
                    organisasjonsform="ORGL",
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/2": PublicService(
            id="fdk-2",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/2",
            identifier="2",
            title={"nn": "Ei anna offentleg teneste"},
            description={
                "nb": "Ei anna offentleg teneste som tener som døme til bruk i utvikling"
            },
            hasCompetentAuthority=[
                Publisher(
                    uri="https://organizations.fellesdatakatalog.digdir.no/organizations/991825827",
                    id=None,
                    name=None,
                    orgPath=None,
                    prefLabel=None,
                    organisasjonsform=None,
                )
            ],
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
        "http://public-service-publisher.fellesdatakatalog.digdir.no/services/3": PublicService(
            id="fdk-3",
            uri="http://public-service-publisher.fellesdatakatalog.digdir.no/services/3",
            identifier="3",
            title={"nn": "Ei anna offentleg teneste"},
            description={
                "nb": "Ei anna offentleg teneste som tener som døme til bruk i utvikling"
            },
            hasCompetentAuthority=None,
            harvest=HarvestMetaData(
                firstHarvested="2020-10-05T13:15:39Z", changed=["2020-10-05T13:15:39Z"]
            ),
            type="publicservices",
        ),
    }

    assert parse_public_services(src) == expected
