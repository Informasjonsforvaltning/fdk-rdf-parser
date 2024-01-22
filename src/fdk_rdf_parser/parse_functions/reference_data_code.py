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


def extract_reference_language_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[ReferenceDataCode]]:
    lang_list = []
    ref_list = resource_list(graph, subject, predicate)
    for lang_ref in ref_list:
        lang = ReferenceDataCode(
            uri=lang_ref.toPython() if not isinstance(lang_ref, BNode) else None,
            code=object_value(graph, lang_ref, DC.identifier),
            prefLabel=value_translations(graph, lang_ref, SKOS.prefLabel),
        )
        if lang.uri is not None or lang.code is not None or lang.prefLabel is not None:
            lang_list.append(lang)
    return lang_list if len(lang_list) > 0 else None
