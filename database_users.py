import psycopg2


class Database:
    def __init__(self) -> None:
        """The constructor of the "Database" class mainly initializes the settings and access to the postgresql database
        """
        self._dbname="postgres"
        self._user="postgres"
        self._password="postgres"
        self._host="localhost"
     
    def connect_to_database(self):
        """The method connects to the database

        Returns:
            conn: The variable conn means a connection to the database. When you connect to a database, you create a "connection", which is usually an object that allows your code to communicate with the database.
        """
        conn = psycopg2.connect(dbname=self._dbname, user=self._user, password=self._password, host=self._host)
        return conn

    def create_book_table(self):
        """The method creates a table in the library database
        """
        conn = self.connect_to_database()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS book (
                id SERIAL PRIMARY KEY,
                name VARCHAR(128) UNIQUE,
                author VARCHAR(128) UNIQUE,
                year_publication INTEGER
            );
        ''')
        conn.commit()
        conn.close()
        
    def create_loaned_book_table(self):
        """The method creates a table in the user database
        """
        conn = self.connect_to_database()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS loaned_books (
                id SERIAL PRIMARY KEY,
                name VARCHAR(128) UNIQUE NOT NULL,
                author VARCHAR(128) UNIQUE NOT NULL,
                year_publication INTEGER NOT NULL
            );
        ''')
        conn.commit()
        conn.close()