from dataclasses import dataclass, field
from typing import Dict, List

from .dcat_resource import DcatResource
from .harvest_meta_data import HarvestMetaData
from .distribution import Distribution
from .temporal import Temporal

@dataclass
class Dataset(DcatResource):
    id: str = None
    harvest: HarvestMetaData = None
    accessRightsComment: List[str] = field(default_factory=list)
    distribution: List[Distribution] = field(default_factory=list)
    source: str = None
    objective: Dict[str, str] = field(default_factory=dict)
    page: List[str] = field(default_factory=list)
    admsIdentifier: List[str] = field(default_factory=list)
    temporal: List[Temporal] = field(default_factory=list)
    subject: List[str] = field(default_factory=list)
    spatial: List[str] = field(default_factory=list)
    provenance: str = None
    accrualPeriodicity: str = None

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
