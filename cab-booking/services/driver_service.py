
from services.user_service import UserService


class DriverService(UserService):


    @classmethod
    def get_driver(self, users, name):
        return super().get_user(users, name)
