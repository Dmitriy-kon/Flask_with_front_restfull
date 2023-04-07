from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model.user import User


class UserDao:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, uid):
        user = self.session.query(User).get(uid)
        return user

    def get_all(self):
        users = self.session.query(User).all()
        return users
