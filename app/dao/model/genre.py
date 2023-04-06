from marshmallow import fields, Schema
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.setup.db.models import Base


class Genre(Base):
    __tablename__ = "genres"
    name: Mapped[str] = mapped_column(String(100), nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
