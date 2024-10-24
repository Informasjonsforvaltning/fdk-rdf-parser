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
    Graph,
    Literal,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    RDF,
)
from rdflib.term import Node


def node_value(node: Node) -> Optional[str]:
    if isinstance(node, Literal) or isinstance(node, URIRef):
        return node.toPython()
    else:
        return None


def is_type(t: URIRef, graph: Graph, topic: Node) -> bool:
    for type_uri_ref in resource_list(graph, topic, RDF.type):
        if type_uri_ref == t:
            return True

    return False


def has_value_on_predicate(graph: Graph, subject: Node, predicate: URIRef) -> bool:
    return graph.value(subject, predicate) is not None


def has_literal_value_on_predicate(
    graph: Graph, subject: Node, predicate: URIRef
) -> bool:
    value = graph.value(subject, predicate)
    return isinstance(value, Literal)


def object_value(graph: Graph, subject: Node, predicate: URIRef) -> Optional[Any]:
    return node_value(graph.value(subject, predicate))


def duration_string_value(
    graph: Graph, subject: Node, predicate: URIRef
) -> Optional[str]:
    value = graph.value(subject, predicate)
    return (
        str(value)
        if value
        and isinstance(value, Literal)
        and isinstance(value.toPython(), timedelta)
        else None
    )


def object_number_value(
    graph: Graph, subject: Node, predicate: URIRef
) -> Optional[Any]:
    value = graph.value(subject, predicate)
    return (
        value.toPython()
        if isinstance(value, Literal)
        and isinstance(string_to_float(str(value)), numbers.Number)
        else None
    )


def value_list(graph: Graph, subject: Node, predicate: URIRef) -> Optional[List[Any]]:
    values = []
    for obj in graph.objects(subject, predicate):
        value = node_value(obj)
        if value is not None:
            values.append(value)
    values.sort()
    return values if len(values) > 0 else None


def value_set(graph: Graph, subject: Node, predicate: URIRef) -> Optional[Set[Any]]:
    values = set()
    for obj in graph.objects(subject, predicate):
        value = node_value(obj)
        if value is not None:
            values.add(value)
    return values if len(values) > 0 else None


def value_translations(
    graph: Graph, subject: Node, predicate: URIRef
) -> Optional[Dict[str, str]]:
    values = {}
    for obj in graph.objects(subject, predicate):
        if isinstance(obj, Literal) and obj.language:
            values[obj.language] = obj.toPython()
        else:
            values["nb"] = node_value(obj)
    return values if len(values) > 0 else None


def value_translations_list(
    graph: Graph, subject: Node, predicate: URIRef
) -> Optional[List[Dict[str, str]]]:
    values = []
    for obj in graph.objects(subject, predicate):
        value = dict()
        if isinstance(obj, Literal) and obj.language:
            value[obj.language] = obj.toPython()
        else:
            value["nb"] = node_value(obj)
        values.append(value)
    return values if len(values) > 0 else None


def resource_list(graph: Graph, subject: Node, predicate: URIRef) -> List[Any]:
    values = []
    for obj in graph.objects(subject, predicate):
        values.append(obj)
    values.sort()
    return values


def uri_or_identifier_list(graph: Graph, subjects: List[Node]) -> Optional[List[str]]:
    values = []
    for subject_ref in subjects:
        value = uri_or_identifier(graph, subject_ref)
        if value:
            values.append(value)
    values.sort()
    return values if len(values) > 0 else None


def uri_or_identifier(graph: Graph, subject: Node) -> Optional[str]:
    uri = resource_uri_value(subject)
    return uri if uri is not None else object_value(graph, subject, DCTERMS.identifier)


def date_value(graph: Graph, subject: Node, predicate: URIRef) -> Optional[str]:
    value = graph.value(subject, predicate)
    if value:
        date_object = node_value(value)
        if isinstance(date_object, datetime):
            return datetime_isoformat(date_object)
        elif isinstance(date_object, date):
            return date_isoformat(date_object)
        else:
            return None
    else:
        return None


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


def _is_skolem_uri(uri: Optional[str]) -> bool:
    return "/.well-known/skolem/" in uri if uri else False


def resource_uri_value(resource: Optional[Node]) -> Optional[str]:
    uri = node_value(resource) if resource else None
    uri = None if _is_skolem_uri(uri) else uri
    return uri
