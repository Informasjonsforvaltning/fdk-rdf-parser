from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Requirement
from fdk_rdf_parser.rdf_utils import (
    cv_uri,
    object_value,
    resource_list,
    value_list,
    value_translations,
)
from .skos_concept import extract_skos_concept


def extract_requirements(graph: Graph, subject: URIRef) -> Optional[List[Requirement]]:
    values = []
    for resource in resource_list(graph, subject, cv_uri("holdsRequirement")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None
        values.append(
            Requirement(
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                dctTitle=value_translations(graph, resource, DCTERMS.title),
                dctType=extract_skos_concept(graph, resource, DCTERMS.type),
                description=value_translations(graph, resource, DCTERMS.description),
                fulfils=value_list(graph, resource, cv_uri("fulfils")),
            )
        )

    return values if len(values) > 0 else None
