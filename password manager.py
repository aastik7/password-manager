from cryptography.fernet import Fernet, InvalidToken
import os
from getpass import getpass

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        write_key()  # Create the key file if it doesn't exist
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def get_master_password():
    if not os.path.exists("master_password.key"):
        master_password = getpass("Set your master password: ")
        with open("master_password.key", "w") as master_file:
            master_file.write(master_password)
    else:
        with open("master_password.key", "r") as master_file:
            master_password = master_file.read()
    return master_password

key = load_key()
fer = Fernet(key)

master_password = get_master_password()

def view():
    master_input = getpass("Enter your master password: ")
    if master_input != master_password:
        print("Incorrect master password. Access denied.")
        return

    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                try:
                    decrypted_password = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "Passwords:", decrypted_password)
                except InvalidToken:
                    print("InvalidToken: Unable to decrypt data for user:", user)
    except FileNotFoundError:
        print("Password file not found. No data to view.")

def add():
    master_input = getpass("Enter your master password: ")
    if master_input != master_password:
        print("Incorrect master password. Access denied.")
        return

    name = input("Account Name: ")
    pwd = input("Account password: ")

    with open("password.txt", 'a') as f:
        encrypted_password = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_password + "\n")

while True:
    mode = input("Would you like to add a password or view existing passwords? Enter 'view', 'add', or press 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
