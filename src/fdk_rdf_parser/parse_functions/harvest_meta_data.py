from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import HarvestMetaData
from fdk_rdf_parser.rdf_utils import objectValue, valueList


def extractMetaData(graph: Graph, subject: URIRef) -> HarvestMetaData:
    return HarvestMetaData(
        firstHarvested=objectValue(graph, subject, DCTERMS.issued),
        changed=valueList(graph, subject, DCTERMS.modified),
    )
