import hashlib
import getpass
users_db = {}
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
def register():
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Please choose another.")
        return
    password = getpass.getpass("Enter a new password: ")
    confirm = getpass.getpass("Confirm password: ")
    if password != confirm:
        print("Passwords do not match.")
        return
    users_db[username] = hash_password(password)
    print("Registration successful.")
def login():
    username = input("Enter your username: ")
    if username not in users_db:
        print("Username not found.")
        return
    password = getpass.getpass("Enter your password: ")
    if users_db[username] == hash_password(password):
        print("Login successful. Welcome,", username)
    else:
        print("Incorrect password.")
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
