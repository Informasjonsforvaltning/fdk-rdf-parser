from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import DataDistributionService
from fdk_rdf_parser.rdf_utils import (
    dcat_api_uri,
    dcat_uri,
    resource_list,
    value_translations,
)
from .skos_concept import extract_skos_concept


def extract_data_distribution_services(
    graph: Graph, subject: URIRef
) -> Optional[List[DataDistributionService]]:
    values = []

    access_services = resource_list(graph, subject, dcat_api_uri("accessService"))
    access_services.extend(resource_list(graph, subject, dcat_uri("accessService")))

    for resource in access_services:
        resource_uri = None
        if isinstance(resource, URIRef):
            resource_uri = resource.toPython()

        endpoint_description = extract_skos_concept(
            graph, resource, dcat_uri("endpointDescription")
        )

        values.append(
            DataDistributionService(
                uri=resource_uri,
                title=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                endpointDescription=(
                    endpoint_description
                    if endpoint_description
                    else extract_skos_concept(
                        graph, resource, dcat_api_uri("endpointDescription")
                    )
                ),
            )
        )

    return values if len(values) > 0 else None
