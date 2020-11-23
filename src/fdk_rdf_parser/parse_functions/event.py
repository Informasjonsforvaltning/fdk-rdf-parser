from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Event
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
    value_translations,
)


def extract_events(graph: Graph, subject: URIRef) -> Optional[List[Event]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("isGroupedBy")):
        resource_uri = None
        if isinstance(resource, URIRef):
            resource_uri = resource.toPython()

        values.append(
            Event(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                title=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                type=object_value(graph, resource, DCTERMS.type),
            )
        )

    return values if len(values) > 0 else None
