from typing import (
    List,
    Optional,
)

from rdflib import (
    Graph,
    Literal,
    URIRef,
)
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import ConformsTo
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    value_translations,
)


def extract_conforms_to(graph: Graph, subject: URIRef) -> Optional[List[ConformsTo]]:
    values = []
    for conforms_to in resource_list(graph, subject, DCTERMS.conformsTo):
        conforms_to_uri = None
        if isinstance(conforms_to, URIRef) or isinstance(conforms_to, Literal):
            conforms_to_uri = conforms_to.toPython()

        source_value = object_value(graph, conforms_to, DCTERMS.source)

        values.append(
            ConformsTo(
                uri=source_value if source_value is not None else conforms_to_uri,
                prefLabel=value_translations(graph, conforms_to, DCTERMS.title),
            )
        )

    return values if len(values) > 0 else None
