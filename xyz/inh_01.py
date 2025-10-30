class arths:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
            print(f'{self.a+self.b}')
        
class aths(arths):
     def __init__(self,c,d):
          
          self.c=c
          self.d=d
     def sub(self):
        print(f"{self.c-self.d}")

a2=aths(4,5)
a2.sub()
