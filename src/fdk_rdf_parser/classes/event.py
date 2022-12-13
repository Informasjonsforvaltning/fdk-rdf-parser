from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from .harvest_meta_data import HarvestMetaData
from .publisher import Publisher
from .skos_concept import SkosConcept


@dataclass
class Event:
    id: Optional[str] = None
    uri: Optional[str] = None
    identifier: Optional[str] = None
    harvest: Optional[HarvestMetaData] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    dctType: Optional[List[SkosConcept]] = None
    hasCompetentAuthority: Optional[List[Publisher]] = None
    relation: Optional[List[str]] = None
    associatedBroaderTypes: Optional[List[str]] = None
    mayInitiate: Optional[List[str]] = None
    subject: Optional[List[str]] = None
    distribution: Optional[List[str]] = None
