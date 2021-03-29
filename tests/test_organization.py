from unittest.mock import Mock

from rdflib import Graph

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.organizations import (
    add_org_path,
    publisher_from_fdk_org_catalog,
)
from fdk_rdf_parser.organizations.utils import organization_url
from .testdata import org_response_0, org_response_1


def test_publisher_from_get_all() -> None:

    expected = Publisher(
        uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        organisasjonsform="ORGL",
    )

    orgs_graph = Graph().parse(data=org_response_0, format="turtle")

    assert (
        publisher_from_fdk_org_catalog(
            Publisher(uri="https://externalurl.org/123456789", id="123456789"),
            orgs_graph,
        )
        == expected
    )


def test_publisher_not_present_in_get_all(mock_organizations_client: Mock) -> None:

    expected = Publisher(
        uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        organisasjonsform="ORGL",
    )

    orgs_graph = Graph().parse(data=org_response_1, format="turtle")

    assert (
        publisher_from_fdk_org_catalog(
            Publisher(uri="https://externalurl.org/123456789", id="123456789"),
            orgs_graph,
        )
        == expected
    )


def test_publisher_not_found(mock_organizations_error: Mock) -> None:

    expected = Publisher(uri="https://externalurl.org/123456789", id="123456789")

    orgs_graph = Graph().parse(data=org_response_1, format="turtle")

    assert (
        publisher_from_fdk_org_catalog(
            Publisher(uri="https://externalurl.org/123456789", id="123456789"),
            orgs_graph,
        )
        == expected
    )


def test_original_pref_label_is_retained(mock_organizations_client: Mock) -> None:

    expected = Publisher(
        uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={"en": "Original label"},
        organisasjonsform="ORGL",
    )

    orgs_graph = Graph().parse(data=org_response_1, format="turtle")

    assert (
        publisher_from_fdk_org_catalog(
            Publisher(
                uri="https://externalurl.org/123456789",
                id="123456789",
                prefLabel={"en": "Original label"},
            ),
            orgs_graph,
        )
        == expected
    )


def test_orgpath(mock_orgpath_client: Mock) -> None:
    publisher_id_0 = Publisher(id="123456789")
    publisher_id_1 = Publisher(id="123 456 789")
    publisher_id_2 = Publisher(id="123456789 ")
    publisher_id_3 = Publisher(
        id=""" 123456789
                                                """
    )
    publisher_nb = Publisher(prefLabel={"nb": "Preflabel Bokmål"})
    publisher_nn = Publisher(prefLabel={"nn": "Preflabel Nynorsk"})
    publisher_en = Publisher(prefLabel={"en": "Preflabel Engelsk"})
    publisher_other = Publisher(prefLabel={"other": "other"})

    expected_id_0 = Publisher(id="123456789", orgPath="/ANNET/123456789")
    expected_id_1 = Publisher(id="123 456 789", orgPath="/ANNET/123456789")
    expected_id_2 = Publisher(id="123456789 ", orgPath="/ANNET/123456789")
    expected_id_3 = Publisher(
        id=""" 123456789
                                                """,
        orgPath="/ANNET/123456789",
    )
    expected_nb = Publisher(
        prefLabel={"nb": "Preflabel Bokmål"}, orgPath="/ANNET/Preflabel Bokmål"
    )
    expected_nn = Publisher(
        prefLabel={"nn": "Preflabel Nynorsk"}, orgPath="/ANNET/Preflabel Nynorsk"
    )
    expected_en = Publisher(
        prefLabel={"en": "Preflabel Engelsk"}, orgPath="/ANNET/Preflabel Engelsk"
    )

    assert add_org_path(publisher_id_0) == expected_id_0
    assert add_org_path(publisher_id_1) == expected_id_1
    assert add_org_path(publisher_id_2) == expected_id_2
    assert add_org_path(publisher_id_3) == expected_id_3
    assert add_org_path(publisher_nb) == expected_nb
    assert add_org_path(publisher_nn) == expected_nn
    assert add_org_path(publisher_en) == expected_en
    assert add_org_path(publisher_other) == Publisher(prefLabel={"other": "other"})


def test_extract_publisher_id_from_enhetsregisteret_uri() -> None:

    expected = Publisher(
        uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        organisasjonsform="ORGL",
    )

    orgs_graph = Graph().parse(data=org_response_0, format="turtle")

    assert (
        publisher_from_fdk_org_catalog(
            Publisher(
                uri="https://data.brreg.no/enhetsregisteret/api/enheter/123456789"
            ),
            orgs_graph,
        )
        == expected
    )


def test_extract_publisher_id_from_org_uri() -> None:

    expected = Publisher(
        uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789",
        id="123456789",
        name="Digitaliseringsdirektoratet",
        orgPath="/STAT/987654321/123456789",
        prefLabel={
            "nn": "Digitaliseringsdirektoratet",
            "nb": "Digitaliseringsdirektoratet",
            "en": "Norwegian Digitalisation Agency",
        },
        organisasjonsform="ORGL",
    )

    orgs_graph = Graph().parse(data=org_response_0, format="turtle")

    assert (
        publisher_from_fdk_org_catalog(
            Publisher(
                uri="https://organizations.fellesdatakatalog.digdir.no/organizations/123456789"
            ),
            orgs_graph,
        )
        == expected
    )


def test_only_extract_publisher_id_from_brreg_uri() -> None:

    expected = Publisher(uri="https://externalurl.org/123456789")

    orgs_graph = Graph().parse(data=org_response_0, format="turtle")

    assert (
        publisher_from_fdk_org_catalog(
            Publisher(uri="https://externalurl.org/123456789"), orgs_graph
        )
        == expected
    )


def test_handles_empty_publisher() -> None:

    expected = Publisher()

    orgs_graph = Graph().parse(data=org_response_0, format="turtle")

    assert publisher_from_fdk_org_catalog(Publisher(), orgs_graph) == expected


def test_responds_with_none_when_none_input() -> None:

    orgs_graph = Graph().parse(data=org_response_0, format="turtle")

    assert publisher_from_fdk_org_catalog(None, orgs_graph) is None


def test_create_org_url() -> None:
    expected = (
        "https://organizations.fellesdatakatalog.digdir.no/organizations/123456789"
    )

    assert organization_url("123456789") == expected
    assert organization_url("123 456 789") == expected
    assert organization_url("123456789 ") == expected
    assert (
        organization_url(
            """ 123456789
                                                """
        )
        == expected
    )
