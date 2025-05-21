from sqlalchemy import DateTime, Float, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from zoneinfo import ZoneInfo
import datetime
from config import *

base_time_zone = ZoneInfo(MODELS_TIME_ZONE)

def now() -> datetime.datetime:
    return datetime.datetime.now(base_time_zone)

class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=now)
    updated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=now, onupdate=now)

class TestModel(Base):
    __tablename__ = "test"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data: Mapped[str] = mapped_column(Text)
