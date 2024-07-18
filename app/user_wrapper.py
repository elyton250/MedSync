# app/user_wrapper.py

from flask_login import UserMixin

class UserWrapper(UserMixin):
    def __init__(self, user_dict, role):
        self.user_dict = user_dict
        self.role = role
        self.id = user_dict['_id']
    
    @property
    def is_active(self):
        # Implement logic to check if the user is active
        return True
    
    @property
    def is_authenticated(self):
        # Implement logic to check if the user is authenticated
        return True
    
    @property
    def is_anonymous(self):
        # Implement logic to check if the user is anonymous
        return False
    
    def get_id(self):
        return str(self.id)
