from typing import Dict

from rdflib import Graph, URIRef
from rdflib.namespace import FOAF, RDF

from .classes import Dataset
from .organizations import getRdfOrgData, publisherFromFDKOrgCatalog
from .parse_functions import parseDataset
from .rdf_utils import dcatURI, resourceList
from .reference_data import extendDatasetWithReferenceData, getAllReferenceData


def isTypeDataset(graph: Graph, topic: URIRef) -> bool:
    for typeURIRef in resourceList(graph, topic, RDF.type):
        if typeURIRef == dcatURI("Dataset"):
            return True

    return False


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
