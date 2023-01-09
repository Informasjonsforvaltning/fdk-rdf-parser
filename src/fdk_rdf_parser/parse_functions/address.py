from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import Address
from fdk_rdf_parser.rdf_utils import (
    object_number_value,
    object_value,
    resource_list,
    value_translations,
)
from fdk_rdf_parser.rdf_utils.ns import vcard_uri


def extract_address(graph: Graph, subject: URIRef) -> Optional[List[Address]]:
    values = []
    for resource in resource_list(graph, subject, vcard_uri("hasAddress")):
        values.append(
            Address(
                streetAddress=object_value(
                    graph, resource, vcard_uri("street-address")
                ),
                locality=object_value(graph, resource, vcard_uri("locality")),
                postalCode=object_number_value(
                    graph, resource, vcard_uri("postal-code")
                ),
                countryName=value_translations(
                    graph, resource, vcard_uri("country-name")
                ),
            )
        )

    return values if len(values) > 0 else None
