import random
import sys
import os
number = random.randint(10000, 1000000)
class ATM:
    def __init__(self, name, account_number, balance = 0):
        
        self.name = name
        self.account_number = account_number
        self.balance = balance
         
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: ${self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: $", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is ${self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: $", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: $", self.balance)
        print()
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:- "))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit: $"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw: $"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
             ..............receipts..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {number} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: ${self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************

          """)
                    custum_file_path = input('do you want to give an path to backup file?(y/n): ')
                    if custum_file_path.upper() == 'Y':
                        path = input('give custum path:- ')
                        name_file = input('give backup file name:- ')

                        with open(os.path.join(path, f'{name_file}.txt'), 'w+') as fp:
                            fp.write(f"""Transaction number: {number} 
Account holder: {self.name.upper()}                  
Account number: {self.account_number}                
Available balance: ${self.balance}""")
                        print(f"""
          ******************************************
                   backup profile file is in 
          {os.path.join(path, f'{name_file}.txt')}
          ******************************************
          """)
                    else:

                        with open(os.path.join(os.curdir, f'{number}.txt'), 'w+') as fp:
                            fp.write(f"""Transaction number: {number} 
Account holder: {self.name.upper()}                  
Account number: {self.account_number}                
Available balance: ${self.balance}""")

                        print(f"""
          ******************************************
                   backup profile file is in 
          {os.path.join(os.curdir, f'{number}.txt')}
          ******************************************
          """)
                    sys.exit()

                 
 
print("*******WELCOME TO BANK OF INDIA*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")
atm = ATM(name, account_number)
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
    
