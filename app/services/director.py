from app.dao.director import DirectorDao


class DirectorService:
    def __init__(self, director_dao: DirectorDao):
        self.director_dao = director_dao

    def get_one(self, uid):
        return self.director_dao.get_one(uid)

    def get_all(self):
        return self.director_dao.get_all()
