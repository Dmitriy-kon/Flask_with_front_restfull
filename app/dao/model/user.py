from marshmallow import fields, Schema

from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.setup.db.models import Base


class User(Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=True)
    surname: Mapped[str] = mapped_column(String(150), nullable=True)

    favorite_genre: Mapped[int] = mapped_column(Integer, nullable=True, default=2)


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()

    favorite_genre = fields.Int()
