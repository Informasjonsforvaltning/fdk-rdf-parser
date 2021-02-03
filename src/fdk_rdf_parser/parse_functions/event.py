from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Event
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    value_translations,
)
from .skos_concept import extract_skos_concept


def extract_events(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Event]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        resource_uri = None
        if isinstance(resource, URIRef):
            resource_uri = resource.toPython()

        values.append(
            Event(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                title=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                type=extract_skos_concept(graph, resource, DCTERMS.type),
            )
        )

    return values if len(values) > 0 else None
