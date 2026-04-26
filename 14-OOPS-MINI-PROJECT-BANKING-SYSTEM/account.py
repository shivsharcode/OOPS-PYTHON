
from abc import ABC, abstractmethod

class Account(ABC):
    
    def __init__(self, name:str, account_number:int, balance:float):
        self.name = name
        self.account_number = account_number
        self.__balance = balance                 # private. attribute  
        # self.__pin = pin                      # pvt. attribute
        
    # setter
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    # setter
    def deposit(self, amount):
        self.__balance += amount
        
    # getter
    def get_balance(self):
        return self.__balance
    
    # setter
    def set_balance(self, new_balance):
        self.__balance = new_balance
    
    
