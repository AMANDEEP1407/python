from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        print("process..just")

class PhonePayment(Payment):
    def process(self):
        print("Payment Phonepe..")

class Creditcard(Payment):
    def process(self):
        print("Payment Credit Card...")

def Check(payment:Payment):
    payment.process()

Check(Creditcard())