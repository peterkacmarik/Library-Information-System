class Book:
    def __init__(self, name: str, author: str, year_publication: int) -> None:
        """The constructor of the Book class initializes the class attributes

        Args:
            name (str): The "name" attribute represents the name of the book
            author (str): The "author" attribute represents the name of the author of the book
            year_publication (int): The "year_publication" attribute represents the year of publication of the book
        """
        self.name = name
        self.author = author
        self.year_publication = year_publication
        
    def __str__(self) -> str:
        """Displays the text form of the Book object

        Returns:
            str: Returns the text form of the attributes
        """
        return f"Name Book: {self.name}, Author: {self.author}, Year: {self.year_publication}"