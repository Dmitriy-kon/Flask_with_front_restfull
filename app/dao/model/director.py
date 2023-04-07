from marshmallow import fields, Schema
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.setup.db.models import Base


class Director(Base):
    __tablename__ = "directors"
    name: Mapped[str] = mapped_column(String(100), nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
