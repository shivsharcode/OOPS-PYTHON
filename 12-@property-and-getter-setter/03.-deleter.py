

class BankAccount:
    
    def __init__(self, value):
        self.__balance = value
        
    # getter
    @property
    def balance(self):
        return self.__balance
    
    # deleter
    @balance.deleter
    def balance(self):
        print("Deleting balance")
        del self.__balance
        
        
acc = BankAccount(1000)

print(acc.balance)   # getter - 1000

del acc.balance       # this will call balance() under the @balance.deleter

# print(acc.balance)   # will throw AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance', bcoz the deleter method has deleted it 

    