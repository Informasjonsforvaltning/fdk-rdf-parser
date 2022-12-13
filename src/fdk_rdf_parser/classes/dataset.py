from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
)

from .catalog import Catalog
from .conforms_to import ConformsTo
from .dcat_resource import PartialDcatResource
from .distribution import Distribution
from .harvest_meta_data import HarvestMetaData
from .publisher import Publisher
from .qualified_attribution import QualifiedAttribution
from .quality_annotation import QualityAnnotation
from .references import Reference
from .skos_code import ReferenceDataCode
from .skos_concept import SkosConcept
from .subject import Subject
from .temporal import Temporal
from .theme import LosNode


@dataclass
class PartialDataset(PartialDcatResource):
    id: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    accessRightsComment: Optional[List[str]] = None
    distribution: Optional[List[Distribution]] = None
    sample: Optional[List[Distribution]] = None
    source: Optional[str] = None
    objective: Optional[Dict[str, str]] = None
    page: Optional[Set[str]] = None
    admsIdentifier: Optional[Set[str]] = None
    temporal: Optional[List[Temporal]] = None
    subject: Optional[List[Subject]] = None
    spatial: Optional[List[ReferenceDataCode]] = None
    provenance: Optional[ReferenceDataCode] = None
    accrualPeriodicity: Optional[ReferenceDataCode] = None
    hasAccuracyAnnotation: Optional[QualityAnnotation] = None
    hasCompletenessAnnotation: Optional[QualityAnnotation] = None
    hasCurrentnessAnnotation: Optional[QualityAnnotation] = None
    hasAvailabilityAnnotation: Optional[QualityAnnotation] = None
    hasRelevanceAnnotation: Optional[QualityAnnotation] = None
    legalBasisForRestriction: Optional[List[SkosConcept]] = None
    legalBasisForProcessing: Optional[List[SkosConcept]] = None
    legalBasisForAccess: Optional[List[SkosConcept]] = None
    conformsTo: Optional[List[ConformsTo]] = None
    informationModel: Optional[List[SkosConcept]] = None
    references: Optional[List[Reference]] = None
    qualifiedAttributions: Optional[List[QualifiedAttribution]] = None
    catalog: Optional[Catalog] = None
    isOpenData: bool = False
    isAuthoritative: bool = False
    isRelatedToTransportportal: bool = False
    inSeries: Optional[str] = None
    prev: Optional[str] = None

    def add_values_from_dcat_resource(self: Any, values: PartialDcatResource) -> None:
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
        self.dctType = values.dctType
        self.issued = values.issued
        self.modified = values.modified
        self.landingPage = values.landingPage
        self.language = values.language


@dataclass
class Dataset(PartialDataset):
    publisher: Optional[Publisher] = None
    losTheme: Optional[List[LosNode]] = None
    type: str = "datasets"

    def add_values_from_partial(self: Any, values: PartialDataset) -> None:
        self.id = values.id
        self.identifier = values.identifier
        self.title = values.title
        self.publisher = values.publisher
        self.description = values.description
        self.descriptionFormatted = values.descriptionFormatted
        self.uri = values.uri
        self.accessRights = values.accessRights
        self.theme = values.theme
        self.keyword = values.keyword
        self.contactPoint = values.contactPoint
        self.dctType = values.dctType
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
        self.references = values.references
        self.qualifiedAttributions = values.qualifiedAttributions
        self.catalog = values.catalog
        self.isOpenData = values.isOpenData
        self.isAuthoritative = values.isAuthoritative
        self.isRelatedToTransportportal = values.isRelatedToTransportportal
        self.inSeries = values.inSeries
        self.prev = values.prev


@dataclass
class DatasetSeries(Dataset):
    first: Optional[str] = None
    last: Optional[str] = None
    specialized_type: str = "dataset_series"

    def add_values_from_dataset(self: Any, values: Dataset) -> None:
        self.id = values.id
        self.identifier = values.identifier
        self.title = values.title
        self.publisher = values.publisher
        self.description = values.description
        self.descriptionFormatted = values.descriptionFormatted
        self.uri = values.uri
        self.accessRights = values.accessRights
        self.theme = values.theme
        self.keyword = values.keyword
        self.contactPoint = values.contactPoint
        self.dctType = values.dctType
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
        self.references = values.references
        self.qualifiedAttributions = values.qualifiedAttributions
        self.catalog = values.catalog
        self.isOpenData = values.isOpenData
        self.isAuthoritative = values.isAuthoritative
        self.isRelatedToTransportportal = values.isRelatedToTransportportal
        self.inSeries = values.inSeries
        self.prev = values.prev
        self.publisher = values.publisher
        self.losTheme = values.losTheme
        self.type = values.type
