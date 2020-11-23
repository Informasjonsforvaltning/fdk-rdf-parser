from dataclasses import dataclass
from typing import Dict, List, Optional

from .event import Event
from .harvest_meta_data import HarvestMetaData
from .publisher import Publisher


@dataclass
class PublicService:
    id: Optional[str] = None
    uri: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    isGroupedBy: Optional[List[Event]] = None
    hasCompetentAuthority: Optional[List[Publisher]] = None
    harvest: Optional[HarvestMetaData] = None
    type: str = "publicservices"
