from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, name, password):
        self.name = name
        self.id = id
        self.password = password

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)
