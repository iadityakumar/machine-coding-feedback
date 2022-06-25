
from services.user_service import UserService


class CustomerService(UserService):


    @classmethod
    def get_customer(self, users, name):
        return super().get_user(users, name)


    @classmethod
    def get_customer_trips(self, customer, trips):
        return [t for r in trips if t.customer == customer]
