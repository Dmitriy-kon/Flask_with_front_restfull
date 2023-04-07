from app.dao.user import UserDao


class UserService:
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    def get_one(self, uid):
        return self.user_dao.get_one(uid)

    def get_all(self):
        return self.user_dao.get_all()
