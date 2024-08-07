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
from .skos_concept import SkosConcept


@dataclass
class DataService(PartialDcatResource):
    id: Optional[str] = None
    dctType: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    endpointDescription: Optional[Set[str]] = None
    endpointURL: Optional[Set[str]] = None
    fdkFormat: Optional[List[MediaTypeOrExtent]] = None
    servesDataset: Optional[Set[str]] = None
    conformsTo: Optional[List[SkosConcept]] = None
    page: Optional[List[str]] = None
    catalog: Optional[Catalog] = None
    type: str = "dataservices"  # used by elasticsearch for indexing

    def add_values_from_dcat_resource(self: Any, values: PartialDcatResource) -> Any:
        self.identifier = values.identifier
        self.publisher = values.publisher
        self.title = values.title
        self.description = values.description
        self.descriptionFormatted = values.descriptionFormatted
        self.uri = values.uri
        self.accessRights = values.accessRights
        self.themeUris = values.themeUris
        self.theme = values.theme
        self.losTheme = values.losTheme
        self.eurovocThemes = values.eurovocThemes
        self.keyword = values.keyword
        self.contactPoint = values.contactPoint
        self.issued = values.issued
        self.modified = values.modified
        self.landingPage = values.landingPage
        self.language = values.language
