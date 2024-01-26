from typing import (
    List,
    Optional,
)

from rdflib import (
    BNode,
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DC,
    DCTERMS,
    SKOS,
)

from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.rdf_utils import (
    adms_uri,
    at_uri,
    cv_uri,
    object_value,
    resource_list,
    value_translations,
)


def filter_reference_data_code_list(
    code_list: List[ReferenceDataCode],
) -> Optional[List[ReferenceDataCode]]:
    non_empty_list = []
    for code in code_list:
        if code.uri is not None or code.code is not None or code.prefLabel is not None:
            non_empty_list.append(code)
    return non_empty_list if len(non_empty_list) > 0 else None


def filter_reference_data_code(
    code: ReferenceDataCode,
) -> Optional[ReferenceDataCode]:
    if code.uri is not None or code.code is not None or code.prefLabel is not None:
        return code
    else:
        return None


def parse_reference_code(
    graph: Graph, code_ref: URIRef, code_predicate: URIRef, label_predicate: URIRef
) -> ReferenceDataCode:
    return ReferenceDataCode(
        uri=code_ref.toPython() if not isinstance(code_ref, BNode) else None,
        code=object_value(graph, code_ref, code_predicate),
        prefLabel=value_translations(graph, code_ref, label_predicate),
    )


def extract_reference_language_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[ReferenceDataCode]]:
    lang_list = []
    ref_list = resource_list(graph, subject, predicate)
    for lang_ref in ref_list:
        lang_list.append(
            parse_reference_code(
                graph, lang_ref, at_uri("authority-code"), SKOS.prefLabel
            )
        )
    return filter_reference_data_code_list(lang_list)


def extract_reference_language_code(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[ReferenceDataCode]:
    lang_ref = graph.value(subject, predicate)
    if lang_ref:
        return filter_reference_data_code(
            parse_reference_code(graph, lang_ref, DC.identifier, SKOS.prefLabel)
        )
    else:
        return None


def extract_reference_access_rights(
    graph: Graph, subject: URIRef
) -> Optional[ReferenceDataCode]:
    rights_ref = graph.value(subject, DCTERMS.accessRights)
    if rights_ref:
        rights = parse_reference_code(graph, rights_ref, DC.identifier, SKOS.prefLabel)
        return filter_reference_data_code(rights)
    else:
        return None


def extract_reference_frequency(
    graph: Graph, subject: URIRef
) -> Optional[ReferenceDataCode]:
    freq_ref = graph.value(subject, DCTERMS.accrualPeriodicity)
    if freq_ref:
        frequency = parse_reference_code(graph, freq_ref, DC.identifier, SKOS.prefLabel)
        return filter_reference_data_code(frequency)
    else:
        return None


def extract_reference_provenance(
    graph: Graph, subject: URIRef
) -> Optional[ReferenceDataCode]:
    prov_ref = graph.value(subject, DCTERMS.provenance)
    if prov_ref:
        provenance = parse_reference_code(
            graph, prov_ref, at_uri("authority-code"), SKOS.prefLabel
        )
        return filter_reference_data_code(provenance)
    else:
        return None


def extract_reference_adms_status(
    graph: Graph, subject: URIRef
) -> Optional[ReferenceDataCode]:
    status_ref = graph.value(subject, adms_uri("status"))
    if status_ref:
        status = parse_reference_code(graph, status_ref, SKOS.notation, SKOS.prefLabel)
        return filter_reference_data_code(status)
    else:
        return None


def extract_reference_evidence_types(
    graph: Graph, subject: URIRef
) -> Optional[List[ReferenceDataCode]]:
    evidence_list = []
    ref_list = resource_list(graph, subject, DCTERMS.type)
    for evidence_ref in ref_list:
        evidence = parse_reference_code(
            graph, evidence_ref, DCTERMS.identifier, SKOS.prefLabel
        )
        evidence.code = evidence.code.split("#")[-1] if evidence.code else None
        evidence_list.append(evidence)
    return filter_reference_data_code_list(evidence_list)


def extract_reference_role_types(
    graph: Graph, subject: URIRef
) -> Optional[List[ReferenceDataCode]]:
    role_list = []
    ref_list = resource_list(graph, subject, cv_uri("role"))
    for role_ref in ref_list:
        role = parse_reference_code(graph, role_ref, DCTERMS.identifier, SKOS.prefLabel)
        role.code = role.code.split("#")[-1] if role.code else None
        role_list.append(role)
    return filter_reference_data_code_list(role_list)


def extract_reference_channel_type(
    graph: Graph, subject: URIRef
) -> Optional[ReferenceDataCode]:
    channel_ref = graph.value(subject, DCTERMS.type)
    if channel_ref:
        channel = parse_reference_code(
            graph, channel_ref, DCTERMS.identifier, SKOS.prefLabel
        )
        channel.code = channel.code.split("#")[-1] if channel.code else None
        return filter_reference_data_code(channel)
    else:
        return None


def extract_reference_publisher_type(
    graph: Graph, subject: URIRef
) -> Optional[ReferenceDataCode]:
    publisher_type_ref = graph.value(subject, DCTERMS.type)
    if publisher_type_ref:
        return filter_reference_data_code(
            parse_reference_code(
                graph, publisher_type_ref, SKOS.notation, SKOS.prefLabel
            )
        )
    else:
        return None


def extract_reference_main_activities(
    graph: Graph, subject: URIRef
) -> Optional[List[ReferenceDataCode]]:
    activities = []
    ref_list = resource_list(graph, subject, DCTERMS.type)
    for activity_ref in ref_list:
        activity = parse_reference_code(
            graph, activity_ref, DC.identifier, SKOS.prefLabel
        )
        activities.append(activity)
    return filter_reference_data_code_list(activities)
