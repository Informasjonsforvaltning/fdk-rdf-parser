from dataclasses import dataclass

from .event import Event


@dataclass
class LifeEvent(Event):
    specialized_type: str = "life_event"
