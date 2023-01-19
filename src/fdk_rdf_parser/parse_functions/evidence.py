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
    uri_or_identifier,
    value_translations,
)
from fdk_rdf_parser.rdf_utils.utils import value_list
from .dcat_resource import extract_reference_data_code_list


def parse_evidence(graph: Graph, resource: URIRef) -> Evidence:
    if is_type(cv_uri("Evidence"), graph, resource):
        rdf_type = EvidenceRdfType.EVIDENCE_TYPE.value
    elif is_type(dcat_uri("Dataset"), graph, resource):
        rdf_type = EvidenceRdfType.DATASET_TYPE.value
    else:
        rdf_type = EvidenceRdfType.UNKNOWN.value

    return Evidence(
        rdfType=rdf_type,
        uri=uri_or_identifier(graph, resource),
        identifier=object_value(graph, resource, DCTERMS.identifier),
        name=value_translations(graph, resource, DCTERMS.title),
        description=value_translations(graph, resource, DCTERMS.description),
        dctType=extract_reference_data_code_list(graph, resource, DCTERMS.type),
        language=extract_reference_data_code_list(graph, resource, DCTERMS.language),
        page=value_list(graph, resource, FOAF.page),
    )


def extract_evidences(graph: Graph, subject: URIRef) -> Optional[List[Evidence]]:
    all_resources = resource_list(graph, subject, cpsv_uri("hasInput"))
    for channel in resource_list(graph, subject, cv_uri("hasChannel")):
        all_resources += resource_list(graph, channel, cpsv_uri("hasInput"))

    evidence_dict = dict()
    for resource in all_resources:
        evidence = parse_evidence(graph, resource)
        evidence_dict[evidence.uri] = evidence

    evidence_list = list(evidence_dict.values())
    return evidence_list if len(evidence_list) > 0 else None
