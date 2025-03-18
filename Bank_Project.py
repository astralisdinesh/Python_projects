class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialamont,accName):
        self.balance=initialamont
        self.name=accName
        print(f'\n account {self.name} created.\n balance = {self.balance}')
    
    def getbalance(self):
        print(f'\n account name is {self.name} \n balance is {self.balance}')
    
    def deposit(self,amount):
        self.balance+=amount
        print('amount deposited')
        print(f'your account name is {self.name} \n updated balance is {self.balance}')
    
    def viableTransaction(self,amount):
        if self.balance>=amount:
            return 
        else:
            raise BalanceException(f'\n sorry ,account {self.name } only has a balance of {self.balance}')
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance-=amount
            print(f'\n withdraw completed')
            self.getbalance()
        except BalanceException as error:
            print(f'\n withdraw interrupted : {error}')
    
    def transfer(self,amount,account):
        try:
            print('\n********\n Beginning Transfer ..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'\n Transfer completed ')
        except BalanceException as error:
            print(f'transfer interrupted : {error}')
class InterrestRewardsAcct(BankAccount):
    def  deposit(self, amount):
        self.balance=self.balance+(amount*1.05)
        print(f'deposited the amount')
        self.getbalance()    
class SavingsAcct(InterrestRewardsAcct):
    def __init__(self,initialAmount,accName):
        super().__init__(initialAmount,accName)
        self.fee=5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print('\n withdraw completed')
            self.getbalance()
        except BalanceException as error:
            print(f'withdraw interrupted : { error}')
            
