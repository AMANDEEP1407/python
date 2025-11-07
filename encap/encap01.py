class B:
    def __init__(self,age,roll,amount):
        self.age=age
        self._rollno=roll # protected attribute
        self.__amount=amount
    def myage(self): # its a getter method with this subclass can access data but attribute
        print(f"My age is {self.age}")

    
    def myamount(self):
         return self.__amount

class A(B):
    def __init__(self,name,age,roll,amount):
        super().__init__(age,roll,amount)
        self.__name=name
        self.age=age
        # print(f"__name:{self.__name}") // you can access directly attribute in that class
    
    def myname(self):
        print(f"I am protected : {self.__name}")
        print(f"I am protected in A: {self.age}")
        #print(f"I am private fromm B in A: {self.__amount}") --># you cannot access private attrubute directly in subclass for access of data of private attri. you can create a method in superclass and then in subclass you access data thrugh that method.
        print(f"I am private fromm B in A: {self.myamount()}")
 
    def Roll(self):
        print(f"this is rollno:{self._rollno}") # protected attribute can be share b/w superclass and subclass


a=A("aman","22",45,2000)
# b=B("22")

a.myname()    
a.Roll()
# print(a._rollno) // protected can be access directly from outside but not recommended
# b.myage()
# print(b.age)

# print(a.__name) // you cannot access this private attribute directly
#  you create a method first then you can easly access 