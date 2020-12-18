from typing import List, Optional

from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import SchemaContactPoint
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
    schema_uri,
    value_translations,
)


def extract_schema_contact_points(
    graph: Graph, subject: URIRef
) -> Optional[List[SchemaContactPoint]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("hasContactPoint")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            SchemaContactPoint(
                uri=resource_uri,
                contactType=value_translations(
                    graph, resource, schema_uri("contactType")
                ),
                description=value_translations(
                    graph, resource, schema_uri("description")
                ),
                email=object_value(graph, resource, schema_uri("email")),
                name=value_translations(graph, resource, schema_uri("name")),
                telephone=object_value(graph, resource, schema_uri("telephone")),
                url=object_value(graph, resource, schema_uri("url")),
            )
        )

    return values if len(values) > 0 else None
