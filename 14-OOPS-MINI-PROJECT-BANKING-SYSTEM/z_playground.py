
from savings_account import SavingsAccount
from current_account import CurrentAccount
import random



choice1 = input("Do you want to open an account? (y/n) : ").strip().lower()

if choice1 == 'n':
    exit()
    
# Take account credentials input
name = input("Enter your name : ").strip()
balance = float(input("Enter your balance : "))
account_number = random.randint(1, 10000)

account_type = input("What type of Account? Enter 's' for Savings, 'c' for current : ").strip().lower()

# Initialise account object
if account_type == 's':
    acc = SavingsAccount(name, account_number, balance)
elif account_type == 'c':
    acc = CurrentAccount(name, account_number, balance)
    
print(acc)

# PLAYGROUND
while True:
    print("\n---------Select service---------")
    print("Enter \n1: for Deposit, \n2: for Withdrawal, \n3: for Check Balance, \n4: for Exit")
    service_choice = int(input("Enter : "))
    print()
    
    # deposit
    if service_choice == 1:
        amount = float(input("Enter amount to be deposited : "))
        acc.deposit(amount)
        
    # withdraw
    if service_choice == 2:
        amount = float(input("Enter amount to be withdrawn : ") )
        acc.withdraw(amount)
        
    # check balance
    if service_choice == 3:
        print(f"Balance = {acc.get_balance()}")
        
    # exit
    if service_choice == 4:
        break
    

        
    