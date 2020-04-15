from typing import List
from dataclasses import dataclass
from datetime import datetime

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import DCTERMS

from .rdf_utils import objectValue, resourceList, dcatURI, schemaURI, owlTimeURI

@dataclass
class Temporal:
    uri: str = None
    startDate: datetime = None
    endDate: datetime = None

def extractTemporal(graph: Graph, subject: URIRef) -> List[Temporal]:
    values = []
    for temporalResource in resourceList(graph, subject, DCTERMS.temporal):
        temporalURI = None
        if isinstance(temporalResource, URIRef):
            temporalURI = temporalResource.toPython()

        if isinstance(temporalResource, BNode) or temporalURI != None:
            startValue = objectValue(graph, temporalResource, dcatURI(u'startDate'))
            endValue = objectValue(graph, temporalResource, dcatURI(u'endDate'))

            startValue = objectValue(graph, temporalResource, schemaURI(u'startDate')) if startValue == None else startValue
            endValue = objectValue(graph, temporalResource, schemaURI(u'endDate')) if endValue == None else endValue

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
    dateValue = graph.value(subject, owlTimeURI(u'inXSDDateTime'))
    dateValue = graph.value(subject, owlTimeURI(u'inXSDDateTimeStamp')) if dateValue == None else dateValue
    dateValue = graph.value(subject, owlTimeURI(u'inXSDDate')) if dateValue == None else dateValue

    if dateValue != None:
        return dateValue.toPython()
    else:
        return None

def extractOwlTimeStart(graph: Graph, subject: URIRef):
    hasBeginning = graph.value(subject, owlTimeURI(u'hasBeginning'))
    if hasBeginning != None:
        return extractOwlTimeInstant(graph, hasBeginning)
    else:
        return None

def extractOwlTimeEnd(graph: Graph, subject: URIRef):
    hasEnd = graph.value(subject, owlTimeURI(u'hasEnd'))
    if hasEnd != None:
        return extractOwlTimeInstant(graph, hasEnd)
    else:
        return None