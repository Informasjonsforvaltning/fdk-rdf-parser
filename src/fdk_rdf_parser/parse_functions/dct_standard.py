from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    OWL,
    RDFS,
)

from fdk_rdf_parser.classes import DctStandard
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    resource_uri_value,
    value_list,
    value_translations,
)


def extract_dct_standard_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[DctStandard]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        values.append(
            DctStandard(
                uri=resource_uri_value(resource),
                title=value_translations(graph, resource, DCTERMS.title),
                seeAlso=value_list(graph, resource, RDFS.seeAlso),
                versionInfo=object_value(graph, resource, OWL.versionInfo),
            )
        )

    return values if len(values) > 0 else None
