from functools import reduce
from typing import Dict, List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, SKOS

from fdk_rdf_parser.classes import BusinessEvent, Event, LifeEvent
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    is_type,
    object_value,
    resource_list,
    value_list,
    value_translations,
)
from .harvest_meta_data import extract_meta_data
from .publisher import extract_list_of_publishers
from .skos_concept import extract_skos_concept


def extend_with_associated_broader_types(
    events: Dict[str, Optional[Event]], event_uri: str, values: List[str]
) -> List[str]:
    current_event: Optional[Event] = events.get(event_uri)
    if current_event and current_event.associatedBroaderTypes:
        values.extend(current_event.associatedBroaderTypes)
    return values


def extract_all_broader_skos_concepts(
    graph: Graph, subject: URIRef, values: List[str]
) -> List[str]:
    broader_list_uris = resource_list(graph, subject, SKOS.broader)

    values.append(subject.toPython())

    for skos_concept_uri in broader_list_uris:
        if skos_concept_uri.toPython() not in values:
            extract_all_broader_skos_concepts(graph, skos_concept_uri, values)

    return values


def extract_broader_types(graph: Graph, event_subject: URIRef) -> Optional[List[str]]:

    broader_type_instances_from_event = resource_list(
        graph, event_subject, DCTERMS.type
    )
    associated_skos_concepts_uris: List[str] = []
    if (
        broader_type_instances_from_event is not None
        and len(broader_type_instances_from_event) > 0
    ):
        reduce(
            lambda output, current: extract_all_broader_skos_concepts(
                graph, current, output
            ),
            broader_type_instances_from_event,
            associated_skos_concepts_uris,
        )

    return (
        associated_skos_concepts_uris
        if len(associated_skos_concepts_uris) > 0
        else None
    )


def parse_event(
    graph: Graph, catalog_record_uri: URIRef, subject: URIRef
) -> Optional[Event]:

    if is_type(
        cv_uri("BusinessEvent"),
        graph,
        subject,
    ):
        return BusinessEvent(
            id=object_value(graph, catalog_record_uri, DCTERMS.identifier),
            uri=subject.toPython(),
            identifier=object_value(graph, subject, DCTERMS.identifier),
            harvest=extract_meta_data(graph, catalog_record_uri),
            title=value_translations(graph, subject, DCTERMS.title),
            description=value_translations(graph, subject, DCTERMS.description),
            dctType=extract_skos_concept(graph, subject, DCTERMS.type),
            hasCompetentAuthority=extract_list_of_publishers(
                graph, subject, cv_uri("hasCompetentAuthority")
            ),
            relation=value_list(graph, subject, DCTERMS.relation),
            associatedBroaderTypes=extract_broader_types(graph, subject),
        )

    else:
        return LifeEvent(
            id=object_value(graph, catalog_record_uri, DCTERMS.identifier),
            uri=subject.toPython(),
            identifier=object_value(graph, subject, DCTERMS.identifier),
            harvest=extract_meta_data(graph, catalog_record_uri),
            title=value_translations(graph, subject, DCTERMS.title),
            description=value_translations(graph, subject, DCTERMS.description),
            dctType=extract_skos_concept(graph, subject, DCTERMS.type),
            hasCompetentAuthority=extract_list_of_publishers(
                graph, subject, cv_uri("hasCompetentAuthority")
            ),
            relation=value_list(graph, subject, DCTERMS.relation),
            associatedBroaderTypes=extract_broader_types(graph, subject),
        )
