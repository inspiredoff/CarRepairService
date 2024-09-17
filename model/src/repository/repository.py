import asyncio
from abc import ABC
from abc import abstractmethod

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

# from model.src.models.entity import Entity
from model.src.repository.models.models import AbstractBase, ClientTable, AddresseesTable, CarsTable
from model.src.model.models import (
    OriginEntity,
    OriginEntityCar,
    OriginEntityClient,
    OriginEntityHistoryRepair,
    OriginEntitySupportCar,
    OriginEntityAddressees)


class OriginRepository(ABC):

    def __init__(self, entity: AbstractBase, async_session: async_sessionmaker[AsyncSession]):
        self.__entity = entity
        self.__async_session = async_session

    async def _extract_query(self, query, extract_method):
        async with self.__async_session() as session:
            res = await session.execute(query)
        return extract_method(res.scalars())

    async def get_entity_by_id(self, id: int) -> OriginEntity:
        query = select(self.__entity).where(self.__entity.id == id)
        return await self._extract_query(query, lambda result: result.one())

    async def get_all_entities(self) -> list[OriginEntity]:
        query = select(self.__entity)
        return await self._extract_query(query, lambda result: result.all())


class CarOriginRepository(OriginRepository):

    # def __init__(self, base: AbstractBase, async_session: async_sessionmaker[AsyncSession]):
    #     super().__init__(base, async_session)

    @abstractmethod
    async def get_entitis_by_make(self, make: str) -> list[CarsTable]:
        pass

    @abstractmethod
    async def get_entitis_by_model(self, model: str) -> list[CarsTable]:
        pass

    @abstractmethod
    async def get_entity_by_id(self, id: int) -> CarsTable:
        pass

    @abstractmethod
    async def get_entity_by_number(self, number: str) -> CarsTable:
        pass

    @abstractmethod
    async def add_entity(self, car: CarsTable) -> None:
        pass


class ClientOriginRepository(OriginRepository):

    @abstractmethod
    async def get_entity_by_first_name(self, first_name: str) -> ClientTable:
        pass

    @abstractmethod
    async def get_entity_by_family_name(self, family_name: str) -> ClientTable:
        pass

    @abstractmethod
    async def get_entity_by_last_name(self, last_name: str) -> ClientTable:
        pass

    @abstractmethod
    async def add_entity(self, client: ClientTable, address: AddresseesTable) -> None:
        pass


class RepairOriginRepository(OriginRepository):

    @abstractmethod
    async def get_entity_by_client_id(self, client_id: int) -> OriginEntityHistoryRepair:
        pass

    @abstractmethod
    async def get_entity_by_car_id(self, car_id) -> OriginEntityHistoryRepair:
        pass

    @abstractmethod
    async def get_entity_by_date(self, date: str) -> OriginEntityHistoryRepair:
        pass

    @abstractmethod
    async def get_entity_by_status(self, state: str) -> OriginEntityHistoryRepair:
        pass

    @abstractmethod
    async def add_entity(self, entity: AbstractBase):
        pass


class CarsModelDatabase(ABC):

    @abstractmethod
    async def get_make_by_id(self, make_id: int) -> OriginEntitySupportCar.make:
        pass

    @abstractmethod
    async def get_model_by_id(self, model_id: int) -> OriginEntitySupportCar.model:
        pass

    @abstractmethod
    async def get_model_by_make_name(self, make: str) -> list[OriginEntitySupportCar.model]:
        pass

    @abstractmethod
    async def get_model_by_make_id(self, make_id: int) -> list[OriginEntitySupportCar.make]:
        pass

    @abstractmethod
    async def get_all_make(self) -> list[OriginEntitySupportCar.make]:
        pass

    @abstractmethod
    async def get_all_model(self) -> list[OriginEntitySupportCar.model]:
        pass

    @abstractmethod
    async def get_make_by_name(self, make_name) -> OriginEntitySupportCar.make:
        pass
