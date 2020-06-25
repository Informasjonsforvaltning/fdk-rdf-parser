from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import HarvestMetaData
from fdk_rdf_parser.rdf_utils import dateList, dateValue


def extractMetaData(graph: Graph, subject: URIRef) -> HarvestMetaData:
    return HarvestMetaData(
        firstHarvested=dateValue(graph, subject, DCTERMS.issued),
        changed=dateList(graph, subject, DCTERMS.modified),
    )
