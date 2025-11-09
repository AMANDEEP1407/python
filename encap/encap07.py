class Employee:
    def __init__(self,salary,bonus):
        self.__salary=salary
        self.__bonus=bonus

    def total_salry(self):
        return self.__salary + self.__bonus
    
    def show_salary(self):
        print(self.total_salry())

e=Employee(20000,3000)
e.show_salary()