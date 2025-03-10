import json
from src.handleuser.signup import Signup
from src.handleuser.login import Login

Signup("First name", "email@gmail.com", "admin", "secret").register()
session = Login("admin", "secret".encode()).access()
print(session)