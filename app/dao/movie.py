from typing import Type

from sqlalchemy import desc

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound, _T
from sqlalchemy.orm.query import RowReturningQuery

from app.dao.model.movie import Movie
from app.dao.model.director import Director
from app.dao.model.genre import Genre


class MovieDao:
    def __init__(self, session: Session):
        self.session = session

    def __get_names(self):
        movie_query = self.session.query(
            Movie.id,
            Movie.title,
            Movie.description,
            Movie.trailer,
            Movie.year,
            Movie.rating,
            Genre.name.label("genre"),
            Director.name.label("director")
        ).join(Movie.genre).join(Movie.director)
        # movie_query = self.session.query(Movie).join(Movie.genre).join(Movie.director)

        return movie_query

    def get_one(self, mid):
        movie = self.__get_names().filter(Movie.id == mid).one()
        return movie

    def get_all(self):
        movies = self.__get_names().all()

        return movies

    def filter_movies(self, filters: dict[str, int | str]) -> RowReturningQuery | list[_T]:
        movies = self.__get_names()

        page = filters.get('page')

        status = filters.get('status')

        if status and status == "new":
            movies = movies.order_by(desc(Movie.created))

        if filters.get("page"):
            _limit = 12
            _offset = (page - 1) * _limit

            movies = movies.offset(_offset).limit(_limit)

        return movies.all()
