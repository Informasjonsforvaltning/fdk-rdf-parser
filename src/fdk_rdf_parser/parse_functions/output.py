from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Output
from fdk_rdf_parser.rdf_utils import (
    cpsv_uri,
    object_value,
    resource_list,
    resource_uri_value,
    value_translations,
)
from .reference_data_code import extract_reference_language_list
from .skos_concept import extract_skos_concept


def extract_outputs(graph: Graph, subject: URIRef) -> Optional[List[Output]]:
    values = []
    for resource in resource_list(graph, subject, cpsv_uri("produces")):
        values.append(
            Output(
                uri=resource_uri_value(resource),
                identifier=object_value(graph, resource, DCTERMS.identifier),
                name=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                language=extract_reference_language_list(
                    graph, resource, DCTERMS.language
                ),
                type=extract_skos_concept(graph, resource, DCTERMS.type),
            )
        )

    return values if len(values) > 0 else None
