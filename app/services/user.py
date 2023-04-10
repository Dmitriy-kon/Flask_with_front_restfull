from app.dao.user import UserDao


class UserService:
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def get_all(self):
        return self.user_dao.get_all()

    def create(self, data: dict):
        user = self.user_dao.create(data)
        return user

    def update(self, uid, data):
        self.user_dao.update(uid, data)

    def delete(self, uid):
        self.user_dao.delete(uid)

    # @staticmethod
    # def __validate_data(data: dict, is_create=None):
    #     if is_create:
    #         return set(data.keys()) == {'email', 'password', 'name', 'surname', 'favorite_genre'}
