from abc import ABC, abstractmethod
import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

# from model.src.models.entity import Entity
from model.src.repository.models.models import AbstractBase


class Database(ABC):

    def __init__(self, base: AbstractBase, async_session: async_sessionmaker[AsyncSession]):
        self.base = base
        self.async_session = async_session

    async def _extract_query(self, query, extract_method):
        async with self.async_session() as session:
            res = await session.execute(query)
        return extract_method(res.scalars())

    async def get_entity_by_id(self, id: int) -> AbstractBase:
        query = select(self.base).where(self.base.id == id)
        return await self._extract_query(query, lambda result: result.one())

    async def get_all_entities(self) -> list[AbstractBase]:
        query = select(self.base)
        return await self._extract_query(query, lambda result: result.all())

    async def add_entity(self, entity: AbstractBase) -> None:
        async with self.async_session() as session:
            session.add(entity)
            await session.commit()


class CarDatabase(Database):

    def __init__(self, base: AbstractBase, async_session: async_sessionmaker[AsyncSession]):
        super().__init__(base, async_session)

    @abstractmethod
    async def get_entity_by_brand(self, brand: str) -> AbstractBase:
        pass

    @abstractmethod
    async def get_entity_by_model(self, model: str) -> AbstractBase:
        pass


class ClientDatabase(Database):

    @abstractmethod
    async def get_entity_by_first_name(self, first_name: str) -> AbstractBase:
        pass

    @abstractmethod
    async def get_entity_by_family_name(self, family_name: str) -> AbstractBase:
        pass

    @abstractmethod
    async def get_entity_by_last_name(self, last_name: str) -> AbstractBase:
        pass


class RepairDatabase(Database):

    @abstractmethod
    async def get_entity_by_client_id(self):
        pass

    @abstractmethod
    async def get_entity_by_car_id(self):
        pass

    @abstractmethod
    async def get_entity_by_date(self):
        pass

    @abstractmethod
    async def get_entity_by_status(self):
        pass