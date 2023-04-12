from app.dao import GenreDao
from app.dao import DirectorDao
from app.dao import MovieDao
from app.dao import UserDao
from app.dao import FavoritesDao

from app.services import GenreService
from app.services import DirectorService
from app.services import MovieService
from app.services import UserService
from app.services import AuthService
from app.services import FavoriteService

from app.setup.db import db

# DAO
genre_dao = GenreDao(session=db.session)
director_dao = DirectorDao(session=db.session)
movie_dao = MovieDao(session=db.session)
user_dao = UserDao(session=db.session)
favorites_dao = FavoritesDao(session=db.session)

# Services
genre_services = GenreService(genre_dao=genre_dao)
director_services = DirectorService(director_dao=director_dao)
movie_services = MovieService(movie_dao=movie_dao)
user_service = UserService(user_dao=user_dao)
auth_service = AuthService(user_service=user_service)
favorites_service = FavoriteService(dao=favorites_dao)
