from typing import List

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Distribution
from fdk_rdf_parser.rdf_utils import objectValue, resourceList, valueList, valueTranslations, dcatURI, dctURI

from .data_distribution_service import extractDataDistributionServices

def extractDistributions(graph: Graph, subject: URIRef) -> List[Distribution]:
    values = []
    for resource in resourceList(graph, subject, dcatURI('distribution')):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()
            
        values.append(
            Distribution(
                uri = resourceUri,
                title = valueTranslations(graph, resource, DCTERMS.title),
                description = valueTranslations(graph, resource, DCTERMS.description),
                downloadURL = valueList(graph, resource, dcatURI('downloadURL')),
                accessURL = valueList(graph, resource, dcatURI('accessURL')),
                license = objectValue(graph, resource, DCTERMS.license),
                conformsTo = valueList(graph, resource, DCTERMS.conformsTo),
                page = valueList(graph, resource, FOAF.page),
                format = valueList(graph, resource, dctURI('format')),
                type = objectValue(graph, resource, DCTERMS.type),
                accessService = extractDataDistributionServices(graph, resource)
            )
        )

    return values if len(values) > 0 else None
