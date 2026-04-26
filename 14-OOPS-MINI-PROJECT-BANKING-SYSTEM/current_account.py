# Current Account  - Overdraft allowed
# overdraft : means you can withdraw upto a certain limit even if your balance drops to zero

from account import Account

class CurrentAccount(Account):
    
    def __init__(self, name: str, account_number: int, balance: float):
        super().__init__(name, account_number, balance)
        self.type = "current"
        self._overdraftLimit = -50000
        
    def __repr__(self):
        return f"CurrentAccount('{self.account_number}')"
    
    def withdraw(self, amount: float):
        
        current_balance = self.get_balance()
        if current_balance - amount < self._overdraftLimit:
            print("Withdrawal Failed")
            print("Overdraft Limit exceeded")
        else:
            current_balance -= amount
            self.set_balance(current_balance)
        
        

