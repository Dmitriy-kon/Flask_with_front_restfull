from flask import request
from flask_restx import Namespace, abort, Resource

from app.exceptions import ItemNotFound, InvalidToken, ItemAlreadyExists

from app.dao.model import MovieSchema
from app.container import user_service, auth_service, movie_services, favorites_service

from app.setup.api.models import movies, movie

favorite_ns = Namespace('favorites', description='Views for favourites')


@favorite_ns.route('/movies/')
class FavouritesViews(Resource):
    @favorite_ns.doc(description='Get user favourites')
    @favorite_ns.response(200, 'Success', model=movies)
    @favorite_ns.response(404, 'Not found')
    def get(self):
        # Get token
        auth_data = request.headers['Authorization']
        token = auth_data.split('Bearer ')[-1]

        # Get id
        email = auth_service.get_email_from_token(token)
        user_id = user_service.get_by_email(email).id

        favourites = favorites_service.get_user_favorites(user_id)
        return MovieSchema(many=True).dump(favourites), 200

    @favorite_ns.route('/movies/<int:movie_id>/')
    class FavouriteView(Resource):
        @favorite_ns.doc(description='Add favourites')
        @favorite_ns.response(200, 'Success', model=movie)
        @favorite_ns.response(404, 'Not found')
        def post(self, movie_id):
            try:
                # Get token
                auth_data = request.headers['Authorization']
                token = auth_data.split('Bearer ')[-1]

                # Get id
                email = auth_service.get_email_from_token(token)
                user_id = user_service.get_by_email(email).id

                movie_check = movie_services.get_one(movie_id)
                if not movie_check:
                    abort(404, 'Movie not found')

                favorites_service.add_favorites(user_id, movie_id)
                return "", 200

            except InvalidToken:
                abort(401, "Access denied")
            except ItemAlreadyExists:
                abort(400, 'Favourite already exist')
            except ItemNotFound:
                abort(404, 'Movie not found')
