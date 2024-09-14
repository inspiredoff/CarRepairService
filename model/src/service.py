from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import dsn



class Service:

    def __init__(self):
        async_engine = create_async_engine(url=dsn, echo=True)
        async_session_factory = async_sessionmaker(async_engine)