from abc import ABC, abstractmethod
import asyncio

class database(ABC):

    @abstractmethod
    async def get_entity_by_id(id:int)->Entity:
        pass

    @abstractmethod
    async def get_entity_by_name(name:str)->Entity:
        pass

    @abstractmethod
    async def get_entity_by_number(number:str)->Entity:
        pass

    