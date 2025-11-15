class Vehicle:
    def start(self):
        print("starting...vehicle")

class Car(Vehicle):
    def start(self):
        print("Starting Car...")

class Bike(Vehicle):
    def start(self):
        print("starting bike...")

def check(c):
    c.start()

check(Bike())
check(Car())
check(Vehicle())