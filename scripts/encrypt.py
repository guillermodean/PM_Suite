# encrypt_decrypt_secrets.py

import os
from cryptography.fernet import Fernet

def generate_key():
    # Generate a key and save it to the organization folder
    key = Fernet.generate_key()
    key_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'organization', 'secret_key.key')
    
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

    print(f"Encryption key generated and saved at: {key_path}")
    return key

def encrypt_folder(key, folder_path):
    cipher = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            with open(file_path, 'rb') as original_file:
                original_data = original_file.read()

            encrypted_data = cipher.encrypt(original_data)

            with open(file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

    print(f"Folder '{folder_path}' encrypted successfully.")

def decrypt_folder(key_path, folder_path):
    with open(key_path, 'rb') as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            with open(file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            decrypted_data = cipher.decrypt(encrypted_data)

            with open(file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)

    print(f"Folder '{folder_path}' decrypted successfully.")
