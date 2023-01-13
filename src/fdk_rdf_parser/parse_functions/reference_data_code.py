from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)

from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.rdf_utils import (
    object_value,
    value_list,
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
