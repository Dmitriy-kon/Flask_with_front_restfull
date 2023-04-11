from typing import Type

from flask_migrate import Migrate

from app.config import Config

from app.view.genre import genre_ns
from app.view.director import directors_ns
from app.view.movie import movies_ns
from app.view.user import user_ns
from app.view.auth import auth_ns

from app.setup.api import api
from app.setup.db import db

from flask import render_template, Flask


def create_app(config_obj: Type[Config]):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route("/")
    def index():
        return "This is index :)"

    # init app
    db.init_app(app)
    api.init_app(app)

    # namespaces
    api.add_namespace(genre_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)

    migrate = Migrate(app, db, render_as_batch=True)

    return app
