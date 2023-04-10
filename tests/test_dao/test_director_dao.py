import pytest

from app.dao.director import DirectorDao
from app.dao.model.director import Director

from run import app


class TestDirectorDao:
    @pytest.fixture(autouse=True)
    def create_instance(self, session):
        self.director_dao = DirectorDao(session=session)

    def test_get_one(self):
        with app.app_context():
            assert type(self.director_dao.get_one(1)) == Director, "Это не модель директора"
            assert self.director_dao.get_one(50) is None
            assert {'id', 'name'} <= set(self.director_dao.get_one(2).__dict__.keys())

    def test_get_all(self):
        with app.app_context():
            assert all(map(lambda x: isinstance(x, Director), self.director_dao.get_all()))
            assert len(self.director_dao.get_all()) > 1

