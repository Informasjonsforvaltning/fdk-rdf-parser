from dataclasses import dataclass
from typing import Any, List, Optional

from .dcat_resource import PartialDcatResource


@dataclass
class DataService(PartialDcatResource):

    id: Optional[str] = None

    endpointDescription: Optional[List[str]] = None
    endpointURL: Optional[List[str]] = None
    mediaType: Optional[List[str]] = None
    servesDataset: Optional[List[str]] = None
    conformsTo: Optional[List[str]] = None

    def addValuesFromDcatResource(self: Any, values: PartialDcatResource) -> Any:
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
