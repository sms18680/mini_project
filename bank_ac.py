class Account:
    # Define an __init__ constructor method with attributes shared by all accounts:
    def __init__(self,acct_nbr,opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance=opening_deposit
    def __str__(self):
        return f'${self.balance:.2f}'
    def deposit(self,dep_amt):
        self.balance+=dep_amt
    def withdraw(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance-=wd_amt
        else:
            return 'Funds unavailable';


class Checking(Account):
    def __init__(self,acct_nbr,opening_deposit):
        super().__init__(acct_nbr,opening_deposit)
    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\nBalance:{Account.__str__(self)}';


class Savings(Account):
    def __init__(self,acct_nbr,opening_deposit):
        super().__init__(acct_nbr,opening_deposit)
    def __str__(self):
        return f'Savings Account #{self.acct_nbr}\nBalance: {Account.__str__(self)}'
class Business(Account):
    def __init__(self,acct_nbr,opening_deposit):
        super().__init__(acct_nbr,opening_deposit)
    def __str__(self):
       return f'Business Account #{self.acct_nbr} \nBalance: {Account.__str__(self)}'