# Duck Typing (Dynamic Polymorphism — Python-Style) ## Due concept operator/method overload / 
# 🧠 Definition

# Python doesn’t care what type an object is —
# it only cares if the object behaves correctly (has the required method).

# “If it walks like a duck and quacks like a duck, it’s a duck.”
# How It Works

# There’s no inheritance here.

# There’s no base class.

# As long as the object has a .fly() method, it works.

# So Python decides at runtime whether an object has the required behavior —
# that’s dynamic (duck) polymorphism.
class Bird:
    def fly(self):
        print("Bird is flying")

class Egle:
   
    def fly(self):
        print("Egle is flying")

def check(s):
    s.fly()

check(Egle())

# Egle().fly()