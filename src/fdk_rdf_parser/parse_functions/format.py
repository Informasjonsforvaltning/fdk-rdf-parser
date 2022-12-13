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
    RDFS,
)

from fdk_rdf_parser.classes import Format
from fdk_rdf_parser.rdf_utils import (
    dct_uri,
    object_value,
    resource_list,
    value_translations,
)
from .dcat_resource import extract_skos_code


def extract_formats(graph: Graph, subject: URIRef) -> Optional[List[Format]]:
    values = []
    for resource in resource_list(graph, subject, DCTERMS.hasFormat):
        format_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            Format(
                uri=format_uri,
                title=value_translations(graph, resource, DCTERMS.title),
                format=object_value(graph, resource, dct_uri("format")),
                language=extract_skos_code(graph, resource, DCTERMS.language),
                seeAlso=object_value(graph, resource, RDFS.seeAlso),
            )
        )

    return values if len(values) > 0 else None
