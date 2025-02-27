import json
import hashlib

text = "Hello, world!"


class login:
    def __init__(self, username, password, database="userdata/users.json"):
        self.username = username
        self.
        self.__password = password
        self.database = database

    def read_db(self):
        with open(self.database, 'r') as f:
            return f.read()

    def write_db(self, data):
        with open(self.database, 'w'):
            data.write(self.database)

    
    def checkhash(self, ):
        return self.__password == hashlib.sha256(self.__password).hexdigest()
        
    
login("admin", text).checkhash()