from rdflib import Graph, URIRef
from rdflib.namespace import RDF, DCTERMS
from dataclasses import dataclass
from typing import List

@dataclass
class Dataset:
    id: str

def parseDatasets(rdfData: str):
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: List = []

    for datasetSubject in datasetsGraph.subjects(predicate=RDF.type, object=URIRef(u'http://www.w3.org/ns/dcat#record')):
        dataset = Dataset(
            id = objectValue(datasetsGraph, datasetSubject, predicate=DCTERMS.identifier)
        )
        datasets.append(dataset)

    return datasets

def objectValue(graph: Graph, subject: URIRef, predicate: URIRef):
    value = graph.value(subject, predicate)
    return value.toPython() if value != None else None