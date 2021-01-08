from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, XSD

from fdk_rdf_parser.classes import LegalResource
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
    value_translations,
)


def extract_legal_resources(
    graph: Graph, subject: URIRef
) -> Optional[List[LegalResource]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("hasLegalResource")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            LegalResource(
                uri=resource_uri,
                description=value_translations(graph, resource, DCTERMS.description),
                url=object_value(graph, resource, XSD.seeAlso),
            )
        )

    return values if len(values) > 0 else None
