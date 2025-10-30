l=[1,23,34]
l[0]=45
print(l)
# A=(1,2,3)
# A[0]=23
# print(A)

def dec(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@dec
def greet():
    print("hello")

greet( )


class Pcar:
    def __init__(self,Patrolcar):
        self.Patrolcar=Patrolcar

    def car1(self):
            

            return f"Partrolcar:{self.Patrolcar}"
        
class Ecar(Pcar):
    def __init__(self, Patrolcar,Electric):
        super().__init__(Patrolcar)

        self.Electric=Electric

    def car2(self):
            return f"Patrolcar:{self.Patrolcar} and Eletric:{self.Electric}"
        
ECAr=Ecar("g63","tesla")
print(ECAr.car2())

        

        



