from typing import Optional

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Participation
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    value_translations,
)
from .skos_concept import extract_skos_concept


def parse_participation(graph: Graph, subject: URIRef) -> Optional[Participation]:
    resource_uri = subject.toPython() if isinstance(subject, URIRef) else None
    return Participation(
        uri=resource_uri,
        identifier=object_value(graph, subject, DCTERMS.identifier),
        description=value_translations(graph, subject, DCTERMS.description),
        role=extract_skos_concept(graph, subject, cv_uri("role")),
        agent=object_value(graph, subject, cv_uri("hasParticipant")),
    )
