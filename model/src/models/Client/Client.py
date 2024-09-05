from dataclasses import dataclass

from model.src.models.car.car import Car
from model.src.models.entity import Entity


@dataclass
class Client(Entity):
    first_name: str
    family_name: str
    last_name: str
    cars: list[Car] = None

    def __post_init__(self):
        self.name = self.first_name + " " + self.family_name + " " + self.last_name
