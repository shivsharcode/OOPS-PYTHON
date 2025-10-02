
class BankAccount:
    
    def __init__(self, account_holder_name, account_type, balance=0):
        self.account_holder = account_holder_name   # public
        
        self._account_type = account_type           # protected
        
        self.__balance = balance                    # private
        
        print("Account Created")
        
        
    # deposit - setter
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} AmountCredited, Balance = {self.__balance}")
        
    # withdraw - setter
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} Amount debited, Balance : {self.__balance}")
        else:
            print("Insufficient balance")
            
    # getter
    def get_balance(self):
        return self.__balance
    
    # printing info
    def account_info(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Type: {self._account_type}")
        
        
def main():
    acc1 = BankAccount("Shiv", "Savings", 1000)
    acc2 = BankAccount("Aryan", "Current", 500)
    
    acc1.deposit(500)
    acc1.withdraw(200)
    acc2.withdraw(700)
    
    acc1.account_info()
    print(acc1.get_balance())
    
    acc2.account_info()
    print(acc2.get_balance())
    
        
main()