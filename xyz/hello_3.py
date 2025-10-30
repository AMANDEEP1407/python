class detial:
    def __init__(self,name,age,salery):
        self.name=name
        self._age=age
        self.__salery=salery

d=detial("name",22,10000)
print(d.name)
print(d._age)
print(d.__salery)