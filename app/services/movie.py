from app.dao.movie import MovieDao


class MovieService:
    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    def get_one(self, uid):
        movie = self.movie_dao.get_one(uid)
        return movie

    def get_all(self, filters: dict | None = None):
        movies = self.movie_dao.get_all(filters)
        return movies
