from typing import Dict

from rdflib import Graph, URIRef

def dcatURI(subString) -> URIRef:
    return URIRef(u'http://www.w3.org/ns/dcat#' + subString)

def admsURI(subString) -> URIRef:
    return URIRef(u'http://www.w3.org/ns/adms#' + subString)

def dcatApNoURI(subString) -> URIRef:
    return URIRef(u'http://difi.no/dcatno#' + subString)

def owlTimeURI(subString) -> URIRef:
    return URIRef(u'https://www.w3.org/TR/owl-time/' + subString)

def schemaURI(subString) -> URIRef:
    return URIRef(u'http://schema.org/' + subString)

def vcardURI(subString) -> URIRef:
    return URIRef(u'http://www.w3.org/2006/vcard/ns#' + subString)

def dctURI(subString) -> URIRef:
    return URIRef(u'http://purl.org/dc/terms/' + subString)

def objectValue(graph: Graph, subject: URIRef, predicate: URIRef):
    value = graph.value(subject, predicate)
    return value.toPython() if value != None else None

def valueList(graph: Graph, subject: URIRef, predicate: URIRef):
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj.toPython())
    values.sort()
    return values

def valueTranslations(graph: Graph, subject: URIRef, predicate: URIRef) -> Dict[str, str]:
    values = {}
    for obj in graph.objects(subject, predicate):
        values[obj.language] = obj.toPython()
    return values

def resourceList(graph: Graph, subject: URIRef, predicate: URIRef):
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj)
    values.sort()
    return values