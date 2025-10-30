class Bird:
    def sound(self):
        print("chii")

class Dog(Bird):
    def sound(self):
        print("barking")

class parrot(Bird):
    def sound(self):
        print("hello")

B=Bird()
D=Dog()
P=parrot()
B.sound()
D.sound()
P.sound()