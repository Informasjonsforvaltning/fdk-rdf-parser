from typing import Dict

from rdflib import Graph, URIRef
from rdflib.namespace import FOAF, RDF

from fdk_rdf_parser.parse_functions import parseDataService, parseDataset
from fdk_rdf_parser.rdf_utils import dcatURI
from .classes import DataService, Dataset
from .organizations import getRdfOrgData, publisherFromFDKOrgCatalog
from .rdf_utils import resourceList
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

            datasets[primaryTopicURI.toPython()] = dataset

    return datasets
