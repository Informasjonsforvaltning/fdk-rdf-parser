from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Reference, SkosCode, SkosConcept


def extractReferences(graph: Graph, subject: URIRef) -> Optional[List[Reference]]:
    referenceProperties = [
        DCTERMS.hasVersion,
        DCTERMS.isVersionOf,
        DCTERMS.isPartOf,
        DCTERMS.hasPart,
        DCTERMS.references,
        DCTERMS.isReferencedBy,
        DCTERMS.replaces,
        DCTERMS.isReplacedBy,
        DCTERMS.requires,
        DCTERMS.isRequiredBy,
        DCTERMS.relation,
        DCTERMS.source,
    ]

    values = []

    for predicate in referenceProperties:
        referenceURI = graph.value(subject, predicate)

        if referenceURI is not None:
            values.append(
                Reference(
                    referenceType=SkosCode(uri=predicate.toPython()),
                    source=SkosConcept(uri=referenceURI.toPython()),
                )
            )

    return values if len(values) > 0 else None
