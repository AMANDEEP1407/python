class Shape:
    def __init__(self,L,B,R):
        self.L=L
        self.B=B
        self.R=R
        
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,L,B,R):
        super().__init__(L,B,R)

    def area(self):
        return f"Rectangle:{self.L * self.B}"
class Circle(Shape):
    def __init__(self,L,B,R):
        super().__init__(L,B,R)

    def area(self):
        return f"Circle Area:{3.14 * self.R * self.R}"
    
def check(shape:Shape):
    print(shape.area())

r=Rectangle(3,4,5)
c=Circle(3,4,5)
check(r)
check(c)
