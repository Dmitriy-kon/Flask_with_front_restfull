from flask_restx import Resource, Namespace
from flask import request

from app.container import movie_services
from app.dao.model import MovieSchema

from app.setup.api.models import movie

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.doc(desciption="Get movie",
                   params={
                       'status': "new, if you need desc new ",
                       'page': "page number"
                   })
    @movies_ns.response(200, "Success", model=movie)
    @movies_ns.response(404, "Not found")
    def get(self):
        filters = {
            'status': request.args.get('status'),
            'page': request.args.get('page', type=int)
        }

        movies = movie_services.get_all(filters)

        if not movies:
            return "directors not found", 404

        res = MovieSchema(many=True).dump(movies)

        return res, 200


@movies_ns.route('/<int:gid>')
class MovieView(Resource):
    @movies_ns.doc(desciption="Get movie")
    @movies_ns.response(200, "Success", model=movie)
    @movies_ns.response(404, "Not found")
    def get(self, gid):
        movie = movie_services.get_one(gid)

        if not movie:
            return f"movie with id {gid}, not found", 404

        res = MovieSchema().dump(movie)
        return res, 200
