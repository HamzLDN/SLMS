import json
import hashlib
import os

class Signup:
    def __init__(self, data, json_file='userdata/users.json'):
        self.fullname = data['fullname']
        self.email = data['email']
        self.username = data['username']
        self.__password = hashlib.sha256(data['password'].encode()).hexdigest()
        self.json_file = json_file

    def check_user(self):
        with open(self.json_file, 'r') as file:
            users = json.load(file)
        
        for ids in users:
            if self.username == users[ids]['username']:
                print("username taken")
                return True
        return False

    def register(self):
        if self.check_user(): return False
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, 'r') as f:
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
            "Full name":    self.fullname,
            "email":        self.email,
            "username":     self.username,
            "password":     self.__password,
        }

        with open(self.json_file, 'w') as f:
            json.dump(users, f, indent=4)
        print(f"User {self.username} added successfully with ID {next_id}!")
        return True
        