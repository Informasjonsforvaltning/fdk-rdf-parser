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

from fdk_rdf_parser.classes import ConformsTo
from fdk_rdf_parser.rdf_utils import (
    object_value,
    resource_list,
    resource_uri_value,
    value_translations,
)


def extract_conforms_to(graph: Graph, subject: URIRef) -> Optional[List[ConformsTo]]:
    values = []
    for conforms_to in resource_list(graph, subject, DCTERMS.conformsTo):
        conforms_to_uri = resource_uri_value(conforms_to)
        source_value = object_value(graph, conforms_to, DCTERMS.source)

        uri_value = object_value(graph, conforms_to, RDFS.seeAlso)
        uri_value = source_value if uri_value is None else uri_value
        uri_value = conforms_to_uri if uri_value is None else uri_value

        values.append(
            ConformsTo(
                uri=uri_value,
                prefLabel=value_translations(graph, conforms_to, DCTERMS.title),
            )
        )

    return values if len(values) > 0 else None
