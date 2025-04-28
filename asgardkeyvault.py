# Asgard Password Vault is a password manager where you can safely
# store, rotate, checkout, and delete your password. Asgard
# Key Vault uses <hashing> and <encyrption> algorithms

import sys
import os
import cryptography
from cryptography.fernet import Fernet

# menu to create new password, rotate(change), checkout(get), and delete password
print("Welcome to Asgard Password Vault!")
print("Use Asgard to securely store anything with a username/id and password \
      including your passwords, personal access tokens and other keys!\n")

print("Choose an option:")
print("(S)tore Password          (G)et Password")
print("(C)hange Password         (D)elete Password")
print("(Q)uit Program\n")

selection = ["S", "s", "C", "c", "Q", "q", "G", "g", "D", "d"]
password_file = "keys.txt"
key_file = "keyfile.key"

def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if user_input not in selection:
                raise ValueError("Invalid input. Please enter a valid selection.")
            print("You entered", user_input)
            return user_input
        except ValueError as e:
            print(f"Error: {e}")

# need to check if encryption key already exists
def open_file_write(password):
    try:
       with open(password_file, "wb") as file:
            file.write(password.encode())
#            print("Password:", password)                                # debug
            print("Password sucessful stored")
    except FileExistsError:
            print('File already exists')

#Generates a new encryption key and saves it to a file
def generate_key():
    
    key = Fernet.generate_key()
    with open(key_file, "wb") as keyfile:
          keyfile.write(key)
    return key

#Creates an encryption object(f), reads data of file containing password,
#encrypts the data, and writes it back out to file
def encrypt_file(password_file, key):
#    print("Filename:", password_file, "key:", key)
    f = Fernet(key)
    with open(password_file, "rb") as file:
         file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(password_file, "wb") as file:
         file.write(encrypted_data)
         print("File encrypted")

# decrypts key
def decrypt_file(password_file, key):

    f = Fernet(key)
    
    with open(password_file, "rb") as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = f.decrypt(encrypted_data)
        plaintext_password = decrypted_data.decode('utf-8')  # or 'latin-1'
        print("File successfully decrypted")
        return plaintext_password
    except Exception as e:
        print(f"Decryption failure: {e}")
        print("Verify you're using the correct key")

def get_key():
    key = open(key_file, "rb").read()
    return key
    
value = get_user_input("Please enter a selection: ")
print("Value:", value)

if value == "Q" or value == "q":
     print("test")
     sys.exit()

if value == "S" or value == "s":
    password = input("Please enter a password (5 or more characters): ")
    open_file_write(password)
    if os.path.exists(key_file):
        print("Encryption Key already exists!")
        key = get_key()
    else:
        key = generate_key()
    encrypt_file(password_file, key)
    print(password)                                                      # debug

if value == "G" or value == "g":
    if os.path.exists(password_file):
        key = get_key()
        password = decrypt_file(password_file, key)
        print(password)
    else:
        print("*** There are no passwords to decrypt ***\n")
        sys.exit(0)   #consider returning user to main menu

# passwords get hashed and salted (not encrypted) for authentication
# file storing the password gets encypted