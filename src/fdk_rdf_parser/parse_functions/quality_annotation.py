from typing import (
    Dict,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    RDF,
)

from fdk_rdf_parser.classes import QualityAnnotation
from fdk_rdf_parser.rdf_utils import (
    dqv_uri,
    linguistic_system_keywords,
    oa_uri,
    object_value,
    resource_list,
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
    has_body: Dict[str, str] = {}
    for has_body_ref in resource_list(graph, subject, oa_uri("hasBody")):
        lang_uri = object_value(graph, has_body_ref, DCTERMS.language)
        lang = linguistic_system_keywords.get(lang_uri if lang_uri else "")

        value = object_value(graph, has_body_ref, RDF.value)
        if value:
            has_body[lang if lang else "no"] = value
    return has_body if len(has_body) > 0 else None
