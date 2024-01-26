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
    at_uri,
    object_value,
    resource_list,
    value_list,
    value_translations,
)


def extract_reference_data_code(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[ReferenceDataCode]:
    uri = object_value(graph, subject, predicate)
    return ReferenceDataCode(uri=uri) if uri is not None else None


def extract_reference_data_code_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[ReferenceDataCode]]:
    ref_data_codes = []
    uri_list = value_list(graph, subject, predicate)
    if uri_list is None:
        return None
    else:
        for uri in uri_list:
            ref_data_codes.append(ReferenceDataCode(uri=uri))
        return ref_data_codes if len(ref_data_codes) > 0 else None


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
