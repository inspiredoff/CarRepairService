from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from model.src.repository.models.models import Car

# from model.src.models.car.car import Car
# from model.src.models.entity import Entity
# from model.src.repository.models.models import CarsTable
from model.src.repository.repository import CarOriginRepository
from model.src.utils.reposytory_utils import RepositoryUtils


class CarRepository(CarOriginRepository):

    def __init__(self, entity: Car, async_session: async_sessionmaker[AsyncSession]):
        super().__init__(entity, async_session)
        self.__async_session = async_session
        self.__entity = entity

    async def get_entity_by_model(self, model: str) -> Car:
        query = select(self.__entity).where(self.__entity.model == model)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_make(self, brand: str) -> Car:
        query = select(self.__entity).where(self.__entity == brand)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_id(self, id: int) -> Car:
        return await super().get_entity_by_id(id)

    async def get_entity_by_number(self, number: str) -> Car:
        query = select(self.__entity).where(self.__entity.sts_number == number)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_all_entities(self) -> list[Car]:
        return await super().get_all_entities()

    async def add_entity(self, entity: Car) -> int:
        await RepositoryUtils(self.__async_session).add_entity([entity])
        return entity.id
