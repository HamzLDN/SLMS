class Librarian(User):
    def __init__(self, name):
        super().__init__(name: str, user_type="Librarian")

    def manage_books(self, library, command, book=None):
        if command == "add": library.add_book(book)
        elif command == "remove": library.remove_book(book)
        elif command == "update": library.update_book(book)
        else: print("Cannot apply changes.")
