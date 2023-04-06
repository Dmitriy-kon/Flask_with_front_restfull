from app.dao.genre import GenreDao

from app.services.genre import GenreService

from app.setup.db import db

# DAO
genre_dao = GenreDao(session=db.session)

# Services
genre_services = GenreService(genre_dao=genre_dao)
