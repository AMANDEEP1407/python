# # method ovrriding
# It’s only needed when your class must initialize data (attributes) for each object.
class Car:
    def __init__(self):
        pass
    def start(self):
        print("starting Car")

    
class Pcar(Car):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def detail(self):
        print(f"Name of Petrol Car : {self.name}")
    def start(self):
        print("starting Patrol Car")


class Ecar(Car):
    def __init__(self):

     pass
    def start(self):
        print("starting Electric Car")


def checkIn(S):
    S.start()    


checkIn(Ecar())