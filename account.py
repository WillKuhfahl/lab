class Account:
    def __init__(self):
        self.account_name = Account('001-Will')
        self.account_balance = 0

    def deposit(self, amount) -> float:
        """
        Function to add an amount to the user's balance
        :param amount: amount that the user wants to add
        :return: returns true if the transaction is sucessful (value > 0), and false if not
        """
        if amount > 0:
            self.account_balance = self.account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount) -> float:
        """
        Function to withdraw an amount from the user's balance
        :param amount: amount that the user want to withdraw
        :return: returns true if the transaction is sucessful (value > 0), and false if not
        """
        if int(amount) > 0:
            self.account_balance = self.account_balance - amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Function to check the overall balance
        :return: returns the account balance
        """
        return self.account_balance

    def get_name(self):
        """
        Function to check the name of the account
        :return: returns the account name
        """
        return self.account_name
