
class BankAccount:
    def __init__(self, value):
        self.__balance = value
        
        
    @property
    def balance(self):
        return self.__balance
    
    
acc = BankAccount(1000)

print(acc.balance)   # 1000