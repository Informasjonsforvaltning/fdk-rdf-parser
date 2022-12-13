from datetime import (
    date,
    datetime,
    timedelta,
)
import numbers
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
)

from isodate import (
    date_isoformat,
    datetime_isoformat,
)
from rdflib import (
    BNode,
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    RDF,
)


def is_type(t: URIRef, graph: Graph, topic: URIRef) -> bool:
    for type_uri_ref in resource_list(graph, topic, RDF.type):
        if type_uri_ref == t:
            return True

    return False


def is_uri_in_list(
    reference_uri: str, graph: Graph, subject: URIRef, predicate: URIRef
) -> bool:
    return reference_uri in map(
        lambda resource: resource.toPython(), resource_list(graph, subject, predicate)
    )


def object_value(graph: Graph, subject: URIRef, predicate: URIRef) -> Optional[Any]:
    value = graph.value(subject, predicate)
    return value.toPython() if value and not isinstance(value, BNode) else None


def duration_string_value(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[str]:
    value = graph.value(subject, predicate)
    return (
        str(value)
        if value
        and not isinstance(value, BNode)
        and isinstance(value.toPython(), timedelta)
        else None
    )


def object_number_value(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[Any]:
    value = graph.value(subject, predicate)
    return (
        value.toPython()
        if not isinstance(value, BNode)
        and isinstance(string_to_float(str(value)), numbers.Number)
        else None
    )


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


def string_to_float(str_value: str) -> Optional[float]:
    dot_split = str_value.split(".")
    comma_split = str_value.split(",")
    if len(dot_split) == 2 and "," not in dot_split[1]:
        to_convert = str_value.replace(",", "")
    elif len(comma_split) == 2 and "." not in comma_split[1]:
        to_convert = str_value.replace(".", "").replace(",", ".")
    else:
        to_convert = str_value

    try:
        return float(to_convert)
    except ValueError:
        return None


linguistic_system_keywords: Dict[str, str] = {
    "http://publications.europa.eu/resource/authority/language/NOR": "no",
    "http://publications.europa.eu/resource/authority/language/NOB": "nb",
    "http://publications.europa.eu/resource/authority/language/NNO": "nn",
    "http://publications.europa.eu/resource/authority/language/ENG": "en",
}
