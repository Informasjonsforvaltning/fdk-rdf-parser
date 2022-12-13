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

from fdk_rdf_parser.classes import Distribution
from fdk_rdf_parser.rdf_utils import (
    dcat_uri,
    dct_uri,
    object_value,
    resource_list,
    value_set,
    value_translations,
)
from .conforms_to import extract_conforms_to
from .data_distribution_service import extract_data_distribution_services
from .media_type import (
    extract_fdk_format,
    extract_media_type,
)
from .skos_concept import extract_skos_concept


def extract_distributions(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Distribution]]:
    values = []
    for resource in resource_list(graph, subject, predicate):
        resource_uri = None
        if isinstance(resource, URIRef):
            resource_uri = resource.toPython()

        values.append(
            Distribution(
                uri=resource_uri,
                title=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                downloadURL=value_set(graph, resource, dcat_uri("downloadURL")),
                accessURL=value_set(graph, resource, dcat_uri("accessURL")),
                license=extract_skos_concept(graph, resource, DCTERMS.license),
                conformsTo=extract_conforms_to(graph, resource),
                page=extract_skos_concept(graph, resource, FOAF.page),
                format=value_set(graph, resource, dct_uri("format")),
                fdkFormat=extract_fdk_format(graph, resource),
                compressFormat=extract_media_type(
                    graph, resource, dcat_uri("compressFormat")
                ),
                packageFormat=extract_media_type(
                    graph, resource, dcat_uri("packageFormat")
                ),
                type=object_value(graph, resource, DCTERMS.type),
                accessService=extract_data_distribution_services(graph, resource),
            )
        )

    return values if len(values) > 0 else None
