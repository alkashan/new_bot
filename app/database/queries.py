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
        """Срабатывает во время команды старт"""
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
        """Выдает права бригадира и возвращает True если пользователь был найден"""
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
    
    @staticmethod
    async def get_foremans():
        async with session_maker() as session:
            result = await session.scalars(
                select(User).where(User.access_level==Rights.FOREMAN)
            )
            await session.commit()
            return result.all()
    
    @staticmethod
    async def update_info(tg_id: int):
        async with session_maker() as session:
            user = await session.scalar(
                select(User).where(User.tg_id==tg_id)
            )
            if user.access_level == Rights.FOREMAN:
                return True
            return False
