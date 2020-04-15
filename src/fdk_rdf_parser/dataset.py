from typing import Dict

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import RDF, DCTERMS, FOAF

from .parse_classes import HarvestMetaData, Dataset, ContactPoint
from .rdf_utils import objectValue, valueList, valueTranslations, dcatURI, admsURI, dcatApNoURI
from .contactpoint import extractContactPoints
from .distribution import extractDistributions
from .temporal import extractTemporal

def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for record in datasetsGraph.subjects(predicate=RDF.type, object=dcatURI(u'record')):
        datasetURI = datasetsGraph.value(record, FOAF.primaryTopic)
        if datasetURI != None:
            datasets[datasetURI.toPython()] = Dataset(
                id = objectValue(datasetsGraph, record, DCTERMS.identifier),
                identifier = valueList(datasetsGraph, datasetURI, DCTERMS.identifier),
                admsIdentifier = valueList(datasetsGraph, datasetURI, admsURI(u'identifier')),
                publisher = objectValue(datasetsGraph, datasetURI, DCTERMS.publisher),
                harvest = HarvestMetaData(
                    firstHarvested = objectValue(datasetsGraph, record, DCTERMS.issued),
                    changed = valueList(datasetsGraph, record, DCTERMS.modified)
                ),
                title = valueTranslations(datasetsGraph, datasetURI, DCTERMS.title),
                description = valueTranslations(datasetsGraph, datasetURI, DCTERMS.description),
                uri = datasetURI.toPython(),
                accessRights = objectValue(datasetsGraph, datasetURI, DCTERMS.accessRights),
                accessRightsComment = valueList(datasetsGraph, datasetURI, dcatApNoURI(u'accessRightsComment')),
                theme = valueList(datasetsGraph, datasetURI, dcatURI(u'theme')),
                keyword = valueList(datasetsGraph, datasetURI, dcatURI(u'keyword')),
                contactPoint = extractContactPoints(datasetsGraph, datasetURI),
                distribution = extractDistributions(datasetsGraph, datasetURI),
                spatial = valueList(datasetsGraph, datasetURI, DCTERMS.spatial),
                source = objectValue(datasetsGraph, datasetURI, dcatApNoURI(u'source')),
                objective = valueTranslations(datasetsGraph, datasetURI, dcatApNoURI(u'objective')),
                type = objectValue(datasetsGraph, datasetURI, DCTERMS.type),
                page = valueList(datasetsGraph, datasetURI, FOAF.page),
                issued = objectValue(datasetsGraph, datasetURI, DCTERMS.issued),
                modified = objectValue(datasetsGraph, datasetURI, DCTERMS.modified),
                temporal = extractTemporal(datasetsGraph, datasetURI)
            )

    return datasets
