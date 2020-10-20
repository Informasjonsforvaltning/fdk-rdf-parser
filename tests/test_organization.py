from unittest.mock import Mock

from rdflib import Graph

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.organizations import (
    add_org_path,
    publisher_from_fdk_org_catalog,
)
from .testdata import org_response_0, org_response_1


def test_publisher_from_get_all() -> None:

    expected = Publisher(
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
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
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
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
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
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
    publisher_id = Publisher(id="123456789")
    publisher_nb = Publisher(prefLabel={"nb": "nb"})
    publisher_nn = Publisher(prefLabel={"nn": "nn"})
    publisher_en = Publisher(prefLabel={"en": "en"})
    publisher_other = Publisher(prefLabel={"other": "other"})

    expected_id = Publisher(id="123456789", orgPath="/ANNET/orgpath")
    expected_nb = Publisher(prefLabel={"nb": "nb"}, orgPath="/ANNET/orgpath")
    expected_nn = Publisher(prefLabel={"nn": "nn"}, orgPath="/ANNET/orgpath")
    expected_en = Publisher(prefLabel={"en": "en"}, orgPath="/ANNET/orgpath")

    assert add_org_path(publisher_id) == expected_id
    assert add_org_path(publisher_nb) == expected_nb
    assert add_org_path(publisher_nn) == expected_nn
    assert add_org_path(publisher_en) == expected_en
    assert add_org_path(publisher_other) == Publisher(prefLabel={"other": "other"})


def test_extract_publisher_id_from_uri() -> None:

    expected = Publisher(
        uri="https://organizations.fellestestkatalog.no/organizations/123456789",
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
