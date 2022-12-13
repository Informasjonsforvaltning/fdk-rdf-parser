from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import OpeningHoursSpecification
from fdk_rdf_parser.parse_functions.skos_code import extract_skos_code_list
from fdk_rdf_parser.rdf_utils import (
    date_value,
    resource_list,
    schema_uri,
)


def extract_opening_hours_specification(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[OpeningHoursSpecification]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            OpeningHoursSpecification(
                uri=resource_uri,
                dayOfWeek=extract_skos_code_list(
                    graph, resource, schema_uri("dayOfWeek")
                ),
                opens=date_value(graph, resource, schema_uri("opens")),
                closes=date_value(graph, resource, schema_uri("closes")),
                validFrom=date_value(graph, resource, schema_uri("validFrom")),
                validThrough=date_value(graph, resource, schema_uri("validThrough")),
            )
        )

    return values if len(values) > 0 else None
