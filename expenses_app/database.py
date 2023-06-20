from contextlib import asynccontextmanager
from .settings import ASYNC_DATABASE_URL, MIN_CONN, MAX_CONN
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine

engine: AsyncEngine = create_async_engine(ASYNC_DATABASE_URL, pool_size=MIN_CONN, max_overflow=MAX_CONN)
async_session: AsyncSession = sessionmaker(engine, class_=AsyncSession)


@asynccontextmanager
async def get_connection() -> AsyncSession:
    async with async_session() as session:
        yield session


class BaseConnection:
    def __init__(self) -> None:
        pass

    async def get_connect(self) -> AsyncSession:
        async with async_session() as session:
            yield session


class AlchemyConnection(BaseConnection):
    def __init__(self) -> None:
        self.engine = create_async_engine(ASYNC_DATABASE_URL,
                                          pool_size=MIN_CONN,
                                          max_overflow=MAX_CONN)
        self.async_session = sessionmaker(engine, class_=AsyncSession)

    async def get_connect(self) -> AsyncSession:
        async with self.async_session() as session:
            yield session
