from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

# from model.src.models.entity import Entity
# from model.src.models.repair.repair import Repair
from model.src.repository.models.models import AbstractBase
from model.src.repository.models.models import HistoryCarRepair
from model.src.repository.repository import RepairOriginRepository
from model.src.utils.reposytory_utils import RepositoryUtils


class RepairStorage(RepairOriginRepository):

    def __init__(self, entity: HistoryCarRepair, async_session: async_sessionmaker[AsyncSession]):
        super().__init__(entity, async_session)
        self.__entity = entity

    async def get_entity_by_id(self, id: int) -> HistoryCarRepair:
        return await super().get_entity_by_id(id)

    async def get_all_entities(self) -> list[HistoryCarRepair]:
        return await super().get_all_entities()

    async def add_entity(self, entity: HistoryCarRepair) -> None:
        await RepositoryUtils(self.async_session).add_entity([entity])

    async def get_entity_by_client_id(self, client_id: int) -> list[HistoryCarRepair]:
        query = select(self.__entity).where(self.__entity.client_id == client_id)
        return await super()._extract_query(query, lambda result: result.all())

    async def get_entity_by_car_id(self, car_id: int) -> list[HistoryCarRepair]:
        query = select(self.__entity).where(self.__entity.car_id == car_id)
        return await super()._extract_query(query, lambda result: result.all())

    async def get_entity_by_date(self, date: str) -> list[HistoryCarRepair]:
        query = select(self.__entity).where(self.__entity.date == date)
        return await super()._extract_query(query, lambda result: result.all())

    async def get_entity_by_status(self, status: str) -> list[HistoryCarRepair]:
        query = select(self.__entity).where(self.__entity.state == status)
        return await super()._extract_query(query, lambda result: result.all())
