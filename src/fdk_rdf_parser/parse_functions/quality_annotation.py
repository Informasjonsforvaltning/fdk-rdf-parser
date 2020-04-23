from typing import Dict
from rdflib import Graph, URIRef
from rdflib.namespace import RDF

from fdk_rdf_parser.classes import QualityAnnotation
from fdk_rdf_parser.rdf_utils import (
    objectValue,
    resourceList,
    valueTranslations,
    dqvURI,
    provURI,
)


def extractQualityAnnotation(
    graph: Graph, subject: URIRef
) -> Dict[str, QualityAnnotation]:
    annotations = {}

    for annotation in resourceList(graph, subject, dqvURI("hasQualityAnnotation")):
        inDimensionValue = objectValue(graph, annotation, dqvURI("inDimension"))
        annotations[inDimensionValue] = QualityAnnotation(
            inDimension=inDimensionValue, hasBody=extractHasBody(graph, annotation)
        )

    return annotations


def extractHasBody(graph: Graph, subject: URIRef) -> Dict[str, str]:
    hasBodyURI = graph.value(subject, provURI("hasBody"))
    if hasBodyURI is not None:
        return valueTranslations(graph, hasBodyURI, RDF.value)
    else:
        return None