from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from .config import system_config
from sqlalchemy.orm import sessionmaker


DATABASE_URI = f"postgresql+asyncpg://{system_config.db_user}:{system_config.db_password}@{system_config.db_host}:" \
               f"{system_config.db_port}/{system_config.db_name}"



engine = create_async_engine(DATABASE_URI)


async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:  # noqa: B008
    async with async_session() as session:
        await session.connection()
        yield session
