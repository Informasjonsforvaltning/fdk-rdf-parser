from typing import Any, Dict, List, Optional

from rdflib import Graph, URIRef


def objectValue(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[Any]:
    value = graph.value(subject, predicate)
    return value.toPython() if value is not None else None


def valueList(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[List[Any]]:
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj.toPython())
    values.sort()
    return values if len(values) > 0 else None


def valueTranslations(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[Dict[str, str]]:
    values = {}
    for obj in graph.objects(subject, predicate):
        values[obj.language] = obj.toPython()
    return values if len(values) > 0 else None


def resourceList(graph: Graph, subject: URIRef, predicate: URIRef) -> List[Any]:
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj)
    values.sort()
    return values
