from typing import Dict

from rdflib import Graph
from rdflib.namespace import FOAF, RDF

from .classes import DataService, Dataset, Publisher, QualifiedAttribution
from .organizations import get_rdf_org_data, publisher_from_fdk_org_catalog
from .parse_functions import parse_data_service, parse_dataset
from .rdf_utils import dcat_uri, is_type
from .reference_data import (
    extend_data_service_with_reference_data,
    extend_dataset_with_reference_data,
    get_data_service_reference_data,
    get_dataset_reference_data,
)


def parse_data_services(data_service_rdf: str) -> Dict[str, DataService]:
    data_services: Dict[str, DataService] = {}
    fdk_orgs = Graph().parse(data=get_rdf_org_data(orgnr=None), format="turtle")
    reference_data = get_data_service_reference_data()

    data_services_graph = Graph().parse(data=data_service_rdf, format="turtle")

    for record_uri in data_services_graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = data_services_graph.value(record_uri, FOAF.primaryTopic)

        if primary_topic_uri and is_type(
            dcat_uri("DataService"), data_services_graph, primary_topic_uri
        ):
            data_service = parse_data_service(
                data_services_graph, record_uri, primary_topic_uri
            )

            data_service.publisher = (
                publisher_from_fdk_org_catalog(data_service.publisher, fdk_orgs)
                if data_service.publisher
                else None
            )

            if data_service.catalog and data_service.catalog.publisher:
                data_service.catalog.publisher = publisher_from_fdk_org_catalog(
                    data_service.catalog.publisher, fdk_orgs
                )

            data_service = extend_data_service_with_reference_data(
                data_service, reference_data
            )

            data_services[primary_topic_uri.toPython()] = data_service

    return data_services


def parse_datasets(rdf_data: str) -> Dict[str, Dataset]:
    datasets_graph = Graph().parse(data=rdf_data, format="turtle")
    fdk_orgs = Graph().parse(data=get_rdf_org_data(orgnr=None), format="turtle")
    reference_data = get_dataset_reference_data()

    datasets: Dict[str, Dataset] = {}

    for record_uri in datasets_graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = datasets_graph.value(record_uri, FOAF.primaryTopic)
        if primary_topic_uri is not None and is_type(
            dcat_uri("Dataset"), datasets_graph, primary_topic_uri
        ):
            partial_dataset = parse_dataset(
                datasets_graph, record_uri, primary_topic_uri
            )

            dataset = Dataset(
                publisher=publisher_from_fdk_org_catalog(
                    partial_dataset.publisher, fdk_orgs
                )
                if partial_dataset.publisher
                else None
            )

            dataset.add_values_from_partial(values=partial_dataset)

            if dataset.catalog and dataset.catalog.publisher:
                dataset.catalog.publisher = publisher_from_fdk_org_catalog(
                    dataset.catalog.publisher, fdk_orgs
                )

            dataset = extend_dataset_with_reference_data(dataset, reference_data)
            dataset = extend_dataset_with_orgs_data(dataset, fdk_orgs)

            datasets[primary_topic_uri.toPython()] = dataset

    return datasets


def extend_dataset_with_orgs_data(
    dataset: Dataset, organizations_graph: Graph
) -> Dataset:
    if isinstance(dataset.qualifiedAttributions, list):
        dataset.qualifiedAttributions = list(
            map(
                lambda qa: enhance_qualified_attribution_agent(qa, organizations_graph),
                dataset.qualifiedAttributions,
            )
        )

    return dataset


def enhance_qualified_attribution_agent(
    qa: QualifiedAttribution, organizations_graph: Graph
) -> QualifiedAttribution:
    if isinstance(qa.agent, Publisher):
        publisher = publisher_from_fdk_org_catalog(
            Publisher(id=qa.agent.id, uri=qa.agent.uri,), organizations_graph
        )

        if isinstance(publisher, Publisher):
            qa.agent = publisher

    return qa
