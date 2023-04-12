from typing import Type

from sqlalchemy import desc, select, Select

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model import Movie


class MovieDao:
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def __get_join_stmt() -> Select:
        stmt = select(Movie).join(Movie.genre).join(Movie.director)
        return stmt

    @staticmethod
    def __filter_movies(stmt: Select, filters: dict[str, int | str] | None) -> Select:
        movies = stmt

        page = filters.get('page', 1)
        status = filters.get('status', None)

        if status == "new":
            movies = movies.order_by(desc(Movie.created))

        if not page:
            page = 1

        _limit = 12
        _offset = (page - 1) * _limit

        movies = movies.offset(_offset).limit(_limit)

        return movies

    def get_one(self, mid: int) -> Movie:
        stmt = self.__get_join_stmt().where(Movie.id == mid)
        movie = self.session.execute(stmt).scalar_one()
        return movie

    def get_all(self, filters: dict | None = None) -> list[Movie]:
        stmt = self.__get_join_stmt()

        if filters:
            stmt = self.__filter_movies(stmt, filters)

        movies = self.session.scalars(stmt).all()

        return movies
