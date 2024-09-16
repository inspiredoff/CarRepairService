from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from model.src.repository.models.models import SupportCar
from model.src.repository.repository import CarsModelDatabase
from model.src.utils.reposytory_utils import RepositoryUtils


class SupportCarRepository(CarsModelDatabase):

    def __init__(self, async_session: async_sessionmaker[AsyncSession]):
        self.__async_session = async_session

    async def get_all_make(self) -> list[str]:
        query = select(SupportCar.make)
        return await RepositoryUtils(self.__async_session).extract_query(query, lambda result: result.all())

    async def get_all_model(self) -> list[str]:
        query = select(SupportCar.model)
        return await RepositoryUtils(self.__async_session).extract_query(query, lambda result: result.all())

    async def get_model_by_make_name(self, make: str) -> str:
        query = select(SupportCar.model).where(SupportCar.make == make)
        return await RepositoryUtils(self.__async_session).extract_query(query, lambda result: result.all())

    async def get_model_by_make_id(self, make_id: int) -> list[str]:
        query = select(SupportCar.model).where(SupportCar.id == make_id)
        return await RepositoryUtils(self.__async_session).extract_query(query, lambda result: result.one())

    async def get_make_by_id(self, make_id: int) -> str:
        query = select(SupportCar.make).where(SupportCar.id == make_id)
        return await RepositoryUtils(self.__async_session).extract_query(query, lambda result: result.one())

    async def get_make_by_name(self, make_name: str) -> str:
        query = select(SupportCar.make).where(SupportCar.make == make_name)
        return await RepositoryUtils(self.__async_session).extract_query(query, lambda result: result.one())

    async def get_model_by_id(self, model_id: int) -> str:
        query = select(SupportCar.model).where(SupportCar.id == model_id)
        return await RepositoryUtils(self.__async_session).extract_query(query, lambda result: result.one())
