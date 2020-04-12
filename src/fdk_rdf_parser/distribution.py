from typing import List
from rdflib import Graph, URIRef, BNode
from rdflib.namespace import DCTERMS, FOAF

from .rdf_utils import objectValue, resourceList, valueList, valueTranslations
from .parse_classes import Distribution

def extractDistributions(graph: Graph, subject: URIRef) -> List[Distribution]:
    values = []
    for resource in resourceList(graph, subject, URIRef(u'http://www.w3.org/ns/dcat#distribution')):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()
            
        values.append(
            Distribution(
                uri = resourceUri,
                title = valueTranslations(graph, resource, DCTERMS.title),
                description = valueTranslations(graph, resource, DCTERMS.description),
                downloadURL = valueList(graph, resource, URIRef(u'http://www.w3.org/ns/dcat#downloadURL')),
                accessURL = valueList(graph, resource, URIRef(u'http://www.w3.org/ns/dcat#accessURL')),
                license = objectValue(graph, resource, DCTERMS.license),
                conformsTo = valueList(graph, resource, DCTERMS.conformsTo),
                page = valueList(graph, resource, FOAF.page),
                format = valueList(graph, resource, URIRef(u'http://purl.org/dc/terms/format')),
                type = objectValue(graph, resource, DCTERMS.type),
                accessService = objectValue(graph, resource, URIRef(u'http://www.w3.org/ns/dcat#accessService'))
            )
        )

    return values
