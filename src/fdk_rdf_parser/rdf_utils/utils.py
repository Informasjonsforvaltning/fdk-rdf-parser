from datetime import date, datetime
from typing import Any, Dict, List, Optional

from isodate import date_isoformat, datetime_isoformat
from rdflib import BNode, Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF


def objectValue(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[Any]:
    value = graph.value(subject, predicate)
    return value.toPython() if value and not isinstance(value, BNode) else None


def valueList(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[List[Any]]:
    values = []
    for obj in graph.objects(subject, predicate):
        if not isinstance(obj, BNode):
            values.append(obj.toPython())
    values.sort()
    return values if len(values) > 0 else None


def valueTranslations(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[Dict[str, str]]:
    values = {}
    for obj in graph.objects(subject, predicate):
        if obj.language:
            values[obj.language] = obj.toPython()
        else:
            values["nb"] = obj.toPython()
    return values if len(values) > 0 else None


def resourceList(graph: Graph, subject: URIRef, predicate: URIRef) -> List[Any]:
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj)
    values.sort()
    return values


def dateValue(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[str]:
    value = graph.value(subject, predicate)
    if value:
        dateObject = value.toPython()
        if isinstance(dateObject, datetime):
            return datetime_isoformat(dateObject)
        elif isinstance(dateObject, date):
            return date_isoformat(dateObject)
        else:
            return None
    else:
        return None


def dateList(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[List[str]]:
    values = []
    for obj in graph.objects(subject, predicate):
        dateObject = obj.toPython()
        if isinstance(dateObject, datetime):
            values.append(datetime_isoformat(dateObject))
        elif isinstance(dateObject, date):
            values.append(date_isoformat(dateObject))
    values.sort()
    return values if len(values) > 0 else None


def catalogRef(graph: Graph, subject: URIRef) -> URIRef:
    catalog_meta_data_ref = graph.value(subject, DCTERMS.isPartOf)
    return graph.value(catalog_meta_data_ref, FOAF.primaryTopic)
