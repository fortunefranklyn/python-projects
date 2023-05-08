from account import Account

class Savings(Account):
    def __init__(self):
        Account.__init__(self)
    def withdraw(self, amount):
        if amount > 5000:
            return "You have reached your limit"
        else:
            return super().withdraw(amount)
print(Savings().withdraw(3000))