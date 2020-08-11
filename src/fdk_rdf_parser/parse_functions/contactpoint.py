from typing import Any, List, Optional

from rdflib import Graph, URIRef

from fdk_rdf_parser.classes import ContactPoint
from fdk_rdf_parser.rdf_utils import dcatURI, objectValue, resourceList, vcardURI


def extractContactPoints(graph: Graph, subject: URIRef) -> Optional[List[ContactPoint]]:
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


def extractHasTelephone(graph: Graph, subject: Any) -> Optional[Any]:
    tel_ref = graph.value(subject, vcardURI("hasTelephone"))
    if tel_ref:
        tel_value = objectValue(graph, tel_ref, vcardURI("hasValue"))
        if tel_value is None:
            tel_value = tel_ref.toPython()

        if "tel:" in tel_value:
            return tel_value[4:]
        else:
            return tel_value
    else:
        return None


def extractHasEmail(graph: Graph, subject: Any) -> Optional[Any]:
    mail_ref = graph.value(subject, vcardURI("hasEmail"))
    if mail_ref:
        email = objectValue(graph, mail_ref, vcardURI("hasValue"))
        if email is None:
            email = mail_ref.toPython()

        if "mailto:" in email:
            return email[7:]
        else:
            return email
    else:
        return None
