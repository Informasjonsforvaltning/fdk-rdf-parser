from dataclasses import dataclass, field
from typing import List
from rdflib import Graph, URIRef, BNode

from .rdf_utils import objectValue, resourceList, dcatURI, vcardURI

@dataclass
class ContactPoint:
    uri: str = None
    fullname: str = None
    email: str = None
    organizationName: str = None
    organizationUnit: str = None
    hasURL: str = None
    hasTelephone: str = None

def extractContactPoints(graph: Graph, subject: URIRef) -> List[ContactPoint]:
    values = []
    for resource in resourceList(graph, subject, dcatURI(u'contactPoint')):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()

        values.append(ContactPoint(
            uri = resourceUri,
            fullname = objectValue(graph, resource, vcardURI(u'fn')),
            email = extractHasEmail(graph, resource),
            organizationName = objectValue(graph, resource, vcardURI(u'hasOrganizationName')),
            organizationUnit = objectValue(graph, resource, vcardURI(u'organization-unit')),
            hasURL = objectValue(graph, resource, vcardURI(u'hasURL')),
            hasTelephone = extractHasTelephone(graph, resource)
        ))

    return values

def extractHasTelephone(graph: Graph, subject: BNode):
    telephone: str = objectValue(graph, subject, vcardURI(u'hasTelephone'))
    if telephone == None:
        return None
    elif 'tel:' in telephone:
        return telephone[4:]
    else:
        return telephone

def extractHasEmail(graph: Graph, subject: BNode):
    email: str = objectValue(graph, subject, vcardURI(u'hasEmail'))
    if email == None:
        return None
    elif 'mailto:' in email:
        return email[7:]
    else:
        return email