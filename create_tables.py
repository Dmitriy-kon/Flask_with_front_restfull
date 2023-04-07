from app.config import Config
from app.server import create_app
from app.setup.db import db


if __name__ == "__main__":
    with create_app(Config).app_context():
        db.create_all()