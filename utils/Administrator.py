from src.handleuser.signup import Signup
from src.handleuser.login import Login
from src.handleuser import delete

class Administrator(User):
    def __init__(self, name):
        super().__init__(name, user_type="Administrator")

    def manage_user_accounts(self, library, action, user=None):
        if action == "add":
            if Signup("First name", "email@gmail.com", "username", "password").register(): #if its true
                library.add_user(user)
            else:
                print('username  has been taken')
        elif action == "remove":
            if remove.delete(user):
                library.remove_user(user)
            else:
              print("Cannot delete user")
        else:
            print("Invalid action.")
