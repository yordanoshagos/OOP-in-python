from datetime import datetime
import uuid
class Transaction:
    def __init__(self, amount, transaction_type, narration=""):
        self.amount = amount
        self.transaction_type = transaction_type  
        self.narration = narration
        self.date_time = datetime.now()
    def __str__(self):
        sign = "+" if self.transaction_type in ['deposit', 'loan', 'interest'] else "-"
        return f"{self.date_time} | {self.transaction_type.upper()} | {sign}{self.amount} | {self.narration}"

class Account:
    def __init__(self, name):
        self.name = name
        self.__account_number = str(uuid.uuid4())  
        self.__transactions = []
        self.loans = []
        self.loan_repaying = []
        self.frozen = False
        self.minimum_balance = 0
   
    def deposit(self, amount):
        if self.frozen:
            return "Account is frozen."
        if amount <= 0:
            return "You can't deposit a negative amount."
        self.__transactions.append(Transaction(amount, 'deposit', 'Deposit made'))
        return f"Deposited {amount}. New balance: {self.get_balance()}"
    
    def withdraw(self, amount):
        if self.frozen:
            return "Account is frozen."
        if amount <= 0:
            return "You can't withdraw a negative amount."
        if self.get_balance() - amount >= self.minimum_balance:
            self.__transactions.append(Transaction(-amount, 'withdrawal', 'Withdrawal made'))
            return f"Withdrew {amount}. New balance: {self.get_balance()}"
        else:
            return "Insufficient funds or below minimum balance."
    
    def transfer(self, amount, user_account):
        if self.frozen:
            return "Account is frozen."
        if amount <= 0:
            return "You can't transfer a negative amount."
        if self.get_balance() - amount >= self.minimum_balance:
            self.__transactions.append(Transaction(-amount, 'transfer', f'Transfer to {user_account.name}'))
            user_account._receive_transfer(amount, self.name)
            return f"Transferred {amount} to {user_account.name}."
        else:
            return "Insufficient funds or below minimum balance."
    
    def _receive_transfer(self, amount, from_name):
        self.__transactions.append(Transaction(amount, 'transfer', f'Received from {from_name}'))
    
    def get_loan(self, amount):
        if self.frozen:
            return "Account is frozen."
        if amount <= 0:
            return "You can't take a negative loan."
        self.loans.append(amount)
        self.__transactions.append(Transaction(amount, 'loan', 'Loan received'))
        return f"Loan of {amount} granted."
    
    def repay_loan(self, amount):
        if amount <= 0:
            return "You can't repay a negative amount."
        if sum(self.loans) == 0:
            return "You have no unpaid loans."
        self.loan_repaying.append(amount)
        self.__transactions.append(Transaction(-amount, 'loan repayment', 'Loan repayment'))
        return f"Repaid {amount}. Remaining loan: {sum(self.loans) - sum(self.loan_repaying)}"
    
    def apply_interest(self):
        if self.frozen:
            return "Account is frozen."
        interest = self.get_balance() * 0.05
        self.__transactions.append(Transaction(interest, 'interest', 'Interest applied'))
        return f"Interest of {interest} applied. New balance: {self.get_balance()}"
    
    def get_balance(self):
        return sum(t.amount for t in self.__transactions)
    
    def get_statement(self):
        print(f"Account statement for {self.name}")
        for t in self.__transactions:
            print(t)
        print(f"Current Balance: {self.get_balance()}")
    
    def view_account_details(self):
        return f"Account Owner: {self.name}, Account Number: {self.__account_number}, Balance: {self.get_balance()}"
    
    def change_account_owner(self, new_name):
        self.name = new_name
        return f"Account owner updated to {new_name}."
    
    def freeze_account(self):
        self.frozen = True
        return "Account has been frozen."
    
    def unfreeze_account(self):
        self.frozen = False
        return "Account has been unfrozen."
    
    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.minimum_balance = amount
            return f"Minimum balance set to {amount}."
        else:
    
            return "Minimum balance cannot be negative."
    
    def close_account(self):
        self.__transactions.clear()
        self.loans.clear()
        self.loan_repaying.clear()
        self.frozen = True
        return "Account closed. All balances cleared and account frozen."

    def get_account_number(self):
        return self.__account_number
    def get_transaction_history(self):
        return list(self.__transactions)






