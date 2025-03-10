class Book:
    def __init__(self,  book_title, author):
        self._title = book_title
        self._author = author
        self._status = "Available"
        self._due_date = None

    def reserve(self): # this will reserve a book if available 
        if self._status == "Available":
            self._status = "Reserved"
            print("The book '{}' has been reserved.".format(self._title))
        else:
            print("The Book '{}' is not available for reservation.".format(self._title))
