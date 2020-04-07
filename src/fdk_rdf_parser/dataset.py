from typing import Dict

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, DCTERMS, FOAF

from .parse_classes import HarvestMetaData, Dataset
from .rdf_utils import objectValue, valueList, valueTranslations

def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for record in datasetsGraph.subjects(predicate=RDF.type, object=URIRef(u'http://www.w3.org/ns/dcat#record')):
        datasetURI = datasetsGraph.value(record, FOAF.primaryTopic)
        if datasetURI != None:
            datasets[datasetURI.toPython()] = Dataset(
                id = objectValue(datasetsGraph, record, predicate=DCTERMS.identifier),
                harvest = HarvestMetaData(
                    firstHarvested = objectValue(datasetsGraph, record, DCTERMS.issued),
                    changed = valueList(datasetsGraph, record, DCTERMS.modified)
                ),
                title = valueTranslations(datasetsGraph, datasetURI, DCTERMS.title),
                description = valueTranslations(datasetsGraph, datasetURI, DCTERMS.description),
                uri=datasetURI.toPython()
            )

    return datasets
