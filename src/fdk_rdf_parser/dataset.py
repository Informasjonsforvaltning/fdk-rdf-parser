from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime

from rdflib import Graph, URIRef, BNode
from rdflib.namespace import RDF, DCTERMS, FOAF

from .rdf_utils import objectValue, valueList, valueTranslations, dcatURI, admsURI, dcatApNoURI

from .harvest_meta_data import HarvestMetaData, extractMetaData
from .contactpoint import ContactPoint, extractContactPoints
from .distribution import Distribution, extractDistributions
from .temporal import Temporal, extractTemporal

@dataclass
class Dataset:
    id: str
    harvest: HarvestMetaData
    identifier: List[str] = field(default_factory=list)
    publisher: str = None
    title: Dict[str, str] = field(default_factory=dict)
    description: Dict[str, str] = field(default_factory=dict)
    uri: str = None
    accessRights: str = None
    accessRightsComment: List[str] = field(default_factory=list)
    theme: List[str] = field(default_factory=list)
    keyword: List[str] = field(default_factory=list)
    contactPoint: List[ContactPoint] = field(default_factory=list)
    distribution: List[Distribution] = field(default_factory=list)
    spatial: List[str] = field(default_factory=list)
    source: str = None
    objective: Dict[str, str] = field(default_factory=dict)
    type: str = None
    page: List[str] = field(default_factory=list)
    admsIdentifier: List[str] = field(default_factory=list)
    issued: datetime = None
    modified: datetime = None
    temporal: List[Temporal] = field(default_factory=list)
    landingPage: List[str] = field(default_factory=list)
    subject: List[str] = field(default_factory=list)
    language: List[str] = field(default_factory=list)
    spatial: List[str] = field(default_factory=list)
    provenance: str = None
    accrualPeriodicity: str = None

def parseDatasets(rdfData: str) -> Dict[str, Dataset]:
    datasetsGraph = Graph().parse(data=rdfData, format="turtle")

    datasets: Dict[str, Dataset] = {}

    for record in datasetsGraph.subjects(predicate=RDF.type, object=dcatURI(u'record')):
        datasetURI = datasetsGraph.value(record, FOAF.primaryTopic)
        if datasetURI != None:
            datasets[datasetURI.toPython()] = Dataset(
                id = objectValue(datasetsGraph, record, DCTERMS.identifier),
                identifier = valueList(datasetsGraph, datasetURI, DCTERMS.identifier),
                admsIdentifier = valueList(datasetsGraph, datasetURI, admsURI(u'identifier')),
                publisher = objectValue(datasetsGraph, datasetURI, DCTERMS.publisher),
                harvest = extractMetaData(datasetsGraph, record),
                title = valueTranslations(datasetsGraph, datasetURI, DCTERMS.title),
                description = valueTranslations(datasetsGraph, datasetURI, DCTERMS.description),
                uri = datasetURI.toPython(),
                accessRights = objectValue(datasetsGraph, datasetURI, DCTERMS.accessRights),
                accessRightsComment = valueList(datasetsGraph, datasetURI, dcatApNoURI(u'accessRightsComment')),
                theme = valueList(datasetsGraph, datasetURI, dcatURI(u'theme')),
                keyword = extractKeyWords(datasetsGraph, datasetURI),
                contactPoint = extractContactPoints(datasetsGraph, datasetURI),
                distribution = extractDistributions(datasetsGraph, datasetURI),
                spatial = valueList(datasetsGraph, datasetURI, DCTERMS.spatial),
                source = objectValue(datasetsGraph, datasetURI, dcatApNoURI(u'source')),
                objective = valueTranslations(datasetsGraph, datasetURI, dcatApNoURI(u'objective')),
                type = objectValue(datasetsGraph, datasetURI, DCTERMS.type),
                page = valueList(datasetsGraph, datasetURI, FOAF.page),
                issued = objectValue(datasetsGraph, datasetURI, DCTERMS.issued),
                modified = objectValue(datasetsGraph, datasetURI, DCTERMS.modified),
                temporal = extractTemporal(datasetsGraph, datasetURI),
                subject = valueList(datasetsGraph, datasetURI, DCTERMS.subject),
                landingPage = valueList(datasetsGraph, datasetURI, dcatURI(u'landingPage')),
                language = valueList(datasetsGraph, datasetURI, DCTERMS.language),
                provenance = objectValue(datasetsGraph, datasetURI, DCTERMS.provenance),
                accrualPeriodicity = objectValue(datasetsGraph, datasetURI, DCTERMS.accrualPeriodicity)
            )

    return datasets

def extractKeyWords(graph: Graph, subject: URIRef):
    values = []
    for keyword in graph.objects(subject, dcatURI(u'keyword')):
        translation = {}
        translation[keyword.language] = keyword.toPython()
        values.append(translation)
    return values