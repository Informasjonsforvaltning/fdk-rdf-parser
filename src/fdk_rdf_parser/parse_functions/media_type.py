from typing import (
    List,
    Optional,
)

from rdflib import (
    DC,
    DCTERMS,
    Graph,
    Literal,
    RDF,
    URIRef,
)
from rdflib.term import Node

from fdk_rdf_parser.classes import (
    MediaTypeOrExtent,
    MediaTypeOrExtentType,
)
from fdk_rdf_parser.rdf_utils import (
    dcat_uri,
    dct_uri,
    euvoc_uri,
    object_value,
    resource_uri_value,
)


def extract_fdk_format(
    graph: Graph, subject: URIRef
) -> Optional[List[MediaTypeOrExtent]]:
    fdk_format: List[MediaTypeOrExtent] = list()
    dct_format = extract_media_type_list(graph, subject, dct_uri("format"))
    fdk_format.extend(dct_format if dct_format else [])
    dcat_media_type = extract_media_type_list(graph, subject, dcat_uri("mediaType"))
    fdk_format.extend(dcat_media_type if dcat_media_type else [])

    return fdk_format if len(fdk_format) > 0 else None


def media_type_name(graph: Graph, subject: Node) -> Optional[str]:
    dct_title = object_value(graph, subject, DCTERMS.title)
    if dct_title is not None:
        return dct_title
    else:
        return object_value(graph, subject, DC.identifier)


def media_type_code(graph: Graph, subject: Node) -> Optional[str]:
    dct_identifier = object_value(graph, subject, DCTERMS.identifier)
    if dct_identifier is not None:
        return dct_identifier
    else:
        return object_value(graph, subject, DC.identifier)


def media_type_type(graph: Graph, subject: Node) -> MediaTypeOrExtentType:
    rdf_type = graph.value(subject, RDF.type)
    if rdf_type == DCTERMS.MediaType:
        return MediaTypeOrExtentType.MEDIA_TYPE
    elif rdf_type == euvoc_uri("FileType"):
        return MediaTypeOrExtentType.FILE_TYPE
    else:
        return MediaTypeOrExtentType.UNKNOWN


def extract_media_type(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[MediaTypeOrExtent]:
    value = graph.value(subject, predicate)
    if not value:
        return None
    elif isinstance(value, Literal):
        return MediaTypeOrExtent(code=value.toPython())
    else:
        uri = resource_uri_value(value)
        media_type = MediaTypeOrExtent(
            uri=uri,
            name=media_type_name(graph, value),
            code=media_type_code(graph, value),
            type=media_type_type(graph, value),
        )
        return media_type if media_type_is_valid(media_type) else None


def extract_media_type_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[MediaTypeOrExtent]]:
    media_types = []
    for obj in graph.objects(subject, predicate):
        if isinstance(obj, Literal):
            media_types.append(MediaTypeOrExtent(code=obj.toPython()))
        else:
            uri = resource_uri_value(obj)
            media_type = MediaTypeOrExtent(
                uri=uri,
                name=media_type_name(graph, obj),
                code=media_type_code(graph, obj),
                type=media_type_type(graph, obj),
            )
            if media_type_is_valid(media_type):
                media_types.append(media_type)
    return media_types if len(media_types) > 0 else None


def media_type_is_valid(media_type: MediaTypeOrExtent) -> bool:
    if media_type == MediaTypeOrExtent():
        return False
    else:
        return True
