import numpy as np
rng = np.random.RandomState(11)

class BankAccount:
    
    def __init__(self, balance = 0):
        self._account_number = rng.randint(10000)  # Protected
        self.__balance = balance # private
        
    
    def deposit(self, amount):
        self.__balance += amount   # private attribute can be accessed within class
        
    # public method
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    
    # public method
    def get_balance(self):
        return self.__balance
        
        
account1 = BankAccount()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(400)
print("Balance : ", account1.get_balance() )

