from enum import Enum

from .database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum

class Rights(Enum):
    FOREMAN: str = 'foreman'
    SIMPLEUSER: str = 'simpleuser'

class User(Base):
    __tablename__ = 'user'
    tg_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    access_level: Mapped[Rights] = mapped_column(SQLEnum(Rights))
    username: Mapped[str]