from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    SKOS,
)

from fdk_rdf_parser.classes import Subject
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    value_translations,
)


def extract_subjects(graph: Graph, dataset_ref: URIRef) -> Optional[List[Subject]]:
    dataset_subjects = []
    for subject_ref in resource_list(graph, dataset_ref, DCTERMS.subject):
        dataset_subjects.append(
            Subject(
                uri=subject_ref.toPython() if isinstance(subject_ref, URIRef) else None,
                identifier=object_value(graph, subject_ref, DCTERMS.identifier),
                prefLabel=value_translations(graph, subject_ref, SKOS.prefLabel),
                definition=value_translations(graph, subject_ref, SKOS.definition),
            )
        )

    return dataset_subjects if len(dataset_subjects) > 0 else None
