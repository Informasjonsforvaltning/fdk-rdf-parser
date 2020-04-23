from typing import List

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import DCTERMS, SKOS, RDF

from fdk_rdf_parser.classes import SkosConcept
from fdk_rdf_parser.rdf_utils import (
    objectValue,
    resourceList,
    valueTranslations,
)


def extractExtraType(graph, skosConcept) -> str:
    extraType = None

    for typeURIRef in resourceList(graph, skosConcept, RDF.type):
        if isinstance(typeURIRef, URIRef) and typeURIRef != SKOS.Concept:
            extraType = typeURIRef.toPython()

    return extraType


def extractSkosConcept(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> List[SkosConcept]:
    values = []
    for skosConcept in resourceList(graph, subject, predicate):
        skosConceptUri = None
        if isinstance(skosConcept, URIRef) or isinstance(skosConcept, Literal):
            skosConceptUri = skosConcept.toPython()

        sourceValue = objectValue(graph, skosConcept, DCTERMS.source)

        values.append(
            SkosConcept(
                uri=sourceValue if sourceValue is not None else skosConceptUri,
                prefLabel=valueTranslations(graph, skosConcept, SKOS.prefLabel),
                extraType=extractExtraType(graph, skosConcept),
            )
        )

    return values if len(values) > 0 else None
