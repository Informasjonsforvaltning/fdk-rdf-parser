from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Channel
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
)
from .skos_concept import extract_skos_concept


def extract_channels(graph: Graph, subject: URIRef) -> Optional[List[Channel]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("hasChannel")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        skos_concepts = extract_skos_concept(graph, resource, DCTERMS.type)
        values.append(
            Channel(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                type=skos_concepts[0]
                if skos_concepts is not None and len(skos_concepts) == 1
                else None,
            )
        )

    return values if len(values) > 0 else None
