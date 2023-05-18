class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return self.balance * self.interestRate / 100


demo1 = SavingsAccount("Ashish", 2000, 5)
interest_amount = demo1.interestAmount()
print("Interest Amount:", interest_amount)  # Output: 100
