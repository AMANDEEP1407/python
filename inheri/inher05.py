# “Nested Chain” — Car, Engine, Body
# MRO: Car → Engine → Body → object (Method Resolution Order)
class Engine:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Engine installed")

class Body:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Body assembled")

class Car(Body,Engine):
    def __init__(self):
        print("Start building car...")
        super().__init__()
        print("Car complete")

car1 = Car()
# Start building car...
# Engine installed
# Body assembled
# Car complete
# Why:
# Car.__init__() calls super() → enters Engine.__init__(). Engine prints, then calls super() → enters Body.__init__() which prints. So Engine’s print shows before Body’s print.

# Car.__init__()
#  ├ print("Start building car...")
#  └ super() → Engine.__init__()
#       ├ super() → Body.__init__()
#       │    ├ super() → object.__init__()
#       │    └ print("Body assembled")
#       └ print("Engine installed")
#  └ print("Car complete")

# Variant A — print before calling super()

# This prints the class’s message first, then calls the next class.

class Engine:
    def __init__(self):
        print("Engine installed")    # print BEFORE super
        super().__init__()

class Body:
    def __init__(self):
        print("Body assembled")      # print BEFORE super
        super().__init__()

class Car(Engine, Body):
    def __init__(self):
        print("Start building car...")
        super().__init__()          # goes to Engine -> Body
        print("Car complete")

Car()


# Output (Variant A):

# Start building car...
# Engine installed
# Body assembled
# Car complete


# Why:
# Car.__init__() calls super() → enters Engine.__init__(). Engine prints, then calls super() → enters Body.__init__() which prints. So Engine’s print shows before Body’s print.