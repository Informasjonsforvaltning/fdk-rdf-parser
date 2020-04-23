from typing import List
from rdflib import Graph, URIRef, BNode

from fdk_rdf_parser.classes import ContactPoint
from fdk_rdf_parser.rdf_utils import objectValue, resourceList, dcatURI, vcardURI


def extractContactPoints(graph: Graph, subject: URIRef) -> List[ContactPoint]:
    values = []
    for resource in resourceList(graph, subject, dcatURI("contactPoint")):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()

        values.append(
            ContactPoint(
                uri=resourceUri,
                fullname=objectValue(graph, resource, vcardURI("fn")),
                email=extractHasEmail(graph, resource),
                organizationName=objectValue(
                    graph, resource, vcardURI("hasOrganizationName")
                ),
                organizationUnit=objectValue(
                    graph, resource, vcardURI("organization-unit")
                ),
                hasURL=objectValue(graph, resource, vcardURI("hasURL")),
                hasTelephone=extractHasTelephone(graph, resource),
            )
        )

    return values if len(values) > 0 else None


def extractHasTelephone(graph: Graph, subject: BNode):
    telephone: str = objectValue(graph, subject, vcardURI("hasTelephone"))
    if telephone is None:
        return None
    elif "tel:" in telephone:
        return telephone[4:]
    else:
        return telephone


def extractHasEmail(graph: Graph, subject: BNode):
    email: str = objectValue(graph, subject, vcardURI("hasEmail"))
    if email is None:
        return None
    elif "mailto:" in email:
        return email[7:]
    else:
        return email
