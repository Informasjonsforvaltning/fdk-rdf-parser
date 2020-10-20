from typing import List, Optional

from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import Publisher, QualifiedAttribution
from fdk_rdf_parser.organizations import organization_number_from_uri
from fdk_rdf_parser.rdf_utils import (
    dcat_uri,
    object_value,
    prov_uri,
    resource_list,
)


def extract_qualified_attributions(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[QualifiedAttribution]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        publisher_uri = object_value(graph, resource, prov_uri("agent"))

        if isinstance(publisher_uri, str):
            publisher_id = organization_number_from_uri(publisher_uri)
            role = object_value(graph, resource, dcat_uri("hadRole"))

            values.append(
                QualifiedAttribution(
                    agent=Publisher(uri=publisher_uri, id=publisher_id), role=role
                )
            )

    return values if len(values) > 0 else None
