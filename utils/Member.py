from utils.User import User
class Member(User):
    def __init__(self, info):
        super().__init__(info, user_type="Member")

    def search_books(self, library, author_name=None, book_title=None):
        books_found = library.search_books(book_title=book_title, author_name=author_name)

        if books_found:
            print("We've found a few books for you:")
            for book in books_found:
                print(f"{book.book_title} by {book.author_name}: {book.status}")
        else:
            print("No books available at the moment.\nPlease try again later.")

    def reserve_book(self, book):
        book.reserve()
