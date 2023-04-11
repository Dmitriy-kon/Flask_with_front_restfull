from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

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

    @user_ns.doc(desciption="Get users", body=user)
    @user_ns.response(201, "Created")
    @user_ns.response(400, "Validation Error")
    def post(self):
        try:
            data = UserSchema().load(request.json)
        except ValidationError as er_:
            return f"{er_}", 400

        user = user_service.create(data)

        return f"Data added with id {user.id}", 201, {"location": f"users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @user_ns.doc(desciption="Get users")
    @user_ns.response(200, "Success", model=user)
    @user_ns.response(404, "Not found")
    def get(self, uid):
        user = user_service.get_one(uid)

        if not user:
            return f"user with id {uid}, not found", 404

        return UserSchema().dump(user), 200

    @user_ns.doc(description='Update user', body=user)
    @user_ns.response(200, "Success", user)
    @user_ns.response(400, "Validation error")
    @user_ns.response(404, "Not found")
    def patch(self, uid):
        try:
            user1 = user_service.get_one(uid)
            data = UserSchema().load(request.json)

            if not user1:
                return f"User with id {uid}, no found", 404

        except ValidationError as er_:
            return f"{er_}", 400

        user = user_service.update(uid, data)

        return f"Data added with id {user.id}", 201, {"location": f"users/{user.id}"}

    @user_ns.doc(description="Delete user by id")
    @user_ns.response(204, "Success delete", user)
    @user_ns.response(404, "user with this id not found")
    def delete(self, uid):
        user = user_service.get_one(uid)

        if not user:
            return f"User with id {uid}, not found", 404

        user_service.delete(uid)

        return f"User with id {uid} deleted", 204
