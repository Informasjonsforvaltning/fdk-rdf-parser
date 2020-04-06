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

    for subject in datasetsGraph.subjects(predicate=RDF.type, object=URIRef(u'http://www.w3.org/ns/dcat#record')):
        dataset = Dataset(
            id = datasetsGraph.value(subject, predicate=DCTERMS.identifier).toPython()
        )
        datasets.append(dataset)

    return datasets