from typing import (
    Any,
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    RDFS,
)

from fdk_rdf_parser.classes import LegalResource
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    value_translations,
)


def extract_legal_resources(
    graph: Graph, subject: URIRef, predicate: Any
) -> Optional[List[LegalResource]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            LegalResource(
                uri=resource_uri,
                description=value_translations(graph, resource, DCTERMS.description),
                url=object_value(graph, resource, RDFS.seeAlso),
            )
        )

    return values if len(values) > 0 else None
