from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

#
# from model.src.models.Client.Client import Client
# from model.src.models.entity import Entity
from model.src.repository.models.models import Client, AbstractBase
from model.src.repository.storage import Database, ClientDatabase


class ClientStorage(ClientDatabase):

    def __init__(self, base: Client, async_session: async_sessionmaker[AsyncSession]):
        super().__init__(base, async_session)

    async def get_entity_by_id(self, id: int) -> Client:
        return await super().get_entity_by_id(id)

    # async def get_entity_by_id(self, id: int) -> Client:
    #     return await super().get_entity_by_id(id)

    async def get_entity_by_number(self, number: str) -> Client:
        return await super().get_entity_by_number(number)

    async def get_all_entities(self) -> list[Client]:
        return await super().get_all_entities()

    async def get_entity_by_first_name(self, first_name: str) -> Client:
        query = select(ClientsTable).where(ClientsTable.first_name == first_name)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_family_name(self, family_name: str) -> Client:
        query = select(ClientsTable).where(ClientsTable.family_name == family_name)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_last_name(self, last_name: str) -> Client:
        query = select(ClientsTable).where(ClientsTable.last_name == last_name)
        return await super()._extract_query(query, lambda result: result.one())

    async def add_entity(self, entity: Entity):
        pass
