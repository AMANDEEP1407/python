class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,d):
        if d>0:
            self.__balance+=d
        else:
            print("balance in Negative is not allowed")

    def withdraw(self,w):
        if w > 0:
            self.__balance -= w

        else:
            print("Invalid Input")

    def check_balance(self):
        print(f"Current Balance is {self.__balance}")
        

b=BankAccount(10000)
b.check_balance()  
b.deposit(230)     
b.check_balance()  
b.withdraw(100)
b.check_balance()  