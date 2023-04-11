import datetime
import calendar

import jwt

from flask_restx import abort
from flask import current_app

from app.exceptions import IncorrectPassword
from app.services.user import UserService
from app.tools.security import Security_hash


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, credentials: dict, is_refresh: bool = False) -> dict:

        email_passed = credentials.get('email')
        password_passed = credentials.get('password')
        user = self.user_service.get_by_email(email_passed)

        if not user:
            abort(404, "User not found")

        # check password
        if not is_refresh:
            password_is_correct = Security_hash().compare_password(user.password, password_passed)
            if not password_is_correct:
                raise IncorrectPassword

        # Generate token data
        token = {
            'email': user.email
        }

        # Generate access token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(
            minutes=current_app.config.get('TOKEN_EXPIRE_MINUTES'))

        token["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(
            token,
            current_app.config.get('SECRET_HERE'),
            algorithm=current_app.config.get('JWT_ALGORITHM'))

        # Generate refresh token

        day30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        token["exp"] = calendar.timegm((day30.timetuple()))

        refresh_token = jwt.encode(
            token,
            current_app.config.get('SECRET_HERE'),
            algorithm=current_app.config.get('JWT_ALGORITHM'))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
