from rdflib import Graph, URIRef, BNode
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Dataset
from fdk_rdf_parser.rdf_utils import objectValue, valueList, valueTranslations, dcatURI, admsURI, dcatApNoURI

from .dcat_resource import parseDcatResource
from .harvest_meta_data import extractMetaData
from .distribution import extractDistributions
from .temporal import extractTemporal

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
