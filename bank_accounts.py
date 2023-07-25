class BankAccount:
    def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self,x):
        self.balance += x
    
    def withdraw(self,x):
        self.balance -= x

    def display_balance(self):
        print(self.balance)
        


bill_jackson = BankAccount("Bill","Jackson",500629,"Checking",1789,500.00)

bill_jackson.display_balance()

bill_jackson.deposit(96)

bill_jackson.display_balance()

bill_jackson.withdraw(25)

bill_jackson.display_balance()