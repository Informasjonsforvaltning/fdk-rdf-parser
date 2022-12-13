from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Participation
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
    value_translations,
)
from .agent import extract_agents_for_participation
from .skos_concept import extract_skos_concept


def extract_participations(
    graph: Graph, subject: URIRef
) -> Optional[List[Participation]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("hasParticipation")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None

        values.append(
            Participation(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                description=value_translations(graph, resource, DCTERMS.description),
                role=extract_skos_concept(graph, resource, cv_uri("role")),
                agents=extract_agents_for_participation(graph, resource_uri),
            )
        )

    return values if len(values) > 0 else None
