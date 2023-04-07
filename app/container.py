from app.dao.genre import GenreDao
from app.dao.director import DirectorDao
from app.dao.movie import MovieDao

from app.services.genre import GenreService
from app.services.director import DirectorService
from app.services.movie import MovieService

from app.setup.db import db

# DAO
genre_dao = GenreDao(session=db.session)
director_dao = DirectorDao(session=db.session)
movie_dao = MovieDao(session=db.session)

# Services
genre_services = GenreService(genre_dao=genre_dao)
director_services = DirectorService(director_dao=director_dao)
movie_services = MovieService(movie_dao=movie_dao)
