from unittest.mock import Mock

from fdk_rdf_parser import parse_data_services
from fdk_rdf_parser.classes import (
    Catalog,
    ContactPoint,
    DataService,
    HarvestMetaData,
    Publisher,
    SkosCode,
    SkosConcept,
)


def test_parse_multiple_data_services(
    mock_organizations_and_reference_data: Mock,
) -> None:

    src = """
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

<https://testdirektoratet.no/catalogs/321>
        a                  dcat:CatalogRecord ;
        dct:identifier     "d6199127-8835-33e1-9108-233cd81e92f9" ;
        dct:issued         "2020-06-22T13:39:27.334Z"^^xsd:dateTime ;
        dct:modified       "2020-06-22T13:39:27.334Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://testutgiver.no/catalogs/987654321> .

<https://testdirektoratet.no/catalogs/123>
        a                  dcat:CatalogRecord ;
        dct:identifier     "d07885d9-0925-339f-bb22-58c28dc30409" ;
        dct:issued         "2020-08-07T09:56:01.329Z"^^xsd:dateTime ;
        dct:modified       "2020-08-07T10:02:26.312Z"^^xsd:dateTime , "2020-08-07T09:56:01.329Z" ;
        foaf:primaryTopic  <https://testutgiver.no/catalogs/123456789> .

<https://testutgiver.no/catalogs/123456789>
        a               dcat:Catalog ;
        dct:publisher   [ a                 vcard:Kind , foaf:Agent ;
                          dct:identifier    "123456789"
                        ] ;
        dct:title      "Data service catalog"@en ;
        dcat:service   <https://testutgiver.no/data-services/2> .

<https://testutgiver.no/data-services/2>
        a                         dcat:DataService ;
        dct:conformsTo            <https://data.norge.no/def/serviceType#CUSTOMER_RELATIONS> ;
        dct:description           "Beskrivelse for å benytte seg av en kaffemaskin"@nb , "Beskrivelse for å benytte seg av en kaffemaskin NYNORSK"@nn , "Beskrivelse for å benytte seg av en kaffemaskin ENGELSK"@en ;
        dct:title                 "Kaffe API Nynorsk ENGELSK"@en , "Kaffe API Nynorsk"@nn , "Kaffe API"@nb ;
        dcat:contactPoint         [ a                          vcard:Organization ;
                                    vcard:fn                   "Contact information" ;
                                    vcard:hasEmail             <mailto:kaffe@epost.no> ;
                                    vcard:hasOrganizationName  "Kaffehuset"@nb ;
                                    vcard:hasURL               <http://www.kaffehuset.no>
                                  ] ;
        dcat:endpointDescription  <http://example.com/dette%20skal%20v%C3%A6re%20en%20lenke> , <http://example.com/Dette%20er%20en%20test> ;
        dcat:endpointURL          <http://kaffe.no> , <https://kaffemaskin.no> ;
        dcat:mediaType            <https://www.iana.org/assignments/media-types/text/turtle> , <https://www.iana.org/assignments/media-types/application/rdf+xml> , <https://www.iana.org/assignments/media-types/application/json> ;
        dcat:servesDataset        <http://testutgiver.no/datasets/abc> .

<https://testdirektoratet.no/dataservices/111>
        a                  dcat:CatalogRecord ;
        dct:identifier     "1" ;
        dct:isPartOf       <https://testdirektoratet.no/catalogs/321> ;
        dct:issued         "2020-06-22T13:39:27.353Z"^^xsd:dateTime ;
        dct:modified       "2020-06-22T13:39:27.353Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://testutgiver.no/dataservices/1> .

<https://testutgiver.no/dataservices/0>
        a                         dcat:DataService ;
        dcat:endpointDescription  <https://raw.githubusercontent.com/Informasjonsforvaltning/fdk-api-harvester/master/src/main/resources/specification/fdk-api-harvester.yaml> .

<https://testutgiver.no/catalogs/987654321>
        a              dcat:Catalog ;
        dct:publisher  <https://organization-catalogue.fellesdatakatalog.brreg.no/organizations/987654321> ;
        dct:title      "Dataservicekatalog2 for Digitaliseringsdirektoratet"@nb ;
        dcat:service   <https://testutgiver.no/dataservices/0> , <https://testutgiver.no/dataservices/1> .

<https://testdirektoratet.no/dataservices/222>
        a                  dcat:CatalogRecord ;
        dct:identifier     "2" ;
        dct:isPartOf       <https://testdirektoratet.no/catalogs/123> ;
        dct:issued         "2020-08-07T09:56:01.329Z"^^xsd:dateTime ;
        dct:modified       "2020-08-07T10:02:26.312Z"^^xsd:dateTime , "2020-08-07T09:56:01.329Z" ;
        foaf:primaryTopic  <https://testutgiver.no/data-services/2> .

<https://testutgiver.no/dataservices/1>
        a                         dcat:DataService ;
        dct:title                 "Testing Testing"@nb ;
        dcat:contactPoint         [ a         vcard:Organization ;
                                    vcard:fn  "Contact information"
                                  ] ;
        dcat:endpointDescription  <http://example.com/> ;
        dcat:endpointURL          <https://vg.no> ;
        dcat:mediaType            <https://www.iana.org/assignments/media-types/application/vnd.geo+json> , <https://www.iana.org/assignments/media-types/application/vnd.oasis.opendocument.spreadsheet> .

<https://testdirektoratet.no/dataservices/000>
        a                  dcat:CatalogRecord ;
        dct:identifier     "d1d698ef-267a-3d57-949f-b2bc44657f3e" ;
        dct:isPartOf       <https://testdirektoratet.no/catalogs/321> ;
        dct:issued         "2020-06-22T13:39:27.353Z"^^xsd:dateTime ;
        dct:modified       "2020-06-22T13:39:27.353Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://testutgiver.no/dataservices/0> ."""

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
                ContactPoint(
                    fullname="Contact information",
                    email="kaffe@epost.no",
                    organizationName="Kaffehuset",
                    hasURL="http://www.kaffehuset.no",
                )
            ],
            id="2",
            harvest=HarvestMetaData(
                firstHarvested="2020-08-07T09:56:01Z", changed=["2020-08-07T10:02:26Z"]
            ),
            endpointDescription=[
                "http://example.com/Dette%20er%20en%20test",
                "http://example.com/dette%20skal%20v%C3%A6re%20en%20lenke",
            ],
            endpointURL=["http://kaffe.no", "https://kaffemaskin.no"],
            mediaType=[
                SkosCode(uri=None, code="application/json", prefLabel={"nb": "JSON"}),
                SkosCode(
                    uri=None, code="application/rdf+xml", prefLabel={"nb": "RDF/XML"}
                ),
                SkosCode(uri=None, code="text/turtle", prefLabel={"nb": "Turtle"}),
            ],
            servesDataset=["http://testutgiver.no/datasets/abc"],
            conformsTo=[
                SkosConcept(
                    uri="https://data.norge.no/def/serviceType#CUSTOMER_RELATIONS"
                )
            ],
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
                uri="https://organization-catalogue.fellesdatakatalog.brreg.no/organizations/987654321",
            ),
            uri="https://testutgiver.no/dataservices/0",
            id="d1d698ef-267a-3d57-949f-b2bc44657f3e",
            harvest=HarvestMetaData(
                firstHarvested="2020-06-22T13:39:27Z", changed=["2020-06-22T13:39:27Z"]
            ),
            endpointDescription=[
                "https://raw.githubusercontent.com/Informasjonsforvaltning/fdk-api-harvester/master/src/main/resources/specification/fdk-api-harvester.yaml"
            ],
            catalog=Catalog(
                id="d6199127-8835-33e1-9108-233cd81e92f9",
                uri="https://testutgiver.no/catalogs/987654321",
                title={"nb": "Dataservicekatalog2 for Digitaliseringsdirektoratet"},
                publisher=Publisher(
                    uri="https://organization-catalogue.fellesdatakatalog.brreg.no/organizations/987654321",
                ),
            ),
        ),
        "https://testutgiver.no/dataservices/1": DataService(
            publisher=Publisher(
                uri="https://organization-catalogue.fellesdatakatalog.brreg.no/organizations/987654321",
            ),
            title={"nb": "Testing Testing"},
            uri="https://testutgiver.no/dataservices/1",
            contactPoint=[
                ContactPoint(
                    fullname="Contact information",
                )
            ],
            id="1",
            harvest=HarvestMetaData(
                firstHarvested="2020-06-22T13:39:27Z", changed=["2020-06-22T13:39:27Z"]
            ),
            endpointDescription=["http://example.com/"],
            endpointURL=["https://vg.no"],
            catalog=Catalog(
                id="d6199127-8835-33e1-9108-233cd81e92f9",
                uri="https://testutgiver.no/catalogs/987654321",
                title={"nb": "Dataservicekatalog2 for Digitaliseringsdirektoratet"},
                publisher=Publisher(
                    uri="https://organization-catalogue.fellesdatakatalog.brreg.no/organizations/987654321",
                ),
            ),
        ),
    }

    assert parse_data_services(src) == expected
