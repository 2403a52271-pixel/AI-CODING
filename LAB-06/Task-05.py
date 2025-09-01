class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()

# Explanation:
# The BankAccount class allows creating a bank account with a name and balance.
# It provides methods to deposit, withdraw, and check the balance, with basic validation and print statements for clarity.
