from typing import List

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Distribution
from fdk_rdf_parser.rdf_utils import objectValue, resourceList, valueList, valueTranslations, dcatURI, dctURI

def extractDistributions(graph: Graph, subject: URIRef) -> List[Distribution]:
    values = []
    for resource in resourceList(graph, subject, dcatURI(u'distribution')):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()
            
        values.append(
            Distribution(
                uri = resourceUri,
                title = valueTranslations(graph, resource, DCTERMS.title),
                description = valueTranslations(graph, resource, DCTERMS.description),
                downloadURL = valueList(graph, resource, dcatURI(u'downloadURL')),
                accessURL = valueList(graph, resource, dcatURI(u'accessURL')),
                license = objectValue(graph, resource, DCTERMS.license),
                conformsTo = valueList(graph, resource, DCTERMS.conformsTo),
                page = valueList(graph, resource, FOAF.page),
                format = valueList(graph, resource, dctURI(u'format')),
                type = objectValue(graph, resource, DCTERMS.type),
                accessService = objectValue(graph, resource, dcatURI(u'accessService'))
            )
        )

    return values
