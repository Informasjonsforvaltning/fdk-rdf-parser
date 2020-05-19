from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS

from fdk_rdf_parser.classes import DataService
from fdk_rdf_parser.rdf_utils import (
    dcatURI,
    objectValue,
    valueList,
)
from .dcat_resource import parseDcatResource


def parseDataService(
    dataServicesGraph: Graph, dataServiceURI: URIRef, recordURI: URIRef
) -> DataService:

    dataService = DataService(
        id=objectValue(dataServicesGraph, recordURI, DCTERMS.identifier),
        endpointURL=valueList(
            dataServicesGraph, dataServiceURI, dcatURI("endpointURL")
        ),
        endpointDescription=valueList(
            dataServicesGraph, dataServiceURI, dcatURI("endpointDescription")
        ),
        mediaType=valueList(dataServicesGraph, dataServiceURI, dcatURI("mediaType")),
        conformsTo=valueList(dataServicesGraph, dataServiceURI, dcatURI("conformsTo")),
        servesDataset=valueList(
            dataServicesGraph, dataServiceURI, dcatURI("servesDataset")
        ),
    )

    dataService.addValuesFromDcatResource(
        parseDcatResource(dataServicesGraph, dataServiceURI)
    )
    return dataService
