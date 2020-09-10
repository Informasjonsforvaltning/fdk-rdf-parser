from typing import Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Catalog
from fdk_rdf_parser.rdf_utils import dcatURI, isType, objectValue, valueTranslations
from .publisher import extractPublisher


def parseCatalog(graph: Graph, childRecordURI: URIRef) -> Optional[Catalog]:
    catalogRecordURI = graph.value(childRecordURI, DCTERMS.isPartOf)

    if catalogRecordURI and isType(dcatURI("CatalogRecord"), graph, catalogRecordURI):
        catalogURI = graph.value(catalogRecordURI, FOAF.primaryTopic)

        if catalogURI and isType(dcatURI("Catalog"), graph, catalogURI):

            return Catalog(
                id=objectValue(graph, catalogRecordURI, DCTERMS.identifier),
                publisher=extractPublisher(graph, catalogURI, catalogURI),
                title=valueTranslations(graph, catalogURI, DCTERMS.title),
                uri=catalogURI.toPython(),
                description=valueTranslations(graph, catalogURI, DCTERMS.description),
            )
    return None
