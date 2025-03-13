class librarian inherits from user:
    constructor(info):
        call the parent constructor with info and user_type set to "librarian"
        store info in _info
## function 
    function get_status():
        return the user type of this librarian
## function 
    function display_name():
        return the stored info (which represents the librarian's name)
## function 
    function manage_books(library, command, optional book):
        if command equals "add":
            call library.add_book(book)
        else if command equals "remove":
            call library.remove_book(book)
        else if command equals "update":
            call library.update_book(book)
        else:
            print "cannot apply changes"
