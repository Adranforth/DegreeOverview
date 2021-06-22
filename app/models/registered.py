from flask_login import UserMixin

class Registered(UserMixin):
    id=''
    def __init__(self, ID_num):
        self.id = ID_num
    def get_id(self):
        return self.id