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

    def delete_password(self):
        if not self.email:
            print("Please log in first.")
            return
        name = input("Enter the name of the password to delete: ")
        self.db.delete_password(self.email, name)
        print("Password deleted successfully!")

    def add_note(self):
        if not self.email:
            print("Please log in first.")
            return
        title = input("Enter title: ")
        text = input("Enter text: ")
        encrypted_text = self.encryption.encrypt_data(text)
        self.db.add_note(self.email, title, encrypted_text)
        print("Note added successfully!")

    def view_notes(self):
        if not self.email:
            print("Please log in first.")
            return
        notes = self.db.get_notes(self.email)
        for title, encrypted_text in notes:
            text = self.encryption.decrypt_data(encrypted_text)
            print(f"Title: {title}, Text: {text}")

    def delete_note(self):
        if not self.email:
            print("Please log in first.")
            return
        title = input("Enter the title of the note to delete: ")
        self.db.delete_note(self.email, title)
        print("Note deleted successfully!")

    def run(self):
        while True:
            if not self.email:
                print("\nMenu:")
                print("1. Register")
                print("2. Login")
                print("3. Exit")
                choice = input("Enter choice: ")
                match choice:
                    case '1':
                        print()
                        self.register_user()
                    case '2':
                        print()
                        self.login_user()
                    case '3':
                        break
                    case _:
                        print()
                        print("Invalid choice. Please try again.")
            else:
                print("\nMenu:")
                print("1. Add Password")
                print("2. View Passwords")
                print("3. Delete Password")
                print("4. Add Note")
                print("5. View Notes")
                print("6. Delete Note")
                print("7. Exit")
                choice = input("Enter choice: ")
                match choice:
                    case '1':
                        print()
                        self.add_password()
                    case '2':
                        print()
                        self.view_passwords()
                    case '3':
                        print()
                        self.delete_password()
                    case '4':
                        print()
                        self.add_note()
                    case '5':
                        print()
                        self.view_notes()
                    case '6':
                        print()
                        self.delete_note()
                    case '7':
                        break
                    case _:
                        print()
                        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    vault = Vault()
    vault.run()