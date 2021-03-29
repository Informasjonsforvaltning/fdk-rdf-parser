from typing import Optional

from rdflib import Graph, URIRef
from rdflib.namespace import FOAF, SKOS

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.rdf_utils import br_uri, object_value, rov_uri, value_translations
from .organizations_client import get_org_path, get_rdf_org_data
from .utils import organization_number_from_uri, organization_url


def publisher_from_fdk_org_catalog(
    publisher: Optional[Publisher], orgs_graph: Graph
) -> Optional[Publisher]:
    if publisher:
        if publisher.id:
            return get_publisher_data_from_organization_catalogue(publisher, orgs_graph)
        elif publisher.uri:
            publisher.id = organization_number_from_uri(publisher.uri)

            if publisher.id:
                return get_publisher_data_from_organization_catalogue(
                    publisher, orgs_graph
                )
            else:
                return add_org_path(publisher)
        else:
            return add_org_path(publisher)
    else:
        return None


def get_publisher_data_from_organization_catalogue(
    publisher: Publisher, orgs_graph: Graph
) -> Publisher:
    org_ref = URIRef(organization_url(publisher.id))

    if (org_ref, None, None) in orgs_graph:
        return parse_publisher(orgs_graph, org_ref, publisher)
    else:
        fdk_org = get_rdf_org_data(orgnr=publisher.id)

        if fdk_org is not None:
            org_graph = Graph().parse(data=fdk_org, format="turtle")
            return parse_publisher(org_graph, org_ref, publisher)
        else:
            return add_org_path(publisher)


def parse_publisher(graph: Graph, org_ref: URIRef, publisher: Publisher) -> Publisher:
    reg_data_ref = graph.value(org_ref, rov_uri("registration"))

    return Publisher(
        id=object_value(graph, reg_data_ref, SKOS.notation),
        uri=org_ref.toPython(),
        name=object_value(graph, org_ref, rov_uri("legalName")),
        orgPath=object_value(graph, org_ref, br_uri("orgPath")),
        prefLabel=publisher.prefLabel
        if publisher.prefLabel
        else value_translations(graph, org_ref, FOAF.name),
        organisasjonsform=object_value(graph, org_ref, rov_uri("orgType")),
    )


def add_org_path(publisher: Publisher) -> Publisher:
    org_path = None
    if publisher.id:
        org_path = get_org_path(publisher.id.strip().replace(" ", ""))
    elif publisher.prefLabel:
        if publisher.prefLabel.get("nb"):
            org_path = get_org_path(publisher.prefLabel["nb"])
        elif publisher.prefLabel.get("nn"):
            org_path = get_org_path(publisher.prefLabel["nn"])
        elif publisher.prefLabel.get("en"):
            org_path = get_org_path(publisher.prefLabel["en"])

    publisher.orgPath = org_path
    return publisher
