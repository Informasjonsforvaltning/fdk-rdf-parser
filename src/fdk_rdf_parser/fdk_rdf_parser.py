from functools import reduce
from typing import Dict, List, Optional

from rdflib import Graph
from rdflib.namespace import FOAF, RDF, SKOS

from .classes import (
    Catalog,
    Concept,
    DataService,
    Dataset,
    Event,
    InformationModel,
    PublicService,
    QualifiedAttribution,
)
from .organizations import get_rdf_org_data, publisher_from_fdk_org_catalog
from .parse_functions import (
    extend_with_associated_broader_types,
    parse_concept,
    parse_data_service,
    parse_dataset,
    parse_event,
    parse_information_model,
    parse_public_service,
)
from .rdf_utils import cpsv_uri, cv_uri, dcat_uri, is_type, model_dcat_ap_no_uri
from .reference_data import (
    extend_data_service_with_reference_data,
    extend_dataset_with_reference_data,
    extend_info_model_with_reference_data,
    extend_public_service_with_reference_data,
    get_data_service_reference_data,
    get_dataset_reference_data,
    get_info_model_reference_data,
    get_public_service_reference_data,
)


def parse_data_services(
    data_service_rdf: str, rdf_format: str = "turtle"
) -> Dict[str, DataService]:
    data_services: Dict[str, DataService] = {}
    fdk_orgs = Graph().parse(data=get_rdf_org_data(orgnr=None), format="turtle")
    reference_data = get_data_service_reference_data()

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

            data_service.publisher = (
                publisher_from_fdk_org_catalog(data_service.publisher, fdk_orgs)
                if data_service.publisher
                else None
            )

            data_service.catalog = extend_catalog_with_orgs_data(
                data_service.catalog, fdk_orgs
            )
            data_service = extend_data_service_with_reference_data(
                data_service, reference_data
            )

            data_services[primary_topic_uri.toPython()] = data_service

    return data_services


def parse_datasets(rdf_data: str, rdf_format: str = "turtle") -> Dict[str, Dataset]:
    datasets_graph = Graph().parse(data=rdf_data, format=rdf_format)
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

            dataset = extend_dataset_with_reference_data(dataset, reference_data)
            dataset = extend_dataset_with_orgs_data(dataset, fdk_orgs)
            dataset.catalog = extend_catalog_with_orgs_data(dataset.catalog, fdk_orgs)

            datasets[primary_topic_uri.toPython()] = dataset

    return datasets


def parse_information_models(
    info_models_rdf: str, rdf_format: str = "turtle"
) -> Dict[str, InformationModel]:
    info_models: Dict[str, InformationModel] = {}
    fdk_orgs = Graph().parse(data=get_rdf_org_data(orgnr=None), format="turtle")
    reference_data = get_info_model_reference_data()

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

            info_model.publisher = (
                publisher_from_fdk_org_catalog(info_model.publisher, fdk_orgs)
                if info_model.publisher
                else None
            )

            info_model.catalog = extend_catalog_with_orgs_data(
                info_model.catalog, fdk_orgs
            )
            info_model = extend_info_model_with_reference_data(
                info_model, reference_data
            )

            info_models[primary_topic_uri.toPython()] = info_model

    return info_models


