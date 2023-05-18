class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate


title = input("Enter the account title: ")
balance = input("Enter the account balance: ")
account = Account(title, balance)
print("Account Title:", account.title)
print("Account Balance:", account.balance)
interestRate = input("Enter the interest rate: ")
savings_account = SavingsAccount(title, balance, interestRate)
print("Savings Account Title:", savings_account.title)
print("Savings Account Balance:", savings_account.balance)
print("Savings Account Interest Rate:", savings_account.interestRate)
