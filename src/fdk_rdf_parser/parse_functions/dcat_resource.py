from typing import Dict, List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import DcatResource
from fdk_rdf_parser.rdf_utils import (
    dcatURI,
    objectValue,
    valueList,
    valueTranslations,
)
from .contactpoint import extractContactPoints
from .publisher import extractPublisher


def parseDcatResource(graph: Graph, subject: URIRef) -> DcatResource:

    return DcatResource(
        identifier=valueList(graph, subject, DCTERMS.identifier),
        publisher=extractPublisher(graph, subject),
        title=valueTranslations(graph, subject, DCTERMS.title),
        description=valueTranslations(graph, subject, DCTERMS.description),
        uri=subject.toPython(),
        accessRights=objectValue(graph, subject, DCTERMS.accessRights),
        theme=valueList(graph, subject, dcatURI("theme")),
        keyword=extractKeyWords(graph, subject),
        contactPoint=extractContactPoints(graph, subject),
        type=objectValue(graph, subject, DCTERMS.type),
        issued=objectValue(graph, subject, DCTERMS.issued),
        modified=objectValue(graph, subject, DCTERMS.modified),
        landingPage=valueList(graph, subject, dcatURI("landingPage")),
        language=valueList(graph, subject, DCTERMS.language),
    )


def extractKeyWords(graph: Graph, subject: URIRef) -> Optional[List[Dict[str, str]]]:
    values = []
    for keyword in graph.objects(subject, dcatURI("keyword")):
        translation = {}
        translation[keyword.language] = keyword.toPython()
        values.append(translation)
    return values if len(values) > 0 else None
