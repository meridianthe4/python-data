from AccountMain import Account

class Current(Account):
    def __init__(self, acc_id, name, balance):
        super().__init__(acc_id, name, balance)
        
    