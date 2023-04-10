import pytest
from sqlalchemy.exc import NoResultFound

from app.dao.movie import MovieDao
from app.dao.model.movie import Movie

from run import app


class TestMovieDao:
    @pytest.fixture(autouse=True)
    def create_instance(self, session):
        self.movie_dao = MovieDao(session=session)

    def test_get_one(self):
        with app.app_context():
            assert type(self.movie_dao.get_one(1)) == Movie, "Это не модель жанра"

            assert {'id', 'title', 'description', 'trailer', 'year', 'rating'} <= set(
                self.movie_dao.get_one(2).__dict__.keys())

            with pytest.raises(NoResultFound):
                self.movie_dao.get_one(50)

    def test_get_all(self, filter1, filter2, filter3):
        with app.app_context():
            assert len(self.movie_dao.get_all(filter1)) == 12
            assert self.movie_dao.get_all(filter3) == []
            assert all(map(lambda x: isinstance(x, Movie), self.movie_dao.get_all()))
            assert len(self.movie_dao.get_all()) > 1
