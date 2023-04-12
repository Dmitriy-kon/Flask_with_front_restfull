from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model import Genre


class GenreDao:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, uid):
        genre = self.session.get(Genre, uid)
        return genre

    def get_all(self):
        stmt = select(Genre)

        genres = self.session.scalars(stmt).all()
        return genres
