from typing import (
    TypeVar,
    Union,
)

from fdk_rdf_parser.classes.concept import Concept
from fdk_rdf_parser.classes.cpsvno_service import Service
from fdk_rdf_parser.classes.dataservice import DataService
from fdk_rdf_parser.classes.dataset import Dataset
from fdk_rdf_parser.classes.event import Event
from fdk_rdf_parser.classes.info_model import InformationModel

ResourceType = TypeVar(
    "ResourceType",
    bound=Union[Dataset, DataService, Concept, InformationModel, Event, Service],
)
