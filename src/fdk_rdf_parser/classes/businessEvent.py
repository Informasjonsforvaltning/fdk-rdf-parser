from dataclasses import dataclass

from .event import Event


@dataclass
class BusinessEvent(Event):
    event_type: str = "business_event"
