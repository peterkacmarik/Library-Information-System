import re


class Validate:
    
    @staticmethod
    def validate_number_menu(menu_number: int):
        """Validation number entered at the input

        Args:
            menu_number (int): The argument represents a menu number

        Raises:
            ValueError: ValueError catches errors on input
        """
        pattern = r'^[1-6]$'
        try:
            if not re.match(pattern, str(menu_number)):
                raise ValueError("Enter only a number in the range 1-6")
        except ValueError as e:
            print(e)

    @staticmethod
    def validate_input_text(input_text: str):
        """Validation of the text entered at the input

        Args:
            input_text (str): The argument represents the text entered at the input

        Raises:
            ValueError: ValueError catches errors on input
        """
        pattern = r'^[a-zA-Z]{3,}\w+(\s+\w+)*$'
        while True:
            if re.match(pattern, str(input_text)):
                break
            else:
                try:
                    if not re.match(pattern, str(input_text)):
                        raise ValueError("Enter min. 3 characters. The text can only contain letters")
                except ValueError as e:
                    print(e)
                input_text = input("\tEnter the title of the book: ").strip().capitalize()

    @staticmethod
    def validate_input_number(input_number: int):
        """Method for validating the number entered as the year of publication of the book

        Args:
            input_number (int): The argument represents the year the book was published

        Raises:
            ValueError: ValueError catches errors on input
        """
        pattern = r'^\d{4}$'
        while True:
            if re.match(pattern, str(input_number)):
                    break
            else:
                try:
                    if not re.match(pattern, str(input_number)):
                        raise ValueError("Enter min. 3 characters. The text can only contain numbers")
                except ValueError as e:
                    print(e)
                input_number = input("\tEnter the year the book was published: ").strip()
            
    @staticmethod
    def validate_book_id(book_id: int):
        """The method validates the book ID entered when borrowing or returning the book

        Args:
            book_id (int): The argument represents the ID of the book

        Raises:
            ValueError: ValueError catches errors on input
        """
        pattern = r'^\d+$'
        while True:
            if re.match(pattern, str(book_id)):
                break
            try:
                if not re.match(pattern, str(book_id)):
                    raise ValueError("You only need to enter a number")
            except ValueError as e:
                print(e)
            book_id = input("\tSelect the ID of the book you want to borrow from the library: ").strip()
