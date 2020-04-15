from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from .rdf_utils import objectValue, valueList
from .temporal import Temporal

@dataclass
class HarvestMetaData:
    firstHarvested: datetime
    changed: List[str] = field(default_factory=list)

def extractMetaData(graph: Graph, subject: URIRef) -> List[HarvestMetaData]:
    return HarvestMetaData(
        firstHarvested = objectValue(graph, subject, DCTERMS.issued),
        changed = valueList(graph, subject, DCTERMS.modified)
    )
