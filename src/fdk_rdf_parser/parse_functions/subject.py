from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, SKOS

from fdk_rdf_parser.classes import Subject
from fdk_rdf_parser.rdf_utils import (
    objectValue,
    resourceList,
    valueTranslations,
)


def extractSubjects(graph: Graph, datasetRef: URIRef) -> Optional[List[Subject]]:
    datasetSubjects = []
    for subjectRef in resourceList(graph, datasetRef, DCTERMS.subject):
        datasetSubjects.append(
            Subject(
                uri=subjectRef.toPython() if isinstance(subjectRef, URIRef) else None,
                identifier=objectValue(graph, subjectRef, DCTERMS.identifier),
                prefLabel=valueTranslations(graph, subjectRef, SKOS.prefLabel),
                definition=valueTranslations(graph, subjectRef, SKOS.definition),
            )
        )

    return datasetSubjects if len(datasetSubjects) > 0 else None
