from typing import List
from rdflib import Graph, URIRef, BNode

from .rdf_utils import objectValue, resourceList
from .parse_classes import ContactPoint

def extractContactPoints(graph: Graph, subject: URIRef) -> List[ContactPoint]:
    values = []
    for resource in resourceList(graph, subject, URIRef(u'http://www.w3.org/ns/dcat#contactPoint')):
        resourceUri = None
        if isinstance(resource, URIRef):
            resourceUri = resource.toPython()

        values.append(ContactPoint(
            uri = resourceUri,
            fullname = objectValue(graph, resource, URIRef(u'http://www.w3.org/2006/vcard/ns#fn')),
            email = extractHasEmail(graph, resource),
            organizationName = objectValue(graph, resource, URIRef(u'http://www.w3.org/2006/vcard/ns#hasOrganizationName')),
            organizationUnit = objectValue(graph, resource, URIRef(u'http://www.w3.org/2006/vcard/ns#organization-unit')),
            hasURL = objectValue(graph, resource, URIRef(u'http://www.w3.org/2006/vcard/ns#hasURL')),
            hasTelephone = extractHasTelephone(graph, resource)
        ))

    return values

def extractHasTelephone(graph: Graph, subject: BNode):
    telephone: str = objectValue(graph, subject, URIRef(u'http://www.w3.org/2006/vcard/ns#hasTelephone'))
    if telephone == None:
        return None
    elif 'tel:' in telephone:
        return telephone[4:]
    else:
        return telephone

def extractHasEmail(graph: Graph, subject: BNode):
    email: str = objectValue(graph, subject, URIRef(u'http://www.w3.org/2006/vcard/ns#hasEmail'))
    if email == None:
        return None
    elif 'mailto:' in email:
        return email[7:]
    else:
        return email