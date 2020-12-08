from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Evidence
from fdk_rdf_parser.rdf_utils import (
    cpsv_uri,
    object_value,
    resource_list,
    value_translations,
)
from .dcat_resource import extract_skos_code_list


def extract_evidences(graph: Graph, subject: URIRef) -> Optional[List[Evidence]]:
    values = []
    for resource in resource_list(graph, subject, cpsv_uri("hasInput")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            Evidence(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                name=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                type=object_value(graph, resource, DCTERMS.type),
                language=extract_skos_code_list(graph, resource, DCTERMS.language),
            )
        )

    return values if len(values) > 0 else None
