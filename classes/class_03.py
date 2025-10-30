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

c1=Car('bmw','520i','2017')
c1.car_user()
c1.update_odo(20)
c1.read_odometer()    
c1.inc_odo(23)   
c1.read_odometer()    
    