from typing import Dict

from rdflib import Graph
from rdflib.namespace import FOAF, RDF

from fdk_rdf_parser.parse_functions.dataset import parseDataset, PartialDataset
from fdk_rdf_parser.rdf_utils import dcatURI


def parseDatasets(rdfData: str) -> Dict[str, PartialDataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, PartialDataset] = {}

    for recordURI in datasetsGraph.subjects(
        predicate=RDF.type, object=dcatURI("record")
    ):
        datasetURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
        if datasetURI is not None:
            datasets[datasetURI.toPython()] = parseDataset(
                datasetsGraph, recordURI, datasetURI
            )

    return datasets
