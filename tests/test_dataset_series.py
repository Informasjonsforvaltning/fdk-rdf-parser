from unittest.mock import Mock

from fdk_rdf_parser import parse_datasets
from fdk_rdf_parser.classes import (
    Catalog,
    Dataset,
    DatasetSeries,
    HarvestMetaData,
    Publisher,
    ReferenceDataCode,
)


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

    with open("tests/test_data/dataset_series0.ttl", "r") as src:
        assert parse_datasets(src.read()) == expected
