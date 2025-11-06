class Car:
    def __init__(self,brand,**kwargs):
        self.brand=brand

    def BName(self):
        print(f"Company name : {self.brand}")

class Ecar(Car):
    def __init__(self,name,brand):
        super().__init__(name=name,brand=brand)
        self.name=name

    def ename(self):
        print(f"this is {self.name}")

class Pcar(Car):
    def __init__(self,name,brand):
        super().__init__(name=name,brand=brand)
        self.name=name

    def pname(self):
        print(f"this is Patrol Car : {self.name}")


p=Pcar("Fortuner","Toyota")
p.pname()
p.BName()