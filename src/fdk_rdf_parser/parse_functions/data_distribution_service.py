from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import DataDistributionService
from fdk_rdf_parser.rdf_utils import (
    dcatApiURI,
    resourceList,
    valueTranslations,
)
from .skos_concept import extractSkosConcept


def extractDataDistributionServices(
    graph: Graph, subject: URIRef
) -> Optional[List[DataDistributionService]]:
    values = []
    for resource in resourceList(graph, subject, dcatApiURI("accessService")):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()

        values.append(
            DataDistributionService(
                uri=resourceUri,
                title=valueTranslations(graph, resource, DCTERMS.title),
                description=valueTranslations(graph, resource, DCTERMS.description),
                endpointDescription=extractSkosConcept(
                    graph, resource, dcatApiURI("endpointDescription")
                ),
            )
        )

    return values if len(values) > 0 else None
