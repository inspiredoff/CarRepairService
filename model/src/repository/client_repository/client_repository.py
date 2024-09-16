from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

#
# from model.src.models.Client.Client import Client
# from model.src.models.entity import Entity
from model.src.repository.models.models import Client, Car, Addressees
from model.src.repository.repository import ClientOriginRepository
from model.src.utils.reposytory_utils import RepositoryUtils


class ClientRepository(ClientOriginRepository):

    def __init__(self, entity: Client, async_session: async_sessionmaker[AsyncSession]):
        super().__init__(entity, async_session)
        self.__entity = entity

    async def get_entity_by_id(self, id: int):
        return await super().get_entity_by_id(id)

    # async def get_entity_by_number(self, number: str) -> Client:
    #     return await super().get_entity_by_number(number)

    async def get_all_entities(self) -> list[Client]:
        return await super().get_all_entities()

    async def get_entity_by_first_name(self, first_name: str) -> Client:
        query = select(self.__entity).where(self.__entity.first_name == first_name)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_family_name(self, family_name: str) -> Client:
        query = select(self.__entity).where(self.__entity.family_name == family_name)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_entity_by_last_name(self, last_name: str) -> Client:
        query = select(self.__entity).where(self.__entity.last_name == last_name)
        return await super()._extract_query(query, lambda result: result.one())

    async def get_car_by_client_id(self, client_id: int) -> list[int]:
        query = select(self.__entity.car_id).where(self.__entity.id == client_id)
        return await super()._extract_query(query, lambda result: result.all())

    async def add_entity(self, entity: Client, number: Addressees):
        utils = RepositoryUtils(self.async_session).add_entity([entity, number])
        return utils

