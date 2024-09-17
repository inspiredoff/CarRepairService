from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from model.src.model.models import OriginEntity
from model.src.repository.models.models import AbstractBase


class RepositoryUtils:

    def __init__(self, async_session: async_sessionmaker[AsyncSession]):
        self.__async_session = async_session

    async def extract_query(self, query, extract_method):
        async with self.__async_session() as session:
            res = await session.execute(query)
        return extract_method(res.scalars())

    async def add_entity(self, entities: list[AbstractBase]) -> list[int]:
        list_ids = []
        async with self.__async_session() as session:
            for entity in entities:
                session.add(entity)
            await session.commit()
        return list_ids
