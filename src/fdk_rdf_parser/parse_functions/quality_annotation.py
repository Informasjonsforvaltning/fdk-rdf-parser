from typing import Dict, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import RDF

from fdk_rdf_parser.classes import QualityAnnotation
from fdk_rdf_parser.rdf_utils import (
    dqv_uri,
    object_value,
    prov_uri,
    resource_list,
    value_translations,
)


def extract_quality_annotation(
    graph: Graph, subject: URIRef
) -> Dict[str, QualityAnnotation]:
    annotations = {}

    for annotation in resource_list(graph, subject, dqv_uri("hasQualityAnnotation")):
        in_dimension_value = object_value(graph, annotation, dqv_uri("inDimension"))
        if in_dimension_value is not None and isinstance(in_dimension_value, str):
            annotations[in_dimension_value] = QualityAnnotation(
                inDimension=in_dimension_value,
                hasBody=extract_has_body(graph, annotation),
            )

    return annotations


def extract_has_body(graph: Graph, subject: URIRef) -> Optional[Dict[str, str]]:
    has_body_uri = graph.value(subject, prov_uri("hasBody"))
    if has_body_uri is not None:
        return value_translations(graph, has_body_uri, RDF.value)
    else:
        return None
