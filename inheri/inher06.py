class A:
    def __init__(self,name):
        self.name=name
    
    def detail(self):
        print(f"Name:{self.detail}")

class B:
    def __init__(self,age):
        self.age=age

    def detail(self):
       print(f"this is age:{self.age}")

        
class D:
    def __init__(self):
        pass 


class C(A,B):
    def __init__(self):
        pass
c=C()
c.detail()