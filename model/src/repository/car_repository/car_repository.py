from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_session, async_sessionmaker, AsyncSession

from model.src.repository.models.models import Car, AbstractBase
# from model.src.models.car.car import Car
# from model.src.models.entity import Entity
# from model.src.repository.models.models import CarsTable
from model.src.repository.repository import OriginRepository, CarOriginRepository


class CarRepository(CarOriginRepository):
    entity = AbcCar()

    def __init__(self, entity: AbcCar(), async_sessionmaker: async_session):
        super().__init__(entity, async_sessionmaker[AsyncSession])
        self.entity = entity

    async def get_entity_by_model(self, model: str) -> entity:
        query = select(self.entity).where(self.entity.model == model)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_brand(self, brand: str) -> entity:
        query = select(self.entity).where(self.entity.brand == brand)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_id(self, id: int) -> entity:
        return await super().get_entity_by_id(id)

    async def get_entity_by_number(self, number: str) -> Car:
        query = select(self.entity).where(self.entity.number == number)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_all_entities(self) -> list[entity]:
        return await super().get_all_entities()

    async def add_entity(self, entity: entity, phone_number: Adresess):
        return await super().add_entity(entity)
