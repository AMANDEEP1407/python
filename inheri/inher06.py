class A:
    def __init__(self,**kwargs):
        pass
    
    def detail(self):
        print(f"Name:")

class B:
    def __init__(self,**kwargs):
        pass

    def detail(self):
       print(f"this is age:")

        
class D:
    def __init__(self):
        pass 


class C(B,A):
    def __init__(self):
        super().__init__()
                           # python firstly tried to find method and attribute in side current class then follow mro if need

    def detail(self):  # it ignore the method resolution order mro
        A.detail(self)
c=C()
c.detail()