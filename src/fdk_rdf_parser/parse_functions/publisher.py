from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
)

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.rdf_utils import (
    br_uri,
    object_value,
    rov_uri,
    value_translations,
)


def extract_publisher(graph: Graph, subject: URIRef) -> Optional[Publisher]:
    publisher = graph.value(subject, DCTERMS.publisher)
    return parse_publisher(graph, publisher) if publisher else None


def parse_publisher(graph: Graph, publisher: URIRef) -> Publisher:
    org_form = object_value(graph, publisher, rov_uri("orgType"))
    publisher = Publisher(
        uri=publisher.toPython() if isinstance(publisher, URIRef) else None,
        id=object_value(graph, publisher, DCTERMS.identifier),
        name=object_value(graph, publisher, rov_uri("legalName")),
        orgPath=object_value(graph, publisher, br_uri("orgPath")),
        prefLabel=value_translations(graph, publisher, FOAF.name),
        organisasjonsform=org_form.split("#")[-1] if org_form else None,
    )

    return set_publisher_name_from_pref_label_if_missing(publisher)


def extract_list_of_publishers(
    public_services_graph: Graph, public_service_uri: URIRef, predicate: URIRef
) -> Optional[List[Publisher]]:
    publisher_list = list(
        map(
            lambda publisher_uri: parse_publisher(public_services_graph, publisher_uri),
            public_services_graph.objects(public_service_uri, predicate),
        )
    )
    return publisher_list if len(publisher_list) > 0 else None


def set_publisher_name_from_pref_label_if_missing(publisher: Publisher) -> Publisher:
    if publisher.name or publisher.prefLabel is None:
        return publisher
    elif publisher.prefLabel.get("nb"):
        publisher.name = publisher.prefLabel.get("nb")
    elif publisher.prefLabel.get("no"):
        publisher.name = publisher.prefLabel.get("no")
    elif publisher.prefLabel.get("nn"):
        publisher.name = publisher.prefLabel.get("nn")
    elif publisher.prefLabel.get("en"):
        publisher.name = publisher.prefLabel.get("en")

    return publisher
