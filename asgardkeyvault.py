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
        with open(password_file, "w") as file:
            file.write(password)
            print("Password:", password)                                #debug
            print("Password sucessful stored")
    except FileExistsError:
            print('File already exists')

def generate_key():
    #Generates a new encryption key and saves it to a file
    key = Fernet.generate_key()
    with open("keyfile.key", "wb") as keyfile:
          keyfile.write(key)
    return key

# Write encryption code
def encrypt_file(password_file, key):
    print("Filename:", password_file, "key:", key)
    f = Fernet(key)
    with open(password_file, "rb") as file:
         file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(password_file, "wb") as file:
         file.write(encrypted_data)
         print("File encrypted")

# passwords get hashed and salted (not encrypted) for authentication
# file storing the password gets encypted

value = get_user_input("Please enter a selection: ")
print("Value:", value)

if value == "Q" or value == "q":
     print("test")
     sys.exit()

if value == "S" or value == "s":
    password = input("Please enter a password (5 or more characters): ")
    open_file_write(password)
    
    print(password)                                                      #Debug

if value == "G" or value == "g":
    password = decrypt_file(password_file, key)

key = generate_key()

encrypt_file(password_file, key)

# under development
def decrypt_file(password_file, key):
    f = Fernet(key)
    with open(password_file, "rb") as file:
        file_data = file.read()
    decrypt_file = f.decrypt(file_data)