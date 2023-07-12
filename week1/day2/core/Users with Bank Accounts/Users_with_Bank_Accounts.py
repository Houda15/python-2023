class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()

# Example usage
user = User("John Doe")
user.display_user_balance()  # Output: User: John Doe, Balance: $0

user.make_deposit(100)
user.display_user_balance()  # Output: User: John Doe, Balance: $100

user.make_withdrawal(30)
user.display_user_balance()  # Output: User: John Doe, Balance: $70
