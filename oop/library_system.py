class Book:
    def __init__(self, title, author):
        """
        Base class for a Book.
        Initializes the title and author attributes.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of the Book instance.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Derived class for an EBook.
        Inherits from Book and adds a file_size attribute.
        """
        super().__init__(title, author)  # Initialize base class attributes
        self.file_size = file_size

    def __str__(self):
        """
        String representation of the EBook instance.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Derived class for a PrintBook.
        Inherits from Book and adds a page_count attribute.
        """
        super().__init__(title, author)  # Initialize base class attributes
        self.page_count = page_count

    def __str__(self):
        """
        String representation of the PrintBook instance.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """
        Library class demonstrating composition.
        Manages a collection of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        for book in self.books:
            print(book)