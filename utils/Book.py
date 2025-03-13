from datetime import datetime, timedelta
from utils.User import User

class Book:
    def __init__(self,  book_title, author):
        self._book_title = book_title
        self._author_name = author
        self._status = "Available"
        self._due_date = None

    def reserve(self): # this will reserve a book if available 
        if self._status == "Available":
            self._status = "Reserved"
            print("The book '{}' has been reserved.".format(self._book_title))
        else:
            print("The Book '{}' is not available for reservation.".format(self._book_title))

    def set_due_date(self, days=14):
        self._due_date = datetime.now() + timedelta(days=days)

    @property
    def author_name(self):
        return self._author_name #Read author Only
        
    @property
    def status(self):
        return self._status # read status

    @status.setter
    def status(self, value):
        self._status = value #able to modify value

    @property
    def due_date(self):
        return self._due_date
        
    @property
    def book_title(self):
        return self._book_title #Read title Only