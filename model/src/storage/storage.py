from abc import ABC, abstractmethod
import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_session

from model.src.models.entity import Entity
from model.src.storage.models.models import AbstractBase


class Database(ABC):

    def __init__(self, base: AbstractBase):
        self.abstract_base = base

    async def _extract_query(self, query, extract_method):
        async with async_session() as session:
            res = await session.execute(query)
        return extract_method(res.scalars())

    async def get_entity_by_id(self, id: int) -> Entity:
        query = select(self.abstract_base).where(self.abstract_base.id == id)
        return await self._extract_query(query, lambda result: result.one())

    async def get_entity_by_number(self, number: str) -> Entity:
        query = select(self.abstract_base).where(self.abstract_base.number == number)
        return await self._extract_query(query, lambda result: result.one())

    async def get_all_entities(self) -> list[Entity]:
        query = select(self.abstract_base)
        return await self._extract_query(query, lambda result: result.all())

    @abstractmethod
    async def add_entity(self, entity: Entity):
        pass


class CarDatabase(Database):

    @abstractmethod
    async def get_entity_by_brand(self):
        pass

    @abstractmethod
    async def get_entity_by_model(self):
        pass