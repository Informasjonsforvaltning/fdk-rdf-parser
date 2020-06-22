from rdflib import Graph, URIRef
from rdflib.namespace import DCTERMS, FOAF

from fdk_rdf_parser.classes import PartialDataset
from fdk_rdf_parser.rdf_utils import (
    admsURI,
    dcatApNoURI,
    dcatURI,
    dqvIsoURI,
    objectValue,
    provURI,
    valueList,
    valueTranslations,
)
from .dcat_resource import parseDcatResource
from .distribution import extractDistributions
from .harvest_meta_data import extractMetaData
from .qualified_attribution import extractQualifiedAttributions
from .quality_annotation import extractQualityAnnotation
from .references import extractReferences
from .skos_code import extractSkosCode, extractSkosCodeList
from .skos_concept import extractSkosConcept
from .subject import extractSubjects
from .temporal import extractTemporal


def parseDataset(
    datasetsGraph: Graph, recordURI: URIRef, datasetURI: URIRef
) -> PartialDataset:
    qualityAnnotations = extractQualityAnnotation(datasetsGraph, datasetURI)

    dataset = PartialDataset(
        id=objectValue(datasetsGraph, recordURI, DCTERMS.identifier),
        admsIdentifier=valueList(datasetsGraph, datasetURI, admsURI("identifier")),
        harvest=extractMetaData(datasetsGraph, recordURI),
        accessRightsComment=valueList(
            datasetsGraph, datasetURI, dcatApNoURI("accessRightsComment")
        ),
        distribution=extractDistributions(
            datasetsGraph, datasetURI, dcatURI("distribution")
        ),
        sample=extractDistributions(datasetsGraph, datasetURI, admsURI("sample")),
        spatial=extractSkosCodeList(datasetsGraph, datasetURI, DCTERMS.spatial),
        source=objectValue(datasetsGraph, datasetURI, dcatApNoURI("source")),
        objective=valueTranslations(
            datasetsGraph, datasetURI, dcatApNoURI("objective")
        ),
        page=valueList(datasetsGraph, datasetURI, FOAF.page),
        temporal=extractTemporal(datasetsGraph, datasetURI),
        subject=extractSubjects(datasetsGraph, datasetURI),
        provenance=extractSkosCode(datasetsGraph, datasetURI, DCTERMS.provenance),
        accrualPeriodicity=extractSkosCode(
            datasetsGraph, datasetURI, DCTERMS.accrualPeriodicity
        ),
        hasAccuracyAnnotation=qualityAnnotations.get(dqvIsoURI("Accuracy").toPython()),
        hasCompletenessAnnotation=qualityAnnotations.get(
            dqvIsoURI("Completeness").toPython()
        ),
        hasCurrentnessAnnotation=qualityAnnotations.get(
            dqvIsoURI("Currentness").toPython()
        ),
        hasAvailabilityAnnotation=qualityAnnotations.get(
            dqvIsoURI("Availability").toPython()
        ),
        hasRelevanceAnnotation=qualityAnnotations.get(
            dqvIsoURI("Relevance").toPython()
        ),
        legalBasisForRestriction=extractSkosConcept(
            datasetsGraph, datasetURI, dcatApNoURI("legalBasisForRestriction")
        ),
        legalBasisForProcessing=extractSkosConcept(
            datasetsGraph, datasetURI, dcatApNoURI("legalBasisForProcessing")
        ),
        legalBasisForAccess=extractSkosConcept(
            datasetsGraph, datasetURI, dcatApNoURI("legalBasisForAccess")
        ),
        conformsTo=extractSkosConcept(datasetsGraph, datasetURI, DCTERMS.conformsTo),
        informationModel=extractSkosConcept(
            datasetsGraph, datasetURI, dcatApNoURI("informationModel")
        ),
        references=extractReferences(datasetsGraph, datasetURI),
        qualifiedAttributions=extractQualifiedAttributions(
            datasetsGraph, datasetURI, provURI("qualifiedAttribution")
        ),
    )

    dataset.addValuesFromDcatResource(
        parseDcatResource(graph=datasetsGraph, subject=datasetURI)
    )

    return dataset
