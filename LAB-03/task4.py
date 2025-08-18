users_db = {}

def register_user():
    """
    Registers a new user by asking for username and password.
    Stores the credentials in the users_db dictionary.
    """
    username = input("Enter a new username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in users_db:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a new password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return
    users_db[username] = password
    print("Registration successful.")

def login_user():
    """
    Logs in a user by verifying username and password.
    """
    username = input("Enter your username: ").strip()
    if username not in users_db:
        print("Username not found. Please register first.")
        return
    password = input("Enter your password: ").strip()
    if users_db[username] == password:
        print(f"Login successful. Welcome, {username}!")
    else:
        print("Incorrect password. Please try again.")

if __name__ == "__main__":
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

