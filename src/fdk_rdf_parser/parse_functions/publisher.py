from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    value_list,
    value_translations,
)


def extract_publisher(
    graph: Graph, subject: URIRef, catalog_subject: URIRef
) -> Optional[Publisher]:
    publisher = graph.value(subject, DCTERMS.publisher)
    publisher = (
        publisher if publisher else graph.value(catalog_subject, DCTERMS.publisher)
    )

    if publisher:
        return Publisher(
            uri=publisher.toPython() if isinstance(publisher, URIRef) else None,
            id=object_value(graph, publisher, DCTERMS.identifier),
            prefLabel=value_translations(graph, publisher, FOAF.name),
        )
    else:
        return None


def extract_authorities_as_publishers(
    public_services_graph: Graph, public_service_uri: URIRef
) -> Optional[List[Publisher]]:
    authorities = value_list(
        public_services_graph, public_service_uri, cv_uri("hasCompetentAuthority")
    )
    if authorities is not None and len(authorities) > 0:
        return list(
            map(
                lambda hasCompetentAuthority: Publisher(uri=hasCompetentAuthority),
                authorities,
            )
        )
    else:
        return None
