from dataclasses import dataclass
from typing import Any, List, Optional

from .catalog import Catalog
from .dcat_resource import PartialDcatResource
from .harvest_meta_data import HarvestMetaData
from .skos_code import SkosCode
from .skos_concept import SkosConcept


@dataclass
class DataService(PartialDcatResource):

    id: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    endpointDescription: Optional[List[str]] = None
    endpointURL: Optional[List[str]] = None
    mediaType: Optional[List[SkosCode]] = None
    servesDataset: Optional[List[str]] = None
    conformsTo: Optional[List[SkosConcept]] = None
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
