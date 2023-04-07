from flask_restx import Resource, Namespace

from app.container import director_services
from app.dao.model.director import DirectorSchema

from app.setup.api.models import director

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    @directors_ns.doc(desciption="Get director")
    @directors_ns.response(200, "Success", model=director)
    @directors_ns.response(404, "Not found")
    def get(self):
        genres = director_services.get_all()

        if not genres:
            return "directors not found", 404

        res = DirectorSchema(many=True).dump(genres)

        return res, 200


@directors_ns.route('/<int:gid>')
class DirectorView(Resource):
    @directors_ns.doc(desciption="Get directors")
    @directors_ns.response(200, "Success", model=director)
    @directors_ns.response(404, "Not found")
    def get(self, gid):
        genre = director_services.get_one(gid)

        if not genre:
            return f"genre with id {gid}, not found", 404

        return DirectorSchema().dump(genre), 200
