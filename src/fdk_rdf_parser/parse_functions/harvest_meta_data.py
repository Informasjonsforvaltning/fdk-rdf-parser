from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import HarvestMetaData
from fdk_rdf_parser.rdf_utils import (
    date_list,
    date_value,
)


def extract_meta_data(graph: Graph, subject: URIRef) -> HarvestMetaData:
    return HarvestMetaData(
        firstHarvested=date_value(graph, subject, DCTERMS.issued),
        changed=date_list(graph, subject, DCTERMS.modified),
    )
