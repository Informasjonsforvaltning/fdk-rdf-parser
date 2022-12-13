from dataclasses import dataclass
from typing import (
    Any,
    List,
    Optional,
    Set,
)

from .catalog import Catalog
from .dcat_resource import PartialDcatResource
from .harvest_meta_data import HarvestMetaData
from .media_type import MediaTypeOrExtent
from .skos_code import ReferenceDataCode
from .skos_concept import SkosConcept


@dataclass
class DataService(PartialDcatResource):

    id: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    endpointDescription: Optional[Set[str]] = None
    endpointURL: Optional[Set[str]] = None
    mediaType: Optional[List[ReferenceDataCode]] = None
    fdkFormat: Optional[List[MediaTypeOrExtent]] = None
    servesDataset: Optional[Set[str]] = None
    conformsTo: Optional[List[SkosConcept]] = None
    page: Optional[List[str]] = None
    catalog: Optional[Catalog] = None
    type: str = "dataservices"

    def add_values_from_dcat_resource(self: Any, values: PartialDcatResource) -> Any:
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
