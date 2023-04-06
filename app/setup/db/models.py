from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, Column, DateTime, Integer

from app.setup.db import db


class Base(db.Model):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


# class Base(db.Model):
#     __abstract__ = True
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     created = Column(DateTime, nullable=False, default=func.now())
#     updated = Column(DateTime, default=func.now(), onupdate=func.now())
