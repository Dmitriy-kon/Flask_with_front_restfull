from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import ValidationError
from werkzeug.exceptions import MethodNotAllowed

from app.container import user_service, auth_service
from app.dao.model import UserSchema

from app.exceptions import ItemNotFound, IncorrectPassword
from app.setup.api.models import user, passwords

user_ns = Namespace('users')


# @user_ns.route('/')
# class UsersView(Resource):
#     @user_ns.doc(desciption="Get users")
#     @user_ns.response(200, "Success", model=user)
#     @user_ns.response(404, "Not found")
#     def get(self):
#         users = user_service.get_all()
#
#         if not users:
#             return "users not found", 404
#
#         res = UserSchema(many=True).dump(users)
#
#         return res, 200
#
#     @user_ns.doc(desciption="Get users", body=user)
#     @user_ns.response(201, "Created")
#     @user_ns.response(400, "Validation Error")
#     def post(self):
#         try:
#             data = UserSchema().load(request.json)
#         except ValidationError as er_:
#             return f"{er_}", 400
#
#         user = user_service.create(data)
#
#         return f"Data added with id {user.id}", 201, {"location": f"users/{user.id}"}


@user_ns.route('/')
class UserView(Resource):
    @user_ns.doc(desciption="Get users")
    @auth_service.auth_required
    @user_ns.response(200, "Success", user)
    @user_ns.response(404, "Not found")
    def get(self):
        try:
            # Get token
            auth_data = request.headers['Authorization']
            token = auth_data.split('Bearer ')[-1]
            email = auth_service.get_email_from_token(token)

            # Get and update data
            user = user_service.get_by_email(email)
            user_d = UserSchema().dump(user)

            return user_d, 200
        except ItemNotFound:
            abort(404, "User not found")

    @user_ns.doc(description='Get user by id', body=user)
    @auth_service.auth_required
    @user_ns.response(200, 'User updated', user)
    @user_ns.response(405, 'Method not allowed')
    @user_ns.response(404, 'Not Found')
    @user_ns.response(404, 'Wrong fields passed')
    def patch(self):
        try:
            # Get token
            auth_data = request.headers['Authorization']
            token = auth_data.split('Bearer ')[-1]
            email = auth_service.get_email_from_token(token)

            # Get and update data
            update_data = UserSchema().dump(request.json)
            user_service.update_info(update_data, email)

            return '', 200
        except MethodNotAllowed:
            abort(405, "You're not allowed to change the data passed")
        except ItemNotFound:
            abort(404, "User not found")
        except ValidationError:
            abort(404, "Wrong fields passed")


@user_ns.route('/password/')
class PasswordView(Resource):

    @user_ns.doc(description='Update user password', body=passwords)
    @auth_service.auth_required
    @user_ns.response(200, 'Password updated', user)
    @user_ns.response(404, 'Not Found')
    @user_ns.response(401, 'Password is incorrect')
    @user_ns.response(405, 'Method not allowed')
    def put(self):
        try:
            # Get token
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = auth_service.get_email_from_token(token)

            # Get data and update data
            passwords = request.json
            user_service.update_password(passwords, email)
            return '', 200
        except ItemNotFound:
            abort(404, "User not found")
        except IncorrectPassword:
            abort(401, "Password is incorrect")
        except MethodNotAllowed:
            abort(405, "Invalid data passed")
