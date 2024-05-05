# user_management.py

from models import User
import storage

#   """Represents a user of the library.
    
#     Attributes:
#         name (str): The name of the user.
#         user_id (str): The ID of the user.
#     """
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users.append(new_user)
        self._save_users()

    def delete_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
        self._save_users()

    def _save_users(self):
        data = [user.to_dict() for user in self.users]
        storage.save_to_file(data, "users.json")

    def load_users(self):
        data = storage.load_from_file("users.json")
        self.users = [User(user['name'], user['user_id']) for user in data]
