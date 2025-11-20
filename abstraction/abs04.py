from abc import ABC,abstractmethod

class Nofication:
    @abstractmethod
    def send(self):
        print("message send")

class EmailNotification(Nofication):
    def send(self,meg):
        print(f"Email meesage:{meg}")
class SMSNotification(Nofication):
    def send(self,meg):
        print(f"SMS meesage:{meg}")
class PushNotification(Nofication):
    def send(self,meg):
        print(f"Push meesage:{meg}")

def check(noti:Nofication,message):
    noti.send(message)

check(PushNotification(),"bill 200")
check(SMSNotification(),"new message")
check(EmailNotification(),"New Email")
