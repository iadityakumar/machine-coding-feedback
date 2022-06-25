

class UserService:


    @classmethod
    def get_user(self, users, name):
        for user in users:
            if user.name == name:
                return user
