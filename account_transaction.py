class AccountComponent:

    account = []
    
    def __init__(self, int_rate, balance ):
        self.int_rate = int_rate
        self.balance = balance
        AccountComponent.account.append(self)

    def deposit (self, amount):
        self.balance += amount
        return self
        
    def withdraw (self, amount):
        
        if (self.balance - amount) >= 0:
            self.balance -= amount
            
        else:
            print("insufficient funds : charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"balance: {self.balance} ")
        return self
    
    def yield_interest (self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    
    @classmethod
    def show_all_accounts(cls):
        for account in cls.account:
            account.display_account_info()
    
userName1 = AccountComponent (.10, 500)
userName2 = AccountComponent(.20, 1000)

userName1.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
userName2.deposit(100).deposit(200).withdraw(400).withdraw(60).withdraw(50).withdraw(100).yield_interest().display_account_info()


AccountComponent.show_all_accounts()
