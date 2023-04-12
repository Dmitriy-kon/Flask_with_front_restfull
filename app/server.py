from typing import Type

from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config

from app.view.genre import genre_ns
from app.view.director import directors_ns
from app.view.movie import movies_ns
from app.view.user import user_ns
from app.view.auth import auth_ns
from app.view.favorites import favorite_ns

from app.setup.api import api
from app.setup.db import db

from flask import render_template, Flask

cors = CORS()


def create_app(config_obj: Type[Config]):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return 'this is main, go to /docs'

    # init app

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    api.init_app(app)
    cors.init_app(app)

    # namespaces
    api.add_namespace(genre_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorite_ns)

    return app
