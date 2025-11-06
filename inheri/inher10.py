class A:
    def __init__(self,name):
        self.name=name

    def Name(self):
        print(f"this is my name;{self.name}")

class B:
    def __init__(self,):
        pass
    def Age(self,e):
        print(f"This is My Age ; {e}")

class C:
    def __init__(self,rollno):
        self.rollno=rollno
        self.myB=B() # see here class B a attribute

    def Roll(self):
        print(f"This is RollNo:{self.rollno}")

c=C(22)       
c.Roll()   
c.myB.Age(33)  # pass a class as a Attribute