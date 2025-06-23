from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url='postgresql+asyncpg://postgres:1234@localhost:5432/vpn_bot',
    echo=True
)

session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass