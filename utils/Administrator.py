
from src.handleuser import delete
from utils.User import User

class Administrator(User):
    def __init__(self, info):
        super().__init__(info, user_type="Administrator")

    
    def manage_user_accounts(self, library, action, user=None):
        if action == "add":
            library.add_user(user)
        elif action == "remove":
            library.remove_user(user)
        else:
            print("Invalid action.")