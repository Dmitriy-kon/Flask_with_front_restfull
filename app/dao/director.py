from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model.director import Director


class DirectorDao:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, uid):
        director = self.session.query(Director).get(uid)
        return director

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors
