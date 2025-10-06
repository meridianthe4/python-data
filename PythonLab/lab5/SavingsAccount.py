
from PythonLab.lab5.AccountMain import Account
# Create SavingsAccount as sub class of account - additional field (type - personal/corporate etc)
# implement withdraw and deposit such that
# - maximum upto 1 lakh can be deposited in an account at a time
# - Min balance 5000 must be maintained while withdrawal (if type = corporate you withdraw full amount = balance)

class SavingsAccount(Account):
    def __init__(self, acc_id, name, balance,type):
        super().__init__(acc_id, name, balance)
        self._type = type
        
    def withdraw(self,amt):
        if (self._balance - amt <5000) and self._type != 'corporate':
            print("Minimum balance should be 5000")
        else:
            self._balance -= amt
            print(f"Withdrawal successful. New balance: {self._balance}")

    def deposite(self,amt):
        if amt > 100000:
            print("Cannot deposit more than 1 lakh at a time.")
        else:
            self._balance += amt
            print(f"Deposit successful. New balance: {self._balance}")

        