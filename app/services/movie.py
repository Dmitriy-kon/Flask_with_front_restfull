from app.dao.movie import MovieDao


class MovieService:
    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    def get_one(self, uid):
        return self.movie_dao.get_one(uid)

    def get_all(self, filters: dict | None = None):
        if filters:
            return self.movie_dao.filter_movies(filters)

        return self.movie_dao.get_all()
