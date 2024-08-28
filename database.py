import sqlite3

class DatabaseManager:
    def __init__(self, db_file='bobrov_vault.db'):
        self.db_file = db_file

    def connect_db(self):
        return sqlite3.connect(self.db_file)

    def create_tables(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            master_password TEXT NOT NULL,
            email TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            website TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            text TEXT NOT NULL
        )
        ''')

        conn.commit()
        conn.close()

if __name__ == '__main__':
    db_manager = DatabaseManager()
    db_manager.create_tables()