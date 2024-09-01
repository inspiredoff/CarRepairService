from abc import ABC, abstractmethod
import asyncio

from model.src.models.entity import Entity


class Database(ABC):

    @abstractmethod
    async def get_entity_by_id(self, id: int) -> Entity:
        pass

    @abstractmethod
    async def get_entity_by_name(self, name: str) -> Entity:
        pass

    @abstractmethod
    async def get_entity_by_number(self, number: str) -> Entity:
        pass

    @abstractmethod
    async def get_all_entities(self) -> list[Entity]:
        pass

    @abstractmethod
    async def add_entity(self, entity: Entity):
        pass
