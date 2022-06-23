from datetime import date, datetime
from time import strftime



class Account :

        def __init__(self,name,account_num):
         self.name = name 
         self.account_num = account_num
         self.balance = 0
         self.deposits = []
         self.withdrawals = []
         self.transaction = 100
         self.loan_balance = 0 
         
        def deposit(self,amount):
            amount = float(input("enter the amount to deposit"))
            self.balance = self.balance + amount
            self.deposits.append(amount)
            deposit_detail = {"date": date.strftime('%Y%m%d%H:%M'),"amount":amount, "narration":"deposit"}
            return f"Dear {self.name},you have deposited {amount} in account,your current balance is {self.balance}"
          
        def withdraw(self,amount):
             if (amount >= self.balance):
                 return f"insufficient funds"
    
             elif amount <= 0:
                 return f"amount must be greater than zero"

             else :
               withdrawal_date = datetime.now()
               self.balance -= amount
               self.withdrawals.append(amount + self.time)
               self.balance -= self.transaction
               withdraw_details = {"date":date.strftime('%Y%m%d%H%M'),"amount":amount,"narration":"withdraw"}
               return f"Dear {self.name} you have withdrawn {amount} and your balance is {self.balance}"
                 
        def statement_deposit(self):
             for x in self.deposit: 
                print(f"dear {self.name} your statement is {x}")

        def statement_withdraw(self):
            for amount in self.withdraw:
                print(f"Dear {self.name} your withdrawal statement is {amount}")

        def current_bal(self):
            return f"dear {self.name} your current account balance is {self.balance}"
            
        def full_statements(self):
            for item in self.deposits and self.withdrawals:

             def deposits_statement (self):
               for deposit in self.deposits:
                 print(f"{deposit}")
        def withdraw_statement (self):
            for withdraw in self.withdraws:
             print(withdraw)

def get_balance (self) :
           return f"Your account balance is {self.balance}"

def full_statement (self) :
           for item in self.combination :
            self.combination.sort(key=lambda item: item['date'], reverse=True)
            date = item['date']
            amount = item['amount']
            narration = item['narration']
            print(f"{date}.... {narration}.... {amount}")

def loan(self,amount):
         amount = sum(self.deposits)
         qualification = (count) * 1/3
         amount += (amount)* 0.03
         if amount <= 100:
            return f"Enter amount more than 100"
         elif self.loan_balance > 0:
            return f"You have an outstanding amount of {self.loan_balance}"
         elif amount >= qualification:
            return f"You cannot borrow more than {count //3}"
         elif len(self.deposits)< 10:
            return f"You must have deposited more than 10 times "
         else:
            self.loan_balance += amount
            return f"Your loan balance is {self.loan_balance}"

def loan_payment(self, amount):
         if amount < self.loan_balance:
            self.loan_balance -= amount
            return f"You have paid {amount} and your have an outstanding balance of {self.loan_balance}"

         elif amount == self.loan_balance:
              self.loan_balance-= amount

         elif amount > self.loan_balance:   
              overpay = amount - self.loan_balance
              self.balance+=overpay
              remaining_amount = amount - overpay
              self.loan_balance -= remaining_amount
         else:
            self.loan_balance-=amount
            return f"You loan is now cleared."
def transfer(self, amount, account):
         if amount > self.balance:
            return f"Your account balance is too low cannot transfer amount"
         elif amount <= 0:
            return f"Enter correct amount" 
         else:
            self.balance-= amount
            account.balance += amount
            return f"You have sent {amount} to {account.account_name} and your balance is {self.balance}"

