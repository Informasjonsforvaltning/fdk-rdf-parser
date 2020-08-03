from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .dcat_resource import PartialDcatResource
from .distribution import Distribution
from .harvest_meta_data import HarvestMetaData
from .publisher import Publisher
from .qualified_attribution import QualifiedAttribution
from .quality_annotation import QualityAnnotation
from .references import Reference
from .skos_code import SkosCode
from .skos_concept import SkosConcept
from .subject import Subject
from .temporal import Temporal
from .theme import ThemeLOS


@dataclass
class PartialDataset(PartialDcatResource):
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
    subject: Optional[List[Subject]] = None
    spatial: Optional[List[SkosCode]] = None
    provenance: Optional[SkosCode] = None
    accrualPeriodicity: Optional[SkosCode] = None
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
    references: Optional[List[Reference]] = None
    qualifiedAttributions: Optional[List[QualifiedAttribution]] = None

    def addValuesFromDcatResource(self: Any, values: PartialDcatResource) -> None:
        self.identifier = values.identifier
        self.publisher = values.publisher
        self.title = values.title
        self.description = values.description
        self.descriptionFormatted = values.descriptionFormatted
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


@dataclass
class Dataset(PartialDataset):
    publisher: Optional[Publisher] = None
    losTheme: Optional[List[ThemeLOS]] = None

    def addValuesFromPartial(self: Any, values: PartialDataset) -> None:
        self.id = values.id
        self.identifier = values.identifier
        self.title = values.title
        self.description = values.description
        self.descriptionFormatted = values.descriptionFormatted
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
        self.harvest = values.harvest
        self.accessRightsComment = values.accessRightsComment
        self.distribution = values.distribution
        self.sample = values.sample
        self.source = values.source
        self.objective = values.objective
        self.page = values.page
        self.admsIdentifier = values.admsIdentifier
        self.temporal = values.temporal
        self.subject = values.subject
        self.spatial = values.spatial
        self.provenance = values.provenance
        self.accrualPeriodicity = values.accrualPeriodicity
        self.hasAccuracyAnnotation = values.hasAccuracyAnnotation
        self.hasCompletenessAnnotation = values.hasCompletenessAnnotation
        self.hasCurrentnessAnnotation = values.hasCurrentnessAnnotation
        self.hasAvailabilityAnnotation = values.hasAvailabilityAnnotation
        self.hasRelevanceAnnotation = values.hasRelevanceAnnotation
        self.legalBasisForRestriction = values.legalBasisForRestriction
        self.legalBasisForProcessing = values.legalBasisForProcessing
        self.legalBasisForAccess = values.legalBasisForAccess
        self.conformsTo = values.conformsTo
        self.informationModel = values.informationModel
        self.qualifiedAttributions = values.qualifiedAttributions
