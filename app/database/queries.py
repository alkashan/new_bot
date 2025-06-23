from sqlalchemy import text, select

from .database import Base, engine, session_maker
from .models import User, Rights


class ORM:
    @staticmethod
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        
    @staticmethod
    async def drop_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.execute(text("DROP TYPE IF EXISTS rights CASCADE"))

    @staticmethod
    async def add_user(user_id: int, username: str):
        async with session_maker() as session:
            user = User(
                tg_id=user_id,
                access_level=Rights.SIMPLEUSER,
                username=username
            )
            session.add(user)
            await session.commit()

    @staticmethod
    async def create_foreman(username: str):
        async with session_maker() as session:
            user = await session.scalar(
                select(User).where(User.username==username)
            )
            if user:
                user.access_level = Rights.FOREMAN
                await session.commit()
                return True
            return False
    
    @staticmethod
    async def delete_foreman(username: str):
        async with session_maker() as session:
            user = await session.scalar(
                select(User).where(User.username==username)
            )
            if user:
                user.access_level = Rights.SIMPLEUSER
                await session.commit()
                return True
            return False