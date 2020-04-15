from dataclasses import dataclass, field
from typing import Dict, List

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import DCTERMS, FOAF

from .rdf_utils import objectValue, resourceList, valueList, valueTranslations, dcatURI, dctURI

@dataclass
class Distribution:
    uri: str = None
    title: Dict[str, str] = field(default_factory=dict)
    description: Dict[str, str] = field(default_factory=dict)
    downloadURL: List[str] = field(default_factory=list)
    accessURL: List[str] = field(default_factory=list)
    license: str = None
    conformsTo: List[str] = field(default_factory=list)
    page: List[str] = field(default_factory=list)
    format: List[str] = field(default_factory=list)
    type: str = None
    accessService: str = None

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
