# Asgard Password Vault is a password manager where you can safely
# store, rotate, checkout, and delete your password. Asgard
# Key Vault uses <hashing> and <encyrption> algorithms

import sys

try:
    with open("keys.txt", "a") as file:
        file.write('This is a test')
except FileExistsError:
        print('File already exists')

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


# passwords get hashed and salted (not encrypted) for authentication
# file storing the password gets encypted

if value == "Q" or value == "q":
     print("test")
     sys.exit()
elif value == "S" or value == "s":
    password = input("Please enter a password (5 or more characters): ")
    
    
    
    print(password)

             