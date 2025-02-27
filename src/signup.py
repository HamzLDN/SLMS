import json
import hashlib
import os

class Signup:
    def __init__(self, username, password):
        self.username = username
        self.__password = hashlib.sha256(password.encode()).hexdigest()
    
    def add_user(self):
        json_file = 'userdata/users.json'

        if os.path.exists(json_file):
            try:
                with open(json_file, 'r') as f:
                    users = json.load(f)
                if not isinstance(users, dict):
                    raise ValueError("Invalid JSON structure.")
            except (json.JSONDecodeError, ValueError):
                users = {}
        else:
            users = {}

        numeric_keys = [int(k) for k in users.keys() if k.isdigit()]
        next_id = str(max(numeric_keys, default=0) + 1)

        users[next_id] = {
            "username": self.username,
            "password": self.__password
        }

        with open(json_file, 'w') as f:
            json.dump(users, f, indent=4)

        print(f"User {self.username} added successfully with ID {next_id}!")

