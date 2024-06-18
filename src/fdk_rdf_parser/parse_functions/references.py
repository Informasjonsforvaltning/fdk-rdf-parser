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
    RDFS,
)

from fdk_rdf_parser.classes import (
    Reference,
    ReferenceDataCode,
    SkosConcept,
)
from fdk_rdf_parser.rdf_utils import (
    resource_list,
    resource_uri_value,
    value_translations,
)


def extract_references(graph: Graph, subject: URIRef) -> Optional[List[Reference]]:
    reference_properties = [
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

    for predicate in reference_properties:
        resources = resource_list(graph, subject, predicate)
        if resources:
            for resource in resources:
                values.append(
                    Reference(
                        referenceType=ReferenceDataCode(uri=predicate.toPython()),
                        source=SkosConcept(
                            uri=resource_uri_value(resource),
                            prefLabel=value_translations(graph, resource, RDFS.label),
                        ),
                    )
                )

    return values if len(values) > 0 else None
