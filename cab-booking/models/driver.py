from models.user import User
from constants import DRIVER_STATUSES, ACTIVE, INACTIVE


class Driver(User):

    def __init__(self,  name):
        super().__init__(name)
        self.status = ACTIVE


    def set_status(self, status=ACTIVE):
        self.status = status

    def is_inactive(self):
        return self.status == INACTIVE
