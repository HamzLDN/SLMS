import json
from src.signup import Signup

Signup("admin", "secret").add_user()
Signup("test", "secret").add_user()