from app.dao import GenreDao


class GenreService:
    def __init__(self, genre_dao: GenreDao):
        self.genre_dao = genre_dao

    def get_one(self, uid):
        return self.genre_dao.get_one(uid)

    def get_all(self):
        return self.genre_dao.get_all()
