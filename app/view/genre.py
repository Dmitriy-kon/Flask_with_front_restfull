from flask_restx import Resource, Namespace

from app.container import genre_services
from app.dao.model.genre import GenreSchema

from app.setup.api.models import genre

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @genre_ns.doc(desciption="Get genres")
    @genre_ns.response(200, "Success", model=genre)
    @genre_ns.response(404, "Not found")
    def get(self):
        genres = genre_services.get_all()

        if not genres:
            return "genres not found", 404

        res = GenreSchema(many=True).dump(genres)

        return res, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @genre_ns.doc(desciption="Get genres")
    @genre_ns.response(200, "Success", model=genre)
    @genre_ns.response(404, "Not found")
    def get(self, gid):
        genre = genre_services.get_one(gid)

        if not genre:
            return f"genre with id {gid}, not found", 404

        return GenreSchema().dump(genre), 200
