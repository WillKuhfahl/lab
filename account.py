class Account:
    """
    A class with details for an account that includes the name of the account and
    the balance within the account.
    """
    def __init__(self, name: str, account_balance = 0) -> None:
        """
        Function creates initial state of an account object which includes account balance
        and account name.
        :param name: The name associated with the account
        :param account_balance: The balance within the account
        """
        self.__account_name = name
        self.__account_balance = account_balance

    def deposit(self, amount) -> float:
        """
        Function to add an amount to the user's balance.
        :param amount: amount that the user wants to add
        :return: returns true if the transaction is successful (value > 0), and false if not
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount) -> float:
        """
        Function to withdraw an amount from the user's balance
        :param amount: amount that the user want to withdraw
        :return: returns true if the transaction is successful (value > 0), and false if not
        """
        if float(amount) > self.__account_balance:
            return False
        elif float(amount) > 0:
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Function to check the overall balance
        :return: returns the account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        Function to check the name of the account
        :return: returns the account name
        """
        return self.__account_name
