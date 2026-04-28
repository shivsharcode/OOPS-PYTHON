
from savings_account import SavingsAccount
from current_account import CurrentAccount
import random



choice1 = input("Do you want to open an account? (y/n) : ").strip().lower()

if choice1 == 'n':
    print("OK :)")
    exit()
    
# Take account credentials input
name = input("Enter your name : ").strip()

while True:
    try:
        balance = float(input("Enter your balance : "))
        break
    except ValueError:
        print("!! Balance must be a NUMBER")
        continue
    
account_number = random.randint(1, 10000)

while True:
    account_type = input("What type of Account? Enter 's' for Savings, 'c' for current : ").strip().lower()

    # Initialise account object
    if account_type == 's':
        acc = SavingsAccount(name, account_number, balance)
        break
    elif account_type == 'c':
        acc = CurrentAccount(name, account_number, balance)
        break
    else:
        print("Invalid Input !!")
        continue
        
print(acc)

# PLAYGROUND
while True:
    print("\n---------Select service---------")
    print("Enter \n1: for Deposit, \n2: for Withdrawal, \n3: for Check Balance, \n4: for Exit")
    try:
        service_choice = int(input("Enter : "))
    except ValueError:
        print("Invalid Input")
        continue
    print()
    
    # deposit
    if service_choice == 1:
        amount = float(input("Enter amount to be deposited : "))
        acc.deposit(amount)
        
    # withdraw
    elif service_choice == 2:
        amount = float(input("Enter amount to be withdrawn : ") )
        acc.withdraw(amount)
        
    # check balance
    elif service_choice == 3:
        print(f"Balance = {acc.get_balance()}")
        
    # exit
    elif service_choice == 4:
        break
    
    else:
        print("Invalid Choice input!")

        
    