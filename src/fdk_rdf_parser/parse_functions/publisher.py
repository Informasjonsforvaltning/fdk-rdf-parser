from typing import Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.rdf_utils import objectValue


def extractPublisher(graph: Graph, subject: URIRef) -> Optional[Publisher]:
    publisherRef = graph.value(subject, DCTERMS.publisher)

    if publisherRef is None:
        return None
    else:
        return Publisher(
            uri=publisherRef.toPython() if isinstance(publisherRef, URIRef) else None,
            id=objectValue(graph, publisherRef, DCTERMS.identifier),
        )
