# (Data Abstraction)

class Car:
    def __check_fuel(self):
            print("Fuel is ok")

    def __ignite(self):
          print("Ignite...")
    def start(self):
          self.__check_fuel()
          self.__ignite()
          print("Car Start")


c=Car()   
c.start()   

