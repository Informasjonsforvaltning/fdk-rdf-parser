from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .catalog import Catalog
from .dcat_resource import PartialDcatResource
from .harvest_meta_data import HarvestMetaData
from .model_element import ModelElement
from .model_property import ModelProperty
from .skos_code import SkosCode
from .temporal import Temporal
from .theme import ThemeLOS


@dataclass
class InformationModel(PartialDcatResource):

    id: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    catalog: Optional[Catalog] = None
    license: Optional[List[SkosCode]] = None
    informationModelIdentifier: Optional[str] = None
    spatial: Optional[List[SkosCode]] = None
    isPartOf: Optional[str] = None
    hasPart: Optional[str] = None
    isReplacedBy: Optional[str] = None
    replaces: Optional[str] = None
    temporal: Optional[List[Temporal]] = None
    hasFormat: Optional[List[str]] = None
    homepage: Optional[str] = None
    status: Optional[str] = None
    versionInfo: Optional[str] = None
    versionNotes: Optional[str] = None
    containsModelElements: Optional[List[str]] = None
    modelElements: Optional[Dict[str, ModelElement]] = None
    modelProperties: Optional[Dict[str, ModelProperty]] = None
    losTheme: Optional[List[ThemeLOS]] = None
    type: str = "informationmodels"

    def add_values_from_dcat_resource(self: Any, values: PartialDcatResource) -> Any:
        self.identifier = values.identifier
        self.publisher = values.publisher
        self.title = values.title
        self.description = values.description
        self.descriptionFormatted = values.descriptionFormatted
        self.uri = values.uri
        self.theme = values.theme
        self.keyword = values.keyword
        self.contactPoint = values.contactPoint
        self.dctType = values.dctType
        self.issued = values.issued
        self.modified = values.modified
        self.language = values.language

    def add_model_element(self: Any, element: ModelElement) -> Any:
        if self.modelElements is None:
            self.modelElements = {}

        self.modelElements[element.identifier] = element

    def add_model_property(self: Any, prop: ModelProperty) -> Any:
        if self.modelProperties is None:
            self.modelProperties = {}

        self.modelProperties[prop.identifier] = prop
