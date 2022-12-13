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


def extract_skos_code(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[ReferenceDataCode]:
    uri = object_value(graph, subject, predicate)
    return ReferenceDataCode(uri=uri) if uri is not None else None


def extract_skos_code_list(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[ReferenceDataCode]]:
    skos_codes = []
    uri_list = value_list(graph, subject, predicate)
    if uri_list is None:
        return None
    else:
        for uri in uri_list:
            skos_codes.append(ReferenceDataCode(uri=uri))
        return skos_codes if len(skos_codes) > 0 else None
