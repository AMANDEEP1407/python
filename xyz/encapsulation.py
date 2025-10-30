class Car:
    def __init__(self,name,model):
        self.name=name
        self.__model=model
    
    def get_model(self):
        return f"{self.__model}"

    def detail(self):
        return f"name:{self.name} model:{self.__model}"

class Elecriccar(Car):
    def __init__(self, name, model,battarysize):
        super().__init__(name, model)

        self.battarysize=battarysize

    def full_detail(self):
        return f"name:{self.name} model:{self.model} battary:{self.battarysize}"
    
# car=Car("figo","2019")
# print(car.model)
# print(car.detail())
ecar=Elecriccar("fortuner","2020","40kwh")
print(ecar.name)
print(ecar.get_model())
# print(ecar.detail())
# print(ecar.full_detail())
