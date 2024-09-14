from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

# from model.src.models.entity import Entity
# from model.src.models.repair.repair import Repair
from model.src.repository.models.models import AbstractBase
from model.src.repository.repository import RepairDatabase


class RepairStorage(RepairDatabase):

    def __init__(self,
                 base: RepairDatabase,
                 async_session: async_sessionmaker[AsyncSession]):
        super().__init__(base, async_session)

    async def get_entity_by_id(self, id: int) -> Repair:
        return await super().get_entity_by_id(id)

    async def get_entity_by_number(self, number: str) -> Repair:
        return await super().get_entity_by_number(number)

    async def get_all_entities(self) -> list[Repair]:
        return await super().get_all_entities()

    async def add_entity(self, entity: Repair) -> None:
        return await super().add_entity(entity)

    async def get_entity_by_client_id(self) -> Repair:
        pass

    async def get_entity_by_car_id(self) -> Repair:
        pass

    async def get_entity_by_date(self) -> Repair:
        pass

    async def get_entity_by_status(self) -> list[Repair]:
        pass
