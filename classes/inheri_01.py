class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def car_user(self):
        print(f'name is {self.model} and year is {self.year} company:{self.make}')
    def read_odometer(self):
        print(f'car km vaule:{self.odometer_reading}')

    def update_odo(self,milage):
        
        if milage >= self.odometer_reading:
            self.odometer_reading=milage

        else:
            print('you cannot roll back')

    def inc_odo(self,addkm):
        self.odometer_reading += addkm

    def fuel_tank(self):
        print("full")

class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size
    def des_battery(self):
        print(f"this car have {self.battery_size}")

        
class Ecar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()
    # def battery_des(self):
    #     print(f"this {self.model} has {self.battery} KW-hm ")
    def fuel_tank(self):
        print("Ecar do't need fuel")


c1=Ecar('tesla','s80','2018')

c1.battery.des_battery()

