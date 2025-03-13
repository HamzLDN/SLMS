class User:
    def __init__(self, fullname, user_type):
        self._fullname = fullname #encapsulation
        self.user_type = user_type
        self._borrowed_books = []

    def display_name(self):
        return self._fullname

    def borrow_book(self, book):
        if len(self._borrowed_books) < 5:
            if book.status == "Available":
                self._borrowed_books.append(book)
                book.status = "Borrowed"
                print(f"{self.display_name()} borrowed {book.book_title}.")
            else:
                print(f"{book.book_title} is not available.")
        else:
            print("You can only borrow up to 5 books.")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.status = "Available"
            print(f"{self.display_name()} returned {book.book_title}.")
        else:
            print(f"{self.display_name()} has not borrowed {book.book_title}.")

    def view_borrowed_books(self):
        print(f"{self.display_name()}'s borrowed books:")
        for book in self._borrowed_books:
            print(f"- {book.book_title} (Due: {book.due_date if book.due_date else 'N/A'})")
