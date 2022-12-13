from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Cost
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_number_value,
    object_value,
    resource_list,
    value_translations,
)
from .channel import extract_channels
from .publisher import extract_list_of_publishers


def extract_costs(graph: Graph, subject: URIRef) -> Optional[List[Cost]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("hasCost")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        channels = extract_channels(graph, resource, cv_uri("ifAccessedThrough"))
        values.append(
            Cost(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                description=value_translations(graph, resource, DCTERMS.description),
                currency=object_value(graph, resource, cv_uri("currency")),
                ifAccessedThrough=channels[0]
                if channels is not None and len(channels) == 1
                else None,
                isDefinedBy=extract_list_of_publishers(
                    graph, resource, cv_uri("isDefinedBy")
                ),
                value=str(object_number_value(graph, resource, cv_uri("value"))),
            )
        )

    return values if len(values) > 0 else None
