from dataclasses import dataclass
from typing import (
    Any,
    List,
    Optional,
)

from .cpsvno_service import Service
from .publisher import Publisher


@dataclass
class PublicService(Service):
    hasCompetentAuthority: Optional[List[Publisher]] = None

    def add_cpsvno_service_values(self: Any, values: Service) -> None:
        self.id = values.id
        self.uri = values.uri
        self.identifier = values.identifier
        self.title = values.title
        self.description = values.description
        self.isDescribedAt = values.isDescribedAt
        self.isGroupedBy = values.isGroupedBy
        self.harvest = values.harvest
        self.keyword = values.keyword
        self.sector = values.sector
        self.isClassifiedBy = values.isClassifiedBy
        self.language = values.language
        self.holdsRequirement = values.holdsRequirement
        self.contactPoint = values.contactPoint
        self.hasParticipation = values.hasParticipation
        self.hasInput = values.hasInput
        self.produces = values.produces
        self.requires = values.requires
        self.follows = values.follows
        self.hasLegalResource = values.hasLegalResource
        self.hasChannel = values.hasChannel
        self.processingTime = values.processingTime
        self.hasCost = values.hasCost
        self.relation = values.relation
        self.spatial = values.spatial
        self.type = values.type
        self.admsStatus = values.admsStatus
        self.subject = values.subject
        self.homepage = values.homepage
        self.dctType = values.dctType
