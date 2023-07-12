class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

# Example usage
account = BankAccount(int_rate=0.02, balance=100)
account.display_account_info()  # Output: Balance: $100

account.deposit(50)
account.display_account_info()  # Output: Balance: $150

account.withdraw(30)
account.display_account_info()  # Output: Balance: $120

account.yield_interest()
account.display_account_info()  # Output: Balance: $122.4
