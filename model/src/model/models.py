from abc import ABC
from dataclasses import dataclass, field, MISSING


@dataclass
class OriginEntity(ABC):
    __id: int | None = None


class OriginEntityAddressees(OriginEntity, ABC):
    __phone_number: int


class OriginEntityCar(OriginEntity, ABC):
    __make: str
    __model: str
    __year: int
    __sts_number: str


class OriginEntityClient(OriginEntity, ABC):
    __first_name: str
    __last_name: str | None
    __family_name: str | None
    __adressees: OriginEntityAddressees
    __car: list[OriginEntity] = field(default_factory=list)


class OriginEntityHistoryRepair(OriginEntity, ABC):
    __date: str
    __cost: int
    __state: str
    __client: OriginEntityClient
    __car: OriginEntityCar


class OriginEntitySupportCar(OriginEntity, ABC):
    __make: str
    __model: str
    __year: int


class Car(OriginEntityCar):

    def __init__(self, make: str, model: str, year: int, sts_number: str, client: OriginEntityClient,
                 id: int | None = None):
        super().__init__(id, make, model, year, sts_number, client)

    @property
    async def make(self):
        return self.__make

    @property
    async def model(self):
        return self.__model

    @property
    async def year(self):
        return self.__year

    @property
    async def sts_number(self):
        return self.__sts_number

    @property
    async def client(self):
        return self.__client

    @make.setter
    async def make(self, make):
        self.__make = make

    @model.setter
    async def model(self, model):
        self.__model = model

    @year.setter
    async def year(self, year):
        self.__year = year

    @sts_number.setter
    async def sts_number(self, sts_number):
        self.__sts_number = sts_number

    @client.setter
    async def client(self, client):
        self.__client = client


class Addressees(OriginEntityAddressees):

    def __init__(self, phone_number, id=None):
        super().__init__(id, phone_number)

    @property
    async def id(self):
        return self.__id

    @property
    async def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    async def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @id.setter
    async def id(self, id):
        self.__id = id


class Client(OriginEntityClient):

    def __init__(self,
                 first_name: str,
                 addressees: OriginEntityAddressees,
                 id: int | None = None,
                 family_name: str | None = None,
                 last_name: str | None = None,
                 ):
        super().__init__(id, first_name, last_name, family_name, addressees)

    @property
    async def id(self):
        return self.__id

    @property
    async def first_name(self):
        return self.__first_name

    @property
    async def last_name(self):
        return self.__last_name

    @property
    async def family_name(self):
        return self.__family_name

    @property
    async def addressees(self):
        return self.__adressees

    @property
    async def car(self):
        return self.__car

    @id.setter
    async def id(self, id):
        self.__id = id

    @first_name.setter
    async def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    async def last_name(self, last_name):
        self.__last_name = last_name

    @family_name.setter
    async def family_name(self, family_name):
        self._family_name = family_name

    @addressees.setter
    async def addressees(self, addressees):
        self.__adressees = addressees

    @car.setter
    async def car(self, car):
        self.__car.append(car)


class HistoryCarRepair(OriginEntityHistoryRepair):

    def __init__(self, date=None, cost=None, state=None, client_id=None, car_id=None):
        super().__init__(id, date, cost, state, client_id, car_id)

    @property
    async def date(self):
        return self.__date

    @property
    async def cost(self):
        return self.__cost

    @property
    async def state(self):
        return self.__state

    @property
    async def client_id(self):
        return self.__client_id

    @property
    async def car_id(self):
        return self.__car_id

    @date.setter
    async def date(self, date):
        self.__date = date

    @cost.setter
    async def cost(self, cost):
        self.__cost = cost

    @state.setter
    async def state(self, state):
        self.__state = state

    @client_id.setter
    async def client_id(self, client_id):
        self.__client_id = client_id

    @car_id.setter
    async def car_id(self, car_id):
        self.__car_id = car_id


class SupportCar(OriginEntitySupportCar):

    def __init__(self, make=None, model=None, year=None):
        super().__init__()
        self.__id = id
        self.__make = make
        self.__model = model
        self.__year = year

    @property
    async def make(self):
        return self.__make

    @property
    async def model(self):
        return self.__model

    @property
    async def year(self):
        return self.__year

    @make.setter
    async def make(self, make):
        self.__make = make

    @model.setter
    async def model(self, model):
        self.__model = model

    @year.setter
    async def year(self, year):
        self.__year = year
