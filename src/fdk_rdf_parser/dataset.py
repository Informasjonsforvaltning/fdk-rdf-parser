from rdflib import Graph, URIRef
from rdflib.namespace import RDF, DCTERMS
from dataclasses import dataclass
from typing import List
from .metadata import HarvestMetaData

@dataclass
class Dataset:
    id: str
    harvest: HarvestMetaData

def parseDatasets(rdfData: str):
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: List[Dataset] = []

    for record in datasetsGraph.subjects(predicate=RDF.type, object=URIRef(u'http://www.w3.org/ns/dcat#record')):
        datasets.append(Dataset(
            id = objectValue(datasetsGraph, record, predicate=DCTERMS.identifier),
            harvest = HarvestMetaData(
                firstHarvested = objectValue(datasetsGraph, record, DCTERMS.issued)
            )
        ))

    return datasets

def objectValue(graph: Graph, subject: URIRef, predicate: URIRef):
    value = graph.value(subject, predicate)
    return value.toPython() if value != None else None