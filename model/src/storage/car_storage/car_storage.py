from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_session

from model.src.models.car.car import Car
from model.src.models.entity import Entity
from model.src.storage.models.models import CarsTable
from model.src.storage.storage import Database, CarDatabase


class CarStorage(CarDatabase):

    def __init__(self):
        super().__init__(CarsTable)

    async def get_entity_by_model(self, model)-> Car:
        query = select(CarsTable).where(CarsTable.model == model)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_brand(self, brand:str)-> Car:
        query = select(CarsTable).where(CarsTable.brand == brand)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_id(self, id: int) -> Car:
        return await super().get_entity_by_id(id)

    async def get_entity_by_number(self, number: str) -> Car:
        return await super().get_entity_by_number(number)

    async def get_all_entities(self) -> list[Entity]:
        return await super().get_all_entities()

    async def add_entity(self, entity: Entity):
        pass