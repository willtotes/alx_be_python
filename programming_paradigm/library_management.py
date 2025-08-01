
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")
        
book1 = Book("B001", "Things Fall Apart", "Chinua Achebe")

print("Name:", book1.name)
print("Title:", book1.title)
print("Author:", book1.author)
print("Year:", book1.year)

print("Checked out?", book1.is_checked_out())

book1.check_out()
print("Checked out?", book1.is_checked_out())

book1.return_book()
print("Checked out?", book1.check_out())




Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self,