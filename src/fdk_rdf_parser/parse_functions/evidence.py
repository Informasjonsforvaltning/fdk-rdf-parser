from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    FOAF,
)

from fdk_rdf_parser.classes.evidence import (
    Evidence,
    EvidenceRdfType,
)
from fdk_rdf_parser.rdf_utils import (
    cpsv_uri,
    cv_uri,
    dcat_uri,
    is_type,
    object_value,
    resource_list,
    value_translations,
)
from fdk_rdf_parser.rdf_utils.utils import value_list
from .dcat_resource import extract_skos_code_list


def extract_evidences(graph: Graph, subject: URIRef) -> Optional[List[Evidence]]:
    values = []
    for resource in resource_list(graph, subject, cpsv_uri("hasInput")):
        resource_uri = resource.toPython() if isinstance(resource, URIRef) else None

        if is_type(cv_uri("Evidence"), graph, resource):
            rdf_type = EvidenceRdfType.EVIDENCE_TYPE.value
        elif is_type(dcat_uri("Dataset"), graph, resource):
            rdf_type = EvidenceRdfType.DATASET_TYPE.value
        else:
            rdf_type = EvidenceRdfType.UNKNOWN.value

        values.append(
            Evidence(
                rdfType=rdf_type,
                uri=resource_uri,
                identifier=object_value(graph, resource, DCTERMS.identifier),
                name=value_translations(graph, resource, DCTERMS.title),
                description=value_translations(graph, resource, DCTERMS.description),
                dctType=extract_skos_code_list(graph, resource, DCTERMS.type),
                language=extract_skos_code_list(graph, resource, DCTERMS.language),
                page=value_list(graph, resource, FOAF.page),
            )
        )

    return values if len(values) > 0 else None
