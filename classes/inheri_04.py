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
    def __init__(self,battery_size=40,rangecar=30):
        self.battery_size = battery_size
        self.rangecar= rangecar
    def des_battery(self):
        print(f"this car have {self.battery_size}")
    def upgrade_battery(self):
        if self.battery_size <= 65:
            self.battery_size =65
            print(f"battery size is updated to {self.battery_size}")
        else:
            print(f"{self.battery_size} is perfect")

    def get_range(self):
        if self.battery_size >= 65:
            # 10km * 1kwh
           self.rangecar= self.battery_size * 10
           print(f"Car range is {self.rangecar}")
        elif  self.battery_size <= 65:
            # 10km * 1kwh
           self.rangecar= self.battery_size * 10
           print(f"Car range is {self.rangecar}")

        

        
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
c1.battery.get_range()
c1.battery.upgrade_battery()
c1.battery.get_range()

