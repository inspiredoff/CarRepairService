from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import dsn
from model.src.repository.car_repository.car_repository import CarRepository
from model.src.repository.client_repository.client_repository import ClientRepository
from model.src.repository.models.models import Client, Car


class Services:

    def __init__(self):
        async_engine = create_async_engine(url=dsn, echo=True)
        self.async_session_factory = async_sessionmaker(async_engine)
        self.client_repository = ClientRepository(Client(), self.async_session_factory)
        self.car_repository = CarRepository(Car(), self.async_session_factory)

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

    async def add_client(self, first_name: str, family_name: str, last_name: str) -> None:
        client = Client()
        client.first_name = first_name
        client.family_name = family_name
        client.last_name = last_name
        await self.client_repository.add_entity(client)

    #Car

    async def get_all_car(self):
        cars = await self.car_repository.get_all_entities()
        print(cars)

    async def get_car_by_id(self, id: int):
        car = await self.car_repository.get_entity_by_id(id)
        print(car)

    async def get_car_by_brand(self, brand: str):
        car = await self.car_repository.get_entity_by_brand(brand)
        print(car)

    async def get_car_by_model(self, model: str):
        car = await self.car_repository.get_entity_by_model(model)
        print(car)

    async def add_car(self, brand: str, model: str, year: int, number: str) -> None:
        car = Car()
        car.brand = brand
        car.model = model
        car.year = year
        car.number = number
        await self.car_repository.add_entity(car)

    #Repair

    async def get_all_repair(self):
        pass

    async def get_repair_by_id(self, id: int):
        pass

    async def get_repair_by_car_id(self, car_id: int):
        pass

    async def get_repair_by_client_id(self, client_id: int):
        pass

    async def get_repair_by_date(self, date: str):
        pass

    async def get_repair_by_status(self, status: str):
        pass
