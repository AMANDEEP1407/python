from abc import ABC,abstractmethod

class  MessageSender:
    @abstractmethod
    def send(self,meg,to):
        print(f"Message To {meg}")
        print(f"Message: {meg}")

class WhatsAppSender(MessageSender):
    def send(self,meg,to):
        print(f"WhatsAppMessage To {to}")
        print(f"WhatsAppMessage: {meg}")
class TelegramSender(MessageSender):
    def send(self,meg,to):
        print(f"TelegramMessage To {to}")
        print(f"TelegramMessage: {meg}")
class SMSSender(MessageSender):
    def send(self,meg,to):
        print(f"SMSSenderMessage To {to}")
        print(f"SMSSenderMessage: {meg}")

def check(message:MessageSender,meg,to):
    message.send(meg,to)

check(TelegramSender(),"Hey Weli,how are you","Weli")
check(SMSSender(),"Hey Weli,how are you","Weli")
check(WhatsAppSender(),"Hey Weli,how are you","Weli")
