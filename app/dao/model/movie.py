from marshmallow import fields, Schema

from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.model.genre import GenreSchema
from app.dao.model.director import DirectorSchema
from app.setup.db.models import Base


class Movie(Base):
    __tablename__ = "movies"
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=False)
    trailer: Mapped[str] = mapped_column(String(150))
    year: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column(Float)

    genre_id: Mapped[int] = mapped_column(Integer, ForeignKey("genres.id"))
    director_id: Mapped[int] = mapped_column(Integer, ForeignKey("directors.id"))

    genre = relationship("Genre")
    director = relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()

    genre = fields.Nested(GenreSchema())
    director = fields.Nested(DirectorSchema())
    # genre = fields.Function(lambda x: x.genre.name, attribute='genre')
    # director = fields.Function(lambda x: x.director.name, attribute='director')
