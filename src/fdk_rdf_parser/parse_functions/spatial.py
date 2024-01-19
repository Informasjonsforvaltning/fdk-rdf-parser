from typing import (
    List,
    Optional,
)

from rdflib import (
    BNode,
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import ReferenceDataCode
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    value_translations,
)


def extract_dct_spatial_list(
    graph: Graph, subject: URIRef
) -> Optional[List[ReferenceDataCode]]:
    spatial_list = []
    ref_list = resource_list(graph, subject, DCTERMS.spatial)
    for spatial_ref in ref_list:
        spatial = ReferenceDataCode(
            uri=spatial_ref.toPython() if not isinstance(spatial_ref, BNode) else None,
            code=object_value(graph, spatial_ref, DCTERMS.identifier),
            prefLabel=value_translations(graph, spatial_ref, DCTERMS.title),
        )
        if (
            spatial.uri is not None
            or spatial.code is not None
            or spatial.prefLabel is not None
        ):
            spatial_list.append(spatial)
    return spatial_list if len(spatial_list) > 0 else None
