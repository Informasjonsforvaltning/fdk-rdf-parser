from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
)

from fdk_rdf_parser.classes import DataService
from fdk_rdf_parser.rdf_utils import (
    dcat_uri,
    object_value,
    value_list,
    value_set,
)
from .catalog import parse_catalog
from .dcat_resource import parse_dcat_resource
from .harvest_meta_data import extract_meta_data
from .media_type import extract_fdk_format
from .skos_code import extract_skos_code_list
from .skos_concept import extract_skos_concept


def parse_data_service(
    data_services_graph: Graph, record_uri: URIRef, data_service_uri: URIRef
) -> DataService:

    data_service = DataService(
        id=object_value(data_services_graph, record_uri, DCTERMS.identifier),
        harvest=extract_meta_data(data_services_graph, record_uri),
        endpointURL=value_set(
            data_services_graph, data_service_uri, dcat_uri("endpointURL")
        ),
        endpointDescription=value_set(
            data_services_graph, data_service_uri, dcat_uri("endpointDescription")
        ),
        mediaType=extract_skos_code_list(
            data_services_graph, data_service_uri, dcat_uri("mediaType")
        ),
        fdkFormat=extract_fdk_format(data_services_graph, data_service_uri),
        conformsTo=extract_skos_concept(
            data_services_graph, data_service_uri, DCTERMS.conformsTo
        ),
        servesDataset=value_set(
            data_services_graph, data_service_uri, dcat_uri("servesDataset")
        ),
        page=value_list(data_services_graph, data_service_uri, FOAF.page),
        catalog=parse_catalog(data_services_graph, record_uri),
    )

    data_service.add_values_from_dcat_resource(
        parse_dcat_resource(
            data_services_graph,
            data_service_uri,
        )
    )
    return data_service
