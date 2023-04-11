from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from app.dao.model.user import User


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

    def get_one(self, uid):
        stmt = select(User).where(User.id == uid)
        user = self.session.scalar(stmt)
        return user

    def get_all(self):
        stmt = select(User)
        users = self.session.scalars(stmt).all()
        return users

    def create(self, data):
        stmt = insert(User).values(**data).returning(User)

        result = self.session.execute(stmt)
        user = result.scalar_one()

        # user = User(**data)
        # self.session.add(user)

        self.session.commit()
        return user

    def update(self, uid, data):
        stmt = update(User) \
            .where(User.id == uid) \
            .values(**data).returning(User)

        result = self.session.execute(stmt)
        user = result.scalar_one()

        self.session.commit()

        return user

    def delete(self, uid):
        stmt = delete(User) \
            .where(User.id == uid)

        self.session.execute(stmt)

        self.session.commit()
