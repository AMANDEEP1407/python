class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    def speak(self):
        print("bowwww..")

class Cat(Animal):
    def speak(self):
        print("meoww..")

class Cow(Animal):
    def speak(self):
        print("maaaaaa..")

def check(animal:Animal):
    animal.speak()

check(Cow())



