from abc import ABC
from dataclasses import dataclass


@dataclass
class OriginEntity(ABC):
    id: int


class OriginEntityAddressees(OriginEntity, ABC):
    __phone_number: int


class OriginEntityClient(OriginEntity, ABC):
    __first_name: str
    __last_name: str
    __family_name: str
    __phone_number: OriginEntityAddressees


class OriginEntityCar(OriginEntity, ABC):
    __make: str
    __model: str
    __year: int
    __sts_number: str
    __client: OriginEntityClient


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

    def __init__(self,id, make, model, year, sts_number, client_id):
        super().__init__()
        self.__id = id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__sts_number = sts_number
        self.__client_id = client_id

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
    async def client_id(self):
        return self.__client_id

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

    @client_id.setter
    async def client_id(self, client_id):
        self.__client_id = client_id


class Addressees(OriginEntityAddressees):

    def __init__(self, phone_number):
        super().__init__()
        self.__id = id
        self.__phone_number = phone_number

    @property
    async def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    async def phone_number(self, phone_number):
        self.__phone_number = phone_number


class Client(OriginEntityClient):

    def __init__(self, phone_number_id=None, first_name=None, family_name=None, last_name=None):
        super().__init__()
        self.__id = id
        self.__phone_number_id = phone_number_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__family_name = family_name

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
    async def phone_number_id(self):
        return self.__phone_number_id

    @first_name.setter
    async def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    async def last_name(self, last_name):
        self.__last_name = last_name

    @family_name.setter
    def family_name(self, value):
        self._family_name = value


class HistoryCarRepair(OriginEntityHistoryRepair):

    def __init__(self, date=None, cost=None, state=None, client_id=None, car_id=None):
        super().__init__()
        self.__id = id
        self.__date = date
        self.__cost = cost
        self.__state = state
        self.__client_id = client_id
        self.__car_id = car_id

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
