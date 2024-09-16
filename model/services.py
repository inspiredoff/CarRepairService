from config import dsn
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from model.src.repository.car_repository.car_repository import CarRepository
from model.src.repository.client_repository.client_repository import ClientRepository
from model.src.repository.models.models import Addressees
from model.src.repository.models.models import Car
from model.src.repository.models.models import Client
from model.src.repository.repository import CarOriginRepository
from model.src.repository.repository import CarsModelDatabase
from model.src.repository.repository import ClientOriginRepository
from model.src.repository.repository import RepairOriginRepository
from model.src.repository.support_car_reposytory.support_car_repository import SupportCarRepository


class Services:

    client_repository: ClientOriginRepository
    car_repository: CarOriginRepository
    support_car_repository: CarsModelDatabase
    history_repair: RepairOriginRepository

    def __init__(self):
        async_engine = create_async_engine(url=dsn, echo=True)
        self.__async_session_factory = async_sessionmaker(async_engine)
        self.client_repository = ClientRepository(Client(), self.__async_session_factory)
        self.car_repository = CarRepository(Car(), self.__async_session_factory)
        self.support_car_repository = SupportCarRepository(self.__async_session_factory)

    # Client

    async def get_all_client(self):
        clients = await self.client_repository.get_all_entities()
        print(clients)

    async def get_client_by_id(self, id: int):
        client = await self.client_repository.get_entity_by_id(id)
        print(client)

    async def get_client_by_first_name(self, first_name: str):
        client = await self.client_repository.get_entity_by_first_name(first_name)
        print(client)

    async def get_client_by_family_name(self, family_name: str):
        client = await self.client_repository.get_entity_by_family_name(family_name)
        print(client)

    async def get_client_by_last_name(self, last_name: str):
        client = await self.client_repository.get_entity_by_last_name(last_name)
        print(client)

    async def add_client(self, first_name: str, family_name: str, last_name: str, phone_number: int) -> None:
        client = Client()
        client.first_name = first_name
        client.family_name = family_name
        client.last_name = last_name
        addrees = Addressees()
        addrees.phone_number = phone_number
        await self.client_repository.add_entity(client, addrees)

    # Car

    async def get_all_car(self):
        cars = await self.car_repository.get_all_entities()
        print(cars)

    async def get_car_by_id(self, id: int):
        car = await self.car_repository.get_entity_by_id(id)
        print(car)

    async def get_car_by_make(self, brand: str):
        car = await self.car_repository.get_entity_by_make(brand)
        print(car)

    async def get_car_by_model(self, model: str):
        car = await self.car_repository.get_entity_by_model(model)
        print(car)

    async def add_car(self, brand: str, model: str, year: int, number: str) -> None:
        car = Car()
        car.make = brand
        car.model = model
        car.year = year
        car.sts_number = number
        await self.car_repository.add_entity(car)

    # Repair

    async def get_all_repair(self):
        await self.history_repair.get_all_entities()

    async def get_repair_by_id(self, id: int):
        await self.history_repair.get_entity_by_id(id)

    async def get_repair_by_car_id(self, car_id: int):
        await self.history_repair.get_entity_by_car_id(car_id)

    async def get_repair_by_client_id(self, client_id: int):
        await self.history_repair.get_entity_by_client_id(client_id)

    async def get_repair_by_date(self, date: str):
        await self.history_repair.get_entity_by_date(date)

    async def get_repair_by_status(self, status: str):
        await self.history_repair.get_entity_by_status(status)

    # SupportCar
    async def get_make_by_id(self, make_id: int):
        await self.support_car_repository.get_make_by_id(make_id)

    async def get_model_by_id(self, model_id:int):
        await self.support_car_repository.get_model_by_id(model_id)

    async def get_model_by_make_name(self, make_name:str):
        await self.support_car_repository.get_model_by_make_name(make_name)

    async def get_model_by_make_id(self, make_id:int):
        await self.support_car_repository.get_model_by_make_id(make_id)

    async def get_make_by_name(self, make_name):
        await self.support_car_repository.get_make_by_name(make_name)

    async def get_all_models(self):
        await self.support_car_repository.get_all_model()

    async def get_all_make(self):
        await self.support_car_repository.get_all_make()



