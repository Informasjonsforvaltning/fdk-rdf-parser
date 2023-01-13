from dataclasses import dataclass
from typing import (
    Any,
    List,
    Optional,
)

from .cpsvno_service import Service
from .organization import Organization


@dataclass
class PublicService(Service):
    hasCompetentAuthority: Optional[List[Organization]] = None

    def add_cpsvno_service_values(self: Any, values: Service) -> None:
        self.id = values.id
        self.uri = values.uri
        self.identifier = values.identifier
        self.title = values.title
        self.description = values.description
        self.harvest = values.harvest
        self.ownedBy = values.ownedBy
        self.contactPoint = values.contactPoint
        self.keyword = values.keyword
        self.sector = values.sector
        self.produces = values.produces
        self.spatial = values.spatial
        self.hasInput = values.hasInput
        self.processingTime = values.processingTime
        self.isDescribedAt = values.isDescribedAt
        self.hasParticipation = values.hasParticipation
        self.isGroupedBy = values.isGroupedBy
        self.isClassifiedBy = values.isClassifiedBy
        self.hasChannel = values.hasChannel
        self.follows = values.follows
        self.hasCost = values.hasCost
        self.requires = values.requires
        self.relation = values.relation
        self.hasLegalResource = values.hasLegalResource
        self.language = values.language
        self.holdsRequirement = values.holdsRequirement
        self.associatedBroaderTypesByEvents = values.associatedBroaderTypesByEvents
        self.type = values.type
        self.admsStatus = values.admsStatus
        self.subject = values.subject
        self.homepage = values.homepage
        self.dctType = values.dctType
        self.thematicAreaUris = values.thematicAreaUris
        self.losThemes = values.losThemes
        self.euDataThemes = values.euDataThemes
        self.participatingAgents = values.participatingAgents
