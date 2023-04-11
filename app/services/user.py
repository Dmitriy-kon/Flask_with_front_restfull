import hashlib

from flask import current_app

from app.dao.model.user import User
from app.dao.user import UserDao
from app.exceptions import ItemNotFound, UserAlreadyExist
from app.tools.security import Security_hash


class UserService:
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    def get_by_email(self, email: str) -> User:
        user = self.user_dao.get_by_email(email)

        if not user:
            raise ItemNotFound

        return user

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def get_all(self):
        return self.user_dao.get_all()

    def create(self, data: dict):
        try:
            user = self.get_by_email(data.get('email'))
            if user:
                raise UserAlreadyExist

        except ItemNotFound:

            data['password'] = Security_hash(). \
                generate_password_hash(data.get('password'))

            # data['password'] = self.create_hash(data.get('password'))

            user = self.user_dao.create(data)
            return user

    def update(self, uid, data: dict):
        if 'password' in data:
            data['password'] = Security_hash(). \
                generate_password_hash(data.get('password'))

        return self.user_dao.update(uid, data)

    def delete(self, uid):
        self.user_dao.delete(uid)

    # def create_hash(self, password: str) -> bytes:
    #     """Create sha256 password hash"""
    #     hash_digest: bytes = hashlib.pbkdf2_hmac(
    #         'sha256',
    #         password.encode('utf-8'),
    #         current_app.config.get('PWD_HASH_SALT'),
    #         current_app.config.get('PWD_HASH_ITERATIONS')
    #     )
    #     return hash_digest

    # @staticmethod
    # def __validate_data(data: dict, is_create=None):
    #     if is_create:
    #         return set(data.keys()) == {'email', 'password', 'name', 'surname', 'favorite_genre'}
