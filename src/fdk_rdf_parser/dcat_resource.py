from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import RDF, DCTERMS, FOAF

from .rdf_utils import objectValue, valueList, valueTranslations, dcatURI, admsURI, dcatApNoURI

from .contactpoint import ContactPoint, extractContactPoints
from .distribution import Distribution, extractDistributions
from .temporal import Temporal, extractTemporal

@dataclass
class DcatResource:
    identifier: List[str] = field(default_factory=list)
    publisher: str = None
    title: Dict[str, str] = field(default_factory=dict)
    description: Dict[str, str] = field(default_factory=dict)
    uri: str = None
    accessRights: str = None
    theme: List[str] = field(default_factory=list)
    keyword: List[str] = field(default_factory=list)
    contactPoint: List[ContactPoint] = field(default_factory=list)
    type: str = None
    issued: datetime = None
    modified: datetime = None
    landingPage: List[str] = field(default_factory=list)
    language: List[str] = field(default_factory=list)

def parseDcatResource(graph: Graph, subject: URIRef) -> DcatResource:

    return DcatResource(
            identifier = valueList(graph, subject, DCTERMS.identifier),
            publisher = objectValue(graph, subject, DCTERMS.publisher),
            title = valueTranslations(graph, subject, DCTERMS.title),
            description = valueTranslations(graph, subject, DCTERMS.description),
            uri = subject.toPython(),
            accessRights = objectValue(graph, subject, DCTERMS.accessRights),
            theme = valueList(graph, subject, dcatURI(u'theme')),
            keyword = extractKeyWords(graph, subject),
            contactPoint = extractContactPoints(graph, subject),
            type = objectValue(graph, subject, DCTERMS.type),
            issued = objectValue(graph, subject, DCTERMS.issued),
            modified = objectValue(graph, subject, DCTERMS.modified),
            landingPage = valueList(graph, subject, dcatURI(u'landingPage')),
            language = valueList(graph, subject, DCTERMS.language)
        )

def extractKeyWords(graph: Graph, subject: URIRef):
    values = []
    for keyword in graph.objects(subject, dcatURI(u'keyword')):
        translation = {}
        translation[keyword.language] = keyword.toPython()
        values.append(translation)
    return values