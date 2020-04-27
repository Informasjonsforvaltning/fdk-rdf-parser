from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .dcat_resource import DcatResource
from .distribution import Distribution
from .harvest_meta_data import HarvestMetaData
from .quality_annotation import QualityAnnotation
from .skos_concept import SkosConcept
from .temporal import Temporal


@dataclass
class Dataset(DcatResource):
    id: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    accessRightsComment: Optional[List[str]] = None
    distribution: Optional[List[Distribution]] = None
    sample: Optional[List[Distribution]] = None
    source: Optional[str] = None
    objective: Optional[Dict[str, str]] = None
    page: Optional[List[str]] = None
    admsIdentifier: Optional[List[str]] = None
    temporal: Optional[List[Temporal]] = None
    subject: Optional[List[str]] = None
    spatial: Optional[List[str]] = None
    provenance: Optional[str] = None
    accrualPeriodicity: Optional[str] = None
    hasAccuracyAnnotation: Optional[QualityAnnotation] = None
    hasCompletenessAnnotation: Optional[QualityAnnotation] = None
    hasCurrentnessAnnotation: Optional[QualityAnnotation] = None
    hasAvailabilityAnnotation: Optional[QualityAnnotation] = None
    hasRelevanceAnnotation: Optional[QualityAnnotation] = None
    legalBasisForRestriction: Optional[List[SkosConcept]] = None
    legalBasisForProcessing: Optional[List[SkosConcept]] = None
    legalBasisForAccess: Optional[List[SkosConcept]] = None
    conformsTo: Optional[List[SkosConcept]] = None
    informationModel: Optional[List[SkosConcept]] = None

    def addValuesFromDcatResource(self: Any, values: DcatResource) -> Any:
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
