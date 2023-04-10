import pytest

from app.dao.genre import GenreDao
from app.dao.model.genre import Genre

from run import app


class TestGenreDao:
    @pytest.fixture(autouse=True)
    def create_instance(self, session):
        self.genre_dao = GenreDao(session=session)

    def test_get_one(self):
        with app.app_context():
            assert type(self.genre_dao.get_one(1)) == Genre, "Это не модель жанра"
            assert {'id', 'name'} <= set(self.genre_dao.get_one(2).__dict__.keys())

            assert self.genre_dao.get_one(53) is None

    def test_get_all(self):
        with app.app_context():
            assert all(map(lambda x: isinstance(x, Genre), self.genre_dao.get_all()))
            assert len(self.genre_dao.get_all()) > 1
