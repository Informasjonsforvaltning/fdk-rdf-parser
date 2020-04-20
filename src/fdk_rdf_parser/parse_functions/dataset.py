from rdflib import Graph, URIRef, BNode
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import Dataset
from fdk_rdf_parser.rdf_utils import objectValue, valueList, valueTranslations, dcatURI, admsURI, dcatApNoURI, dqvIsoURI

from .dcat_resource import parseDcatResource
from .harvest_meta_data import extractMetaData
from .distribution import extractDistributions
from .temporal import extractTemporal
from .quality_annotation import extractQualityAnnotation
from .skos_concept import extractSkosConcept

def parseDataset(datasetsGraph: Graph, recordURI: URIRef, datasetURI: URIRef) -> Dataset:
    qualityAnnotations = extractQualityAnnotation(datasetsGraph, datasetURI)

    dataset = Dataset(
        id = objectValue(datasetsGraph, recordURI, DCTERMS.identifier),
        admsIdentifier = valueList(datasetsGraph, datasetURI, admsURI('identifier')),
        harvest = extractMetaData(datasetsGraph, recordURI),
        accessRightsComment = valueList(datasetsGraph, datasetURI, dcatApNoURI('accessRightsComment')),
        distribution = extractDistributions(datasetsGraph, datasetURI),
        spatial = valueList(datasetsGraph, datasetURI, DCTERMS.spatial),
        source = objectValue(datasetsGraph, datasetURI, dcatApNoURI('source')),
        objective = valueTranslations(datasetsGraph, datasetURI, dcatApNoURI('objective')),
        page = valueList(datasetsGraph, datasetURI, FOAF.page),
        temporal = extractTemporal(datasetsGraph, datasetURI),
        subject = valueList(datasetsGraph, datasetURI, DCTERMS.subject),
        provenance = objectValue(datasetsGraph, datasetURI, DCTERMS.provenance),
        accrualPeriodicity = objectValue(datasetsGraph, datasetURI, DCTERMS.accrualPeriodicity),
        hasAccuracyAnnotation = qualityAnnotations.get(dqvIsoURI('Accuracy').toPython()),
        hasCompletenessAnnotation = qualityAnnotations.get(dqvIsoURI('Completeness').toPython()),
        hasCurrentnessAnnotation = qualityAnnotations.get(dqvIsoURI('Currentness').toPython()),
        hasAvailabilityAnnotation = qualityAnnotations.get(dqvIsoURI('Availability').toPython()),
        hasRelevanceAnnotation = qualityAnnotations.get(dqvIsoURI('Relevance').toPython()),
        legalBasisForRestriction = extractSkosConcept(datasetsGraph, datasetURI, dcatApNoURI('legalBasisForRestriction')),
        legalBasisForProcessing = extractSkosConcept(datasetsGraph, datasetURI, dcatApNoURI('legalBasisForProcessing')),
        legalBasisForAccess = extractSkosConcept(datasetsGraph, datasetURI, dcatApNoURI('legalBasisForAccess')),
        conformsTo = extractSkosConcept(datasetsGraph, datasetURI, DCTERMS.conformsTo),
        informationModel = extractSkosConcept(datasetsGraph, datasetURI, dcatApNoURI('informationModel'))
    )
    
    dataset.addValuesFromDcatResource(parseDcatResource(graph=datasetsGraph, subject=datasetURI))
    
    return dataset
