import json
import hashlib
im

class Login:
    def __init__(self, username:str, password:str, database="userdata/users.json"):
        self.username = username
        self.__password = password
        self.database = database

    def read_db_password(self):
        with open(self.database, 'r') as f:
            info = json.load(f)
        
        for user in info:
            if info[user]['username'] == self.username:
                return info[user]['password']
        return False
    
    def access(self):
        # It will compare the hash of the password
        db_password = self.read_db_password()
        if not db_password: return False
        return db_password.encode() == hashlib.sha256(self.__password).hexdigest().encode()
    