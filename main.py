import json
from src.handleuser.signup import Signup
from src.handleuser.login import Login
impor
Signup("aadmin", "secret").register()

session = Login("aadmin", "secret".encode()).access()
print(session)