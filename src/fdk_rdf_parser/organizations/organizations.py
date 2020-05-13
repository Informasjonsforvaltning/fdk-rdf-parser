from rdflib import Graph, URIRef
from rdflib.namespace import FOAF, SKOS

from fdk_rdf_parser.classes import Publisher, PublisherId
from fdk_rdf_parser.rdf_utils import brURI, objectValue, rovURI, valueTranslations
from .organizations_client import getRdfOrgData
from .utils import organizationUrl


def publisherFromFDKOrgCatalog(publisherId: PublisherId, orgsGraph: Graph) -> Publisher:
    if publisherId.id is None:
        return returnPublisherId(publisherId)
    else:
        orgRef = URIRef(organizationUrl(publisherId.id))

        if (orgRef, None, None) in orgsGraph:
            return parsePublisher(orgsGraph, orgRef)
        else:
            fdkOrg = getRdfOrgData(orgnr=publisherId.id)

            if fdkOrg is not None:
                orgGraph = Graph().parse(data=fdkOrg, format="turtle")
                return parsePublisher(orgGraph, orgRef)
            else:
                return returnPublisherId(publisherId)


def parsePublisher(graph: Graph, orgRef: URIRef) -> Publisher:
    regDataRef = graph.value(orgRef, rovURI("registration"))

    return Publisher(
        id=objectValue(graph, regDataRef, SKOS.notation),
        uri=orgRef.toPython(),
        name=objectValue(graph, orgRef, rovURI("legalName")),
        orgPath=objectValue(graph, orgRef, brURI("orgPath")),
        prefLabel=valueTranslations(graph, orgRef, FOAF.name),
        organisasjonsform=objectValue(graph, orgRef, rovURI("orgType")),
    )


def returnPublisherId(publisherId: PublisherId) -> Publisher:
    return Publisher(uri=publisherId.uri, id=publisherId.id)
