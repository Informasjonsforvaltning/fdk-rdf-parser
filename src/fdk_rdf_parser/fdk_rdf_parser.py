from typing import Dict

from rdflib import Graph
from rdflib.namespace import FOAF, RDF

from .classes import DataService, Dataset, Publisher, QualifiedAttribution
from .organizations import getRdfOrgData, publisherFromFDKOrgCatalog
from .parse_functions import parseDataService, parseDataset
from .rdf_utils import dcatURI, isType
from .reference_data import (
    extendDataServiceWithReferenceData,
    extendDatasetWithReferenceData,
    getDataServiceReferenceData,
    getDatasetReferenceData,
)


def parseDataServices(dataServiceRDF: str) -> Dict[str, DataService]:
    dataServices: Dict[str, DataService] = {}
    fdkOrgs = Graph().parse(data=getRdfOrgData(orgnr=None), format="turtle")
    referenceData = getDataServiceReferenceData()

    dataServicesGraph = Graph().parse(data=dataServiceRDF, format="turtle")

    for recordURI in dataServicesGraph.subjects(
        predicate=RDF.type, object=dcatURI("CatalogRecord")
    ):
        primaryTopicURI = dataServicesGraph.value(recordURI, FOAF.primaryTopic)

        if primaryTopicURI and isType(
            dcatURI("DataService"), dataServicesGraph, primaryTopicURI
        ):
            data_service = parseDataService(
                dataServicesGraph, recordURI, primaryTopicURI
            )

            data_service.publisher = (
                publisherFromFDKOrgCatalog(data_service.publisher, fdkOrgs)
                if data_service.publisher
                else None
            )

            if data_service.catalog and data_service.catalog.publisher:
                data_service.catalog.publisher = publisherFromFDKOrgCatalog(
                    data_service.catalog.publisher, fdkOrgs
                )

            data_service = extendDataServiceWithReferenceData(
                data_service, referenceData
            )

            dataServices[primaryTopicURI.toPython()] = data_service

    return dataServices


def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")
    fdkOrgs = Graph().parse(data=getRdfOrgData(orgnr=None), format="turtle")
    referenceData = getDatasetReferenceData()

    datasets: Dict[str, Dataset] = {}

    for recordURI in datasetsGraph.subjects(
        predicate=RDF.type, object=dcatURI("CatalogRecord")
    ):
        primaryTopicURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
        if primaryTopicURI is not None and isType(
            dcatURI("Dataset"), datasetsGraph, primaryTopicURI
        ):
            partialDataset = parseDataset(datasetsGraph, recordURI, primaryTopicURI)

            dataset = Dataset(
                publisher=publisherFromFDKOrgCatalog(partialDataset.publisher, fdkOrgs)
                if partialDataset.publisher
                else None
            )

            dataset.addValuesFromPartial(values=partialDataset)

            if dataset.catalog and dataset.catalog.publisher:
                dataset.catalog.publisher = publisherFromFDKOrgCatalog(
                    dataset.catalog.publisher, fdkOrgs
                )

            dataset = extendDatasetWithReferenceData(dataset, referenceData)
            dataset = extendDatasetWithOrgsData(dataset, fdkOrgs)

            datasets[primaryTopicURI.toPython()] = dataset

    return datasets


def extendDatasetWithOrgsData(dataset: Dataset, organizationsGraph: Graph) -> Dataset:
    if isinstance(dataset.qualifiedAttributions, list):
        dataset.qualifiedAttributions = list(
            map(
                lambda qa: enhanceQualifiedAttributionAgent(qa, organizationsGraph),
                dataset.qualifiedAttributions,
            )
        )

    return dataset


def enhanceQualifiedAttributionAgent(
    qa: QualifiedAttribution, organizationsGraph: Graph
) -> QualifiedAttribution:
    if isinstance(qa.agent, Publisher):
        publisher = publisherFromFDKOrgCatalog(
            Publisher(id=qa.agent.id, uri=qa.agent.uri,), organizationsGraph
        )

        if isinstance(publisher, Publisher):
            qa.agent = publisher

    return qa
