class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model

    def detail(self):
        return f"name:{self.name} model:{self.model}"

class Elecriccar(Car):
    def __init__(self, name, model,battarysize):
        super().__init__(name, model)

        self.battarysize=battarysize

    def full_detail(self):
        return f"name:{self.name} model:{self.model} battary:{self.battarysize}"
    
car=Car("figo","2019")
# print(car.model)
print(car.detail())
ecar=Elecriccar("fortuner","2020","40kwh")
print(ecar.detail())
print(ecar.full_detail())