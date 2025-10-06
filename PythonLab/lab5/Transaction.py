# Create Bank App with Transaction class
# Create Method withdraw_from_account(account : Account)  and deposit_to_account(account : Account)
# These methods will return the new balance after deposite/withdraw

# Creare user class with user interface that gives 2 menu options
# 1. Deposit
# 2. Withdraw

# Both options will ask user to enter money to withdraw/deposite
# Display a statement with each transaction and final balance after user exits from the menu\

# Identify possible Exceptions and implement them

class Transaction:
    def withdraw_from_account(self, account, amt):
        account.withdraw(amt)
        return account._balance
    
    def deposit_to_account(self, account, amt):
        account.deposit(amt)
        return account._balance
    
if __name__ == "__main__":
    from PythonLab.lab5.SavingsAccount import SavingsAccount
    from PythonLab.lab5.CurrentAccount import CurrentAccount
    
    sa = SavingsAccount(101, "Alok", 20000, "personal")
    ca = CurrentAccount(201, "Bandhu", 50000)
    
    transaction = Transaction()
    
    print(sa)
    print(ca)
    
    transaction.deposit_to_account(sa, 50000)
    transaction.withdraw_from_account(ca, 20000)
    
    print(sa)
    print(ca)

