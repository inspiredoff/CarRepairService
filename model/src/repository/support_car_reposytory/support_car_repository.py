from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from model.src.repository.models.models import SupportCar
from model.src.repository.repository import CarsModelDatabase
from model.src.utils.reposytory_utils import RepositoryUtils


class SupportCarRepository(CarsModelDatabase):

    def __init__(self, async_session: async_sessionmaker[AsyncSession]):
        self.async_session = async_session

    async def get_brands_by_id(self) -> list[SupportCar.make]:
        query = select(SupportCar.make)
        return await RepositoryUtils(self.async_session()).extract_query(query, lambda result: result.all())

    async def get_model_by_id(self) -> list[SupportCar.model]:
        query = select(SupportCar.model)
        return await RepositoryUtils(self.async_session()).extract_query(query, lambda result: result.all())

    async def get_model_by_brand_name(self, brand: str) -> SupportCar.make:
        query = select(SupportCar.model).where(SupportCar.make == brand)
        return await RepositoryUtils(self.async_session()).extract_query(query, lambda result: result.all())

    async def get_model_by_brand_id(self, id: int) -> SupportCar.model:
        query = select(SupportCar.model).where(SupportCar.id == id)
        return await RepositoryUtils(self.async_session()).extract_query(query, lambda result: result.one())
