from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
    SKOS,
)

from fdk_rdf_parser.classes import Organization
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    org_uri,
    rov_uri,
)
from fdk_rdf_parser.rdf_utils.ns import br_uri
from fdk_rdf_parser.rdf_utils.utils import (
    is_type,
    value_list,
    value_translations,
)
from .dcat_resource import extract_reference_data_code


def parse_organization(graph: Graph, organization_uri: URIRef) -> Organization:
    organization = Organization(
        uri=organization_uri.toPython()
        if isinstance(organization_uri, URIRef)
        else None,
        identifier=object_value(graph, organization_uri, DCTERMS.identifier),
    )
    if is_type(org_uri("Organization"), graph, organization_uri) or is_type(
        cv_uri("PublicOrganisation"), graph, organization_uri
    ):
        organization.name = value_translations(graph, organization_uri, DCTERMS.title)
        organization.title = value_translations(graph, organization_uri, SKOS.prefLabel)
        organization.homepage = value_list(graph, organization_uri, FOAF.homepage)
        organization.spatial = value_list(graph, organization_uri, DCTERMS.spatial)
        organization.orgType = extract_reference_data_code(
            graph, organization_uri, DCTERMS.type
        )
    elif is_type(rov_uri("RegisteredOrganization"), graph, organization_uri):
        organization.name = value_translations(
            graph, organization_uri, rov_uri("legalName")
        )
        organization.orgPath = object_value(graph, organization_uri, br_uri("orgPath"))
        organization.title = value_translations(graph, organization_uri, FOAF.name)
        organization.homepage = value_list(graph, organization_uri, FOAF.homepage)
    return set_organization_name_from_pref_label_if_missing(organization)


def extract_organizations(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Organization]]:
    organization_list = list(
        map(
            lambda organization_uri: parse_organization(graph, organization_uri),
            graph.objects(subject, predicate),
        )
    )
    return organization_list if len(organization_list) > 0 else None


def set_organization_name_from_pref_label_if_missing(
    organization: Organization,
) -> Organization:
    if (organization.name and len(organization.name) > 0) or organization.title is None:
        return organization
    organization.name = organization.title
    return organization
