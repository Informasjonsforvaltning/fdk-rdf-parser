from typing import List

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Temporal
from fdk_rdf_parser.rdf_utils import objectValue, resourceList, dcatURI, schemaURI, owlTimeURI

def extractTemporal(graph: Graph, subject: URIRef) -> List[Temporal]:
    values = []
    for temporalResource in resourceList(graph, subject, DCTERMS.temporal):
        temporalURI = None
        if isinstance(temporalResource, URIRef):
            temporalURI = temporalResource.toPython()

        if isinstance(temporalResource, BNode) or temporalURI != None:
            startValue = objectValue(graph, temporalResource, dcatURI('startDate'))
            endValue = objectValue(graph, temporalResource, dcatURI('endDate'))

            startValue = objectValue(graph, temporalResource, schemaURI('startDate')) if startValue == None else startValue
            endValue = objectValue(graph, temporalResource, schemaURI('endDate')) if endValue == None else endValue

            startValue = extractOwlTimeStart(graph, temporalResource) if startValue == None else startValue
            endValue = extractOwlTimeEnd(graph, temporalResource) if endValue == None else endValue

            values.append(
                Temporal(
                    uri = temporalURI,
                    startDate = startValue,
                    endDate = endValue)
            )

    return values

def extractOwlTimeInstant(graph: Graph, subject: URIRef):
    dateValue = graph.value(subject, owlTimeURI('inXSDDateTime'))
    dateValue = graph.value(subject, owlTimeURI('inXSDDateTimeStamp')) if dateValue == None else dateValue
    dateValue = graph.value(subject, owlTimeURI('inXSDDate')) if dateValue == None else dateValue

    if dateValue != None:
        return dateValue.toPython()
    else:
        return None

def extractOwlTimeStart(graph: Graph, subject: URIRef):
    hasBeginning = graph.value(subject, owlTimeURI('hasBeginning'))
    if hasBeginning != None:
        return extractOwlTimeInstant(graph, hasBeginning)
    else:
        return None

def extractOwlTimeEnd(graph: Graph, subject: URIRef):
    hasEnd = graph.value(subject, owlTimeURI('hasEnd'))
    if hasEnd != None:
        return extractOwlTimeInstant(graph, hasEnd)
    else:
        return None