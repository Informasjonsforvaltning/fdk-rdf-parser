from dataclasses import dataclass
from typing import Dict, List

from .dcat_resource import DcatResource
from .harvest_meta_data import HarvestMetaData
from .distribution import Distribution
from .temporal import Temporal
from .quality_annotation import QualityAnnotation
from .skos_concept import SkosConcept


@dataclass
class Dataset(DcatResource):
    id: str = None
    harvest: HarvestMetaData = None
    accessRightsComment: List[str] = None
    distribution: List[Distribution] = None
    sample: List[Distribution] = None
    source: str = None
    objective: Dict[str, str] = None
    page: List[str] = None
    admsIdentifier: List[str] = None
    temporal: List[Temporal] = None
    subject: List[str] = None
    spatial: List[str] = None
    provenance: str = None
    accrualPeriodicity: str = None
    hasAccuracyAnnotation: QualityAnnotation = None
    hasCompletenessAnnotation: QualityAnnotation = None
    hasCurrentnessAnnotation: QualityAnnotation = None
    hasAvailabilityAnnotation: QualityAnnotation = None
    hasRelevanceAnnotation: QualityAnnotation = None
    legalBasisForRestriction: List[SkosConcept] = None
    legalBasisForProcessing: List[SkosConcept] = None
    legalBasisForAccess: List[SkosConcept] = None
    conformsTo: List[SkosConcept] = None
    informationModel: List[SkosConcept] = None

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
