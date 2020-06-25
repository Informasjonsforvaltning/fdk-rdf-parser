from typing import Dict, List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import PartialDcatResource, ThemeEU
from fdk_rdf_parser.rdf_utils import (
    dateValue,
    dcatURI,
    objectValue,
    valueList,
    valueTranslations,
)
from .contactpoint import extractContactPoints
from .publisher import extractPublisher
from .skos_code import extractSkosCode, extractSkosCodeList


def parseDcatResource(graph: Graph, subject: URIRef) -> PartialDcatResource:
    return PartialDcatResource(
        identifier=valueList(graph, subject, DCTERMS.identifier),
        publisher=extractPublisher(graph, subject),
        title=valueTranslations(graph, subject, DCTERMS.title),
        description=valueTranslations(graph, subject, DCTERMS.description),
        uri=subject.toPython(),
        accessRights=extractSkosCode(graph, subject, DCTERMS.accessRights),
        theme=extractThemes(graph, subject),
        keyword=extractKeyWords(graph, subject),
        contactPoint=extractContactPoints(graph, subject),
        type=objectValue(graph, subject, DCTERMS.type),
        issued=dateValue(graph, subject, DCTERMS.issued),
        modified=dateValue(graph, subject, DCTERMS.modified),
        landingPage=valueList(graph, subject, dcatURI("landingPage")),
        language=extractSkosCodeList(graph, subject, DCTERMS.language),
    )


def extractThemes(graph: Graph, subject: URIRef) -> Optional[List[ThemeEU]]:
    themes = valueList(graph, subject, dcatURI("theme"))
    if themes is not None and len(themes) > 0:
        return list(map(lambda themeURI: ThemeEU(id=themeURI), themes))
    else:
        return None


def extractKeyWords(graph: Graph, subject: URIRef) -> Optional[List[Dict[str, str]]]:
    values = []
    for keyword in graph.objects(subject, dcatURI("keyword")):
        translation = {}
        translation[keyword.language] = keyword.toPython()
        values.append(translation)
    return values if len(values) > 0 else None
