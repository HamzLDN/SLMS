class library:
    constructor:
        initialize empty lists for books and users

    function add_book(book):
        add the book to the books list and print a confirmation message

    function remove_book(book):
        if the book is in the books list, remove it and print a confirmation; otherwise, print a not-found message

    function search_books(book_title=None, author_name=None):
        initialize an empty list called found_books
        for each book in the books list:
            if the provided book_title is found in the book's title (case-insensitive) or the provided author_name is in the book's author (case-insensitive), add the book to found_books
        return found_books

    function get_book_by_title(title):
        for each book in the books list:
            if the book's title matches the given title exactly (case-insensitive), return that book
        return none

    function add_user(user):
        add the user to the users list and print a confirmation message

    function remove_user(user):
        if the user exists in the users list, remove them and print a confirmation; otherwise, print a not-found message

main:
    create an instance of library
    create two book objects with titles and authors, then add them to the library
    create instances for member, librarian, and administrator, and add them to the library
    loop indefinitely:
        prompt the user for a command and split the input into parts
        if the command is "search":
            if a book title is provided, call member.search_books with the library and book title; otherwise, print an error message
        else if the command is "borrow":
            if a book title is provided, retrieve the book from the library by title and if found, call member.borrow_book(book); otherwise, print an error message
        else if the command is "reserve":
            if a book title is provided, retrieve the book from the library by title and if found, call member.reserve_book(book); otherwise, print an error message
        else if the command is "view borrowed":
            call member.view_borrowed_books()
        else if the command is "add":
            if adding a book: extract the book title from the command, prompt for the author, create a new book, and add it to the library
            if adding a user: extract the user type and user name from the command, create a new user of the specified type, and add them to the library
        else if the command is "remove":
            if removing a book: extract the book title, retrieve the book from the library, and if found, remove it; otherwise, print an error message
            if removing a user: extract the user name, search for the user in the library's users list, and if found, remove them; otherwise, print an error message
        else if the command is "exit":
            print an exit message and break the loop
        else if the command is "help":
            print the list of available commands
        else:
            print an unknown command message
