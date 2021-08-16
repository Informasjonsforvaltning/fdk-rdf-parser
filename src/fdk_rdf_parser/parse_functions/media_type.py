import logging
from typing import List, Optional

from rdflib import BNode, Graph, URIRef

from fdk_rdf_parser.classes import MediaType


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
