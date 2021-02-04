from dataclasses import dataclass

from .event import Event


@dataclass
class LifeEvent(Event):
    event_type: str = "life_event"
