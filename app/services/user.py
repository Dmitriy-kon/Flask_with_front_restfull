import hashlib

from flask import current_app
from werkzeug.exceptions import MethodNotAllowed

from app.dao.model.user import User
from app.dao.user import UserDao
from app.exceptions import ItemNotFound, UserAlreadyExist, IncorrectPassword
from app.tools.security import Security_hash


class UserService:
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    def get_by_email(self, email: str) -> User:
        user = self.user_dao.get_by_email(email)

        if not user:
            raise ItemNotFound

        return user

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

    def update_info(self, data: dict, email: str) -> None:
        """
        :raises MethodNotAllowed: If changing email or password
        """

        # Check user exists
        self.get_by_email(email)

        # Check data is okay
        if 'password' not in data.keys() and 'email' not in data.keys():
            self.user_dao.update_by_email(data, email)
        else:
            raise MethodNotAllowed

    def update_password(self, data: dict, email: str):
        user = self.get_by_email(email)
        current_password = data.get('old_password')
        new_password = data.get('new_password')

        if None in {current_password, new_password}:
            raise MethodNotAllowed

        if not Security_hash().compare_password(user.password, current_password):
            raise IncorrectPassword

        data = {
            'password': Security_hash().generate_password_hash(new_password)
        }
        self.user_dao.update_by_email(data, email)

    def delete(self, uid):
        self.user_dao.delete(uid)
