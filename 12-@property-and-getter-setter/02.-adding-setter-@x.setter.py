

class BankAccount:
    def __init__(self, value):
        self.__balance = value
        
    # getter
    @property
    def balance(self):
        return self.__balance
        
    # setter
    @balance.setter
    def balance(self, new_value):
        if new_value < 0:
            print("Invalid balance")
        else:
            self.__balance = new_value
            
        
acc = BankAccount(1000)

print(acc.balance)   # calls getter method balance()

acc.balance = 500    # calls setter method balance under the @balance.setter

print(acc.balance)

acc.balance = -100