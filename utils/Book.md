    Creae class called book:
        define __init__(book_title, author):
            set book_title to input book_title
            set author_name to input author
            set status to "available"
            set due_date to none
    
        define reserve():
            if status is "available":
                set status to "reserved"
                print message: book has been reserved
            else:
                print message: book is not available for reservation
    
        define set_due_date(days=14):
            set due_date to current date + number of days
    
        define author_name (property):
            return author_name
    
        define status (property):
            return status
    
        define status setter(value):
            set status to input value
    
        define due_date (property):
            return due_date
    
        define book_title (property):
            return book_title
    
        Property is a get/setter. Helps protect memory through read/write
