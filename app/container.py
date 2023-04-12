from app.dao.genre import GenreDao
from app.dao.director import DirectorDao
from app.dao.movie import MovieDao
from app.dao.user import UserDao
from app.dao.favorites import FavoritesDao

from app.services.genre import GenreService
from app.services.director import DirectorService
from app.services.movie import MovieService
from app.services.user import UserService
from app.services.auth import AuthService
from app.services.favorites import FavoriteService

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