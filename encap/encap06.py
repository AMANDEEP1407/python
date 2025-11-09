class Bank:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        print(f"Balance:{self.__balance}")

    def deposite(self,d):
        self.__balance=d

    def withdraw(self,w):
        self.__balance -= w

b=Bank(0)
b.deposite(1000)
b.withdraw(500)
b.get_balance()

