class Account:
    def __init__(self, name):
        self.name = name
        self.deposits = []
        self.withdrawals = []
        self.transfers = []
        self.loans = []
        self.loan_repaying = []
        self.frozen = False
        self.minimum_balance = 0
    def deposit(self, amount):
        if self.frozen:
            return "Account is frozen."
        if amount > 0:
            self.deposits.append(amount)
            return f"Deposited {amount}. New balance: {self.get_balance()}"
        else:
            return "You can't deposit a negative amount."
    def withdraw(self, amount):
        if self.frozen:
            return "Account is frozen."
        if amount > 0:
            if self.get_balance() - amount >= self.minimum_balance:
                self.withdrawals.append(amount)
                return f"Withdrew {amount}. New balance: {self.get_balance()}"
            else:
                return "Insufficient funds or below minimum balance."
        else:
            return "You can't withdraw a negative amount."
    def get_balance(self):
        return sum(self.deposits) - sum(self.withdrawals) - sum(self.transfers)
    def transfer(self, amount, user_account):
        if self.frozen:
            return "Account is frozen."
        if amount > 0:
            if self.get_balance() - amount >= self.minimum_balance:
                self.transfers.append(amount)
                user_account.deposit(amount)
                return f"Transferred {amount} to {user_account.name}."
            else:
                return "Insufficient funds or below minimum balance."
        else:
            return "You can't transfer a negative amount."
    def get_loan(self, amount):
        if self.frozen:
            return "Account is frozen."
        if amount > 0:
            self.loans.append(amount)
            return f"Loan of {amount} granted."
        else:
            return "You can't take a negative loan."
    def repay_loan(self, amount):
        if amount > 0:
            if sum(self.loans) > 0:
                self.loan_repaying.append(amount)
                return f"Repaid {amount}. Remaining loan: {sum(self.loans) - sum(self.loan_repaying)}"
            else:
                return "You have no unpaid loans."
        else:
            return "You can't repay a negative amount."
    def get_statement(self):
        print(f"Account statement for {self.name}")
        print("Deposits:")
        for d in self.deposits:
            print(f"  +{d}")
        print("Withdrawals:")
        for w in self.withdrawals:
            print(f"  -{w}")
        print("Transfers:")
        for t in self.transfers:
            print(f"  -{t}")
        print(f"Current Balance: {self.get_balance()}")
    def view_account_details(self):
        return f"Account Owner: {self.name}, Balance: {self.get_balance()}"
    def change_account_owner(self, new_name):
        self.name = new_name
        return f"Account owner updated to {new_name}."
    def apply_interest(self):
        if self.frozen:
            return "Account is frozen."
        interest = self.get_balance() * 0.05
        self.deposits.append(interest)
        return f"Interest of {interest} applied. New balance: {self.get_balance()}"
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
        self.deposits.clear()
        self.withdrawals.clear()
        self.transfers.clear()
        self.loans.clear()
        self.loan_repaying.clear()
        self.frozen = True
        return "Account closed. All balances cleared and account frozen."
    




