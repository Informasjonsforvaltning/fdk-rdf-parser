from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Channel
from fdk_rdf_parser.parse_functions.address import extract_address
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
)
from fdk_rdf_parser.rdf_utils.ns import (
    cpsv_uri,
    cv_uri,
    vcard_uri,
)
from fdk_rdf_parser.rdf_utils.utils import (
    duration_string_value,
    resource_uri_value,
    value_list,
    value_translations,
)
from .reference_data_code import extract_reference_channel_type


def extract_channels(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Channel]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        values.append(
            Channel(
                uri=resource_uri_value(resource),
                identifier=object_value(graph, resource, DCTERMS.identifier),
                channelType=extract_reference_channel_type(graph, resource),
                description=value_translations(graph, resource, DCTERMS.description),
                address=extract_address(graph, resource),
                processingTime=duration_string_value(
                    graph, resource, cv_uri("processingTime")
                ),
                hasInput=value_list(graph, resource, cpsv_uri("hasInput")),
                email=value_list(graph, resource, vcard_uri("hasEmail")),
                url=value_list(graph, resource, vcard_uri("hasURL")),
                telephone=value_list(graph, resource, vcard_uri("hasTelephone")),
            )
        )

    return values if len(values) > 0 else None
