from dataclasses import dataclass, field
from typing import List
from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from .rdf_utils import objectValue

@dataclass
class Reference:
    referenceType: str = None
    source: str = None

def extractReferences(graph: Graph, subject: URIRef) -> List[Reference]:
    referenceProperties = [
        DCTERMS.hasVersion, DCTERMS.isVersionOf,
        DCTERMS.isPartOf, DCTERMS.hasPart,
        DCTERMS.references, DCTERMS.isReferencedBy,
        DCTERMS.replaces, DCTERMS.isReplacedBy,
        DCTERMS.requires, DCTERMS.isRequiredBy,
        DCTERMS.relation, DCTERMS.source
    ]

    values = []

    for predicate in referenceProperties:
        referenceURI = objectValue(graph, subject, predicate)

        if referenceURI != None:
            values.append(
                Reference(
                    referenceType = predicate.toPython(),
                    source = referenceURI ))

    return values