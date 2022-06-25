from models.user import User

class Customer(User):

    def __init__(self, name):
        super().__init__(name)
