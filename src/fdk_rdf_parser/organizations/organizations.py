from rdflib import Graph, URIRef
from rdflib.namespace import FOAF, SKOS

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.rdf_utils import brURI, objectValue, rovURI, valueTranslations
from .organizations_client import getOrgPath, getRdfOrgData
from .utils import organizationUrl


def publisherFromFDKOrgCatalog(publisher: Publisher, orgsGraph: Graph) -> Publisher:
    if publisher.id is None:
        return addOrgPath(publisher)
    else:
        orgRef = URIRef(organizationUrl(publisher.id))

        if (orgRef, None, None) in orgsGraph:
            return parsePublisher(orgsGraph, orgRef, publisher)
        else:
            fdkOrg = getRdfOrgData(orgnr=publisher.id)

            if fdkOrg is not None:
                orgGraph = Graph().parse(data=fdkOrg, format="turtle")
                return parsePublisher(orgGraph, orgRef, publisher)
            else:
                return addOrgPath(publisher)


def parsePublisher(graph: Graph, orgRef: URIRef, publisher: Publisher) -> Publisher:
    regDataRef = graph.value(orgRef, rovURI("registration"))

    return Publisher(
        id=objectValue(graph, regDataRef, SKOS.notation),
        uri=orgRef.toPython(),
        name=objectValue(graph, orgRef, rovURI("legalName")),
        orgPath=objectValue(graph, orgRef, brURI("orgPath")),
        prefLabel=publisher.prefLabel
        if publisher.prefLabel
        else valueTranslations(graph, orgRef, FOAF.name),
        organisasjonsform=objectValue(graph, orgRef, rovURI("orgType")),
    )


def addOrgPath(publisher: Publisher) -> Publisher:
    orgPath = None
    if publisher.id:
        orgPath = getOrgPath(publisher.id)
    elif publisher.prefLabel:
        if publisher.prefLabel.get("nb"):
            orgPath = getOrgPath(publisher.prefLabel["nb"])
        elif publisher.prefLabel.get("nn"):
            orgPath = getOrgPath(publisher.prefLabel["nn"])
        elif publisher.prefLabel.get("en"):
            orgPath = getOrgPath(publisher.prefLabel["en"])

    publisher.orgPath = orgPath
    return publisher
