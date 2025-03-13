A user class:
## Constructor
    constructor(fullname, user_type): initialize fullname, user_type, and an empty borrowed_books list
## Function
    function display_name(): return the user's fullname
    function borrow_book(book): if fewer than 5 books are borrowed and the book is available, add it and mark as borrowed; otherwise, print an appropriate message
    function return_book(book): if the book is borrowed, remove it and mark it as available; otherwise, print an appropriate message
    function view_borrowed_books(): print the list of borrowed books along with their due dates (or "n/a" if no due date)
