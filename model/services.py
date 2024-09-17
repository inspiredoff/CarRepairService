from config import dsn
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from model.src.model.models import Addressees
from model.src.model.models import Car
from model.src.model.models import Client
from model.src.model.models import HistoryCarRepair
from model.src.model.models import SupportCar
from model.src.repository.car_repository.car_repository import CarRepository
from model.src.repository.client_repository.client_repository import ClientRepository
from model.src.repository.models.models import CarsTable, ClientTable, AddresseesTable
from model.src.repository.repository import CarOriginRepository
from model.src.repository.repository import CarsModelDatabase
from model.src.repository.repository import ClientOriginRepository
from model.src.repository.repository import RepairOriginRepository
from model.src.repository.support_car_reposytory.support_car_repository import SupportCarRepository
from model.src.utils.outpututils import OutputUtils


class Services:

    client_repository: ClientOriginRepository
    car_repository: CarOriginRepository
    support_car_repository: CarsModelDatabase
    history_repair: RepairOriginRepository

    def __init__(self):
        async_engine = create_async_engine(url=dsn, echo=True)
        self.__async_session_factory = async_sessionmaker(async_engine)
        self.client_repository = ClientRepository(ClientTable(), self.__async_session_factory)
        self.car_repository = CarRepository(CarsTable(), self.__async_session_factory)
        self.support_car_repository = SupportCarRepository(self.__async_session_factory)

    # Client

    async def get_all_clients(self):
        clients = await self.client_repository.get_all_entities()
        client_model = await self.__model_into_table_model(clients)
        await OutputUtils.print_entity_ms(client_model)


    async def get_client_by_id(self, id: int):
        client = await self.client_repository.get_entity_by_id(id)
        client_model = await self.__model_into_table_model(client)
        await OutputUtils.print_entity_ms(client_model)


    async def get_clients_by_first_name(self, first_name: str):
        client = await self.client_repository.get_entity_by_first_name(first_name)
        client_model = await self.__model_into_table_model(client)
        await OutputUtils.print_entity_ms(client_model)

    async def get_clients_by_family_name(self, family_name: str):
        client = await self.client_repository.get_entity_by_family_name(family_name)
        client_model = await self.__model_into_table_model(client)
        await OutputUtils.print_entity_ms(client_model)

    async def get_clients_by_last_name(self, last_name: str):
        client = await self.client_repository.get_entity_by_last_name(last_name)
        client_model = await self.__model_into_table_model(client)
        await OutputUtils.print_entity_ms(client_model)

    async def add_client(self, first_name: str, family_name: str, last_name: str, phone_number: int) -> None:
        addressees = AddresseesTable()
        addressees.phone_number = phone_number
        client = ClientTable()
        client.first_name = first_name
        client.family_name = family_name
        client.last_name = last_name
        client.addressees = addressees
        await self.client_repository.add_entity(client, addressees)
        client_model = await self.__model_into_table_model(client)
        await OutputUtils.print_entity_ms(client_model)

    async def __model_into_table_model(self, client):
        client_model = Client(
            first_name=client.first_name,
            addressees=client.addresses,
            family_name=client.family_name,
            last_name=client.last_name,
            id=client.id
        )
        return client_model

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
        car = Car(make=brand, model=model, year=year, sts_number=number)
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

