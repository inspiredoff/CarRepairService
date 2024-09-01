from datetime import datetime

from dataclasses import dataclass

from model.src.models.Client.Client import Client
from model.src.models.entity import Entity


@dataclass
class Car(Entity):
    id: int
    brand: str
    model: str
    year: datetime
    number: str
    client: Client = None

    def __post_init__(self):
        self.name = self.brand + " " + self.model + " " + str(self.year)
