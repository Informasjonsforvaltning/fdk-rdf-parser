from datetime import date, datetime
from typing import Any, Dict, List, Optional, Set

from isodate import date_isoformat, datetime_isoformat
from rdflib import BNode, Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF, RDF


def is_type(t: URIRef, graph: Graph, topic: URIRef) -> bool:
    for type_uri_ref in resource_list(graph, topic, RDF.type):
        if type_uri_ref == t:
            return True

    return False


def object_value(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[Any]:
    value = graph.value(subject, predicate)
    return value.toPython() if value and not isinstance(value, BNode) else None


def value_list(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[List[Any]]:
    values = []
    for obj in graph.objects(subject, predicate):
        if not isinstance(obj, BNode):
            values.append(obj.toPython())
    values.sort()
    return values if len(values) > 0 else None


def value_set(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[Set[Any]]:
    values = set()
    for obj in graph.objects(subject, predicate):
        if not isinstance(obj, BNode):
            values.add(obj.toPython())
    return values if len(values) > 0 else None


def value_translations(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[Dict[str, str]]:
    values = {}
    for obj in graph.objects(subject, predicate):
        if obj.language:
            values[obj.language] = obj.toPython()
        else:
            values["nb"] = obj.toPython()
    return values if len(values) > 0 else None


def resource_list(graph: Graph, subject: URIRef, predicate: URIRef) -> List[Any]:
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj)
    values.sort()
    return values


def uri_or_identifier_list(graph: Graph, subjects: List[URIRef]) -> Optional[List[str]]:
    values = []
    for subject_ref in subjects:
        value = uri_or_identifier(graph, subject_ref)
        if value:
            values.append(value)
    values.sort()
    return values if len(values) > 0 else None


def uri_or_identifier(graph: Graph, subject: URIRef) -> Optional[str]:
    return (
        subject.toPython()
        if isinstance(subject, URIRef)
        else object_value(graph, subject, DCTERMS.identifier)
    )


def date_value(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[str]:
    value = graph.value(subject, predicate)
    if value:
        date_object = value.toPython()
        if isinstance(date_object, datetime):
            return datetime_isoformat(date_object)
        elif isinstance(date_object, date):
            return date_isoformat(date_object)
        else:
            return None
    else:
        return None


def date_list(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[List[str]]:
    values = []
    for obj in graph.objects(subject, predicate):
        date_object = obj.toPython()
        if isinstance(date_object, datetime):
            values.append(datetime_isoformat(date_object))
        elif isinstance(date_object, date):
            values.append(date_isoformat(date_object))
    values.sort()
    return values if len(values) > 0 else None


def catalog_ref(graph: Graph, subject: URIRef) -> URIRef:
    catalog_meta_data_ref = graph.value(subject, DCTERMS.isPartOf)
    return graph.value(catalog_meta_data_ref, FOAF.primaryTopic)
