from typing import Any, List, Optional

from rdflib import BNode, Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Temporal
from fdk_rdf_parser.rdf_utils import (
    dateValue,
    dcatURI,
    owlTimeURI,
    resourceList,
    schemaURI,
)


def extractTemporal(graph: Graph, subject: URIRef) -> Optional[List[Temporal]]:
    values = []
    for temporalResource in resourceList(graph, subject, DCTERMS.temporal):
        temporalURI = None
        if isinstance(temporalResource, URIRef):
            temporalURI = temporalResource.toPython()

        if isinstance(temporalResource, BNode) or temporalURI is not None:
            startValue = dateValue(graph, temporalResource, dcatURI("startDate"))
            endValue = dateValue(graph, temporalResource, dcatURI("endDate"))

            startValue = (
                dateValue(graph, temporalResource, schemaURI("startDate"))
                if startValue is None
                else startValue
            )
            endValue = (
                dateValue(graph, temporalResource, schemaURI("endDate"))
                if endValue is None
                else endValue
            )

            startValue = (
                extractOwlTimeStart(graph, temporalResource)
                if startValue is None
                else startValue
            )
            endValue = (
                extractOwlTimeEnd(graph, temporalResource)
                if endValue is None
                else endValue
            )

            values.append(
                Temporal(uri=temporalURI, startDate=startValue, endDate=endValue)
            )

    return values if len(values) > 0 else None


def extractOwlTimeInstant(graph: Graph, subject: Any) -> Optional[str]:
    owlDate = dateValue(graph, subject, owlTimeURI("inXSDDateTime"))
    owlDate = (
        dateValue(graph, subject, owlTimeURI("inXSDDateTimeStamp"))
        if owlDate is None
        else owlDate
    )
    owlDate = (
        dateValue(graph, subject, owlTimeURI("inXSDDate"))
        if owlDate is None
        else owlDate
    )

    return owlDate


def extractOwlTimeStart(graph: Graph, subject: Any) -> Any:
    hasBeginning = graph.value(subject, owlTimeURI("hasBeginning"))
    if hasBeginning is not None:
        return extractOwlTimeInstant(graph, hasBeginning)
    else:
        return None


def extractOwlTimeEnd(graph: Graph, subject: Any) -> Any:
    hasEnd = graph.value(subject, owlTimeURI("hasEnd"))
    if hasEnd is not None:
        return extractOwlTimeInstant(graph, hasEnd)
    else:
        return None
