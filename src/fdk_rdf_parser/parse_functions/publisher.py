from typing import Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.rdf_utils import objectValue, valueTranslations


def extractPublisher(
    graph: Graph, subject: URIRef, catalog_subject: URIRef
) -> Optional[Publisher]:
    publisher = graph.value(subject, DCTERMS.publisher)
    publisher = (
        publisher if publisher else graph.value(catalog_subject, DCTERMS.publisher)
    )

    if publisher:
        return Publisher(
            uri=publisher.toPython() if isinstance(publisher, URIRef) else None,
            id=objectValue(graph, publisher, DCTERMS.identifier),
            prefLabel=valueTranslations(graph, publisher, FOAF.name),
        )
    else:
        return None
