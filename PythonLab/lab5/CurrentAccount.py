from PythonLab.lab5.AccountMain import Account

# Create CurrentAccount as sub class of account
# implement withdraw and deposit such that
# - maximum upto 2 lakh can be deposited in an account at a time
# - Min balance 10000 must be maintained while withdrawal

class CurrentAccount(Account):
    def __init__(self, acc_id, name, balance):
        super().__init__(acc_id, name, balance)
        
    def withdraw(self,amt):
        if self._balance - amt < 10000:
            print("Minimum balance should be 10000")
        else:
            self._balance -= amt
            print(f"Withdrawal successful. New balance: {self._balance}")

    def deposit(self, amt):
        if amt > 200000:
            print("Cannot deposit more than 2 lakh at a time.")
        else:
            self._balance += amt
            print(f"Deposit successful. New balance: {self._balance}")
