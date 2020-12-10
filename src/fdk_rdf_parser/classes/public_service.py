from dataclasses import dataclass
from typing import Dict, List, Optional

from .criterion_requirement import CriterionRequirement
from .event import Event
from .evidence import Evidence
from .harvest_meta_data import HarvestMetaData
from .output import Output
from .participation import Participation
from .publisher import Publisher
from .skos_code import SkosCode
from .skos_concept import SkosConcept


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
    keyword: Optional[List[Dict[str, str]]] = None
    sector: Optional[List[SkosConcept]] = None
    isClassifiedBy: Optional[List[SkosConcept]] = None
    language: Optional[List[SkosCode]] = None
    hasCriterion: Optional[List[CriterionRequirement]] = None
    hasParticipation: Optional[List[Participation]] = None
    hasInput: Optional[List[Evidence]] = None
    produces: Optional[List[Output]] = None
    requires: Optional[List["PublicService"]] = None
    type: str = "publicservices"
