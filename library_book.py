from database_users import Database


class LibraryBook:
    database = Database()
    
    @classmethod
    def add_book_to_library(cls, name: str, author: str, year_publication: int):
        """The class method adds the book to the library database

        Args:
            name (str): The "name" attribute represents the name of the book
            author (str): The "author" attribute represents the name of the author of the book
            year_publication (int): The "year_publication" attribute represents the year of publication of the book

        Returns:
            name (str): Return the string of the name of the book
        """
        conn = cls.database.connect_to_database()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO book (name, author, year_publication)"
            "VALUES (%s, %s, %s);", (name, author, year_publication)
        )
        
        conn.commit()
        conn.close()
        
        return name
    
    @classmethod
    def view_books(cls):
        """The method displays all the books that are in the database

        Returns:
            list: Returns a list of all books
        """
        conn = cls.database.connect_to_database()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM book;"
        )
        
        rows_books = cursor.fetchall()
        
        conn.commit()
        conn.close()
        
        list_all_books = []
        
        for row_book in rows_books:
            list_all_books.append(f"\tID: {row_book[0]} Name: {row_book[1]} Author: {row_book[2]} Year: {row_book[3]}")
        return list_all_books
    
    @classmethod
    def delete_library_book(cls, book_id: int):
        """The method removes the book from the database

        Args:
            book_id (int): Represents the ID of the book in the database
        """
        conn = cls.database.connect_to_database()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM book WHERE id=%s", (book_id,)
        )
        
        found_book = cursor.fetchall()
        if found_book:
            cursor.execute(
                "DELETE FROM book WHERE id=%s", (book_id,)
            )
        
        conn.commit()
        conn.close()