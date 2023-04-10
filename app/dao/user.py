from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model.user import User


class UserDao:
    def __init__(self, session: Session):
        self.session = session

    def get_one(self, uid):
        user = self.session.get(User, uid)
        return user

    def get_all(self):
        stmt = select(User)
        users = self.session.scalars(stmt).all()
        return users
