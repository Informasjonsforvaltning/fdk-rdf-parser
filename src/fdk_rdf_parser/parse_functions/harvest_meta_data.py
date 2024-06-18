from rdflib import Graph
from rdflib.namespace import DCTERMS
from rdflib.term import Node

from fdk_rdf_parser.classes import HarvestMetaData
from fdk_rdf_parser.rdf_utils import date_value


def extract_meta_data(graph: Graph, subject: Node) -> HarvestMetaData:
    return HarvestMetaData(
        firstHarvested=date_value(graph, subject, DCTERMS.issued),
        modified=date_value(graph, subject, DCTERMS.modified),
    )
