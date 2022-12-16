from dataclasses import dataclass
from typing import (
    Dict,
    List,
    Optional,
)

from fdk_rdf_parser.classes.theme import (
    EuDataTheme,
    LosNode,
)
from .channel import Channel
from .contactpoint import CVContactPoint
from .cost import Cost
from .evidence import Evidence
from .harvest_meta_data import HarvestMetaData
from .legal_resource import LegalResource
from .output import Output
from .participation import Participation
from .publisher import Publisher
from .requirement import Requirement
from .rule import Rule
from .skos_code import ReferenceDataCode
from .skos_concept import SkosConcept


@dataclass
class Service:
    id: Optional[str] = None
    uri: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[Dict[str, str]] = None
    description: Optional[Dict[str, str]] = None
    harvest: Optional[HarvestMetaData] = None
    ownedBy: Optional[List[Publisher]] = None
    contactPoint: Optional[List[CVContactPoint]] = None
    keyword: Optional[List[Dict[str, str]]] = None
    sector: Optional[List[SkosConcept]] = None
    produces: Optional[List[Output]] = None
    spatial: Optional[List[str]] = None
    hasInput: Optional[List[Evidence]] = None
    processingTime: Optional[str] = None
    isDescribedAt: Optional[List[SkosConcept]] = None
    hasParticipation: Optional[List[Participation]] = None
    isGroupedBy: Optional[List[str]] = None
    isClassifiedBy: Optional[List[SkosConcept]] = None
    hasChannel: Optional[List[Channel]] = None
    follows: Optional[List[Rule]] = None
    hasCost: Optional[List[Cost]] = None
    requires: Optional[List["Service"]] = None
    relation: Optional[List["Service"]] = None
    hasLegalResource: Optional[List[LegalResource]] = None
    language: Optional[List[ReferenceDataCode]] = None
    holdsRequirement: Optional[List[Requirement]] = None
    associatedBroaderTypesByEvents: Optional[List[str]] = None
    type: str = "publicservices"
    admsStatus: Optional[ReferenceDataCode] = None
    subject: Optional[List[str]] = None
    homepage: Optional[List[str]] = None
    dctType: Optional[List[ReferenceDataCode]] = None
    thematicAreaUris: Optional[List[str]] = None
    losThemes: Optional[List[LosNode]] = None
    euDataThemes: Optional[List[EuDataTheme]] = None
