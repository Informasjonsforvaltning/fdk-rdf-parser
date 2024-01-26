from typing import (
    Dict,
    Optional,
)

from rdflib import Graph
from rdflib.namespace import (
    FOAF,
    RDF,
    SKOS,
)

from .classes import (
    Concept,
    DataService,
    Dataset,
    Event,
    InformationModel,
    Service,
)
from .parse_functions import (
    parse_concept,
    parse_cpsvno_service,
    parse_data_service,
    parse_dataset,
    parse_dataset_series,
    parse_event,
    parse_information_model,
)
from .rdf_utils import (
    cpsv_uri,
    cpsvno_uri,
    cv_uri,
    dcat_uri,
    is_type,
    model_dcat_ap_no_uri,
)


def parse_data_services(
    data_service_rdf: str, rdf_format: str = "turtle"
) -> Dict[str, DataService]:
    data_services: Dict[str, DataService] = {}

    data_services_graph = Graph().parse(data=data_service_rdf, format=rdf_format)

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

            data_services[primary_topic_uri.toPython()] = data_service

    return data_services


def parse_datasets(rdf_data: str, rdf_format: str = "turtle") -> Dict[str, Dataset]:
    datasets_graph = Graph().parse(data=rdf_data, format=rdf_format)

    datasets: Dict[str, Dataset] = {}

    for record_uri in datasets_graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = datasets_graph.value(record_uri, FOAF.primaryTopic)
        if primary_topic_uri is not None and (
            is_type(dcat_uri("Dataset"), datasets_graph, primary_topic_uri)
            or is_type(dcat_uri("DatasetSeries"), datasets_graph, primary_topic_uri)
        ):
            partial_dataset = parse_dataset(
                datasets_graph, record_uri, primary_topic_uri
            )

            dataset = Dataset()
            dataset.add_values_from_partial(values=partial_dataset)

            if is_type(dcat_uri("DatasetSeries"), datasets_graph, primary_topic_uri):
                series = parse_dataset_series(datasets_graph, primary_topic_uri)
                series.add_values_from_dataset(values=dataset)
                datasets[primary_topic_uri.toPython()] = series
            else:
                datasets[primary_topic_uri.toPython()] = dataset

    return datasets


def parse_information_models(
    info_models_rdf: str, rdf_format: str = "turtle"
) -> Dict[str, InformationModel]:
    info_models: Dict[str, InformationModel] = {}

    info_models_graph = Graph().parse(data=info_models_rdf, format=rdf_format)

    for record_uri in info_models_graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = info_models_graph.value(record_uri, FOAF.primaryTopic)

        if primary_topic_uri and is_type(
            model_dcat_ap_no_uri("InformationModel"),
            info_models_graph,
            primary_topic_uri,
        ):
            info_model = parse_information_model(
                info_models_graph, record_uri, primary_topic_uri
            )

            info_models[primary_topic_uri.toPython()] = info_model

    return info_models


def parse_public_services(
    public_service_rdf: str, rdf_format: str = "turtle"
) -> Dict[str, Service]:
    cpsvno_services: Dict[str, Service] = {}

    cpsvno_services_graph = Graph().parse(data=public_service_rdf, format=rdf_format)

    for catalog_record_uri in cpsvno_services_graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = cpsvno_services_graph.value(
            catalog_record_uri, FOAF.primaryTopic
        )

        if primary_topic_uri and (
            is_type(
                cpsvno_uri("Service"),
                cpsvno_services_graph,
                primary_topic_uri,
            )
            or is_type(
                cpsv_uri("PublicService"),
                cpsvno_services_graph,
                primary_topic_uri,
            )
        ):
            cpsvno_service = parse_cpsvno_service(
                cpsvno_services_graph, catalog_record_uri, primary_topic_uri
            )

            cpsvno_services[primary_topic_uri.toPython()] = cpsvno_service

    return cpsvno_services


def parse_events(
    event_rdf: str, rdf_format: str = "turtle"
) -> Dict[str, Optional[Event]]:
    events: Dict[str, Optional[Event]] = {}
    graph = Graph().parse(data=event_rdf, format=rdf_format)

    for catalog_record_uri in graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = graph.value(catalog_record_uri, FOAF.primaryTopic)

        if primary_topic_uri and (
            is_type(
                cv_uri("Event"),
                graph,
                primary_topic_uri,
            )
            or is_type(
                cv_uri("BusinessEvent"),
                graph,
                primary_topic_uri,
            )
            or is_type(
                cv_uri("LifeEvent"),
                graph,
                primary_topic_uri,
            )
        ):
            event = parse_event(graph, catalog_record_uri, primary_topic_uri)

            events[primary_topic_uri.toPython()] = event

    return events


def parse_concepts(concepts_rdf: str, rdf_format: str = "turtle") -> Dict[str, Concept]:
    concepts: Dict[str, Concept] = {}
    concepts_graph = Graph().parse(data=concepts_rdf, format=rdf_format)

    for record_uri in concepts_graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = concepts_graph.value(record_uri, FOAF.primaryTopic)

        if primary_topic_uri and is_type(
            SKOS.Concept,
            concepts_graph,
            primary_topic_uri,
        ):
            concept = parse_concept(concepts_graph, record_uri, primary_topic_uri)

            concepts[primary_topic_uri.toPython()] = concept

    return concepts
