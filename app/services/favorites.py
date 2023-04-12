from app.dao import FavoritesDao

from app.exceptions import ItemAlreadyExists


class FavoriteService:
    def __init__(self, dao: FavoritesDao):
        self.dao = dao

    def get_user_favorites(self, user_id: int):
        movies = self.dao.get_user_favorites(user_id)
        return movies

    def add_favorites(self, uid: int, mid: int):
        data = {
            "user_id": uid,
            "movie_id": mid
        }

        if self.dao.get_favorites(uid, mid):
            raise ItemAlreadyExists

        self.dao.create(data)
