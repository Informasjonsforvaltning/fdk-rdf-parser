from typing import List, Optional

from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import SkosCode
from fdk_rdf_parser.rdf_utils import objectValue, valueList


def extractSkosCode(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[SkosCode]:
    uri = objectValue(graph, subject, predicate)
    return SkosCode(uri=uri) if uri is not None else None


def extractSkosCodeList(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[SkosCode]]:
    skosCodes = []
    uriList = valueList(graph, subject, predicate)
    if uriList is None:
        return None
    else:
        for uri in uriList:
            skosCodes.append(SkosCode(uri=uri))
        return skosCodes if len(skosCodes) > 0 else None
