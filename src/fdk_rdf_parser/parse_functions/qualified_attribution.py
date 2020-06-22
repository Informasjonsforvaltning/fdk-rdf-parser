from typing import List, Optional

from rdflib import BNode, Graph, URIRef

from fdk_rdf_parser.classes import Publisher, QualifiedAttribution
from fdk_rdf_parser.organizations import organisationNumberFromUri
from fdk_rdf_parser.rdf_utils import (
    dcatURI,
    objectValue,
    provURI,
    resourceList,
)


def extractQualifiedAttributions(
    graph: Graph, subject: URIRef, predicate: URIRef
) -> Optional[List[QualifiedAttribution]]:
    values = []
    for resource in resourceList(graph, subject, predicate):
        publisherUri = None
        publisherId = None
        role = None

        if isinstance(resource, URIRef) or isinstance(resource, BNode):
            publisherUri = objectValue(graph, resource, provURI("agent"))

            if isinstance(publisherUri, str):
                publisherId = organisationNumberFromUri(publisherUri)
                role = objectValue(graph, resource, dcatURI("hadRole"))

                values.append(
                    QualifiedAttribution(
                        agent=Publisher(uri=publisherUri, id=publisherId), role=role
                    )
                )

    return values if len(values) > 0 else None
