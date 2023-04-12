from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session

from app.dao.model import Movie
from app.dao.model import Favorite


class FavoritesDao:
    def __init__(self, session: Session):
        self.session = session

    def get_user_favorites(self, user_id: int):
        """Get all user favorites movies"""
        stmt = select(Movie).join(Favorite).where(Favorite.user_id == user_id, Movie.id == Favorite.movie_id)
        result = self.session.scalars(stmt).all()
        return result

    def get_favorites(self, uid: int, mid: int):
        stmt = select(Favorite).where(Favorite.user_id == uid, Favorite.movie_id == mid)
        result = self.session.execute(stmt).all()
        return result

    def create(self, data):
        stmt = insert(Favorite).values(**data).returning(Favorite)

        result = self.session.execute(stmt)
        user = result.scalar_one()

        self.session.commit()
        return user

    def delete(self, fid):
        stmt = delete(Favorite) \
            .where(Favorite.id == fid)

        self.session.execute(stmt)

        self.session.commit()
