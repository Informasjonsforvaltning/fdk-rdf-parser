from typing import Dict
from rdflib import Graph
from rdflib.namespace import RDF, FOAF

from .dataset import Dataset, parseDataset
from .rdf_utils import dcatURI

def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for recordURI in datasetsGraph.subjects(predicate=RDF.type, object=dcatURI(u'record')):
        datasetURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
        if datasetURI != None:
            datasets[datasetURI.toPython()] = parseDataset(datasetsGraph, recordURI, datasetURI)

    return datasets