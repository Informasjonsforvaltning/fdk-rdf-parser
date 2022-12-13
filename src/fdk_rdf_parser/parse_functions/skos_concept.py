from typing import (
    Any,
    List,
    Optional,
)

from rdflib import (
    Graph,
    Literal,
    URIRef,
)
from rdflib.namespace import (
    DCTERMS,
    RDF,
    SKOS,
)

from fdk_rdf_parser.classes import SkosConcept
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    value_list,
    value_translations,
)


def extract_extra_type(graph: Graph, skos_concept: Any) -> Optional[str]:
    extra_type = None

    for type_uri_ref in resource_list(graph, skos_concept, RDF.type):
        if isinstance(type_uri_ref, URIRef) and type_uri_ref != SKOS.Concept:
            extra_type = type_uri_ref.toPython()

    return extra_type


def extract_skos_concept(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[SkosConcept]]:
    values = []
    for skos_concept in resource_list(graph, subject, predicate):
        skos_concept_uri = None
        if isinstance(skos_concept, URIRef) or isinstance(skos_concept, Literal):
            skos_concept_uri = skos_concept.toPython()

        source_value = object_value(graph, skos_concept, DCTERMS.source)

        values.append(
            SkosConcept(
                uri=source_value if source_value is not None else skos_concept_uri,
                prefLabel=value_translations(graph, skos_concept, SKOS.prefLabel),
                extraType=extract_extra_type(graph, skos_concept),
                broader=value_list(graph, skos_concept, SKOS.broader),
                narrower=value_list(graph, skos_concept, SKOS.narrower),
            )
        )

    return values if len(values) > 0 else None
