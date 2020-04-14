from typing import Dict

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import RDF, DCTERMS, FOAF

from .parse_classes import HarvestMetaData, Dataset, ContactPoint
from .rdf_utils import objectValue, valueList, valueTranslations
from .contactpoint import extractContactPoints
from .distribution import extractDistributions

def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for record in datasetsGraph.subjects(predicate=RDF.type, object=URIRef(u'http://www.w3.org/ns/dcat#record')):
        datasetURI = datasetsGraph.value(record, FOAF.primaryTopic)
        if datasetURI != None:
            datasets[datasetURI.toPython()] = Dataset(
                id = objectValue(datasetsGraph, record, DCTERMS.identifier),
                identifier = objectValue(datasetsGraph, datasetURI, DCTERMS.identifier),
                publisher = objectValue(datasetsGraph, datasetURI, DCTERMS.publisher),
                harvest = HarvestMetaData(
                    firstHarvested = objectValue(datasetsGraph, record, DCTERMS.issued),
                    changed = valueList(datasetsGraph, record, DCTERMS.modified)
                ),
                title = valueTranslations(datasetsGraph, datasetURI, DCTERMS.title),
                description = valueTranslations(datasetsGraph, datasetURI, DCTERMS.description),
                uri = datasetURI.toPython(),
                accessRights = objectValue(datasetsGraph, datasetURI, DCTERMS.accessRights),
                accessRightsComment = objectValue(datasetsGraph, datasetURI, URIRef(u'http://difi.no/dcatno#accessRightsComment')),
                theme = valueList(datasetsGraph, datasetURI, URIRef(u'http://www.w3.org/ns/dcat#theme')),
                keyword = valueList(datasetsGraph, datasetURI, URIRef(u'http://www.w3.org/ns/dcat#keyword')),
                contactPoint = extractContactPoints(datasetsGraph, datasetURI),
                distribution = extractDistributions(datasetsGraph, datasetURI),
                spatial = valueList(datasetsGraph, datasetURI, DCTERMS.spatial)
            )

    return datasets
