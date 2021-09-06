import logging
from typing import List, Optional

from rdflib import BNode, Graph, URIRef

from fdk_rdf_parser.classes import MediaType
from fdk_rdf_parser.rdf_utils import dcat_uri, dct_uri


def extract_fdk_format(graph: Graph, subject: URIRef) -> Optional[List[MediaType]]:
    fdk_format: List[MediaType] = list()
    dct_format = extract_media_type_list(graph, subject, dct_uri("format"))
    fdk_format.extend(dct_format if dct_format else [])
    dcat_media_type = extract_media_type_list(graph, subject, dcat_uri("mediaType"))
    fdk_format.extend(dcat_media_type if dcat_media_type else [])

    return fdk_format if len(fdk_format) > 0 else None


def extract_media_type(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[MediaType]:
    value = graph.value(subject, predicate)
    if not value or isinstance(value, BNode):
        logging.error(
            f"Unable to parse {predicate.toPython()} for {subject.toPython()}"
        )
        return None
    elif isinstance(value, URIRef):
        return MediaType(uri=value.toPython())
    else:
        return MediaType(code=value.toPython())


def extract_media_type_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[MediaType]]:
    media_types = []
    for obj in graph.objects(subject, predicate):
        if isinstance(obj, BNode):
            logging.error(
                f"Unable to parse {predicate.toPython()} for {subject.toPython()}"
            )
        elif isinstance(obj, URIRef):
            media_types.append(MediaType(uri=obj.toPython()))
        else:
            media_types.append(MediaType(code=obj.toPython()))
    return media_types if len(media_types) > 0 else None
