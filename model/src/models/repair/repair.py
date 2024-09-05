from dataclasses import dataclass

from model.src.models.entity import Entity
from model.src.models.repair.status import Status


@dataclass
class Repair(Entity):

    date:int
    cost:int
    status: Status
    client_id:int
    car_id:int
