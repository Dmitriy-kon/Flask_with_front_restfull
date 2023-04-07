from flask_restx import Resource, Namespace

from app.container import movie_services
from app.dao.model.movie import MovieSchema

from app.setup.api.models import movie

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.doc(desciption="Get movie")
    @movies_ns.response(200, "Success", model=movie)
    @movies_ns.response(404, "Not found")
    def get(self):
        genres = movie_services.get_all()

        if not genres:
            return "directors not found", 404

        res = MovieSchema(many=True).dump(genres)

        return res, 200


@movies_ns.route('/<int:gid>')
class MovieView(Resource):
    @movies_ns.doc(desciption="Get movie")
    @movies_ns.response(200, "Success", model=movie)
    @movies_ns.response(404, "Not found")
    def get(self, gid):
        genre = movie_services.get_one(gid)

        if not genre:
            return f"genre with id {gid}, not found", 404

        return MovieSchema().dump(genre), 200
