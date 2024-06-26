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
    resource_uri_value,
    value_translations,
)
from .reference_data_code import extract_reference_language_code


def extract_formats(graph: Graph, subject: URIRef) -> Optional[List[Format]]:
    values = []
    for resource in resource_list(graph, subject, DCTERMS.hasFormat):
        values.append(
            Format(
                uri=resource_uri_value(resource),
                title=value_translations(graph, resource, DCTERMS.title),
                format=object_value(graph, resource, dct_uri("format")),
                language=extract_reference_language_code(
                    graph, resource, DCTERMS.language
                ),
                seeAlso=object_value(graph, resource, RDFS.seeAlso),
            )
        )

    return values if len(values) > 0 else None
