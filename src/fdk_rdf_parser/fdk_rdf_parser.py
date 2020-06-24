from typing import Dict

from rdflib import Graph, URIRef
from rdflib.namespace import FOAF, RDF

from .classes import DataService, Dataset, Publisher, PublisherId, QualifiedAttribution
from .organizations import getRdfOrgData, publisherFromFDKOrgCatalog
from .parse_functions import parseDataService, parseDataset
from .rdf_utils import dcatURI, resourceList
from .reference_data import extendDatasetWithReferenceData, getAllReferenceData


def isTypeDataset(graph: Graph, topic: URIRef) -> bool:
    for typeURIRef in resourceList(graph, topic, RDF.type):
        if typeURIRef == dcatURI("Dataset"):
            return True

    return False


def parseDataServices(dataServiceRDF: str) -> Dict[str, DataService]:
    dataServices: Dict[str, DataService] = {}

    dataServicesGraph = Graph().parse(data=dataServiceRDF, format="turtle")

    for recordURI in dataServicesGraph.subjects(
        predicate=RDF.type, object=dcatURI("CatalogRecord")
    ):
        primaryTopicURI = dataServicesGraph.value(recordURI, FOAF.primaryTopic)

        for dataServiceURI in resourceList(
            dataServicesGraph, primaryTopicURI, dcatURI("service")
        ):
            dataServices[dataServiceURI.toPython()] = parseDataService(
                dataServicesGraph, dataServiceURI, recordURI
            )

    return dataServices


def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")
    fdkOrgs = Graph().parse(data=getRdfOrgData(orgnr=None), format="turtle")
    referenceData = getAllReferenceData()

    datasets: Dict[str, Dataset] = {}

    for recordURI in datasetsGraph.subjects(
        predicate=RDF.type, object=dcatURI("CatalogRecord")
    ):
        primaryTopicURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
        if primaryTopicURI is not None and isTypeDataset(
            datasetsGraph, primaryTopicURI
        ):
            partialDataset = parseDataset(datasetsGraph, recordURI, primaryTopicURI)

            dataset = Dataset(
                publisher=publisherFromFDKOrgCatalog(partialDataset.publisher, fdkOrgs)
                if partialDataset.publisher is not None
                else None
            )

            dataset.addValuesFromPartial(values=partialDataset)

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
    if isinstance(qa.agent, PublisherId):
        publisher = publisherFromFDKOrgCatalog(
            PublisherId(id=qa.agent.id, uri=qa.agent.uri,), organizationsGraph
        )

        if isinstance(publisher, Publisher):
            qa.agent = publisher

    return qa
