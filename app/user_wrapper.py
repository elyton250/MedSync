# app/user_wrapper.py

from flask_login import UserMixin

class UserWrapper:
    def __init__(self, user, role):
        self.user = user
        self.role = role

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user.get('_id'))

    @property
    def first_name(self):
        return self.user.get('first_name')

    @property
    def last_name(self):
        return self.user.get('last_name')

    @property
    def _id(self):
        return self.user.get('_id')

