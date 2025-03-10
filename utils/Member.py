class Member(User):
    def __init__(self, name):
        super().__init__(name, user_type="Member")

    def search_book(self, library, author_name=None book_title=None):
        books_found = library.search_books(title, author_name)
        if books_found:
            print("We've found a few books for you")
            for book in books_found:
                print("{} by {}: {}".format(book.book_title, book.author_name, book.status))
        else:
            print("No books available at the moment.\nPlease try again later")
