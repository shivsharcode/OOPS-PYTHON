# Savings Account : Minimum balance rule

from account import Account

class SavingsAccount(Account):
    
    def __init__(self, name: str, account_number: int, balance: float):
        super().__init__(name, account_number, balance)  # calling parent __init__ to set inherited attributes
        self.type = "savings"
        self._minBalance = 500   # protected
    
             
    def __repr__(self):
        return f"SavingsAccount('{self.account_number}')"
    
    
    # setter
    def withdraw(self, amount):
        
        current_balance = self.get_balance()
        
        if current_balance - amount < self._minBalance:
            print("Cannot transact")
            print("Minimum Balance required")
            
        else:
            current_balance -= amount
            self.set_balance(current_balance)
            print("Withdrawal successful")
            

