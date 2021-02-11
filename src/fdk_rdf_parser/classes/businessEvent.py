from dataclasses import dataclass

from .event import Event


@dataclass
class BusinessEvent(Event):
    pass
