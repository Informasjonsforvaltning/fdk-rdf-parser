from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import RDF, DCTERMS, FOAF

from .rdf_utils import objectValue, valueList, valueTranslations, dcatURI, admsURI, dcatApNoURI

from .dcat_resource import DcatResource, parseDcatResource
from .harvest_meta_data import HarvestMetaData, extractMetaData
from .contactpoint import ContactPoint, extractContactPoints
from .distribution import Distribution, extractDistributions
from .temporal import Temporal, extractTemporal

@dataclass
class Dataset(DcatResource):
    id: str = None
    harvest: HarvestMetaData = None
    accessRightsComment: List[str] = field(default_factory=list)
    distribution: List[Distribution] = field(default_factory=list)
    source: str = None
    objective: Dict[str, str] = field(default_factory=dict)
    page: List[str] = field(default_factory=list)
    admsIdentifier: List[str] = field(default_factory=list)
    temporal: List[Temporal] = field(default_factory=list)
    subject: List[str] = field(default_factory=list)
    spatial: List[str] = field(default_factory=list)
    provenance: str = None
    accrualPeriodicity: str = None

    def addValuesFromDcatResource(self, values: DcatResource):
        self.identifier = values.identifier
        self.publisher = values.publisher
        self.title = values.title
        self.description = values.description
        self.uri = values.uri
        self.accessRights = values.accessRights
        self.theme = values.theme
        self.keyword = values.keyword
        self.contactPoint = values.contactPoint
        self.type = values.type
        self.issued = values.issued
        self.modified = values.modified
        self.landingPage = values.landingPage
        self.language = values.language

def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for recordURI in datasetsGraph.subjects(predicate=RDF.type, object=dcatURI(u'record')):
        datasetURI = datasetsGraph.value(recordURI, FOAF.primaryTopic)
        if datasetURI != None:
            datasets[datasetURI.toPython()] = parseDataset(datasetsGraph, recordURI, datasetURI)

    return datasets

def parseDataset(datasetsGraph: Graph, recordURI: URIRef, datasetURI: URIRef) -> Dataset:
    dataset = Dataset(
        id = objectValue(datasetsGraph, recordURI, DCTERMS.identifier),
        admsIdentifier = valueList(datasetsGraph, datasetURI, admsURI(u'identifier')),
        harvest = extractMetaData(datasetsGraph, recordURI),
        accessRightsComment = valueList(datasetsGraph, datasetURI, dcatApNoURI(u'accessRightsComment')),
        distribution = extractDistributions(datasetsGraph, datasetURI),
        spatial = valueList(datasetsGraph, datasetURI, DCTERMS.spatial),
        source = objectValue(datasetsGraph, datasetURI, dcatApNoURI(u'source')),
        objective = valueTranslations(datasetsGraph, datasetURI, dcatApNoURI(u'objective')),
        page = valueList(datasetsGraph, datasetURI, FOAF.page),
        temporal = extractTemporal(datasetsGraph, datasetURI),
        subject = valueList(datasetsGraph, datasetURI, DCTERMS.subject),
        provenance = objectValue(datasetsGraph, datasetURI, DCTERMS.provenance),
        accrualPeriodicity = objectValue(datasetsGraph, datasetURI, DCTERMS.accrualPeriodicity)
    )
    
    dataset.addValuesFromDcatResource(parseDcatResource(graph=datasetsGraph, subject=datasetURI))
    
    return dataset
