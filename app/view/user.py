from flask_restx import Resource, Namespace

from app.container import user_service
from app.dao.model.user import UserSchema

from app.setup.api.models import user

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @user_ns.doc(desciption="Get users")
    @user_ns.response(200, "Success", model=user)
    @user_ns.response(404, "Not found")
    def get(self):
        users = user_service.get_all()

        if not users:
            return "users not found", 404

        res = UserSchema(many=True).dump(users)

        return res, 200

    def post(self, data):
        pass


@user_ns.route('/<int:gid>')
class UserView(Resource):
    @user_ns.doc(desciption="Get users")
    @user_ns.response(200, "Success", model=user)
    @user_ns.response(404, "Not found")
    def get(self, gid):
        user = user_service.get_one(gid)

        if not user:
            return f"user with id {gid}, not found", 404

        return UserSchema().dump(user), 200

    def put(self):
        pass
