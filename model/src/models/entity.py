from abc import ABC
from dataclasses import dataclass


@dataclass
class Entity(ABC):
    id: int
    number: str

