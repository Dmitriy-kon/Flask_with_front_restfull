from marshmallow import fields, Schema

from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.model.genre import GenreSchema
from app.setup.db.models import Base


class User(Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=True)
    surname: Mapped[str] = mapped_column(String(150), nullable=True)
    favorite_genre_id: Mapped[int] = mapped_column(Integer, ForeignKey("genres.id", name='fk_user_genre'),
                                                   nullable=True)

    favorite_genre = relationship("Genre")


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str(load_only=True)
    name = fields.Str()
    surname = fields.Str()

    favorite_genre_id = fields.Int(load_only=True)
    favorite_genre = fields.Nested(GenreSchema())
