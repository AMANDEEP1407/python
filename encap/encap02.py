# 🔒 Encapsulation in Python
# 🧠 Definition:

# Encapsulation is the process of bundling data (attributes) and methods (functions) that work on that data into a single unit — a class —
# and restricting direct access to some of that data.

# 👉 In short:
# Hide internal details, protect data, and control access.

# 🎯 Purpose of Encapsulation
# Goal	Meaning
# ✅ Data Protection	Prevent accidental modification of internal data
# ✅ Controlled Access	Provide safe “getter” and “setter” methods
# ✅ Data Hiding	Hide unnecessary details from external code
# ✅ Better Code Maintenance	Keeps your code modular and easy to debug
class detail:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,value):
        if value > 0:
            self.__salary=value

        else:
            print("give positive number!")

class employ(detail):
    def __init__(self, name,dep,salary):
        super().__init__(name,salary)
        self.dep=dep

    def Em(self):
        print(f"Name:{self.name}")
        print(f"Name:{self.dep}")
        print(f"Name:{self.get_salary()}")
e=employ("raman","cs",20000)
e.Em()
e.set_salary(1000)
print(e.get_salary())


# how to access private attributes from a subclass in Python.

# First — The Core Rule

# In Python, private attributes (with __) are not truly hidden.
# They’re name-mangled by the interpreter to make accidental access hard — not impossible.

# So a variable like:

# self.__amount


# is actually stored internally as:

# self._ClassName__amount


# That means if your class name is B, then:

# self.__amount  →  self._B__amount

# 1. Accessing Private Attribute in Subclass (Using Name Mangling)



# def show_private(self):
#         print(f"Accessing private from subclass: {self._B__amount}") 

# 2. using getter and setter