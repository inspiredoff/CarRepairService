from abc import ABC
from dataclasses import dataclass


@dataclass
class OriginEntity(ABC):
    id: int


class OriginEntityClient(OriginEntity, ABC):
    first_name: str
    last_name: str
    family_name: str
    phone_number: int


class OriginEntityCar(OriginEntity, ABC):
    make: str
    model: str
    year: int
    sts_number: str
    client_id: int


class OriginEntityHistoryRepair(OriginEntity, ABC):
    date: str
    cost: int
    state: str
    client_id: int
    car_id: int


class Car(OriginEntityCar):
    pass


class Client(OriginEntityClient):
    pass


class HistoryCarRepair(OriginEntityHistoryRepair):
    pass
