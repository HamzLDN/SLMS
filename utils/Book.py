from datetime import datetime
import timedelta
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

    def set_due_date(self, days=14):
        self._due_date = datetime.now() + timedelta(days=days)

    @property
    def author(self):
        return self._author #Read author Only
        
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
    def title(self):
        return self._title #Read title Only



