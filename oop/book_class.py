class Book:
    def __init__(self, title, author, year):
        """
        Constructor for the Book class.
        Initializes the title, author, and year attributes.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor for the Book class.
        Prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        Returns a formatted string with the title, author, and year.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.
        Returns a string that can be used to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"