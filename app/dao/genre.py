from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model.genre import Genre


class GenreDao:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, uid):
        genre = self.session.query(Genre).get(uid)
        return genre

    def get_all(self):
        genres = self.session.query(Genre).all()
        return genres
