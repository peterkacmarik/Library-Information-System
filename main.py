from library_book import LibraryBook
from user import *
from menu import menu
from validate import Validate


# Connect and create database table if not exist
# database = Database()
# database.connect_to_database()
# database.create_book_table()
# database.create_loaned_book_table()

while True:
    # The main loop of the program
    menu()
    # The menu function mainly displays the application menu
    select_option = input("Choose an option from the menu: ")
    # Validation of the input number
    Validate.validate_number_menu(select_option)
    
    if select_option == "6":
        # If the number 6 is selected, the application will end
        print("The application has ended...")
        break
    
    elif select_option == "1":
        # If the number 1 is selected, an object "book_added" will be created that will be added to the library database
        enter_name_book = input("\tEnter the title of the book: ").strip().capitalize()
        Validate.validate_input_text(enter_name_book)
        enter_author_book = input("\tEnter the author of the book: ").strip().capitalize()
        Validate.validate_input_text(enter_author_book)
        enter_year_book = input("\tEnter the year the book was published: ").strip()
        Validate.validate_input_number(enter_year_book)

        # Adding a book to the library database
        book_added = LibraryBook.add_book_to_library(enter_name_book, enter_author_book, enter_year_book)
        print(f"The Book: '{book_added}' has been added to the library")

    elif select_option == "2":
        #Displays all books in the library if the condition is met
        print("List of books in the library database:")
        list_books = LibraryBook.view_books()
        if list_books:
            for library_book in list_books:
                print(library_book)
        else:
            print("The list of books is empty!")
    
    elif select_option == "3":
        # Displays all user books in the library if the condition is met
        print("List of all the user's books:")
        list_user_books = User.view_books()
        if list_user_books:
            for user_book in list_user_books:
                print(user_book)
        else:
            print("The list of books is empty!")
            
    elif select_option == "4":
        # Entering the book id and validating the entry of the correct number
        book_id_for_borrowing = input("\tSelect the ID of the book you want to borrow from the library: ").strip()
        Validate.validate_book_id(book_id_for_borrowing)

        # Borrow a book from the library if it is in the library
        loaned_book = User.borrow_book_from_library(book_id_for_borrowing)
        while loaned_book:
            print(f"The Book with ID: {book_id_for_borrowing} has been added to the user's library")
            break
        else:
            print(f"The Book with ID: {book_id_for_borrowing} is not in the library")

        # Remove the book from the library
        LibraryBook.delete_library_book(book_id_for_borrowing)

    elif select_option == "5":
        # Entering the book id and validating the entry of the correct number
        id_returned_book = input("\tSelect the ID of the book you want to return to the library: ")
        Validate.validate_book_id(id_returned_book)
        
        # Return the book to the library if it is in the user's library
        book_to_return = User.return_borrowed_book(id_returned_book)
        while book_to_return:
            print(f"The Book with ID: {id_returned_book} was returned to the library")
            break
        else:
            print(f"The Book with ID: {id_returned_book} is not in the user library")
            
        # Remove the book from the library
        User.delete_user_book(id_returned_book)