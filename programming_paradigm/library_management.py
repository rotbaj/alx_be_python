# library_management.py

class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance with a title, author, and availability status.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Check out the book if it is available.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Return the book if it is checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Check if the book is available.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Return a string representation of the book.
        """
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self._books = []  # Private list to store books

    def add_book(self, book):
        """
        Add a book to the library.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title if it is available.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book}")
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """
        Return a book by title if it is checked out.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book}")
                return
        print(f"Book '{title}' is not checked out or does not exist.")

    def list_available_books(self):
        """
        List all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")