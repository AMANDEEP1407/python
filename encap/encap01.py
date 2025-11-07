class B:
    def __init__(self,age,roll):
        self.age=age
        self._rollno=roll # protected attribute
    def myage(self):
        print(f"My age is {self.age}")

    
    

class A(B):
    def __init__(self,name,age,roll):
        super().__init__(age,roll)
        self.__name=name
        self.age=age
        

    def myname(self):
        print(f"I am protected : {self.__name}")
        print(f"I am protected in A: {self.age}")
    def Roll(self):
        print(f"this is rollno:{self._rollno}") # protect attribute can be share b/w superclass and subclass


a=A("aman","22",45)
# b=B("22")

a.myname()    
a.Roll()
# b.myage()
# print(b.age)

# print(a.__name) // you cannot access this private attribute directly
#  you create a method first then you can easly access 