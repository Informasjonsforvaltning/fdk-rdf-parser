from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import CriterionRequirement
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
    value_translations,
)


def extract_criterion_requirements(
    graph: Graph, subject: URIRef
) -> Optional[List[CriterionRequirement]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("hasCriterion")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            CriterionRequirement(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                name=value_translations(graph, resource, DCTERMS.title),
                type=object_value(graph, resource, DCTERMS.type),
            )
        )

    return values if len(values) > 0 else None