def parse_public_services(
    public_service_rdf: str, event_rdf: str = None, rdf_format: str = "turtle"
) -> Dict[str, PublicService]:
    public_services: Dict[str, PublicService] = {}
    fdk_orgs = Graph().parse(data=get_rdf_org_data(orgnr=None), format=rdf_format)
    reference_data = get_public_service_reference_data()

    events: Dict[str, Optional[Event]] = (
        parse_events(event_rdf) if event_rdf is not None else {}
    )

    public_services_graph = Graph().parse(data=public_service_rdf, format=rdf_format)

    for catalog_record_uri in public_services_graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = public_services_graph.value(
            catalog_record_uri, FOAF.primaryTopic
        )

        if primary_topic_uri and is_type(
            cpsv_uri("PublicService"),
            public_services_graph,
            primary_topic_uri,
        ):
            public_service = parse_public_service(
                public_services_graph, catalog_record_uri, primary_topic_uri
            )

            if (
                public_service.hasCompetentAuthority is not None
                and len(public_service.hasCompetentAuthority) > 0
            ):
                public_service.hasCompetentAuthority = list(
                    filter(
                        None,
                        map(
                            lambda authority: publisher_from_fdk_org_catalog(
                                authority, fdk_orgs
                            ),
                            public_service.hasCompetentAuthority,
                        ),
                    )
                )

            if public_service.hasCost is not None and len(public_service.hasCost) > 0:
                costs = []
                for cost in public_service.hasCost:
                    if cost.isDefinedBy is not None and len(cost.isDefinedBy) > 0:
                        cost.isDefinedBy = list(
                            filter(
                                None,
                                map(
                                    lambda isDefinedBy: publisher_from_fdk_org_catalog(
                                        isDefinedBy, fdk_orgs
                                    ),
                                    cost.isDefinedBy,
                                ),
                            )
                        )
                    costs.append(cost)
                public_service.hasCost = costs

            if (
                public_service.isGroupedBy is not None
                and len(public_service.isGroupedBy) > 0
            ):
                associated_skos_concepts_uris: List[str] = []
                reduce(
                    lambda output, current_event_uri: extend_with_associated_broader_types(
                        events, current_event_uri, output
                    ),
                    public_service.isGroupedBy,
                    associated_skos_concepts_uris,
                )
                public_service.associatedBroaderTypesByEvents = (
                    associated_skos_concepts_uris
                    if associated_skos_concepts_uris
                    and len(associated_skos_concepts_uris) > 0
                    else None
                )

            public_service = extend_public_service_with_reference_data(
                public_service, reference_data
            )

            public_services[primary_topic_uri.toPython()] = public_service

    return public_services


def parse_events(
    event_rdf: str, rdf_format: str = "turtle"
) -> Dict[str, Optional[Event]]:
    events: Dict[str, Optional[Event]] = {}

    fdk_orgs = Graph().parse(data=get_rdf_org_data(orgnr=None), format=rdf_format)
    graph = Graph().parse(data=event_rdf, format=rdf_format)

    for catalog_record_uri in graph.subjects(
        predicate=RDF.type, object=dcat_uri("CatalogRecord")
    ):
        primary_topic_uri = graph.value(catalog_record_uri, FOAF.primaryTopic)

        if primary_topic_uri and (
            is_type(
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

            if (
                event
                and event.hasCompetentAuthority is not None
                and len(event.hasCompetentAuthority) > 0
            ):
                event.hasCompetentAuthority = list(
                    filter(
                        None,
                        map(
                            lambda authority: publisher_from_fdk_org_catalog(
                                authority, fdk_orgs
                            ),
                            event.hasCompetentAuthority,
                        ),
                    )
                )

            events[primary_topic_uri.toPython()] = event

    return events


def parse_concepts(concepts_rdf: str, rdf_format: str = "turtle") -> Dict[str, Concept]:
    concepts: Dict[str, Concept] = {}
    fdk_orgs = Graph().parse(data=get_rdf_org_data(orgnr=None), format="turtle")

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

            concept.publisher = publisher_from_fdk_org_catalog(
                concept.publisher, fdk_orgs
            )
            if concept.collection:
                concept.collection.publisher = publisher_from_fdk_org_catalog(
                    concept.collection.publisher, fdk_orgs
                )

            concepts[primary_topic_uri.toPython()] = concept

    return concepts


def extend_catalog_with_orgs_data(
    catalog: Optional[Catalog], organizations_graph: Graph
) -> Optional[Catalog]:
    if catalog:
        catalog.publisher = publisher_from_fdk_org_catalog(
            catalog.publisher, organizations_graph
        )
    return catalog


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
    qa.agent = publisher_from_fdk_org_catalog(qa.agent, organizations_graph)

    return qa
