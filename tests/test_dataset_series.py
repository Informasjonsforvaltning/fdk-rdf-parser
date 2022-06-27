from unittest.mock import Mock

from fdk_rdf_parser import parse_datasets
from fdk_rdf_parser.classes import (
    Catalog,
    Dataset,
    DatasetSeries,
    HarvestMetaData,
    Publisher,
    SkosCode,
)


def test_parse_dataset_series(mock_reference_data_client: Mock) -> None:

    src = """
        @prefix br:    <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/organization-catalog.owl#> .
        @prefix fdk:   <https://raw.githubusercontent.com/Informasjonsforvaltning/fdk-reasoning-service/main/src/main/resources/ontology/fdk.owl#> .
        @prefix orgtype:   <https://raw.githubusercontent.com/Informasjonsforvaltning/organization-catalog/main/src/main/resources/ontology/org-type.ttl#> .
        @prefix rov:   <http://www.w3.org/ns/regorg#> .
        @prefix ex: <http://example.org/> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix dcat: <http://www.w3.org/ns/dcat#> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

        ex:EUCatalog a dcat:Catalog ;
            dct:title "European Data Catalog"@en ;
            dct:publisher  <https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062> ;
            dcat:dataset ex:budget  ;
            .

        ex:budget a dcat:Dataset , dcat:DatasetSeries ;
            dct:title "Budget data"@en ;
            dct:provenance <http://data.brreg.no/datakatalog/provinens/nasjonal> ;
            fdk:isAuthoritative true ;
            dct:publisher  <https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062> ;
            dcat:first ex:budget-2018 ;
            dcat:last ex:budget-2020 ;
            .

        ex:budget-2018 a dcat:Dataset ;
            dct:title "Budget data for year 2018"@en ;
            dct:publisher  <https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062> ;
            dcat:inSeries ex:budget ;
            dct:issued "2019-01-01"^^xsd:date ;
            .

        ex:budget-2019 a dcat:Dataset ;
            dct:title "Budget data for year 2019"@en ;
            dct:publisher  <https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062> ;
            dcat:inSeries ex:budget ;
            dct:issued "2020-01-01"^^xsd:date ;
            dcat:prev ex:budget-2018 ;
            .

        ex:budget-2020 a dcat:Dataset ;
            dct:title "Budget data for year 2020"@en ;
            dct:publisher  <https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062> ;
            dcat:inSeries ex:budget ;
            dct:issued "2021-01-01"^^xsd:date ;
            dcat:prev ex:budget-2019 ;
            .

        <https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062>
            a                     rov:RegisteredOrganization ;
            dct:identifier        "910298062" ;
            rov:legalName         "KARMSUND OG KYSNESSTRAND REVISJON" ;
            foaf:name             "Karmsund og kysnesstrand revisjon"@nb ;
            rov:orgType           orgtype:ORGL ;
            br:orgPath            "/ANNET/910298062" .

        <http://localhost:5000/catalogs/df68b420-fb97-3770-9580-7518734632b1>
            a                  dcat:CatalogRecord ;
            dct:identifier     "df68b420-fb97-3770-9580-7518734632b1" ;
            dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            foaf:primaryTopic  ex:EUCatalog .

        <http://localhost:5000/datasets/f1e8443d-910f-3838-87e3-2b5e7ee307a6>
            a                  dcat:CatalogRecord ;
            dct:identifier     "f1e8443d-910f-3838-87e3-2b5e7ee307a6" ;
            dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:isPartOf       <http://localhost:5000/catalogs/df68b420-fb97-3770-9580-7518734632b1> ;
            foaf:primaryTopic  ex:budget-2020 .

        <http://localhost:5000/datasets/ca883493-7848-3116-8e1a-2b2e610a0fc1>
            a                  dcat:CatalogRecord ;
            dct:identifier     "ca883493-7848-3116-8e1a-2b2e610a0fc1" ;
            dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:isPartOf       <http://localhost:5000/catalogs/df68b420-fb97-3770-9580-7518734632b1> ;
            foaf:primaryTopic  ex:budget-2018 .

        <http://localhost:5000/datasets/51704c08-c174-393d-add5-348d3b304aeb>
            a                  dcat:CatalogRecord ;
            dct:identifier     "51704c08-c174-393d-add5-348d3b304aeb" ;
            dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:isPartOf       <http://localhost:5000/catalogs/df68b420-fb97-3770-9580-7518734632b1> ;
            foaf:primaryTopic  ex:budget-2019 .

        <http://localhost:5000/datasets/ad115f63-9edc-30dc-ab81-f6866e0631ea>
            a                  dcat:CatalogRecord ;
            dct:identifier     "ad115f63-9edc-30dc-ab81-f6866e0631ea" ;
            dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:isPartOf       <http://localhost:5000/catalogs/df68b420-fb97-3770-9580-7518734632b1> ;
            foaf:primaryTopic  ex:budget ."""

    expected = {
        "http://example.org/budget": DatasetSeries(
            publisher=Publisher(
                uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                id="910298062",
                name="KARMSUND OG KYSNESSTRAND REVISJON",
                orgPath="/ANNET/910298062",
                prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                organisasjonsform="ORGL",
            ),
            title={"en": "Budget data"},
            uri="http://example.org/budget",
            id="ad115f63-9edc-30dc-ab81-f6866e0631ea",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z", changed=["2020-03-12T11:52:16Z"]
            ),
            catalog=Catalog(
                id="df68b420-fb97-3770-9580-7518734632b1",
                publisher=Publisher(
                    uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                    id="910298062",
                    name="KARMSUND OG KYSNESSTRAND REVISJON",
                    orgPath="/ANNET/910298062",
                    prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                    organisasjonsform="ORGL",
                ),
                title={"en": "European Data Catalog"},
                uri="http://example.org/EUCatalog",
            ),
            provenance=SkosCode(
                uri="http://data.brreg.no/datakatalog/provinens/nasjonal",
                code="NASJONAL",
                prefLabel={
                    "en": "Authoritativ source",
                    "nb": "Autoritativ kilde",
                    "nn": "Autoritativ kilde",
                },
            ),
            isOpenData=False,
            isAuthoritative=True,
            isRelatedToTransportportal=False,
            inSeries=None,
            type="datasets",
            first="http://example.org/budget-2018",
            last="http://example.org/budget-2020",
            specialized_type="dataset_series",
        ),
        "http://example.org/budget-2018": Dataset(
            publisher=Publisher(
                uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                id="910298062",
                name="KARMSUND OG KYSNESSTRAND REVISJON",
                orgPath="/ANNET/910298062",
                prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                organisasjonsform="ORGL",
            ),
            title={"en": "Budget data for year 2018"},
            uri="http://example.org/budget-2018",
            issued="2019-01-01",
            id="ca883493-7848-3116-8e1a-2b2e610a0fc1",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z", changed=["2020-03-12T11:52:16Z"]
            ),
            catalog=Catalog(
                id="df68b420-fb97-3770-9580-7518734632b1",
                publisher=Publisher(
                    uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                    id="910298062",
                    name="KARMSUND OG KYSNESSTRAND REVISJON",
                    orgPath="/ANNET/910298062",
                    prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                    organisasjonsform="ORGL",
                ),
                title={"en": "European Data Catalog"},
                uri="http://example.org/EUCatalog",
            ),
            isOpenData=False,
            isAuthoritative=False,
            isRelatedToTransportportal=False,
            inSeries="http://example.org/budget",
            type="datasets",
        ),
        "http://example.org/budget-2019": Dataset(
            publisher=Publisher(
                uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                id="910298062",
                name="KARMSUND OG KYSNESSTRAND REVISJON",
                orgPath="/ANNET/910298062",
                prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                organisasjonsform="ORGL",
            ),
            title={"en": "Budget data for year 2019"},
            uri="http://example.org/budget-2019",
            issued="2020-01-01",
            id="51704c08-c174-393d-add5-348d3b304aeb",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z", changed=["2020-03-12T11:52:16Z"]
            ),
            catalog=Catalog(
                id="df68b420-fb97-3770-9580-7518734632b1",
                publisher=Publisher(
                    uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                    id="910298062",
                    name="KARMSUND OG KYSNESSTRAND REVISJON",
                    orgPath="/ANNET/910298062",
                    prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                    organisasjonsform="ORGL",
                ),
                title={"en": "European Data Catalog"},
                uri="http://example.org/EUCatalog",
            ),
            isOpenData=False,
            isAuthoritative=False,
            isRelatedToTransportportal=False,
            inSeries="http://example.org/budget",
            prev="http://example.org/budget-2018",
            type="datasets",
        ),
        "http://example.org/budget-2020": Dataset(
            publisher=Publisher(
                uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                id="910298062",
                name="KARMSUND OG KYSNESSTRAND REVISJON",
                orgPath="/ANNET/910298062",
                prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                organisasjonsform="ORGL",
            ),
            title={"en": "Budget data for year 2020"},
            uri="http://example.org/budget-2020",
            issued="2021-01-01",
            id="f1e8443d-910f-3838-87e3-2b5e7ee307a6",
            harvest=HarvestMetaData(
                firstHarvested="2020-03-12T11:52:16Z", changed=["2020-03-12T11:52:16Z"]
            ),
            catalog=Catalog(
                id="df68b420-fb97-3770-9580-7518734632b1",
                publisher=Publisher(
                    uri="https://organization-catalog.staging.fellesdatakatalog.digdir.no/organizations/910298062",
                    id="910298062",
                    name="KARMSUND OG KYSNESSTRAND REVISJON",
                    orgPath="/ANNET/910298062",
                    prefLabel={"nb": "Karmsund og kysnesstrand revisjon"},
                    organisasjonsform="ORGL",
                ),
                title={"en": "European Data Catalog"},
                uri="http://example.org/EUCatalog",
            ),
            isOpenData=False,
            isAuthoritative=False,
            isRelatedToTransportportal=False,
            inSeries="http://example.org/budget",
            prev="http://example.org/budget-2019",
            type="datasets",
        ),
    }

    assert parse_datasets(src) == expected
