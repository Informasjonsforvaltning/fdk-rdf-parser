from dataclasses import asdict
from unittest.mock import Mock

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser import parse_datasets
from fdk_rdf_parser.classes import (
    Catalog,
    Dataset,
    DatasetSeries,
    HarvestMetaData,
    InSeries,
    Publisher,
    ReferenceDataCode,
)
from fdk_rdf_parser.fdk_rdf_parser import (
    parse_dataset,
    parse_dataset_json_serializable,
)
from fdk_rdf_parser.parse_functions.dataset import _parse_dataset_series


def test_parse_dataset_series(mock_reference_data_client: Mock) -> None:
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
            provenance=ReferenceDataCode(
                uri="http://data.brreg.no/datakatalog/provinens/nasjonal",
                code="NASJONAL",
                prefLabel={
                    "en": "Authoritativ source",
                    "nb": "Autoritativ kilde",
                    "nn": "Autoritativ kilde",
                },
            ),
            datasetsInSeries=[
                "http://example.org/budget-2020",
                "http://example.org/budget-2019",
                "http://example.org/budget-2018",
            ],
            isOpenData=False,
            isAuthoritative=True,
            isRelatedToTransportportal=False,
            inSeries=None,
            type="datasets",
            last="http://example.org/budget-2020",
            specializedType="datasetSeries",
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
            inSeries=InSeries(
                uri="http://example.org/budget",
                id="ad115f63-9edc-30dc-ab81-f6866e0631ea",
                title={"en": "Budget data"},
            ),
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
            inSeries=InSeries(
                uri="http://example.org/budget",
                id="ad115f63-9edc-30dc-ab81-f6866e0631ea",
                title={"en": "Budget data"},
            ),
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
            inSeries=InSeries(
                uri="http://example.org/budget",
                id="ad115f63-9edc-30dc-ab81-f6866e0631ea",
                title={"en": "Budget data"},
            ),
            prev="http://example.org/budget-2019",
            type="datasets",
        ),
    }

    with open("tests/test_data/dataset_series0.ttl", "r") as src:
        assert parse_datasets(src.read()) == expected


def test_parse_dataset_series_abort_on_circular_graph(
    mock_reference_data_client: Mock,
) -> None:
    src = """
        @prefix ex: <http://example.org/> .
        @prefix dcat: <http://www.w3.org/ns/dcat#> .


        ex:budget a dcat:Dataset , dcat:DatasetSeries ;
            dcat:last ex:budget-2020 ;
            .

        ex:budget-2017 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            .

        ex:budget-2018 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            dcat:prev ex:budget-2020 ;
            .

        ex:budget-2019 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            dcat:prev ex:budget-2018 ;
            .

        ex:budget-2020 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            dcat:prev ex:budget-2019 ;
            .
    """
    expected = DatasetSeries(
        specializedType="datasetSeries",
        datasetsInSeries=[
            "http://example.org/budget-2020",
            "http://example.org/budget-2019",
            "http://example.org/budget-2018",
        ],
        last="http://example.org/budget-2020",
    )

    graph = Graph().parse(data=src, format="turtle")
    assert _parse_dataset_series(graph, URIRef("http://example.org/budget")) == expected


def test_parse_dataset_series_broken_linked_list(
    mock_reference_data_client: Mock,
) -> None:
    src = """
        @prefix ex: <http://example.org/> .
        @prefix dcat: <http://www.w3.org/ns/dcat#> .


        ex:budget a dcat:Dataset , dcat:DatasetSeries ;
            dcat:last ex:budget-2020 ;
            .

        ex:budget-2016 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            .

        ex:budget-2017 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            .

        ex:budget-2018 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            .

        ex:budget-2019 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            dcat:prev ex:budget-2018 ;
            .

        ex:budget-2020 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            dcat:prev ex:budget-2019 ;
            .

    """
    expected = DatasetSeries(
        specializedType="datasetSeries",
        datasetsInSeries=[
            "http://example.org/budget-2020",
            "http://example.org/budget-2019",
            "http://example.org/budget-2018",
        ],
        last="http://example.org/budget-2020",
    )

    graph = Graph().parse(data=src, format="turtle")
    assert _parse_dataset_series(graph, URIRef("http://example.org/budget")) == expected


def test_parse_single_dataset_series(
    mock_reference_data_client: Mock,
) -> None:
    graph = """
        @prefix ex: <http://example.org/> .
        @prefix dcat: <http://www.w3.org/ns/dcat#> .
        @prefix foaf:  <http://xmlns.com/foaf/0.1/> .
        @prefix dct: <http://purl.org/dc/terms/> .
        @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .


        <http://localhost:5000/datasets/f1e8443d-910f-3838-87e3-2b5e7ee307a6>
            a                  dcat:CatalogRecord ;
            dct:identifier     "f1e8443d-910f-3838-87e3-2b5e7ee307a6" ;
            dct:issued         "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            dct:modified       "2020-03-12T11:52:16.122Z"^^xsd:dateTime ;
            foaf:primaryTopic  ex:budget .


        ex:budget a dcat:Dataset , dcat:DatasetSeries ;
            dcat:last ex:budget-2020 ;
            .

        ex:budget-2019 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            .

        ex:budget-2020 a dcat:Dataset ;
            dcat:inSeries ex:budget ;
            dcat:prev ex:budget-2019 ;
            .

    """
    expected = DatasetSeries(
        specializedType="datasetSeries",
        uri="http://example.org/budget",
        id="f1e8443d-910f-3838-87e3-2b5e7ee307a6",
        harvest=HarvestMetaData(
            firstHarvested="2020-03-12T11:52:16Z", changed=["2020-03-12T11:52:16Z"]
        ),
        datasetsInSeries=[
            "http://example.org/budget-2020",
            "http://example.org/budget-2019",
        ],
        last="http://example.org/budget-2020",
    )

    assert parse_dataset(graph) == expected
    assert parse_dataset_json_serializable(graph) == asdict(expected)
