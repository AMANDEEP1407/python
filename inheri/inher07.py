class A:    # findme can with this 
    def __init__(self,name):
        self.name=name
    
    def detail(self):
        print(f"Name:")
    def findme(self):
        print("find Me")

class B(A):
    def __init__(self):
        pass
        
    def detail(self):
       print(f"this is age:")

        

        


class C(B):
    def __init__(self):
        super().__init__()
                          
    def detail(self):  
        A.detail(self)
c=C()
# c.findme()