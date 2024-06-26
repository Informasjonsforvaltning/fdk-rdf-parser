from functools import reduce
from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCAT,
    DCTERMS,
    SKOS,
)
from rdflib.term import Node

from fdk_rdf_parser.classes import (
    BusinessEvent,
    Event,
    LifeEvent,
)
from fdk_rdf_parser.rdf_utils import (
    cpsvno_uri,
    cv_uri,
    is_type,
    object_value,
    resource_list,
    resource_uri_value,
    value_list,
    value_translations,
)
from .catalog import parse_catalog
from .harvest_meta_data import extract_meta_data
from .skos_concept import extract_skos_concept


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


def _parse_event(graph: Graph, catalog_record_uri: Node, subject: URIRef) -> Event:
    event = Event(
        id=object_value(graph, catalog_record_uri, DCTERMS.identifier),
        uri=resource_uri_value(subject),
        identifier=object_value(graph, subject, DCTERMS.identifier),
        harvest=extract_meta_data(graph, catalog_record_uri),
        title=value_translations(graph, subject, DCTERMS.title),
        description=value_translations(graph, subject, DCTERMS.description),
        dctType=extract_skos_concept(graph, subject, DCTERMS.type),
        relation=value_list(graph, subject, DCTERMS.relation),
        associatedBroaderTypes=extract_broader_types(graph, subject),
        mayInitiate=value_list(graph, subject, cpsvno_uri("mayInitiate")),
        subject=value_list(graph, subject, DCTERMS.subject),
        distribution=value_list(graph, subject, DCAT.distribution),
        catalog=parse_catalog(graph, catalog_record_uri),
    )

    if is_type(
        cv_uri("Event"),
        graph,
        subject,
    ):
        return event

    elif is_type(
        cv_uri("BusinessEvent"),
        graph,
        subject,
    ):
        business_event = BusinessEvent()
        business_event.add_event_values(event)
        return business_event

    else:
        life_event = LifeEvent()
        life_event.add_event_values(event)
        return life_event
