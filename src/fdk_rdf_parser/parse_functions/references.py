from typing import List, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import Reference, SkosCode, SkosConcept
from fdk_rdf_parser.rdf_utils import value_list


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
        references = value_list(graph, subject, predicate)
        if references:
            for reference in references:
                values.append(
                    Reference(
                        referenceType=SkosCode(uri=predicate.toPython()),
                        source=SkosConcept(uri=reference),
                    )
                )

    return values if len(values) > 0 else None
