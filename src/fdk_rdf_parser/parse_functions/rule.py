from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Rule
from fdk_rdf_parser.rdf_utils import (
    cpsv_uri,
    object_value,
    resource_list,
    resource_uri_value,
    value_translations,
)
from fdk_rdf_parser.rdf_utils.utils import value_list
from .reference_data_code import extract_reference_language_list


def extract_rules(graph: Graph, subject: URIRef) -> Optional[List[Rule]]:
    values = []
    for resource in resource_list(graph, subject, cpsv_uri("follows")):
        values.append(
            Rule(
                uri=resource_uri_value(resource),
                identifier=object_value(graph, resource, DCTERMS.identifier),
                description=value_translations(graph, resource, DCTERMS.description),
                language=extract_reference_language_list(
                    graph, resource, DCTERMS.language
                ),
                name=value_translations(graph, resource, DCTERMS.title),
                implements=value_list(graph, resource, cpsv_uri("implements")),
            )
        )

    return values if len(values) > 0 else None
