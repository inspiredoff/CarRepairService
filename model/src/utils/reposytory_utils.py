from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from model.src.repository.models.models import AbstractBase


class RepositoryUtils:

    def __init__(self, async_session: async_sessionmaker[AsyncSession]):
        self.__async_session = async_session

    async def extract_query(self, query, extract_method):
        async with self.__async_session() as session:
            res = await session.execute(query)
        return extract_method(res.scalars())

    async def add_entity(self, entities: list[AbstractBase]) -> list[dict[str, int]]:
        list_ids = []
        async with self.__async_session() as session:
            for i in entities:
                session.add(i)
                list_ids.append({type(i): i.id})
            await session.commit()
        return list_ids
