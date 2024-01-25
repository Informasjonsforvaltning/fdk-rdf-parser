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


def extract_reference_language_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[ReferenceDataCode]]:
    lang_list = []
    ref_list = resource_list(graph, subject, predicate)
    for lang_ref in ref_list:
        lang_list.append(
            ReferenceDataCode(
                uri=lang_ref.toPython() if not isinstance(lang_ref, BNode) else None,
                code=object_value(graph, lang_ref, DC.identifier),
                prefLabel=value_translations(graph, lang_ref, SKOS.prefLabel),
            )
        )
    return filter_reference_data_code_list(lang_list)


def extract_reference_access_rights(
    graph: Graph, subject: URIRef
) -> Optional[ReferenceDataCode]:
    rights_ref = graph.value(subject, DCTERMS.accessRights)
    if rights_ref:
        rights = ReferenceDataCode(
            uri=rights_ref.toPython() if not isinstance(rights_ref, BNode) else None,
            code=object_value(graph, rights_ref, DC.identifier),
            prefLabel=value_translations(graph, rights_ref, SKOS.prefLabel),
        )
        return filter_reference_data_code(rights)
    else:
        return None
