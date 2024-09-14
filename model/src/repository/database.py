from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncAttrs
)

from sqlalchemy.orm import DeclarativeBase




class Base(DeclarativeBase):
    pass
