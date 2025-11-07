class company:
    def __init__(self,name,revenue,secret_code):
           self.name=name
           self._revenue=revenue
           self.__secret_code=secret_code


c=company("aman",2000,2323)
print(c.name)
print(c._revenue)
print(c._company__secret_code)
        