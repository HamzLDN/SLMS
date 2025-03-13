import json
from src.handleuser.signup import Signup
from src.handleuser.login import Login
from utils.Administrator import Administrator
from utils.Member import Member
from utils.Book import Book
from utils.Librarian import Librarian
from utils.User import User


class Library:
    def __init__(self):
        self._books = []
        self._users = []

    def add_book(self, book):
        self._books.append(book)
        print("Book '{}' by {} added to the library.".format(book.book_title, book.author_name))

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)
            print("Book '{}' by {} removed from the library.".format(book.book_title, book.author_name))
        else:
            print("Book '{}' not found in the library.".format(book.book_title))

    def search_books(self, book_title=None, author_name=None):
        found_books = []

        for book in self._books:
            title_match = book_title and book_title.lower() in book.book_title.lower()
            author_match = author_name and author_name.lower() in book.author_name.lower()

            if title_match or author_match:
                found_books.append(book)

        return found_books


    def get_book_by_title(self, title):
        """Method to get a book by its title."""
        for book in self._books:
            if title.lower() == book.book_title.lower():
                return book
        return None 

    def add_user(self, user):
        self._users.append(user)
        print(f"User {user.display_name()} added to the library.")

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            print(f"User {user.display_name()} removed from the library.")
        else:
            print(f"User {user.display_name()} not found.")


if __name__ == "__main__":
    library = Library()

    # Create books and add to the library
    book1 = Book("Python Programming", "John Doe")
    book2 = Book("Learn Data Science", "Jane Smith")
    library.add_book(book1)
    library.add_book(book2)

    # Initialize member, librarian, and admin users
    member = Member("saffie")
    librarian = Librarian("bob")
    admin = Administrator("alice")
    
    library.add_user(member)
    library.add_user(librarian)
    library.add_user(admin)
    print("Books in library:")

    while True:
        command = input("Enter a command (or 'help' for options): ").lower().split(" ")
        
        if command[0] == 'search':
            if len(command) > 1:
                book_title = " ".join(command[1:])
                member.search_books(library, book_title=book_title)  # Call search_books on member
            else:
                print("Please specify a book title to search for.")
        
        elif command[0] == 'borrow':
            if len(command) > 1:
                book_title = " ".join(command[1:])
                book = library.get_book_by_title(book_title)
                if book:
                    member.borrow_book(book)
                else:
                    print(f"Book '{book_title}' not found.")
            else:
                print("Please specify a book title to borrow.")
        
        elif command[0] == 'reserve':
            if len(command) > 1:
                book_title = " ".join(command[1:])
                book = library.get_book_by_title(book_title)
                if book:
                    member.reserve_book(book)
                else:
                    print(f"Book '{book_title}' not found.")
            else:
                print("Please specify a book title to reserve.")

        elif command[0] == 'view':
            if len(command) > 1 and command[1] == 'borrowed':
                member.view_borrowed_books()
        
        elif command[0] == 'add':
            if len(command) > 1:
                entity = command[1]
                
                if entity == 'book' and len(command) > 2:
                    book_title = " ".join(command[2:])
                    author = input("Enter author name: ")
                    new_book = Book(book_title, author)
                    library.add_book(new_book)

                elif entity == 'user' and len(command) > 2:
                    user_type = command[2].capitalize()
                    user_name = " ".join(command[3:])
                    if user_type == "Member":
                        new_user = Member(user_name)
                    elif user_type == "Librarian":
                        new_user = Librarian(user_name)
                    elif user_type == "Administrator":
                        new_user = Administrator(user_name)
                    else:
                        print(f"Unknown user type '{user_type}'.")
                        continue
                    library.add_user(new_user)

                else:
                    print("Please provide valid arguments to add a book or user.")
        
        elif command[0] == 'remove':
            if len(command) > 1:
                entity = command[1]

                if entity == 'book' and len(command) > 2:
                    book_title = " ".join(command[2:])
                    book = library.get_book_by_title(book_title)
                    if book:
                        library.remove_book(book)
                    else:
                        print(f"Book '{book_title}' not found.")

                elif entity == 'user' and len(command) > 2:
                    user_name = " ".join(command[2:])
                    user = next((u for u in library._users if u.display_name() == user_name), None)
                    if user:
                        library.remove_user(user)
                    else:
                        print(f"User '{user_name}' not found.")

                else:
                    print("Please provide valid arguments to remove a book or user.")
        
        elif command[0] == 'exit':
            print("Exiting the program...")
            break

        elif command[0] == 'help':
            print("Available commands:")
            print("  search [book_title] - Search for a book")
            print("  borrow [book_title] - Borrow a book")
            print("  reserve [book_title] - Reserve a book")
            print("  view borrowed - View borrowed books")
            print("  add book [book_title] - Add a new book")
            print("  add user [user_type] [user_name] - Add a new user (types: Member, Librarian, Administrator)")
            print("  remove book [book_title] - Remove a book")
            print("  remove user [user_name] - Remove a user")
            print("  exit - Exit the program")
        
        else:
            print("Unknown command. Type 'help' for options.")
