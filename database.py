import sqlite3

class Database:
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
            email TEXT NOT NULL UNIQUE,
            master_password TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            website TEXT,
            FOREIGN KEY (email) REFERENCES users (email)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            FOREIGN KEY (email) REFERENCES users (email)
        )
        ''')

        conn.commit()
        conn.close()

    def register_user(self, email, master_password):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (email, master_password) VALUES (?, ?)
        ''', (email, master_password))
        conn.commit()
        conn.close()

    def get_master_password(self, email):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT master_password FROM users WHERE email = ?
        ''', (email,))
        master_password = cursor.fetchone()
        conn.close()
        if master_password:
            return master_password[0]
        return None

    def login_user(self, email, master_password):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT email FROM users WHERE email = ? AND master_password = ?
        ''', (email, master_password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return user[0]  # Return user email
        return None

    def get_passwords(self, email):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT name, username, password, website FROM passwords WHERE email = ?
        ''', (email,))
        passwords = cursor.fetchall()
        conn.close()
        return passwords

    def add_password(self, email, name, username, password, website):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO passwords (email, name, username, password, website) VALUES (?, ?, ?, ?, ?)
        ''', (email, name, username, password, website))
        conn.commit()
        conn.close()

    def delete_password(self, email, name):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM passwords WHERE email = ? AND name = ?
        ''', (email, name))
        conn.commit()
        conn.close()

    def get_notes(self, email):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT title, text FROM notes WHERE email = ?
        ''', (email,))
        notes = cursor.fetchall()
        conn.close()
        return notes

    def add_note(self, email, title, text):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO notes (email, title, text) VALUES (?, ?, ?)
        ''', (email, title, text))
        conn.commit()
        conn.close()

    def delete_note(self, email, title):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM notes WHERE email = ? AND title = ?
        ''', (email, title))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    db = Database()
    db.create_tables()