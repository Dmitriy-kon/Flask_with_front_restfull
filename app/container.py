from app.dao.genre import GenreDao
from app.dao.director import DirectorDao

from app.services.genre import GenreService
from app.services.director import DirectorService

from app.setup.db import db

# DAO
genre_dao = GenreDao(session=db.session)
director_dao = DirectorDao(session=db.session)

# Services
genre_services = GenreService(genre_dao=genre_dao)
director_services = DirectorService(director_dao=director_dao)
