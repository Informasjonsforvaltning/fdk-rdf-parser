from typing import Dict
from rdflib import Graph
from rdflib.namespace import RDF, FOAF

from fdk_rdf_parser.parse_functions.dataset import Dataset, parseDataset
from fdk_rdf_parser.rdf_utils import dcatURI

def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for recordURI in datasetsGraph.subjects(predicate=RDF.type, object=dcatURI('record')):
        datasetURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
        if datasetURI != None:
            datasets[datasetURI.toPython()] = parseDataset(datasetsGraph, recordURI, datasetURI)

    return datasets