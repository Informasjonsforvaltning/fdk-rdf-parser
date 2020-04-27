from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Distribution
from fdk_rdf_parser.rdf_utils import (
    dcatURI,
    dctURI,
    objectValue,
    resourceList,
    valueList,
    valueTranslations,
)
from .data_distribution_service import extractDataDistributionServices
from .skos_concept import extractSkosConcept


def extractDistributions(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[Distribution]]:
    values = []
    for resource in resourceList(graph, subject, predicate):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()

        values.append(
            Distribution(
                uri=resourceUri,
                title=valueTranslations(graph, resource, DCTERMS.title),
                description=valueTranslations(graph, resource, DCTERMS.description),
                downloadURL=valueList(graph, resource, dcatURI("downloadURL")),
                accessURL=valueList(graph, resource, dcatURI("accessURL")),
                license=extractSkosConcept(graph, resource, DCTERMS.license),
                conformsTo=extractSkosConcept(graph, resource, DCTERMS.conformsTo),
                page=extractSkosConcept(graph, resource, FOAF.page),
                format=valueList(graph, resource, dctURI("format")),
                type=objectValue(graph, resource, DCTERMS.type),
                accessService=extractDataDistributionServices(graph, resource),
            )
        )

    return values if len(values) > 0 else None
