import json
from src.handleuser.signup import Signup
from src.handleuser.login import Login

# Signup("First name", "email@gmail.com", "admin", "secret").register()
# session = Login("admin", "secret".encode()).access()
# print(session)

class User:
    def __init__(self, name, user_type):
        self._name = name
        self._user_type = user_type
        self._borrowed_books = []
