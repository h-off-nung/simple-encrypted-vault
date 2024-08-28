import os
from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        if not os.path.exists(self.key_file):
            self.generate_key()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        with open(self.key_file, 'rb') as key_file:
            return key_file.read()

    def encrypt_data(self, data):
        key = self.load_key()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        key = self.load_key()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data

if __name__ == '__main__':
    manager = Encryption()