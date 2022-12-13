from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import QualifiedAttribution
from fdk_rdf_parser.rdf_utils import (
    dcat_uri,
    object_value,
    prov_uri,
    resource_list,
)
from .publisher import parse_publisher


def extract_qualified_attributions(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[QualifiedAttribution]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        publisher_uri = graph.value(resource, prov_uri("agent"))

        if isinstance(publisher_uri, URIRef):
            role = object_value(graph, resource, dcat_uri("hadRole"))

            values.append(
                QualifiedAttribution(
                    agent=parse_publisher(graph, publisher_uri), role=role
                )
            )

    return values if len(values) > 0 else None
