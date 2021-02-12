from typing import Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import BusinessEvent, Event, LifeEvent
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    is_type,
    object_value,
    value_translations,
)
from .harvest_meta_data import extract_meta_data
from .publisher import extract_authorities_as_publishers
from .skos_concept import extract_skos_concept


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
            hasCompetentAuthority=extract_authorities_as_publishers(graph, subject),
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
            hasCompetentAuthority=extract_authorities_as_publishers(graph, subject),
        )
