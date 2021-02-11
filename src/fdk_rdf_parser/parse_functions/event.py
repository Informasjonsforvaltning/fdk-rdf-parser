from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import BusinessEvent, Event, LifeEvent
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    is_type,
    object_value,
    resource_list,
    value_translations,
)
from .publisher import extract_authorities_as_publishers
from .skos_concept import extract_skos_concept


def parse_event(graph: Graph, subject: URIRef) -> Optional[Event]:
    subject_uri = None

    if isinstance(subject, URIRef):
        subject_uri = subject.toPython()

    if is_type(
        cv_uri("BusinessEvent"),
        graph,
        subject,
    ):
        return BusinessEvent(
            id=subject_uri,
            uri=subject_uri,
            identifier=object_value(graph, subject, DCTERMS.identifier),
            title=value_translations(graph, subject, DCTERMS.title),
            description=value_translations(graph, subject, DCTERMS.description),
            dctType=extract_skos_concept(graph, subject, DCTERMS.type),
            hasCompetentAuthority=extract_authorities_as_publishers(graph, subject),
        )

    if is_type(
        cv_uri("LifeEvent"),
        graph,
        subject,
    ):
        return LifeEvent(
            id=subject_uri,
            uri=subject_uri,
            identifier=object_value(graph, subject, DCTERMS.identifier),
            title=value_translations(graph, subject, DCTERMS.title),
            description=value_translations(graph, subject, DCTERMS.description),
            dctType=extract_skos_concept(graph, subject, DCTERMS.type),
            hasCompetentAuthority=extract_authorities_as_publishers(graph, subject),
        )

    return None


def extract_events(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Event]]:
    values: List[Event] = []
    for resource in resource_list(graph, subject, predicate):
        event = parse_event(graph, resource)
        if event:
            values.append(event)

    return values if len(values) > 0 else None
