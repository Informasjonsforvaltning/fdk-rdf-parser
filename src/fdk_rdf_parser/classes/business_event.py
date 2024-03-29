from dataclasses import dataclass
from typing import Any

from .event import Event


@dataclass
class BusinessEvent(Event):
    specialized_type: str = "business_event"

    def add_event_values(self: Any, values: Event) -> None:
        self.id = values.id
        self.uri = values.uri
        self.identifier = values.identifier
        self.harvest = values.harvest
        self.title = values.title
        self.description = values.description
        self.dctType = values.dctType
        self.relation = values.relation
        self.associatedBroaderTypes = values.associatedBroaderTypes
        self.mayInitiate = values.mayInitiate
        self.subject = values.subject
        self.distribution = values.distribution
        self.catalog = values.catalog
