import pytest

from app.setup.db import db


@pytest.fixture()
def session():
    return db.session


@pytest.fixture()
def filter1():
    return {'status': 'new', 'page': 2}


@pytest.fixture()
def filter2():
    return {'status': 'no', 'page': 0}


@pytest.fixture()
def filter3():
    return {'status': None, 'page': 12}
