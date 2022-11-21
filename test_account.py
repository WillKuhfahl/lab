import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('001-Will', 24)
        self.a2 = Account('Sandra-002', 12)

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        # a1 testing
        assert self.a1.get_name() == "001-Will"
        assert self.a1.get_balance() == 24

        # a2 testing
        assert self.a2.get_name() == 'Sandra-002'
        assert self.a2.get_balance() == 12

    def test_deposit(self):
        # a1 testing
        assert self.a1.deposit(12) == True
        assert self.a1.deposit(1.33) == True
        assert self.a1.deposit(-3) == False
        assert self.a1.deposit(0) == False

        # a2 testing
        assert self.a2.deposit(120) == True
        assert self.a2.deposit(1.42) == True
        assert self.a2.deposit(-23) == False
        assert self.a2.deposit(0) == False

    def test_withdraw(self):
        # a1 testing
        assert self.a1.withdraw(1) == True
        assert self.a1.withdraw(2.3243) == True
        assert self.a1.withdraw(-12) == False
        assert self.a1.withdraw(0) == False
        assert self.a1.withdraw(500) == False

        # a2 testing
        assert self.a2.withdraw(3) == True
        assert self.a2.withdraw(2.3) == True
        assert self.a2.withdraw(-20) == False
        assert self.a2.withdraw(0) == False
        assert self.a2.withdraw(3000) == False

if __name__ == "__main__":
    main()

