# class Student:
#     def __init__(self,name,country,school):
#      name = name
#      country = country
#      school = school
# def greeting (self,name,country,school):
#  return f"hello {self.name} from {self.country} welcome to {self.school}"

#         self.name = name
#         self.account_num = account_num
#         balance = 0

        #def deposit(self,amount):
#             balance +=amount
#             return f"dear {self.name},you have deposited {amount},your account balance is {self.balance}"
   

class Account :

        def __init__(self,name,account_num):
         self.name = name 
         self.account_num = account_num
         self.balance = 0
         self.deposits = []
         self.withdrawals = []
         self.transaction = 100


        def deposit(self,amount):
             amount = float(input("enter the amount to deposit"))
             self.balance = self.balance + amount
             self.deposits.append(amount)
             return f"Dear {self.name},you have deposited {amount} in account,your current balance is {self.balance}"


        def withdraw(self,amount):
             if (amount >= self.balance):
                 return f"insufficient funds"
             
             elif amount <= 0:
                 return f"amount must be greater than zero"

             else :
                 self.balance -= amount
                 self.withdrawals.append(amount)
                 self.balance -= self.transaction 
                 return f"Dear {self.name} you have withdrawn {amount} and your balance is {self.balance}"


        def statement_deposit(self):
             for x in self.deposit: 
                print(f"dear {self.name} your statement is {x}")

        def statement_withdraw(self):
             for amount in self.withdraw:
                print(f"Dear {self.name} your withdrawal statement is {amount}")

        def current_bal(self):
            return f"dear {self.name} your current account balance is {self.balance}"
            





         
                     



