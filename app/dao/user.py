from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model import User


class UserDao:
    def __init__(self, session: Session):
        self.session = session

    # def get_one(self, uid):
    #     user = self.session.get(User, uid)
    #     return user

    def get_by_email(self, email: str):
        try:
            stmt = select(User).where(User.email == email)
            user = self.session.scalar(stmt)

            return user

        except NoResultFound:
            return None

    def update_by_email(self, data: dict, email: str) -> None:
        """Update user with data"""
        stmt = update(User).where(User.email == email).values(**data).returning(User)
        self.session.execute(stmt)
        self.session.commit()

    def create(self, data):
        stmt = insert(User).values(**data).returning(User)

        result = self.session.execute(stmt)
        user = result.scalar_one()

        self.session.commit()
        return user

    def delete(self, uid):
        stmt = delete(User) \
            .where(User.id == uid)

        self.session.execute(stmt)

        self.session.commit()
