from typing import Optional

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
)

from fdk_rdf_parser.classes import Catalog
from fdk_rdf_parser.rdf_utils import (
    dcat_uri,
    is_type,
    object_value,
    value_translations,
)
from .publisher import extract_publisher


def parse_catalog(graph: Graph, child_record_uri: URIRef) -> Optional[Catalog]:
    catalog_record_uri = graph.value(child_record_uri, DCTERMS.isPartOf)

    if catalog_record_uri and is_type(
        dcat_uri("CatalogRecord"), graph, catalog_record_uri
    ):
        catalog_uri = graph.value(catalog_record_uri, FOAF.primaryTopic)

        if catalog_uri and is_type(dcat_uri("Catalog"), graph, catalog_uri):

            return Catalog(
                id=object_value(graph, catalog_record_uri, DCTERMS.identifier),
                publisher=extract_publisher(graph, catalog_uri),
                title=value_translations(graph, catalog_uri, DCTERMS.title),
                uri=catalog_uri.toPython(),
                description=value_translations(graph, catalog_uri, DCTERMS.description),
            )
    return None
