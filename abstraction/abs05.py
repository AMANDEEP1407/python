from abc import ABC,abstractmethod

class Database:
    @abstractmethod
    def connect(self):
        print("Database Connected")
    @abstractmethod
    def disconnect(self):
        print("Database Disconnected")

class Mysql(Database):
    def connect(self):
        print("Mysql Database Connected")
    def disconnect(self):
        print("Mysql Database Disconnected")


class PostgreSQL(Database):
    def connect(self):
        print("PostgreSQL Database Connected")
    def disconnect(self):
        print("PostgreSQL Database Disconnected")


class MongoDB(Database):
    def connect(self):
        print("MongoDB Database Connected")
    def disconnect(self):
        print("MongoDB Database Disconnected")

def checkConnect(data1:Database):
    data1.connect()
def checkDisconnect(data1:Database):
    data1.disconnect()

checkConnect(Mysql())
checkDisconnect(Mysql())
