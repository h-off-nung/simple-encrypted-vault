from database import Database
from encryption import Encryption

class Vault:
    def __init__(self):
        self.db = Database()
        self.encryption = Encryption()
        self.email = None

    def register_user(self):
        email = input("Enter email: ")
        master_password = input("Enter master password: ")
        encrypted_master_password = self.encryption.encrypt_data(master_password)
        self.db.register_user(email, encrypted_master_password)
        print("User registered successfully!")

    def login_user(self):
        email = input("Enter email: ")
        master_password = input("Enter master password: ")
        stored_encrypted_password = self.db.get_master_password(email)
        if stored_encrypted_password:
            decrypted_master_password = self.encryption.decrypt_data(stored_encrypted_password)
            if master_password == decrypted_master_password:
                self.email = email
                print("Login successful!")
            else:
                print("Invalid email or password.")
        else:
            print("Invalid email or password.")

    def add_password(self):
        if not self.email:
            print("Please log in first.")
            return
        name = input("Enter name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        website = input("Enter website (optional): ")
        encrypted_password = self.encryption.encrypt_data(password)
        self.db.add_password(self.email, name, username, encrypted_password, website)
        print("Password added successfully!")

    def view_passwords(self):
        if not self.email:
            print("Please log in first.")
            return
        passwords = self.db.get_passwords(self.email)
        for name, username, encrypted_password, website in passwords:
            password = self.encryption.decrypt_data(encrypted_password)
            print(f"Name: {name}, Username: {username}, Password: {password}, Website: {website}")

    def add_note(self):
        if not self.email:
            print("Please log in first.")
            return
        title = input("Enter title: ")
        text = input("Enter text: ")
        self.db.add_note(self.email, title, text)
        print("Note added successfully!")

    def view_notes(self):
        if not self.email:
            print("Please log in first.")
            return
        notes = self.db.get_notes(self.email)
        for title, text in notes:
            print(f"Title: {title}, Text: {text}")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Register")
            print("2. Login")
            print("3. Add Password")
            print("4. View Passwords")
            print("5. Add Note")
            print("6. View Notes")
            print("7. Exit")
            choice = input("Enter choice: ")
            match choice:
                case '1':
                    self.register_user()
                case '2':
                    self.login_user()
                case '3':
                    self.add_password()
                case '4':
                    self.view_passwords()
                case '5':
                    self.add_note()
                case '6':
                    self.view_notes()
                case '7':
                    break
                case _:
                    print("Invalid choice. Please try again.")

if __name__ == '__main__':
    vault = Vault()
    vault.run()