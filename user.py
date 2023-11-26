from database_users import Database


class User:
    database = Database()
    
    @classmethod
    def borrow_book_from_library(cls, book_id: int):
        """The method of borrowing a book from the library

        Args:
            book_id (int): Represents the ID of the book in the database

        Returns:
            return: Return True if the condition is met
            return: Return False if the condition is not met
        """
        conn = cls.database.connect_to_database()
        cursor = conn.cursor()
        
        # Search book with ID
        cursor.execute(
            "SELECT * FROM book WHERE id=%s", (book_id,)
        )
        # List of books in the database
        book_in_library = cursor.fetchall()
        
        # If the condition is met, add the book to the user's database and return True, otherwise return False
        if book_in_library:
            for book in book_in_library:
                #print(f"Book ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year: {book[3]}")
                cursor.execute(
                        "INSERT INTO loaned_books (name, author, year_publication)"
                        "VALUES (%s, %s, %s);", (book[1], book[2], book[3])
                    )
                conn.commit()
                conn.close()
            return True
        else:
            return False

    @classmethod
    def return_borrowed_book(cls, book_id: int):
        """ Return the borrowed book to the library

        Args:
            book_id (int): Represents the ID of the book in the database

        Returns:
            return: Return True if the condition is met
            return: Return False if the condition is not met
        """
        conn = cls.database.connect_to_database()
        cursor = conn.cursor()
        
        # Search book with ID
        cursor.execute(
            "SELECT * FROM loaned_books WHERE id=%s", (book_id,)
        )
        # List of books in the database
        book_from_user_library = cursor.fetchall()
        
        if book_from_user_library:
            for book in book_from_user_library:
                #print(f"Book ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year: {book[3]}")
            
                cursor.execute(
                        "INSERT INTO book (name, author, year_publication)"
                        "VALUES (%s, %s, %s);", (book[1], book[2], book[3])
                    )
                conn.commit()
                conn.close()
            return True
        else:
            False
    
    @classmethod
    def delete_user_book(cls,book_id):
        """_summary_

        Args:
            book_id (int): Represents the ID of the book in the database

        Returns:
            return: Return the book ID
        """
        # Set updated data
        conn = cls.database.connect_to_database()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM loaned_books WHERE id=%s", (book_id,)
        )
        found_book = cursor.fetchall()
        if found_book:
            cursor.execute(
                "DELETE FROM loaned_books WHERE id=%s", (book_id,)
            )
             
            conn.commit()
            conn.close()
        return book_id
    
    @classmethod
    def view_books(cls):
        """_summary_

        Returns:
            return: Return list all book in database
            return: Return False if the condition is not met
        """
        conn = cls.database.connect_to_database()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM loaned_books;"
        )
        
        all_books = cursor.fetchall()
        conn.commit()
        conn.close()
        
        list_all_books = []
        if list_all_books:
            for one_row_book in all_books:
                list_all_books.append(f"\tID: {one_row_book[0]} Name: {one_row_book[1]} Author: {one_row_book[2]} Year: {one_row_book[3]}")
            return list_all_books
        else:
            return False