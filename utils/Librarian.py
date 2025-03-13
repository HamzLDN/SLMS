from utils.User import User
class Librarian(User):
    def __init__(self, info):
        super().__init__(info, user_type="Librarian")
        self._info = info

    def get_status(self):
        return self._user_type

    def display_name(self):
        return self._info
        

    def manage_books(self, library, command, book=None):
        if command == "add": library.add_book(book)
        elif command == "remove": library.remove_book(book)
        elif command == "update": library.update_book(book)
        else: print("Cannot apply changes.")
