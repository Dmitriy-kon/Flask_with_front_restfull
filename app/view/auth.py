from flask import request
from flask_restx import Namespace, Resource, abort
from marshmallow import ValidationError

from app.container import user_service, auth_service
from app.dao.model import UserSchema

from app.exceptions import UserAlreadyExist, ItemNotFound, IncorrectPassword, InvalidToken
from app.setup.api.models import auth, tokens_model

auth_ns = Namespace('auth', description='Authorization and authentication')


@auth_ns.route('/register/')
class AuthView(Resource):

    @auth_ns.doc(description='User registration', body=auth)
    @auth_ns.response(201, 'User registered')
    @auth_ns.response(400, 'Bad Request')
    def post(self):
        credentials = {
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }
        if None in credentials.values():
            abort(400, "wrong fields passed")

        try:
            data = UserSchema().load(credentials)
            user = user_service.create(data)
            return '', 201, {"location": f"/user/{user.id}"}
        except ValidationError:
            abort(400, "Not valid data passed")
        except UserAlreadyExist:
            abort(400, "user already exist")


@auth_ns.route('/login/')
class AuthLoginView(Resource):

    @auth_ns.doc(description='Get tokens', body=auth)
    @auth_ns.response(201, 'Tokens created', tokens_model)
    @auth_ns.response(400, 'Bad Request, not valid data passed')
    @auth_ns.response(401, 'Unauthorized, wrong password')
    @auth_ns.response(404, 'Not Found, no user with such e-mail')
    def post(self):
        credentials = {
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }
        if None in credentials.values():
            abort(400, "wrong fields passed")

        try:
            user = user_service.get_by_email(credentials['email'])
            tokens = auth_service.generate_tokens(credentials)
            return tokens, 201
        except ItemNotFound:
            abort(401, 'User not found')
        except IncorrectPassword:
            abort(401, 'Incorrect password')

    @auth_ns.doc(description='Get new tokens', body=tokens_model)
    @auth_ns.response(201, 'Tokens created', tokens_model)
    @auth_ns.response(401, 'Invalid refresh token')
    def put(self):
        try:
            # Check data valid
            refresh_token = request.json.get('refresh_token')
            if not refresh_token:
                abort(400, 'Not valid data passed')

            # Get tokens
            tokens = auth_service.approve_token(refresh_token)
            return tokens, 201
        except InvalidToken:
            abort(401, 'Invalid token passed')
