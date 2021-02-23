from dataclasses import dataclass

from .event import Event


@dataclass
class BusinessEvent(Event):
    specialized_type: str = "business_event"
