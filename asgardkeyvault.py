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

value = get_user_input("Please enter a selection: ")
print("Value:", value)

def open_file_write(password):
    try:
        with open("keys.txt", "w") as file:
            file.write(password)
            return "Password sucessful stored"
    except FileExistsError:
            print('File already exists')
# passwords get hashed and salted (not encrypted) for authentication
# file storing the password gets encypted

if value == "Q" or value == "q":
     print("test")
     sys.exit()

if value == "S" or value == "s":
    password = input("Please enter a password (5 or more characters): ")
    result = open_file_write(password)
    print(result)
    
    print(password)

def generate_key():
     #Generates a new encryption key and saves it to a file
     key = Fernet.generate_key()
     with open("keyfile.key", "wb") as keyfile:
          keyfile.write(key)

# Write encryption code
def encrypt_file(filename, key):

generate_key()