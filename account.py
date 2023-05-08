class Account:
    accountName = "fortune franklyn"
    accountBalance = 200000
    accountNumber = 8163532857
    def __init__(self):
        self.accountBalance
        self.accountName
        self.accountNumber
    def deposit(self, amount):
        self.accountBalance = self.accountBalance + amount
        return f"Your new amount is {self.accountBalance}"
    def withdraw(self, amount):
        self.accountBalance = self.accountBalance - amount
        return f"Your current account balance is now {self.accountBalance}"