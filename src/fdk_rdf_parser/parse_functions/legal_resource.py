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
    resource_list,
    resource_uri_value,
    value_list,
    value_translations,
)


def extract_legal_resources(
    graph: Graph, subject: URIRef, predicate: Any
) -> Optional[List[LegalResource]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        values.append(
            LegalResource(
                uri=resource_uri_value(resource),
                dctTitle=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                seeAlso=value_list(graph, resource, RDFS.seeAlso),
                relation=value_list(graph, resource, DCTERMS.relation),
            )
        )

    return values if len(values) > 0 else None
