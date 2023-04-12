from marshmallow import fields, Schema

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.model.movie import MovieSchema
from app.setup.db import db

from datetime import datetime

from sqlalchemy import func, DateTime, Integer


class Favorite(db.Model):
    __tablename__ = "favorite_movies"
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", name='fk_user_id'), primary_key=True)
    movie_id: Mapped[int] = mapped_column(Integer, ForeignKey("movies.id", name='fk_movie_id'), primary_key=True)

    user: Mapped["User"] = relationship("User", back_populates='favorite_movies')
    movie: Mapped["Movie"] = relationship("Movie", back_populates='favorite_movies')

    created: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class FavouriteSchema(Schema):
    user_id = fields.Int()
    movie = fields.Nested(MovieSchema())
