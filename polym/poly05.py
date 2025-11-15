class Empolyee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def detail(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")

    def bonus(self):
        return 0

class manager(Empolyee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def bonus(self):
        return self.salary* 0.20
    
class developer(Empolyee):
    def __init__(self, name, salary):
        super().__init__(name, salary)


    def bonus(self):
        return self.salary * 0.10
    
def check(empolyee:Empolyee):
    print(f"Name:{empolyee.name} Bonus :{empolyee.bonus()}")

d=developer("deepali",20000)
check(d)
m=manager("Deepanshu",22000)
check(m)