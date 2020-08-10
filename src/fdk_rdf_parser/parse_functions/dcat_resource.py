import re
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


def parseDcatResource(
    graph: Graph, subject: URIRef, catalog_subject: URIRef
) -> PartialDcatResource:
    formatted_description = valueTranslations(graph, subject, DCTERMS.description)
    return PartialDcatResource(
        identifier=valueList(graph, subject, DCTERMS.identifier),
        publisher=extractPublisher(graph, subject, catalog_subject),
        title=valueTranslations(graph, subject, DCTERMS.title),
        description=description_html_cleaner(formatted_description)
        if formatted_description
        else None,
        descriptionFormatted=formatted_description,
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
        if keyword.language:
            translation[keyword.language] = keyword.toPython()
        else:
            translation["nb"] = keyword.toPython()
        values.append(translation)
    return values if len(values) > 0 else None


def description_html_cleaner(formatted: Dict[str, str]) -> Optional[Dict[str, str]]:
    cleaner_regex = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
    description = {}
    for language in formatted:
        description[language] = re.sub(cleaner_regex, "", formatted[language])

    return description if len(description) > 0 else None
