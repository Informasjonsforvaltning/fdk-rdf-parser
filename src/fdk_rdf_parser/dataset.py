from dataclasses import dataclass
from typing import Dict

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, DCTERMS, FOAF

from .metadata import HarvestMetaData
from .rdf_utils import objectValue, objectList

@dataclass
class Dataset:
    id: str
    harvest: HarvestMetaData

def parseDatasets(rdfData: str):
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for record in datasetsGraph.subjects(predicate=RDF.type, object=URIRef(u'http://www.w3.org/ns/dcat#record')):
        datasetURI = objectValue(datasetsGraph, record, FOAF.primaryTopic)
        datasets[datasetURI] = Dataset(
            id = objectValue(datasetsGraph, record, predicate=DCTERMS.identifier),
            harvest = HarvestMetaData(
                firstHarvested = objectValue(datasetsGraph, record, DCTERMS.issued),
                changed = objectList(datasetsGraph, record, DCTERMS.modified)
            )
        )

    return datasets
