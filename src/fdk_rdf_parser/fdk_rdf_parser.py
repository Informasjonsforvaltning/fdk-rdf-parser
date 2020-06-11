from typing import Dict

from rdflib import Graph
from rdflib.namespace import FOAF, RDF

from .classes import Dataset
from .organizations import getRdfOrgData, publisherFromFDKOrgCatalog
from .parse_functions import parseDataset
from .rdf_utils import dcatURI
from .reference_data import extendDatasetWithReferenceData, getAllReferenceData


def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")
    fdkOrgs = Graph().parse(data=getRdfOrgData(orgnr=None), format="turtle")
    referenceData = getAllReferenceData()

    datasets: Dict[str, Dataset] = {}

    for recordURI in datasetsGraph.subjects(
        predicate=RDF.type, object=dcatURI("record")
    ):
        datasetURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
        if datasetURI is not None:
            partialDataset = parseDataset(datasetsGraph, recordURI, datasetURI)

            dataset = Dataset(
                publisher=publisherFromFDKOrgCatalog(partialDataset.publisher, fdkOrgs)
                if partialDataset.publisher is not None
                else None
            )

            dataset.addValuesFromPartial(values=partialDataset)

            dataset = extendDatasetWithReferenceData(dataset, referenceData)

            datasets[datasetURI.toPython()] = dataset

    return datasets
