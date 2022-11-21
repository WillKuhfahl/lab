class Account:
    def __init__(self):
        self.account_name = Account('001-Will')
        self.account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.account_balance = self.account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if int(amount) > 0:
            self.account_balance = self.account_balance - amount
            return True
        else:
            return False

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name
